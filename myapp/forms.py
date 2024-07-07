from django.shortcuts import render
from django import forms
from myapp.models import Order, Review, Book

class FeedbackForm(forms.Form):
    FEEDBACK_CHOICES = [
        ('B', 'Borrow'),
        ('P', 'Purchase'),
    ]
    feedback = forms.ChoiceField(choices=FEEDBACK_CHOICES)

class SearchForm(forms.Form):
    name = forms.CharField(label='Your Name', required=False)
    category = forms.ChoiceField(
        label='Select a category:',
        choices=[(category, category) for category in Book.objects.values_list('category', flat=True).distinct()],
        required=False,
        widget=forms.RadioSelect
    )
    max_price = forms.IntegerField(label='Maximum Price', min_value=0)

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['books', 'member', 'order_type']
        widgets = {
            'books': forms.CheckboxSelectMultiple(),
            'order_type': forms.RadioSelect
        }
        labels = {'member': 'Member name'}

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['reviewer', 'book', 'rating', 'comments']
        widgets = {
            'book': forms.RadioSelect()
        }
        labels = {
            'reviewer': 'Please enter a valid email',
            'rating': 'Rating: An integer between 1 (worst) and 5 (best)'
        }

def place_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.save()
            form.save_m2m()  # Save the many-to-many data for the form

            member = order.member
            order_type = order.order_type

            if order_type == 1:  # Assuming 1 represents borrowing
                for book in order.books.all():
                    member.borrowed_books.add(book)

            return render(request, 'myapp/order_response.html', {'order': order})
        else:
            return render(request, 'myapp/placeorder.html', {'form': form})
    else:
        form = OrderForm()
        return render(request, 'myapp/placeorder.html', {'form': form})

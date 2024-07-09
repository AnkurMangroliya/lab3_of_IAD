from django import forms
from myapp.models import Order, Review, Book

class FeedbackForm(forms.Form):
    FEEDBACK_CHOICES = [
        ('B', 'Borrow'),
        ('P', 'Purchase'),
    ]
    feedback = forms.MultipleChoiceField(choices=FEEDBACK_CHOICES)

class SearchForm(forms.Form):
    name = forms.CharField(label='Your Name', required=False)
    category = forms.ChoiceField(
        choices=[
            ('fiction', 'Fiction'),
            ('non-fiction', 'Non-Fiction'),
            ('science', 'Science'),
            ('math', 'Math'),
        ],
        widget=forms.RadioSelect,
        required=False,
        label='Select a category:'
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
        labels = {
            'member': u'Member name',
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['reviewer', 'book', 'rating', 'comments']
        widgets = {
            'book': forms.RadioSelect()
        }
        labels = {
            'reviewer': 'Please enter a valid email',
            'rating': 'Rating: An integer between 1 (worst) and 5 (best)',
        }

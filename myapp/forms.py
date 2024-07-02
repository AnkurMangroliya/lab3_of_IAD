from django import forms

class FeedbackForm(forms.Form):
    FEEDBACK_CHOICES = [
        ('B', 'Borrow'),
        ('P', 'Purchase'),
    ]
    feedback =   forms.ChoiceField(choices = FEEDBACK_CHOICES)

class SearchForm(forms.Form):
    name = forms.CharField(label='Your Name', required=False)
    CATEGORY_CHOICES = [
        ('S', 'Scinece&Tech'),
        ('F', 'Fiction'),
        ('B', 'Biography'),
        ('T', 'Travel'),
        ('O', 'Other')
    ]
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, label='Select a category:', required=False,
                                 widget=forms.RadioSelect)
    max_price = forms.IntegerField(label='Maximum Price', min_value=0)

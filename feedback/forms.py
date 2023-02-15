from django import forms

class FeedbackForm(forms.Form):
    name = forms.CharField(label='Имя',max_length=7, min_length=2, error_messages={
        'max_length': 'Слишком много символов',
        'min_length': 'Слишком мало символов',
        'required': 'Заполните поле'
    })

    surname= forms.CharField()
    feedback= forms.CharField(widget=forms.Textarea(attrs={'rows': 7, 'cols': 30}))
    rating = forms.IntegerField(label='Рейтинг',max_value=5, min_value=1)

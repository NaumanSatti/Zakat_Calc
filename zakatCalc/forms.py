from django import forms

Choices=(
    ('Value of gold', 'Value of gold'),
    ('value of silver', 'value of silver'),
)
class ZakatForm(forms.Form):
    cashinhand=forms.IntegerField(label='Cash in hand and in Bank Accounts')
    cashdep= forms.IntegerField(label='Cash deposited for some future purpose, e.g. Hajj')
    cashloans=forms.IntegerField(label='Cash given out in loans')
    investment=forms.IntegerField(label='Investments, shares, saving certificates, pensions funded by money in one’s possession')
    zakat=forms.ChoiceField(label='Zakat According to: ',choices = Choices)


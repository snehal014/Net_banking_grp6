from django import forms


# creating a form
class InputForm(forms.Form):  # form class must be inherited from 'Form' class
    # 'form' is a key to your class 'InputForm'


    Account_No= forms.IntegerField()
    First_Name= forms.CharField(max_length=200)
    Last_Name=forms.CharField(max_length=200)
    Address= forms.CharField(max_length=200)
    City=forms.CharField(max_length=200)
    State=forms.CharField(max_length=200)
    Phone_Number=forms.CharField(max_length=200)
    Email=forms.CharField(max_length=200)
    Customer_ID= forms.IntegerField()
    Ac_Opening_Date= forms.DateField()
    IFSC= forms.CharField(max_length=200)
    FD= forms.CharField(max_length=200)
    Balance= forms.IntegerField()

# class InputTransaction():
#     Account_No = forms.IntegerField()
#     Ammount = forms.IntegerField()

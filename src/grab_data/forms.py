from django import forms


class Access_Token(forms.Form):


    token               =forms.CharField(label="Access Token")
    types_of_data       =forms.CharField(label="Data Type",help_text="Example:posts.Make sure you write Data Types in lowercase")
    data_fields         =forms.CharField(label="Data Fields",help_text="Example:comments.Make sure you write Data Types in lowercase")
    number_of_data      =forms.CharField(label="Number of Data")

from django import forms
from .models import pythonPost

class PostModelForm(forms.ModelForm):
    class Meta:
        model = pythonPost
        #어떤 필드를 입력 받을지 서주기
        fields = ['title', 'body'] #필드가 많을 때는 __all__이라고 적으면
from django import forms
from .. import models

# ModelForm


class RegisterModelForm(forms.ModelForm):
    # 修改password的效果
    password = forms.CharField(label='密码',
                               widget=forms.PasswordInput())
    # 新增东西
    confirm_password = forms.CharField(label='重复密码',
                                       widget=forms.PasswordInput())

    class Meta:
        model = models.Userinfo
        fields = '__all__'
    # def __init__(self,*args,**kwargs):
    #     super().__init__(*args,**kwargs)
    #     for name,field in self.fields.items():
    #         field.widget.attr
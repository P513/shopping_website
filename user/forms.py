from django import forms
from .models import User


class SignUpForm(forms.Form):
    _id = forms.CharField(
        error_messages={'required': '아이디를 입력해주세요.'}, max_length=64, label='아이디',)
    nickname = forms.CharField(
        error_messages={'required': '닉네임을 입력해주세요.'}, max_length=64, label='닉네임',)
    email = forms.EmailField(
        error_messages={'required': '이메일을 입력해주세요.'}, label='이메일',)
    password = forms.CharField(
        error_messages={'required': '비밀번호를 입력해주세요.'}, max_length=64, widget=forms.PasswordInput, label='비밀번호',)
    confirm_password = forms.CharField(
        error_messages={'required': '비밀번호를 한번 더 입력해주세요.'}, widget=forms.PasswordInput, label='비밀번호 확인',)

    def clean(self):
        cleaned_data = super().clean()
        check = 1
        _id = cleaned_data.get('_id')
        if _id:
            if User.objects.filter(_id=_id).exists():
                self.add_error('_id', '존재하는 아이디입니다.')
                check = 0
        nickname = cleaned_data.get('nickname')
        if nickname:
            if User.objects.filter(nickname=nickname).exists():
                self.add_error('nickname', '존재하는 닉네임입니다.')
                check = 0
        email = cleaned_data.get('email')
        if email:
            if User.objects.filter(email=email).exists():
                self.add_error('email', '이미 가입된 이메일입니다.')
                check = 0
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password:
            if password != confirm_password:
                self.add_error('password', '비밀번호가 서로 다릅니다.')
                self.add_error('confirm_password', '비밀번호가 서로 다릅니다.')
            else:
                if check == 1:
                    user = User(
                        _id=_id,
                        nickname=nickname,
                        email=email,
                        password=password,
                    )
                    user.save()


class LoginForm(forms.Form):
    _id = forms.CharField(
        error_messages={'required': '아이디를 입력해주세요.'}, max_length=64, label='아이디',)
    password = forms.CharField(
        error_messages={'required': '비밀번호를 입력해주세요.'}, max_length=64, widget=forms.PasswordInput, label='비밀번호',)

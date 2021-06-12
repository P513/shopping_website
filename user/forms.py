from django import forms


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
        error_messages={'required': '비밀번호를 입력해주세요.'}, widget=forms.PasswordInput, label='비밀번호',)

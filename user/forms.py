from django import forms
from .models import User
from django.contrib.auth.hashers import check_password, make_password


class SignUpForm(forms.Form):
    userid = forms.CharField(
        error_messages={'required': '아이디를 입력해주세요.'}, max_length=64, label='아이디',)
    nickname = forms.CharField(
        error_messages={'required': '닉네임을 입력해주세요.'}, max_length=64, label='닉네임',)
    email = forms.EmailField(
        error_messages={'required': '이메일을 입력해주세요.'}, label='이메일',)
    password = forms.CharField(
        error_messages={'required': '비밀번호를 입력해주세요.'}, widget=forms.PasswordInput, label='비밀번호',)
    confirm_password = forms.CharField(
        error_messages={'required': '비밀번호를 한번 더 입력해주세요.'}, widget=forms.PasswordInput, label='비밀번호 확인',)

    def clean(self):
        if 'signup' in self.data:
            cleaned_data = super().clean()
            check = 1
            userid = cleaned_data.get('userid')
            if userid:
                if User.objects.filter(userid=userid).exists():
                    self.add_error('userid', '존재하는 아이디입니다.')
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
                            userid=userid,
                            nickname=nickname,
                            email=email,
                            password=make_password(password),
                            grade='user',
                        )
                        user.save()
        elif 'checkID' in self.data:
            cleaned_data = super().clean()
            userid = cleaned_data.get('userid')
            if userid:
                if User.objects.filter(userid=userid).exists():
                    self.add_error('userid', '존재하는 아이디입니다.')
        elif 'checkName' in self.data:
            cleaned_data = super().clean()
            nickname = cleaned_data.get('nickname')
            if nickname:
                if User.objects.filter(nickname=nickname).exists():
                    self.add_error('nickname', '존재하는 닉네임입니다.')
        elif 'checkMail' in self.data:
            cleaned_data = super().clean()
            email = cleaned_data.get('email')
            if email:
                if User.objects.filter(email=email).exists():
                    self.add_error('email', '존재하는 이메일입니다.')


class LoginForm(forms.Form):
    userid = forms.CharField(
        error_messages={'required': '아이디를 입력해주세요.'}, max_length=64, label='아이디',)
    password = forms.CharField(
        error_messages={'required': '비밀번호를 입력해주세요.'}, max_length=64, widget=forms.PasswordInput, label='비밀번호',)

    def clean(self):
        cleaned_data = super().clean()
        userid = cleaned_data.get('userid')
        password = cleaned_data.get('password')

        if userid and password:
            try:
                user = User.objects.get(userid=userid)
            except User.DoesNotExist:
                self.add_error('userid', '해당 아이디가 존재하지 않습니다.')
                return
            if not check_password(password, user.password):
                self.add_error('password', '비밀번호가 틀렸습니다.')
            else:
                self.userid = user.userid

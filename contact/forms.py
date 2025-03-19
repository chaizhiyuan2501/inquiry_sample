from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label="お名前", max_length=100)
    email = forms.EmailField(label="メールアドレス")
    subject = forms.CharField(label="件名", max_length=100)
    message = forms.CharField(label="メッセージ", widget=forms.Textarea)
    send_copy = forms.BooleanField(label="自分にも送信する", required=False)

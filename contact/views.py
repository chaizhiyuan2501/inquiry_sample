from django.shortcuts import render, redirect
from .forms import ContactForm
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
from django.core.mail import EmailMessage


# Create your views here.
def index(request):
    return render(request, "contact/index.html")


def contact_form(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]
            sender = form.cleaned_data["sender"]
            myself = form.cleaned_data["myself"]
            recipients = [settings.EMAIL_HOST_USER]
            if myself:
                recipients.append(sender)
            try:
                # send_mail(subject, message, sender, recipients)
                email = EmailMessage(
                    subject=subject,
                    body=message,
                    from_email=f"{sender}",  # 设置发件人邮箱
                    to=recipients,
                    headers={"Reply-To": sender},  # 可选：让收件人回复时发送到 `sender`
                )
                email.send()
            except BadHeaderError:
                return HttpResponse("無効なヘッダーが見つかりました。")
            return redirect("contact:complete")
    else:
        form = ContactForm()
    return render(request, "contact/contact_form.html", {"form": form})


def complete(request):
    return render(request, "contact/complete.html")

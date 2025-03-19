from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.conf import settings
from .forms import ContactForm


def contact_form(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]
            send_copy = form.cleaned_data["send_copy"]

            full_message = (
                f"お名前: {name}\nメールアドレス: {email}\n\nメッセージ:\n{message}"
            )
            recipients = [settings.EMAIL_HOST_USER]
            if send_copy:
                recipients.append(email)

            try:
                email_message = EmailMessage(
                    subject=subject,
                    body=full_message,
                    from_email=settings.EMAIL_HOST_USER,  # サーバーメールアドレス
                    to=recipients,
                    headers={"Reply-To": email},  # 返信先を送信者にする
                )
                email_message.send()
            except Exception as e:
                return HttpResponse(f"メール送信中にエラーが発生しました: {e}")

            return redirect("contact:complete")

    else:
        form = ContactForm()

    return render(request, "contact/contact_form.html", {"form": form})


def complete(request):
    return render(request, "contact/complete.html")

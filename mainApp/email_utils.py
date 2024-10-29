from django.core.mail import get_connection, EmailMultiAlternatives
from django.core.cache import cache
from django.conf import settings

def get_next_email_account():
    current_index = cache.get("current_email_index", 0)
    next_index = (current_index + 1) % len(settings.EMAIL_ACCOUNTS)
    cache.set("current_email_index", next_index)
    return settings.EMAIL_ACCOUNTS[next_index]

def send_rotating_email(subject, body, recipient, html_content=None):
    email_account = get_next_email_account()
    
    # Create a custom connection with rotating email credentials
    connection = get_connection(
        backend=settings.EMAIL_BACKEND,
        host=settings.EMAIL_HOST,
        port=settings.EMAIL_PORT,
        username=email_account["EMAIL_HOST_USER"],
        password=email_account["EMAIL_HOST_PASSWORD"],
        use_tls=settings.EMAIL_USE_TLS
    )

    email = EmailMultiAlternatives(
        subject=subject,
        body=body,
        from_email=email_account["EMAIL_HOST_USER"],
        to=[recipient],
        connection=connection  # Use custom connection
    )
    
    if html_content:
        email.attach_alternative(html_content, "text/html")
    
    email.send()

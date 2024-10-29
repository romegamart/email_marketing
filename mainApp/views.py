import pandas as pd
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from .models import Customer
from django.conf import settings
from django.http import HttpResponse

# def send_bulk_emails(request):
#     if request.method == 'POST':
#         excel_file = request.FILES['excel_file']
#         subject = request.POST.get('subject')
#         message_template = request.POST.get('message')  # corrected POST method
        
#         # Load the Excel file
#         try:
#             df = pd.read_excel(excel_file)
#         except Exception as e:
#             return render(request, 'send_email.html', {'error': 'Invalid file format'})

#         # Iterate through rows and send emails
#         for index, row in df.iterrows():
#             name = row.get('name')
#             email = row.get('email')
            
#             # Save customer data if needed
#             customer_data = Customer(email=email, name=name)
#             customer_data.save()
            
#             # Customize HTML message with dynamic values
#             html_content = render_to_string('email-template.html', {
#                 'title': subject,
#                 'name': name,
#                 'message': message_template
#             })
            
#             # Create an email with HTML content
#             email_message = EmailMultiAlternatives(
#                 subject=subject,
#                 body=message_template,  # fallback text in case HTML is not supported
#                 from_email=settings.DEFAULT_FROM_EMAIL,
#                 to=[email],
#             )
#             email_message.attach_alternative(html_content, "text/html")
#             email_message.send(fail_silently=False)

#         return HttpResponse("Emails sent successfully!", status=200)

#     return render(request, 'send_email.html')



#For Multiple Switching Email Account....
from .email_utils import send_rotating_email

def send_bulk_emails(request):
    if request.method == 'POST':
        excel_file = request.FILES['excel_file']
        subject = request.POST.get('subject')
        message_template = request.POST.get('message')
        
        try:
            df = pd.read_excel(excel_file)
        except Exception as e:
            return render(request, 'send_email.html', {'error': 'Invalid file format'})

        for index, row in df.iterrows():
            name = row.get('name')
            email = row.get('email')
            
            customer_data = Customer(email=email, name=name)
            customer_data.save()
            
            html_content = render_to_string('email-template.html', {
                'title': subject,
                'name': name,
                'message': message_template
            })

            send_rotating_email(subject, message_template, email, html_content)

        return HttpResponse("Emails sent successfully!", status=200)

    return render(request, 'send_email.html')

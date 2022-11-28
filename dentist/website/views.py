from unicodedata import name
from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    if request.method == "POST" :
        your_name = request.POST['your-name']
        your_phone = request.POST['your-phone']
        your_email = request.POST['your-email']
        your_message = request.POST['message']
        #send an email
        send_mail(
            'Mr/Ms ' + your_name + ' Kontakt form',
            'Message from Mr/Ms : ' + your_name + '\nEmail : ' + your_email + '\nPhone : ' + your_phone + '\nMessage : ' +  your_message,
            'your_email',
            ['status.electronics.test.mail@gmail.com'],
            fail_silently=False,
        )
        return render(request, 'pages/index.html', {'your_name': your_name})
    else:
        return render(request, 'pages/index.html', {})

def about(request):
    return render(request, 'pages/about.html', {})


def service(request):
    return render(request, 'pages/service.html', {})


def pricing(request):
    return render(request, 'pages/pricing.html', {})


def contact(request):
    if request.method == "POST" :
        message_name = request.POST['message-name']
        message_surname = request.POST['message-surname']
        message_phone = request.POST['message-phone']
        message_email = request.POST['message-email']
        message = request.POST['message']
        #send an email
        send_mail(
            'Mr/Ms ' + message_name + ' Kontakt form',
            'Message from Mr/Ms : ' + message_name + ' ' + message_surname + '\nEmail : ' + message_email + '\nPhone Number : ' + message_phone + '\nMessage : ' +  message,
            'message_email',
            ['status.electronics.test.mail@gmail.com'],
            fail_silently=False,
        )

        return render(request, 'pages/contact.html', {'message_name': message_name})
    else:
        return render(request, 'pages/contact.html', {})


def blog(request):
    return render(request, 'pages/blog.html', {})


def blog_details(request):
    return render(request, 'pages/blog-details.html', {})

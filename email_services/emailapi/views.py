from django.conf import settings
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def send_email(request):
    if request.method == 'POST':
        try:

            data = json.loads(request.body)
            receiver_email = data.get('receiver_email')
            subject = data.get('subject')
            body_text = data.get('body_text')


            if not receiver_email or not subject or not body_text:
                return JsonResponse({'error': 'All fields (receiver_email, subject, body_text) are required.'}, status=400)


            send_mail(
                subject,
                body_text,
                settings.EMAIL_HOST_USER,             [receiver_email],
                fail_silently=False,
            )


            return JsonResponse({'message': 'Email sent successfully'}, status=200)

        except Exception as e:

            return JsonResponse({'error': str(e)}, status=500)


    return JsonResponse({'error': 'Invalid HTTP method. Only POST is allowed.'}, status=405)

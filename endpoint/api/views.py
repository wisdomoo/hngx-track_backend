from django.shortcuts import render

from django.http import JsonResponse
from django.utils import timezone
from api.models import Info

def get_info(request):
    slack_name = request.GET.get('slack_name')
    track = request.GET.get('track')

    current_day = timezone.now().strftime('%A')

    info = Info(slack_name=slack_name, track=track)
    info.save()

    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": timezone.now().strftime('%Y-%m-%dT%H:%M:%SZ'),
        "track": track,
        "github_file_url": "https://github.com/wisdomoo/hngx-track_backend/blob/master/endpoint/api/views.py",
        "github_repo_url": "https://github.com/wisdomoo/hngx-track_backend",
        "status_code": 200
    }

    return JsonResponse(response_data)


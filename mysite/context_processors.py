from .models import StaticContent
def add_recs_status_to_context(request):
    if StaticContent.objects.count():
        static_content = StaticContent.objects.first()
        return {
            'recruiting': static_content.recs_form
        }
    else:
        return {}
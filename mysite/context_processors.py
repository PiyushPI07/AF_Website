from .models import StaticContent
def add_recs_status_to_context(request):
    static_content = StaticContent.objects.get(id=1)
    return {
        'recruiting': static_content.recs_form
    }
from django.views import generic
from .models import Post


class IndexView(generic.ListView):
    model = Post

    def get_queryset(self):
        """Sort the articles so that the most recent article is at the top."""

        return Post.objects.order_by('-created_at')

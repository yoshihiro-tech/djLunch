from .models import Category


def common(request):
    """テンプレートに渡すデータ"""
    context = {
        'category_list': Category.objects.all()
    }
    return context

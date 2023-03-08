from home.models import Featured, Post


def get_featured_posts():
    featured_posts = []
    queryset = Featured.objects.order_by('-created_at')[:2]
    for item in queryset:
        split = item.link.split('/')
        slug = split[-1]
        if Post.objects.filter(slug=slug).exists():
            featured_posts.append(Post.objects.get(slug=slug))
    return featured_posts

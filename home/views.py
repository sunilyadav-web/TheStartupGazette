from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse
from django.views.generic import TemplateView, DetailView, CreateView

from home.models import *
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.messages.views import SuccessMessageMixin

from home.selector import get_featured_posts


class HomeView(TemplateView):
    template_name = "home/home.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        posts = Post.objects.filter(status=StatusEnum.PUBLISH).order_by('-publish_date')
        ctx['posts'] = posts[:10]
        ctx['last_post'] = posts.latest('publish_date')

        ctx['startup_stories'] = posts.filter(tag=Tag.objects.get(name='startup stories'))[:6]
        ctx['featured_posts'] = get_featured_posts()
        ctx['sliders'] = Slider.objects.all()
        return ctx


def error(request):
    return HttpResponse('Hello error')


class PostDetailView(DetailView):
    model = Post
    template_name = "home/post_detail.html"


class CategoryFilterView(TemplateView):
    template_name = "home/category_filter.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        category_object = get_object_or_404(Category, name=kwargs.get('name', None))
        ctx['posts'] = Post.objects.filter(category=category_object, status=StatusEnum.PUBLISH)
        ctx['category'] = category_object
        return ctx


class TagFilterView(TemplateView):
    template_name = "home/tag_filter.html"

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.tag_object = get_object_or_404(Tag, name=kwargs.get('name', None))

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['posts'] = Post.objects.filter(tag=self.tag_object, status=StatusEnum.PUBLISH)
        ctx['tag'] = self.tag_object
        return ctx


class ContactView(SuccessMessageMixin, CreateView):
    template_name = 'home/contact.html'
    model = Contact
    fields = '__all__'
    success_message = 'Thank you for getting in touch, we will respond to you very soon!'

    def get_success_url(self):
        return reverse("home:contact")


class AboutUsView(TemplateView):
    template_name = "home/about_us.html"


def search(request):
    context = {}
    try:
        query = request.GET.get('q', None)
        if query:
            context['query'] = query

            if len(query) > 78:
                messages.warning(request, 'Query length cannot be greater than 77 characters')
                context['posts'] = Post.objects.none()
            else:
                queryset = Post.objects.filter(
                    Q(title__icontains=query) | Q(content__icontains=query), status=StatusEnum.PUBLISH
                ).order_by('-publish_date')

                paginator = Paginator(queryset, 5)
                pager_number = request.GET.get('page')
                page = paginator.get_page(pager_number)
                page_range = paginator.page_range
                context['posts'] = page
                context['page_range'] = page_range
                context['querysetLength'] = queryset.count()
                if queryset.count() < 1:
                    messages.warning(request, f"Query not found <strong>{query}</strong>")
        else:
            messages.warning(request, 'Query cannot be empty please define something.')
            context['posts'] = Post.objects.none()
    except Exception as e:
        print('Search Exception : ', e)
        messages.warning(request, 'Something went wrong!')
    return render(request, 'home/search.html', context)


class TermAndConditionView(TemplateView):
    template_name = "home/term_condition.html"


class PrivacyPolicyView(TemplateView):
    template_name = "home/privacy_policy.html"


# ========SEO Robots.txt File=======
def robot(request):
    return render(request, 'home/robots.txt')
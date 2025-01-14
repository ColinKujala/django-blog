from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.views.generic import ListView, DetailView

from blogging.models import Post


def stub_view(request, *args, **kwargs):
    body = "Stub View\n\n"
    if args:
        body += "Args:\n"
        body += "\n".join(["\t%s" % a for a in args])
    if kwargs:
        body += "Kwargs:\n"
        body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
    return HttpResponse(body, content_type="text/plain")

"""
Replacing function views with class-based views

def list_view(request):
    published = Post.objects.exclude(published_date__exact=None)
    posts = published.order_by('-published_date')
    context = {'posts': posts}
    return render(request, 'blogging/list.html', context)
"""
class BlogListView(ListView):
    """Blog list view"""
    queryset = Post.objects.exclude(
        published_date__exact=None
    ).order_by('-published_date')
    template_name = 'blogging/list.html'


"""
Replacing function views with class-based views

def detail_view(request, post_id):
    published = Post.objects.exclude(published_date__exact=None)
    try:
        post = published.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404
    context = {'post': post}
    return render(request, 'blogging/detail.html', context)
"""
class BlogDetailView(DetailView):
    """Blog detail view"""
    queryset = Post.objects.exclude(published_date__exact=None)
    template_name = 'blogging/detail.html'


"""
Note to self

Job of views is to build a context and then render a template.
There is a shortcut from django to more easily render a template.
instead of getting a template with 
django.template.loader.get_template('some template.html')
and then making a body with that template.render(context),
can instead just bring in the django.shortcuts.render and do
render(request, 'some template.html', context)
"""
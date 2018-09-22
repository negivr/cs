from django.shortcuts import render


posts = [
    {
        'author': 'Negovan Veljkovic',
        'title': 'Blog 1',
        'content': 'First blog content',
        'date_posted': 'August 27, 2018'
    },
{
        'author': 'Jane Doe',
        'title': 'Blog 2',
        'content': 'Second blog content',
        'date_posted': 'August 28, 2018'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')






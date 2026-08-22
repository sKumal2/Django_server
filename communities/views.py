from django.shortcuts import render

# Create your views here.
def communities(request):
    return render(request, 'communities/index.html')


def community_detail(request, slug):
    hardcoded_posts = {
        'javascript': [
            {
                'title': 'What JavaScript feature changed the way you code?',
                'author': 'scriptwizard',
                'time': '2h ago',
                'body': 'Optional chaining and nullish coalescing made my frontend code cleaner and safer.',
                'upvotes': '3.9k',
                'comments': 412,
            },
            {
                'title': 'Built a tiny state manager in 60 lines',
                'author': 'frontendfox',
                'time': '5h ago',
                'body': 'I made a lightweight store for side projects and it feels surprisingly fast.',
                'upvotes': '1.7k',
                'comments': 128,
            },
            {
                'title': 'Async/await debugging tips that save hours',
                'author': 'asyncnomad',
                'time': '9h ago',
                'body': 'Use structured logging around await boundaries to track race conditions quickly.',
                'upvotes': '980',
                'comments': 74,
            },
        ]
    }

    context = {
        'slug': slug,
        'community_name': f"r/{slug}",
        'posts': hardcoded_posts.get(slug, []),
    }
    return render(request, 'communities/detail.html', context)



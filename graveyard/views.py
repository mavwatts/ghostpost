from django.shortcuts import render, HttpResponseRedirect, reverse
from graveyard import models
from graveyard.forms import PostForm

# Create your views here.
def index_view(request):
    ghostposts = models.BoastRoast.objects.all().order_by('-timeposted')
    return render(request, 'index.html', {'welcome': "Ghosts: Roasts and Boasts", 'ghostpost': ghostposts})

def boast_view(request):
    boast = models.BoastRoast.objects.all().order_by('-timeposted')
    return render(
        request, 'boasts.html', {'headline': 'All Boast Ghostposts!', 'boast': boast}
        )

def roast_view(request):
    roast = models.BoastRoast.objects.all().order_by('-timeposted')
    return render(
        request, 'roasts.html', {'headline': 'All Roast Ghostposts!', 'roast': roast}
        )

def create_post_view(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            models.BoastRoast.objects.create(
                choices=data.get('choices'),
                user_input=data.get('user_input')
            )
            return HttpResponseRedirect(reverse('homepage'))

    form = PostForm()
    return render(request, 'generic_form.html', {'form': form})

def upvote_view(request, upvote_id):
    post = models.BoastRoast.objects.filter(id=upvote_id).first()
    post.upvotes += 1
    post.save()
    return HttpResponseRedirect('/')

def downvote_view(request, downvote_id):
    post = models.BoastRoast.objects.filter(id=downvote_id).first()
    post.downvotes += 1
    post.save()
    return HttpResponseRedirect('/')

def sorted_votes(request):
    sort_by_votes = sorted(models.BoastRoast.objects.all(), key=lambda x: x.totalvotes, reverse=True)
    return render(request, "sortbyvotes.html", {'sort_by_votes':sort_by_votes})

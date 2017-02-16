from __future__ import print_function

from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Grabber
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .forms import PostForm
from django.utils import timezone
import random
from itertools import chain

# Create your views here.

def grabber_two(request,pkt=0):

    if pkt != 0:
        grabber = Grabber.objects.get(pk=pkt)
        grabber.addVote()
    randomA = random.randint(1, 102)
    randomB = random.randint(1, 102)
    while(randomA == randomB):
        randomB = random.randint(1, 28)

    postsA = Grabber.objects.all().filter(pk=randomA)
    postsB = Grabber.objects.all().filter(pk=randomB)

    posts = list(chain(postsA,postsB))
    return render(request, 'polls/poll_list.html', {'posts': posts})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def dope(request,pk):
    grabber = Grabber.objects.get(pk=pk)
    grabber.addVote()
    return redirect(grabber_two())
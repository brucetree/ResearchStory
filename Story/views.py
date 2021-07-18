from django.shortcuts import render
from .models import Story
from .storyform import StoryForm
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

def upload(request):
    if request.method=="GET":
        form=StoryForm()
    elif request.method=="POST":
        form=StoryForm(data=request.POST)
        if form.is_valid():
            story=Story()
            story.title_name=request.POST.get('title')
            story.category=request.POST.get('category')
            story.text=request.POST.get('text')
            story.video=request.POST.get('videoUrl')
            story.paper_link=request.POST.get('paperLink')
            story.save()
            #form.save()
            return HttpResponseRedirect(reverse("Story:storyList"))

    return render(request,'upload.html',locals())




def storyList(request):
    story = Story.objects.filter()
    return render(request, 'story.html', locals())


def storyListCategory(request, category):
    story = Story.objects.filter(category=category)
    return render(request, 'story.html', locals())


def getStory(request, story_id):
    story = Story.objects.get(id=story_id)
    title_name = story.title_name
    created_time = story.created_time
    category = story.category
    views = story.views
    text = story.text
    video = story.video
    paper_link = story.paper_link
    try:
        video = f"https://www.youtube.com/embed/{video.split('/')[-1]}"
    except AttributeError:
        pass
    kwarg = {
        "title_name": title_name,
        "created_time": created_time,
        "category": category,
        "views": views,
        "text": text,
        "video": video,
        "paper_link": paper_link
    }

    story.viewed()

    return render(request, 'storyPage.html', kwarg)




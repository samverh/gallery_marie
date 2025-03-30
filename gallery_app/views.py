from django.shortcuts import render
# from django.conf import settings
from .models import Image
import cloudinary.api

import os

def index(request):

    
    # files = os.listdir(os.path.join(settings.STATIC_ROOT, "images/under_your_feet"))
    # files = ["images/under_your_feet/" + file for file in files]
    # files = Image.objects.all()
    # images = Image.objects.all()

    images = cloudinary.api.resources(type="upload", prefix="gallerymarie", resource_type="image")
    image_urls = [img["secure_url"] for img in images["resources"]]

    context = {
            "images": image_urls
        }

    return render(request, "index.html", context)


def under_your_feet(request):

    # get images from cloudinary storage
    images = cloudinary.api.resources(
                                type="upload", 
                                prefix="gallerymarie", 
                                resource_type="image",
                                max_results=500) 
    
    image_urls = [img["secure_url"] for img in images["resources"]]

    context = {
            "images":  image_urls
        }

    return render(request, "under_your_feet.html", context)


def seen_to_be_seen(request):

    # pass the list of image files to the template
    files = Image.objects.filter(set="seen_to_be_seen")
    context = {
        'image_files': files,
        'title': 'Seen To Be Seen'
    }
    print(files)

    return render(request, "seen_to_be_seen.html", context)


def state_of_decay(request):

    # pass the list of image files to the template
    files_bar = Image.objects.filter(set="state_of_decay-bar")
    files_bioscoop = Image.objects.filter(set="state_of_decay-bioscoop")
    context = {
        'image_files_bar': files_bar,
        'image_files_bioscoop': files_bioscoop,
        'title': 'State Of Decay'
    }

    return render(request, "state_of_decay.html", context)


def sculptures(request):

    # pass the list of image files to the template
    files = Image.objects.filter(set="sculptures")
    context = {
        'image_files': files,
        'title': 'Sculptures'
    }

    return render(request, "sculptures.html", context)


def posters(request):

    # pass the list of image files to the template
    files = Image.objects.filter(set="posters")
    context = {
        'image_files': files,
        'title': 'Posters'
    }

    return render(request, "posters.html", context)


def contact(request):
    context = {
        'title': "Contact"
    }

    return render(request, "contact.html", context)


def collages(request):

    # pass the list of image files to the template
    files = Image.objects.filter(set="collages")
    context = {
        'image_files': files,
        'title': 'Collages'
    }

    return render(request, "collages.html", context)
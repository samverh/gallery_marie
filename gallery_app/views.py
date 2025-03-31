from django.shortcuts import render
# from django.conf import settings
from .models import Image
import cloudinary.api
from cloudinary.api import resources_by_tag
import os


def index(request):

    # fetch image details by public_id
    image_data = cloudinary.api.resource("marie")

    # get the URL of the image
    marie_image = image_data["secure_url"]

    current_work_folders = {"hoofden": "hoofden", 
                            "state_of_decay-bar": "state_of_decay", 
                            "state_of_decay-bioscoop": "state_of_decay", 
                            "under_your_feet": "under_your_feet", 
                            "gallerymarie": "under_your_feet", 
                            "project pop/pop fashion": "poppen"}
    current_work_images = []

    for folder in current_work_folders.keys():

        # fetch all images in the folder
        response = cloudinary.api.resources(type="upload", prefix=folder + "/")

        # filter images where public_id ends with 'main'
        for resource in response.get("resources", []):
            if resource["public_id"].endswith("main"):  # exact match for 'main'
                data = {}
                data["title"] = folder.split("-")[0]
                data["url"] = resource["secure_url"]
                data["link"] = current_work_folders[folder]
                current_work_images.append(data)  # get image URL
    # print(current_work_images)

    context = {
            "marie":  marie_image,
            "current_work_images": current_work_images
        }

    return render(request, "index.html", context)


def under_your_feet(request):

    # get images from cloudinary storage
    images = cloudinary.api.resources(
                                type="upload", 
                                prefix="under_your_feet", 
                                resource_type="image",
                                max_results=500) 
    
    image_urls = [img["secure_url"] for img in images["resources"]]

    # # fetch media from a specific folder
    # response = resources_by_tag("under_your_feet")
    # media_list = response["resources"]

    # # sort by public_id (adjust key as needed)
    # sorted_media = sorted(media_list, key=lambda x: x["public_id"])
    # print(sorted_media)

    context = {
            "images":  image_urls
        }

    return render(request, "under_your_feet.html", context)


def seen_to_be_seen(request):

    # get images from cloudinary storage
    images = cloudinary.api.resources(
                                type="upload", 
                                prefix="seen_to_be_seen", 
                                resource_type="image",
                                max_results=500) 
    
    image_urls = [img["secure_url"] for img in images["resources"]]

    context = {
            "images":  image_urls
        }
    return render(request, "seen_to_be_seen.html", context)


def hoofden(request):

    # get images from cloudinary storage
    images = cloudinary.api.resources(
                                type="upload", 
                                prefix="hoofden", 
                                resource_type="image",
                                max_results=500) 
    
    image_urls = [img["secure_url"] for img in images["resources"]]

    context = {
            "images":  image_urls
        }
    return render(request, "hoofden.html", context)


def poppen(request):

    # get images from cloudinary storage
    images = cloudinary.api.resources(
                                type="upload", 
                                prefix="poppen", 
                                resource_type="image",
                                max_results=500) 
    
    image_urls = [img["secure_url"] for img in images["resources"]]

    context = {
            "images":  image_urls
        }

    return render(request, "poppen.html", context)


def state_of_decay(request):

    # get images from cloudinary storage
    images_bar = cloudinary.api.resources(
                                type="upload", 
                                prefix="state_of_decay-bar", 
                                resource_type="image",
                                max_results=500) 
    image_bar_urls = [img["secure_url"] for img in images_bar["resources"]]

    # get images from cloudinary storage
    images_bioscoop = cloudinary.api.resources(
                                type="upload", 
                                prefix="state_of_decay-bioscoop", 
                                resource_type="image",
                                max_results=500) 
    image_bioscoop_urls = [img["secure_url"] for img in images_bioscoop["resources"]]
    context = {
            "title": "State of decay",
            "image_files_bar":  image_bar_urls,
            "image_files_bioscoop":  image_bioscoop_urls
        }

    return render(request, "state_of_decay.html", context)


def sculptures(request):

    # get images from cloudinary storage
    images = cloudinary.api.resources(
                                type="upload", 
                                prefix="sculptures", 
                                resource_type="image",
                                max_results=500) 
    
    image_urls = [img["secure_url"] for img in images["resources"]]

    context = {
        "title": "Sculptures",
        "images":  image_urls
    }
    return render(request, "sculptures.html", context)


def posters(request):

    # get images from cloudinary storage
    images = cloudinary.api.resources(
                                type="upload", 
                                prefix="posters", 
                                resource_type="image",
                                max_results=500) 
    
    image_urls = [img["secure_url"] for img in images["resources"]]

    context = {
        "title": "Posters",
        "images":  image_urls
    }

    return render(request, "posters.html", context)


def dimensions(request):

    # get images from cloudinary storage
    images = cloudinary.api.resources(
                                type="upload", 
                                prefix="2d_into_3d", 
                                resource_type="image",
                                max_results=500) 
    
    image_urls = [img["secure_url"] for img in images["resources"]]

    context = {
        "title": "2D into 3D",
        "images":  image_urls
    }

    return render(request, "posters.html", context)


def drawings(request):

    # get images from cloudinary storage
    images = cloudinary.api.resources(
                                type="upload", 
                                prefix="drawings", 
                                resource_type="image",
                                max_results=500) 
    
    image_urls = [img["secure_url"] for img in images["resources"]]

    context = {
        "title": "Paper drawings",
        "images":  image_urls
    }

    return render(request, "drawings.html", context)



def crab(request):

    # pass the list of image files to the template
    files = Image.objects.filter(set="crab")
    context = {
        'image_files': files,
        'title': 'crab'
    }

    return render(request, "crab.html", context)


def posters(request):

    # get images from cloudinary storage
    images = cloudinary.api.resources(
                                type="upload", 
                                prefix="posters", 
                                resource_type="image",
                                max_results=500) 
    
    image_urls = [img["secure_url"] for img in images["resources"]]

    context = {
            "images":  image_urls
        }

    return render(request, "posters.html", context)



def collages(request):

    # get images from cloudinary storage
    images = cloudinary.api.resources(
                                type="upload", 
                                prefix="collages", 
                                resource_type="image",
                                max_results=500) 
    
    image_urls = [img["secure_url"] for img in images["resources"]]

    context = {
            "images":  image_urls
        }

    return render(request, "collages.html", context)
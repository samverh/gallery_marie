from django.shortcuts import render
# from django.conf import settings
from .models import Image
import cloudinary.api
from cloudinary.api import resources_by_tag
import os


NAVIGATION_ROUTES = [
    "drawings",
    "collages",
    "posters",
    "poppen",
    "sculptures",
    "under_your_feet",
    "state_of_decay",
    "2d_into_3d",
    "seen_to_be_seen",
    "crab"
]


def get_navigation_links(current_route):
    index = NAVIGATION_ROUTES.index(current_route)
    
    left_nav = NAVIGATION_ROUTES[index - 1] if index > 0 else None
    right_nav = NAVIGATION_ROUTES[index + 1] if index < len(NAVIGATION_ROUTES) - 1 else None
    
    return left_nav, right_nav


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
                            "current_work": "under_your_feet",
                            "project pop/pop fashion": "poppen"}
    current_work_images = []

    for folder in current_work_folders.keys():

        # fetch all images in the folder
        response = cloudinary.api.resources(type="upload", prefix=folder + "/")

        # filter images where public_id ends with 'main'
        for resource in response.get("resources", []):
            if resource["public_id"].endswith("main") or folder == "current_work":  # exact match for 'main'
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

    # get navigation
    left_nav, right_nav = get_navigation_links("under_your_feet")

    context = {
        "left_nav": left_nav,
        "right_nav": right_nav,
        "images":  image_urls
    }

    return render(request, "under_your_feet.html", context)


def seen_to_be_seen(request):

    # get images from cloudinary storage
    # images = cloudinary.api.resources(
    #                             type="upload", 
    #                             prefix="seen_to_be_seen", 
    #                             resource_type="media",
    #                             max_results=500) 
    # if images:
    #     image_urls = [img["secure_url"] for img in images["resources"]]
    # else:
    image_urls = []

    # get navigation
    left_nav, right_nav = get_navigation_links("seen_to_be_seen")

    context = {
        "left_nav": left_nav,
        "right_nav": right_nav,
        "title": "Seen to be Seen",
        "images":  image_urls
    }
    return render(request, "image_columns.html", context)


def hoofden(request):

    # get images from cloudinary storage
    images = cloudinary.api.resources(
                                type="upload", 
                                prefix="hoofden", 
                                resource_type="image",
                                max_results=500) 
    
    image_urls = [img["secure_url"] for img in images["resources"]]

    # get navigation
    left_nav, right_nav = get_navigation_links("hoofden")

    context = {
        "left_nav": left_nav,
        "right_nav": right_nav,
        "title": "",
        "images":  image_urls
    }
    return render(request, "hoofden.html", context)


def poppen(request):

    # get images from cloudinary storage
    images = cloudinary.api.resources(
                                type="upload", 
                                prefix="project pop", 
                                resource_type="image",
                                max_results=500) 
    
    image_urls = [img["secure_url"] for img in images["resources"] if "pop/pop/" in img["public_id"]]

    # get navigation
    left_nav, right_nav = get_navigation_links("poppen")

    context = {
        "left_nav": left_nav,
        "right_nav": right_nav,
            "title": "Poppen / dolls",
            "right_nav": "sculptures",
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
    image_bar_urls = [img["secure_url"] for img in images_bar["resources"] if not "kiaqrwt6jdikv5jcqeme" in str(img) and not "main" in str(img)]

    # get images from cloudinary storage
    images_bioscoop = cloudinary.api.resources(
                                type="upload", 
                                prefix="state_of_decay-bioscoop", 
                                resource_type="image",
                                max_results=500) 
    image_bioscoop_urls = [img["secure_url"] for img in images_bioscoop["resources"] if not "zyltm1y5mmrjpmix2fri" in str(img)]

    kriterion_image = cloudinary.api.resource(type="upload", 
                                public_id="state_of_decay-bar/kiaqrwt6jdikv5jcqeme", 
                                resource_type="image")
    kriterion_image = kriterion_image["secure_url"]

    main_image = cloudinary.api.resource(type="upload", 
                                public_id="state_of_decay-bar/main", 
                                resource_type="image")
    main_image = main_image["secure_url"]

    poster_image = cloudinary.api.resource(type="upload", 
                                public_id="state_of_decay-bioscoop/zyltm1y5mmrjpmix2fri", 
                                resource_type="image")
    poster_image = poster_image["secure_url"]
    
    # get navigation
    left_nav, right_nav = get_navigation_links("state_of_decay")

    context = {
        "left_nav": left_nav,
        "right_nav": right_nav,
            "title": "State of decay",
            "kriterion_image": kriterion_image,
            "poster_image": poster_image,
            "main_image": main_image,
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

    # get navigation
    left_nav, right_nav = get_navigation_links("sculptures")

    context = {
        "left_nav": left_nav,
        "right_nav": right_nav,
        "title": "Sculptures",
        "images":  image_urls
    }
    return render(request, "image_columns.html", context)


def dimensions(request):

    # get images from cloudinary storage
    images = cloudinary.api.resources(
                                type="upload", 
                                prefix="2d_into_3d", 
                                resource_type="image",
                                max_results=500) 
    
    image_urls = [img["secure_url"] for img in images["resources"]]

    # get navigation
    left_nav, right_nav = get_navigation_links("2d_into_3d")

    context = {
        "left_nav": left_nav,
        "right_nav": right_nav,
        "title": "2D into 3D",
        "images":  image_urls
    }

    return render(request, "image_columns.html", context)


def drawings(request):

    # get images from cloudinary storage
    images = cloudinary.api.resources(
                                type="upload", 
                                prefix="2d", 
                                resource_type="image",
                                max_results=500) 
    
    drawings_images = [img["secure_url"] for img in images["resources"] if "2d/drawings" in img["public_id"]]
    squareheads_images = [img["secure_url"] for img in images["resources"] if "2d/squareheads" in img["public_id"]]

    # get navigation
    left_nav, right_nav = get_navigation_links("drawings")

    context = {
        "left_nav": left_nav,
        "right_nav": right_nav,
        "title": "Paper Drawings",
        "drawings_images": drawings_images,
        "squareheads_images":  squareheads_images
    }

    return render(request, "drawings.html", context)


def crab(request):

    # pass the list of image files to the template
    files = []

    # get navigation
    left_nav, right_nav = get_navigation_links("crab")

    context = {
        "left_nav": left_nav,
        "right_nav": right_nav,
        'image_files': files,
        'title': 'crab'
    }

    return render(request, "image_columns.html", context)


def posters(request):

    # get images from cloudinary storage
    images = cloudinary.api.resources(
                                type="upload", 
                                prefix="posters", 
                                resource_type="image",
                                max_results=500) 
    
    image_urls = [img["secure_url"] for img in images["resources"]]

    # get navigation
    left_nav, right_nav = get_navigation_links("posters")

    context = {
        "left_nav": left_nav,
        "right_nav": right_nav,        
        "title": "Posters",
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
        
    # separate images by folder
    folder1_images = [img["secure_url"] for img in images["resources"] if "daily" in img["public_id"]]
    folder2_images = [img["secure_url"] for img in images["resources"] if "dancers" in img["public_id"]]
    folder3_images = [img["secure_url"] for img in images["resources"] if "extra" in img["public_id"]]

    # get navigation
    left_nav, right_nav = get_navigation_links("collages")

    context = {
        "left_nav": left_nav,
        "right_nav": right_nav,
        "title": "Collages",
        "daily_images": folder1_images,
        "dancers_images": folder2_images,
        "extra_images": folder3_images
    }
    
    return render(request, "collages.html", context)
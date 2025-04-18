from django.shortcuts import render
# from django.conf import settings
from .models import Image
import cloudinary.api
from cloudinary.api import resources_by_tag
from django.core.cache import cache
import os


NAVIGATION_ROUTES = [
    "index",
    "drawings",
    "collages",
    "posters",
    "poppen",
    "sculptures",
    "under_your_feet",
    "state_of_decay",
    "2d_into_3d",
    "hoofden",
    "seen_to_be_seen",
    "crab"
]

# set a global cache timeout (e.g., 1 hour)
cache_timeout = 3600 * 24  # seconds


def get_navigation_links(current_route):
    index = NAVIGATION_ROUTES.index(current_route)
    
    left_nav = NAVIGATION_ROUTES[index - 1] if index > 0 else None
    right_nav = NAVIGATION_ROUTES[index + 1] if index < len(NAVIGATION_ROUTES) - 1 else None
    
    return left_nav, right_nav


def index(request):

    # if not cached, fetch from Cloudinary and cache the results
    marie_image = cache.get("marie_image")
    if marie_image is None:

        # fetch image details by public_id
        image_data = cloudinary.api.resource("marie")
        

        # get the URL of the image
        marie_image = image_data["secure_url"]
        cache.set("marie_image", marie_image, cache_timeout)

    # if not cached, fetch from Cloudinary and cache the results
    recent_work_images = cache.get("recent_work_images")
    if recent_work_images is None:

        recent_work_folders = {
            "state_of_decay-bar": {"route": "state_of_decay", "text": "Staat van Verval"}, 
            "state_of_decay-bioscoop": {"route": "state_of_decay", "text": "Staat van Verval"}, 
            "current_work": {"route": "under_your_feet", "text": "Under Your Feet"},
            "project pop/pop fashion": {"route": "poppen", "text": "Poppen / dolls"},
            "hoofden": {"route": "hoofden", "text": "Faces x Silkscreen"}
        }
        recent_work_images = []

        for folder in recent_work_folders.keys():

            # fetch all images in the folder
            response = cloudinary.api.resources(type="upload", prefix=folder + "/", max_results=500)

            # filter images where public_id ends with 'main'
            for resource in response.get("resources", []):

                if resource["public_id"].endswith("main") or folder == "current_work":  # exact match for 'main'
                    
                    # quickfix: hoofden in currentwork folder -> juiste route en titel
                    if resource["public_id"].endswith("girls_currentwork"):
                        folder = "hoofden"

                    data = {}
                    data["title"] = folder.split("-")[0]
                    data["url"] = resource["secure_url"]
                    data["route"] = recent_work_folders[folder]["route"]
                    data["tooltip"] = recent_work_folders[folder]["text"]
                    recent_work_images.append(data)  # get image URL

    # if not cached, fetch from Cloudinary and cache the results
    current_work_images = cache.get("current_work_images")
    if current_work_images is None:

        # fetch all images in the 'hoofden' folder
        response = cloudinary.api.resources(type="upload", prefix="hoofden/", max_results=50)
        current_work_images = []

        # filter work in progress images where public_id ends with 'wip'
        for resource in response.get("resources", []):
            if resource["public_id"].endswith("wip"):
                current_work_images.append(resource["secure_url"])
                
        # cache the results      
        cache.set("current_work_images", current_work_images, cache_timeout)

        # print(current_work_images)

    # get navigation
    left_nav, right_nav = get_navigation_links("index")

    context = {
        "left_nav": left_nav,
        "right_nav": right_nav,
        "marie": marie_image,
        "current_work_images": current_work_images,
        "recent_work_images": recent_work_images
    }

    return render(request, "index.html", context)


def under_your_feet(request):

    route = "under_your_feet"

    # try to get images from cache
    image_urls = cache.get(route)

    # fetch images from Cloudinary only if not in cache
    if not image_urls:
        images = cloudinary.api.resources(
            type="upload",
            prefix=route,
            resource_type="image",
            max_results=500
        )
        image_urls = [img["secure_url"] for img in images["resources"]]

        # store the image URLs in cache
        cache.set(route, image_urls, timeout=cache_timeout)

    # get navigation
    left_nav, right_nav = get_navigation_links(route)

    context = {
        "left_nav": left_nav,
        "right_nav": right_nav,
        "title": "Under Your Feet",
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
        "title": "Faces x Silkscreen",
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
                                public_id="state_of_decay-bar/fam", 
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
            "title": "Staat van Verval",
            "kriterion_image": kriterion_image,
            "poster_image": poster_image,
            "main_image": main_image,
            "image_files_bar":  image_bar_urls,
            "image_files_bioscoop":  image_bioscoop_urls
        }

    return render(request, "state_of_decay.html", context)


def sculptures(request):

    route = "sculptures"

    # try to get images from cache
    image_urls = cache.get(route)

    # fetch images from Cloudinary only if not in cache
    if not image_urls:
        images = cloudinary.api.resources(
            type="upload",
            prefix=route,
            resource_type="image",
            max_results=500
        )
        image_urls = [img["secure_url"] for img in images["resources"]]

        # store the image URLs in cache
        cache.set(route, image_urls, timeout=cache_timeout)

    # get navigation
    left_nav, right_nav = get_navigation_links(route)

    context = {
        "left_nav": left_nav,
        "right_nav": right_nav,
        "title": "Sculptures",
        "images": image_urls
    }
    
    return render(request, "image_columns.html", context)


def dimensions(request):

    route = "2d_into_3d"

    # try to get images from cache
    image_urls = cache.get(route)

    # fetch images from Cloudinary only if not in cache
    if not image_urls:
        images = cloudinary.api.resources(
            type="upload",
            prefix=route,
            resource_type="image",
            max_results=500
        )
        image_urls = [img["secure_url"] for img in images["resources"]]

        # store the image URLs in cache
        cache.set(route, image_urls, timeout=cache_timeout)

    # get navigation
    left_nav, right_nav = get_navigation_links(route)

    context = {
        "left_nav": left_nav,
        "right_nav": right_nav,
        "title": "2D Into 3D",
        "images": image_urls
    }
    
    return render(request, "image_columns.html", context)


def drawings(request):
    route = "drawings"
    cache_key_drawings = "drawings"
    cache_key_squareheads = "squareheads"

    # try to get images from cache
    drawings_images = cache.get(cache_key_drawings)
    squareheads_images = cache.get(cache_key_squareheads)

    # fetch images from Cloudinary only if not in cache
    if not drawings_images or not squareheads_images:
        images = cloudinary.api.resources(
            type="upload",
            prefix="2d",
            resource_type="image",
            max_results=500
        )

        drawings_images = [img["secure_url"] for img in images["resources"] if f"2d/{cache_key_drawings}" in img["public_id"]]
        squareheads_images = [img["secure_url"] for img in images["resources"] if f"2d/{cache_key_squareheads}" in img["public_id"]]

        # store the image URLs in cache
        cache.set(cache_key_drawings, drawings_images, timeout=cache_timeout)
        cache.set(cache_key_squareheads, squareheads_images, timeout=cache_timeout)

    # get navigation
    left_nav, right_nav = get_navigation_links(route)

    context = {
        "left_nav": left_nav,
        "right_nav": right_nav,
        "title": "Paper Drawings",
        "drawings_images": drawings_images,
        "squareheads_images": squareheads_images
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
        'title': 'Crab'
    }

    return render(request, "image_columns.html", context)


def posters(request):

    route = "posters"

    # try to get images from cache
    image_urls = cache.get(route)

    # fetch images from Cloudinary only if not in cache
    if not image_urls:
        images = cloudinary.api.resources(
            type="upload",
            prefix=route,
            resource_type="image",
            max_results=500
        )
        image_urls = [img["secure_url"] for img in images["resources"] if not "original_size/" in str(img)]

        # store the image URLs in cache
        cache.set(route, image_urls, timeout=cache_timeout)

    # get navigation
    left_nav, right_nav = get_navigation_links(route)

    context = {
        "left_nav": left_nav,
        "right_nav": right_nav,
        "title": "Posters",
        "images": image_urls
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
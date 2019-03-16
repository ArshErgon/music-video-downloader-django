
import pafy
import os

from django.shortcuts import render, redirect
from .forms import MusicUrl         # importing all forms and model dot(.) means current directory means from music.forms import MusicUrl
from .models import MusicModelJAM, MusicModelMobile

# Everything is working fine the searching of the song get the song information but one thing is not working.
# downloading songs and videos are working if give the location for download but in deployment every user has different location for downloading things then how can I make it
# I try import os and <a href="" download></a> but it still can't work

# ================== what is request ===================
#  request is what user has type like google.com show us google logo etc but google.com/mail give us gmail the thing which are after / is request
# ================== what is remder here ==================
# remder mix the html code and directory items and we can use it in html link   {{ x }} by using x = { x : "12"}

# ========================== How each function works ===================================
#  -------------------------- music_home function -------------------------------------
# 1. it display the home page with a form which is inbuit in django look in music/forms.py
# 2. link is getting the youtube url
# 3. In music variable all the information regarding to the url link name, author, likes, etc we got
# 4. MusicModelJAM is our database(see music/models.py) it save the link because it can inherit to download_data it will say missing one argument which is request

#  for desktop download start here

def music_home(request):
    form = MusicUrl(request.POST or None)
    music = ''  # Make a empty string so you can't get a UnBoundError
    print(request.POST.get('url'))
    print('Try block start here')
    try:
        link = request.POST.get('url') # get the url and search for it
        music = pafy.new(link) # get all information about the song
        MusicModelJAM.objects.create(url=link) # save the data in database so that we can inherited it to another function
        # It can't inherited like this global keyword can work but when the function calls we say one argument is missing "request"
        return render(request, 'music/music_home.html', {'form':form, 'music':music})
    except:
        pass
    print(music)
    return render(request, 'music/music_home.html', {'form':form})

# -------------------------- download_data (to download music) --------------------------
# 1. again form
# 2. here the link keyword take the link from the database (but in data there may be lot of links so we use the for loop)
# 3. for loop to get all the data in link
# 4. after getting last data we delete the database
# 5. user_need tell which thing he want song or to download video (if, elif, else)
# 6. music_down tell where it should download the music or video

def download_data(request):
    form = MusicUrl(request.POST or None) # form see in forms.py
    links = MusicModelJAM.objects.all() # get all element that are present in database
    music_down = ''                     # empty string for not to face UnBoundError
    print(request.path_info)
    # print(os.getcwd(), 'printing working directory for know the download loca')
    for link in links:
        pass
    music = pafy.new(link)
    MusicModelJAM.objects.all().delete()
    MusicModelJAM.objects.all().delete()

    user_need =  request.POST.get("selected")

    if str(user_need) == 'Audio:m4a@128k':
        music_down = music.getbestaudio(preftype='m4a')
        music_down.download(filepath="C:")
        # music_down.download()
        return redirect("/thank/")

    elif str(user_need) == 'Video:mp4@640x360':
        music_down = getbest(preftype='mp4')
        music_down.download(filepath="C:")
        return redirect("/thank/")

    elif str(user_need) == 'Video:mp4@1920x1080':
        music_down = getbestideo(preftype='mp4')
        music_down.download(filepath="C:")
        return redirect("/thank/")
    else:
        pass
    return render(request, 'music/music_home.html', {'form':form})

# End here
# ============================ mobile_music_search =============================
# this will redirect to a html page which made only for mobile devices I use javascript for this (see music_home.html last line)
# 1. again form
# 2 it is same as music_home function
# from here mobile music downloader start

def mobile_music_search(request):
    form = MusicUrl(request.POST or None)
    try:
        link = request.POST.get('url')
        music = pafy.new(link)
        MusicModelMobile.objects.create(url=link)
        return render(request, 'music/mobile_music_downloader.html', {'form':form, 'music':music})
    except:
        pass


    return render(request, "music/mobile_music_downloader.html", {'form': form})

# ======================== mobile_music_downloader ===========================
# ====================== it is same as download_data functin ==================
# 1. here the music download path is Internal storage\\Downloads\\ most common download location in android
# 2. the redirect goes to thank page download complete
def mobile_music_downloader(request):
    form = MusicUrl(request.POST or None)
    links = MusicModelMobile.objects.all()
    for link in links:
        pass
    music = pafy.new(link)
    MusicModelMobile.objects.all().delete()
    MusicModelMobile.objects.all().delete()
    user_need =  request.POST.get("selected")

    if str(user_need) == 'Audio:m4a@128k':
        music_down = music.getbestaudio(preftype='m4a')
        music_down.download(filepath="Internal storage\\Downloads\\")
        # music_down.download(filepath="C:\\Users\\HP\\Desktop\\APK projects") # save location on mobile devices

        # return redirect('%s'%(str(request.path_info)))
        print("Mobile download")
        return redirect("/thank/")

    elif str(user_need) == 'Video:mp4@640x360':
        music_down = getbest(preftype='mp4')
        music_down.download(filepath="Internal storage\\Downloads\\")
        return redirect("/thank/")

    elif str(user_need) == 'Video:mp4@1920x1080':
        music_down = getbestideo(preftype='mp4')
        music_down.download(filepath="Internal storage\\Downloads\\")
        return redirect("/thank/")

    else:
        pass

    return render(request, 'music/mobile_music_downloader.html', {'form':form})

# end here

# thank you page
def thankyou(request):
    return render(request, 'index.html')

# practice function for testing
def trypage(request):
    links = MusicModelJAM.objects.all()
    music_down = ''
    location = request.POST.get("name")
    print(location)
    print(request.path_info)
    for link in links:
        pass
    music = pafy.new(link)
    try:
        link = request.POST.get('url')
        music = pafy.new(link)
        print(music)
        music_title = music.title
        music_author = music.author
        music_thumbnail = music.bigthumbhd
        music_url = music.watchv_url
        music_category = music.category
        print(music_category, 'condition start here')
    except:
        pass
    return render(request, 'try.html', {'music':music, 'location':location})

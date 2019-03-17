
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
        print(music)

        return render(request, 'music/music_home.html', {'form':form, 'music':music})
    except:
        pass
    print(music)
    return render(request, 'music/music_home.html', {'form':form, 'music':music})

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
    extension = music_down = ''                     # empty string for not to face UnBoundError
    print(request.path_info)
    # print(os.getcwd(), 'printing working directory for know the download loca')

    for link in links:
        pass
    music = pafy.new(link)

    user_need =  request.POST.get("selected")

    if str(user_need) == 'Audio:m4a@128k':
        music_down = music.getbestaudio(preftype='m4a')
        # print(dir(music_down))
        extension = music_down.extension    # taking the extension of the music like m4a for audio or mp4 for videos
        return render(request, 'music/music_home.html', {'form':form, 'extension':extension, 'music':music, 'music_down':music_down})

    elif str(user_need) == 'Video:mp4@640x360':
        music_down = music.getbest(preftype='mp4')
        extension = music_down.extension
        return render(request, 'music/music_home.html', {'form':form, 'extension':extension, 'music':music, 'music_down':music_down})

    elif str(user_need) == 'Video:mp4@1920x1080':
        music_down = music.getbest(preftype='mp4')
        extension = music_down.extension
        return render(request, 'music/music_home.html', {'form':form, 'extension':extension, 'music':music,  'music_down':music_down})
    else:
        pass
    # MusicModelJAM.objects.all().delete()
    # MusicModelJAM.objects.all().delete()
    return render(request, 'music/music_home.html', {'form':form, 'extension':extension})


# # practice function for testing
# def trypage(request):
#     links = MusicModelJAM.objects.all()
#     music_down = ''
#
#     print(request.path_info)
#     for link in links:
#         pass
#     music = pafy.new(link)
#     music_down = music.getbestvideo(preftype="mp4")
#     # extension = 'm4a'
#     extension = music_down.extension
#     print(dir(music_down))
#     # time.sleep(20)
#     # music_try = music_down.download()
#     # try:
#     #     music = pafy.new(link)
#     #     print(music)
#     #     print(dir(music))
#     #
#     #     music_down = music.getbestaudio(preftype='m4a')
#     #     print(music_down, 'printing it here')
#     #     return render(request, 'try.html', {'music':music, 'music_down':music_down})
#     # except:
#     #     pass
#     # print(music_down, 'downloading music')
#     # print(request.POST.get("location"), 'location is print here')
#     return render(request, 'try.html', {'music':music, 'music_down':music_down, 'extension':extension, 'link':link})

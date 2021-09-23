from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
from django.contrib import messages
import pytube
import os


# Create your views here.
def home(request):
    return render(request, 'home.html')


def playlist(request):
    return render(request, 'palylist_home.html')


def mp3(request):
    return render(request, 'mp3_home.html')


def about(request):
    return render(request, 'about.html')


def copy(request):
    return render(request, 'copyright.html')


def dmca(request):
    return render(request, 'dmca.html')


def faqs(request):
    return render(request, 'faqs.html')


def contact(request):
    return render(request, 'contactus.html')


def privacy(request):
    return render(request, 'privacypolicy.html')


def terms(request):
    return render(request, 'termsofservice.html')


def msg(request, message):
    return render(request, 'download.html', {'msg': message})


@csrf_exempt
def download(request):
    global link
    # link = str(request.POST.get('link'))
    # print(link)
    link = request.GET.get('url')
    print(link)
    yt = pytube.YouTube(link)
    print(yt)
    dis = {}
    ls = []

    video = yt.streams.filter(progressive="True")
    audio = yt.streams.filter(only_audio="True")
    for i in video:
        print(i)
        dis['res'] = i.resolution
        dis['frm'] = i.mime_type
        dis['size'] = str(round((i.filesize) / 1048576, 2)) + 'MB'

        ls.append(dis.copy())

    for j in audio:
        dis['res'] = j.abr
        dis['frm'] = j.mime_type
        dis['size'] = str(round((j.filesize) / 1048576, 2)) + 'MB'

        ls.append(dis.copy())

    print(ls)
    embed_link = link.replace("watch?v=", "embed/")
    print(embed_link)
    data = {
        'embd': embed_link,
        'obj': ls
    }
    dump = json.dumps(data)
    return render(request, 'video.html', {'embd': embed_link, 'obj': ls})
    # return HttpResponse(dump, content_type='application/json')


def post_upload(request):
    global link
    url = link

    obj = pytube.YouTube(url)
    res = str(request.POST.get('resolution'))

    f = str(request.POST.get('format')).split("/")

    fromate = f[0]
    frm = f[1]

    video = './download/video'
    audio = './download/audio'
    msg = ''
    if fromate == 'video':
        dv = obj.streams.filter(progressive="True", resolution=res, file_extension=frm).first()
        # dv.download(output_path=video)
        dv.download()

        msg = dv.title + ' Video Download Successfully '
        print(msg)

        data = {
            'status': 'video',
            'msg': msg
        }
        dump = json.dumps(data)
        return HttpResponse(dump, content_type='application/json')

    elif fromate == 'audio':
        dv = obj.streams.filter(abr=res, file_extension=frm).first()
        # dv.download(audio)
        dv.download()

        msg = dv.title + ' Audio Download Successfully'
        print(msg)
        data = {
            'status': 'audio',
            'msg': msg
        }
        dump = json.dumps(data)
        return HttpResponse(dump, content_type='application/json')

    else:
        msg = 'Check your Internet connection or Enter Valid Link '
        print(msg)
        # data = 'fail'
        # return 'fail'

        data = {
            'status': 'Fail',
            'msg': msg
        }
        dump = json.dumps(data)
        return HttpResponse(dump, content_type='application/json')


def playlist_download(request):
    global link
    link = request.GET.get('url')
    yt = pytube.Playlist(link)
    dis = {}
    ls = []

    for video in yt.videos:
        video1 = video.streams.filter(progressive="True")
    print(video1)

    for i in video1:
        print(i)
        dis['res'] = i.resolution
        dis['frm'] = i.mime_type
        dis['size'] = str(round((i.filesize) / 1048576, 2)) + 'MB'

        ls.append(dis.copy())

    for video in yt.videos:
        audio = video.streams.filter(only_audio="True")
    print(audio)

    for j in audio:
        dis['res'] = j.abr
        dis['frm'] = j.mime_type
        dis['size'] = str(round((j.filesize) / 1048576, 2)) + 'MB'

        ls.append(dis.copy())

    embed_link = link.replace("watch?v=", "embed/")

    return render(request, 'playlist_video.html', {'embd': embed_link, 'obj': ls})


def playlist_upload(request):
    global link
    url = link

    obj = pytube.Playlist(url)
    res = str(request.POST.get('resolution'))

    f = str(request.POST.get('format')).split("/")

    fromate = f[0]
    frm = f[1]

    video = './download/playlist/video'
    audio = './download/playlist/audio'
    msg = ''
    if fromate == 'video':
        for dv in obj.videos:
            dv1 = dv.streams.filter(progressive="True", resolution=res, file_extension=frm).first()
            dv1.download(output_path=video)
            # dv1.download()

        msg = obj.title + 'Playlist in Video Download Successfully '
        print(msg)

        data = {
            'status': 'video',
            'msg': msg
        }
        dump = json.dumps(data)
        return HttpResponse(dump, content_type='application/json')

    elif fromate == 'audio':
        for da in obj.videos:
            da1 = da.streams.filter(abr=res, file_extension=frm).first()
            da1.download(output_path=audio)
            # da1.download()

        msg = obj.title + 'Playlist in Audio Download Successfully'
        print(msg)
        data = {
            'status': 'audio',
            'msg': msg
        }
        dump = json.dumps(data)
        return HttpResponse(dump, content_type='application/json')

    else:
        msg = 'Check your Internet connection or Enter Valid Link '
        print(msg)
        # data = 'fail'
        # return 'fail'

        data = {
            'status': 'Fail',
            'msg': msg
        }
        dump = json.dumps(data)
        return HttpResponse(dump, content_type='application/json')


def mp3_download(request):
    global link
    link = request.GET.get('url')
    yt = pytube.YouTube(link)
    dis = {}
    ls = []

    audio = yt.streams.filter(only_audio="True")

    for j in audio:
        dis['res'] = j.abr
        dis['frm'] = 'mp3'
        dis['size'] = str(round((j.filesize) / 1048576, 2)) + 'MB'

        ls.append(dis.copy())

    embed_link = link.replace("watch?v=", "embed/")

    return render(request, 'mp3_video.html', {'embd': embed_link, 'obj': ls})


def mp3_upload(request):
    global link
    url = link

    obj = pytube.YouTube(url)
    res = str(request.POST.get('resolution'))

    # f = str(request.POST.get('format')).split("/")

    # fromate = f[0]
    # frm = f[1]

    audio = './download/audio'
    msg = ''

    # if fromate == 'audio':
    if obj:
        da = obj.streams.filter(abr=res).first()
        out_file = da.download(output_path=audio)
        # out_file = da.download()
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

        msg = obj.title + 'Convert into mp3 Audio Download Successfully'
        print(msg)
        data = {
            'status': 'audio',
            'msg': msg
        }
        dump = json.dumps(data)
        return HttpResponse(dump, content_type='application/json')

    else:
        msg = 'Check your Internet connection or Enter Valid Link '
        print(msg)
        # data = 'fail'
        # return 'fail'

        data = {
            'status': 'Fail',
            'msg': msg
        }
        dump = json.dumps(data)
        return HttpResponse(dump, content_type='application/json')

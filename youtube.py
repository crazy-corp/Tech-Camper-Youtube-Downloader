from  pytube import YouTube
import PySimpleGUI as sg
import time
import os
import subprocess

previousprogress = 0
ico=b'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'
def on_progress(stream, chunk, bytes_remaining):
    global previousprogress
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining 

    liveprogress = (int)(bytes_downloaded / total_size * 100)
    if liveprogress > previousprogress:
        previousprogress = liveprogress
        window['progbar'].update_bar(liveprogress)
#python -m pip install git+https://github.com/nficano/pytube
sg.theme('Black')	# Add a touch of color
# All the stuff inside your window.
layout = [[sg.Text('Enter The Link'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Youtube Downloader - TechCamper', layout,icon=ico)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, link = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel'or event =='Ok':	# if user closes window or clicks cancel
        window.close()
    yt=YouTube(link[0])
    Available_streams=yt.streams.order_by('resolution').desc()
    b=yt.streams.filter(progressive=True).order_by('resolution').desc()
    c=yt.streams.filter(only_audio=True)  
    layout = [[sg.Text('All Available Streams (post process required)')],[sg.Listbox(values=Available_streams, size=(60, 8))],
    [sg.Text('Video+Audio (Fastest)')],[sg.Listbox(values=b, size=(60, 3))],[sg.Text('Only Audio')],[sg.Listbox(values=c, size=(60, 3))],
          [sg.Text('Enter itag'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')],[sg.Text('Downloading progress')],
          [sg.ProgressBar(100, orientation='h', size=(40, 20), key='progbar')]]
    window = sg.Window('Youtube Downloader - TechCamper', layout,icon=ico)
    event,itag = window.read()
    yt.register_on_progress_callback(on_progress)
    file=yt.streams.get_by_itag(itag[3])
    if file not in b and file not in c:
        file.download(filename="TempMp4")
        c.first().download(filename="TemMp3")
        sg.Print('Post Process', do_not_reroute_stdout=False)
        x=yt.title
        x=x.split("|")
        x=x[0]
        x=x.replace(" ","_")
        y=x+".mp4"
        try:
            cmd="ffmpeg.exe -i TempMp4.mp4 -i TemMp3.mp4 -c copy "+y
            subprocess.call(cmd, shell=True)                                    
            print('Mixing Done')
            os.remove("TempMp4.mp4")
            os.remove("TemMp3.mp4")
        except:
            try:
                cmd="ffmpeg.exe -i TempMp4.webm -i TemMp3.mp4 -c copy "+y
                subprocess.call(cmd, shell=True)                                    
                print('Mixing Done')
                os.remove("TempMp4.webm")
                os.remove("TemMp3.mp4")
            except:
                try:
                    cmd="ffmpeg.exe -i TempMp4.mp4 -i TemMp3.webm -c copy "+y
                    subprocess.call(cmd, shell=True)                                    
                    print('Mixing Done')
                    os.remove("TempMp4.mp4")
                    os.remove("TemMp3.webm")
                except:
                    cmd="ffmpeg.exe -i TempMp4.webm -i TemMp3.webm -c copy "+y
                    subprocess.call(cmd, shell=True)                                    
                    print('Mixing Done')
                    os.remove("TempMp4.webm")
                    os.remove("TemMp3.webm")
    else:
        yt.streams.get_by_itag(itag[3]).download()
    sg.PopupNonBlocking("Downloaded into app Directory",icon=ico)
    time.sleep(2)
    if event == sg.WIN_CLOSED or event == 'Cancel'or event =='Ok':	# if user closes window or clicks cancel
        break
window.close()
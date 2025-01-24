# Auto Generated Shorts Videos using Manim and ChatTTS

This project show how to generate a short video without any editing or recording.
Everything is completed by pure coding and model generation. 

Result

https://www.youtube.com/shorts/rv0BuhHG9TQ

Free free to give star ⭐ for this project.

## Pre-requisites 

I'm using Ubuntu 24.04, Miniforge Python 3.11. Packages needed are :

1. Manim for video creation ( https://github.com/ManimCommunity/manim )
2. ChatTTS for audio generation ( https://github.com/2noise/ChatTTS )
3. FFMPEG for audio + video merging

Please follow each step installation.

### Setup and Generate the video

```
git clone https://github.com/yodiaditya/manim-shorts
cd manim-shorts
manim -pqk main.py Main
```

### Generate audio
The pre-generated audio located at `assets` and for voice embedding in `embedding` folder.

If you want to know, please check `audio.py`

```
python audio.py
```

## Merging Audio and Video
Copy the output of Manim video into `assets` folder. Then go inside and run this

```
ffmpeg -i Main.mp4 -i 1.wav -i 2.wav -i 3.wav -i silent.wav -i 4.wav -filter_complex \
"[1:a][2:a]concat=n=2:v=0:a=1[a1]; \
 [a1][3:a]concat=n=2:v=0:a=1[a2]; \
 [a2][4:a]concat=n=2:v=0:a=1[a3]; \
 [a3][5:a]concat=n=2:v=0:a=1[aout]" \
-map 0:v -map "[aout]" -c:v copy -c:a aac final_video.mp4
```

## Credits
By @yodiaditya. Happy to connect with you over Linkedin and Github!
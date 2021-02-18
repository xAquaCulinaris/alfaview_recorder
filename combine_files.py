import moviepy.editor as mpe

def combine_audio(vidname, audname, outname, fps=25):
    print('Starting combining files..')
    my_clip = mpe.VideoFileClip(vidname)
    audio_background = mpe.AudioFileClip(audname)
    final_clip = my_clip.set_audio(audio_background)
    final_clip.write_videofile(outname,fps=fps)
    print('Files have been combined..')

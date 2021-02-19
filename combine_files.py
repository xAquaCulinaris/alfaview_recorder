import moviepy.editor as mpe
from config_parser import get_config_string

def combine_audio(vidname, audname, fps=25):
    outname = get_config_string('DEFAULT', 'outputFile')

    print('Starting combining files..')
    my_clip = mpe.VideoFileClip(vidname)
    audio_background = mpe.AudioFileClip(audname)
    final_clip = my_clip.set_audio(audio_background)
    final_clip.write_videofile(outname,fps=fps)
    print('Files have been combined..')

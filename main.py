import musicalgestures

def analyse_video(video_name, stack_title, preprocessing=False):
    if preprocessing:
        mg = musicalgestures.MgVideo(video_name, contrast=55, brightness=30)
    else:
        mg = musicalgestures.MgVideo(video_name)

    # Horizontal  & vertical motiongrams, centroid & quantity of motion plots, motion videos, directograms, impacts
    # & motion average
    motiongrams = mg.motiongrams()
    motionplots = mg.motionplots()
    motion_video = mg.motionvideo()
    directograms = mg.directograms()
    impact_envelopes = mg.impacts(detection=False)
    impact_detection = mg.impacts(detection=True)
    motion_average = motion_video.average()
    my_list = musicalgestures.MgList(motiongrams, directograms, impact_envelopes, impact_detection, motionplots,
                                     motion_average)
    figures_stack = my_list.as_figure(title=stack_title)
    print(figures_stack)

    # Motion history video
    mg.history(mg.of + '_motion.avi', history_length=25)

    # sparse optical flow
    mg.flow.sparse()


if __name__ == '__main__':
    analyse_video('videos/clarinet_1/Brahms uprigth 003.avi', 'Clarinet Standing #1')
    analyse_video('videos/clarinet_2/Brahms Natural 004.avi', 'Clarinet Standing #2', True)



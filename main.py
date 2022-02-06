import musicalgestures

def analyse_video(video_name, stack_title, preprocessing=False):
    if preprocessing:
        mg = musicalgestures.MgObject(video_name, contrast=55, brightness=30)
    else:
        mg = musicalgestures.MgObject(video_name)

    # Horizontal  & vertical motiongrams, centroid & quantity of motion plots, motion videos & motion average
    motiongrams = mg.motiongrams()
    motionplots = mg.motionplots()
    motion_video = mg.motionvideo()
    motion_average = motion_video.average()
    motion_video.show()
    my_list = musicalgestures.MgList(motiongrams, motionplots, motion_average)
    figures_stack = my_list.as_figure(title=stack_title)
    print(figures_stack)

    # Motion history video
    mg.history(mg.of + '_motion.avi', history_length=25)

    # sparse optical flow
    flow_sparse = mg.flow.sparse()


if __name__ == '__main__':
    analyse_video('videos/clarinet_1/Brahms uprigth 003.avi', 'Clarinet Standing #1')
    analyse_video('videos/clarinet_2/Brahms Natural 004.avi', 'Clarinet Standing #2', True)



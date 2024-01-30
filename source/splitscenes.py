from classes.scene_splitter import SceneSplitter

splitter = SceneSplitter()
scenes = splitter.find_scenes('./media/homevid.avi')
print(scenes)
    
for start_time, end_time in scenes:
    print(f'Scene starts at {start_time.get_seconds()}s and ends at {end_time.get_seconds()}s')
    print(f'Scene starts at frame {start_time.get_frames()} and ends at frame {end_time.get_frames()}')

    
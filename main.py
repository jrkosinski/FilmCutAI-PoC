from source.classes.scene_splitter import SceneSplitter
from source.utils.encode_image import encode_frame_base64

scene_splitter = SceneSplitter()
scene_list = scene_splitter.find_scenes('./media/homevid.avi', write_out_scenes=True, output_dir="./scene_output")


print(scene_list)
import MemePy as mp
from PIL import Image

dob = '12/34/5678'
dod = '12/34/6789'

im = Image.open('./resources/ImageLibrary/dead_person.jpg')
width, height = im.size
#print(width, height)

with open('./resources/meme-def-template.json', 'r') as f:
    lines_with_placeholders = f.readlines()

nb_pos_encounters = 0
nb_dim_encounters = 0
top_box_size = 200
bottom_box_size = 900
text_color = [255, 255, 255]

lines_to_export = []
for line in lines_with_placeholders:
    if "\"pos\"" in line:
        if nb_pos_encounters < 1:
            line = line.replace("TOP_X", str((width - top_box_size) // 2), 1)
            line = line.replace("TOP_Y", str(height // 20), 1)
        else:
            line = line.replace("BOTTOM_X", str((width - bottom_box_size) // 2), 1)
            line = line.replace("BOTTOM_Y", str(7.5 * height // 10), 1)
        nb_pos_encounters += 1
    elif "\"dimensions\"" in line:
        if nb_dim_encounters < 1:
            line = line.replace("TOP_BOX_SIZE", str(top_box_size))
        else:
            line = line.replace("BOTTOM_BOX_SIZE", str(bottom_box_size))
        nb_dim_encounters += 1
    elif "\"text_color\"" in line:
        line = line.replace("TEXT_COLOR", str(text_color))
    lines_to_export.append(line)

#print(lines_to_export)

with open('./resources/MemeLibrary/meme-def.json', 'w') as f:
    f.writelines(lines_to_export)


mp.add_external_resource_dir('./resources')
mp.save_meme_to_disk('DeadPerson', '.', ['R.I.P.', dob+'\n'+dod])




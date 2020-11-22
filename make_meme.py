import MemePy as mp
from PIL import Image

TOP_BOX_SIZE = 200
BOTTOM_BOX_SIZE = 1000
TEXT_COLOR = [255, 255, 255]

def make_meme(birth_date, death_date, image_path):
    im = Image.open(image_path)
    width, height = im.size
    im.convert("RGB").save(image_path)
    #print(width, height)

    with open('./meme-def-template.JSON', 'r') as f:
        lines_with_placeholders = f.readlines()

    nb_pos_encounters = 0
    nb_dim_encounters = 0

    lines_to_export = []
    for line in lines_with_placeholders:
        if "\"pos\"" in line:
            if nb_pos_encounters < 1:
                line = line.replace("TOP_X", str((width - TOP_BOX_SIZE) // 2), 1)
                line = line.replace("TOP_Y", str(height // 20), 1)
            else:
                line = line.replace("BOTTOM_X", str((width - BOTTOM_BOX_SIZE) // 2), 1)
                line = line.replace("BOTTOM_Y", str(7.5 * height // 10), 1)
            nb_pos_encounters += 1
        elif "\"dimensions\"" in line:
            if nb_dim_encounters < 1:
                line = line.replace("TOP_BOX_SIZE", str(TOP_BOX_SIZE))
            else:
                line = line.replace("BOTTOM_BOX_SIZE", str(BOTTOM_BOX_SIZE))
            nb_dim_encounters += 1
        elif "\"text_color\"" in line:
            line = line.replace("TEXT_COLOR", str(TEXT_COLOR))
        lines_to_export.append(line)

    # print(lines_to_export)

    with open('./resources/MemeLibrary/meme-def.json', 'w') as f:
        f.writelines(lines_to_export)

    mp.add_external_resource_dir('./resources')
    mp.save_meme_to_disk('DeadPerson', '.', ['R.I.P.', birth_date + '\n' + death_date + ' '])

if __name__ == '__main__':
    make_meme('2000-02-28', '2000-05-05', './resources/ImageLibrary/dead_person.jpg')

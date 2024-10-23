from PIL import Image
import numpy as np
import json
import os


def get_average_color(image_path):
    img = Image.open(image_path)
    img = img.convert('RGB')
    img_array = np.array(img)
    average_color = img_array.mean(axis=(0, 1))
    average_color = average_color.astype(int)
    
    return average_color.tolist()
def provide_text_document(text_document_path):
    with open(text_document_path,"r") as file:
        content=json.load(file)
    return content

def save_text_document(text_document_path,data):
    with open(text_document_path,"w") as file:
        json.dump(data,file,indent=4)
   

def convert_block_and_save_data(folder_path):
    content=provide_text_document(text_document_path)
    content=[]
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            try:
                color=get_average_color(file_path)
                new_data={
                    "name":os.path.splitext(os.path.basename(file_path))[0],
                    "rgb":color
                }
                content.append(new_data)
                print(f"Processed and saved: {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")
    sorted_data = sorted(content, key=lambda x: x['rgb'])
    save_text_document(text_document_path,sorted_data)




text_document_path=r''
blocks_folder=r''
#convert_block_and_save_data(blocks_folder)





import json
import math
def provide_text_document(text_document_path):
    with open(text_document_path,"r") as file:
        content=json.load(file)
    return content

def calculate_rgb_distance(rgb1, rgb2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(rgb1, rgb2)))

def find_nearest_block(data, target_rgb):
    nearest_block = None
    nearest_distance = float('inf')

    for block in data:
        current_distance = calculate_rgb_distance(block['rgb'], target_rgb)
        if current_distance < nearest_distance:
            nearest_distance = current_distance
            nearest_block = block

    return nearest_block


text_document_path=r''

target_rgb = [254, 254, 254]  # Example target RGB value
data = provide_text_document(text_document_path)
nearest_block = find_nearest_block(data, target_rgb)

if nearest_block:
    print(f"The block nearest to {target_rgb} is:")
    print(json.dumps(nearest_block, indent=4))
else:
    print("No blocks found.")
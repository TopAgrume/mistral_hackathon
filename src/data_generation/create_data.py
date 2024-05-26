import numpy as np
from PIL import Image as im 
import pandas as pd
from tqdm import tqdm
import re

paths = [("apple", "apple.npy"), ("bicycle", "bicycle.npy"), ("car", "car.npy")]
 
dfs = []

chars = [" ", ".", ",", ":", ";", "-", "=", "+", "*", "#", "@"]
pixel_range = len(chars) - 1

for label, file in paths:    
    df = pd.DataFrame(columns=["messages"])
    tmp = np.load(rf"{file}")
    len_tmp = len(tmp)
    
    for i in tqdm(range(1, len_tmp)):
        img = tmp[i].reshape((28, 28))
        img = im.fromarray(img)

        new_width = 50
        new_height = 27.5
        img = img.resize((new_width, int(new_height))).convert('L')

        pixels = img.getdata()
        new_pixels = [chars[pixel * pixel_range // 255] for pixel in pixels]
        new_pixels = ''.join(new_pixels)
        
        new_pixels_count = len(new_pixels)
        ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
        ascii_image = "\n".join(ascii_image)
        skipping_return = re.sub(r'\n{2,}', '\n', ascii_image)
        formatting_ascii = re.sub(r'\n', f'\n<{label}_start>', skipping_return)
        
        df.loc[i] = {"messages": [{"role": "user", "content": f"Generate me an ASCII art of {label}"}, {"role": "assistant", "content": f"Here is ASCII art of {label} : {ascii_image}"}]}
    dfs.append(df)
    
final_df = pd.concat(dfs)

df_train=final_df.sample(frac=0.95, random_state=42)
df_eval=final_df.drop(df_train.index)

df_train.to_json("multi_train.jsonl", orient="records", lines=True)
df_eval.to_json("multi_eval.jsonl", orient="records", lines=True)

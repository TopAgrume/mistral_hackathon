import numpy as np
from PIL import Image as im 
import pandas as pd
from tqdm import tqdm

paths = [("apple", "full_numpy_bitmap_apple.npy"), ("airplane", "full_numpy_bitmap_airplane.npy"), ("radio", "full_numpy_bitmap_radio.npy"), ("birthday cake", "full_numpy_bitmap_birthday cake.npy"), ("eiffel tower", "full_numpy_bitmap_The Eiffel Tower.npy")]
 
dfs = []

chars = [" ", ",", "$", "Y", "+", "P", "*", "%", "D", "J", "@"]

for label, file in paths:    
    df = pd.DataFrame(columns=["messages"])
    tmp = np.load(rf"C:\Users\maelr\Downloads\{file}")
    len_tmp = len(tmp)
    
    for i in tqdm(range(len_tmp)):
        img = tmp[i].reshape((28, 28))
        img = im.fromarray(img)

        new_width = 50
        new_height = 27.5
        img = img.resize((new_width, int(new_height))).convert('L')

        pixels = img.getdata()
        new_pixels = [chars[pixel // 25] for pixel in pixels]
        new_pixels = ''.join(new_pixels)
        
        new_pixels_count = len(new_pixels)
        ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
        ascii_image = "\n".join(ascii_image)
        df.loc[i] = {"messages": [{"role": "user", "content": f"ASCII {label}"}, {"role": "assistant", "content": f"ASCII {label} : {ascii_image}"}]}
        
    dfs.append(df)
    
final_df = pd.concat(dfs)

df_train=final_df.sample(frac=0.95, random_state=42)
df_eval=final_df.drop(df_train.index)

df_train.to_json("multi_train.jsonl", orient="records", lines=True)
df_eval.to_json("multi_eval.jsonl", orient="records", lines=True)
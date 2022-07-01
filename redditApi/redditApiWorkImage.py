import gpt_2_simple as gpt2_simple
import tensorflow as tf
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import praw
import random
import gpt_2_simple as gpt2_simple
from datetime import datetime
from selenium import webdriver
import time
import tkinter as tk
import os



reddit = praw.Reddit(
    client_id = "YMqvij20Fyf7EHf5ddtiAA",
    client_secret = "giOJJdo8UuusPovme_6f7DhkABeBlw",
    username = "BanMe12345",
    password= "19331945",
    user_agent = "Junk"
)

##subreddit = reddit.subreddit("AskReddit");
##hot_python = subreddit.hot(limit=1000);
##for submission in hot_python:
##  print(submission.title);


def get_top_title():
  global sub_name
  sub_name = input_box.get("1.0", "end-1c")
  global title_list
  title_list = []
  print("test1")
  for submission in reddit.subreddit(sub_name).top(limit=10):
  #for submission in reddit.subreddit(sub_name).top(limit=10):
    title_list.append(submission.title)
    print(submission.title)
    time.sleep(2)
    file = os.open('junk.txt', os.O_RDWR|os.O_CREAT)
    for i in range(0,len(title_list)-1):
      os.write(file,title_list[i].encode()+"\n".encode())
    os.close(file)  
  return title_list

window = tk.Tk()
greeting = tk.Label(text="Welcome to reddit bot")
greeting.pack()

global input_box
input_box = tk.Text(height=2, width=19)
input_box.pack()






def post_shit():
    SubReddit = str("r/" + sub_name)
    print(SubReddit)
    subreddit = reddit.subreddit(SubReddit)
    image = os.open('Picture.png', os.O_RDWR)
    subreddit.submit_image(c, image)
    



def generate_text():
    gpt2_simple.download_gpt2(model_name='124M')
    tf.compat.v1.reset_default_graph() # https://stackoverflow.com/questions/40782271/attributeerror-module-tensorflow-has-no-attribute-reset-default-graph
    sess = gpt2_simple.start_tf_sess() #


    # gpt2_simple.finetune(sess, dataset="junk.txt", steps=500, model_name='124M', sample_every=200, save_every=500, print_every=10, restore_from='fresh')
    gpt2_simple.finetune(sess, dataset="junk.txt", steps=10, restore_from='latest')
    # This will take time. ignore the warning
    gpt2_simple.generate(sess, run_name='run1', length=100,destination_path="junk_writer.txt")
    text = os.open('junk.txt', os.O_RDWR)
    return text

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
s = open("leftists_soup.txt", encoding="utf8")
a_string = s.read()
split_string = a_string. split("\n")
print(split_string)
c = split_string[random.randint(1,len(split_string) - 1)]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#




def Image_draw():
    image = Image.open("Picture.png")
    font_type = ImageFont.truetype("arial.ttf", 64)
    draw = ImageDraw.Draw(image)
    draw.text(xy=(random.randint(0,900), random.randint(0,100)), text= c, fill=(random.randint(0, 255), random.randint(0,255), random.randint(0,255)), font=font_type)
    image.save("Picture.png")
    ##image.show();



def main():
    time.sleep(2)
    print('test4')
    input_box.delete("1.0", "end-1c")
    get_top_title_gui_button = tk.Button(
    text="click me to scrap a subreddit's top post titles",
    width=35,
    height=18,
    bg="grey",
    fg="yellow",
    command=lambda: get_top_title()
)
    get_top_title_gui_button.pack(side='left')

    post_shit_gui_button = tk.Button(
    text="Click me to post shit",
    width=35,
    height=18,
    bg="grey",
    fg="yellow",
    command=lambda: post_shit()
)
    post_shit_gui_button.pack(side='left')
  
    train_model_gui_button = tk.Button(
    text = "Train Model",
    width=35,
    height=18,
    bg="grey",
    fg="yellow",
    command=lambda: generate_text(sub_name, "junk.txt")
  )
    train_model_gui_button.pack(side='left')
    ##Generate_thingy();
    Image_draw()

    image = "Picture.png"

    ##subreddit.submit_image(c,image);
    


main()
window.mainloop()
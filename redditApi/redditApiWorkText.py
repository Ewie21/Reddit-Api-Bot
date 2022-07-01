import os
import json
from matplotlib import image
import numpy as np
import praw
import time
import tkinter as tk
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.models import Sequential
import random as rd
import gpt_2_simple as gpt2_simple
from datetime import datetime
#from google.colab import files, drive
def generate_text(seed_text_file):
  #gpt2_simple.download_gpt2(model_name='124M') # Will take sometime....
  #gpt2_simple.mount_gdrive()
  tf.compat.v1.reset_default_graph() # https://stackoverflow.com/questions/40782271/attributeerror-module-tensorflow-has-no-attribute-reset-default-graph
  sess = gpt2_simple.start_tf_sess() # 
  # gpt2_simple.finetune(sess, dataset="junk.txt", steps=500, model_name='124M', sample_every=200, save_every=500, print_every=10, restore_from='fresh')
  #use this to generate leftists soup gpt2_simple.finetune(sess, dataset="CM.txt", steps=60, restore_from='latest')
  gpt2_simple.finetune(sess, dataset=seed_text_file, steps=10, restore_from='latest')#use this in the final reddit project
  # This will take time. ignore all warning
  #gpt2_simple.copy_checkpoint_to_gdrive(run_name='run1')
  gpt2_simple.generate(sess, run_name='run1', length=10,destination_path="junk_writer.txt")
  #drive.mount('/content/drive')
  return "junk_writer.txt"


reddit = praw.Reddit(
    client_id = "29F_gIYqb6jhqjOiCSWRpA",
    client_secret = "0WLW1kOXMnrOZEt7yj9vsimQsW5e0w",
    username = "JunkScrapper",
    password= "19141918",
    user_agent = "Junkkkk"
)
#sub_name = ""


def get_top_title():
  global sub_name
  sub_name = input_box.get("1.0", "end-1c")
  print(sub_name)
  global title_list
  title_list = []
  print("test1")
  for submission in reddit.subreddit(sub_name).controversial(limit=10):
    print("test5")
  #for submission in reddit.subreddit(sub_name).top(limit=10):
    title_list.append(submission.title)
    print(submission.title)
    time.sleep(2)
  file = os.open('junk.txt', os.O_RDWR|os.O_CREAT)
  for i in range(0,len(title_list)-1):
    os.write(file,title_list[i].encode()+"\n".encode())
  os.close(file)  
  return title_list

def post_shit(sub_name):
  subreddit = reddit.subreddit(sub_name)
  title = str(os.open("junk_writer.txt", os.O_RDWR|os.O_CREAT)).split('\n')
  content_list = title
  subreddit.submit(title[0],selftext=content_list[0])
  return print("Posted")

window = tk.Tk()
greeting = tk.Label(text="Welcome to reddit bot")
greeting.pack()

global input_box
input_box = tk.Text(height=2, width=19)
input_box.pack()



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
  command=lambda: post_shit(sub_name)
)
  post_shit_gui_button.pack(side='left')
  
  train_model_gui_button = tk.Button(
    text = "Train Model",
    width=35,
    height=18,
    bg="grey",
    fg="yellow",
    command=lambda: generate_text('junk.txt')
  )
  train_model_gui_button.pack(side='left')
  
  #entry = tk.Entry(root, textvariable = sub_name).grid(row=0, column=1) #entry textbox
  #entry.pack()
main()

window.mainloop()
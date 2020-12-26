#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os
import shutil

dir1 = "/home/optimal/Documents/wallpapers/"
dir2 = "/home/optimal/Documents/"
dir3 = "/home/optimal/Documents/python/"
dir4 = "/home/optimal/Documents/zip/"
dir5 = "/home/optimal/Documents/sh/"
dir6 = "/home/optimal/Documents/deb/"
dir7 = "/home/optimal/Documents/other files/"





def moveto(dst):
    return lambda src: shutil.move(src, dst)

action = {
    'pdf': moveto(dir2),
    'docx': moveto(dir2),
    'exe': moveto(dir2),
    'jpg': moveto(dir1),
    'torrent': os.remove,
        'png': moveto(dir1),

            'py': moveto(dir3),
            'zip': moveto(dir4),
                'sh': moveto(dir5),
                'deb': moveto(dir6),

        'png': moveto(dir1),
    
        'jpeg': moveto(dir1),



}

src_dir = '/home/optimal/Downloads'
for file in os.listdir(src_dir):
    ext = os.path.splitext(file)[1][1:]
    if ext in action:
        action[ext](os.path.join(src_dir, file))


# In[ ]:





# In[ ]:





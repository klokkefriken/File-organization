#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os
import shutil

dir1 = "//"
dir2 = "/"
dir3 = "//"
dir4 = "//"
dir5 = "//"
dir6 = "//"
dir7 = "//"





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





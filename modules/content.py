import os
from typing import Dict, List

import markdown2

#Returns the 2 .md files in each page dir
def get_content(dir: str) -> Dict:
    #Markdown extensions
    extras = {
        "html-classes" : None,
        "fenced-code-blocks": None,
        "break-on-newline" : None,
    }
    #Check if paths exist
    if ((os.path.exists(f"{dir}/leftside.md") and os.path.exists(f"{dir}/rightside.md")) == False):
        return {
            "left": "<span>Content not found!</span>", 
            "right": "<span>Content not found!</span>"
        }

    
    #extract md files
    content = {} 

    with open(f"{dir}/leftside.md", 'r') as file:
        content["left"] = markdown2.markdown(file.read(), extras=extras)
        file.close()

    with open(f"{dir}/rightside.md", 'r') as file:
        content["right"] = markdown2.markdown(file.read(), extras=extras)
        file.close()

    return content 

#Return all directories within a directory 
def get_dirs(dir: str) -> List:
    if (os.path.exists(dir) == False):
        return []
    
    dirs = []
    for d in os.listdir(dir):
        if (os.path.isdir(f"{dir}/{d}") and (d != "media")):
            dirs.append(d)

    return dirs


#Recursive method to explore all directories
def deep_ls(dir: str, dirlist: list) -> List:
    if (os.path.exists(dir) == False):
        return dirlist

    for d in os.listdir(dir):
        if (os.path.isdir(f"{dir}/{d}") and (d != "media")):
            print(d)
            dirlist.append(f"{dir}/{d}")
            deep_ls(f"{dir}/{d}", dirlist)

    return dirlist


def get_deep_ls(dir: str) -> List:
    if (os.path.exists(dir) == False):
        print(dir)
        return []

    return deep_ls(dir, [dir])










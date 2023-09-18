import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
scripts_dir = os.path.join(current_dir, 'scripts')
sys.path.append(scripts_dir)

from scripts.lsb import *
from scripts.makeqrto01text import *
from scripts.msb import *
from scripts.multibase import *
from scripts.rgbnumber import *
from scripts.weakpasszip import *
from scripts.pretreatment import *
import random
import base64

banner = """
    烂题生成器
    当前模块数: 6
"""

cengshu = input('Please enter the number of layers you want to "tao"> ')
if(cengshu.isdigit()):
    secret_text = input('Please enter the flag you want to set> ').encode()
    selectable_modules = ['lsb', 'msb', 'rgbnumber', 'makeqrto01text', 'multibase', 'weakpasszip']
    print("waiting...")
    pretreatment()
    for _ in range(int(cengshu)):
        choice = random.choice(selectable_modules)
        secret_text = eval(choice + '(secret_text)')
    print("Here is the base64-encoded attachment")
    print(base64.b64encode(secret_text))
    print("done")
    
else:
    print("Invalid input")
    exit()
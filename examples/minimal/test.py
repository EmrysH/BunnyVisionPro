

import os,sys

print("path:",sys.path)

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.insert(0,os.path.split(rootPath)[0])
print("path_updated:",sys.path)

from bunny_teleop.test_improt import BimanualAlignmentMode

print("ok")

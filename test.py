import fileblock as fb
from fileblock import Block
from fileblock.Directory import Directory, deep_maker
from fileblock.btype import FILE
import json

block = Block("./")
# code_file = Block("./fileblock/__version__.py")
# block.append(code_file)
print(block.children)
leaves = block.leaves
pys = leaves.extension_filter("py")
print(pys)



# import os

# for i in os.walk("./"):
#     print(i)
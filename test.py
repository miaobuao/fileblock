import fileblock as fb
from fileblock import Block
from fileblock.Directory import Directory, deep_maker
from fileblock.btype import FILE
import json

block = Block("./")
print(block.children)
leaves = block.leaves
pys = leaves.extension_filter("py")
print(pys)
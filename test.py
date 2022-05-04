from posixpath import abspath
from site import abs_paths
import fileblock as fb
from fileblock import Block
from fileblock.Children import Children
from fileblock.btype import FILE
import json

block = Block("./")
print(block.leaves.pop([1, [2, 3]]))
# root = fb.Block("./")
# print(root.children.map(f))
# print(fb.unfold(1, 2, [4], [6, [7, [10]]]))
# print(root.children.to_json("./ceshi.json", file_only=True))
# print(Children([root.children, Children([root.children]), root.children]).unfold())
# root.children >> 2
# print(fb.file_filter(root.children))
# test_block = Block("./111")
# print(test_block.children)
# fb.remove(test_block)
# print(fb.get_path(root.children))
# tp = root.append("a/c/b", fb.FILE)
# tp.copyTo(Block("./test_dir"))
# print(FILE == FILE)
# print(tp.isfile)
# print(fb.make_children(root.children, [root.children]).unfold())
# print(root.search("__", fb.FILE))
# Block("./a").copyTo(Block("./test_dir"))
# print(fb.unfold([1, 2, ], 2))
# print(tp.leaves)

# children = root.leaves
# print(children.paths)
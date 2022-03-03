import fileblock as fb
from fileblock import Block
from fileblock.Children import Children
from fileblock.btype import FILE
import json

json.dump
root = fb.Block("./")
# print(root.children.to_json("./ceshi.json", file_only=True))
# print(Children([root.children, root.children]).unfold())
# tp = root.append("a/c/b", fb.FILE)
# tp.copyTo(Block("./test_dir"))
# print(FILE == FILE)
# print(tp.isfile)
print(fb.make_children(root.children, [root.children]).unfold())
# Block("./a").copyTo(Block("./test_dir"))

# print(tp.leaves)

# children = root.leaves
# print(children.paths)
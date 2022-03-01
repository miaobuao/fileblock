import fileblock as fb
from fileblock import Block

root = fb.Block("./")
tp = root.append("a/c/b", fb.FILE)
tp.copyTo(Block("./test_dir"))

print(tp.isfile)

Block("./a").copyTo(Block("./test_dir"))

print(tp.leaves)

children = root.leaves
print(children.paths)


# File Block

[Programe](https://github.com/miaobuao/fileblock)

<center>

<h3>简化文件处理</h3>

*simplify file processing*

</center>

## Installing from pip

```shell
pip install fileblock
```

## How to use

```python
import fileblock as fb
from fileblock import Block, Children
```

### Block

#### Create Block

```python
file_block = Block("./") # 创建一个Block
```

| 参数 | 类型   | 返回值 | 描述                  |
| ---- | ------ | ------ | --------------------- |
| name | string | None   | 创建 block 的逻辑位置 |

<article class="message is-primary">
  <div class="message-header">
    Tips
  </div>
  <div class="message-body">
  <em>path</em>不一定是真实存在的文件或者文件夹路径
  </div>
</article>

#### block.sub_block(path)

| 参数 | 类型   | 返回值 | 描述                    |
| ---- | ------ | ------ | -----------------------|
| path | string | Block  | 相对于 block 的相对路径 |

#### block.append(name, type=FILE)

| 参数 | 类型   | 描述                    |
| ---- | ------ | -----------------------|
| name | string   | 相对于 block 的相对路径 |
| type | btype.FILE / btype.DIR | 需要添加的节点类型 |

返回新生成节点的Block对象


<article class="message is-primary">
  <div class="message-header">
    Tips
  </div>
  <div class="message-body">
            当type == FILE时，若name形如x1/x2, 则会新建x1文件夹，返回的是x2的Block对象，而不是x1
  </div>
</article>

#### block.join_path(path)

| 参数 | 类型   |描述                    |
| ---- | ------ |-----------------------|
| path | string| 需要拼接的文件/文件夹路径 |

返回拼接后的路径

#### block.remove()

说明：

如果该 block 对象是真实存在的文件/文件夹, 则从磁盘上永久删除该文件/文件夹

#### block.moveTo(target)

| 参数 | 类型   |描述                    |
| ---- | ------ |-----------------------|
| target | Block| 一个类型为Dir的Block对象|

如果block存在，则会把其中的文件与文件夹移动到target对应的文件夹内

#### block.copyTo(target: Block)

| 参数 | 类型   |描述                    |
| ---- | ------ |-----------------------|
| target | Block| 一个类型为Dir的Block对象|

把 Block 及其 Children 都拷贝如 target 中

#### block.cut(\*rates:int|float)->list[Children]

| 参数 | 类型   |描述                    |
| ---- | ------ |-----------------------|
| rates | int/float| 需要划分的比重|

举个例子🌰

rates为(x_1, x_2, x_3, x_4)时，会把block的children划分成4份，

令 m = sum(rates), 那么第i份占 x_i / m

#### block.get_file_contents() -> bytes

如果block时文件，则返回该文件的bytes内容

#### block.leaves

Block文件树的叶子节点构成的[Children](#children)集合

#### block.isfile -> bool

当block存在，且为文件时等于True

#### block.isdir -> bool

当block存在，且为文件夹时为True

#### block.exists -> bool

当block存在时为True

#### block.children -> Children[Block]

返回block对象包含的子文件与子文件夹构成的[Children](#children)集合

#### block.btype ->  __FILE | __DIR | None

返回该Block对象的类型 ```FILE``` | ```DIR``` | ```None```
### Children

*Children类继承自list*
#### children.paths -> list[str]

返回所有Block的绝对路径

#### children.shuffle -> Children:

返回打乱顺序的Children，不改变本身内容

#### 加法

```python
c1 = Children()
c2 = Children()
c3 = c1 + c2 # type(c3) == Children
```

## TODO LIST

- [ ] save & load
  - [ ] to_csv
  - [ ] to_json
  - [ ] to_pkl
  - [ ] from_csv
  - [ ] from_json
  - [ ] from_pkl

## License

[Apache 2.0](https://github.com/miaobuao/fileblock/blob/main/LICENSE)



<style>
.message .is-primary {
  background-color: #ebfffc;
}
.message {
  background-color: #f5f5f5;
  border-radius: .375em;
  font-size: 1rem;
}
body {
  font-size: 1em;
  font-weight: 400;
  line-height: 1.5;
}
body, button{
  font-family: BlinkMacSystemFont,-apple-system,"Segoe UI",Roboto,Oxygen,Ubuntu,Cantarell,"Fira Sans","Droid Sans","Helvetica Neue",Helvetica,Arial,sans-serif;
}
:root {
  --newsletter-strip-size: 16px;
  --newsletter-border-size: 1.5rem;
}
html {
  font-size: 16px;
  text-rendering: optimizeLegibility;
  -webkit-text-size-adjust: 100%;
  -moz-text-size-adjust: 100%;
}
.message.is-primary .message-header {
  background-color: #00d1b2;
  color: #fff;
}
.message-header {
  align-items: center;
  background-color: #4a4a4a;
  border-radius: .375em .375em 0 0;
  color: #fff;
  display: flex;
  font-weight: 700;
  justify-content: space-between;
  line-height: 1.25;
  padding: .75em 1em;
  position: relative;
}
.message.is-primary .message-body {
  border-color: #00d1b2;
  color: #00947e;
}
.message-header + .message-body {
  border-width: 0;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}
.message-body {
  border-color: #dbdbdb;
  border-radius: .375em;
  border-top-left-radius: 0.375em;
  border-top-right-radius: 0.375em;
  border-style: solid;
  border-width: 0 0 0 4px;
  color: #4a4a4a;
  padding: 1.25em 1.5em;
}
</style>
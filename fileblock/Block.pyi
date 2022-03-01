from os.path import split, splitext, isfile, exists, join, isdir, abspath
from os import listdir, makedirs, mkdir, remove, rmdir
from .Children import Children
from .btype import FILE, DIR
import shutil

class Block:

    def __init__(self, path: str) -> None:
        '''
            @parameter path - 文件/文件夹路径
        '''
        pass
    
    def sub_block(self, path: str)->Block:
        '''
            @parameter path - 子文件或子文件夹的相对路径
            @returns
                子文件/子文件夹的Block对象
        '''
        pass
    
    def append(self, name, type=FILE)->Block:
        '''
            往block中新增一个文件/文件夹

            TIPS:
                当type == FILE时，若name形如x1/x2, 则会新建x1文件夹，返回的是x2的Block对象，而不是x1
        '''
        pass

    def join_path(self, path: str)->str:
        '''
            @parameter path - 需要拼接的文件/文件夹路径
            @returns:
                拼接后的路径
        '''
        pass
    
    def remove(self)->None:
        '''
             如果该block对象是真实存在的文件/文件夹, 则从磁盘上永久删除该文件/文件夹
        '''
        pass

    def moveTo(self, target)->None:
        pass
    
    def copyTo(self, target: Block)->None:
        '''
            把Block及其Children都拷贝如target中
        '''
        pass

    
    @property
    def leaves(self) -> Children:
        pass

    def cut(self, *rates:int|float)->list[Children]:
        '''
            切割文件夹内的文件块
            @parameter - rates 分割比例，可以是整数，也可以是浮点数
        '''
        pass
    
    def get_file_contents(self)->bytes:
        '''
            如果Block是文件，则返回文件的bytes
        '''
        pass

    @property
    def isfile(self) -> bool:
        '''
            block类型是文件则返回True
        '''
        pass

    @property
    def isdir(self) -> bool:
        '''
            block类型是文件夹则返回True
        '''
        pass
    
    @property
    def exists(self) -> bool:
        '''
            该block是否存在
        '''
        pass
    
    @property
    def children(self) -> Children[Block]:
        pass

    
    @property
    def btype(self):
        pass
    
    @property
    def abstract(self):
        pass


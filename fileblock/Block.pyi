from os.path import split, splitext, isfile, exists, join, isdir, abspath
from os import listdir, makedirs, mkdir, remove, rmdir
from .Directory import Directory
from .btype import FILE, DIR
import shutil
from .Abstrcat import Abstract
class Block:

    def __init__(self, path: str):
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

    def moveTo(self, target: Block|str)->Block:
        pass
    
    def copyTo(self, target: Block|str)->Block:
        '''
            把Block及其Children都拷贝如target中
        '''
        pass

    def search(self, name, type=None)->Directory:
        '''
            在block内进行搜索，返回所有匹配的文件/文件夹
            
            可选参数type的值应为 fileblock.FILE 或 fileblock.DIR
        '''
        pass

    def cut(self, *rates:int|float)->Directory[Directory]:
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
    
    def enter(self, path)->Block:...

    @property
    def children(self) -> Directory:...

    @property
    def path(self)->str:...
    
    @property
    def leaves(self)->Directory:...

    @property
    def abspath(self)->str:...
    
    @property
    def directory(self)->str:...
    
    @property
    def file_full_name(self)->str:...
    
    @property
    def filename(self)->str:...
    
    @property
    def extension(self)->str:...

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
    def btype(self):
        pass
    
    @property
    def abstract(self, force_abspath=False)->Abstract:
        '''
            返回一个Abstract对象,包含了该Block的基本文件信息
        '''
        pass

    @property
    def super_dir_name(self)->str:
        pass

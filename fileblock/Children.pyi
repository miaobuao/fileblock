
class Children(list):

    def map(self, fn)->Children:
        pass
        
    def to_json(self, path: str, file_only=False, dir_only=False, force_abspath = False, indent=None)->None:
        """注：若file_only 和 dir_only 同时为 True 则 全都输出."""
        pass
        
    def unfold(self)->Children:
        pass

    @staticmethod
    def make(*child)->Children:
        pass

    @property
    def abspaths(self)->Children:
        pass
    
    def shuffle(self)->Children:
        pass
    
    @property
    def super_dir_names(self)->Children:
        pass

    def __add__(self, x)->Children:
        pass
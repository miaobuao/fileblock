class Children(list):
    
    @property
    def paths(self) -> list[str]:
        '''
            返回所有Block的绝对路径
        '''
        pass

    @property
    def shuffle(self) ->Children:
        '''
        返回打乱顺序的Children，不改变本身内容
        '''
        pass

    def __add__(self, x: Children) -> Children:
        pass
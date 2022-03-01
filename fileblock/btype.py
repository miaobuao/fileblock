class __BaseType:
    value = None
    def __repr__(self) -> str:
        return self.__str__()

class __DIR(__BaseType):
    value = 1
    def __str__(self) -> str:
        return "dir"

class __FILE(__BaseType):
    value = 0
    def __str__(self) -> str:
        return "file"

FILE = __FILE()
DIR = __DIR()
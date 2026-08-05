from .storage import JSONStorage

class MemoryManager:
    def __init__(self):
        self.storage=JSONStorage()
        self.data=self.storage.load()
    def set(self,key,value,namespace="shared"):
        self.data.setdefault(namespace,{})[key]=value
        self.storage.save(self.data)
    def get(self,key,namespace="shared",default=None):
        return self.data.get(namespace,{}).get(key,default)

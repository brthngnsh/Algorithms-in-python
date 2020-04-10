#This file contains only Stack initialization
#it implements stack eith max API
import collections
class Stack :
    ElementWithCachedMax = collections.namedtuple('ElementWithCachedMax',('element','max'))

    def __init__(self, *args, **kwargs):
        self._element_with_cached_max = []
    
    def empty(self) :
        return len(_element_with_cached_max) == 0

    def max(self) :
        if self.empty() :
            raise IndexError('Index Error :: Empty List')
        return self._element_with_cached_max[-1].max
    
    def pop(self) :
        if self.empty() :
            raise IndexError('pop() : Empty stack')
        return self._element_with_cached_max.pop().element

    def push(self,x):
        self._element_with_cached_max.append(self._element_with_cached_max(x,x if self.empty() else max(x,self.max())))


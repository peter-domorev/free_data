from abc import ABC, abstractmethod

class ICommand(ABC):
    
    @property
    @abstractmethod
    def helpme_syntax(self):
        pass
    
    @property
    @abstractmethod
    def helpme_guide(self):
        pass
    
    
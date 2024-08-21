from abc import ABC,abstractmethod

class Builder(ABC):
    
    
    @abstractmethod
    def set_seats():
        pass

    @abstractmethod
    def set_engine():
        pass

    @abstractmethod
    def set_gps():
        pass

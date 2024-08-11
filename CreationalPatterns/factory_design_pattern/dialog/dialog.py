from abc import ABC, abstractmethod

class Dialog(ABC):

    def render(self):
        rendering = self.create_button()
        return rendering

    @abstractmethod
    def create_button(slef):
        pass


from abc import ABC,abstractmethod

class StudentServices(ABC):

    @abstractmethod
    def add_studentinfo(self):
        pass

    @abstractmethod
    def display_studentinfo(self):
        pass


    @abstractmethod
    def update_studentinfo(self):
        pass


    @abstractmethod
    def remove_student(self):
        pass
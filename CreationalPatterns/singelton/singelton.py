
class Singelton:
    _instance = None

    def __init__(self):
        raise Exception ("you can not call this contructor, use get_instace() to create an object")
    

    @classmethod
    def get_instance(cls):
        cls._instance = cls.__new__(cls) if (cls._instance == None) else cls._instance  
        # if cls._instance == None:
        #     cls._instance = cls.__new__(cls)
        # return cls._instance
        
        



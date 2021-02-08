class Singleton(type):
    _instances = {}


    def __call__(cls, *args, **kwargs):
        if not cls in cls._instances:
            new_instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = new_instance
        
        return cls._instances[cls]

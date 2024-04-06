class TaskInMemoryDatabase:
    repository: list = []
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(TaskInMemoryDatabase, cls).__new__(cls)
            cls.__instance.__initialized = False
        return cls.__instance

    def __init__(self):
        if self.__initialized:
            return
        self.__initialized = True


TaskInMemoryDatabase()

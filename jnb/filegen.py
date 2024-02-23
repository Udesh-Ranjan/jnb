class FileGen:
    def __init__(self):
        pass

    @staticmethod
    def create_file(name, content=None):
        with open(name, "w") as file:
            if content is not None:
                file.write(content)

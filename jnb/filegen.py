class FileGen:
    """
    A class that provides methods for creating and managing files.

     Example usage:
     >>> file_gen = FileGen()
     >>> file_gen.create_file("my_file.txt", "This is the content of my file.")
     >>> file_gen.create_files(["file1.txt", "file2.txt"], "Common content.")

    Methods:
        - create_file(name: str, content=str | None = None) -> None
            Creates a file with the given name and writes content to it.
        - create_files(file_names: List[str], content=str | None = None) -> None
            Creates multiple files with the given names and writes content to each.
    """

    def __init__(self):
        """
        Initializes the FileGen object, preparing it for file creation
        """
        pass

    @staticmethod
    def create_file(name, content=None):
        """
        Creates a file with the given name and writes the specified content to it.

        :param name: The name of the file to be created.
        :type name: str
        :param content: The content to be written to the file, defaults to None.
        :type content: str, optional
        :raises IOError: If an error occurs during file creation.
        :return: None
        """

        with open(name, "w") as file:
            if content is not None:
                file.write(content)

    @staticmethod
    def create_files(file_names, content) -> None:
        """
        Creates multiple files with the given names and writes the specified content to each file.

        :param file_names: A list of names of the files to be created.
        :type file_names: list of str
        :param content: The content to be written to each of the files,
        defaults to None.
        :type content: str, optional
        :raises IOError: If an error occurs during file creation.
        :return: None
        """

        for file_name in file_names:
            FileGen.create_file(file_name, content)

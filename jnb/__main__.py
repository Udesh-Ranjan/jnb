"""
This is the main module of the `jnb` package. The `jnb` package is used for creating new Jupyter Notebook files.

The module imports necessary classes from the `jnb` package:
    - `FileGen` for creating files,
    - `NBMeta` for getting notebook metadata and content,
    - `ParseData` for parsing command-line arguments.

The `main` function is the entry point of the program. It parses the command-line arguments to get the names of the
notebooks to be created. Then it creates the notebooks with the default content.

This script is executed when the module is run directly.

Example:
    $ python -m jnb --create my_notebook1.ipynb my_notebook2.ipynb
        This will create `my_notebook1.ipynb` and `my_notebook2.ipynb` in the current directory with
        the default content.

    $ python -m jnb --create c:/users/.../my_notebook1.ipynb c:/users/.../my_notebook2.ipynb
        Creates `my_notebook1.ipynb` and `my_notebook2.ipynb` notebooks in the specified path.

    $ python -m jnb -h
        Displays the usage and help message and then exits.

"""

from jnb.filegen import FileGen
from jnb.nbmeta import NBMeta
from jnb.parsedata import ParseData


def main():
    args = ParseData.parse_data()

    FileGen.create_files(args.create,
                         NBMeta.get_notebook_content())


if __name__ == "__main__":
    main()

import tempfile

from jnb.filegen import FileGen
from jnb.parsedata import ParseData
from jnb.nbmeta import NBMeta
import io
import os
import pytest


def test_help_documentation_raises_system_exit_error():
    """
    Test if the help documentation raises a SystemExit error.

    This test case checks if calling the help documentation with '-h' argument raises a SystemExit error.
    """

    with pytest.raises(SystemExit) as error:
        parser = ParseData.get_parser()
        parser.parse_args(['-h'])


def test_help_documentation_msg_is_not_empty():
    """
    Test if the help documentation message is not empty.

    This test case checks if the help documentation message is not empty when printed.
    """

    output_data = io.StringIO()
    parser = ParseData.get_parser()
    parser.print_help(file=output_data)
    assert output_data.getvalue()


def test_creating_multiple_files_using_jnb_command():
    """
    Test creating multiple files using the jnb command.

    This test case checks if multiple files can be created using the jnb command and if the content of the files is
    correct.
    """

    with tempfile.TemporaryDirectory() as dir_name:
        files_path = [os.path.join(dir_name,
                                   f"file{1}.ipynb") for i in range(3)]

        jnb_command = ["-c", *files_path]
        parser = ParseData.get_parser()
        args = parser.parse_args(jnb_command)

        file_names = args.create
        FileGen.create_files(file_names,
                             NBMeta.get_notebook_content())

        for file_name in file_names:
            with open(file_name, 'r') as file:
                assert file.read() == NBMeta.get_notebook_content()


def test_notebook_content_is_correct():
    """
    Test if the notebook content is correct.

    This test case checks if the content of a notebook file is correct after it has been written to.
    """

    with tempfile.NamedTemporaryFile(suffix='.ipynb') as file:
        file.write(bytes(NBMeta.get_notebook_content(), 'utf-8'))
        file.seek(0)
        assert file.read().decode('utf-8') == NBMeta.get_notebook_content()


def test_passing_invalid_command_line_args():
    """
    Test passing invalid command line arguments.

    This test case checks if passing invalid command line arguments raises a SystemExit error.
    """

    with pytest.raises(SystemExit) as error:
        parser = ParseData.get_parser()
        parser.parse_args(['-p'])
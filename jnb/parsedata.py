import argparse


class ParseData:
    """
    The ParseData class provides methods for parsing command-line arguments.

    Methods:
        - get_parser(): Returns an argparse.ArgumentParser object for parsing command-line arguments.
        - parse_data(): Parses the command-line arguments and returns argparse.Namespace which
         denotes the parsed data.
    """

    def __init__(self):
        """
        Initialized ParseData object.
        """
        pass

    @staticmethod
    def get_parser():
        """
        Creates and returns an argparse.ArgumentParser object for parsing command-line arguments.

        :return: An ArgumentParser object for parsing command-line arguments.
        :rtype: argparse.ArgumentParser
        """

        parser = argparse.ArgumentParser(prog='JNB')
        parser.add_argument('-c', '--create',
                            action='extend',
                            help='New Jupyter Notebooks to be created',
                            nargs='+',
                            type=str,
                            required=True)
        return parser

    @staticmethod
    def parse_data():
        """
        Parses the command-line arguments and performs instruction as specified by the command line arguments.

        :return: The parsed command-line arguments.
        :rtype: argparse.Namespace
        """

        parser = ParseData.get_parser()
        args = parser.parse_args()
        return args

import nbformat


class NBMeta:
    """
    NBMeta class provides methods for getting Jupyter Notebook metadata and content.

    Methods:
        - get_nbformat(): Returns the current notebook format version.
        - get_nbformat_minor(): Returns the current minor notebook format version.
        - get_notebook_content(): Returns the notebook content in string format.
    """

    def __init__(self):
        """
        Initializes the NBMeta object.
        """
        pass

    @staticmethod
    def get_nbformat():
        """
        Gets the current notebook format version.

        :return: The current notebook format version.
        :rtype: int
        """

        return nbformat.current_nbformat

    @staticmethod
    def get_nbformat_minor():
        """
        Gets the current minor notebook format version.

        :return: The current minor notebook format version.
        :rtype: int
        """

        return nbformat.current_nbformat_minor

    @staticmethod
    def get_notebook_content():
        """
        Gets the notebook content in string format.

        :return: The notebook content in string format.
        :rtype: str
        """

        return (
                '{\n'
                ' "cells": [],\n'
                ' "metadata": {},\n'
                ' "nbformat": ' + str(NBMeta.get_nbformat()) + ',\n'
                ' "nbformat_minor": ' + str(NBMeta.get_nbformat_minor()) + '\n'
                '}'
        )

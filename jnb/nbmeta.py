import nbformat


class NbMeta:
    def __int__(self):
        pass

    @staticmethod
    def get_nbformat():
        return nbformat.current_nbformat

    @staticmethod
    def get_nbformat_minor():
        return nbformat.current_nbformat_minor

    @staticmethod
    def get_notebook_content():
        return """
{
 "cells": [],
 "metadata": {},""" + f"""
 "nbformat": {NbMeta.get_nbformat()},
 "nbformat_minor": {NbMeta.get_nbformat_minor()}
""" + '}'


# print(Manager.get_notebook_content())

# with open(r"C:\Users\devpa\Documents\DevLog\ScalerClass\DataVisualization\KuldeepLectures\test2.ipynb", 'w') as file:
#     file.write(Manager.get_notebook_content())
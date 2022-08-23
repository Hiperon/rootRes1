"""Package with all modules I wrote for the purpose of this task

This package has three modules:
    * rootf - Functions and class for importing ond operating on root datatype
    * rstats - Stats for data got from root datatype
    * vis - Module for basic visualization of data"""
# Code from StackOverflow, need to understand it and make it work, it should automate putting packages in __all__
# from os.path import dirname, basename, isfile, join
# import glob
# modules = glob.glob(join(dirname(__file__), "*.py"))
# __all__ = [basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]

__all__ =['rootf', 'rstat', 'vis']

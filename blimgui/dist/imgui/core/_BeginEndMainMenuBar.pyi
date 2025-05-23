# encoding: utf-8
# module imgui.core
# from C:\Users\justi\AppData\Local\Programs\Python\Python37-32\lib\site-packages\imgui\core.cp37-win32.pyd
# by generator 1.147
"""
.. todo:: consider inlining every occurence of ``_cast_args_ImVecX`` (profile)
.. todo: verify mem safety of char* variables and check for leaks
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import warnings as warnings # C:\Users\justi\AppData\Local\Programs\Python\Python37-32\lib\warnings.py
from itertools import izip_longest


from .object import object

class _BeginEndMainMenuBar(object):
    """
    Return value of :func:`begin_main_menu_bar` exposing ``opened`` (displayed) boolean attribute.
        See :func:`begin_main_menu_bar` for an explanation and examples.
    
        Can be used as a context manager (in a ``with`` statement) to automatically call :func:`end_main_menu_bar`
        (if necessary) to end the main menu bar created with :func:`begin_main_menu_bar` when the block ends,
        even if an exception is raised.
    
        This class is not intended to be instantiated by the user (thus the `_` name prefix).
        It should be obtained as the return value of the :func:`begin_main_menu_bar` function.
    """
    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __enter__(self): # real signature unknown; restored from __doc__
        """ _BeginEndMainMenuBar.__enter__(self) """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __exit__(self, exc_type, exc_val, exc_tb): # real signature unknown; restored from __doc__
        """ _BeginEndMainMenuBar.__exit__(self, exc_type, exc_val, exc_tb) """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ _BeginEndMainMenuBar.__reduce_cython__(self) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ _BeginEndMainMenuBar.__setstate_cython__(self, __pyx_state) """
        pass

    opened = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __hash__ = None



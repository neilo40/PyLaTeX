# -*- coding: utf-8 -*-
"""
This module implements the base LaTeX object.

..  :copyright: (c) 2014 by Jelte Fennema.
    :license: MIT, see License for more details.
"""

from ordered_set import OrderedSet
from pylatex.utils import dumps_list
from abc import abstractmethod, ABCMeta


class LatexObject(metaclass=ABCMeta):

    """The class that every other LaTeX class is a subclass of.

    This class implements the main methods that every LaTeX object needs. For
    conversion to LaTeX formatted strings it implements the dumps, dump and
    generate_tex methods. It also provides the methods that can be used to
    represent the packages required by the LatexObject.


    Args
    ----
    packages: :class:`list` of `~.Package` instances
        Packages that are required by this LaTeX class.

    """

    def __init__(self, packages=None):

        if packages is None:
            packages = []

        self.packages = OrderedSet(packages)

    @abstractmethod
    def dumps(self):
        """Represent the class as a string in LaTeX syntax.

        This method should be implemented by any class that subclasses this
        class.
        """

    def dump(self, file_w):
        """Write the LaTeX representation of the class to a file.

        Args
        ----
        file_w: io.TextIOBase
            The file object in which to save the data

        """

        file_w.write(self.dumps())

    def generate_tex(self, filepath):
        """Generate a .tex file.

        Args
        ----
        filepath: str
            The name of the file (without .tex)
        """

        with open(filepath + '.tex', 'w', encoding='utf-8') as newf:
            self.dump(newf)

    def dumps_packages(self):
        """Represent the packages needed as a string in LaTeX syntax.

        Returns
        -------
        list
        """

        return dumps_list(self.packages)

    def dump_packages(self, file_w):
        """Write the LaTeX representation of the packages to a file.

        file_w: io.TextIOBase
            The file object in which to save the data

        """

        file_w.write(self.dumps_packages())
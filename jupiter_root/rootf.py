"""Functions and class for importing ond operating on root datatype

Class exported by rootf.py:
    * Rootf - class simplifies imports of root data
"""
import uproot


class Rootf:
    """ Class simplifies imports of root data

    Rootf take name of file as parameter, and remembers it. It expects file to be in ./data folder. So far there is
    only one first level branch named 'Coincidences', it expects files to look that way. Working with files that
    looks different may need other function, reformat class, or import of better library for root files. Rootf does
    not read full file until it's told to, that way it fully uses incredible 'root' files properties. It will
    return only lowest level branch it is asked too, as awkward array.

    :parameter self.path: remembers path for root file.

    Methods for this class:
        *get_arr - Returns awkward array from chosen branch.
    """
    def __init__(self, name) -> None:
        """Takes name of file as parameter, to make data imports simpler. Remembers it as path.

        :param name: name of file that we want to import data from.
        :type name: str
        """
        self.path = "data/" + name

    def _open_f(self):
        """Opens file for other functions to work on it.

        :return: Opened file root type.
        """
        return uproot.open(self.path)

    def get_arr(self, arr):
        """Returns awkward array from chosen branch.

        This method is here to make simpler importing single branch from root file. It expects it to be second level
        branch inside 'Coincidences' level. If it needs to work on roots with different structures, it needs to be
        rebuilt or just work with other library than uproot. It reads only one branch, so can fully use root data type.

        :param arr: name of the branch we want get data from
        :type arr: str
        :return: it returns simple awkward array from branch we chose.
        :rtype: awkward array
        """
        with self._open_f() as file:
            return file["Coincidences"][arr].array()

import uproot


class Rootf:
    def __init__(self, name) -> None:
        self.path = "data/" + name

    def _open_f(self):
        return uproot.open(self.path)

    def get_arr(self, arr):
        with self._open_f() as file:
            return file["Coincidences"]["time1"].array()


import typing
class ScrapedData:
    def __init__(self):
        self.main:typing.Dict[str, str] = {}

class MainScrapedData(ScrapedData):
    def __init__(self):
        super().__init__()
        self.compare: typing.Dict[str, str] = {}

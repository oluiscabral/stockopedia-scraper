import abc
import typing
from formatted_data import FormattedData
class Template(abc.ABC):
    @staticmethod
    def format(scraped_data) -> typing.List[FormattedData]:
        raise NotImplementedError

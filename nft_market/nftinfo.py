import dataclasses
from typing import *

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


@dataclasses.dataclass
class NFTInfo:
    id: str
    name: str
    num_items_all: Optional[int]
    num_listing: Optional[int]
    num_owners: Optional[int]
    floor: float
    volume: float

    def __post_init__(self):
        assert self.id is not None
        assert self.name is not None
        assert self.floor is not None
        assert self.volume is not None
    # enddef


class NFTInfoBuilder:
    def __init__(self, driver: WebDriver, id: str):
        self.driver = driver
        self.id = id

        # properties
        self._name = ...
        self._num_items_all = None
        self._num_listing = None
        self._num_owners = None
        self._floor = ...
        self._volume = ...
    # enddef

    @staticmethod
    def _text2float(s: str) -> float:
        s_rep = s.replace(',', '').replace('<', '').replace('>', '').replace('$', '') \
            .replace('k', '*1000').replace('K', '*1000') \
            .replace('m', '*1000000').replace('M', '*1000000') \
            .replace('B', '*1000000000')
        try:
            f = float(eval(s_rep))
        except Exception as e:
            print(f'orig: {s}, replaced: {s_rep}')
            raise e
        # endtry

        return f
    # enddef

    @staticmethod
    def _text2int(s: str) -> int:
        return int(NFTInfoBuilder._text2float(s))
    # enddef

    def _find_text(self, xpath: str) -> str:
        return self.driver.find_element(by=By.XPATH, value=xpath).text
    # enddef

    def build(self) -> NFTInfo:
        nft = NFTInfo(id=self.id,
                      name=self._name,
                      num_items_all=self._num_items_all,
                      num_listing=self._num_listing,
                      num_owners=self._num_owners,
                      floor=self._floor,
                      volume=self._volume)

        return nft
    # enddef

    def name(self, xpath: str, post: Callable[str, str] = None) -> 'NFTInfoBuilder':
        s = self._find_text(xpath)
        if post is not None:
            s = post(s)
        # endif

        self._name = s
        return self
    # enddef

    def num_items_all(self, xpath: str, post: Callable[str, str] = None) -> 'NFTInfoBuilder':
        i = self._find_text(xpath)
        if post is not None:
            i = post(i)
        # endif
        i = self._text2int(i)

        self._num_items_all = i
        return self
    # enddef

    def num_listing(self, xpath: str, post: Callable[str, str] = None) -> 'NFTInfoBuilder':
        i = self._find_text(xpath)
        if post is not None:
            i = post(i)
        # endif
        i = self._text2int(i)

        self._num_listing = i
        return self
    # enddef

    def num_owners(self, xpath: str, post: Callable[str, str] = None) -> 'NFTInfoBuilder':
        i = self._find_text(xpath)
        if post is not None:
            i = post(i)
        # endif
        i = self._text2int(i)

        self._num_owners = i
        return self
    # enddef

    def floor(self, xpath: str, post: Callable[str, str] = None) -> 'NFTInfoBuilder':
        f = self._find_text(xpath)
        if post is not None:
            f = post(f)
        # endif
        f = self._text2float(f)

        self._floor = f
        return self
    # enddef

    def volume(self, xpath: str, post: Callable[str, str] = None) -> 'NFTInfoBuilder':
        f = self._find_text(xpath)
        if post is not None:
            f = post(f)
        # endif
        f = self._text2float(f)

        self._volume = f
        return self
    # enddef

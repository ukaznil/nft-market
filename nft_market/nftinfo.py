import dataclasses
import warnings
from typing import *

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


@dataclasses.dataclass
class NFTInfo:
    id: str
    name: str
    num_supply: Optional[int]
    num_listing: Optional[int]
    num_owners: Optional[int]
    floor: float
    volume: float

    def __post_init__(self):
        assert self.id is not None, self.id
        # assert self.name is not None and len(self.name) > 0, self.name
        assert self.name is not None, self.name
        assert self.floor is not None, self.floor
        assert self.volume is not None, self.volume
    # enddef

    @property
    def num_items_all(self):
        warnings.warn('The property "num_items_all" has been deprecated. It will be no longer available in future updates. Please use "num_supply" instead.')

        return self.num_supply
    # enddef


class NFTInfoBuilder:
    def __init__(self, driver: WebDriver, id: str):
        self.driver = driver
        self.id = id

        # properties
        self._name = ...
        self._num_supply = None
        self._num_listing = None
        self._num_owners = None
        self._floor = ...
        self._volume = ...
    # enddef

    def _text2float(self, s: str) -> float:
        s_rep = s.replace(',', '').replace('<', '').replace('>', '').replace('$', '') \
            .replace('k', '*1000').replace('K', '*1000') \
            .replace('m', '*1000000').replace('M', '*1000000') \
            .replace('B', '*1000000000')
        try:
            f = float(eval(s_rep))
        except Exception as e:
            print(f"ID: {self.id}, orig: '{s}', replaced: {s_rep}")
            raise e
        # endtry

        return f
    # enddef

    def _text2int(self, s: str) -> int:
        return int(self._text2float(s))
    # enddef

    def _find_text(self, xpath: str) -> str:
        return self.driver.find_element(by=By.XPATH, value=xpath).text
    # enddef

    def build(self) -> NFTInfo:
        nft = NFTInfo(id=self.id,
                      name=self._name,
                      num_supply=self._num_supply,
                      num_listing=self._num_listing,
                      num_owners=self._num_owners,
                      floor=self._floor,
                      volume=self._volume)

        return nft
    # enddef

    def name(self, xpath: str, post: Callable[str, str] = None) -> 'NFTInfoBuilder':
        try:
            s = self._find_text(xpath)

            if post is not None:
                s = post(s)
            # endif
        except Exception as e:
            raise ValueError(f'ID: {self.id}, Cause: name, {e}')
        # endtry

        self._name = s
        return self
    # enddef

    def num_supply(self, xpath: str, post: Callable[str, str] = None) -> 'NFTInfoBuilder':
        try:
            i = self._find_text(xpath)

            if post is not None:
                i = post(i)
                # endif

            if i is not None:
                i = self._text2int(i)
            # endif
        except Exception as e:
            raise ValueError(f'ID: {self.id}, Cause: num_supply, {e}')
        # endtry

        self._num_supply = i
        return self
    # enddef

    def num_listing(self, xpath: str, post: Callable[str, str] = None) -> 'NFTInfoBuilder':
        try:
            i = self._find_text(xpath)

            if post is not None:
                i = post(i)
                # endif

            if i is not None:
                i = self._text2int(i)
            # endif
        except Exception as e:
            raise ValueError(f'ID: {self.id}, Cause: num_listing, {e}')
        # endtry

        self._num_listing = i
        return self
    # enddef

    def num_owners(self, xpath: str, post: Callable[str, str] = None) -> 'NFTInfoBuilder':
        try:
            i = self._find_text(xpath)

            if post is not None:
                i = post(i)
            # endif

            if i is not None:
                i = self._text2int(i)
            # endif
        except Exception as e:
            raise ValueError(f'ID: {self.id}, Cause: num_owners, {e}')
        # endtry

        self._num_owners = i
        return self
    # enddef

    def floor(self, xpath: str, post: Callable[str, str] = None) -> 'NFTInfoBuilder':
        try:
            f = self._find_text(xpath)

            if post is not None:
                f = post(f)
            # endif

            if f is not None:
                f = self._text2float(f)
            # endif
        except Exception as e:
            raise ValueError(f'ID: {self.id}, Cause: floor, {e}')
        # endtry

        self._floor = f
        return self
    # enddef

    def volume(self, xpath: str, post: Callable[str, str] = None) -> 'NFTInfoBuilder':
        try:
            f = self._find_text(xpath)

            if post is not None:
                f = post(f)
                # endif

            if f is not None:
                f = self._text2float(f)
            # endif
        except Exception as e:
            raise ValueError(f'ID: {self.id}, Cause: volume, {e}')
        # endtry

        self._volume = f
        return self
    # enddef

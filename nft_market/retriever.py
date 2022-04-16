import itertools
import logging
import os
import time
from functools import cached_property
from typing import *

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.webdriver import Service
from webdriver_manager.firefox import GeckoDriverManager

from nft_market.market import Market
from nft_market.nftinfo import NFTInfo


class _WebDriver:
    @cached_property
    def executable_path(self) -> str:
        return GeckoDriverManager(log_level=logging.NOTSET).install()
    # enddef


class _WebFetcher:
    def __init__(self, url: str, webdriver: _WebDriver, sec_wait: int):
        self.url = url
        self.executable_path = webdriver.executable_path
        self.sec_wait = sec_wait

        options = Options()
        options.add_argument('--headless')
        options.add_argument('--incognito')
        self.options = options
    # enddef

    def __enter__(self):
        self.driver = webdriver.Firefox(options=self.options,
                                        service=Service(executable_path=self.executable_path,
                                                        log_path=os.devnull))
        self.driver.maximize_window()
        self.driver.get(url=self.url)
        self.driver.implicitly_wait(self.sec_wait)
        time.sleep(self.sec_wait)

        return self.driver
    # enddef

    def __exit__(self, exc_type, exc_val, exc_tb):
        time.sleep(self.sec_wait)
        self.driver.quit()
    # enddef


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


def _text2int(s: str) -> int:
    return int(_text2float(s))


class Retriever:
    def __init__(self, sec_wait: int = 10, num_retry: int = 5, verbose: bool = False):
        self.option = {
            'webdriver': _WebDriver(),
            'sec_wait': sec_wait
            }
        self.sec_wait = sec_wait
        self.num_retry = num_retry
        self.verbose = verbose
    # enddef

    def fetch(self, market: Market, id: str) -> NFTInfo:
        '''Fetch the current information of the specific NFT.
        Args:
            market (nft_market.Market): One of the enums of nft_market.Market
            id (str): The ID of the NFT. You can find it on the URL on the marketplace.

        Returns:
            (nft_market.NFTInfo)
        '''
        if market == Market.OpenSea:
            func = self._retrieve_opensea
        elif market == Market.Entrepot:
            func = self._retrieve_entrepot
        elif market == Market.tofuNFT:
            func = self._retrieve_tofunft
        elif market == Market.PancakeSwap:
            func = self._retrieve_pancakeswap
        elif market == Market.Rarible:
            func = self._retrieve_rarible
        elif market == Market.GhostMarket:
            func = self._retrieve_ghostmarket
        elif market == Market.Cryptocom:
            func = self._retrieve_cryptocom
        elif market == Market.Gem:
            func = self._retrieve_gem
        elif market == Market.LooksRare:
            func = self._retrieve_looksrare
        elif market == Market.NFTrade:
            func = self._retrieve_nftrade
        elif market == Market.Solanart:
            func = self._retrieve_solanart
        elif market == Market.MagicEden:
            func = self._retrieve_magiceden
        elif market == Market.XANALIA:
            func = self._retrieve_xanalia
        else:
            raise NotImplementedError(market)
        # endif

        num_retry = 0
        error = NotImplemented
        while num_retry <= self.num_retry:
            nft, error = func(id)

            if nft is not None:
                assert error is None

                return nft
            else:
                assert error is not None

                num_retry += 1
                time.sleep(self.sec_wait)
            # endif
        # endwhile

        raise error
    # enddef

    def _retrieve_opensea(self, id: str) -> Tuple[NFTInfo, Exception]:
        url = f'https://opensea.io/collection/{id}'

        nft = None
        with _WebFetcher(url, **self.option) as driver:
            for c1 in [4, 5]:
                error = None
                try:
                    name = driver.find_element(by=By.XPATH,
                                               value=f'//*[@id="main"]/div/div/div[1]/div[2]/div[3]/h1').text
                    num_items_all = None
                    num_listing = _text2int(driver.find_element(by=By.XPATH,
                                                                value=f'//*[@id="main"]/div/div/div[1]/div[2]/div[{c1}]/div/div[1]/a/div/div[1]/div/span/div').text)
                    num_owners = _text2int(driver.find_element(by=By.XPATH,
                                                               value=f'//*[@id="main"]/div/div/div[1]/div[2]/div[{c1}]/div/div[2]/a/div/div[1]/div/span/div').text)
                    floor = _text2float(driver.find_element(by=By.XPATH,
                                                            value=f'//*[@id="main"]/div/div/div[1]/div[2]/div[{c1}]/div/div[3]/a/div/div[1]/div/span/div').text)
                    volume = _text2float(driver.find_element(by=By.XPATH,
                                                             value=f'//*[@id="main"]/div/div/div[1]/div[2]/div[{c1}]/div/div[4]/a/div/div[1]/div/span/div').text)

                    nft = NFTInfo(id=id, name=name,
                                  num_items_all=num_items_all, num_listing=num_listing, num_owners=num_owners,
                                  floor=floor, volume=volume)
                    break
                except Exception as e:
                    error = e
                    continue
                # endtry
            # endfor
        # endwith

        return nft, error
    # enddef

    def _retrieve_entrepot(self, id: str) -> Tuple[NFTInfo, Exception]:
        url = f'https://entrepot.app/marketplace/{id}'

        nft = None
        with _WebFetcher(url, **self.option) as driver:
            for c1 in [2, 3]:
                error = None
                try:
                    name = driver.find_element(by=By.XPATH,
                                               value=f'//*[@id="root"]/main/div/div[1]/div/div[1]/div/div[3]/h1').text
                    num_items_all = None
                    num_listing = _text2int(driver.find_element(by=By.XPATH,
                                                                value=f'//*[@id="root"]/main/div/div[1]/div/div[1]/div/div[2]/div[1]/div/div[2]/strong').text)
                    num_owners = None
                    floor = _text2float(driver.find_element(by=By.XPATH,
                                                            value=f'//*[@id="mainListings"]/div[2]/div/div[2]/div[2]/div/div[1]/div/a/div[{c1}]/div/div[4]/p').text)
                    volume = _text2float(driver.find_element(by=By.XPATH,
                                                             value=f'//*[@id="root"]/main/div/div[1]/div/div[1]/div/div[2]/div[1]/div/div[1]/strong').text)
                    nft = NFTInfo(id=id, name=name,
                                  num_items_all=num_items_all, num_listing=num_listing, num_owners=num_owners,
                                  floor=floor, volume=volume)
                    break
                except Exception as e:
                    error = e
                    continue
                # endtry
            # endfor
        # endwith

        return nft, error
    # enddef

    def _retrieve_tofunft(self, id: str) -> Tuple[NFTInfo, Exception]:
        url = f'https://tofunft.com/collection/{id}/items'

        nft = None
        with _WebFetcher(url, **self.option) as driver:
            error = None
            try:
                name = driver.find_element(by=By.XPATH,
                                           value=f'//*[@id="__next"]/div[2]/div[1]/div[1]/h1').text
                num_items_all = None
                num_listing = _text2int(driver.find_element(by=By.XPATH,
                                                            value=f'//*[@id="__next"]/div[2]/div[1]/div[2]/div[1]/div[3]/div[2]').text)
                num_owners = _text2int(driver.find_element(by=By.XPATH,
                                                           value=f'//*[@id="__next"]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]').text)
                floor = _text2float(driver.find_element(by=By.XPATH,
                                                        value=f'//*[@id="__next"]/div[2]/div[1]/div[2]/div[1]/div[5]/div[2]').text)
                volume = _text2float(driver.find_element(by=By.XPATH,
                                                         value=f'//*[@id="__next"]/div[2]/div[1]/div[2]/div[1]/div[4]/div[2] ').text)

                nft = NFTInfo(id=id, name=name,
                              num_items_all=num_items_all, num_listing=num_listing, num_owners=num_owners,
                              floor=floor, volume=volume)
            except Exception as e:
                error = e
            # endtry
        # endwith

        return nft, error
    # enddef

    def _retrieve_pancakeswap(self, id: str) -> Tuple[NFTInfo, Exception]:
        url = f'https://pancakeswap.finance/nfts/collections/{id}'

        nft = None
        with _WebFetcher(url, **self.option) as driver:
            error = None
            try:
                name = driver.find_element(by=By.XPATH,
                                           value=f'//*[@id="__next"]/div[1]/div[3]/div/div[1]/div/div[3]/div[1]/h1').text
                num_items_all = _text2int(driver.find_element(by=By.XPATH,
                                                              value=f'//*[@id="__next"]/div[1]/div[3]/div/div[1]/div/div[3]/div[2]/div/div[1]/div[2]').text)
                num_listing = _text2int(driver.find_element(by=By.XPATH,
                                                            value=f'//*[@id="__next"]/div[1]/div[3]/div/div[1]/div/div[3]/div[2]/div/div[2]/div[2]').text)
                num_owners = None
                floor = _text2float(driver.find_element(by=By.XPATH,
                                                        value=f'//*[@id="__next"]/div[1]/div[3]/div/div[1]/div/div[3]/div[2]/div/div[3]/div[2]').text)
                volume = _text2float(driver.find_element(by=By.XPATH,
                                                         value=f'//*[@id="__next"]/div[1]/div[3]/div/div[1]/div/div[3]/div[2]/div/div[4]/div[2]').text)

                nft = NFTInfo(id=id, name=name,
                              num_items_all=num_items_all, num_listing=num_listing, num_owners=num_owners,
                              floor=floor, volume=volume)
            except Exception as e:
                error = e
            # endtry
        # endwith

        return nft, error
    # enddef

    def _retrieve_rarible(self, id: str) -> Tuple[NFTInfo, Exception]:
        if id.startswith('0x'):
            url = f'https://rarible.com/collection/{id}/items'
        else:
            # Seems that "named" projects have a different URL schema.
            url = f'https://rarible.com/{id}/items'
        # endif

        nft = None
        with _WebFetcher(url, **self.option) as driver:
            error = None
            try:
                name = driver.find_element(by=By.XPATH,
                                           value=f'//*[@id="root"]/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/div[1]/span').text
                num_items_all = _text2int(driver.find_element(by=By.XPATH,
                                                              value=f'//*[@id="root"]/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/div[2]/div[4]/span[2]/span').text)
                num_listing = None
                num_owners = _text2int(driver.find_element(by=By.XPATH,
                                                           value=f'//*[@id="root"]/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/div[2]/div[5]/span[2]/span').text)
                floor = _text2float(driver.find_element(by=By.XPATH,
                                                        value=f'//*[@id="root"]/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/span[2]/span').text)
                volume = _text2float(driver.find_element(by=By.XPATH,
                                                         value=f'//*[@id="root"]/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/div[2]/div[6]/span[2]/span').text)

                nft = NFTInfo(id=id, name=name,
                              num_items_all=num_items_all, num_listing=num_listing, num_owners=num_owners,
                              floor=floor, volume=volume)
            except Exception as e:
                error = e
            # endtry
        # endwith

        return nft, error
    # enddef

    def _retrieve_ghostmarket(self, id: str) -> Tuple[NFTInfo, Exception]:
        url = f'https://ghostmarket.io/collection/{id}'

        nft = None
        with _WebFetcher(url, **self.option) as driver:
            for c_floor in ['span/div[2]/', '', ]:
                error = None
                try:
                    name = driver.find_element(by=By.XPATH,
                                               value=f'//*[@id="__layout"]/div/section/div/div[1]/div[3]/span[1]').text
                    num_items_all = _text2int(driver.find_element(by=By.XPATH,
                                                                  value=f'//*[@id="__layout"]/div/section/div/div[2]/div[1]/div/div[1]/span/div[2]/div/div/div[1]').text)
                    num_listing = None
                    num_owners = _text2int(driver.find_element(by=By.XPATH,
                                                               value=f'//*[@id="__layout"]/div/section/div/div[2]/div[1]/div/div[2]/span/div[2]/div/div/div[1]').text)
                    floor = _text2float(driver.find_element(by=By.XPATH,
                                                            value=f'//*[@id="__layout"]/div/section/div/div[2]/div[1]/div/div[3]/{c_floor}div/div/div[1]').text)
                    volume = _text2float(driver.find_element(by=By.XPATH,
                                                             value=f'//*[@id="__layout"]/div/section/div/div[2]/div[1]/div/div[4]/{c_floor}div/div/div[1]').text)

                    nft = NFTInfo(id=id, name=name,
                                  num_items_all=num_items_all, num_listing=num_listing, num_owners=num_owners,
                                  floor=floor, volume=volume)
                    break
                except Exception as e:
                    error = e
                    continue
                # endtry
            # endfor
        # endwith

        return nft, error
    # enddef

    def _retrieve_cryptocom(self, id: str) -> Tuple[NFTInfo, Exception]:
        url = f'https://crypto.com/nft/collection/{id}'

        nft = None
        with _WebFetcher(url, **self.option) as driver:
            error = None
            try:
                name = driver.find_element(by=By.XPATH,
                                           value=f'//*[@id="root"]/div[1]/div/div[3]/div/div[1]').text
                num_items_all = None
                num_listing = _text2int(driver.find_element(by=By.XPATH,
                                                            value=f'//*[@id="root"]/div[1]/div/div[3]/div/div[2]/div/div[1]/span').text)
                num_owners = _text2int(driver.find_element(by=By.XPATH,
                                                           value=f'//*[@id="root"]/div[1]/div/div[3]/div/div[2]/div/div[2]/span').text)
                floor = _text2float(driver.find_element(by=By.XPATH,
                                                        value=f'//*[@id="root"]/div[1]/div/div[3]/div/div[2]/div/div[3]/div/div[2]/div/span[2]/div').text)
                volume = _text2float(driver.find_element(by=By.XPATH,
                                                         value=f'//*[@id="root"]/div[1]/div/div[3]/div/div[2]/div/div[4]/div/span[2]/div').text)

                nft = NFTInfo(id=id, name=name,
                              num_items_all=num_items_all, num_listing=num_listing, num_owners=num_owners,
                              floor=floor, volume=volume)
            except Exception as e:
                error = e
            # endtry
        # endwith

        return nft, error
    # enddef

    def _retrieve_gem(self, id: str) -> Tuple[NFTInfo, Exception]:
        url = f'https://www.gem.xyz/collection/{id}'

        nft = None
        with _WebFetcher(url, **self.option) as driver:
            error = None
            try:
                name = driver.find_element(by=By.XPATH,
                                           value=f'//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div').text
                num_items_all = None
                num_listing = _text2int(driver.find_element(by=By.XPATH,
                                                            value=f'//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/div[3]/div[1]/div[2]/div[1]').text \
                                        .replace('results', ''))
                num_owners = None
                floor = _text2float(driver.find_element(by=By.XPATH,
                                                        value=f'//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div[1]/div/div[1]/div[2]/span[3]/span[2]').text)
                volume = _text2float(driver.find_element(by=By.XPATH,
                                                         value=f'//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div[1]/div/div[1]/div[2]/span[1]/span[2]').text)

                nft = NFTInfo(id=id, name=name,
                              num_items_all=num_items_all, num_listing=num_listing, num_owners=num_owners,
                              floor=floor, volume=volume)
            except Exception as e:
                error = e
            # endtry
        # endwith

        return nft, error
    # enddef

    def _retrieve_looksrare(self, id: str) -> Tuple[NFTInfo, Exception]:
        url = f'https://looksrare.org/collections/{id}'

        nft = None
        with _WebFetcher(url, **self.option) as driver:
            for c_name, c_listing in itertools.product([4, 5], [6, 7]):
                error = None
                try:
                    name = driver.find_element(by=By.XPATH,
                                               value=f'//*[@id="__next"]/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/div[{c_name}]/div/div[2]/div[1]/h1').text
                    num_items_all = None
                    num_listing = _text2int(driver.find_element(by=By.XPATH,
                                                                value=f'//*[@id="__next"]/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/div[{c_listing}]/div/div/div/div[3]/div[2]').text)
                    num_owners = _text2int(driver.find_element(by=By.XPATH,
                                                               value=f'//*[@id="__next"]/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/div[{c_listing}]/div/div/div/div[4]/div[2]').text)
                    floor = _text2float(driver.find_element(by=By.XPATH,
                                                            value=f'//*[@id="__next"]/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/div[{c_listing}]/div/div/div/div[1]/div[2]/div[1]').text)
                    volume = _text2float(driver.find_element(by=By.XPATH,
                                                             value=f'//*[@id="__next"]/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/div[{c_listing}]/div/div/div/div[2]/div[2]/div').text)

                    nft = NFTInfo(id=id, name=name,
                                  num_items_all=num_items_all, num_listing=num_listing, num_owners=num_owners,
                                  floor=floor, volume=volume)
                    break
                except Exception as e:
                    error = e
                    continue
                # endtry
            # endfor
        # endwith

        return nft, error
    # enddef

    def _retrieve_nftrade(self, id: str) -> Tuple[NFTInfo, Exception]:
        url = f'https://nftrade.com/assets/{id}'

        nft = None
        with _WebFetcher(url, **self.option) as driver:
            error = None
            try:
                name = driver.find_element(by=By.XPATH,
                                           value=f'//*[@id="__next"]/div/main/div/div/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]').text
                num_items_all = None
                num_listing = None
                num_owners = None
                floor = _text2float(driver.find_element(by=By.XPATH,
                                                        value=f'//*[@id="__next"]/div/main/div/div/div[1]/div[1]/div[4]/div[2]/div[1]/div[2]').text)
                volume = _text2float(driver.find_element(by=By.XPATH,
                                                         value=f'//*[@id="__next"]/div/main/div/div/div[1]/div[1]/div[4]/div[2]/div[4]/div[2]').text)

                nft = NFTInfo(id=id, name=name,
                              num_items_all=num_items_all, num_listing=num_listing, num_owners=num_owners,
                              floor=floor, volume=volume)
            except Exception as e:
                error = e
            # endtry
        # endwith

        return nft, error
    # enddef

    def _retrieve_solanart(self, id: str) -> Tuple[NFTInfo, Exception]:
        url = f'https://solanart.io/collections/{id}'

        nft = None
        with _WebFetcher(url, **self.option) as driver:
            error = None
            try:
                name = driver.find_element(by=By.XPATH,
                                           value=f'//*[@id="__next"]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/h2').text
                num_items_all = _text2int(driver.find_element(by=By.XPATH,
                                                              value=f'//*[@id="__next"]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]').text)
                num_listing = _text2int(driver.find_element(by=By.XPATH,
                                                            value=f'//*[@id="__next"]/div/div[1]/div[2]/div[2]/div[3]/div[2]/div[2]/div[2]').text \
                                        .split(' ')[0])
                num_owners = _text2int(driver.find_element(by=By.XPATH,
                                                           value=f'//*[@id="__next"]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div[3]/div[1]').text)
                floor = _text2float(driver.find_element(by=By.XPATH,
                                                        value=f'//*[@id="__next"]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div[5]/div[1]').text \
                                    .replace('◎', ''))
                volume = _text2float(driver.find_element(by=By.XPATH,
                                                         value=f'//*[@id="__next"]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div[7]/div[1]').text \
                                     .replace('◎', ''))

                nft = NFTInfo(id=id, name=name,
                              num_items_all=num_items_all, num_listing=num_listing, num_owners=num_owners,
                              floor=floor, volume=volume)
            except Exception as e:
                error = e
            # endtry
        # endwith

        return nft, error
    # enddef

    def _retrieve_magiceden(self, id: str) -> Tuple[NFTInfo, Exception]:
        def _remove_sol_mark(s: str) -> str:
            return s.strip(" ◎")

        url = f'https://magiceden.io/marketplace/{id}'

        nft = None
        with _WebFetcher(url, **self.option) as driver:
            error = None
            try:
                # /html/body/div[2]/div/div/div/div[2]/div[2]/div[1]/div/h1
                #   //*[@id="root"]/div/div/div/div[2]/div[2]/div[1]/div/h1
                name = driver.find_element(by=By.XPATH,
                                           value=f'//*[@id="root"]/div/div/div/div[2]/div[2]/div[1]/div/h1').text
                num_items_all = None
                num_listing = _text2int(driver.find_element(by=By.XPATH,
                                                            value=f'//*[@id="root"]/div/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div/div[4]/div/span[2]').text)
                num_owners = None
                floor = _text2float(_remove_sol_mark(driver.find_element(by=By.XPATH,
                                                                         value=f'//*[@id="root"]/div/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div/div[3]/div/span[2]').text))
                volume = _text2float(_remove_sol_mark(driver.find_element(by=By.XPATH,
                                                                          value=f'//*[@id="root"]/div/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div/div[2]/div/span[2]').text))

                nft = NFTInfo(id=id, name=name,
                              num_items_all=num_items_all, num_listing=num_listing, num_owners=num_owners,
                              floor=floor, volume=volume)
            except Exception as e:
                error = e
            # endtry
        # endwith

        return nft, error
    # enddef

    def _retrieve_xanalia(self, id: str) -> Tuple[NFTInfo, Exception]:
        url = f'https://www.xanalia.com/{id}'

        nft = None
        error = None
        with _WebFetcher(url, **self.option) as driver:
            try:
                name = driver.find_element(by=By.XPATH,
                                           value=f'/html/body/div/div[1]/div[3]/div/div/div/div[2]/div/div[1]').text
                num_items_all = _text2int(driver.find_element(by=By.XPATH,
                                                              value=f'//*[@id="home-page"]/div/div/div/div[2]/div/div[2]/div[1]/h5').text)
                num_listing = None
                num_owners = _text2int(driver.find_element(by=By.XPATH,
                                                           value=f'//*[@id="home-page"]/div/div/div/div[2]/div/div[2]/div[2]/h5').text)
                floor = _text2float(driver.find_element(by=By.XPATH,
                                                        value=f'//*[@id="home-page"]/div/div/div/div[2]/div/div[2]/div[3]/h5').text)
                volume = _text2float(driver.find_element(by=By.XPATH,
                                                         value=f'//*[@id="home-page"]/div/div/div/div[2]/div/div[2]/div[4]/h5').text)

                nft = NFTInfo(id=id, name=name,
                              num_items_all=num_items_all, num_listing=num_listing, num_owners=num_owners,
                              floor=floor, volume=volume)
            except Exception as e:
                error = e
            # endtry
        # endwith

        return nft, error
    # enddef

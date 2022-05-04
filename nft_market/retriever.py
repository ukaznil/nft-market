import itertools
import logging
import os
import time
from typing import *

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.webdriver import Service
from webdriver_manager.firefox import GeckoDriverManager

from nft_market.market import Market
from nft_market.nftinfo import NFTInfo, NFTInfoBuilder


class _WebFetcher:
    def __init__(self, url: str, executable_path: str, sec_wait: int):
        self.url = url
        self.executable_path = executable_path
        self.sec_wait = sec_wait

        options = Options()
        options.add_argument('--headless')
        options.add_argument('--incognito')
        options.add_argument('--disable-extensions')
        options.add_argument('--proxy-server="direct://"')
        options.add_argument('--proxy-bypass-list=*')
        options.add_argument('--start-maximized')

        self.options = options
    # enddef

    def __enter__(self):
        self.driver = webdriver.Firefox(options=self.options,
                                        service=Service(executable_path=self.executable_path,
                                                        log_path=os.devnull))
        self.driver.get(url=self.url)
        self.driver.implicitly_wait(self.sec_wait)
        time.sleep(self.sec_wait)

        return self.driver
    # enddef

    def __exit__(self, exc_type, exc_val, exc_tb):
        time.sleep(self.sec_wait)
        self.driver.close()
        self.driver.quit()
    # enddef


class Retriever:
    def __init__(self, sec_wait: int = 10, num_retry: int = 5, verbose: bool = False):
        self.option = {
            'executable_path': GeckoDriverManager(log_level=logging.NOTSET).install(),
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
        elif market == Market.CetoSwap:
            func = self._retrieve_cetoswap
        elif market == Market.Coinbase:
            func = self._retrieve_coinbase
        elif market == Market.CCC:
            func = self._retrieve_ccc
        elif market == Market.NiftyGateway:
            func = self._retrieve_niftygateway
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

                print(f'An error in "{id}" [{num_retry}/{self.num_retry + 1}]')
            # endif
        # endwhile

        raise error
    # enddef

    def _retrieve_opensea(self, id: str) -> Tuple[NFTInfo, Exception]:
        url = f'https://opensea.io/collection/{id}'

        nft = None
        try:
            with _WebFetcher(url, **self.option) as driver:
                for c1 in [4, 5]:
                    error = None

                    try:
                        nft = NFTInfoBuilder(driver, id) \
                            .name('//*[@id="main"]/div/div/div[1]/div[2]/div[3]/h1') \
                            .num_listing(f'//*[@id="main"]/div/div/div[1]/div[2]/div[{c1}]/div/div[1]/a/div/div[1]/div/span/div') \
                            .num_owners(f'//*[@id="main"]/div/div/div[1]/div[2]/div[{c1}]/div/div[2]/a/div/div[1]/div/span/div') \
                            .floor(f'//*[@id="main"]/div/div/div[1]/div[2]/div[{c1}]/div/div[3]/a/div/div[1]/div/span/div') \
                            .volume(f'//*[@id="main"]/div/div/div[1]/div[2]/div[{c1}]/div/div[4]/a/div/div[1]/div/span/div') \
                            .build()
                        break
                    except Exception as e:
                        error = e
                        continue
                    # endtry
                # endfor
            # endwith
        except Exception as e:
            error = e
        # endtry

        return nft, error
    # enddef

    def _retrieve_entrepot(self, id: str) -> Tuple[NFTInfo, Exception]:
        url = f'https://entrepot.app/marketplace/{id}'

        nft = None
        try:
            with _WebFetcher(url, **self.option) as driver:
                for c1 in [2, 3]:
                    error = None

                    try:
                        nft = NFTInfoBuilder(driver, id) \
                            .name('//*[@id="root"]/main/div/div[1]/div/div[1]/div/div[3]/h1') \
                            .num_listing('//*[@id="root"]/main/div/div[1]/div/div[1]/div/div[2]/div[1]/div/div[2]/strong') \
                            .floor(f'//*[@id="mainListings"]/div[2]/div/div[2]/div[2]/div/div[1]/div/a/div[{c1}]/div/div[4]/p') \
                            .volume('//*[@id="root"]/main/div/div[1]/div/div[1]/div/div[2]/div[1]/div/div[1]/strong') \
                            .build()
                        break
                    except Exception as e:
                        error = e
                        continue
                    # endtry
                # endfor
            # endwith
        except Exception as e:
            error = e
        # endtry

        return nft, error
    # enddef

    def _retrieve_tofunft(self, id: str) -> Tuple[NFTInfo, Exception]:
        url = f'https://tofunft.com/collection/{id}/items'

        nft = None
        try:
            with _WebFetcher(url, **self.option) as driver:
                error = None

                nft = NFTInfoBuilder(driver, id) \
                    .name('//*[@id="__next"]/div[2]/div[1]/div[1]/h1') \
                    .num_listing('//*[@id="__next"]/div[2]/div[1]/div[2]/div[1]/div[3]/div[2]') \
                    .num_owners('//*[@id="__next"]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]') \
                    .floor('//*[@id="__next"]/div[2]/div[1]/div[2]/div[1]/div[5]/div[2]') \
                    .volume('//*[@id="__next"]/div[2]/div[1]/div[2]/div[1]/div[4]/div[2]') \
                    .build()
            # endwith
        except Exception as e:
            error = e
        # endtry

        return nft, error
    # enddef

    def _retrieve_pancakeswap(self, id: str) -> Tuple[NFTInfo, Exception]:
        url = f'https://pancakeswap.finance/nfts/collections/{id}'

        nft = None
        try:
            with _WebFetcher(url, **self.option) as driver:
                error = None

                nft = NFTInfoBuilder(driver, id) \
                    .name('//*[@id="__next"]/div[1]/div[3]/div/div[1]/div/div[3]/div[1]/h1') \
                    .num_supply('//*[@id="__next"]/div[1]/div[3]/div/div[1]/div/div[3]/div[2]/div/div[1]/div[2]') \
                    .num_listing('//*[@id="__next"]/div[1]/div[3]/div/div[1]/div/div[3]/div[2]/div/div[2]/div[2]') \
                    .floor('//*[@id="__next"]/div[1]/div[3]/div/div[1]/div/div[3]/div[2]/div/div[3]/div[2]') \
                    .volume('//*[@id="__next"]/div[1]/div[3]/div/div[1]/div/div[3]/div[2]/div/div[4]/div[2]') \
                    .build()
            # endwith
        except Exception as e:
            error = e
        # endtry

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
        try:
            with _WebFetcher(url, **self.option) as driver:
                error = None

                nft = NFTInfoBuilder(driver, id) \
                    .name('//*[@id="root"]/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/div[1]/span') \
                    .num_supply('//*[@id="root"]/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/div[2]/div[4]/span[2]/span') \
                    .num_owners('//*[@id="root"]/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/div[2]/div[5]/span[2]/span') \
                    .floor('//*[@id="root"]/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/span[2]/span') \
                    .volume('//*[@id="root"]/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/div[2]/div[6]/span[2]/span') \
                    .build()
            # endwith
        except Exception as e:
            error = e
            # endtry

        return nft, error
    # enddef

    def _retrieve_ghostmarket(self, id: str) -> Tuple[NFTInfo, Exception]:
        url = f'https://ghostmarket.io/collection/{id}/?tab=nfts'

        nft = None
        try:
            with _WebFetcher(url, **self.option) as driver:
                for c_floor in ['span/div[2]/', '', ]:
                    error = None

                    try:
                        nft = NFTInfoBuilder(driver, id) \
                            .name('//*[@id="__layout"]/div/section/div/div[1]/div[3]/span[1]') \
                            .num_supply('//*[@id="__layout"]/div/section/div/div[2]/div[1]/div/div[1]/span/div[2]/div/div/div[1]') \
                            .num_owners('//*[@id="__layout"]/div/section/div/div[2]/div[1]/div/div[2]/span/div[2]/div/div/div[1]') \
                            .floor(f'//*[@id="__layout"]/div/section/div/div[2]/div[1]/div/div[3]/{c_floor}div/div/div[1]') \
                            .volume(f'//*[@id="__layout"]/div/section/div/div[2]/div[1]/div/div[4]/{c_floor}div/div/div[1]') \
                            .build()
                        break
                    except Exception as e:
                        error = e
                        continue
                    # endtry
                # endfor
            # endwith
        except Exception as e:
            error = e
        # endtry

        return nft, error
    # enddef

    def _retrieve_cryptocom(self, id: str) -> Tuple[NFTInfo, Exception]:
        url = f'https://crypto.com/nft/collection/{id}'

        nft = None
        try:
            with _WebFetcher(url, **self.option) as driver:
                error = None

                nft = NFTInfoBuilder(driver, id) \
                    .name('//*[@id="root"]/div[1]/div/div[3]/div/div[1]') \
                    .num_listing('//*[@id="root"]/div[1]/div/div[3]/div/div[2]/div/div[1]/span') \
                    .num_owners('//*[@id="root"]/div[1]/div/div[3]/div/div[2]/div/div[2]/span') \
                    .floor('//*[@id="root"]/div[1]/div/div[3]/div/div[2]/div/div[3]/div/div[2]/div/span[2]/div') \
                    .volume('//*[@id="root"]/div[1]/div/div[3]/div/div[2]/div/div[4]/div/span[2]/div') \
                    .build()
            # endwith
        except Exception as e:
            error = e
        # endtry

        return nft, error
    # enddef

    def _retrieve_gem(self, id: str) -> Tuple[NFTInfo, Exception]:
        url = f'https://www.gem.xyz/collection/{id}'

        nft = None
        try:
            with _WebFetcher(url, **self.option) as driver:
                error = None

                nft = NFTInfoBuilder(driver, id) \
                    .name('//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div') \
                    .num_listing('//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/div[3]/div[1]/div[2]/div[1]',
                                 lambda s: s.replace('results', '')) \
                    .floor('//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div[1]/div/div[1]/div[2]/span[3]/span[2]') \
                    .volume('//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div[1]/div/div[1]/div[2]/span[1]/span[2]') \
                    .build()
            # endwith
        except Exception as e:
            error = e
        # endtry

        return nft, error
    # enddef

    def _retrieve_looksrare(self, id: str) -> Tuple[NFTInfo, Exception]:
        url = f'https://looksrare.org/collections/{id}'

        nft = None
        try:
            with _WebFetcher(url, **self.option) as driver:
                for c_name, c_other in itertools.product([4, 5], [6, 7]):
                    error = None

                    try:
                        nft = NFTInfoBuilder(driver, id) \
                            .name(f'//*[@id="__next"]/div[2]/div/div/div/div[1]/div[2]/div[2]/div[2]/div[{c_name}]/div/div[2]/div[1]/h1') \
                            .num_listing(f'//*[@id="__next"]/div[2]/div/div/div/div[1]/div[2]/div[2]/div[2]/div[{c_other}]/div/div/div/div[3]/div[2]') \
                            .num_owners(f'//*[@id="__next"]/div[2]/div/div/div/div[1]/div[2]/div[2]/div[2]/div[{c_other}]/div/div/div/div[4]/div[2]') \
                            .floor(f'//*[@id="__next"]/div[2]/div/div/div/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/a/div[1]/div[3]/div[1]/div') \
                            .volume(f'//*[@id="__next"]/div[2]/div/div/div/div[1]/div[2]/div[2]/div[2]/div[{c_other}]/div/div/div/div[2]/div[2]/div ') \
                            .build()
                        break
                    except Exception as e:
                        error = e
                        continue
                    # endtry
                # endfor
            # endwith
        except Exception as e:
            error = e
        # endtry

        return nft, error
    # enddef

    def _retrieve_nftrade(self, id: str) -> Tuple[NFTInfo, Exception]:
        url = f'https://nftrade.com/assets/{id}'

        nft = None
        try:
            with _WebFetcher(url, **self.option) as driver:
                error = None

                nft = NFTInfoBuilder(driver, id) \
                    .name('//*[@id="__next"]/div/main/div/div/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]') \
                    .floor('//*[@id="__next"]/div/main/div/div/div[1]/div[1]/div[4]/div[2]/div[1]/div[2]') \
                    .volume('//*[@id="__next"]/div/main/div/div/div[1]/div[1]/div[4]/div[2]/div[4]/div[2]') \
                    .build()
            # endwith
        except Exception as e:
            error = e
        # endtry

        return nft, error
    # enddef

    def _retrieve_solanart(self, id: str) -> Tuple[NFTInfo, Exception]:
        url = f'https://solanart.io/collections/{id}?tab=items'

        nft = None
        try:
            with _WebFetcher(url, **self.option) as driver:
                error = None

                nft = NFTInfoBuilder(driver, id) \
                    .name('//*[@id="__next"]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/h2') \
                    .num_supply('//*[@id="__next"]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]') \
                    .num_owners('//*[@id="__next"]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div[3]/div[1]') \
                    .floor('//*[@id="__next"]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div[5]/div[1]',
                           self._remove_sol_mark) \
                    .volume('//*[@id="__next"]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div[7]/div[1]',
                            self._remove_sol_mark) \
                    .build()
            # endwith
        except Exception as e:
            error = e
        # endtry

        return nft, error
    # enddef

    @staticmethod
    def _remove_sol_mark(s: str) -> str:
        return s.strip(" ◎")

    def _retrieve_magiceden(self, id: str) -> Tuple[NFTInfo, Exception]:
        url = f'https://magiceden.io/marketplace/{id}'

        nft = None
        try:
            with _WebFetcher(url, **self.option) as driver:
                error = None

                nft = NFTInfoBuilder(driver, id) \
                    .name('//*[@id="root"]/div/div/div/div[3]/div[2]/div[1]/div/h1') \
                    .num_listing('//*[@id="root"]/div/div/div/div[3]/div[2]/div[1]/div/div[4]/div/div/div[4]/div/span[2]') \
                    .floor('//*[@id="root"]/div/div/div/div[3]/div[2]/div[1]/div/div[4]/div/div/div[1]/div/span[2]',
                           self._remove_sol_mark) \
                    .volume('//*[@id="root"]/div/div/div/div[3]/div[2]/div[1]/div/div[4]/div/div/div[2]/div/span[2]',
                            self._remove_sol_mark) \
                    .build()
            # endwith
        except Exception as e:
            error = e
        # endtry

        return nft, error
    # enddef

    def _retrieve_xanalia(self, id: str) -> Tuple[NFTInfo, Exception]:
        url = f'https://www.xanalia.com/{id}'

        nft = None
        try:
            with _WebFetcher(url, **self.option) as driver:
                error = None

                nft = NFTInfoBuilder(driver, id) \
                    .name('//*[@id="home-page"]/div/div/div/div[2]/div/div[1]') \
                    .num_supply('//*[@id="home-page"]/div/div/div/div[2]/div/div[2]/div[1]/h5') \
                    .num_owners('//*[@id="home-page"]/div/div/div/div[2]/div/div[2]/div[2]/h5') \
                    .floor('//*[@id="home-page"]/div/div/div/div[2]/div/div[2]/div[3]/h5') \
                    .volume('//*[@id="home-page"]/div/div/div/div[2]/div/div[2]/div[4]/h5') \
                    .build()
            # endwith
        except Exception as e:
            error = e
        # endtry

        return nft, error
    # enddef

    def _retrieve_cetoswap(self, id: str) -> Tuple[NFTInfo, Exception]:
        url = f'https://7pnex-saaaa-aaaai-qbhwa-cai.raw.ic0.app/#/nftmarket/{id}'

        nft = None
        try:
            with _WebFetcher(url, **self.option) as driver:
                error = None

                nft = NFTInfoBuilder(driver, id) \
                    .name('//*[@id="root"]/section/section/main/div/div[2]/div[1]/div[1]') \
                    .num_supply('//*[@id="root"]/section/section/main/div/div[2]/div[1]/div[3]/div[5]/div/div/div/div[1]') \
                    .num_listing('//*[@id="root"]/section/section/main/div/div[2]/div[1]/div[3]/div[1]/div/div/div/div[1]') \
                    .num_owners('//*[@id="root"]/section/section/main/div/div[2]/div[1]/div[3]/div[2]/div/div/div/div[1]') \
                    .floor('//*[@id="root"]/section/section/main/div/div[2]/div[1]/div[3]/div[3]/div/div/div/div[1]/div/div') \
                    .volume('//*[@id="root"]/section/section/main/div/div[2]/div[1]/div[3]/div[4]/div/div/div/div[1]/div/div') \
                    .build()
            # endwith
        except Exception as e:
            error = e
        # endtry

        return nft, error
    # enddef

    def _retrieve_coinbase(self, id: str) -> Tuple[NFTInfo, Exception]:
        url = f'https://nft.coinbase.com/collection/{id}'

        nft = None
        try:
            with _WebFetcher(url, **self.option) as driver:
                error = None

                nft = NFTInfoBuilder(driver, id) \
                    .name('//*[@id="app"]/div[3]/div/div/main/div[1]/div[2]/h1/span/span[1]') \
                    .num_listing('//*[@id="app"]/div[3]/div/div/main/div[1]/div[2]/div[2]/div/div[1]/span[1]') \
                    .num_owners('//*[@id="app"]/div[3]/div/div/main/div[1]/div[2]/div[2]/div/div[2]/span[1]') \
                    .floor('//*[@id="app"]/div[3]/div/div/main/div[1]/div[2]/div[2]/div/div[3]/span[1]',
                           lambda s: s.split(' ')[0]) \
                    .volume('//*[@id="app"]/div[3]/div/div/main/div[1]/div[2]/div[2]/div/div[4]/span[1]',
                            lambda s: s.split(' ')[0]) \
                    .build()
            # endwith
        except Exception as e:
            error = e
        # endtry

        return nft, error
    # enddef

    def _retrieve_ccc(self, id: str) -> Tuple[NFTInfo, Exception]:
        url = f'https://skeh5-daaaa-aaaai-aar4q-cai.raw.ic0.app/#/collection/{id}'

        nft = None
        try:
            with _WebFetcher(url, **self.option) as driver:
                error = None

                nft = NFTInfoBuilder(driver, id) \
                    .name('//*[@id="app"]/div[1]/div[2]/main/div/div[1]/div[2]/h2') \
                    .num_supply('//*[@id="app"]/div[1]/div[2]/main/div/div[1]/div[3]/div[5]/div[2]') \
                    .num_listing('//*[@id="app"]/div[1]/div[2]/main/div/div[1]/div[3]/div[2]/div[2]') \
                    .num_owners('//*[@id="app"]/div[1]/div[2]/main/div/div[1]/div[3]/div[4]/div[2]',
                                lambda s: None if s == 'N/A' else s) \
                    .floor('//*[@id="app"]/div[1]/div[2]/main/div/div[1]/div[3]/div[3]/div[2]/div') \
                    .volume('//*[@id="app"]/div[1]/div[2]/main/div/div[1]/div[3]/div[1]/div[2]/div') \
                    .build()
            # endwith
        except Exception as e:
            error = e
        # endtry

        return nft, error
    # enddef

    def _retrieve_niftygateway(self, id: str) -> Tuple[NFTInfo, Exception]:
        url = f'https://niftygateway.com/marketplace/collectible/{id}'

        nft = None
        try:
            with _WebFetcher(url, **self.option) as driver:
                error = None

                nft = NFTInfoBuilder(driver, id) \
                    .name('//*[@id="root"]/div/div[1]/div/div/div[2]/div[1]/div/div[2]/h2') \
                    .num_listing('//*[@id="tabpanel-0"]/div/div[1]/div/div[1]/p/b') \
                    .num_owners('//*[@id="root"]/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[1]/div/h4/span') \
                    .floor('//*[@id="root"]/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[2]/div/h4/span',
                           lambda s: s.split(' ')[0]) \
                    .volume('//*[@id="root"]/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[4]/div/h4/span',
                            lambda s: s.split(' ')[0]) \
                    .build()
            # endwith
        except Exception as e:
            error = e
        # endtry

        return nft, error
    # enddef

    def _retrieve_empty(self, id: str) -> Tuple[NFTInfo, Exception]:
        raise NotImplementedError
        url = f'{id}'

        nft = None
        try:
            with _WebFetcher(url, **self.option) as driver:
                error = None

                nft = NFTInfoBuilder(driver, id) \
                    .name('') \
                    .num_supply('') \
                    .num_listing('') \
                    .num_owners('') \
                    .floor('') \
                    .volume('') \
                    .build()
            # endwith
        except Exception as e:
            error = e
        # endtry

        return nft, error
    # enddef

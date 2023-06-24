import os
import time
from enum import Enum, auto
from typing import *
from warnings import warn

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService

from nft_market.market import Explorer, Market
from nft_market.nftinfo import NFTInfo, NFTInfoBuilder


class Browser(Enum):
    Firefox = auto()
    Chrome = auto()


class _WebFetcher:
    def __init__(self, url: str, browser: Browser, sec_wait: int, headless: bool):
        self.browser = browser
        self.url = url
        self.sec_wait = sec_wait

        if self.browser == Browser.Firefox:
            options = FirefoxOptions()
        elif self.browser == Browser.Chrome:
            options = ChromeOptions()
        else:
            raise NotImplementedError(self.browser)
        # endif
        options.headless = headless
        options.accept_insecure_certs = True
        options.add_argument('--no-sandbox')
        options.add_argument('--incognito')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-extensions')
        options.add_argument('--proxy-server="direct://"')
        options.add_argument('--proxy-bypass-list=*')
        options.add_argument('--start-maximized')

        self.options = options
    # enddef

    def __enter__(self):
        if self.browser == Browser.Firefox:
            self.driver = webdriver.Firefox(options=self.options,
                                            service=FirefoxService(log_path=os.devnull),
                                            )
        elif self.browser == Browser.Chrome:
            import chromedriver_binary
            _ = chromedriver_binary.chromedriver_filename

            self.driver = webdriver.Chrome(options=self.options,
                                           service=ChromeService(log_path=os.devnull),
                                           )
        else:
            raise NotImplementedError(self.browser)
        # endif

        self.driver.get(url=self.url)
        self.driver.implicitly_wait(self.sec_wait)
        time.sleep(self.sec_wait)

        return self.driver
    # enddef

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.quit()
    # enddef


class Retriever:
    def __init__(self, browser: Browser, sec_wait: int = 10, num_retry: int = 5, verbose: bool = False, headless: bool = True):
        self.option = {
            'browser': browser,
            'sec_wait': sec_wait,
            'headless': headless,
            }
        self.sec_wait = sec_wait
        self.num_retry = num_retry
        self.verbose = verbose
    # enddef

    def fetch(self, market: Union[Market, Explorer], id: str) -> NFTInfo:
        '''Fetch the current information of the specific NFT.
        Args:
            market (nft_market.Market): One of the enums of nft_market.Market
            id (str): The ID of the NFT. You can find it on the URL on the marketplace.

        Returns:
            (nft_market.NFTInfo)
        '''
        if market == Market.OpenSea:
            func = self._retrieve_opensea
        elif market == Explorer.NFTgeek:
            func = self._retrieve_nftgeek
        elif market == Explorer.ICScan:
            func = self._retrieve_icscan
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
        elif market == Market.NFTrade:
            func = self._retrieve_nftrade
        elif market == Market.Solanart:
            func = self._retrieve_solanart
        elif market == Market.MagicEden:
            func = self._retrieve_magiceden
        elif market == Market.XANALIA:
            func = self._retrieve_xanalia
        elif market == Market.Coinbase:
            func = self._retrieve_coinbase
        elif market == Market.NiftyGateway:
            func = self._retrieve_niftygateway
        # deprecated
        elif market == Market.Entrepot:
            warn(f'Please replace NFTGeek instead.')
            func = self._retrieve_entrepot
        elif market == Market.CetoSwap:
            warn(f'Please replace NFTGeek instead.')
            func = self._retrieve_cetoswap
        elif market == Market.CCC:
            warn(f'Please replace NFTGeek instead.')
            func = self._retrieve_ccc
        elif market == Market.Jelly:
            warn(f'Please replace NFTGeek instead.')
            func = self._retrieve_jelly
        elif market == Market.YUMI:
            warn(f'Please replace NFTGeek instead.')
            func = self._retrieve_yumi
        else:
            raise NotImplementedError(market)
        # endif

        num_retry = 0
        error = NotImplemented
        while num_retry <= self.num_retry:
            nft, error = func(id)

            if nft is not None:
                # assert error is None, f'nft: {nft}, error: {error}'
                if error is not None:
                    print(f'[Warning] {error}')
                # endif

                return nft
            else:
                assert error is not None, f'nft: {nft}, error: {error}'

                num_retry += 1
                time.sleep(self.sec_wait)

                if self.verbose:
                    print(f'An error in "{id}" [{num_retry}/{self.num_retry + 1}]')
                # endif
            # endif
        # endwhile

        raise error
    # enddef

    def _retrieve_opensea(self, id: str) -> Tuple[NFTInfo, Exception]:
        url = f'https://opensea.io/collection/{id}'

        nft = None
        with _WebFetcher(url, **self.option) as driver:
            error = None
            try:
                nft = NFTInfoBuilder(driver, id) \
                    .name('//*[@id="main"]/div/div/div/div[3]/div/div/div[1]/div/div[2]/h1') \
                    .num_supply('//*[@id="main"]/div/div/div/div[5]/div/div[1]/div/div[1]/div[1]/span/div[2]/span/div/span[1]/div/div[2]/span/div/div[2]/span') \
                    .floor('//*[@id="main"]/div/div/div/div[5]/div/div[1]/div/div[2]/div[3]/div/div[6]/a/div/span[1]/div', post=lambda s: s.split('\n')[0]) \
                    .volume('//*[@id="main"]/div/div/div/div[5]/div/div[1]/div/div[2]/div[3]/div/div[3]/a/div/span[1]/div', post=lambda s: s.split('\n')[0]) \
                    .build()
            except Exception as e:
                error = e
            # endtry
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

        return nft, error
    # enddef

    def _retrieve_tofunft(self, id: str) -> Tuple[NFTInfo, Exception]:
        url = f'https://tofunft.com/collection/{id}/items'

        nft = None
        with _WebFetcher(url, **self.option) as driver:
            error = None
            try:
                nft = NFTInfoBuilder(driver, id) \
                    .name('//*[@id="__next"]/div[2]/div[1]/div[1]/h1') \
                    .num_listing('//*[@id="__next"]/div[2]/div[1]/div[2]/div[1]/div[3]/div[2]') \
                    .num_owners('//*[@id="__next"]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]') \
                    .floor('//*[@id="__next"]/div[2]/div[1]/div[2]/div[1]/div[5]/div[2]') \
                    .volume('//*[@id="__next"]/div[2]/div[1]/div[2]/div[1]/div[4]/div[2]') \
                    .build()
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
                nft = NFTInfoBuilder(driver, id) \
                    .name('//*[@id="__next"]/div[1]/div[3]/div/div[1]/div/div[3]/div[1]/h1') \
                    .num_supply('//*[@id="__next"]/div[1]/div[3]/div/div[1]/div/div[3]/div[2]/div/div[1]/div[2]') \
                    .num_listing('//*[@id="__next"]/div[1]/div[3]/div/div[1]/div/div[3]/div[2]/div/div[2]/div[2]') \
                    .floor('//*[@id="__next"]/div[1]/div[3]/div/div[1]/div/div[3]/div[2]/div/div[3]/div[2]') \
                    .volume('//*[@id="__next"]/div[1]/div[3]/div/div[1]/div/div[3]/div[2]/div/div[4]/div[2]') \
                    .build()
            except Exception as e:
                error = e
            # endtry
        # endwith

        return nft, error
    # enddef

    def _retrieve_rarible(self, id: str) -> Tuple[NFTInfo, Exception]:
        if id.startswith('0x'):
            url = f'https://rarible.com/collection/{id}'
        else:
            # Seems that "named" projects have a different URL schema.
            url = f'https://rarible.com/{id}/items'
        # endif

        nft = None
        with _WebFetcher(url, **self.option) as driver:
            error = None
            try:
                nft = NFTInfoBuilder(driver, id) \
                    .name('//*[@id="root"]/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div/span') \
                    .num_supply('//*[@id="root"]/div[2]/div/div/div[2]/div/div/div[1]/div[3]/div/div[1]/div[3]/div/span') \
                    .num_owners('//*[@id="root"]/div[2]/div/div/div[2]/div/div/div[1]/div[3]/div/div[1]/div[4]/div/span') \
                    .floor('//*[@id="root"]/div[2]/div/div/div[2]/div/div/div[1]/div[3]/div/div[1]/div[1]/div/span',
                           post=lambda s: s.replace('ETH', '')) \
                    .volume('//*[@id="root"]/div[2]/div/div/div[2]/div/div/div[1]/div[3]/div/div[1]/div[2]/div/span',
                            post=lambda s: s.replace('ETH', '')) \
                    .build()
            except Exception as e:
                error = e
            # endtry
        # endwith

        return nft, error
    # enddef

    def _retrieve_ghostmarket(self, id: str) -> Tuple[NFTInfo, Exception]:
        url = f'https://ghostmarket.io/collection/{id}/?tab=nfts'

        nft = None
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

        return nft, error
    # enddef

    def _retrieve_cryptocom(self, id: str) -> Tuple[NFTInfo, Exception]:
        url = f'https://crypto.com/nft/collection/{id}'

        nft = None
        with _WebFetcher(url, **self.option) as driver:
            error = None
            try:
                nft = NFTInfoBuilder(driver, id) \
                    .name('//*[@id="root"]/div[1]/div/div[3]/div/div[1]/div[2]') \
                    .num_listing('//*[@id="root"]/div[1]/div/div[3]/div/div[3]/div/div[1]/span') \
                    .num_owners('//*[@id="root"]/div[1]/div/div[3]/div/div[3]/div/div[2]/span') \
                    .floor('//*[@id="root"]/div[1]/div/div[3]/div/div[3]/div/div[3]/div/div[2]/div/span[2]/div') \
                    .volume('//*[@id="root"]/div[1]/div/div[3]/div/div[3]/div/div[4]/div/span[2]/div') \
                    .build()
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
                nft = NFTInfoBuilder(driver, id) \
                    .name('//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div') \
                    .num_listing('//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/div[2]/div[1]/div/div[2]/div[1]',
                                 lambda s: s.replace('results', '')) \
                    .floor('//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div[1]/div/div[1]/div[2]/span[3]/span[2]') \
                    .volume('//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div[1]/div/div[1]/div[2]/span[1]/span[2]') \
                    .build()
            except Exception as e:
                error = e
            # endtry
        # endwith

        return nft, error
    # enddef

    def _retrieve_nftrade(self, id: str) -> Tuple[NFTInfo, Exception]:
        url = f'https://nftrade.com/assets/{id}'

        nft = None
        with _WebFetcher(url, **self.option) as driver:
            error = None
            try:
                nft = NFTInfoBuilder(driver, id) \
                    .name('//*[@id="__next"]/div/main/div/div/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]') \
                    .floor('//*[@id="__next"]/div/main/div/div/div[1]/div[1]/div[4]/div[2]/div[1]/div[2]') \
                    .volume('//*[@id="__next"]/div/main/div/div/div[1]/div[1]/div[4]/div[2]/div[4]/div[2]') \
                    .build()
            except Exception as e:
                error = e
            # endtry
        # endwith

        return nft, error
    # enddef

    def _retrieve_solanart(self, id: str) -> Tuple[NFTInfo, Exception]:
        url = f'https://solanart.io/collections/{id}?tab=items'

        nft = None
        with _WebFetcher(url, **self.option) as driver:
            error = None
            try:
                nft = NFTInfoBuilder(driver, id) \
                    .name('//*[@id="__next"]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/h2') \
                    .num_supply('//*[@id="__next"]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]') \
                    .num_owners('//*[@id="__next"]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div[3]/div[1]') \
                    .floor('//*[@id="__next"]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div[5]/div[1]',
                           self._remove_sol_mark) \
                    .volume('//*[@id="__next"]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div[7]/div[1]',
                            self._remove_sol_mark) \
                    .build()
            except Exception as e:
                error = e
            # endtry
        # endwith

        return nft, error
    # enddef

    @staticmethod
    def _remove_sol_mark(s: str) -> str:
        return s.strip(" ◎")

    def _retrieve_magiceden(self, id: str) -> Tuple[NFTInfo, Exception]:
        url = f'https://magiceden.io/marketplace/{id}'

        nft = None
        with _WebFetcher(url, **self.option) as driver:
            error = None
            try:
                nft = NFTInfoBuilder(driver, id) \
                    .name('//*[@id="root"]/div/div/div/div[3]/div[2]/div[1]/div/h1') \
                    .num_listing('//*[@id="root"]/div/div/div/div[3]/div[2]/div[1]/div/div[4]/div/div/div[4]/div/span[2]') \
                    .floor('//*[@id="root"]/div/div/div/div[3]/div[2]/div[1]/div/div[4]/div/div/div[1]/div/span[2]',
                           self._remove_sol_mark) \
                    .volume('//*[@id="root"]/div/div/div/div[3]/div[2]/div[1]/div/div[4]/div/div/div[2]/div/span[2]',
                            self._remove_sol_mark) \
                    .build()
            except Exception as e:
                error = e
            # endtry
        # endwith

        return nft, error
    # enddef

    def _retrieve_xanalia(self, id: str) -> Tuple[NFTInfo, Exception]:
        url = f'https://www.xanalia.com/{id}'

        nft = None
        with _WebFetcher(url, **self.option) as driver:
            error = None
            try:
                nft = NFTInfoBuilder(driver, id) \
                    .name('//*[@id="home-page"]/div/div/div/div[2]/div/div[1]') \
                    .num_supply('//*[@id="home-page"]/div/div/div/div[2]/div/div[2]/div[1]/h5') \
                    .num_owners('//*[@id="home-page"]/div/div/div/div[2]/div/div[2]/div[2]/h5') \
                    .floor('//*[@id="home-page"]/div/div/div/div[2]/div/div[2]/div[3]/h5') \
                    .volume('//*[@id="home-page"]/div/div/div/div[2]/div/div[2]/div[4]/h5') \
                    .build()
            except Exception as e:
                error = e
            # endtry
        # endwith

        return nft, error
    # enddef

    def _retrieve_cetoswap(self, id: str) -> Tuple[NFTInfo, Exception]:
        url = f'https://7pnex-saaaa-aaaai-qbhwa-cai.raw.ic0.app/#/nftmarket/{id}'

        nft = None
        with _WebFetcher(url, **self.option) as driver:
            error = None
            try:
                nft = NFTInfoBuilder(driver, id) \
                    .name('//*[@id="root"]/section/section/main/div/div[2]/div[1]/div[1]') \
                    .num_supply('//*[@id="root"]/section/section/main/div/div[2]/div[1]/div[3]/div[5]/div/div/div/div[1]') \
                    .num_listing('//*[@id="root"]/section/section/main/div/div[2]/div[1]/div[3]/div[1]/div/div/div/div[1]') \
                    .num_owners('//*[@id="root"]/section/section/main/div/div[2]/div[1]/div[3]/div[2]/div/div/div/div[1]') \
                    .floor('//*[@id="root"]/section/section/main/div/div[2]/div[1]/div[3]/div[3]/div/div/div/div[1]/div/div') \
                    .volume('//*[@id="root"]/section/section/main/div/div[2]/div[1]/div[3]/div[4]/div/div/div/div[1]/div/div') \
                    .build()
            except Exception as e:
                error = e
            # endtry
        # endwith

        return nft, error
    # enddef

    def _retrieve_coinbase(self, id: str) -> Tuple[NFTInfo, Exception]:
        url = f'https://nft.coinbase.com/collection/{id}'

        nft = None
        with _WebFetcher(url, **self.option) as driver:
            error = None
            try:
                nft = NFTInfoBuilder(driver, id) \
                    .name('//*[@id="app"]/div[3]/div/div/main/div[1]/div[2]/h1/span/span[1]') \
                    .num_listing('//*[@id="app"]/div[3]/div/div/main/div[1]/div[2]/div[2]/div/div[1]/span[1]') \
                    .num_owners('//*[@id="app"]/div[3]/div/div/main/div[1]/div[2]/div[2]/div/div[2]/span[1]') \
                    .floor('//*[@id="app"]/div[3]/div/div/main/div[1]/div[2]/div[2]/div/div[3]/span[1]/div/div/div/span[1]',
                           lambda s: s.replace('ETH', '')) \
                    .volume('//*[@id="app"]/div[3]/div/div/main/div[1]/div[2]/div[2]/div/div[4]/span[1]',
                            lambda s: s.replace('ETH', '')) \
                    .build()
            except Exception as e:
                error = e
            # endtry
        # endwith

        return nft, error
    # enddef

    def _retrieve_ccc(self, id: str) -> Tuple[NFTInfo, Exception]:
        url = f'https://skeh5-daaaa-aaaai-aar4q-cai.raw.ic0.app/#/collection/{id}'

        nft = None
        with _WebFetcher(url, **self.option) as driver:
            error = None
            try:
                nft = NFTInfoBuilder(driver, id) \
                    .name('//*[@id="app"]/div[1]/div[2]/main/div/div[1]/div[2]/h2') \
                    .num_supply('//*[@id="app"]/div[1]/div[2]/main/div/div[1]/div[3]/div[5]/div[2]') \
                    .num_listing('//*[@id="app"]/div[1]/div[2]/main/div/div[1]/div[3]/div[2]/div[2]') \
                    .num_owners('//*[@id="app"]/div[1]/div[2]/main/div/div[1]/div[3]/div[4]/div[2]',
                                lambda s: None if s == 'N/A' else s) \
                    .floor('//*[@id="app"]/div[1]/div[2]/main/div/div[1]/div[3]/div[3]/div[2]/div') \
                    .volume('//*[@id="app"]/div[1]/div[2]/main/div/div[1]/div[3]/div[1]/div[2]/div') \
                    .build()
            except Exception as e:
                error = e
            # endtry
        # endwith

        return nft, error
    # enddef

    def _retrieve_niftygateway(self, id: str) -> Tuple[NFTInfo, Exception]:
        url = f'https://niftygateway.com/marketplace/collectible/{id}'

        nft = None
        with _WebFetcher(url, **self.option) as driver:
            error = None
            try:
                nft = NFTInfoBuilder(driver, id) \
                    .name('//*[@id="root"]/div/div[1]/div/div/div[2]/div[1]/div/div[2]/h2') \
                    .num_listing('//*[@id="tabpanel-0"]/div/div[1]/div/div[1]/p/b') \
                    .num_owners('//*[@id="root"]/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[1]/div/h4/span') \
                    .floor('//*[@id="root"]/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[2]/div/h4/span',
                           lambda s: s.split(' ')[0]) \
                    .volume('//*[@id="root"]/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[4]/div/h4/span',
                            lambda s: s.split(' ')[0]) \
                    .build()
            except Exception as e:
                error = e
            # endtry
        # endwith

        return nft, error
    # enddef

    def _retrieve_jelly(self, id: str) -> Tuple[NFTInfo, Exception]:
        url = 'https://jelly.xyz/'

        nft = None
        with _WebFetcher(url, **self.option) as driver:
            error = None
            try:
                nft = NFTInfoBuilder(driver, id) \
                    .name('//*[@id="theme-root-element"]/div[3]/div[1]/div/div[2]/div[1]/div[2]/h2') \
                    .num_supply('//*[@id="radix-6-content-items"]/div/div[2]/div/div[1]/div[1]/div[1]/div[1]/div[2]') \
                    .num_owners('//*[@id="radix-6-content-items"]/div/div[2]/div/div[1]/div[1]/div[1]/div[2]/div[2]') \
                    .floor('//*[@id="radix-6-content-items"]/div/div[2]/div/div[1]/div[1]/div[1]/div[3]/div[2]') \
                    .volume('//*[@id="radix-6-content-items"]/div/div[2]/div/div[1]/div[1]/div[1]/div[4]/div[2]') \
                    .build()
            except Exception as e:
                error = e
            # endtry
        # endwith

        return nft, error
    # enddef

    def _retrieve_yumi(self, id: str) -> Tuple[NFTInfo, Exception]:
        url = f'https://tppkg-ziaaa-aaaal-qatrq-cai.raw.ic0.app/market/collection-nft-list?id={id}'

        nft = None
        with _WebFetcher(url, **self.option) as driver:
            error = None
            try:
                nft = NFTInfoBuilder(driver, id) \
                    .name('//*[@id="App"]/section/div/div/div/div/div[1]/div[2]/div[2]') \
                    .num_listing('//*[@id="App"]/section/div/div/div/div/div[1]/div[3]/div[1]/span[1]') \
                    .num_owners('//*[@id="App"]/section/div/div/div/div/div[1]/div[3]/div[2]/span[1]') \
                    .floor('//*[@id="App"]/section/div/div/div/div/div[1]/div[3]/div[3]/span[1]') \
                    .volume('//*[@id="App"]/section/div/div/div/div/div[1]/div[3]/div[4]/span[1]') \
                    .build()
            except Exception as e:
                error = e
            # endtry
        # endwith

        return nft, error
    # enddef

    def _retrieve_nftgeek(self, id: str) -> Tuple[NFTInfo, Exception]:
        url_base = f'https://t5t44-naaaa-aaaah-qcutq-cai.raw.ic0.app/collection/{id}'
        url = f'{url_base}/summary'

        concat_space = lambda s: s.replace(' ', '')

        nft = None
        with _WebFetcher(url, **self.option) as driver:
            error = None
            try:
                nft = NFTInfoBuilder(driver, id) \
                    .name('//*[@id="root"]/div[2]/div[2]/div/div/div[1]/div/div/span') \
                    .num_supply('//*[@id="root"]/div[2]/div[2]/div/div/div[2]/div[3]/div/div[1]/div/div[2]/span',
                                post=concat_space) \
                    .num_listing('//*[@id="root"]/div[2]/div[2]/div/div/div[2]/div[3]/div/div[6]/div/div[2]/span',
                                 post=concat_space) \
                    .floor('//*[@id="root"]/div[2]/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[2]/span',
                           post=concat_space) \
                    .volume('//*[@id="root"]/div[2]/div[2]/div/div/div[2]/div[3]/div/div[4]/div/div[2]/span',
                            post=concat_space) \
                    .build()
            except Exception as e:
                error = e
            # endtry
        # endwith

        url_holders = f'{url_base}/holders'
        with _WebFetcher(url_holders, **self.option) as driver:
            error_holders = None
            try:
                nft_holders = NFTInfoBuilder(driver, id) \
                    .name('//*[@id="root"]/div[2]/div[2]/div/div/div[1]/div/div/span') \
                    .num_owners('//*[@id="root"]/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[2]/span',
                                post=concat_space) \
                    .build()
                nft.num_owners = nft_holders.num_owners
            except Exception as e:
                error_holders = e
            # endtry
        # endwith

        return nft, error
    # enddef

    def _retrieve_icscan(self, id: str) -> Tuple[NFTInfo, Exception]:
        url = f'https://icscan.io/nft/collection/{id}'

        nft = None
        with _WebFetcher(url, **self.option) as driver:
            error = None
            try:
                nft = NFTInfoBuilder(driver, id) \
                    .name('//*[@id="__next"]/div/div/main/div[2]/div[4]/div/div[1]/div[1]/div/div[1]') \
                    .num_supply('//*[@id="__next"]/div/div/main/div[2]/div[4]/div/div[2]/div[2]/div[1]/div[2]/div[2]') \
                    .num_listing('//*[@id="__next"]/div/div/main/div[2]/div[4]/div/div[2]/div[2]/div[1]/div[3]/div[2]') \
                    .num_owners('//*[@id="__next"]/div/div/main/div[2]/div[4]/div/div[2]/div[1]/div[2]/div[2]',
                                post=lambda s: s.split('\n')[0]) \
                    .floor('//*[@id="__next"]/div/div/main/div[2]/div[4]/div/div[2]/div[1]/div[1]/div[2]',
                           post=lambda s: s.split(' ')[0]) \
                    .volume('//*[@id="__next"]/div/div/main/div[2]/div[4]/div/div[2]/div[2]/div[2]/div[1]/div[2]',
                            post=lambda s: s.replace('ICP', '')) \
                    .build()
            except Exception as e:
                error = e
            # endtry
        # endwith

        return nft, error
    # enddef

    def _retrieve_empty(self, id: str) -> Tuple[NFTInfo, Exception]:
        raise NotImplementedError
        url = f'{id}'

        nft = None
        with _WebFetcher(url, **self.option) as driver:
            error = None
            try:
                nft = NFTInfoBuilder(driver, id) \
                    .name('') \
                    .num_supply('') \
                    .num_listing('') \
                    .num_owners('') \
                    .floor('') \
                    .volume('') \
                    .build()
            except Exception as e:
                error = e
            # endtry
        # endwith

        return nft, error
    # enddef

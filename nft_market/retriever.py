import os
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.webdriver import Service

from nft_market.market import Market
from nft_market.nftinfo import NFTInfo


class _NFTWebDriver:
    def __init__(self, url: str, sec_wait: int):
        self.url = url
        self.sec_wait = sec_wait

        options = Options()
        options.add_argument('--headless')
        self.options = options
    # enddef

    def __enter__(self):
        self.driver = webdriver.Firefox(options=self.options, service=Service(log_path=os.devnull))
        self.driver.switch_to.new_window()
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
    s = s.replace(',', '').replace('<', '').replace('>', '').replace('$', '') \
        .replace('k', '*1000').replace('K', '*1000') \
        .replace('M', '*1000000') \
        .replace('B', '*1000000000')
    f = float(eval(s))

    return f


def _text2int(s: str) -> int:
    return int(_text2float(s))


class Retriever:
    def __init__(self, sec_wait: int = 10, num_retry: int = 5, verbose: bool = False):
        self.option = {
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
        elif market == Market.Tofu:
            func = self._retrieve_tofu
        elif market == Market.PancakeSwap:
            func = self._retrieve_pancakeswap
        elif market == Market.Rarible:
            func = self._retrieve_rarible
        elif market == Market.GhostMarket:
            func = self._retrieve_ghostmarket
        else:
            raise NotImplementedError(market)
        # endif

        num_retry = 0
        error = NotImplemented
        while num_retry <= self.num_retry:
            nft = None
            try:
                nft = func(id)
                if nft is None:
                    raise ValueError(id)
                # endif
            except Exception as e:
                error = e
                num_retry += 1
                time.sleep(self.sec_wait)
            # endtry

            if nft is not None:
                return nft
            # endif
        # endwhile

        raise error
    # enddef

    def _retrieve_opensea(self, id: str) -> NFTInfo:
        url = f'https://opensea.io/collection/{id}'

        nft = None
        with _NFTWebDriver(url, **self.option) as driver:
            for c1 in [4, 5]:
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
                except NoSuchElementException as e:
                    if self.verbose:
                        print(e)
                    # endif
                    continue
                # endtry
            # endfor
        # endwith

        return nft
    # enddef

    def _retrieve_entrepot(self, id: str) -> NFTInfo:
        url = f'https://entrepot.app/marketplace/{id}'

        nft = None
        with _NFTWebDriver(url, **self.option) as driver:
            for c1 in [2, 3]:
                try:
                    name = driver.find_element(by=By.XPATH,
                                               value=f'//*[@id="root"]/main/div/div[1]/div/div[1]/div/div[3]/h1').text
                    num_items_all = None
                    num_listing = _text2int(driver.find_element(by=By.XPATH,
                                                                value='//*[@id="root"]/main/div/div[1]/div/div[1]/div/div[2]/div[1]/div/div[2]/strong').text)
                    num_owners = None
                    floor = _text2float(driver.find_element(by=By.XPATH,
                                                            value=f'//*[@id="mainListings"]/div[2]/div/div[2]/div[2]/div/div[1]/div/a/div[{c1}]/div/div[4]/p').text)
                    volume = _text2float(driver.find_element(by=By.XPATH,
                                                             value='//*[@id="root"]/main/div/div[1]/div/div[1]/div/div[2]/div[1]/div/div[1]/strong').text)
                    nft = NFTInfo(id=id, name=name,
                                  num_items_all=num_items_all, num_listing=num_listing, num_owners=num_owners,
                                  floor=floor, volume=volume)
                    break
                except NoSuchElementException as e:
                    if self.verbose:
                        print(e)
                    # endif
                    continue
                # endtry
            # endfor
        # endwith

        return nft
    # enddef

    def _retrieve_tofu(self, id: str) -> NFTInfo:
        url = f'https://tofunft.com/collection/{id}/items'

        nft = None
        with _NFTWebDriver(url, **self.option) as driver:
            try:
                name = driver.find_element(by=By.XPATH,
                                           value=f'//*[@id="__next"]/div[2]/div[1]/div[1]/h1').text
                num_items_all = None
                num_listing = _text2int(driver.find_element(by=By.XPATH,
                                                            value='//*[@id="__next"]/div[2]/div[1]/div[2]/div[1]/div[3]/div[2]').text)
                num_owners = _text2int(driver.find_element(by=By.XPATH,
                                                           value='//*[@id="__next"]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]').text)
                floor = _text2float(driver.find_element(by=By.XPATH,
                                                        value='//*[@id="__next"]/div[2]/div[1]/div[2]/div[1]/div[5]/div[2]').text)
                volume = _text2float(driver.find_element(by=By.XPATH,
                                                         value='//*[@id="__next"]/div[2]/div[1]/div[2]/div[1]/div[4]/div[2] ').text)

                nft = NFTInfo(id=id, name=name,
                              num_items_all=num_items_all, num_listing=num_listing, num_owners=num_owners,
                              floor=floor, volume=volume)
            except Exception as e:
                if self.verbose:
                    print(e)
                # endif
            # endtry
        # endwith

        return nft
    # enddef

    def _retrieve_pancakeswap(self, id: str) -> NFTInfo:
        url = f'https://pancakeswap.finance/nfts/collections/{id}'

        nft = None
        with _NFTWebDriver(url, **self.option) as driver:
            try:
                name = driver.find_element(by=By.XPATH,
                                           value=f'//*[@id="__next"]/div[1]/div[3]/div/div[1]/div/div[3]/div[1]/h1').text
                num_items_all = _text2int(driver.find_element(by=By.XPATH,
                                                              value='//*[@id="__next"]/div[1]/div[3]/div/div[1]/div/div[3]/div[2]/div/div[1]/div[2]').text)
                num_listing = _text2int(driver.find_element(by=By.XPATH,
                                                            value='//*[@id="__next"]/div[1]/div[3]/div/div[1]/div/div[3]/div[2]/div/div[2]/div[2]').text)
                num_owners = None
                floor = _text2float(driver.find_element(by=By.XPATH,
                                                        value='//*[@id="__next"]/div[1]/div[3]/div/div[1]/div/div[3]/div[2]/div/div[3]/div[2]').text)
                volume = _text2float(driver.find_element(by=By.XPATH,
                                                         value='//*[@id="__next"]/div[1]/div[3]/div/div[1]/div/div[3]/div[2]/div/div[4]/div[2]').text)

                nft = NFTInfo(id=id, name=name,
                              num_items_all=num_items_all, num_listing=num_listing, num_owners=num_owners,
                              floor=floor, volume=volume)
            except Exception as e:
                if self.verbose:
                    print(e)
                # endif
            # endtry
        # endwith

        return nft
    # enddef

    def _retrieve_rarible(self, id: str) -> NFTInfo:
        if id.startswith('0x'):
            url = f'https://rarible.com/collection/{id}/items'
        else:
            # Seems that "named" projects have a different URL schema.
            url = f'https://rarible.com/{id}/items'
        # endif

        nft = None
        with _NFTWebDriver(url, **self.option) as driver:
            try:
                name = driver.find_element(by=By.XPATH,
                                           value=f'//*[@id="root"]/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/div[1]/span').text
                num_items_all = _text2int(driver.find_element(by=By.XPATH,
                                                              value='//*[@id="root"]/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/div[2]/div[4]/span[2]/span').text)
                num_listing = None
                num_owners = _text2int(driver.find_element(by=By.XPATH,
                                                           value='//*[@id="root"]/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/div[2]/div[5]/span[2]/span').text)
                floor = _text2float(driver.find_element(by=By.XPATH,
                                                        value='//*[@id="root"]/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/span[2]/span').text)
                volume = _text2float(driver.find_element(by=By.XPATH,
                                                         value='//*[@id="root"]/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/div[2]/div[6]/span[2]/span').text)

                nft = NFTInfo(id=id, name=name,
                              num_items_all=num_items_all, num_listing=num_listing, num_owners=num_owners,
                              floor=floor, volume=volume)
            except Exception as e:
                if self.verbose:
                    print(e)
                # endif
            # endtry
        # endwith

        return nft
    # enddef

    def _retrieve_ghostmarket(self, id: str) -> NFTInfo:
        url = f'https://ghostmarket.io/collection/{id}'

        nft = None
        with _NFTWebDriver(url, **self.option) as driver:
            for c_floor in ['//*[@id="__layout"]/div/section/div/div[2]/div[1]/div/div[3]/span/div[2]/div/div/div[1]',
                            '//*[@id="__layout"]/div/section/div/div[2]/div[1]/div/div[3]/div/div/div[1]']:
                try:
                    name = driver.find_element(by=By.XPATH,
                                               value=f'//*[@id="__layout"]/div/section/div/div[1]/div[3]/span[1]').text
                    num_items_all = _text2int(driver.find_element(by=By.XPATH,
                                                                  value='//*[@id="__layout"]/div/section/div/div[2]/div[1]/div/div[1]/div/div/div[1]').text)
                    num_listing = None
                    num_owners = _text2int(driver.find_element(by=By.XPATH,
                                                               value='//*[@id="__layout"]/div/section/div/div[2]/div[1]/div/div[2]/div/div/div[1]').text)
                    floor = _text2float(driver.find_element(by=By.XPATH,
                                                            value=c_floor).text)
                    volume = _text2float(driver.find_element(by=By.XPATH,
                                                              value='//*[@id="__layout"]/div/section/div/div[2]/div[1]/div/div[4]/div/div/div[1]').text)

                    nft = NFTInfo(id=id, name=name,
                                  num_items_all=num_items_all, num_listing=num_listing, num_owners=num_owners,
                                  floor=floor, volume=volume)
                    break
                except NoSuchElementException as e:
                    if self.verbose:
                        print(e)
                    # endif
                    continue
                # endtry
            # endfor
        # endwith

        return nft
    # enddef

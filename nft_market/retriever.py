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
    s = s.replace(',', '').replace('<', '').replace('>', '') \
        .replace('k', '*1000').replace('K', '*1000') \
        .replace('M', '*1000000')
    f = float(eval(s))

    return f


def _text2int(s: str) -> int:
    return int(_text2float(s))


class Retriever:
    def __init__(self, sec_wait: int = 10):
        self.option = {
            'sec_wait': sec_wait
            }
        self.sec_wait = sec_wait
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
        else:
            raise NotImplementedError(market)
        # endif

        num_retry = 0
        error = NotImplemented
        while num_retry < 5:
            try:
                return func(id)
            except Exception as e:
                error = e
                num_retry += 1
                time.sleep(self.sec_wait)
            # endtry
        # endwhile

        raise error
    # enddef

    def _retrieve_opensea(self, id: str) -> NFTInfo:
        url = f'https://opensea.io/collection/{id}'

        nft = NotImplemented
        with _NFTWebDriver(url, **self.option) as driver:
            for c1 in [4, 5]:
                try:
                    num_items_all = None
                    num_listing = _text2int(driver.find_element(by=By.XPATH,
                                                                value=f'//*[@id="main"]/div/div/div[1]/div[2]/div[{c1}]/div/div[1]/a/div/div[1]/div/span/div').text)
                    num_owners = _text2int(driver.find_element(by=By.XPATH,
                                                               value=f'//*[@id="main"]/div/div/div[1]/div[2]/div[{c1}]/div/div[2]/a/div/div[1]/div/span/div').text)
                    floor = _text2float(driver.find_element(by=By.XPATH,
                                                            value=f'//*[@id="main"]/div/div/div[1]/div[2]/div[{c1}]/div/div[3]/a/div/div[1]/div/span/div').text)
                    volume = _text2float(driver.find_element(by=By.XPATH,
                                                             value=f'//*[@id="main"]/div/div/div[1]/div[2]/div[{c1}]/div/div[4]/a/div/div[1]/div/span/div').text)

                    nft = NFTInfo(name=id,
                                  num_items_all=num_items_all, num_listing=num_listing, num_owners=num_owners,
                                  floor=floor, volume=volume)
                    break
                except NoSuchElementException as e:
                    continue
                # endtry
            # endfor
        # endwith

        return nft
    # enddef

    def _retrieve_entrepot(self, id: str) -> NFTInfo:
        url = f'https://entrepot.app/marketplace/{id}'

        nft = NotImplemented
        with _NFTWebDriver(url, **self.option) as driver:
            for c1 in [2, 3]:
                try:
                    num_items_all = None
                    num_listing = _text2int(driver.find_element(by=By.XPATH,
                                                                value='//*[@id="root"]/main/div/div[1]/div/div[1]/div/div[2]/div[1]/div/div[2]/strong').text)
                    num_owners = None
                    floor = _text2float(driver.find_element(by=By.XPATH,
                                                            value=f'//*[@id="mainListings"]/div[2]/div/div[2]/div[2]/div/div[1]/div/a/div[{c1}]/div/div[4]/p').text)
                    volume = _text2float(driver.find_element(by=By.XPATH,
                                                             value='//*[@id="root"]/main/div/div[1]/div/div[1]/div/div[2]/div[1]/div/div[1]/strong').text)
                    nft = NFTInfo(name=id,
                                  num_items_all=num_items_all, num_listing=num_listing, num_owners=num_owners,
                                  floor=floor, volume=volume)
                except NoSuchElementException as e:
                    continue
                # endtry
            # endfor
        # endwith

        return nft
    # enddef

    def _retrieve_tofu(self, id: str) -> NFTInfo:
        url = f'https://tofunft.com/collection/{id}/items'

        nft = NotImplemented
        with _NFTWebDriver(url, **self.option) as driver:
            try:
                num_items_all = None
                num_listing = _text2int(driver.find_element(by=By.XPATH,
                                                            value='//*[@id="__next"]/div[2]/div[1]/div[2]/div[1]/div[3]/div[2]').text)
                num_owners = _text2int(driver.find_element(by=By.XPATH,
                                                           value='//*[@id="__next"]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]').text)
                floor = _text2float(driver.find_element(by=By.XPATH,
                                                        value='//*[@id="__next"]/div[2]/div[1]/div[2]/div[1]/div[5]/div[2]').text)
                volume = _text2float(driver.find_element(by=By.XPATH,
                                                         value='//*[@id="__next"]/div[2]/div[1]/div[2]/div[1]/div[4]/div[2] ').text)

                nft = NFTInfo(name=id,
                              num_items_all=num_items_all, num_listing=num_listing, num_owners=num_owners,
                              floor=floor, volume=volume)
            except NoSuchElementException as e:
                pass
            # endtry
        # endwith

        return nft
    # enddef

    def _retrieve_pancakeswap(self, id: str) -> NFTInfo:
        url = f'https://pancakeswap.finance/nfts/collections/{id}'

        nft = NotImplemented
        with _NFTWebDriver(url, **self.option) as driver:
            num_items_all = _text2int(driver.find_element(by=By.XPATH,
                                                          value='//*[@id="__next"]/div[1]/div[3]/div/div[1]/div/div[3]/div[2]/div/div[1]/div[2]').text)
            num_listing = _text2int(driver.find_element(by=By.XPATH,
                                                        value='//*[@id="__next"]/div[1]/div[3]/div/div[1]/div/div[3]/div[2]/div/div[2]/div[2]').text)
            num_owners = None
            floor = _text2float(driver.find_element(by=By.XPATH,
                                                    value='//*[@id="__next"]/div[1]/div[3]/div/div[1]/div/div[3]/div[2]/div/div[3]/div[2]').text)
            volume = _text2float(driver.find_element(by=By.XPATH,
                                                     value='//*[@id="__next"]/div[1]/div[3]/div/div[1]/div/div[3]/div[2]/div/div[4]/div[2]').text)

            nft = NFTInfo(name=id,
                          num_items_all=num_items_all, num_listing=num_listing, num_owners=num_owners,
                          floor=floor, volume=volume)
        # endwith

        return nft
    # enddef

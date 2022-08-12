from enum import Enum, auto


class Market(Enum):
    OpenSea = auto()
    tofuNFT = auto()
    PancakeSwap = auto()
    Rarible = auto()
    GhostMarket = auto()
    Cryptocom = auto()
    Gem = auto()
    NFTrade = auto()
    Solanart = auto()
    MagicEden = auto()
    XANALIA = auto()
    Coinbase = auto()
    NiftyGateway = auto()
    # deprecated
    Entrepot = auto()
    CetoSwap = auto()
    CCC = auto()
    Jelly = auto()
    YUMI = auto()


class Explorer(Enum):
    NFTgeek = auto()
    ICScan = auto()

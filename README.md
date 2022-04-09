# nft-market

[![test](https://github.com/ukaznil/nft-market/actions/workflows/pytest.yml/badge.svg)](https://github.com/ukaznil/nft-market/actions/workflows/pytest.yml)

## What is it?

**nft-market** is a Python library by which current market information of NFTs on several famous NFT markets (OpenSea,
Tofu, PancakeSwap, etc) can be obtained.

## Main features

**nft-market** provides simple APIs that return market information by your giving both the ID for a specific NFT and the
marketplace.

```python
from nft_market import Market, Retriever

r = Retriever()
print(r.fetch(Market.OpenSea, 'boredapeyachtclub'))  # Bored Ape Yacht Club

# [Output]
# type: nft_market.NFTInfo
# NFTInfo(name='boredapeyachtclub', num_items_all=None, num_listing=10000, num_owners=6400, floor=110.0, volume=487100.0)
```

### Currently supported maketplaces

At this moment, the following marketplaces are supported in **nft-market**.

- [OpenSea](https://opensea.io/)
- [Entrepot](https://entrepot.app/)
- [Tofu](https://tofunft.com/)
- [PancakeSwap](https://pancakeswap.finance/nfts)

Other marketplaces will be added in the list in the future. You can, off course, request them in issues if needed
immediately.

## Installation

You can install **nft-market** by pip.

```shell
$ pip install nft-market
```

Also, as **nft-market** depends on Firefox and its driver, you need to install them.

```shell
[mac]
$ brew install firefox

[ubuntu]
$ sudo apt install firefox
```

Besides, all Python dependencies are listed up in `requirements.txt`. Please install them
by `$ pip install -r requirements.txt` if you install **nft-market** not by pip but by cloning from GitHub.
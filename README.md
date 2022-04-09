# nft-market

## What is it?

*nft-market* is a Python library by which current market information of NFTs on several famous NFT markets (OpenSea,
Tofu, PancakeSwap, etc) can be obtained.

## Main Features

*nft-market* provides simple APIs that return market information by your giving both the ID for a specific NFT and the
marketplace.

```python
from nft_market import Market, Retriever

r = Retriever()
print(r.fetch(Market.OpenSea, 'boredapeyachtclub'))  # Bored Ape Yacht Club

# [Output]
# type: nft_market.NFTInfo
# NFTInfo(name='boredapeyachtclub', num_items_all=None, num_listing=10000, num_owners=6400, floor=110.0, volume=487100.0)
```

## Dependencies

As *nft-market* depends on Firefox and its driver, you need to install them.

```shell
[mac]
$ brew install firefox

[ubuntu]
$ sudo apt install firefox
```

Besides, all Python dependencies are listed up in `requirements.txt`.

Please install them by `$ pip install -r requirements.txt` if you install *nft-market* not by pip but cloning from
GitHub.

## Requests for adding marketplaces

Requests (bug reports, adding marketplaces, etc) are always welcome!
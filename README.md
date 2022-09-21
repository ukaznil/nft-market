# nft-market

[![PyPI version](https://badge.fury.io/py/nft-market.svg)](https://badge.fury.io/py/nft-market)
[![test](https://github.com/ukaznil/nft-market/actions/workflows/pytest.yml/badge.svg?branch=master)](https://github.com/ukaznil/nft-market/actions/workflows/pytest.yml)
[![Downloads](https://pepy.tech/badge/nft-market)](https://pepy.tech/project/nft-market)

## What is it?

**nft-market** is a Python library by which current market information of NFTs on several famous NFT markets (OpenSea,
Magic Eden, tofuNFT, PancakeSwap, etc) can be obtained.

## Main features

**nft-market** provides simple APIs that return market information just by your giving the following arguments.

- The marketplace (from `nft_market.Market`)
- the ID of a specific NFT ([See the below in detail](https://github.com/ukaznil/nft-market#how-to-get-the-id-of-a-nft))

```python
from nft_market import Market, Retriever

r = Retriever()
print(r.fetch(Market.OpenSea, 'boredapeyachtclub'))  # Bored Ape Yacht Club

# [Output]
# type: nft_market.NFTInfo
# NFTInfo(id='boredapeyachtclub', name='Bored Ape Yacht Club', num_supply=None, num_listing=10000, num_owners=6400, floor=111.0, volume=487600.0)
```

### Currently supported marketplaces

At this moment, the following marketplaces are supported in **nft-market**.

- [OpenSea](https://opensea.io/)
- [Entrepot](https://entrepot.app/) (depreacated)
- [tofuNFT](https://tofunft.com/)
- [PancakeSwap](https://pancakeswap.finance/nfts/)
- [Rarible](https://rarible.com/)
- [GhostMarket](https://ghostmarket.io/)
- [Crypto.com](https://crypto.com/nft/)
- [Gem](https://www.gem.xyz/)
- [NFTrade](https://nftrade.com/)
- [Solanart](https://solanart.io/)
- [Magic Eden](https://magiceden.io/)
- [XANALIA](https://www.xanalia.com/)
- [CetoSwap](https://7pnex-saaaa-aaaai-qbhwa-cai.raw.ic0.app/) (depreacated)
- [Coinbase](https://nft.coinbase.com/)
- [CCC](https://skeh5-daaaa-aaaai-aar4q-cai.raw.ic0.app/) (depreacated)
- [Nifty Gateway](https://niftygateway.com/)
- [Jelly](https://jelly.xyz/) (depreacated)
- [YUMI](https://tppkg-ziaaa-aaaal-qatrq-cai.raw.ic0.app/)

Other marketplaces will be added into the list in the future. You can, off course, request them in issues if needed
immediately. Either PRs or issues are always welcome!

### Currently supported explorers

The following explorers are supported in **nft-market**.
If possible, using these explorers is recommended rather than using the above marketplaces, such as Enterpot, for more stability.

- [ICScan](https://icscan.io/nft) (Supporting: ICP)
- [NFTgeek](https://t5t44-naaaa-aaaah-qcutq-cai.raw.ic0.app/) (Supporting: ICP)

### How to get the ID of a NFT?

Although it depends on which marketplace you use, you can basically find it in the URL.

#### Example 1: OpenSea

When you want to retrieve the information of the NFT of [Bored Ape Yacht Club
](https://opensea.io/collection/boredapeyachtclub), the URL looks like `https://opensea.io/collection/boredapeyachtclub`
. In this URL, what differs according to a NFT is the part of `boredapeyachtclub`, which is all you need to use **
nft-market**.

#### Example 2: tofuNFT

URLs look like `https://tofunft.com/collection/astardegens/items`. In this case, what **nft-market** requires is only
the part of `astardegens`.

#### Other examples

We have several examples of the usage in [samples.py](https://github.com/ukaznil/nft-market/blob/master/samples.py) for
references.

### Available information

What you can retrieve may change by a marketplace you specify, as follows.
Other information may be provided in the future!

| Market        | Name    | #Supply | #Listing | #Owners    | Floor   | Volume  |
|---------------|---------|---------|----------|------------|---------|---------|
| OpenSea       | &check; | &check; |          |            | &check; | &check; |
| Entrepot      | &check; |         | &check;  |            | &check; | &check; |
| tofuNFT       | &check; |         | &check;  | &check;    | &check; | &check; |
| PancakeSwap   | &check; | &check; | &check;  |            | &check; | &check; |
| Rarible       | &check; | &check; |          | &check;    | &check; | &check; |
| GhostMarket   | &check; | &check; |          | &check;    | &check; | &check; |
| Crypto.com    | &check; |         | &check;  | &check;    | &check; | &check; |
| Gem           | &check; |         | &check;  |            | &check; | &check; |
| NFTrade       | &check; |         |          |            | &check; | &check; |
| Solanart      | &check; | &check; |          | &check;    | &check; | &check; |
| Magic Eden    | &check; |         | &check;  |            | &check; | &check; |
| XANALIA       | &check; | &check; |          | &check;    | &check; | &check; | 
| CetoSwap      | &check; | &check; | &check;  | &check;    | &check; | &check; | 
| Coinbase      | &check; |         | &check;  | &check;    | &check; | &check; |
| CCC           | &check; | &check; | &check;  | &check;(*) | &check; | &check; |
| Nifty Gateway | &check; |         | &check;  | &check;    | &check; | &check; |
| Jelly         | &check; | &check; |          | &check;    | &check; | &check; |
| YUMI          | &check; |         | &check;  | &check;    | &check; | &check; |

| Explorer | Ecosystem | Name    | #Supply | #Listing  | #Owners | Floor   | Volume  |
|----------|-----------|---------|---------|-----------|---------|---------|---------|
| ICScan   | ICP       | &check; | &check; | &check;   | &check; | &check; | &check; |
| NFTgeek  | ICP       | &check; | &check; | &check;   | &check; | &check; | &check; |

"&check;(*)" means it can return None value depending on items.

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

## For developers

You can run tests similarly as GitHub Actions in your local environment by using [ACT](https://github.com/nektos/act).
We highly recommend you try this for at least what you added before push.

### Installation

```shell
# mac
$ brew install act

# Linux
$ curl https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash

# Windows Chocolatey
$ choco install act-cli

# Windows Scoop
$ scoop install act
```

### How to use act?

Make sure that you're already running Docker Desktop, and then just run act!

```shell
$ act push --container-architecture linux/amd64
```

Note that when you see choices as for the default size of images, you need at least "Medium".

```shell
Default image and other options can be changed manually in ~/.actrc (please refer to https://github.com/nektos/act#configuration for additional information about file structure)  [Use arrows to move, type to filter, ? for more help]
  Large
> Medium
  Micro
```
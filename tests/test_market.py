from nft_market import Market, Retriever

r = Retriever(num_retry=0, verbose=True)


def test_opensea():
    # OpenSea
    print(r.fetch(Market.OpenSea, 'clonex'))  # CLONE X - X TAKASHI MURAKAMI
    print(r.fetch(Market.OpenSea, 'azuki'))  # Azuki
    print(r.fetch(Market.OpenSea, 'mutant-ape-yacht-club'))  # Mutant Ape Yacht Club


def test_entrepot():
    # Entrepot
    print(r.fetch(Market.Entrepot, 'btcflower'))  # BTC Flower
    print(r.fetch(Market.Entrepot, 'poked'))  # Poked bots
    print(r.fetch(Market.Entrepot, 'motoko'))  # Motoko Day Drop


def test_tofunft():
    # tofuNFT
    print(r.fetch(Market.tofuNFT, 'gh0stlygh0sts-eth'))  # Gh0stly Gh0sts
    print(r.fetch(Market.tofuNFT, 'samurise'))  # Lost SamuRise
    print(r.fetch(Market.tofuNFT, 'gh0stlygh0sts-bsc'))  # Gh0stly Gh0sts


def test_pancakeswap():
    # PancakeSwap
    print(r.fetch(Market.PancakeSwap, '0x0a8901b0e25deb55a87524f0cc164e9644020eba'))  # Pancake Squad
    print(r.fetch(Market.PancakeSwap, '0xDf7952B35f24aCF7fC0487D01c8d5690a60DBa07'))  # Pancake Bunnies
    print(r.fetch(Market.PancakeSwap, '0x4bd2a30435e6624CcDee4C60229250A84a2E4cD6'))  # Gamester Apes


def test_rarible():
    # Rarible
    print(r.fetch(Market.Rarible, '0x3110ef5f612208724ca51f5761a69081809f03b7'))  # Impostors Genesis Aliens
    print(r.fetch(Market.Rarible, '0x49cf6f5d44e70224e2e23fdcdd2c053f30ada28b'))  # CloneX
    print(r.fetch(Market.Rarible, 'boredapeyachtclub'))  # BoredApeYachtClub


def test_ghostmarket():
    # GhostMarket
    print(r.fetch(Market.GhostMarket, 'neoverse'))  # Neoverse
    print(r.fetch(Market.GhostMarket, 'tothemoon'))  # TOTHEMOON
    print(r.fetch(Market.GhostMarket, 'humswap-bowls'))  # Humswap Bowls


def test_cryptocom():
    # Crypto.com
    print(r.fetch(Market.Cryptocom, '6c7b1a68479f2fc35e9f81e42bcb7397'))  # Ballies Origins
    print(r.fetch(Market.Cryptocom, '82421cf8e15df0edcaa200af752a344f'))  # Loaded Lions
    print(r.fetch(Market.Cryptocom, '4ff90f089ac3ef9ce342186adc48a30d'))  # AlphaBot Society


def test_gem():
    # Gem
    print(r.fetch(Market.Gem, 'official-moar-by-joan-cornella'))  # "MOAR" by Joan Cornella
    print(r.fetch(Market.Gem, 'hakinft-io'))  # HAKI NFT
    print(r.fetch(Market.Gem, 'los-muertos-world'))  # Los Muertos World


def test_looksrare():
    # LooksRare
    print(r.fetch(Market.LooksRare, '0x4E1f41613c9084FdB9E34E11fAE9412427480e56'))  # Terraforms
    print(r.fetch(Market.LooksRare, '0x1dfe7Ca09e99d10835Bf73044a23B73Fc20623DF'))  # More Loot
    print(r.fetch(Market.LooksRare, '0xcE25E60A89F200B1fA40f6c313047FFe386992c3'))  # dotdotdot


def test_nftrade():
    # NFTrade
    print(r.fetch(Market.NFTrade, 'polygon/0xc93c53de60d1a28df01e41f5bc04619039d2ef4f'))  # League of Kingdoms Skin
    print(r.fetch(Market.NFTrade, 'bsc/0x8815fae8feb5e1b2f8a6c7c948d9fd1866e07a4f'))  # Mines of Dalarnia Land Plots
    print(r.fetch(Market.NFTrade, 'avalanche/0xaab56a5a22db41d6663aab0f8f0bed979c84c569'))  # PIRATE CHEST v2


def test_solanart():
    # Solanart
    # See this issue: https://github.com/ukaznil/nft-market/issues/2
    pass
    # print(r.fetch(Market.Solanart, 'degenape'))  # Degenerate Ape Academy
    # print(r.fetch(Market.Solanart, 'aurory'))  # Aurory
    # print(r.fetch(Market.Solanart, 'solpunks'))  # SolPunks


def test_magiceden():
    # MagicEden
    # See this issue: https://github.com/ukaznil/nft-market/issues/2
    pass
    # print(r.fetch(Market.MagicEden, 'solgods'))  # SOLgods
    # print(r.fetch(Market.MagicEden, 'tombstoned'))  # TombStoned High Society
    # print(r.fetch(Market.MagicEden, 'degods'))  # DeGods


def test_xanalia():
    # XANALIA
    print(r.fetch(Market.XANALIA, 'collections/blindbox/62113e1774d1af3e04bc313d'))  # ULTRAMAN
    print(r.fetch(Market.XANALIA, 'collections/blindbox/624d51f705901f306d552f25'))  # Rooster Fighter
    print(r.fetch(Market.XANALIA,
                  'collection-details/623b46a6f9b8020cf8c9c167/0xE737d5A35A41fFd6072503BCA9C3013632287305'))  # XANA Alpha pass


def test_cetoswap():
    # CetoSwap
    print(r.fetch(Market.CetoSwap, 'zombie'))  # Crazy Zombie
    print(r.fetch(Market.CetoSwap, 'shoes'))  # Dragon Boots
    print(r.fetch(Market.CetoSwap, 'cars'))  # IC CARS

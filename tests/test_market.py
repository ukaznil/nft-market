from nft_market import Market, Retriever

r = Retriever()


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


def test_tofu():
    # Tofu
    print(r.fetch(Market.Tofu, 'gh0stlygh0sts-eth'))  # Gh0stly Gh0sts
    print(r.fetch(Market.Tofu, 'samurise'))  # Lost SamuRise
    print(r.fetch(Market.Tofu, 'gh0stlygh0sts-bsc'))  # Gh0stly Gh0sts


def test_pancakeswap():
    # PancakeSwap
    print(r.fetch(Market.PancakeSwap, '0x0a8901b0e25deb55a87524f0cc164e9644020eba'))  # Pancake Squad
    print(r.fetch(Market.PancakeSwap, '0xDf7952B35f24aCF7fC0487D01c8d5690a60DBa07'))  # Pancake Bunnies
    print(r.fetch(Market.PancakeSwap, '0x4bd2a30435e6624CcDee4C60229250A84a2E4cD6'))  # Gamester Apes


def test_rarible():
    print(r.fetch(Market.Rarible, '0x3110ef5f612208724ca51f5761a69081809f03b7'))  # Impostors Genesis Aliens
    print(r.fetch(Market.Rarible, '0x49cf6f5d44e70224e2e23fdcdd2c053f30ada28b'))  # CloneX
    print(r.fetch(Market.Rarible, 'boredapeyachtclub'))  # BoredApeYachtClub

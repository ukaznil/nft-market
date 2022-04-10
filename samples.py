from nft_market import Market, Retriever

r = Retriever(num_retry=0)


def sample_opensea():
    # OpenSea
    print(r.fetch(Market.OpenSea, 'clonex'))  # CLONE X - X TAKASHI MURAKAMI
    print(r.fetch(Market.OpenSea, 'azuki'))  # Azuki
    print(r.fetch(Market.OpenSea, 'mutant-ape-yacht-club'))  # Mutant Ape Yacht Club
    print(r.fetch(Market.OpenSea, 'beanzofficial'))  # BEANZ Official
    print(r.fetch(Market.OpenSea, 'arcade-land'))  # Arcade Land
    print(r.fetch(Market.OpenSea, 'akumaorigins'))  # Akuma Origins
    print(r.fetch(Market.OpenSea, 'boredapeyachtclub'))  # Bored Ape Yacht Club
    print(r.fetch(Market.OpenSea, 'kiwami-genesis'))  # KIWAMI Genesis
    print(r.fetch(Market.OpenSea, 'shinsekai-portal'))  # Shinsekai Portal
    print(r.fetch(Market.OpenSea, 'impostors-genesis-aliens'))  # Impostors Genesis Aliens


def sample_entrepot():
    # Entrepot
    print(r.fetch(Market.Entrepot, 'btcflower'))  # BTC Flower
    print(r.fetch(Market.Entrepot, 'poked'))  # Poked bots
    print(r.fetch(Market.Entrepot, 'motoko'))  # Motoko Day Drop
    print(r.fetch(Market.Entrepot, 'icpunks'))  # ICPunks
    print(r.fetch(Market.Entrepot, 'ogmedals'))  # OG MEDALS
    print(r.fetch(Market.Entrepot, 'cronics'))  # Cronic Critters
    print(r.fetch(Market.Entrepot, 'icpuppies'))  # ICPuppies
    print(r.fetch(Market.Entrepot, 'spaceapes'))  # Dfinity Space Apes
    print(r.fetch(Market.Entrepot, 'icdinos'))  # IC Dinos
    print(r.fetch(Market.Entrepot, 'ethflower'))  # ETH Flower


def sample_tofu():
    # Tofu
    print(r.fetch(Market.Tofu, 'gh0stlygh0sts-eth'))  # Gh0stly Gh0sts
    print(r.fetch(Market.Tofu, 'samurise'))  # Lost SamuRise
    print(r.fetch(Market.Tofu, 'gh0stlygh0sts-bsc'))  # Gh0stly Gh0sts
    print(r.fetch(Market.Tofu, 'meta-warden'))  # MetaWarden
    print(r.fetch(Market.Tofu, 'league-of-kingdoms-item'))  # League of Kingdoms ITEM
    print(r.fetch(Market.Tofu, 'tiny-dinos-polygon'))  # tiny dinos
    print(r.fetch(Market.Tofu, 'astardegens'))  # AstarDegens
    print(r.fetch(Market.Tofu, 'astar-punks'))  # Astar Punks
    print(r.fetch(Market.Tofu, 'universe-ecosystem'))  # Universe Ecosystem
    print(r.fetch(Market.Tofu, 'node-whales'))  # Node Whales


def sample_pancakeswap():
    # PancakeSwap
    print(r.fetch(Market.PancakeSwap, '0x0a8901b0e25deb55a87524f0cc164e9644020eba'))  # Pancake Squad
    print(r.fetch(Market.PancakeSwap, '0xDf7952B35f24aCF7fC0487D01c8d5690a60DBa07'))  # Pancake Bunnies
    print(r.fetch(Market.PancakeSwap, '0x4bd2a30435e6624CcDee4C60229250A84a2E4cD6'))  # Gamester Apes
    print(r.fetch(Market.PancakeSwap, '0x11304895f41C5A9b7fBFb0C4B011A92f1020EF96'))  # ShitPunks
    print(r.fetch(Market.PancakeSwap, '0x44d85770aEa263F9463418708125Cd95e308299B'))  # BornBadBoys
    print(r.fetch(Market.PancakeSwap, '0x3da8410e6EF658c06E277a2769816688c37496CF'))  # BornBadGirls
    print(r.fetch(Market.PancakeSwap, '0xA46A4920B40f134420b472B16b3328d74D7B6B70'))  # The Bull Society
    print(r.fetch(Market.PancakeSwap, '0x98F606A4cdDE68b9f68732D21fb9bA8B5510eE48'))  # LittleGhosts
    print(r.fetch(Market.PancakeSwap, '0x467044e6A297084baAEBd53b6f1649C07527E273'))  # CyberBearz Army
    print(r.fetch(Market.PancakeSwap, '0x57A7c5d10c3F87f5617Ac1C60DA60082E44D539e'))  # Dauntless Alpies

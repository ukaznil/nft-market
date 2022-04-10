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


def sample_tofunft():
    # tofuNFT
    print(r.fetch(Market.tofuNFT, 'gh0stlygh0sts-eth'))  # Gh0stly Gh0sts
    print(r.fetch(Market.tofuNFT, 'samurise'))  # Lost SamuRise
    print(r.fetch(Market.tofuNFT, 'gh0stlygh0sts-bsc'))  # Gh0stly Gh0sts
    print(r.fetch(Market.tofuNFT, 'meta-warden'))  # MetaWarden
    print(r.fetch(Market.tofuNFT, 'league-of-kingdoms-item'))  # League of Kingdoms ITEM
    print(r.fetch(Market.tofuNFT, 'tiny-dinos-polygon'))  # tiny dinos
    print(r.fetch(Market.tofuNFT, 'astardegens'))  # AstarDegens
    print(r.fetch(Market.tofuNFT, 'astar-punks'))  # Astar Punks
    print(r.fetch(Market.tofuNFT, 'universe-ecosystem'))  # Universe Ecosystem
    print(r.fetch(Market.tofuNFT, 'node-whales'))  # Node Whales


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


def sample_rarible():
    # Rarible
    print(r.fetch(Market.Rarible, '0x4a8c9d751eeabc5521a68fb080dd7e72e46462af'))  # Arcade Land
    print(r.fetch(Market.Rarible, '0x3110ef5f612208724ca51f5761a69081809f03b7'))  # Impostors Genesis Aliens
    print(r.fetch(Market.Rarible, '0x49cf6f5d44e70224e2e23fdcdd2c053f30ada28b'))  # CloneX
    print(r.fetch(Market.Rarible, 'boredapeyachtclub'))  # BoredApeYachtClub
    print(r.fetch(Market.Rarible, 'losmuertos'))  # Los Muertos
    print(r.fetch(Market.Rarible, '0xeb3a9a839dfeeaf71db1b4ed6a8ae0ccb171b227'))  # MOAR by Joan Cornella
    print(r.fetch(Market.Rarible, '0xf97df1e168c27e22eedd34c05ae0615605c5dcbf'))  # Aki Story
    print(r.fetch(Market.Rarible, '0x4554c0b38d23450f7a32d58281a2b6e423bb27a6'))  # Kureiji
    print(r.fetch(Market.Rarible, 'loserclub'))  # Loser Club
    print(r.fetch(Market.Rarible, '0x98b82d9efc577b1c3aa6578342121231db2b47b9'))  # Shinsekai Portal


def sample_ghostmarket():
    # GhostMarket
    print(r.fetch(Market.GhostMarket, 'neoverse'))  # Neoverse
    print(r.fetch(Market.GhostMarket, 'tothemoon'))  # TOTHEMOON
    print(r.fetch(Market.GhostMarket, 'humswap-bowls'))  # Humswap Bowls
    print(r.fetch(Market.GhostMarket, 'puppet'))  # Puppet
    print(r.fetch(Market.GhostMarket, 'ghost'))  # Ghost
    print(r.fetch(Market.GhostMarket, 'somniumwave'))  # SOMNIUMWAVE
    print(r.fetch(Market.GhostMarket, 'antcoins'))  # AntCoins
    print(r.fetch(Market.GhostMarket, '22rs'))  # 22 Racing Series
    print(r.fetch(Market.GhostMarket, 'fcc'))  # Featured Community
    print(r.fetch(Market.GhostMarket, 'luckytiger'))  # LuckyTiger


def sample_cryptocom():
    # Crypto.com
    print(r.fetch(Market.Cryptocom, '6c7b1a68479f2fc35e9f81e42bcb7397'))  # Ballies Origins
    print(r.fetch(Market.Cryptocom, '82421cf8e15df0edcaa200af752a344f'))  # Loaded Lions
    print(r.fetch(Market.Cryptocom, '4ff90f089ac3ef9ce342186adc48a30d'))  # AlphaBot Society
    print(r.fetch(Market.Cryptocom, 'bd2890bc85bd036bc71e999a147b7fe5'))  # Cryptoverse
    print(r.fetch(Market.Cryptocom, 'faa3d8da88f9ee2f25267e895db71471'))  # PsychoKitties: The New Era
    print(r.fetch(Market.Cryptocom, '282ff8943c87c682b06dfcbb531b7118'))  # POTATOES ARE HUMANS TOO
    print(r.fetch(Market.Cryptocom, '8539b9d1f2337bf5725c75d2a47e4f0d'))  # Cosmic Creatures
    print(r.fetch(Market.Cryptocom, '69d0601d6d4ecd0ea670835645d47b0d'))  # PsychoKitties: The Rise Of Mollies
    print(r.fetch(Market.Cryptocom, '66b8c165ad4babe1b488b4981d07438e'))  # PHAZES
    print(r.fetch(Market.Cryptocom, '6e656ea14b0863f3cf1dbd41554302d3'))  # The Art of Giving

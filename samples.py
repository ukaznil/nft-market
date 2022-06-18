from nft_market import Market, Retriever

r = Retriever(num_retry=0, verbose=True)


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
    print(r.fetch(Market.OpenSea, 'impostors-genesis-aliens'))  # Impostors Genesis Aliens


def sample_entrepot():
    # Entrepot
    print(r.fetch(Market.Entrepot, 'btcflower'))  # BTC Flower
    print(r.fetch(Market.Entrepot, 'poked'))  # Poked bots
    print(r.fetch(Market.Entrepot, 'motoko'))  # Motoko Day Drop
    print(r.fetch(Market.Entrepot, 'icpunks'))  # ICPunks
    print(r.fetch(Market.Entrepot, 'ogmedals'))  # OG MEDALS
    print(r.fetch(Market.Entrepot, 'cronics'))  # Cronic Critters
    # print(r.fetch(Market.Entrepot, 'icpuppies'))  # ICPuppies
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


def sample_gem():
    # Gem
    print(r.fetch(Market.Gem, 'official-moar-by-joan-cornella'))  # "MOAR" by Joan Cornella
    print(r.fetch(Market.Gem, 'hakinft-io'))  # HAKI NFT
    print(r.fetch(Market.Gem, 'los-muertos-world'))  # Los Muertos World
    print(r.fetch(Market.Gem, 'boredapeyachtclub'))  # Bored Ape Yacht Club
    print(r.fetch(Market.Gem, 'arcade-land'))  # Arcade Land
    print(r.fetch(Market.Gem, 'hikarinftofficial'))  # Hikari Official
    print(r.fetch(Market.Gem, 'impostors-genesis-aliens'))  # Impostors Genesis Aliens
    print(r.fetch(Market.Gem, 'official-kreepy-club'))  # OFFICIAL KREEPY CLUB
    print(r.fetch(Market.Gem, 'froyokittenscollection'))  # froyo kittens
    print(r.fetch(Market.Gem, 'mutant-ape-yacht-club'))  # Mutant Ape Yacht Club


def sample_looksrare():
    # LooksRare
    print(r.fetch(Market.LooksRare, '0x4E1f41613c9084FdB9E34E11fAE9412427480e56'))  # Terraforms
    print(r.fetch(Market.LooksRare, '0x1dfe7Ca09e99d10835Bf73044a23B73Fc20623DF'))  # More Loot
    print(r.fetch(Market.LooksRare, '0xcE25E60A89F200B1fA40f6c313047FFe386992c3'))  # dotdotdot
    print(r.fetch(Market.LooksRare, '0x7Bd29408f11D2bFC23c34f18275bBf23bB716Bc7'))  # Meebits
    print(r.fetch(Market.LooksRare, '0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D'))  # Bored Ape Yacht Club
    print(r.fetch(Market.LooksRare, '0x60E4d786628Fea6478F785A6d7e704777c86a7c6'))  # Mutant Ape Yacht Club
    print(r.fetch(Market.LooksRare, '0x7a376C1F8eDF7BA7Eb94A7438a8313a17D830FF8'))  # ProjectKevins
    print(r.fetch(Market.LooksRare, '0xED5AF388653567Af2F388E6224dC7C4b3241C544'))  # Azuki
    print(r.fetch(Market.LooksRare, '0x49cF6f5d44E70224e2E23fDcdd2C053F30aDA28B'))  # CloneX
    print(r.fetch(Market.LooksRare, '0xBd785591D714f691E939de7ec6D72550a44c598c'))  # AlphaDoggg Tag


def sample_nftrade():
    # NFTrade
    print(r.fetch(Market.NFTrade, 'polygon/0xc93c53de60d1a28df01e41f5bc04619039d2ef4f'))  # League of Kingdoms Skin
    print(r.fetch(Market.NFTrade, 'bsc/0x8815fae8feb5e1b2f8a6c7c948d9fd1866e07a4f'))  # Mines of Dalarnia Land Plots
    print(r.fetch(Market.NFTrade, 'avalanche/0xaab56a5a22db41d6663aab0f8f0bed979c84c569'))  # PIRATE CHEST v2
    print(r.fetch(Market.NFTrade, 'avalanche/0x023a1eafc590d790fabd1d00872881c2a9e3c74a'))  # Louverture
    print(r.fetch(Market.NFTrade, 'bsc/0xe9b9497798b5fe949039c01b1a772bdcb7e9ba10'))  # Gamer NFLs
    print(r.fetch(Market.NFTrade, 'avalanche/0xa69fee085a4c38656ce9c37a064a330725307482'))  # Avalant
    print(r.fetch(Market.NFTrade, 'avalanche/0x4a8e6a9b93e55af71882f3afaa10141715ce5fd2'))  # Tiny Bones Club
    print(r.fetch(Market.NFTrade, 'avalanche/0xeab33f781ada4ee7e91fd63ad87c5bb47ffb8a83'))  # Yield Hunt
    print(r.fetch(Market.NFTrade, 'avalanche/0xd5c6064e09ff127e24900adfb8559c4ee0634729'))  # NodeBears
    print(r.fetch(Market.NFTrade, 'avalanche/0x6cc4cc814c7154fb67965c8044cc803b3199ec53'))  # Pizza Game Chef Tools


def sample_solanart():
    # Solanart
    print(r.fetch(Market.Solanart, 'degenape'))  # Degenerate Ape Academy
    print(r.fetch(Market.Solanart, 'aurory'))  # Aurory
    print(r.fetch(Market.Solanart, 'solpunks'))  # SolPunks
    print(r.fetch(Market.Solanart, 'degeneratetrashpandas'))  # Degenerate Trash Pandas
    print(r.fetch(Market.Solanart, 'degenerate_ape_kindergarten'))  # Degenerate Ape Kindergarten
    print(r.fetch(Market.Solanart, 'grimsyndicate'))  # Grim Syndicate
    print(r.fetch(Market.Solanart, 'cyberpharmacist'))  # Cyber Pharmacy
    print(r.fetch(Market.Solanart, 'famousfoxfederation'))  # Famous Fox Federation
    print(r.fetch(Market.Solanart, 'nyanheroes'))  # Nyan Heroes
    print(r.fetch(Market.Solanart, 'verseestatexvincentfaudemer'))  # Verse Estate


def sample_magiceden():
    # MagicEden
    print(r.fetch(Market.MagicEden, 'solgods'))  # SOLgods
    print(r.fetch(Market.MagicEden, 'tombstoned'))  # TombStoned High Society
    print(r.fetch(Market.MagicEden, 'degods'))  # DeGods
    print(r.fetch(Market.MagicEden, 'degendojonft'))  # Degen Dojo
    print(r.fetch(Market.MagicEden, 'cosmic_ape_crusaders'))  # Cosmic Ape Crusaders
    print(r.fetch(Market.MagicEden, 'atadians'))  # OG Atadians
    print(r.fetch(Market.MagicEden, 'blocksmith_labs'))  # Blocksmith Labs
    print(r.fetch(Market.MagicEden, 'decimusdynamics'))  # Decimus Dynamics
    print(r.fetch(Market.MagicEden, 'dhly'))  # Dahlys
    print(r.fetch(Market.MagicEden, 'fellowapes'))  # Fellow Apes


def sample_xanalia():
    # XANALIA
    print(r.fetch(Market.XANALIA, 'collections/blindbox/62113e1774d1af3e04bc313d'))  # ULTRAMAN
    print(r.fetch(Market.XANALIA, 'collections/blindbox/624d51f705901f306d552f25'))  # Rooster Fighter
    print(r.fetch(Market.XANALIA,
                  'collection-details/623b46a6f9b8020cf8c9c167/0xE737d5A35A41fFd6072503BCA9C3013632287305'))  # XANA Alpha pass
    print(r.fetch(Market.XANALIA, 'collection/underground_city'))  # underground_city
    print(r.fetch(Market.XANALIA,
                  'collection-details/61ea500dd6b5cb14adc7703a/0xE5A34Ca6a9a43d05Be4F23Cf8b8AA319099e326B'))  # Masami Tanaka
    print(r.fetch(Market.XANALIA,
                  'collection-details/61f2965cec90c7ef60603e96/0xc715aCf1dbE37978dF21D945857f36d22d5097aB'))  # Momento Series
    print(r.fetch(Market.XANALIA,
                  'collection-details/621341b6499b06610040cd3a/0x5D20CB885d960B52350262B2989033460C1448B7'))  # The Inflorescence
    print(r.fetch(Market.XANALIA,
                  'collection-details/6231783fdbf3f95b07f8fb5c/0xB11F73B3A221FEA1e3395f15721E5a8c2C0735fD'))  # The Tripp
    print(r.fetch(Market.XANALIA,
                  'collection-details/61f3a7d25824090df3ee8dc1/61f3a7d25824090df3ee8dc1'))  # Natalia From Moscow
    print(r.fetch(Market.XANALIA,
                  'collection-details/61bd83fa1145b8b8d1524493/0x5bfcfCBfb35298052238E191569f7E300b9b74B1'))  # Angels and Demons


def sample_cetoswap():
    # CetoSwap
    print(r.fetch(Market.CetoSwap, 'zombie'))  # Crazy Zombie
    print(r.fetch(Market.CetoSwap, 'shoes'))  # Dragon Boots
    print(r.fetch(Market.CetoSwap, 'cars'))  # IC CARS
    print(r.fetch(Market.CetoSwap, 'eggs'))  # Bobo Eggs


def sample_coinbase():
    # Coinbase
    print(r.fetch(Market.Coinbase, 'ethereum/0x23581767a106ae21c074b2276D25e5C3e136a68b'))  # Moonbirds
    print(r.fetch(Market.Coinbase, 'ethereum/0x60E4d786628Fea6478F785A6d7e704777c86a7c6'))  # Mutant Ape Yacht Club
    print(r.fetch(Market.Coinbase, 'ethereum/0x341A1c534248966c4b6AFaD165B98DAED4B964ef'))  # Murakami.Flowers Seed
    print(r.fetch(Market.Coinbase, 'ethereum/0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D'))  # Bored Ape Yacht Club
    print(r.fetch(Market.Coinbase, 'ethereum/0x86825dFCa7A6224cfBd2DA48e85DF2fc3Aa7C4B1'))  # RTFKT - MNLTH 🗿
    print(r.fetch(Market.Coinbase, 'ethereum/0xba30E5F9Bb24caa003E9f2f0497Ad287FDF95623'))  # Bored Ape Kennel Club
    print(r.fetch(Market.Coinbase, 'ethereum/0x306b1ea3ecdf94aB739F1910bbda052Ed4A9f949'))  # Beanz
    print(r.fetch(Market.Coinbase, 'ethereum/0x9378368ba6b85c1FbA5b131b530f5F5bEdf21A18'))  # VeeFriends Series 2
    print(r.fetch(Market.Coinbase, 'ethereum/0x49cF6f5d44E70224e2E23fDcdd2C053F30aDA28B'))  # CloneX
    # print(r.fetch(Market.Coinbase, 'ethereum/0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB'))  # CryptoPunks


def sample_ccc():
    # CCC
    print(r.fetch(Market.CCC, 'zombie'))  # Crazy Zombie
    print(r.fetch(Market.CCC, 'turtles'))  # ICTurtles
    print(r.fetch(Market.CCC, 'gang'))  # DfinityGangs
    print(r.fetch(Market.CCC, 'avocado'))  # Avocado Research
    print(r.fetch(Market.CCC, 'icity'))  # ICity ICmoe
    print(r.fetch(Market.CCC, 'lion'))  # IC LIONS
    print(r.fetch(Market.CCC, 'shoe'))  # Dragon Boots
    print(r.fetch(Market.CCC, 'car'))  # IC CARS


def sample_niftygateway():
    # Nifty Gateway
    print(r.fetch(Market.NiftyGateway, '0xc71561e12faf378b07eacd36b3d0eb0d13a5fb1c'))  # Awkward Astronauts
    print(r.fetch(Market.NiftyGateway, '0xa5a1e6972ace6f4ae388fbafcb7ec12013b64f53'))  # NOOBPUNKS
    print(r.fetch(Market.NiftyGateway, '0x5ae681e32a503abe7bf52a25565bbdc712dbea98'))  # Sellouts
    print(r.fetch(Market.NiftyGateway, '0xc3f8a0f5841abff777d3eefa5047e8d413a1c9ab'))  # m
    print(r.fetch(Market.NiftyGateway, '0xc1aa2a21d0c1c861e3b5fa4df8f14db5e24fcd81'))  # Crystal Pop


def sample_jelly():
    # Jelly
    print(r.fetch(Market.Jelly, 'crowns'))  # Crowns

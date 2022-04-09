import dataclasses
from typing import *


@dataclasses.dataclass
class NFTInfo:
    name: str
    num_items_all: Optional[int]
    num_listing: Optional[int]
    num_owners: Optional[int]
    floor: float
    volume: float

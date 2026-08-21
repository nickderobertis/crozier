

import typing

from .filter_block_hash import FilterBlockHash
from .filter_from_block import FilterFromBlock

Filter = typing.Union[FilterFromBlock, FilterBlockHash]

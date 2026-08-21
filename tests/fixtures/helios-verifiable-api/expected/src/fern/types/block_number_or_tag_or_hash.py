

import typing

from .block_tag import BlockTag
from .hash32 import Hash32
from .uint import Uint

BlockNumberOrTagOrHash = typing.Union[Uint, BlockTag, Hash32]

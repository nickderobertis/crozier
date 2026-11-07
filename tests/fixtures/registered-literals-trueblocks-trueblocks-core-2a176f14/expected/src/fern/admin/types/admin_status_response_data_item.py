

import typing

from ...types.cache_item import CacheItem
from ...types.chain import Chain
from ...types.status import Status

AdminStatusResponseDataItem = typing.Union[CacheItem, Chain, Status]



import typing

from .multiple_live_items import MultipleLiveItems
from .single_live_item import SingleLiveItem

CreateItemLiveItemsRequestBody = typing.Union[SingleLiveItem, MultipleLiveItems]

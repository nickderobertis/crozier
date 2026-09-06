

import typing

from .multiple_items import MultipleItems
from .single_item import SingleItem

CreateItemItemsRequestBody = typing.Union[SingleItem, MultipleItems]



import typing

from .multiple_cms_items_item import MultipleCmsItemsItem
from .single_cms_item import SingleCmsItem

CreateItemsItemsRequestFieldData = typing.Union[SingleCmsItem, typing.List[MultipleCmsItemsItem]]

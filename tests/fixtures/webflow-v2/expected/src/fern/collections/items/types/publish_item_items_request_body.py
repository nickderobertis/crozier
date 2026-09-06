

import typing

from .item_i_ds import ItemIDs
from .item_i_ds_with_locales import ItemIDsWithLocales

PublishItemItemsRequestBody = typing.Union[ItemIDs, ItemIDsWithLocales]

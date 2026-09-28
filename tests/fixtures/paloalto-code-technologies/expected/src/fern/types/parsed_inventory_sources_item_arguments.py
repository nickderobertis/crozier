

import typing

from .parsed_inventory_sources_item_arguments_one_item import ParsedInventorySourcesItemArgumentsOneItem

ParsedInventorySourcesItemArguments = typing.Union[
    typing.List[str], typing.List[ParsedInventorySourcesItemArgumentsOneItem]
]

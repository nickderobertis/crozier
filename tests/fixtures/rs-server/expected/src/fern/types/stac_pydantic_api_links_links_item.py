

import typing

from .items_link import ItemsLink
from .link import Link
from .pagination_link import PaginationLink
from .search_link import SearchLink

StacPydanticApiLinksLinksItem = typing.Union[SearchLink, PaginationLink, ItemsLink, Link]



import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .library_item_base import LibraryItemBase
from .media_minified import MediaMinified


class LibraryItemMinified(LibraryItemBase):
    """
    A single item on the server, like a book or podcast. Minified media format.
    """

    media: typing.Optional[MediaMinified] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

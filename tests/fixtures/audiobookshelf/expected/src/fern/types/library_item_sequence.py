

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .library_item_base import LibraryItemBase
from .sequence import Sequence


class LibraryItemSequence(LibraryItemBase):
    """
    A single item on the server, like a book or podcast. Includes series sequence information.
    """

    sequence: typing.Optional[Sequence] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

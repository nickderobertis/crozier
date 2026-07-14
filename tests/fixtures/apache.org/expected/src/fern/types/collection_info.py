

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CollectionInfo(UniversalBaseModel):
    """
    Metadata about collection.
    """

    total_entries: typing.Optional[int] = pydantic.Field(default=None)
    """
    Count of objects in the current result set.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

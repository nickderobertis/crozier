

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .id import Id
from .nullable_id import NullableId


class File(UniversalBaseModel):
    id: Id
    name: str = pydantic.Field()
    """
    FolderResource name
    """

    url: str = pydantic.Field()
    """
    Public url
    """

    size: typing.Optional[int] = pydantic.Field(default=None)
    """
    File size
    """

    folder: typing.Optional[NullableId] = None
    thumbnail: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

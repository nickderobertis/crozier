

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .id import Id
from .nullable_id import NullableId


class Folder(UniversalBaseModel):
    id: Id
    name: str = pydantic.Field()
    """
    FolderResource name
    """

    parent: typing.Optional[NullableId] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .id import Id


class LinkedFolder(UniversalBaseModel):
    id: typing.Optional[Id] = None
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the folder
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

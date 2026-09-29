

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .category import Category


class Context(UniversalBaseModel):
    id: typing.Optional[str] = None
    label: typing.Optional[str] = None
    type: typing.Optional[str] = None
    category: typing.Optional[typing.List[Category]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nested_manufacturer import NestedManufacturer


class NestedModuleType(UniversalBaseModel):
    display: typing.Optional[str] = None
    id: typing.Optional[int] = None
    manufacturer: typing.Optional[NestedManufacturer] = None
    model: str
    url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

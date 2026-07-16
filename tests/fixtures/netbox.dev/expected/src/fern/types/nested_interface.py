

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .nested_device import NestedDevice


class NestedInterface(UniversalBaseModel):
    occupied: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="_occupied")] = None
    cable: typing.Optional[int] = None
    device: typing.Optional[NestedDevice] = None
    display: typing.Optional[str] = None
    id: typing.Optional[int] = None
    name: str
    url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

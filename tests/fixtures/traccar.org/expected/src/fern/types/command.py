

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .command_attributes import CommandAttributes


class Command(UniversalBaseModel):
    attributes: typing.Optional[CommandAttributes] = None
    description: typing.Optional[str] = None
    device_id: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="deviceId")] = None
    id: typing.Optional[int] = None
    type: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

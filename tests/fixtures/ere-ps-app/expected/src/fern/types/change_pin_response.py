

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .pin_result_enum import PinResultEnum
from .status import Status


class ChangePinResponse(UniversalBaseModel):
    status: typing.Optional[Status] = None
    pin_result_enum: typing_extensions.Annotated[
        typing.Optional[PinResultEnum], FieldMetadata(alias="pinResultEnum"), pydantic.Field(alias="pinResultEnum")
    ] = None
    left_tries: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="leftTries"), pydantic.Field(alias="leftTries")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

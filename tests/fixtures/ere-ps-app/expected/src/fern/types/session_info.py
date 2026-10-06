

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .duration import Duration


class SessionInfo(UniversalBaseModel):
    signature_mode: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="signatureMode"), pydantic.Field(alias="signatureMode")
    ] = None
    count_remaining: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="countRemaining"), pydantic.Field(alias="countRemaining")
    ] = None
    time_remaining: typing_extensions.Annotated[
        typing.Optional[Duration], FieldMetadata(alias="timeRemaining"), pydantic.Field(alias="timeRemaining")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

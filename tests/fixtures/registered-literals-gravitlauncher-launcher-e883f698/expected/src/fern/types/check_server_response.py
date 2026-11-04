

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .user import User


class CheckServerResponse(UniversalBaseModel):
    user: typing.Optional[User] = None
    hardware_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="hardwareId"), pydantic.Field(alias="hardwareId")
    ] = None
    session_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="sessionId"), pydantic.Field(alias="sessionId")
    ] = None
    session_properties: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]],
        FieldMetadata(alias="sessionProperties"),
        pydantic.Field(alias="sessionProperties"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

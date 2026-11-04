

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class EnvironmentRegistrationCallbackPayloadBody(UniversalBaseModel):
    session_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="sessionId"), pydantic.Field(alias="sessionId")
    ] = None
    session_path: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="sessionPath"), pydantic.Field(alias="sessionPath")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

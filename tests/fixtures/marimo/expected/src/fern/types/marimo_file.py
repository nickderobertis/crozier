

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .session_id import SessionId


class MarimoFile(UniversalBaseModel):
    initialization_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="initializationId"), pydantic.Field(alias="initializationId")
    ] = None
    last_modified: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="lastModified"), pydantic.Field(alias="lastModified")
    ] = None
    name: str
    path: str
    session_id: typing_extensions.Annotated[
        typing.Optional[SessionId], FieldMetadata(alias="sessionId"), pydantic.Field(alias="sessionId")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

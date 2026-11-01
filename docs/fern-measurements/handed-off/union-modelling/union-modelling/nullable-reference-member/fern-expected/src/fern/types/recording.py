

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .recording_started_at import RecordingStartedAt


class Recording(UniversalBaseModel):
    title: typing.Optional[str] = None
    started_at: typing_extensions.Annotated[
        typing.Optional[RecordingStartedAt], FieldMetadata(alias="startedAt"), pydantic.Field(alias="startedAt")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

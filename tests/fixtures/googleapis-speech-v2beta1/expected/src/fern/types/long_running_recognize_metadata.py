

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class LongRunningRecognizeMetadata(UniversalBaseModel):
    """
    Describes the progress of a long-running `LongRunningRecognize` call. It is included in the `metadata` field of the `Operation` returned by the `GetOperation` call of the `google::longrunning::Operations` service.
    """

    last_update_time: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="lastUpdateTime"),
        pydantic.Field(alias="lastUpdateTime", description="Output only. Time of the most recent processing update."),
    ] = None
    """
    Output only. Time of the most recent processing update.
    """

    progress_percent: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="progressPercent"),
        pydantic.Field(
            alias="progressPercent",
            description="Output only. Approximate percentage of audio processed thus far. Guaranteed to be 100 when the audio is fully processed and the results are available.",
        ),
    ] = None
    """
    Output only. Approximate percentage of audio processed thus far. Guaranteed to be 100 when the audio is fully processed and the results are available.
    """

    start_time: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="startTime"),
        pydantic.Field(alias="startTime", description="Output only. Time when the request was received."),
    ] = None
    """
    Output only. Time when the request was received.
    """

    uri: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URI of the audio file being transcribed. Empty if the audio was sent as byte content.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

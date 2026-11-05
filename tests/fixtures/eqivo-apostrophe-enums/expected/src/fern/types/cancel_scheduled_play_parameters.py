

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CancelScheduledPlayParameters(UniversalBaseModel):
    sched_play_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="SchedPlayId"),
        pydantic.Field(
            alias="SchedPlayId",
            description="Unique identifier returned when scheduled playback was originally requested",
        ),
    ]
    """
    Unique identifier returned when scheduled playback was originally requested
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

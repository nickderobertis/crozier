

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AbsoluteTimeRangeConfigModelValue(UniversalBaseModel):
    """
    Time range object
    """

    end_time: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="endTime"),
        pydantic.Field(alias="endTime", description="End timestamp"),
    ] = None
    """
    End timestamp
    """

    start_time: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="startTime"),
        pydantic.Field(alias="startTime", description="Start timestamp"),
    ] = None
    """
    Start timestamp
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

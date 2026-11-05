

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ScheduleHangupParameters(UniversalBaseModel):
    call_uuid: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="CallUUID"),
        pydantic.Field(alias="CallUUID", description="Unique identifier of the call"),
    ]
    """
    Unique identifier of the call
    """

    time: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="Time"),
        pydantic.Field(alias="Time", description="Time (in seconds) after which the call in question will be hung up"),
    ]
    """
    Time (in seconds) after which the call in question will be hung up
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

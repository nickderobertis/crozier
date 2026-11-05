

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CancelScheduledHangupParameters(UniversalBaseModel):
    sched_hangup_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="SchedHangupId"),
        pydantic.Field(
            alias="SchedHangupId",
            description="Unique identifier returned when scheduled hangup was originally requested",
        ),
    ]
    """
    Unique identifier returned when scheduled hangup was originally requested
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

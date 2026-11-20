

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .crossing_delayed_notice_phase import CrossingDelayedNoticePhase


class CrossingDelayedNotice(UniversalBaseModel):
    """
    The crossing is delayed.
    """

    phase: typing.Optional[CrossingDelayedNoticePhase] = pydantic.Field(default=None)
    """
    Where the crossing stands.
    """

    minutes_late: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="minutesLate"), pydantic.Field(alias="minutesLate")
    ] = None
    crossing_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="crossingId"), pydantic.Field(alias="crossingId")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

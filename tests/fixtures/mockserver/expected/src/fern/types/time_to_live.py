

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .time_to_live_time_unit import TimeToLiveTimeUnit


class TimeToLive(UniversalBaseModel):
    """
    time expectation is valid for
    """

    time_unit: typing_extensions.Annotated[
        typing.Optional[TimeToLiveTimeUnit], FieldMetadata(alias="timeUnit"), pydantic.Field(alias="timeUnit")
    ] = None
    time_to_live: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="timeToLive"), pydantic.Field(alias="timeToLive")
    ] = None
    unlimited: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

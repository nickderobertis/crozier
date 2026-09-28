

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ClockStatus(UniversalBaseModel):
    """
    clock status response
    """

    current_instant: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="currentInstant"),
        pydantic.Field(alias="currentInstant", description="the current server clock instant"),
    ] = None
    """
    the current server clock instant
    """

    current_epoch_millis: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="currentEpochMillis"),
        pydantic.Field(alias="currentEpochMillis", description="the current server clock time as epoch milliseconds"),
    ] = None
    """
    the current server clock time as epoch milliseconds
    """

    frozen: typing.Optional[bool] = pydantic.Field(default=None)
    """
    true if the clock is currently frozen
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

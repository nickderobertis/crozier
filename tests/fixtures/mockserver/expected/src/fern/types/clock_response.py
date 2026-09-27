

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ClockResponse(UniversalBaseModel):
    """
    clock control response after a freeze, advance, or reset action
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    the action that was performed (freeze, advance, or reset)
    """

    current_instant: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="currentInstant"),
        pydantic.Field(alias="currentInstant", description="the current server clock instant after the action"),
    ] = None
    """
    the current server clock instant after the action
    """

    current_epoch_millis: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="currentEpochMillis"),
        pydantic.Field(
            alias="currentEpochMillis",
            description="the current server clock time as epoch milliseconds after the action",
        ),
    ] = None
    """
    the current server clock time as epoch milliseconds after the action
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

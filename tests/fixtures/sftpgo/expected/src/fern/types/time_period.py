

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TimePeriod(UniversalBaseModel):
    day_of_week: typing.Optional[int] = pydantic.Field(default=None)
    """
    Day of week, 0 Sunday, 6 Saturday
    """

    from_: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="from"),
        pydantic.Field(alias="from", description="Start time in HH:MM format"),
    ] = None
    """
    Start time in HH:MM format
    """

    to: typing.Optional[str] = pydantic.Field(default=None)
    """
    End time in HH:MM format
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class InputDatePayloadDateRange(UniversalBaseModel):
    """
    Restrict selectable dates to a specific range.
    """

    from_: typing_extensions.Annotated[
        typing.Optional[dt.date],
        FieldMetadata(alias="from"),
        pydantic.Field(alias="from", description="Start date of the allowed range."),
    ] = None
    """
    Start date of the allowed range.
    """

    to: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    End date of the allowed range.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

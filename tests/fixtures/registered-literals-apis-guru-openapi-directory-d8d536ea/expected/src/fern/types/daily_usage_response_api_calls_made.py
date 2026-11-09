

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DailyUsageResponseApiCallsMade(UniversalBaseModel):
    """
    Total API calls made for the billing cycle.
    """

    count: int = pydantic.Field()
    """
    Total API calls made for the billing cycle
    """

    last_updated: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="lastUpdated"),
        pydantic.Field(alias="lastUpdated", description="Last Updated date and time for the field apiCallsMade"),
    ] = None
    """
    Last Updated date and time for the field apiCallsMade
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

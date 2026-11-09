

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DailyUsageResponseApiCallsBillable(UniversalBaseModel):
    """
    Total number of API calls billed for the billing cycle.
    """

    count: int = pydantic.Field()
    """
    Total API calls billed  for the billing cycle
    """

    last_updated: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="lastUpdated"),
        pydantic.Field(alias="lastUpdated", description="Last Updated date and time for the field apiCallsBillable"),
    ] = None
    """
    Last Updated date and time for the field apiCallsBillable
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

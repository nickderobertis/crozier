

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class StockUsedQueryParameters(UniversalBaseModel):
    filter_date_from: typing_extensions.Annotated[
        typing.Optional[dt.date],
        FieldMetadata(alias="filterDateFrom"),
        pydantic.Field(
            alias="filterDateFrom",
            description="Filter stock used on or after this date (yyyy-mm-dd) default is 90 days ago and max up to 180 days ago",
        ),
    ] = None
    """
    Filter stock used on or after this date (yyyy-mm-dd) default is 90 days ago and max up to 180 days ago
    """

    page_cursor: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="pageCursor"), pydantic.Field(alias="pageCursor")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

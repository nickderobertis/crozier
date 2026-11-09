

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .asset_report_id import AssetReportId
from .asset_report_item import AssetReportItem
from .asset_report_user import AssetReportUser


class AssetReport(UniversalBaseModel):
    """
    An object representing an Asset Report
    """

    asset_report_id: AssetReportId
    client_report_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    An identifier you determine and submit for the Asset Report.
    """

    date_generated: dt.datetime = pydantic.Field()
    """
    The date and time when the Asset Report was created, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (e.g. "2018-04-12T03:32:11Z").
    """

    days_requested: float = pydantic.Field()
    """
    The duration of transaction history you requested
    """

    items: typing.List[AssetReportItem] = pydantic.Field()
    """
    Data returned by Plaid about each of the Items included in the Asset Report.
    """

    user: AssetReportUser

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

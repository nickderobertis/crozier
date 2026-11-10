

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .account_assets import AccountAssets
from .item_id import ItemId


class AssetReportItem(UniversalBaseModel):
    """
    A representation of an Item within an Asset Report.
    """

    accounts: typing.List[AccountAssets] = pydantic.Field()
    """
    Data about each of the accounts open on the Item.
    """

    date_last_updated: dt.datetime = pydantic.Field()
    """
    The date and time when this Item’s data was last retrieved from the financial institution, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format.
    """

    institution_id: str = pydantic.Field()
    """
    The id of the financial institution associated with the Item.
    """

    institution_name: str = pydantic.Field()
    """
    The full financial institution name associated with the Item.
    """

    item_id: ItemId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

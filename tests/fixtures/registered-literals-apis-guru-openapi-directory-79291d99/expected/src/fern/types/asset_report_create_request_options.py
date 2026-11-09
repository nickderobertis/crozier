

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .asset_report_add_ons import AssetReportAddOns
from .asset_report_user import AssetReportUser


class AssetReportCreateRequestOptions(UniversalBaseModel):
    """
    An optional object to filter `/asset_report/create` results. If provided, must be non-`null`. The optional `user` object is required for the report to be eligible for Fannie Mae's Day 1 Certainty program.
    """

    add_ons: typing.Optional[typing.List[AssetReportAddOns]] = pydantic.Field(default=None)
    """
    Use this field to request a `fast_asset` report. When Fast Assets is requested, Plaid will create two versions of the Asset Report: first, the Fast Asset Report, which will contain only current identity and balance information, and later, the Full Asset Report, which will also contain historical balance information and transaction data. A `PRODUCT_READY` webhook will be fired for each Asset Report when it is ready, and the `report_type` field will indicate whether the webhook is firing for the `full` or `fast` Asset Report. To retrieve the Fast Asset Report, call `/asset_report/get` with `fast_report` set to `true`. There is no additional charge for using Fast Assets.
    """

    client_report_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Client-generated identifier, which can be used by lenders to track loan applications.
    """

    include_fast_report: typing.Optional[bool] = pydantic.Field(default=None)
    """
    true to return balance and identity earlier as a fast report. Defaults to false if omitted.
    """

    products: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Additional information that can be included in the asset report. Possible values: `"investments"`
    """

    user: typing.Optional[AssetReportUser] = None
    webhook: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL to which Plaid will send Assets webhooks, for example when the requested Asset Report is ready.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

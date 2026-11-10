

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .asset_report_user import AssetReportUser


class AssetReportRefreshRequestOptions(UniversalBaseModel):
    """
    An optional object to filter `/asset_report/refresh` results. If provided, cannot be `null`. If not specified, the `options` from the original call to `/asset_report/create` will be used.
    """

    client_report_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Client-generated identifier, which can be used by lenders to track loan applications.
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

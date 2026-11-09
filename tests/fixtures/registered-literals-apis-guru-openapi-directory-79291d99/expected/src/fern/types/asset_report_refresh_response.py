

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .asset_report_id import AssetReportId
from .asset_report_token import AssetReportToken
from .request_id import RequestId


class AssetReportRefreshResponse(UniversalBaseModel):
    """
    AssetReportRefreshResponse defines the response schema for `/asset_report/refresh`
    """

    asset_report_id: AssetReportId
    asset_report_token: AssetReportToken
    request_id: RequestId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

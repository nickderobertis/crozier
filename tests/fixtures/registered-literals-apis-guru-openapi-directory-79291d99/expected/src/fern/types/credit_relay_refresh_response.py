

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .asset_report_id import AssetReportId
from .request_id import RequestId


class CreditRelayRefreshResponse(UniversalBaseModel):
    """
    CreditRelayRefreshResponse defines the response schema for `/credit/relay/refresh`
    """

    asset_report_id: typing.Optional[AssetReportId] = None
    relay_token: str
    request_id: RequestId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

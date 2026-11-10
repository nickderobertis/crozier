

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .asset_report import AssetReport
from .request_id import RequestId
from .warning import Warning


class AssetReportGetResponse(UniversalBaseModel):
    """
    AssetReportGetResponse defines the response schema for `/asset_report/get`
    """

    report: AssetReport
    request_id: RequestId
    warnings: typing.List[Warning] = pydantic.Field()
    """
    If the Asset Report generation was successful but identity information cannot be returned, this array will contain information about the errors causing identity information to be missing
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

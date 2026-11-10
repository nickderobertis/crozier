

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AssetReportPdfGetRequestOptions(UniversalBaseModel):
    """
    An optional object to filter or add data to `/asset_report/get` results. If provided, must be non-`null`.
    """

    days_to_include: typing.Optional[int] = pydantic.Field(default=None)
    """
    The maximum integer number of days of history to include in the Asset Report.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

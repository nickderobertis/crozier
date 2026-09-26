

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ProvidersSummaryResponse(UniversalBaseModel):
    brand_color: typing.Optional[str] = None
    default_locale: typing.Optional[str] = None
    endpoints_count: int
    export_preset: typing.Optional[str] = None
    monthly_cap_usd: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

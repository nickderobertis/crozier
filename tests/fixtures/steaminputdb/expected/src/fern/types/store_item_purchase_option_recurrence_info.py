

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class StoreItemPurchaseOptionRecurrenceInfo(UniversalBaseModel):
    billing_agreement_type: typing.Optional[int] = None
    formatted_renewal_price: typing.Optional[str] = None
    packageid: typing.Optional[int] = None
    renewal_price_in_cents: typing.Optional[int] = None
    renewal_time_period: typing.Optional[int] = None
    renewal_time_unit: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

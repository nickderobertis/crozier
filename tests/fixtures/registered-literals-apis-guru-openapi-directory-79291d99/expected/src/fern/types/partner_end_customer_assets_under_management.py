

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PartnerEndCustomerAssetsUnderManagement(UniversalBaseModel):
    """
    Assets under management for the given end customer. Required for end customers with monthly service commitments.
    """

    amount: float
    iso_currency_code: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

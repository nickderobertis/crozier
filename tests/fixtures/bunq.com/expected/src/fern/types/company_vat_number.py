

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CompanyVatNumber(UniversalBaseModel):
    country: typing.Optional[str] = pydantic.Field(default=None)
    """
    The country of the VAT identification number.
    """

    value: typing.Optional[str] = pydantic.Field(default=None)
    """
    The VAT identification number number.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

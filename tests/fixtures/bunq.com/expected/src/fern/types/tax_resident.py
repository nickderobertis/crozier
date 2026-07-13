

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TaxResident(UniversalBaseModel):
    country: typing.Optional[str] = pydantic.Field(default=None)
    """
    The country of the tax number.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status of the tax number. Either CONFIRMED or UNCONFIRMED.
    """

    tax_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    The tax number.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

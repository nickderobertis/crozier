

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .error import Error
from .v1money import V1Money


class V1PaymentTax(UniversalBaseModel):
    """
    V1PaymentTax
    """

    applied_money: typing.Optional[V1Money] = None
    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Any errors that occurred during the request.
    """

    fee_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the tax, if available. Taxes applied in older versions of Square Register might not have an ID.
    """

    inclusion_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Whether the tax is an ADDITIVE tax or an INCLUSIVE tax.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The merchant-defined name of the tax.
    """

    rate: typing.Optional[str] = pydantic.Field(default=None)
    """
    The rate of the tax, as a string representation of a decimal number. A value of 0.07 corresponds to a rate of 7%.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

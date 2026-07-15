

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TaxRatesFilter(UniversalBaseModel):
    assets: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Boolean to describe if tax rate can be used for asset accounts
    """

    equity: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Boolean to describe if tax rate can be used for equity accounts
    """

    expenses: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Boolean to describe if tax rate can be used for expense accounts
    """

    liabilities: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Boolean to describe if tax rate can be used for liability accounts
    """

    revenue: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Boolean to describe if tax rate can be used for revenue accounts
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

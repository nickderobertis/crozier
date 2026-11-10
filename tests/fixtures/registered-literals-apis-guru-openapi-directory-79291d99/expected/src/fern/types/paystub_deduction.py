

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PaystubDeduction(UniversalBaseModel):
    """
    Deduction on the paystub
    """

    is_pretax: typing.Optional[bool] = pydantic.Field(default=None)
    """
    `true` if the deduction is pre-tax; `false` otherwise.
    """

    total: typing.Optional[float] = pydantic.Field(default=None)
    """
    The amount of the deduction.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the deduction, as provided on the paystub. For example: `"401(k)"`, `"FICA MED TAX"`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

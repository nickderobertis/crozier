

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PaymentOptions(UniversalBaseModel):
    """ """

    autocomplete: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether the `Payment` objects created from this `TerminalCheckout` are automatically
    `COMPLETED` or left in an `APPROVED` state for later modification.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

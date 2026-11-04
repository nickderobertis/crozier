

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .checkout_accepted_next_step import CheckoutAcceptedNextStep


class CheckoutAccepted(UniversalBaseModel):
    """
    Response returned when checkout processing requires an additional payer action, such as a 3DS challenge or a redirect to an external payment method page.
    """

    next_step: typing.Optional[CheckoutAcceptedNextStep] = pydantic.Field(default=None)
    """
    Instructions for the next action the payer or client must take.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .checkout_accepted_next_step_mechanism_item import CheckoutAcceptedNextStepMechanismItem


class CheckoutAcceptedNextStep(UniversalBaseModel):
    """
    Instructions for the next action the payer or client must take.
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL to open or submit in order to continue processing.
    """

    method: typing.Optional[str] = pydantic.Field(default=None)
    """
    HTTP method to use when following the next step.
    """

    redirect_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Merchant URL where the payer returns after the external flow finishes.
    """

    mechanism: typing.Optional[typing.List[CheckoutAcceptedNextStepMechanismItem]] = pydantic.Field(default=None)
    """
    Allowed presentation mechanisms for the next step. `iframe` means the flow can be embedded, while `browser` means it can be completed through a full-page redirect.
    """

    payload: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    Parameters required to complete the next step. The exact keys depend on the payment provider and flow type.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

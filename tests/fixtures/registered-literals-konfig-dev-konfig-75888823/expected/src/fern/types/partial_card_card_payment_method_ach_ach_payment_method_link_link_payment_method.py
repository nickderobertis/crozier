

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ach_payment_method import AchPaymentMethod
from .card_payment_method import CardPaymentMethod
from .link_payment_method import LinkPaymentMethod


class PartialCardCardPaymentMethodAchAchPaymentMethodLinkLinkPaymentMethod(UniversalBaseModel):
    """
    Make all properties in T optional
    """

    card: typing.Optional[CardPaymentMethod] = None
    ach: typing.Optional[AchPaymentMethod] = None
    link: typing.Optional[LinkPaymentMethod] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

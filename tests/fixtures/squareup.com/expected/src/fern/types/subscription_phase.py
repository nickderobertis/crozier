

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .money import Money


class SubscriptionPhase(UniversalBaseModel):
    """
    Describes a phase in a subscription plan. For more information, see
    [Set Up and Manage a Subscription Plan](https://developer.squareup.com/docs/subscriptions-api/setup-plan).
    """

    cadence: str = pydantic.Field()
    """
    The billing cadence of the phase. For example, weekly or monthly. This field cannot be changed after a `SubscriptionPhase` is created.
    """

    ordinal: typing.Optional[int] = pydantic.Field(default=None)
    """
    The position this phase appears in the sequence of phases defined for the plan, indexed from 0. This field cannot be changed after a `SubscriptionPhase` is created.
    """

    periods: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of `cadence`s the phase lasts. If not set, the phase never ends. Only the last phase can be indefinite. This field cannot be changed after a `SubscriptionPhase` is created.
    """

    recurring_price_money: Money
    uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Square-assigned ID of the subscription phase. This field cannot be changed after a `SubscriptionPhase` is created.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

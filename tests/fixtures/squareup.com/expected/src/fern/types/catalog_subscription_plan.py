

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .subscription_phase import SubscriptionPhase


class CatalogSubscriptionPlan(UniversalBaseModel):
    """
    Describes a subscription plan. For more information, see
    [Set Up and Manage a Subscription Plan](https://developer.squareup.com/docs/subscriptions-api/setup-plan).
    """

    name: str = pydantic.Field()
    """
    The name of the plan.
    """

    phases: typing.List[SubscriptionPhase] = pydantic.Field()
    """
    A list of SubscriptionPhase containing the [SubscriptionPhase](https://developer.squareup.com/reference/square_2021-08-18/objects/SubscriptionPhase) for this plan.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

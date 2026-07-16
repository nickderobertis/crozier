

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .info import Info


class SubscriptionEvent(UniversalBaseModel):
    """
    Describes changes to subscription and billing states.
    """

    effective_date: str = pydantic.Field()
    """
    The date, in YYYY-MM-DD format (for
    example, 2013-01-15), when the subscription event went into effect.
    """

    id: str = pydantic.Field()
    """
    The ID of the subscription event.
    """

    info: typing.Optional[Info] = None
    plan_id: str = pydantic.Field()
    """
    The ID of the subscription plan associated with the subscription.
    """

    subscription_event_type: str = pydantic.Field()
    """
    Type of the subscription event.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

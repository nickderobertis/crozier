

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .subscription_dto import SubscriptionDto
from .subscriptions_response_limit import SubscriptionsResponseLimit
from .subscriptions_response_offset import SubscriptionsResponseOffset


class SubscriptionsResponse(UniversalBaseModel):
    """
    Модель ответа получения подписок
    """

    subscriptions: typing.Optional[typing.List[SubscriptionDto]] = None
    offset: typing.Optional[SubscriptionsResponseOffset] = None
    limit: typing.Optional[SubscriptionsResponseLimit] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

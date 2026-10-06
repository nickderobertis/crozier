

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .subscribers_response_limit import SubscribersResponseLimit
from .subscribers_response_offset import SubscribersResponseOffset
from .subscription_dto import SubscriptionDto


class SubscribersResponse(UniversalBaseModel):
    """
    Модель ответа получения подписчиков
    """

    subscribers: typing.Optional[typing.List[SubscriptionDto]] = None
    offset: typing.Optional[SubscribersResponseOffset] = None
    limit: typing.Optional[SubscribersResponseLimit] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

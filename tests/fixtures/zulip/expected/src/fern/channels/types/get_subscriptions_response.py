

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.subscription import Subscription


class GetSubscriptionsResponse(UniversalBaseModel):
    result: typing.Optional[typing.Any] = None
    msg: typing.Optional[typing.Any] = None
    ignored_parameters_unsupported: typing.Optional[typing.Any] = None
    subscriptions: typing.List[Subscription] = pydantic.Field()
    """
    A list of dictionaries where each dictionary contains
    information about one of the subscribed channels.
    
    **Changes**: Removed `email_address` field from the dictionary
    in Zulip 8.0 (feature level 226).
    
    Removed `role` field from the dictionary
    in Zulip 6.0 (feature level 133).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

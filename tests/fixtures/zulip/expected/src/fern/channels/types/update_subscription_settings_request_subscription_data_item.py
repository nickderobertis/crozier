

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.subscription_property import SubscriptionProperty
from ...types.subscription_property_value import SubscriptionPropertyValue


class UpdateSubscriptionSettingsRequestSubscriptionDataItem(UniversalBaseModel):
    stream_id: int = pydantic.Field()
    """
    The unique ID of a channel.
    """

    property: SubscriptionProperty
    value: SubscriptionPropertyValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

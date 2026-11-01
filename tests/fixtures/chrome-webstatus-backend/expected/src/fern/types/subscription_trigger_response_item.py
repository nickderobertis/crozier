

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .subscription_trigger_response_value import SubscriptionTriggerResponseValue


class SubscriptionTriggerResponseItem(UniversalBaseModel):
    """
    Represents a single trigger in a subscription response, indicating its status.
    """

    value: SubscriptionTriggerResponseValue
    raw_value: typing.Optional[str] = pydantic.Field(default=None)
    """
    The original, raw value from the database. Only present if the 'value' is 'unknown', allowing clients to identify and manage deprecated triggers.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

from .enum_unknown import EnumUnknown
from .subscription_trigger_writable import SubscriptionTriggerWritable

SubscriptionTriggerResponseValue = typing.Union[SubscriptionTriggerWritable, EnumUnknown]

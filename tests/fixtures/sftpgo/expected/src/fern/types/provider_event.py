

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .provider_event_action import ProviderEventAction
from .provider_event_object_type import ProviderEventObjectType


class ProviderEvent(UniversalBaseModel):
    id: typing.Optional[str] = None
    timestamp: typing.Optional[int] = pydantic.Field(default=None)
    """
    unix timestamp in nanoseconds
    """

    action: typing.Optional[ProviderEventAction] = None
    username: typing.Optional[str] = None
    ip: typing.Optional[str] = None
    object_type: typing.Optional[ProviderEventObjectType] = None
    object_name: typing.Optional[str] = None
    object_data: typing.Optional[str] = pydantic.Field(default=None)
    """
    base64 of the JSON serialized object with sensitive fields removed
    """

    role: typing.Optional[str] = None
    instance_id: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

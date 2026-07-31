

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class MessagingV1LinkshorteningMessagingService(UniversalBaseModel):
    domain_sid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique string identifies the domain resource
    """

    messaging_service_sid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique string that identifies the messaging service
    """

    url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

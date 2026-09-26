

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RegisterQueueResponseRealmAvailableVideoChatProvidersValue(UniversalBaseModel):
    """
    `{provider_name}`: Dictionary containing the details of the
    video call provider with the name of the chat provider as
    the key.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the video call provider.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the video call provider.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

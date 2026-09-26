

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetEventsResponseEventsItemMessageTypeSender(UniversalBaseModel):
    """
    Object describing the user who was previously typing the message.
    """

    user_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The user's ID.
    """

    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Zulip API email address for the user.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

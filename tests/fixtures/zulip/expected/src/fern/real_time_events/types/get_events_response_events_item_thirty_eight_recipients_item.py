

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetEventsResponseEventsItemThirtyEightRecipientsItem(UniversalBaseModel):
    """
    Object containing the user ID and Zulip API email of a recipient.
    """

    user_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the user.
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

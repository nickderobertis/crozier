

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetEventsResponseEventsItemTwoPersonNewEmail(UniversalBaseModel):
    """
    When the Zulip API email address of a user changes,
    either due to the user's email address changing, or
    due to changes in the user's
    [email address visibility][help-email-visibility].

    [help-email-visibility]: /help/configure-email-visibility
    """

    user_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the user affected by this change.
    """

    new_email: typing.Optional[str] = pydantic.Field(default=None)
    """
    The new value of `email` for the user. The client
    should update any data structures associated
    with this user to use this new value as the
    user's Zulip API email address.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

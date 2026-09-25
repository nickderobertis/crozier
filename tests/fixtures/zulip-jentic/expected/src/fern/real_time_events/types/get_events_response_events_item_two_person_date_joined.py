

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetEventsResponseEventsItemTwoPersonDateJoined(UniversalBaseModel):
    """
    Sent when the `date_joined` value is updated after an
    imported stub user or a user created via the API logs
    in for the first time.

    **Changes**: New in Zulip 12.0 (feature level 475).
    """

    user_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the user affected by this change.
    """

    date_joined: typing.Optional[str] = pydantic.Field(default=None)
    """
    The time when the user logged in to their account
    for the first time.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetEventsResponseEventsItemTwoPersonEmail(UniversalBaseModel):
    """
    When a user changes their [profile time zone](/help/change-your-timezone).
    """

    user_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of modified user.
    """

    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Zulip API email of the user.
    
    **Deprecated**: This field will be removed in a future
    release as it is redundant with the `user_id`.
    """

    timezone: typing.Optional[str] = pydantic.Field(default=None)
    """
    The IANA identifier of the new profile time zone for the user.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

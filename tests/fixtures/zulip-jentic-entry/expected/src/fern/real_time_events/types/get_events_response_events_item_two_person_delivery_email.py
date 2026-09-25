

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetEventsResponseEventsItemTwoPersonDeliveryEmail(UniversalBaseModel):
    """
    When the value of a user's delivery email as visible to you changes,
    either due to the email address changing or your access to the user's
    email changing via an update to their `email_address_visibility`
    setting.

    **Changes**: Prior to Zulip 7.0 (feature level 163), this event was
    sent only to the affected user, and this event would only be triggered
    by changing the affected user's delivery email.
    """

    user_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the user affected by this change.
    """

    delivery_email: typing.Optional[str] = pydantic.Field(default=None)
    """
    The new delivery email of the user.
    
    This value can be `null` if the affected user
    changed their `email_address_visibility` setting
    such that you cannot access their real email.
    
    **Changes**: Before Zulip 7.0 (feature level 163),
    `null` was not a possible value for this event as
    it was only sent to the affected user when their
    email address was changed.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

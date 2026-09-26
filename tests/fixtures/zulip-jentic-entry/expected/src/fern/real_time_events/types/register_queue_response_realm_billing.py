

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RegisterQueueResponseRealmBilling(UniversalBaseModel):
    """
    Present if `realm_billing` is present in `fetch_event_types`.

    A dictionary containing billing information of the organization.

    **Changes**: New in Zulip 10.0 (feature level 363).
    """

    has_pending_sponsorship_request: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether there is a pending sponsorship request for the organization. Note that
    this field will always be `false` if the user is not in `can_manage_billing_group`.
    
    **Changes**: New in Zulip 10.0 (feature level 363).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

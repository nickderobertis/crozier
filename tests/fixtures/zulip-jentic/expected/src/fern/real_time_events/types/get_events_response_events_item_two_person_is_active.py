

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetEventsResponseEventsItemTwoPersonIsActive(UniversalBaseModel):
    """
    When a user is deactivated or reactivated. Only
    users who can access the modified user under the
    organization's `can_access_all_users_group` policy
    will receive this event.

    Clients receiving a deactivation event should
    remove the user from all user groups in their data
    structures, because deactivated users cannot be
    members of groups.

    **Changes**: Prior to Zulip 10.0 (feature level
    303), reactivation events were sent to users who
    could not access the reactivated user due to a
    `can_access_all_users_group` policy. Also,
    previously, Clients were not required to update
    group membership records during user deactivation.

    New in Zulip 8.0 (feature level 222). Previously the server
    sent a `realm_user` event with `op` field set to `remove`
    when deactivating a user and a `realm_user` event with `op`
    field set to `add` when reactivating a user.
    """

    user_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the user affected by this change.
    """

    is_active: typing.Optional[bool] = pydantic.Field(default=None)
    """
    A boolean describing whether the user account has been deactivated.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

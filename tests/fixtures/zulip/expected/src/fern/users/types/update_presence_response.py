

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .update_presence_response_presences_value import UpdatePresenceResponsePresencesValue


class UpdatePresenceResponse(UniversalBaseModel):
    result: typing.Any
    msg: typing.Any
    ignored_parameters_unsupported: typing.Optional[typing.Any] = None
    presence_last_update_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The identifier for the latest user presence data returned in
    the `presences` data of the response.
    
    If a value was passed for `last_update_id`, then this is
    guaranteed to be equal to or greater than that value. If it
    is the same value, then that indicates to the client that
    there were no updates to previously received user presence
    data.
    
    The client should then pass this value as the `last_update_id`
    parameter when it next queries this endpoint, in order to only
    receive new user presence data and avoid redundantly fetching
    already known information.
    
    This will be `-1` if no value was passed for
    [`last_update_id`](#parameter-last_update_id) and no user
    presence data was returned by the server. This can happen, for
    example, if an organization has disabled presence.
    
    **Changes**: New in Zulip 9.0 (feature level 263).
    """

    server_timestamp: typing.Optional[float] = pydantic.Field(default=None)
    """
    Only present if `ping_only` is `false`.
    
    The time when the server fetched the `presences` data included
    in the response.
    """

    presences: typing.Optional[typing.Dict[str, UpdatePresenceResponsePresencesValue]] = pydantic.Field(default=None)
    """
    Only present if `ping_only` is `false`.
    
    A dictionary where each entry describes the presence details
    of a user in the Zulip organization. Entries can be in either
    the modern presence format or the legacy presence format.
    
    These entries will be the modern presence format when the
    `last_updated_id` parameter is passed, or when the deprecated
    `slim_presence` parameter is `true`.
    
    If the deprecated `slim_presence` parameter is `false` and the
    `last_updated_id` parameter is omitted, the entries will be in
    the legacy presence API format.
    
    **Note**: The legacy presence format should only be used when
    interacting with old servers. It will be removed as soon as
    doing so is practical.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

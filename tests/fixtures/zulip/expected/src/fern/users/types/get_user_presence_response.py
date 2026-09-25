

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_user_presence_response_presence import GetUserPresenceResponsePresence


class GetUserPresenceResponse(UniversalBaseModel):
    result: typing.Optional[typing.Any] = None
    msg: typing.Optional[typing.Any] = None
    ignored_parameters_unsupported: typing.Optional[typing.Any] = None
    server_timestamp: typing.Optional[float] = pydantic.Field(default=None)
    """
    The time when the server fetched the `presence` data
    included in the response. Matches the similar field
    in other presence responses.
    
    **Changes**: New in Zulip 12.0 (feature level 497).
    """

    presence: typing.Optional[GetUserPresenceResponsePresence] = pydantic.Field(default=None)
    """
    An object containing the presence details for the user.
    
    The object contains both the modern format fields
    (`active_timestamp` and `idle_timestamp`) and the legacy
    format fields (`website` and `aggregated` dictionaries,
    which contain a timestamp and a status string). New
    integrations should use the modern fields; the legacy
    fields are retained for backwards compatibility.
    
    **Changes**: In Zulip 12.0 (feature level 497),
    the `website` and `aggregated` legacy dictionaries were
    restored alongside the modern fields, for backwards
    compatibility with integrations written against earlier
    versions of the API.
    
    In Zulip 12.0 (feature level 487), the `active_timestamp`
    and `idle_timestamp` fields were added to this object, and
    the `website` and `aggregated` dictionaries were
    temporarily removed.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

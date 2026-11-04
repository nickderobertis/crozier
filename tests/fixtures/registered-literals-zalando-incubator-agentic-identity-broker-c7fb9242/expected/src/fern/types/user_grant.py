

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class UserGrant(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    Unique grant identifier
    """

    principal: str = pydantic.Field()
    """
    User principal who created the grant
    """

    agent_id: str = pydantic.Field()
    """
    Agent receiving the delegated access
    """

    valid_until: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Optional grant expiration (ISO 8601 format).
    Null indicates indefinite grant (no expiration).
    Expired grants are filtered out automatically.
    """

    granted_permission_sets: typing.Dict[str, typing.List[str]] = pydantic.Field()
    """
    Map of granted permission sets. Keys are permission set UUIDs, values are arrays of service UUIDs included in that permission set grant.
    Empty object `{}` is only allowed when revoking (POST endpoint).
    """

    created_at: dt.datetime = pydantic.Field()
    """
    ISO 8601 timestamp when grant was created
    """

    updated_at: dt.datetime = pydantic.Field()
    """
    ISO 8601 timestamp when grant was last updated
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

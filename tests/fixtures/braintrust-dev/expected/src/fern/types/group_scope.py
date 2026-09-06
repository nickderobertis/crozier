

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .group_scope_type import GroupScopeType


class GroupScope(UniversalBaseModel):
    """
    Process spans/traces grouped by a field (e.g., session_id)
    """

    type: GroupScopeType
    group_by: str = pydantic.Field()
    """
    Field path to group by, e.g. metadata.session_id
    """

    idle_seconds: typing.Optional[float] = pydantic.Field(default=None)
    """
    Optional: trigger after this many seconds of inactivity
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

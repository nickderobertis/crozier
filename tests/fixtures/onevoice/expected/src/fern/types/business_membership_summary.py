

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .business_membership_role_ref import BusinessMembershipRoleRef


class BusinessMembershipSummary(UniversalBaseModel):
    id: str
    name: str
    role: BusinessMembershipRoleRef
    status: str
    deletion_pending_until: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Present for pending-deletion organizations, including the last organization. Restore via POST /businesses/{id}/restore before this deadline; ordinary organization reads remain unavailable.
    """

    joined_at: dt.datetime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

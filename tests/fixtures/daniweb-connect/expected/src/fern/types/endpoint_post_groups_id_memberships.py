

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .endpoint_post_groups_id_memberships_data import EndpointPostGroupsIdMembershipsData


class EndpointPostGroupsIdMemberships(UniversalBaseModel):
    data: typing.Optional[EndpointPostGroupsIdMembershipsData] = None
    success: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(EndpointPostGroupsIdMemberships)

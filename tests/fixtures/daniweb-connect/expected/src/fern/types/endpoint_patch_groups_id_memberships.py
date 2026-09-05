

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .api_pagination import ApiPagination
from .endpoint_patch_groups_id_memberships_data_item import EndpointPatchGroupsIdMembershipsDataItem


class EndpointPatchGroupsIdMemberships(UniversalBaseModel):
    data: typing.Optional[typing.List[EndpointPatchGroupsIdMembershipsDataItem]] = None
    pagination: typing.Optional[ApiPagination] = None
    success: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(EndpointPatchGroupsIdMemberships)

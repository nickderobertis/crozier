

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .endpoint_get_users_id_synergies_data_item import EndpointGetUsersIdSynergiesDataItem


class EndpointGetUsersIdSynergies(UniversalBaseModel):
    data: typing.Optional[typing.List[EndpointGetUsersIdSynergiesDataItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(EndpointGetUsersIdSynergies)

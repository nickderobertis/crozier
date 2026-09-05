

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .endpoint_patch_users_id_synergies_data import EndpointPatchUsersIdSynergiesData


class EndpointPatchUsersIdSynergies(UniversalBaseModel):
    data: typing.Optional[EndpointPatchUsersIdSynergiesData] = None
    success: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

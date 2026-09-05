

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .endpoint_post_audiences_id_memberships_data import EndpointPostAudiencesIdMembershipsData


class EndpointPostAudiencesIdMemberships(UniversalBaseModel):
    data: typing.Optional[EndpointPostAudiencesIdMembershipsData] = None
    success: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

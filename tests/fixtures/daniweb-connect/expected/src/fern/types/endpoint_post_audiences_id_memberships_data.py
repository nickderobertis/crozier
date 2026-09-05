

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .endpoint_post_audiences_id_memberships_data_audience import EndpointPostAudiencesIdMembershipsDataAudience
from .user import User


class EndpointPostAudiencesIdMembershipsData(UniversalBaseModel):
    audience: typing.Optional[EndpointPostAudiencesIdMembershipsDataAudience] = None
    member: typing.Optional[User] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

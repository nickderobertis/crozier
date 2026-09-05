

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .endpoint_post_users_invites_data_discovered import EndpointPostUsersInvitesDataDiscovered
from .endpoint_post_users_invites_data_emailed import EndpointPostUsersInvitesDataEmailed
from .endpoint_post_users_invites_data_existing import EndpointPostUsersInvitesDataExisting
from .endpoint_post_users_invites_data_invalid import EndpointPostUsersInvitesDataInvalid


class EndpointPostUsersInvitesData(UniversalBaseModel):
    discovered: typing.Optional[EndpointPostUsersInvitesDataDiscovered] = None
    emailed: typing.Optional[EndpointPostUsersInvitesDataEmailed] = None
    existing: typing.Optional[EndpointPostUsersInvitesDataExisting] = None
    invalid: typing.Optional[EndpointPostUsersInvitesDataInvalid] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .endpoint_get_users_nearby_data_item_distance_away import EndpointGetUsersNearbyDataItemDistanceAway
from .user import User


class EndpointGetUsersNearbyDataItem(UniversalBaseModel):
    distance_away: typing.Optional[EndpointGetUsersNearbyDataItemDistanceAway] = None
    user: typing.Optional[User] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

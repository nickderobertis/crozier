

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .endpoint_get_users_id_synergies_data_item_match_distance_away import (
    EndpointGetUsersIdSynergiesDataItemMatchDistanceAway,
)
from .endpoint_get_users_id_synergies_data_item_match_industry import EndpointGetUsersIdSynergiesDataItemMatchIndustry
from .endpoint_get_users_id_synergies_data_item_match_mutual_connections import (
    EndpointGetUsersIdSynergiesDataItemMatchMutualConnections,
)


class EndpointGetUsersIdSynergiesDataItemMatch(UniversalBaseModel):
    algorithmic_match: typing.Optional[bool] = None
    complementary_goals: typing.Optional[typing.List[str]] = None
    distance_away: typing.Optional[EndpointGetUsersIdSynergiesDataItemMatchDistanceAway] = None
    industry: typing.Optional[EndpointGetUsersIdSynergiesDataItemMatchIndustry] = None
    mutual_connections: typing.Optional[EndpointGetUsersIdSynergiesDataItemMatchMutualConnections] = None
    recommendation_strength: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .endpoint_get_users_id_synergies_data_item_additional import EndpointGetUsersIdSynergiesDataItemAdditional
from .endpoint_get_users_id_synergies_data_item_match import EndpointGetUsersIdSynergiesDataItemMatch
from .endpoint_get_users_id_synergies_data_item_meet import EndpointGetUsersIdSynergiesDataItemMeet
from .endpoint_get_users_id_synergies_data_item_relationship import EndpointGetUsersIdSynergiesDataItemRelationship


class EndpointGetUsersIdSynergiesDataItem(UniversalBaseModel):
    additional: typing.Optional[EndpointGetUsersIdSynergiesDataItemAdditional] = None
    conversation: typing.Optional["Conversation"] = None
    match: typing.Optional[EndpointGetUsersIdSynergiesDataItemMatch] = None
    meet: typing.Optional[EndpointGetUsersIdSynergiesDataItemMeet] = None
    relationship: typing.Optional[EndpointGetUsersIdSynergiesDataItemRelationship] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .conversation import Conversation
from .message import Message

update_forward_refs(EndpointGetUsersIdSynergiesDataItem, Conversation=Conversation, Message=Message)

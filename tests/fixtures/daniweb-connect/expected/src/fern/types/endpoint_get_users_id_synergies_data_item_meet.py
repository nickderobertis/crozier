

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .endpoint_get_users_id_synergies_data_item_meet_payment import EndpointGetUsersIdSynergiesDataItemMeetPayment


class EndpointGetUsersIdSynergiesDataItemMeet(UniversalBaseModel):
    payment: typing.Optional[EndpointGetUsersIdSynergiesDataItemMeetPayment] = None
    price_usd: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

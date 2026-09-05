

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .endpoint_get_users_id_synergies_data_item_meet_payment_paypal import (
    EndpointGetUsersIdSynergiesDataItemMeetPaymentPaypal,
)


class EndpointGetUsersIdSynergiesDataItemMeetPayment(UniversalBaseModel):
    paypal: typing.Optional[EndpointGetUsersIdSynergiesDataItemMeetPaymentPaypal] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

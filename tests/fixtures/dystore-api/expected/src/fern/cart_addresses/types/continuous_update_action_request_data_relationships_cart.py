

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .continuous_update_action_request_data_relationships_cart_data import (
    ContinuousUpdateActionRequestDataRelationshipsCartData,
)


class ContinuousUpdateActionRequestDataRelationshipsCart(UniversalBaseModel):
    data: typing.Optional[ContinuousUpdateActionRequestDataRelationshipsCartData] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

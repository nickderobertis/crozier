

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .selected_fulfillment_option_zero_type import SelectedFulfillmentOptionZeroType


class SelectedFulfillmentOptionZero(UniversalBaseModel):
    type: typing.Optional[SelectedFulfillmentOptionZeroType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

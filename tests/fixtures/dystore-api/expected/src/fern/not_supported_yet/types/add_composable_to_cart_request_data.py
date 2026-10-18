

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .add_composable_to_cart_request_data_attributes import AddComposableToCartRequestDataAttributes


class AddComposableToCartRequestData(UniversalBaseModel):
    attributes: typing.Optional[AddComposableToCartRequestDataAttributes] = None
    type: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

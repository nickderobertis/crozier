

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .add_composable_to_cart_request_data_attributes_components_item import (
    AddComposableToCartRequestDataAttributesComponentsItem,
)
from .add_composable_to_cart_request_data_attributes_composable import (
    AddComposableToCartRequestDataAttributesComposable,
)


class AddComposableToCartRequestDataAttributes(UniversalBaseModel):
    components: typing.Optional[typing.List[AddComposableToCartRequestDataAttributesComponentsItem]] = None
    composable: typing.Optional[AddComposableToCartRequestDataAttributesComposable] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .create_cart_line_add_to_cart_request_data_attributes import CreateCartLineAddToCartRequestDataAttributes


class CreateCartLineAddToCartRequestData(UniversalBaseModel):
    attributes: typing.Optional[CreateCartLineAddToCartRequestDataAttributes] = None
    type: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

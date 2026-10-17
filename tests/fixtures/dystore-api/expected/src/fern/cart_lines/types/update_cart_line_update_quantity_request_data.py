

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .update_cart_line_update_quantity_request_data_attributes import UpdateCartLineUpdateQuantityRequestDataAttributes


class UpdateCartLineUpdateQuantityRequestData(UniversalBaseModel):
    attributes: typing.Optional[UpdateCartLineUpdateQuantityRequestDataAttributes] = None
    id: typing.Optional[str] = None
    type: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .attach_shipping_option_action_request_data_attributes import AttachShippingOptionActionRequestDataAttributes


class AttachShippingOptionActionRequestData(UniversalBaseModel):
    attributes: typing.Optional[AttachShippingOptionActionRequestDataAttributes] = None
    id: typing.Optional[str] = None
    type: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .link_delivery_delivery_method import LinkDeliveryDeliveryMethod


class LinkDeliveryCommunicationMethod(UniversalBaseModel):
    """
    The communication method containing both the type and address to send the URL.
    """

    address: typing.Optional[str] = pydantic.Field(default=None)
    """
    The phone number / email address that link delivery sessions are delivered to. Phone numbers must be in E.164 format.
    """

    method: typing.Optional[LinkDeliveryDeliveryMethod] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

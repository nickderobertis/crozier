

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .link_delivery_communication_method import LinkDeliveryCommunicationMethod


class LinkDeliveryRecipient(UniversalBaseModel):
    """
    Metadata related to the recipient. If the information required to populate this field is not available, leave it blank.
    """

    communication_methods: typing.Optional[typing.List[LinkDeliveryCommunicationMethod]] = pydantic.Field(default=None)
    """
    The list of communication methods to send the Link Delivery URL to. If delivery is not required, leave this field blank.
    """

    first_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    First name of the recipient. Will be used in the body of the email / text (if configured). If this information is not available, leave this field blank.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

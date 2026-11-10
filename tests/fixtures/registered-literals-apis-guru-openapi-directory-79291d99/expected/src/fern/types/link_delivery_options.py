

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .link_delivery_recipient import LinkDeliveryRecipient


class LinkDeliveryOptions(UniversalBaseModel):
    """
    Optional metadata related to the link delivery session
    """

    recipient: typing.Optional[LinkDeliveryRecipient] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

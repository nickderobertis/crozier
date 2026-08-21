

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .distribution_list_items_item_origins_items_item_custom_origin_config_origin_ssl_protocols_items_item import (
    DistributionListItemsItemOriginsItemsItemCustomOriginConfigOriginSslProtocolsItemsItem,
)


class DistributionListItemsItemOriginsItemsItemCustomOriginConfigOriginSslProtocols(UniversalBaseModel):
    """
    The SSL/TLS protocols that you want CloudFront to use when communicating with your origin over HTTPS.
    """

    quantity: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="Quantity"),
        pydantic.Field(
            alias="Quantity",
            description="The number of SSL/TLS protocols that you want to allow CloudFront to use when establishing an HTTPS connection with this origin. ",
        ),
    ]
    """
    The number of SSL/TLS protocols that you want to allow CloudFront to use when establishing an HTTPS connection with this origin. 
    """

    items: typing_extensions.Annotated[
        typing.List[DistributionListItemsItemOriginsItemsItemCustomOriginConfigOriginSslProtocolsItemsItem],
        FieldMetadata(alias="Items"),
        pydantic.Field(
            alias="Items", description="A list that contains allowed SSL/TLS protocols for this distribution."
        ),
    ]
    """
    A list that contains allowed SSL/TLS protocols for this distribution.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

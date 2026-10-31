

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .available_sku_request_sku_names_item import AvailableSkuRequestSkuNamesItem
from .available_sku_request_transfer_type import AvailableSkuRequestTransferType


class AvailableSkuRequest(UniversalBaseModel):
    """
    The filters for showing the available skus.
    """

    country: str = pydantic.Field()
    """
    ISO country code. Country for hardware shipment. For codes check: https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements
    """

    location: str = pydantic.Field()
    """
    Location for data transfer. For locations check: https://management.azure.com/subscriptions/SUBSCRIPTIONID/locations?api-version=2018-01-01
    """

    sku_names: typing_extensions.Annotated[
        typing.Optional[typing.List[AvailableSkuRequestSkuNamesItem]],
        FieldMetadata(alias="skuNames"),
        pydantic.Field(alias="skuNames", description="Sku Names to filter for available skus"),
    ] = None
    """
    Sku Names to filter for available skus
    """

    transfer_type: typing_extensions.Annotated[
        AvailableSkuRequestTransferType,
        FieldMetadata(alias="transferType"),
        pydantic.Field(alias="transferType", description="Type of the transfer."),
    ]
    """
    Type of the transfer.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

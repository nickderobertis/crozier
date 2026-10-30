

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .fulfillment_simulation_external_marketplace_response_items_item import (
    FulfillmentSimulationExternalMarketplaceResponseItemsItem,
)
from .fulfillment_simulation_external_marketplace_response_logistics_info_item import (
    FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItem,
)
from .fulfillment_simulation_external_marketplace_response_payment_data import (
    FulfillmentSimulationExternalMarketplaceResponsePaymentData,
)
from .fulfillment_simulation_external_marketplace_response_rates_and_benefits_data import (
    FulfillmentSimulationExternalMarketplaceResponseRatesAndBenefitsData,
)


class FulfillmentSimulationExternalMarketplaceResponse(UniversalBaseModel):
    country: typing.Optional[str] = pydantic.Field(default=None)
    """
    Three letter ISO code of the country of the shipping address.
    """

    items: typing.Optional[typing.List[FulfillmentSimulationExternalMarketplaceResponseItemsItem]] = pydantic.Field(
        default=None
    )
    """
    Information on each item in the cart.
    """

    logistics_info: typing_extensions.Annotated[
        typing.Optional[typing.List[FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItem]],
        FieldMetadata(alias="logisticsInfo"),
        pydantic.Field(
            alias="logisticsInfo",
            description="Array with logistics information on each item of the `items` array in the `orderForm`.",
        ),
    ] = None
    """
    Array with logistics information on each item of the `items` array in the `orderForm`.
    """

    marketing_data: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="marketingData"),
        pydantic.Field(
            alias="marketingData",
            description="Object containing promotion data such as coupon tracking information and internal or external UTMs.",
        ),
    ] = None
    """
    Object containing promotion data such as coupon tracking information and internal or external UTMs.
    """

    payment_data: typing_extensions.Annotated[
        typing.Optional[FulfillmentSimulationExternalMarketplaceResponsePaymentData],
        FieldMetadata(alias="paymentData"),
        pydantic.Field(alias="paymentData", description="Payment data information."),
    ] = None
    """
    Payment data information.
    """

    postal_code: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="postalCode"),
        pydantic.Field(alias="postalCode", description="Postal Code."),
    ] = None
    """
    Postal Code.
    """

    rates_and_benefits_data: typing_extensions.Annotated[
        typing.Optional[FulfillmentSimulationExternalMarketplaceResponseRatesAndBenefitsData],
        FieldMetadata(alias="ratesAndBenefitsData"),
        pydantic.Field(
            alias="ratesAndBenefitsData", description="Information on rates and benefits that apply to the order."
        ),
    ] = None
    """
    Information on rates and benefits that apply to the order.
    """

    selectable_gifts: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.Any]],
        FieldMetadata(alias="selectableGifts"),
        pydantic.Field(
            alias="selectableGifts", description="Array containing the data of the item selected as a gift."
        ),
    ] = None
    """
    Array containing the data of the item selected as a gift.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

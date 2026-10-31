

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .fulfillment_simulation_external_marketplace_response_payment_data_payment_systems_item import (
    FulfillmentSimulationExternalMarketplaceResponsePaymentDataPaymentSystemsItem,
)


class FulfillmentSimulationExternalMarketplaceResponsePaymentData(UniversalBaseModel):
    """
    Payment data information.
    """

    available_accounts: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.Any]],
        FieldMetadata(alias="availableAccounts"),
        pydantic.Field(alias="availableAccounts", description="Available accounts."),
    ] = None
    """
    Available accounts.
    """

    available_associations: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="availableAssociations"),
        pydantic.Field(alias="availableAssociations", description="Available associations."),
    ] = None
    """
    Available associations.
    """

    available_tokens: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.Any]],
        FieldMetadata(alias="availableTokens"),
        pydantic.Field(alias="availableTokens", description="Available tokens."),
    ] = None
    """
    Available tokens.
    """

    gift_card_messages: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.Any]],
        FieldMetadata(alias="giftCardMessages"),
        pydantic.Field(alias="giftCardMessages", description="Array of gift card messages."),
    ] = None
    """
    Array of gift card messages.
    """

    gift_cards: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.Any]],
        FieldMetadata(alias="giftCards"),
        pydantic.Field(alias="giftCards", description="Gift card information, if it applies to the order."),
    ] = None
    """
    Gift card information, if it applies to the order.
    """

    installment_options: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.Any]],
        FieldMetadata(alias="installmentOptions"),
        pydantic.Field(alias="installmentOptions", description="Installment options information."),
    ] = None
    """
    Installment options information.
    """

    payment_systems: typing_extensions.Annotated[
        typing.Optional[typing.List[FulfillmentSimulationExternalMarketplaceResponsePaymentDataPaymentSystemsItem]],
        FieldMetadata(alias="paymentSystems"),
        pydantic.Field(alias="paymentSystems", description="Information on payment systems."),
    ] = None
    """
    Information on payment systems.
    """

    payments: typing.Optional[typing.List[typing.Any]] = pydantic.Field(default=None)
    """
    Information on each payment.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

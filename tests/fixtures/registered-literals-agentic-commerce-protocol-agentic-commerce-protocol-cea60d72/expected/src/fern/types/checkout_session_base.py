

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .authentication_metadata import AuthenticationMetadata
from .authentication_provider import AuthenticationProvider
from .buyer import Buyer
from .checkout_session_base_fulfillment_options_item import CheckoutSessionBaseFulfillmentOptionsItem
from .checkout_session_base_messages_item import CheckoutSessionBaseMessagesItem
from .checkout_session_base_status import CheckoutSessionBaseStatus
from .fulfillment_details import FulfillmentDetails
from .line_item import LineItem
from .link import Link
from .payment_provider import PaymentProvider
from .selected_fulfillment_option import SelectedFulfillmentOption
from .total import Total


class CheckoutSessionBase(UniversalBaseModel):
    id: str
    buyer: typing.Optional[Buyer] = None
    payment_provider: typing.Optional[PaymentProvider] = None
    authentication_provider: typing.Optional[AuthenticationProvider] = None
    status: CheckoutSessionBaseStatus
    currency: str
    line_items: typing.List[LineItem]
    fulfillment_details: typing.Optional[FulfillmentDetails] = None
    fulfillment_options: typing.List[CheckoutSessionBaseFulfillmentOptionsItem]
    selected_fulfillment_options: typing.Optional[typing.List[SelectedFulfillmentOption]] = None
    totals: typing.List[Total]
    messages: typing.List[CheckoutSessionBaseMessagesItem]
    links: typing.List[Link]
    authentication_metadata: typing.Optional[AuthenticationMetadata] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

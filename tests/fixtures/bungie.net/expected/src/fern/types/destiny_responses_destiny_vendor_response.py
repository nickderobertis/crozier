

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_item_component_set_ofint32 import DestinyItemComponentSetOfint32
from .dictionary_component_response_ofint32and_destiny_vendor_sale_item_component import (
    DictionaryComponentResponseOfint32AndDestinyVendorSaleItemComponent,
)
from .single_component_response_of_destiny_currencies_component import (
    SingleComponentResponseOfDestinyCurrenciesComponent,
)
from .single_component_response_of_destiny_string_variables_component import (
    SingleComponentResponseOfDestinyStringVariablesComponent,
)
from .single_component_response_of_destiny_vendor_categories_component import (
    SingleComponentResponseOfDestinyVendorCategoriesComponent,
)
from .single_component_response_of_destiny_vendor_component import SingleComponentResponseOfDestinyVendorComponent


class DestinyResponsesDestinyVendorResponse(UniversalBaseModel):
    """
    A response containing all of the components for a vendor.
    """

    categories: typing.Optional[SingleComponentResponseOfDestinyVendorCategoriesComponent] = pydantic.Field(
        default=None
    )
    """
    Categories that the vendor has available, and references to the sales therein.
    COMPONENT TYPE: VendorCategories
    """

    currency_lookups: typing_extensions.Annotated[
        typing.Optional[SingleComponentResponseOfDestinyCurrenciesComponent],
        FieldMetadata(alias="currencyLookups"),
        pydantic.Field(
            alias="currencyLookups",
            description='A "lookup" convenience component that can be used to quickly check if the character has access to items that can be used for purchasing.\r\nCOMPONENT TYPE: CurrencyLookups',
        ),
    ] = None
    """
    A "lookup" convenience component that can be used to quickly check if the character has access to items that can be used for purchasing.
    COMPONENT TYPE: CurrencyLookups
    """

    item_components: typing_extensions.Annotated[
        typing.Optional[DestinyItemComponentSetOfint32],
        FieldMetadata(alias="itemComponents"),
        pydantic.Field(
            alias="itemComponents",
            description="Item components, keyed by the vendorItemIndex of the active sale items.\r\nCOMPONENT TYPE: [See inside the DestinyItemComponentSet contract for component types.]",
        ),
    ] = None
    """
    Item components, keyed by the vendorItemIndex of the active sale items.
    COMPONENT TYPE: [See inside the DestinyItemComponentSet contract for component types.]
    """

    sales: typing.Optional[DictionaryComponentResponseOfint32AndDestinyVendorSaleItemComponent] = pydantic.Field(
        default=None
    )
    """
    Sales, keyed by the vendorItemIndex of the item being sold.
    COMPONENT TYPE: VendorSales
    """

    string_variables: typing_extensions.Annotated[
        typing.Optional[SingleComponentResponseOfDestinyStringVariablesComponent],
        FieldMetadata(alias="stringVariables"),
        pydantic.Field(
            alias="stringVariables",
            description="A map of string variable values by hash for this character context.\r\nCOMPONENT TYPE: StringVariables",
        ),
    ] = None
    """
    A map of string variable values by hash for this character context.
    COMPONENT TYPE: StringVariables
    """

    vendor: typing.Optional[SingleComponentResponseOfDestinyVendorComponent] = pydantic.Field(default=None)
    """
    The base properties of the vendor.
    COMPONENT TYPE: Vendors
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

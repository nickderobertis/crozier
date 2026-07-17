

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_item_component_set_ofint32 import DestinyItemComponentSetOfint32
from .dictionary_component_response_ofuint32and_destiny_vendor_categories_component import (
    DictionaryComponentResponseOfuint32AndDestinyVendorCategoriesComponent,
)
from .dictionary_component_response_ofuint32and_destiny_vendor_component import (
    DictionaryComponentResponseOfuint32AndDestinyVendorComponent,
)
from .dictionary_component_response_ofuint32and_personal_destiny_vendor_sale_item_set_component import (
    DictionaryComponentResponseOfuint32AndPersonalDestinyVendorSaleItemSetComponent,
)
from .single_component_response_of_destiny_currencies_component import (
    SingleComponentResponseOfDestinyCurrenciesComponent,
)
from .single_component_response_of_destiny_string_variables_component import (
    SingleComponentResponseOfDestinyStringVariablesComponent,
)
from .single_component_response_of_destiny_vendor_group_component import (
    SingleComponentResponseOfDestinyVendorGroupComponent,
)


class DestinyResponsesDestinyVendorsResponse(UniversalBaseModel):
    """
    A response containing all of the components for all requested vendors.
    """

    categories: typing.Optional[DictionaryComponentResponseOfuint32AndDestinyVendorCategoriesComponent] = (
        pydantic.Field(default=None)
    )
    """
    Categories that the vendor has available, and references to the sales therein. These are keyed by the Vendor Hash, so you will get one Categories Component per vendor returned.
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
        typing.Optional[typing.Dict[str, DestinyItemComponentSetOfint32]],
        FieldMetadata(alias="itemComponents"),
        pydantic.Field(
            alias="itemComponents",
            description="The set of item detail components, one set of item components per Vendor. These are keyed by the Vendor Hash, so you will get one Item Component Set per vendor returned.\r\nThe components contained inside are themselves keyed by the vendorSaleIndex, and will have whatever item-level components you requested (Sockets, Stats, Instance data etc...) per item being sold by the vendor.",
        ),
    ] = None
    """
    The set of item detail components, one set of item components per Vendor. These are keyed by the Vendor Hash, so you will get one Item Component Set per vendor returned.
    The components contained inside are themselves keyed by the vendorSaleIndex, and will have whatever item-level components you requested (Sockets, Stats, Instance data etc...) per item being sold by the vendor.
    """

    sales: typing.Optional[DictionaryComponentResponseOfuint32AndPersonalDestinyVendorSaleItemSetComponent] = (
        pydantic.Field(default=None)
    )
    """
    Sales, keyed by the vendorItemIndex of the item being sold. These are keyed by the Vendor Hash, so you will get one Sale Item Set Component per vendor returned.
    Note that within the Sale Item Set component, the sales are themselves keyed by the vendorSaleIndex, so you can relate it to the corrent sale item definition within the Vendor's definition.
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

    vendor_groups: typing_extensions.Annotated[
        typing.Optional[SingleComponentResponseOfDestinyVendorGroupComponent],
        FieldMetadata(alias="vendorGroups"),
        pydantic.Field(
            alias="vendorGroups",
            description="For Vendors being returned, this will give you the information you need to group them and order them in the same way that the Bungie Companion app performs grouping. It will automatically be returned if you request the Vendors component.\r\nCOMPONENT TYPE: Vendors",
        ),
    ] = None
    """
    For Vendors being returned, this will give you the information you need to group them and order them in the same way that the Bungie Companion app performs grouping. It will automatically be returned if you request the Vendors component.
    COMPONENT TYPE: Vendors
    """

    vendors: typing.Optional[DictionaryComponentResponseOfuint32AndDestinyVendorComponent] = pydantic.Field(
        default=None
    )
    """
    The base properties of the vendor. These are keyed by the Vendor Hash, so you will get one Vendor Component per vendor returned.
    COMPONENT TYPE: Vendors
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

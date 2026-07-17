

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .dictionary_component_response_ofuint32and_destiny_public_vendor_component import (
    DictionaryComponentResponseOfuint32AndDestinyPublicVendorComponent,
)
from .dictionary_component_response_ofuint32and_destiny_vendor_categories_component import (
    DictionaryComponentResponseOfuint32AndDestinyVendorCategoriesComponent,
)
from .dictionary_component_response_ofuint32and_public_destiny_vendor_sale_item_set_component import (
    DictionaryComponentResponseOfuint32AndPublicDestinyVendorSaleItemSetComponent,
)
from .single_component_response_of_destiny_string_variables_component import (
    SingleComponentResponseOfDestinyStringVariablesComponent,
)
from .single_component_response_of_destiny_vendor_group_component import (
    SingleComponentResponseOfDestinyVendorGroupComponent,
)


class DestinyResponsesDestinyPublicVendorsResponse(UniversalBaseModel):
    """
    A response containing all valid components for the public Vendors endpoint.
     It is a decisively smaller subset of data compared to what we can get when we know the specific user making the request.
     If you want any of the other data - item details, whether or not you can buy it, etc... you'll have to call in the context of a character. I know, sad but true.
    """

    categories: typing.Optional[DictionaryComponentResponseOfuint32AndDestinyVendorCategoriesComponent] = (
        pydantic.Field(default=None)
    )
    """
    Categories that the vendor has available, and references to the sales therein. These are keyed by the Vendor Hash, so you will get one Categories Component per vendor returned.
    COMPONENT TYPE: VendorCategories
    """

    sales: typing.Optional[DictionaryComponentResponseOfuint32AndPublicDestinyVendorSaleItemSetComponent] = (
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
            description="A set of string variable values by hash for a public vendors context.\r\nCOMPONENT TYPE: StringVariables",
        ),
    ] = None
    """
    A set of string variable values by hash for a public vendors context.
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

    vendors: typing.Optional[DictionaryComponentResponseOfuint32AndDestinyPublicVendorComponent] = pydantic.Field(
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

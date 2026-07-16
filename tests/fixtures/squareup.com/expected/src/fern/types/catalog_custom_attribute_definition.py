

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .catalog_custom_attribute_definition_number_config import CatalogCustomAttributeDefinitionNumberConfig
from .catalog_custom_attribute_definition_selection_config import CatalogCustomAttributeDefinitionSelectionConfig
from .catalog_custom_attribute_definition_string_config import CatalogCustomAttributeDefinitionStringConfig
from .source_application import SourceApplication


class CatalogCustomAttributeDefinition(UniversalBaseModel):
    """
    Contains information defining a custom attribute. Custom attributes are
    intended to store additional information about a catalog object or to associate a
    catalog object with an entity in another system. Do not use custom attributes
    to store any sensitive information (personally identifiable information, card details, etc.).
    [Read more about custom attributes](https://developer.squareup.com/docs/catalog-api/add-custom-attributes)
    """

    allowed_object_types: typing.List[str] = pydantic.Field()
    """
    The set of Catalog Object Types that this Custom Attribute may be applied to.
    Currently, only `ITEM` and `ITEM_VARIATION` are allowed. At least one type must be included.
    """

    app_visibility: typing.Optional[str] = pydantic.Field(default=None)
    """
    The visibility of a custom attribute to applications other than the application
    that created the attribute.
    """

    custom_attribute_usage_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    __Read-only.__ The number of custom attributes that reference this
    custom attribute definition. Set by the server in response to a ListCatalog
    request with `include_counts` set to `true`.  If the actual count is greater
    than 100, `custom_attribute_usage_count` will be set to `100`.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Seller-oriented description of the meaning of this Custom Attribute,
    any constraints that the seller should observe, etc. May be displayed as a tooltip in Square UIs.
    """

    key: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the desired custom attribute key that can be used to access
    the custom attribute value on catalog objects. Cannot be modified after the
    custom attribute definition has been created.
    Must be between 1 and 60 characters, and may only contain the characters `[a-zA-Z0-9_-]`.
    """

    name: str = pydantic.Field()
    """
     The name of this definition for API and seller-facing UI purposes.
    The name must be unique within the (merchant, application) pair. Required.
    May not be empty and may not exceed 255 characters. Can be modified after creation.
    """

    number_config: typing.Optional[CatalogCustomAttributeDefinitionNumberConfig] = None
    selection_config: typing.Optional[CatalogCustomAttributeDefinitionSelectionConfig] = None
    seller_visibility: typing.Optional[str] = pydantic.Field(default=None)
    """
    The visibility of a custom attribute in seller-facing UIs (including Square Point
    of Sale applications and Square Dashboard). May be modified.
    """

    source_application: typing.Optional[SourceApplication] = None
    string_config: typing.Optional[CatalogCustomAttributeDefinitionStringConfig] = None
    type: str = pydantic.Field()
    """
    The type of this custom attribute. Cannot be modified after creation.
    Required.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

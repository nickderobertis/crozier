

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .catalog_category import CatalogCategory
from .catalog_custom_attribute_definition import CatalogCustomAttributeDefinition
from .catalog_custom_attribute_value import CatalogCustomAttributeValue
from .catalog_discount import CatalogDiscount
from .catalog_image import CatalogImage
from .catalog_item_option_value import CatalogItemOptionValue
from .catalog_item_variation import CatalogItemVariation
from .catalog_measurement_unit import CatalogMeasurementUnit
from .catalog_modifier import CatalogModifier
from .catalog_pricing_rule import CatalogPricingRule
from .catalog_product_set import CatalogProductSet
from .catalog_quick_amounts_settings import CatalogQuickAmountsSettings
from .catalog_subscription_plan import CatalogSubscriptionPlan
from .catalog_tax import CatalogTax
from .catalog_time_period import CatalogTimePeriod
from .catalog_v1id import CatalogV1Id


class CatalogObject(UniversalBaseModel):
    """
    The wrapper object for the Catalog entries of a given object type.

    The type of a particular `CatalogObject` is determined by the value of the
    `type` attribute and only the corresponding data attribute can be set on the `CatalogObject` instance.
    For example, the following list shows some instances of `CatalogObject` of a given `type` and
    their corresponding data attribute that can be set:
    - For a `CatalogObject` of the `ITEM` type, set the `item_data` attribute to yield the `CatalogItem` object.
    - For a `CatalogObject` of the `ITEM_VARIATION` type, set the `item_variation_data` attribute to yield the `CatalogItemVariation` object.
    - For a `CatalogObject` of the `MODIFIER` type, set the `modifier_data` attribute to yield the `CatalogModifier` object.
    - For a `CatalogObject` of the `MODIFIER_LIST` type, set the `modifier_list_data` attribute to yield the `CatalogModifierList` object.
    - For a `CatalogObject` of the `CATEGORY` type, set the `category_data` attribute to yield the `CatalogCategory` object.
    - For a `CatalogObject` of the `DISCOUNT` type, set the `discount_data` attribute to yield the `CatalogDiscount` object.
    - For a `CatalogObject` of the `TAX` type, set the `tax_data` attribute to yield the `CatalogTax` object.
    - For a `CatalogObject` of the `IMAGE` type, set the `image_data` attribute to yield the `CatalogImageData`  object.
    - For a `CatalogObject` of the `QUICK_AMOUNTS_SETTINGS` type, set the `quick_amounts_settings_data` attribute to yield the `CatalogQuickAmountsSettings` object.
    - For a `CatalogObject` of the `PRICING_RULE` type, set the `pricing_rule_data` attribute to yield the `CatalogPricingRule` object.
    - For a `CatalogObject` of the `TIME_PERIOD` type, set the `time_period_data` attribute to yield the `CatalogTimePeriod` object.
    - For a `CatalogObject` of the `PRODUCT_SET` type, set the `product_set_data` attribute to yield the `CatalogProductSet`  object.
    - For a `CatalogObject` of the `SUBSCRIPTION_PLAN` type, set the `subscription_plan_data` attribute to yield the `CatalogSubscriptionPlan` object.


    For a more detailed discussion of the Catalog data model, please see the
    [Design a Catalog](https://developer.squareup.com/docs/catalog-api/design-a-catalog) guide.
    """

    absent_at_location_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of locations where the object is not present, even if `present_at_all_locations` is `true`.
    This can include locations that are deactivated.
    """

    catalog_v1ids: typing_extensions.Annotated[
        typing.Optional[typing.List[CatalogV1Id]],
        FieldMetadata(alias="catalog_v1_ids"),
        pydantic.Field(
            alias="catalog_v1_ids",
            description="The Connect v1 IDs for this object at each location where it is present, where they\ndiffer from the object's Connect V2 ID. The field will only be present for objects that\nhave been created or modified by legacy APIs.",
        ),
    ] = None
    """
    The Connect v1 IDs for this object at each location where it is present, where they
    differ from the object's Connect V2 ID. The field will only be present for objects that
    have been created or modified by legacy APIs.
    """

    category_data: typing.Optional[CatalogCategory] = None
    custom_attribute_definition_data: typing.Optional[CatalogCustomAttributeDefinition] = None
    custom_attribute_values: typing.Optional[typing.Dict[str, CatalogCustomAttributeValue]] = pydantic.Field(
        default=None
    )
    """
    A map (key-value pairs) of application-defined custom attribute values. The value of a key-value pair
    is a [CatalogCustomAttributeValue](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogCustomAttributeValue) object. The key is the `key` attribute
    value defined in the associated [CatalogCustomAttributeDefinition](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogCustomAttributeDefinition)
    object defined by the application making the request.
    
    If the `CatalogCustomAttributeDefinition` object is
    defined by another application, the `CatalogCustomAttributeDefinition`'s key attribute value is prefixed by
    the defining application ID. For example, if the `CatalogCustomAttributeDefinition` has a `key` attribute of
    `"cocoa_brand"` and the defining application ID is `"abcd1234"`, the key in the map is `"abcd1234:cocoa_brand"`
    if the application making the request is different from the application defining the custom attribute definition.
    Otherwise, the key used in the map is simply `"cocoa_brand"`.
    
    Application-defined custom attributes that are set at a global (location-independent) level.
    Custom attribute values are intended to store additional information about a catalog object
    or associations with an entity in another system. Do not use custom attributes
    to store any sensitive information (personally identifiable information, card details, etc.).
    """

    discount_data: typing.Optional[CatalogDiscount] = None
    id: str = pydantic.Field()
    """
    An identifier to reference this object in the catalog. When a new `CatalogObject`
    is inserted, the client should set the id to a temporary identifier starting with
    a "`#`" character. Other objects being inserted or updated within the same request
    may use this identifier to refer to the new object.
    
    When the server receives the new object, it will supply a unique identifier that
    replaces the temporary identifier for all future references.
    """

    image_data: typing.Optional[CatalogImage] = None
    image_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Identifies the `CatalogImage` attached to this `CatalogObject`.
    """

    is_deleted: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If `true`, the object has been deleted from the database. Must be `false` for new objects
    being inserted. When deleted, the `updated_at` field will equal the deletion time.
    """

    item_data: typing.Optional["CatalogItem"] = None
    item_option_data: typing.Optional["CatalogItemOption"] = None
    item_option_value_data: typing.Optional[CatalogItemOptionValue] = None
    item_variation_data: typing.Optional[CatalogItemVariation] = None
    measurement_unit_data: typing.Optional[CatalogMeasurementUnit] = None
    modifier_data: typing.Optional[CatalogModifier] = None
    modifier_list_data: typing.Optional["CatalogModifierList"] = None
    present_at_all_locations: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If `true`, this object is present at all locations (including future locations), except where specified in
    the `absent_at_location_ids` field. If `false`, this object is not present at any locations (including future locations),
    except where specified in the `present_at_location_ids` field. If not specified, defaults to `true`.
    """

    present_at_location_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of locations where the object is present, even if `present_at_all_locations` is `false`.
    This can include locations that are deactivated.
    """

    pricing_rule_data: typing.Optional[CatalogPricingRule] = None
    product_set_data: typing.Optional[CatalogProductSet] = None
    quick_amounts_settings_data: typing.Optional[CatalogQuickAmountsSettings] = None
    subscription_plan_data: typing.Optional[CatalogSubscriptionPlan] = None
    tax_data: typing.Optional[CatalogTax] = None
    time_period_data: typing.Optional[CatalogTimePeriod] = None
    type: str = pydantic.Field()
    """
    The type of this object. Each object type has expected
    properties expressed in a structured format within its corresponding `*_data` field below.
    """

    updated_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    Last modification [timestamp](https://developer.squareup.com/docs/build-basics/working-with-dates) in RFC 3339 format, e.g., `"2016-08-15T23:59:33.123Z"`
    would indicate the UTC time (denoted by `Z`) of August 15, 2016 at 23:59:33 and 123 milliseconds.
    """

    version: typing.Optional[int] = pydantic.Field(default=None)
    """
    The version of the object. When updating an object, the version supplied
    must match the version in the database, otherwise the write will be rejected as conflicting.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .catalog_item import CatalogItem
from .catalog_item_option import CatalogItemOption
from .catalog_modifier_list import CatalogModifierList

update_forward_refs(
    CatalogObject, CatalogItem=CatalogItem, CatalogItemOption=CatalogItemOption, CatalogModifierList=CatalogModifierList
)

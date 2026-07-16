

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CatalogCustomAttributeValue(UniversalBaseModel):
    """
    An instance of a custom attribute. Custom attributes can be defined and
    added to `ITEM` and `ITEM_VARIATION` type catalog objects.
    [Read more about custom attributes](https://developer.squareup.com/docs/catalog-api/add-custom-attributes).
    """

    boolean_value: typing.Optional[bool] = pydantic.Field(default=None)
    """
    A `true` or `false` value. Populated if `type` = `BOOLEAN`.
    """

    custom_attribute_definition_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    __Read-only.__ The id of the [CatalogCustomAttributeDefinition](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogCustomAttributeDefinition) this value belongs to.
    """

    key: typing.Optional[str] = pydantic.Field(default=None)
    """
    __Read-only.__ A copy of key from the associated `CatalogCustomAttributeDefinition`.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the custom attribute.
    """

    number_value: typing.Optional[str] = pydantic.Field(default=None)
    """
    Populated if `type` = `NUMBER`. Contains a string
    representation of a decimal number, using a `.` as the decimal separator.
    """

    selection_uid_values: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    One or more choices from `allowed_selections`. Populated if `type` = `SELECTION`.
    """

    string_value: typing.Optional[str] = pydantic.Field(default=None)
    """
    The string value of the custom attribute.  Populated if `type` = `STRING`.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    __Read-only.__ A copy of type from the associated `CatalogCustomAttributeDefinition`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

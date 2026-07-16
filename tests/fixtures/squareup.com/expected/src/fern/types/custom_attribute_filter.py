

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .range import Range


class CustomAttributeFilter(UniversalBaseModel):
    """
    Supported custom attribute query expressions for calling the
    [SearchCatalogItems](https://developer.squareup.com/reference/square_2021-08-18/catalog-api/search-catalog-items)
    endpoint to search for items or item variations.
    """

    bool_filter: typing.Optional[bool] = pydantic.Field(default=None)
    """
    A query expression to filter items or item variations by matching their custom attributes'
    `boolean_value` property values
    against the specified Boolean expression.
    """

    custom_attribute_definition_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A query expression to filter items or item variations by matching their custom attributes'
    `custom_attribute_definition_id`
    property value against the the specified id.
    """

    key: typing.Optional[str] = pydantic.Field(default=None)
    """
    A query expression to filter items or item variations by matching their custom attributes'
    `key` property value against
    the specified key.
    """

    number_filter: typing.Optional[Range] = None
    selection_uids_filter: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A query expression to filter items or item variations by matching  their custom attributes'
    `selection_uid_values`
    values against the specified selection uids.
    """

    string_filter: typing.Optional[str] = pydantic.Field(default=None)
    """
    A query expression to filter items or item variations by matching their custom attributes'
    `string_value`  property value
    against the specified text.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .writable_custom_field_filter_logic import WritableCustomFieldFilterLogic
from .writable_custom_field_type import WritableCustomFieldType
from .writable_custom_field_ui_visibility import WritableCustomFieldUiVisibility


class WritableCustomField(UniversalBaseModel):
    choices: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Comma-separated list of available choices (for selection fields)
    """

    content_types: typing.List[str]
    created: typing.Optional[dt.datetime] = None
    data_type: typing.Optional[str] = None
    default: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = pydantic.Field(default=None)
    """
    Default value for the field (must be a JSON value). Encapsulate strings with double quotes (e.g. "Foo").
    """

    description: typing.Optional[str] = None
    display: typing.Optional[str] = None
    filter_logic: typing.Optional[WritableCustomFieldFilterLogic] = pydantic.Field(default=None)
    """
    Loose matches any instance of a given string; exact matches the entire field.
    """

    group_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Custom fields within the same group will be displayed together
    """

    id: typing.Optional[int] = None
    label: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the field as displayed to users (if not provided, the field's name will be used)
    """

    last_updated: typing.Optional[dt.datetime] = None
    name: str = pydantic.Field()
    """
    Internal field name
    """

    object_type: typing.Optional[str] = None
    required: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If true, this field is required when creating new objects or editing an existing object.
    """

    search_weight: typing.Optional[int] = pydantic.Field(default=None)
    """
    Weighting for search. Lower values are considered more important. Fields with a search weight of zero will be ignored.
    """

    type: typing.Optional[WritableCustomFieldType] = pydantic.Field(default=None)
    """
    The type of data this custom field holds
    """

    ui_visibility: typing.Optional[WritableCustomFieldUiVisibility] = pydantic.Field(default=None)
    """
    Specifies the visibility of custom field in the UI
    """

    url: typing.Optional[str] = None
    validation_maximum: typing.Optional[int] = pydantic.Field(default=None)
    """
    Maximum allowed value (for numeric fields)
    """

    validation_minimum: typing.Optional[int] = pydantic.Field(default=None)
    """
    Minimum allowed value (for numeric fields)
    """

    validation_regex: typing.Optional[str] = pydantic.Field(default=None)
    """
    Regular expression to enforce on text field values. Use ^ and $ to force matching of entire string. For example, <code>^[A-Z]{3}$</code> will limit values to exactly three uppercase letters.
    """

    weight: typing.Optional[int] = pydantic.Field(default=None)
    """
    Fields with higher weights appear lower in a form.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

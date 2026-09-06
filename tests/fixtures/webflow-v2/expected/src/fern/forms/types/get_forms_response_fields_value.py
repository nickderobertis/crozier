

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_forms_response_fields_value_type import GetFormsResponseFieldsValueType


class GetFormsResponseFieldsValue(UniversalBaseModel):
    """
    An object containing field info for a specific fieldID.
    """

    display_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="displayName"),
        pydantic.Field(alias="displayName", description="The field name displayed on the site"),
    ] = None
    """
    The field name displayed on the site
    """

    type: typing.Optional[GetFormsResponseFieldsValueType] = pydantic.Field(default=None)
    """
    The field type
    """

    placeholder: typing.Optional[str] = pydantic.Field(default=None)
    """
    The placeholder text for the field
    """

    user_visible: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="userVisible"),
        pydantic.Field(alias="userVisible", description="Whether the field is visible to the user"),
    ] = None
    """
    Whether the field is visible to the user
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

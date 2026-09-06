

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .option_field_metadata import OptionFieldMetadata
from .option_field_type import OptionFieldType


class OptionField(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier for a Field
    """

    is_editable: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isEditable"),
        pydantic.Field(alias="isEditable", description="Define whether the field is editable"),
    ] = None
    """
    Define whether the field is editable
    """

    is_required: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isRequired"),
        pydantic.Field(alias="isRequired", description="define whether a field is required in a collection"),
    ] = None
    """
    define whether a field is required in a collection
    """

    type: OptionFieldType = pydantic.Field()
    """
    The [Option field type](/data/reference/field-types-item-values#option)
    """

    display_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="displayName"), pydantic.Field(alias="displayName", description="The name of a field")
    ]
    """
    The name of a field
    """

    help_text: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="helpText"),
        pydantic.Field(alias="helpText", description="Additional text to help anyone filling out this field"),
    ] = None
    """
    Additional text to help anyone filling out this field
    """

    metadata: OptionFieldMetadata = pydantic.Field()
    """
    The metadata for the Option field.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

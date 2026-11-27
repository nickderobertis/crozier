

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .nested_form_definition import NestedFormDefinition
from .nested_form_field_instance_providers_item import NestedFormFieldInstanceProvidersItem
from .nested_form_field_type import NestedFormFieldType


class NestedFormField(UniversalBaseModel):
    definition: typing.Optional[NestedFormDefinition] = None
    instance_providers: typing_extensions.Annotated[
        typing.Optional[typing.List[NestedFormFieldInstanceProvidersItem]],
        FieldMetadata(alias="instanceProviders"),
        pydantic.Field(
            alias="instanceProviders",
            description="Form instance declare how users can generate new instances of nested forms within a nested form field. The most obvious way to do this is just to add a new blank form; however, very often we want to describe behavior like everytime I scan a barcode, please add a new instance of this nested form with that barcode being resolved to an entity in a specific field.",
        ),
    ] = None
    """
    Form instance declare how users can generate new instances of nested forms within a nested form field. The most obvious way to do this is just to add a new blank form; however, very often we want to describe behavior like everytime I scan a barcode, please add a new instance of this nested form with that barcode being resolved to an entity in a specific field.
    """

    type: typing.Optional[NestedFormFieldType] = pydantic.Field(default=None)
    """
    The type of this form field. Type declares how this field behaves and dictates the additional properties passed along with the required properties like label and key
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

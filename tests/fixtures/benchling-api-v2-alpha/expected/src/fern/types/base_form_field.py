

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .entity_link_form_field_entity_type import EntityLinkFormFieldEntityType
from .free_form_text_form_field_canned_responses import FreeFormTextFormFieldCannedResponses
from .free_form_text_form_field_default_keyboard import FreeFormTextFormFieldDefaultKeyboard
from .nested_form_definition import NestedFormDefinition
from .nested_form_field_instance_providers_item import NestedFormFieldInstanceProvidersItem
from .string_select_form_field_form_factor import StringSelectFormFieldFormFactor
from .string_select_form_field_option import StringSelectFormFieldOption


class Base(UniversalBaseModel):
    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Description of the purpose of this field
    """

    is_required: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isRequired"),
        pydantic.Field(
            alias="isRequired",
            description="Whether this field is required to be filled out in order to be a valid submission",
        ),
    ] = None
    """
    Whether this field is required to be filled out in order to be a valid submission
    """

    key: typing.Optional[str] = pydantic.Field(default=None)
    """
    Reference key of this form field. Used to fix identity of fields beyond the label
    """

    label: typing.Optional[str] = pydantic.Field(default=None)
    """
    End user facing name of this form field. What you see when you fill out the form each time
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class BaseFormField_Barcode(Base):
    type: typing.Literal["BARCODE"] = "BARCODE"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class BaseFormField_DateSelection(Base):
    type: typing.Literal["DATE_SELECTION"] = "DATE_SELECTION"
    days_allowed_in_future: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="daysAllowedInFuture"), pydantic.Field(alias="daysAllowedInFuture")
    ] = None
    default_today: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="defaultToday"), pydantic.Field(alias="defaultToday")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class BaseFormField_EntityLink(Base):
    type: typing.Literal["ENTITY_LINK"] = "ENTITY_LINK"
    entity_type: typing_extensions.Annotated[
        typing.Optional[EntityLinkFormFieldEntityType],
        FieldMetadata(alias="entityType"),
        pydantic.Field(alias="entityType"),
    ] = None
    schema_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="schemaId"), pydantic.Field(alias="schemaId")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class BaseFormField_Form(Base):
    type: typing.Literal["FORM"] = "FORM"
    definition: typing.Optional[NestedFormDefinition] = None
    instance_providers: typing_extensions.Annotated[
        typing.Optional[typing.List[NestedFormFieldInstanceProvidersItem]],
        FieldMetadata(alias="instanceProviders"),
        pydantic.Field(alias="instanceProviders"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class BaseFormField_FreeFormText(Base):
    type: typing.Literal["FREE_FORM_TEXT"] = "FREE_FORM_TEXT"
    canned_responses: typing_extensions.Annotated[
        typing.Optional[FreeFormTextFormFieldCannedResponses],
        FieldMetadata(alias="cannedResponses"),
        pydantic.Field(alias="cannedResponses"),
    ] = None
    default_keyboard: typing_extensions.Annotated[
        typing.Optional[FreeFormTextFormFieldDefaultKeyboard],
        FieldMetadata(alias="defaultKeyboard"),
        pydantic.Field(alias="defaultKeyboard"),
    ] = None
    number_of_lines: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="numberOfLines"), pydantic.Field(alias="numberOfLines")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class BaseFormField_StringSelection(Base):
    type: typing.Literal["STRING_SELECTION"] = "STRING_SELECTION"
    form_factor: typing_extensions.Annotated[
        typing.Optional[StringSelectFormFieldFormFactor],
        FieldMetadata(alias="formFactor"),
        pydantic.Field(alias="formFactor"),
    ] = None
    max_selections: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="maxSelections"), pydantic.Field(alias="maxSelections")
    ] = None
    options: typing.Optional[typing.List[StringSelectFormFieldOption]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


BaseFormField = typing_extensions.Annotated[
    typing.Union[
        BaseFormField_Barcode,
        BaseFormField_DateSelection,
        BaseFormField_EntityLink,
        BaseFormField_Form,
        BaseFormField_FreeFormText,
        BaseFormField_StringSelection,
    ],
    pydantic.Field(discriminator="type"),
]

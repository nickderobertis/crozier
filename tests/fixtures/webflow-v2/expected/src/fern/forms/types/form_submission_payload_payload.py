

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .form_submission_payload_payload_schema_item import FormSubmissionPayloadPayloadSchemaItem


class FormSubmissionPayloadPayload(UniversalBaseModel):
    """
    The payload of data sent from Webflow
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the form
    """

    site_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="siteId"),
        pydantic.Field(alias="siteId", description="The ID of the site that the form was submitted from"),
    ] = None
    """
    The ID of the site that the form was submitted from
    """

    data: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    The data submitted in the form
    """

    schema_: typing_extensions.Annotated[
        typing.Optional[typing.List[FormSubmissionPayloadPayloadSchemaItem]],
        FieldMetadata(alias="schema"),
        pydantic.Field(alias="schema", description="A list of fields from the submitted form"),
    ] = None
    """
    A list of fields from the submitted form
    """

    submitted_at: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="submittedAt"),
        pydantic.Field(alias="submittedAt", description="The timestamp the form was submitted"),
    ] = None
    """
    The timestamp the form was submitted
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    the ID of the event
    """

    form_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="formId"),
        pydantic.Field(alias="formId", description="The ID of the form submission"),
    ] = None
    """
    The ID of the form submission
    """

    form_element_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="formElementId"),
        pydantic.Field(alias="formElementId", description="The uniqueID of the Form element"),
    ] = None
    """
    The uniqueID of the Form element
    """

    locale_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="localeId"),
        pydantic.Field(
            alias="localeId",
            description="The ID of the locale the form was submitted from. `null` for primary-locale submissions or sites without localization.",
        ),
    ] = None
    """
    The ID of the locale the form was submitted from. `null` for primary-locale submissions or sites without localization.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

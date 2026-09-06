

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class UpdateSubmissionFormsResponse(UniversalBaseModel):
    """
    A form submission
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique ID of the Form submission
    """

    display_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="displayName"),
        pydantic.Field(alias="displayName", description="The Form name displayed on the site"),
    ] = None
    """
    The Form name displayed on the site
    """

    site_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="siteId"),
        pydantic.Field(alias="siteId", description="The unique ID of the Site the Form belongs to"),
    ] = None
    """
    The unique ID of the Site the Form belongs to
    """

    workspace_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="workspaceId"),
        pydantic.Field(alias="workspaceId", description="The unique ID of the Workspace the Site belongs to"),
    ] = None
    """
    The unique ID of the Workspace the Site belongs to
    """

    date_submitted: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="dateSubmitted"),
        pydantic.Field(alias="dateSubmitted", description="Date that the Form was submitted on"),
    ] = None
    """
    Date that the Form was submitted on
    """

    form_response: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="formResponse"),
        pydantic.Field(alias="formResponse", description="The data submitted in the Form"),
    ] = None
    """
    The data submitted in the Form
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

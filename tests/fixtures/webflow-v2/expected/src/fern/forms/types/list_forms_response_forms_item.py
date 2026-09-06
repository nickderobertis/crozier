

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .list_forms_response_forms_item_fields_value import ListFormsResponseFormsItemFieldsValue
from .list_forms_response_forms_item_response_settings import ListFormsResponseFormsItemResponseSettings


class ListFormsResponseFormsItem(UniversalBaseModel):
    """
    A Webflow form
    """

    display_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="displayName"),
        pydantic.Field(alias="displayName", description="The Form name displayed on the site"),
    ] = None
    """
    The Form name displayed on the site
    """

    created_on: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="createdOn"),
        pydantic.Field(alias="createdOn", description="Date that the Form was created on"),
    ] = None
    """
    Date that the Form was created on
    """

    last_updated: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="lastUpdated"),
        pydantic.Field(alias="lastUpdated", description="Date that the Form was last updated on"),
    ] = None
    """
    Date that the Form was last updated on
    """

    fields: typing.Optional[typing.Dict[str, ListFormsResponseFormsItemFieldsValue]] = pydantic.Field(default=None)
    """
    A collection of form field objects
    """

    response_settings: typing_extensions.Annotated[
        typing.Optional[ListFormsResponseFormsItemResponseSettings],
        FieldMetadata(alias="responseSettings"),
        pydantic.Field(alias="responseSettings", description="Settings for form responses"),
    ] = None
    """
    Settings for form responses
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique ID for the Form
    """

    site_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="siteId"),
        pydantic.Field(alias="siteId", description="The unique ID of the Site the Form belongs to"),
    ] = None
    """
    The unique ID of the Site the Form belongs to
    """

    site_domain_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="siteDomainId"),
        pydantic.Field(alias="siteDomainId", description="The unique ID corresponding to the site's Domain name"),
    ] = None
    """
    The unique ID corresponding to the site's Domain name
    """

    page_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pageId"),
        pydantic.Field(alias="pageId", description="The unique ID for the Page on which the Form is placed"),
    ] = None
    """
    The unique ID for the Page on which the Form is placed
    """

    page_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pageName"),
        pydantic.Field(alias="pageName", description="The user-visible name of the Page where the Form is placed"),
    ] = None
    """
    The user-visible name of the Page where the Form is placed
    """

    form_element_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="formElementId"),
        pydantic.Field(alias="formElementId", description="The unique ID of the Form element"),
    ] = None
    """
    The unique ID of the Form element
    """

    workspace_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="workspaceId"),
        pydantic.Field(alias="workspaceId", description="The unique ID of the Workspace the Site belongs to"),
    ] = None
    """
    The unique ID of the Workspace the Site belongs to
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

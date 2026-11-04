

import datetime as dt
import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nodes_draft_registrations_partial_update_request_attributes_node_license import (
    NodesDraftRegistrationsPartialUpdateRequestAttributesNodeLicense,
)


class NodesDraftRegistrationsPartialUpdateRequestAttributes(UniversalBaseModel):
    """
    The properties of the Draft Registration entity.
    """

    category: typing.Optional[str] = pydantic.Field(default=None)
    """
    The category of the Draft Registration.
    """

    current_user_permissions: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The current users permission level for the Draft Registration.
    """

    datetime_initiated: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The time at which the draft registration was first initiated, as an iso8601 formatted timestamp.
    """

    datetime_updated: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The time at which the draft registration was last updated, as an iso8601 formatted timestamp.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the Draft Registration.
    """

    has_project: typing.Optional[bool] = pydantic.Field(default=None)
    """
    This indicates whether a Draft Registration was branched from a project.
    """

    node_license: typing.Optional[NodesDraftRegistrationsPartialUpdateRequestAttributesNodeLicense] = None
    registration_metadata: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    This is a legacy format for `registration_responses`.
    """

    registration_responses: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    A dictionary of question IDs and responses from the registration schema.
    """

    tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The searchable tags of the Draft Registration.
    """

    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    The title of the Draft Registration.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

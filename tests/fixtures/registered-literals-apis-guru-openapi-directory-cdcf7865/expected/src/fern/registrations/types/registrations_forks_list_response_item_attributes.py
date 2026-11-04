

import datetime as dt
import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .registrations_forks_list_response_item_attributes_category import (
    RegistrationsForksListResponseItemAttributesCategory,
)


class RegistrationsForksListResponseItemAttributes(UniversalBaseModel):
    """
    The properties of the registration entity.
    """

    category: typing.Optional[RegistrationsForksListResponseItemAttributesCategory] = pydantic.Field(default=None)
    """
    The category of the registered node.
    """

    collection: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether or not this registration represents a collection. This value should always be `false`. This field may be deprecated in future versions.
    """

    current_user_can_comment: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether or not the current user has permission to post comments on this registration. Comments on registrations can be set to allow all users to comment or restricted to only contributors.
    """

    current_user_permissions: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of strings representing the permissions for the current user on this registration. Valid permissions are "admin", "read", and "write".
    """

    date_created: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The time at which the registered node was created, as an iso8601 formatted timestamp.
    """

    date_modified: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The time at which the registered node was last modified, as an iso8601 formatted timestamp.
    """

    date_registered: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The time at which this registration was created, as an iso8601 formatted timestamp.
    """

    date_withdrawn: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The time at which this registration was withdrawn, as an iso8601 formatted timestamp.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the registered node.
    """

    embargo_end_date: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The time at which the embargo on this registration will be lifted and the registration will become public, as an iso8601 formatted timestamp.
    """

    fork: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether or not this registration represents a fork of another node.
    """

    node_license: typing.Optional[str] = pydantic.Field(default=None)
    """
    A dictionary containing the metadata (copyright year and holder) associated with the registered node license (required for certain license types).
    """

    pending_embargo_approval: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether or not the embargo associated with this registration is pending approval from project administrators.
    """

    pending_registration_approval: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether or not the registration is pending approval from project administrators.
    """

    pending_withdrawal: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether or not the registration is pending approval for withdrawal from project administrators.
    """

    preprint: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether or not a preprint has been created from this node, or if this node was created for a preprint.
    """

    public: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether or not the registration is publicly visible.
    """

    registered_meta: typing.Optional[str] = pydantic.Field(default=None)
    """
    A dictionary with supplemental registration questions and responses.
    """

    registration: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether or not this is a registration. This value should always be `true`. This field may be deprecated in future versions.
    """

    registration_supplement: typing.Optional[str] = pydantic.Field(default=None)
    """
    The title of the registration schema this registration conforms to.
    """

    tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of strings that describe the registered node.
    """

    template_from: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique ID of the node from which the registered node was templated, if the registered node was created from a template.
    """

    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    The title of the registered node.
    """

    withdrawal_justification: typing.Optional[str] = pydantic.Field(default=None)
    """
    The reasoning for why this registration was withdrawn, as entered by the administrator that initiated the withdrawal.
    """

    withdrawn: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether or not this registration has been withdrawn.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import datetime as dt
import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nodes_forks_create_request_attributes_category import NodesForksCreateRequestAttributesCategory


class NodesForksCreateRequestAttributes(UniversalBaseModel):
    """
    The properties of the node entity.
    """

    category: NodesForksCreateRequestAttributesCategory = pydantic.Field()
    """
    The category of the node, as selected by project contributors.
    """

    collection: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether or not this node represents a collection. This value should always be `false`. This field may be deprecated in future versions.
    """

    current_user_can_comment: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether or not the current user has permission to post comments on this node. Comments on nodes can be set to allow all users to comment (if public) or restricted to only allow comments from contributors.
    """

    current_user_permissions: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of strings representing the permissions for the current user on this node. Valid permissions are "admin", "read", and "write".
    """

    date_created: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The time at which the node was created, as an iso8601 formatted timestamp.
    """

    date_modified: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The time at which the node was last modified, as an iso8601 formatted timestamp.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the node.
    """

    fork: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether or not this node represents a fork of another node.
    """

    forked_date: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    If this node is a fork of another node, the time at which the node was created, as an iso8601 formatted timestamp.
    """

    node_license: typing.Optional[str] = pydantic.Field(default=None)
    """
    A dictionary containing the metadata (copyright year and holder) associated with the node license (required for certain license types).
    """

    preprint: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether or not a preprint has been created from this node, or if this node was created for a preprint.
    """

    public: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether or not the node is publicly visible. This field is only editable by project administrators.
    """

    registration: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether or not the node represents a registration. This value should always be `false`. This field may be deprecated in future versions.
    """

    tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of strings that describe this node, as entered by project contributors.
    """

    template_from: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique ID of the node from which this node was templated, if this node was created from a template.
    """

    title: str = pydantic.Field()
    """
    The title of the node.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RegistrationsListResponseItemRelationships(UniversalBaseModel):
    """
    URLs to other entities or entity collections that have a relationship to the registration entity.
    """

    affiliated_institutions: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the list of institutions this registration is affiliated with.
    """

    children: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the list of the registered node's children (components).
    """

    citation: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the citation details of this registration.
    """

    comments: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the list of comments on this registration.
    """

    contributors: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the list of contributors on this registration.
    """

    files: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the list of storage providers that have been enabled on this registration.
    """

    forks: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the list of nodes that are forks of this registration.
    """

    identifiers: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the list of identifiers for this registration (i.e. ARK and DOI identifiers).
    """

    linked_nodes: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the list of nodes that are linked to this registration.
    """

    logs: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the list of log actions pertaining to this registration.
    """

    node_links: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the list of nodes that are linked to this registration. This field is deprecated as of verson 2.1; use the linked_nodes link instead.
    """

    parent: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the node that is the direct parent of the current registration, if the current registration is a child registration.
    """

    registered_by: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the user that initiated this registration.
    """

    registered_from: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the node that this registration was registered from.
    """

    registration_schema: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the metaschema that this registration conforms to.
    """

    root: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the node that is the top-level parent of the current registration. If the current registration is the top-level node, the root is the current registration.
    """

    view_only_links: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the list of view only links that have been created for this registration.
    """

    wikis: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the list of wiki pages for this registration.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

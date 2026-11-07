

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class InstitutionsNodeListResponseItemRelationships(UniversalBaseModel):
    """
    URLs to other entities or entity collections that have a relationship to the node entity.
    """

    affiliated_institutions: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the list of institutions this node is affiliated with.
    """

    children: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the list of this node's children (components).
    """

    citation: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the citation details of this node.
    """

    comments: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the list of comments on this node.
    """

    contributors: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the list of contributors on this node.
    """

    draft_registrations: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the list of registrations that have been initiated from this node and are still in a draft state.
    """

    files: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the list of storage providers that have been enabled on this node.
    """

    forked_from: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the node which this node was forked from, if this node is a fork.
    """

    forks: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the list of nodes that are forks of this node.
    """

    identifiers: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the list of identifiers for this node (i.e. ARK and DOI identifiers).
    """

    license: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the license that has been applied to this node.
    """

    linked_nodes: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the list of nodes that are linked to the current node.
    """

    logs: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the list of log actions pertaining to this node.
    """

    node_links: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the list of nodes that are linked to the current node. This field is deprecated as of verson 2.1; use the linked_nodes link instead.
    """

    parent: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the node that is the direct parent of the current node, if the current node is a child node.
    """

    preprints: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the list of preprints that this node relates to.
    """

    registrations: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the list of registrations that have been created from this node.
    """

    root: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the node that is the top-level parent of the current node. If the current node is the top-level node, the root is the current node.
    """

    template_node: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the node that the current node was templated from, if the current node was created from a template.
    """

    view_only_links: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the list of view only links that have been created for this node.
    """

    wikis: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the list of wiki pages for this node.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

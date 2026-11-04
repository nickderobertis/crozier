

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class NodesLogsListResponseItemAttributesParams(UniversalBaseModel):
    """
    The type of action performed on the OSF. See description for full list of possible actions.
    """

    addon: typing.Optional[str] = pydantic.Field(default=None)
    """
    The addon associated with the connected node.
    """

    anonymous_link: typing.Optional[bool] = pydantic.Field(default=None)
    """
    The view only link added to the node was anonymous.
    """

    bucket: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Amazon s3 bucket connected to the connected node.
    """

    citation_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of citation associated with the connected node.
    """

    contributors: typing.Optional[str] = pydantic.Field(default=None)
    """
    List of contributors on the connected node involved in the action represented by this node log.
    """

    data_set: typing.Optional[str] = pydantic.Field(default=None)
    """
    The dataset associated with the connected node.
    """

    destination: typing.Optional[str] = pydantic.Field(default=None)
    """
    A dictionary with information about the destination for the move of the item on the node associated with this log. Details include the path, url, addon, node_url and node_title.
    """

    figshare_title: typing.Optional[str] = pydantic.Field(default=None)
    """
    Title of the fighshare project associated with this node log
    """

    file: typing.Optional[str] = pydantic.Field(default=None)
    """
    Dictionary with information about the file involved with the log.
    """

    filename: typing.Optional[str] = pydantic.Field(default=None)
    """
    Filename for the file associated with the log.
    """

    folder: typing.Optional[str] = pydantic.Field(default=None)
    """
    Folder associated with the log.
    """

    folder_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the folder associated with the log.
    """

    forward_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL that the connected node forwards to.
    """

    github_repo: typing.Optional[str] = pydantic.Field(default=None)
    """
    The github repository involved with the action represented by this node log.
    """

    github_user: typing.Optional[str] = pydantic.Field(default=None)
    """
    The github user involved with the action represented by this node log.
    """

    identifiers: typing.Optional[str] = pydantic.Field(default=None)
    """
    Dictionary containing the DOI and ARK ID for a preprint associated with the log.
    """

    institution: typing.Optional[str] = pydantic.Field(default=None)
    """
    Dictionary containing the ID and Name of the institution associated with the log.
    """

    kind: typing.Optional[str] = pydantic.Field(default=None)
    """
    Kind of the object associated with the log.
    """

    license: typing.Optional[str] = pydantic.Field(default=None)
    """
    License for the associated node.
    """

    old_page: typing.Optional[str] = pydantic.Field(default=None)
    """
    Old name of wiki page for a wiki rename log action.
    """

    page: typing.Optional[str] = pydantic.Field(default=None)
    """
    Current name of wiki page for rename log action.
    """

    page_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Primary key of the wiki page associated with the log.
    """

    params_node: typing.Optional[str] = pydantic.Field(default=None)
    """
    Node that is refered to in the params of the log.
    """

    params_project: typing.Optional[str] = pydantic.Field(default=None)
    """
    Project that is refered to in the params of the log.
    """

    path: typing.Optional[str] = pydantic.Field(default=None)
    """
    Path for a file associated with the log.
    """

    pointer: typing.Optional[str] = pydantic.Field(default=None)
    """
    A dictionary with information about the node that is linked to the associated node.
    """

    preprint: typing.Optional[str] = pydantic.Field(default=None)
    """
    Preprint related to the associated node.
    """

    preprint_provider: typing.Optional[str] = pydantic.Field(default=None)
    """
    Preprint provider for the associated node.
    """

    previous_institution: typing.Optional[str] = pydantic.Field(default=None)
    """
    If a primary institution for the associated node is changed, this will show the previous institution.
    """

    source: typing.Optional[str] = pydantic.Field(default=None)
    """
    A dictionary with information about the source of a move related event for a log. Details include the path, url, addon, node_url and node_title.
    """

    study: typing.Optional[str] = pydantic.Field(default=None)
    """
    Dataverse study linked to the associated node.
    """

    tag: typing.Optional[str] = pydantic.Field(default=None)
    """
    Tag associated with the associated node.
    """

    tags: typing.Optional[str] = pydantic.Field(default=None)
    """
    Tags associated with the associated node.
    """

    target: typing.Optional[str] = pydantic.Field(default=None)
    """
    A dictionary containing details about the target of the log. Details include the path, url, addon, node_url and node_title.
    """

    template_node: typing.Optional[str] = pydantic.Field(default=None)
    """
    A dictionary containing information about the node that was used as a template for the associated node.
    """

    title_new: typing.Optional[str] = pydantic.Field(default=None)
    """
    The new title for the associated node.
    """

    title_original: typing.Optional[str] = pydantic.Field(default=None)
    """
    The original title for the associated node
    """

    updated_fields: typing.Optional[str] = pydantic.Field(default=None)
    """
    A dictionary containing all of the fields updated on the associated node.
    """

    urls: typing.Optional[str] = pydantic.Field(default=None)
    """
    Links to access information about the file associated with this log.
    """

    version: typing.Optional[str] = pydantic.Field(default=None)
    """
    Version of the wiki page associated with this log.
    """

    wiki: typing.Optional[str] = pydantic.Field(default=None)
    """
    A dictionary with information about the wiki page associated with the log.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

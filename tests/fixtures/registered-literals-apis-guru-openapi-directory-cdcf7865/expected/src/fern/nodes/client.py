

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawNodesClient, RawNodesClient
from .types.nodes_addon_read_response import NodesAddonReadResponse
from .types.nodes_addons_folders_list_response_item import NodesAddonsFoldersListResponseItem
from .types.nodes_addons_list_response_item import NodesAddonsListResponseItem
from .types.nodes_children_create_request_attributes import NodesChildrenCreateRequestAttributes
from .types.nodes_children_create_request_relationships import NodesChildrenCreateRequestRelationships
from .types.nodes_children_list_response_item import NodesChildrenListResponseItem
from .types.nodes_citation_list_response import NodesCitationListResponse
from .types.nodes_citation_read_response import NodesCitationReadResponse
from .types.nodes_comment_create_request_attributes import NodesCommentCreateRequestAttributes
from .types.nodes_comment_create_request_relationships import NodesCommentCreateRequestRelationships
from .types.nodes_comments_list_response_item import NodesCommentsListResponseItem
from .types.nodes_contributors_create_request_attributes import NodesContributorsCreateRequestAttributes
from .types.nodes_contributors_create_request_relationships import NodesContributorsCreateRequestRelationships
from .types.nodes_contributors_list_response_item import NodesContributorsListResponseItem
from .types.nodes_contributors_partial_update_request_attributes import NodesContributorsPartialUpdateRequestAttributes
from .types.nodes_contributors_partial_update_request_relationships import (
    NodesContributorsPartialUpdateRequestRelationships,
)
from .types.nodes_contributors_read_response_item import NodesContributorsReadResponseItem
from .types.nodes_create_request_attributes import NodesCreateRequestAttributes
from .types.nodes_create_request_relationships import NodesCreateRequestRelationships
from .types.nodes_draft_registrations_create_request_attributes import NodesDraftRegistrationsCreateRequestAttributes
from .types.nodes_draft_registrations_list_response_item import NodesDraftRegistrationsListResponseItem
from .types.nodes_draft_registrations_partial_update_request_attributes import (
    NodesDraftRegistrationsPartialUpdateRequestAttributes,
)
from .types.nodes_files_list_response_item import NodesFilesListResponseItem
from .types.nodes_files_read_response import NodesFilesReadResponse
from .types.nodes_forks_create_request_attributes import NodesForksCreateRequestAttributes
from .types.nodes_forks_create_request_relationships import NodesForksCreateRequestRelationships
from .types.nodes_forks_list_response_item import NodesForksListResponseItem
from .types.nodes_identifiers_list_response_item import NodesIdentifiersListResponseItem
from .types.nodes_institutions_list_response_item import NodesInstitutionsListResponseItem
from .types.nodes_linked_nodes_list_response_item import NodesLinkedNodesListResponseItem
from .types.nodes_list_response_item import NodesListResponseItem
from .types.nodes_logs_list_response_item import NodesLogsListResponseItem
from .types.nodes_preprints_list_response_item import NodesPreprintsListResponseItem
from .types.nodes_providers_list_response_item import NodesProvidersListResponseItem
from .types.nodes_providers_read_response import NodesProvidersReadResponse
from .types.nodes_read_response import NodesReadResponse
from .types.nodes_registrations_list_response_item import NodesRegistrationsListResponseItem
from .types.nodes_view_only_links_list_response_item import NodesViewOnlyLinksListResponseItem
from .types.nodes_view_only_links_read_response import NodesViewOnlyLinksReadResponse
from .types.nodes_wikis_list_response_item import NodesWikisListResponseItem


OMIT = typing.cast(typing.Any, ...)


class NodesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawNodesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawNodesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawNodesClient
        """
        return self._raw_client

    def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[NodesListResponseItem]:
        """

        A paginated list of nodes, representing projects and components, on the OSF.

        The returned nodes are those which are public or which the user has access to view.

        The returned nodes are sorted by their `date_modified`, with the most recently updated nodes appearing first.

        Registrations cannot be accessed through this endpoint (use the [registrations](#tag/Registrations) endpoints instead).
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of 10 nodes. Each resource in the array is a separate node object and contains the full representation of the node, meaning additional requests to a node's detail view are not necessary.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        This request should never return an error.
        #### Filtering
        You can optionally request that the response only include nodes that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/nodes/?filter[title]=reproducibility.

        Nodes may be filtered by their `id`, `title`, `category`, `description`, `public`, `tags`, `date_created`, `date_modified`, `root`, `parent`, `preprint`, and `contributors`.

        Most fields are string fields and will be filtered using simple substring matching. Public and preprint are boolean fields, and can be filtered using truthy values, such as **true**, **false**, **0** or **1**. Note that quoting true or false in the query will cause the match to fail.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NodesListResponseItem]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.nodes.list()
        """
        _response = self._raw_client.list(request_options=request_options)
        return _response.data

    def create(
        self,
        *,
        attributes: NodesCreateRequestAttributes,
        type: str,
        relationships: typing.Optional[NodesCreateRequestRelationships] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Creates a new node.

        On the OSF, nodes are considered **projects** or **components**. The difference between a project and a component is that a project is a top-level node, and a component is a child of a project.

        Additionally, nodes have a `category` field that includes **project** as an option. The categorization determines what icon is displayed with the node on the OSF, and helps with search organization. Projects (top-level nodes) may have a category other than project, and components (children) may have a category of **project**.
        #### Required
        Required fields for creating a node include:

        &nbsp;&nbsp;&nbsp;&nbsp`title`

        &nbsp;&nbsp;&nbsp;&nbsp`category`

        Note: Nodes default to **private** unless the `public` field is explicitly set to **true** in the request payload.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the created node, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        attributes : NodesCreateRequestAttributes
            The properties of the node entity.

        type : str
            The type identifier of the node entity (`nodes`).

        relationships : typing.Optional[NodesCreateRequestRelationships]
            URLs to other entities or entity collections that have a relationship to the node entity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.nodes import (
            NodesCreateRequestAttributes,
            NodesCreateRequestAttributesCategory,
        )

        from fern import FernApi

        client = FernApi()
        client.nodes.create(
            attributes=NodesCreateRequestAttributes(
                category=NodesCreateRequestAttributesCategory.ANALYSIS,
                title="title",
            ),
            type="type",
        )
        """
        _response = self._raw_client.create(
            attributes=attributes, type=type, relationships=relationships, request_options=request_options
        )
        return _response.data

    def read(self, node_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> NodesReadResponse:
        """
        Retrieves the details of a given node (project or component).
        #### Permissions
        Only project contributors may retrieve the details of a private node. Attempting to retreive a private node for which you are not a contributor will result in a **403 Forbidden** response.

        Authentication is not required to view the details of a public node, as public nodes give read-only access to everyone.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested node, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NodesReadResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.nodes.read(
            node_id="node_id",
        )
        """
        _response = self._raw_client.read(node_id, request_options=request_options)
        return _response.data

    def delete(self, node_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """

        Permanently deletes a node. This action cannot be undone.
        #### Permissions
        Only project administrators may delete a node. Attempting to delete a node for which you are not an administrator will result in a **403 Forbidden** response.
        #### Returns
        If the request is successful, no content is returned.

        If the request is unsuccessful, a JSON object with an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.nodes.delete(
            node_id="node_id",
        )
        """
        _response = self._raw_client.delete(node_id, request_options=request_options)
        return _response.data

    def partial_update(
        self,
        node_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates a node by setting the values of the attributes specified in the request body. Any unspecified attributes will be left unchanged.

        Nodes can be updated with either a **PUT** or **PATCH** request. The `title` and `category` fields are mandatory in a **PUT** request, and optional in a **PATCH**.
        #### Permissions
        Only write contributors may update a node. Attempting to update a node for which you do not have write access will result in a **403 Forbidden** response.
        #### Returns
        Returns a JSON object with a `data` key containing the new representation of the updated node, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.nodes.partial_update(
            node_id="node_id",
            request={
                "data": {
                    "attributes": {
                        "description": "An updated abstract.",
                        "public": True,
                        "tags": ["cancer biology", "reproducibility"],
                    },
                    "id": "{node_id}",
                    "type": "nodes",
                }
            },
        )
        """
        _response = self._raw_client.partial_update(node_id, request=request, request_options=request_options)
        return _response.data

    def addons_list(
        self, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NodesAddonsListResponseItem]:
        """

        A paginated list of addons connected to the given node or project.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of at most 10 addon objects. Each resource in the array is a separate addon object and contains the full representation of the addon, meaning additional requests to a addon's detail view are not necessary.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NodesAddonsListResponseItem]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.nodes.addons_list(
            node_id="node_id",
        )
        """
        _response = self._raw_client.addons_list(node_id, request_options=request_options)
        return _response.data

    def addon_read(
        self, node_id: str, provider: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NodesAddonReadResponse:
        """
        Retrieve details of an individual addon connected to this node.
        #### Permissions
        NodeSettings that are attached to public nodes will give read-only access to everyone. Private nodes require explicit read permission. Write and admin access are the same for public and private nodes. Administrators on a parent node have implicit read permissions for all child nodes.
        Any users with write or admin access to the node are able to deauthorize an enabled addon, but only the addon authorizer is able to change the configuration (i.e. selected folder) of an already-configured NodeSettings entity.
        #### Returns
        Returns a JSON object with a `data` key containing the details of the requested addon, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        provider : str
            The unique identifier of the addon.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NodesAddonReadResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.nodes.addon_read(
            node_id="node_id",
            provider="provider",
        )
        """
        _response = self._raw_client.addon_read(node_id, provider, request_options=request_options)
        return _response.data

    def node_addon_update(
        self,
        node_id: str,
        provider: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates a node addon by setting the values of the attributes specified in the request body. Any unspecified attributes will be left unchanged.

        Node addon can be updated with either a **PUT** or **PATCH** request. The `external_account_id`, `enabled`, and `folder_id` fields are mandatory in a **PUT**, and optional in **PATCH**. Non-string values will be accepted and stringified, however we make no promises about the stringification output.

        To delete or deauthorize a node addon, issue a **PUT** with all fields set to `null` or `False`, or a **PATCH** with enabled set `False`.
        #### Permissions
        NodeSettings that are attached to public nodes will give read-only access to everyone. Private nodes require explicit read permission. Write and admin access are the same for public and private nodes. Administrators on a parent node have implicit read permissions for all child nodes.
        Any users with write or admin access to the node are able to deauthorize an enabled addon, but only the addon authorizer is able to change the configuration (i.e. selected folder) of an already-configured NodeSettings entity.

        #### Returns
        Returns a JSON object with a `data` key containing the new representation of the updated node addon, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        provider : str
            The unique identifier of the addon.

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.nodes.node_addon_update(
            node_id="node_id",
            provider="provider",
            request={
                "data": {
                    "attributes": {
                        "external_account_id": "{account_id}",
                        "folder_id": "{folder_id}",
                        "folder_path": "{folder_path}",
                        "label": "{label}",
                        "url": "{url}",
                    },
                    "id": "{provider}",
                    "type": "node_addons",
                }
            },
        )
        """
        _response = self._raw_client.node_addon_update(
            node_id, provider, request=request, request_options=request_options
        )
        return _response.data

    def addons_folders_list(
        self, node_id: str, provider: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NodesAddonsFoldersListResponseItem]:
        """

        A paginated list of folders retrieved from the associated third-party (provider) service.
        #### Permissions
        Folders are visible only to the user that authorized the addon.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of addon folder objects. Each resource in the array is a separate addon folder object and contains the full representation of the addon folder, meaning additional requests to a addon folder's detail view are not necessary.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        provider : str
            The unique identifier of the provider

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NodesAddonsFoldersListResponseItem]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.nodes.addons_folders_list(
            node_id="node_id",
            provider="provider",
        )
        """
        _response = self._raw_client.addons_folders_list(node_id, provider, request_options=request_options)
        return _response.data

    def children_list(
        self, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NodesChildrenListResponseItem]:
        """

        A paginated list of the next level child nodes for the given node. The returned nodes are sorted by their `date_modified`, with the most recently updated child nodes appearing first.

        The list will include child nodes that are public, as well as child nodes that are private, if the authenticated user has permission to view them.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of up to 10 child nodes. If the given node has zero child nodes, the `data` key will contain an empty array. Each resource in the array is a separate node object and contains the full representation of the child node, meaning additional requests to the child node's detail view are not necessary.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        This request should never return an error.
        #### Filtering
        You can optionally request that the response only include nodes that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/nodes/ezcuj/children/?filter[title]=reproducibility.

        Nodes may be filtered by their `id`, `title`, `category`, `description`, `public`, `tags`, `date_created`, `date_modified`, `root`, `parent`, `preprint`, and `contributors`.

        Most fields are string fields and will be filtered using simple substring matching. Public and preprint are boolean fields, and can be filtered using truthy values, such as **true**, **false**, **0** or **1**. Note that quoting true or false in the query will cause the match to fail.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NodesChildrenListResponseItem]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.nodes.children_list(
            node_id="node_id",
        )
        """
        _response = self._raw_client.children_list(node_id, request_options=request_options)
        return _response.data

    def children_create(
        self,
        node_id: str,
        *,
        attributes: NodesChildrenCreateRequestAttributes,
        type: str,
        relationships: typing.Optional[NodesChildrenCreateRequestRelationships] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Creates a new child node.

        Note: Creating a child node via this endpoint will function the same as creating a node via the node list endpoint, but the child node will have the given node set as its parent.
        #### Permissions
        Only write contributors may create children nodes.
        #### Required
        Required fields for creating a node include:

        &nbsp;&nbsp;&nbsp;&nbsp`title`

        &nbsp;&nbsp;&nbsp;&nbsp`category`

        Note: nodes default to **private** unless the `public` field is explicitly set to **true** in the request payload.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the created node, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        attributes : NodesChildrenCreateRequestAttributes
            The properties of the node entity.

        type : str
            The type identifier of the node entity (`nodes`).

        relationships : typing.Optional[NodesChildrenCreateRequestRelationships]
            URLs to other entities or entity collections that have a relationship to the node entity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.nodes import (
            NodesChildrenCreateRequestAttributes,
            NodesChildrenCreateRequestAttributesCategory,
        )

        from fern import FernApi

        client = FernApi()
        client.nodes.children_create(
            node_id="node_id",
            attributes=NodesChildrenCreateRequestAttributes(
                category=NodesChildrenCreateRequestAttributesCategory.ANALYSIS,
                title="title",
            ),
            type="type",
        )
        """
        _response = self._raw_client.children_create(
            node_id, attributes=attributes, type=type, relationships=relationships, request_options=request_options
        )
        return _response.data

    def citation_list(
        self, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NodesCitationListResponse:
        """
        The citation details for a node, in CSL format.
        #### Returns
        Returns a JSON object with a `data` key that contains the representation of the details necessary for the node citation.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NodesCitationListResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.nodes.citation_list(
            node_id="node_id",
        )
        """
        _response = self._raw_client.citation_list(node_id, request_options=request_options)
        return _response.data

    def citation_read(
        self, node_id: str, style_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NodesCitationReadResponse:
        """
        The citation for a node in a specific style.
        #### Returns
        Returns a JSON object with a `data` key that contains the representation of the node citation, in the requested style.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        style_id : str
            The unique identifier of the citation style.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NodesCitationReadResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.nodes.citation_read(
            node_id="node_id",
            style_id="style_id",
        )
        """
        _response = self._raw_client.citation_read(node_id, style_id, request_options=request_options)
        return _response.data

    def comments_list(
        self, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NodesCommentsListResponseItem]:
        """

        A paginated list of comments related to a given node.

        The returned comments are sorted by their creation date, with the most recent comments appearing first.
        #### Permissions
        Comments on public nodes are given read-only access to everyone.

        If the node comment-level is `private`, only contributors have permission to comment.

        If the comment-level is `public`, any logged-in OSF user can comment.

        Comments on private nodes are only visible to contributors and administrators on the parent node.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of comment objects. Each resource in the array is a separate comment object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
        #### Filtering
        You can optionally request that the response only include comments that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/nodes/ezcuj/comments/?filter[target_id]=jg7sezmdnt93

        Nodes may be filtered by their `deleted`, `target_id`, `date_created`, `date_modified`.

        Most fields are string fields and will be filtered using simple substring matching. Public and preprint are boolean fields, and can be filtered using truthy values, such as **true**, **false**, **0** or **1**. Note that quoting `true` or `false` in the query will cause the match to fail.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NodesCommentsListResponseItem]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.nodes.comments_list(
            node_id="node_id",
        )
        """
        _response = self._raw_client.comments_list(node_id, request_options=request_options)
        return _response.data

    def comment_create(
        self,
        node_id: str,
        *,
        attributes: typing.Optional[NodesCommentCreateRequestAttributes] = OMIT,
        relationships: typing.Optional[NodesCommentCreateRequestRelationships] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Create a comment on a given node overview page or a reply to a comment on that node.

        To create a comment on the node overview page, the target `type` would be "nodes" and the target `id` would be the node `id`.

        To reply to a comment on this node, the target `type` would be "comments" and the target `id` would be the `id` of the comment to reply to.
        #### Required
        A relationship object with a `data` key, containing the target (`comments` or `nodes`) type and a target `id` is required.
        In addition, the `content` attribute describing the relationship between the node and the comment is required.
        #### Returns
        Returns a JSON object with a data key containing the representation of the new comment, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node you want to comment on.

        attributes : typing.Optional[NodesCommentCreateRequestAttributes]
            The properties of the comment entity.

        relationships : typing.Optional[NodesCommentCreateRequestRelationships]
            URLs to other entities or entity collections that have a relationship to the comment entity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.nodes.comment_create(
            node_id="node_id",
        )
        """
        _response = self._raw_client.comment_create(
            node_id, attributes=attributes, relationships=relationships, request_options=request_options
        )
        return _response.data

    def contributors_list(
        self, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NodesContributorsListResponseItem]:
        """
        A paginated list of the node's contributors, sorted by their index.

        Contributors are users who can make changes to the node or, in the case of private nodes, have read access to the node.

        Contributors are categorized as either "bibliographic" or "non-bibliographic". From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed on the project overview page on the OSF, while non-bibliographic contributors are not.

        Note that if an anonymous view_only key is being used to view the list of contributors, the user relationship will not be exposed and the contributor ID will be an empty string.

        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of 10 contributors. Each resource in the array contains the full representation of the contributor, meaning additional requests to a contributor's detail view are not necessary. Additionally, the full representation of the user this contributor represents is automatically embedded within the `data` key of the response.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
        #### Filtering
        You can optionally request that the response only include contributors that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/nodes/y9jdt/contributors/?filter[bibliographic]=true.

        Contributors may be filtered by their `bibliographic` and `permission` attributes.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NodesContributorsListResponseItem]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.nodes.contributors_list(
            node_id="node_id",
        )
        """
        _response = self._raw_client.contributors_list(node_id, request_options=request_options)
        return _response.data

    def contributors_create(
        self,
        node_id: str,
        *,
        relationships: NodesContributorsCreateRequestRelationships,
        attributes: typing.Optional[NodesContributorsCreateRequestAttributes] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Adds a contributor to a node, effectively creating a relationship between the node and a user.

        Contributors are users who can make changes to the node or, in the case of private nodes, have read access to the node.

        Contributors are categorized as either "bibliographic" or "non-bibliographic" contributors. From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed on the project overview page on the OSF, while non-bibliographic contributors are not.
        #### Permissions
        Only project administrators can add contributors to a node.
        #### Required
        A relationship object with a `data` key, containing the `users` type and valid user ID is required.

        All attributes describing the relationship between the node and the user are optional.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the new contributor, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        relationships : NodesContributorsCreateRequestRelationships
            URLs to other entities or entity collections that have a relationship to the contributor entity.

        attributes : typing.Optional[NodesContributorsCreateRequestAttributes]
            The properties of the contributor entity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.nodes import NodesContributorsCreateRequestRelationships

        from fern import FernApi

        client = FernApi()
        client.nodes.contributors_create(
            node_id="node_id",
            relationships=NodesContributorsCreateRequestRelationships(
                user="user",
            ),
        )
        """
        _response = self._raw_client.contributors_create(
            node_id, relationships=relationships, attributes=attributes, request_options=request_options
        )
        return _response.data

    def contributors_read(
        self, node_id: str, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NodesContributorsReadResponseItem]:
        """
        Retrieves the details of a given contributor.

        Contributors are users who can make changes to the node or, in the case of private nodes, have read access to the node.

        Contributors are categorized as either "bibliographic" or "non-bibliographic". From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed on the project overview page on the OSF, while non-bibliographic contributors are not.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested contributor, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        user_id : str
            The unique identifier of the user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NodesContributorsReadResponseItem]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.nodes.contributors_read(
            node_id="node_id",
            user_id="user_id",
        )
        """
        _response = self._raw_client.contributors_read(node_id, user_id, request_options=request_options)
        return _response.data

    def contributors_delete(
        self, node_id: str, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Removes a contributor from a node. This request only removes the relationship between the node and the user, it does not delete the user itself.

        A node must always have at least one admin, and attempting to remove the only admin from a node will result in a **400 Bad Request** response.
        #### Permissions
        A user can remove themselves as a node contributor. Otherwise, only project administrators can remove contributors.
        #### Returns
        If the request is successful, no content is returned.

        If the request is unsuccessful, a JSON object with an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        user_id : str
            The unique identifier of the user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.nodes.contributors_delete(
            node_id="node_id",
            user_id="user_id",
        )
        """
        _response = self._raw_client.contributors_delete(node_id, user_id, request_options=request_options)
        return _response.data

    def contributors_partial_update(
        self,
        node_id: str,
        user_id: str,
        *,
        relationships: NodesContributorsPartialUpdateRequestRelationships,
        attributes: typing.Optional[NodesContributorsPartialUpdateRequestAttributes] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates a contributor by setting the values of the attributes specified in the request body. Any unspecified attributes will be left unchanged.

        Contributors can be updated with either a **PUT** or **PATCH** request. Since this endpoint has no mandatory attributes, PUT and PATCH are functionally the same.
        #### Permissions
        Only project administrators can update the contributors on a node.
        #### Returns
        Returns a JSON object with a `data` key containing the new representation of the updated contributor, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        If the given user is not already in the contributor list, a 404 Not Found error will be returned. A node must always have at least one admin, and any attempt to downgrade the permissions of a sole admin will result in a 400 Bad Request error.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        user_id : str
            The unique identifier of the user.

        relationships : NodesContributorsPartialUpdateRequestRelationships
            URLs to other entities or entity collections that have a relationship to the contributor entity.

        attributes : typing.Optional[NodesContributorsPartialUpdateRequestAttributes]
            The properties of the contributor entity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.nodes import NodesContributorsPartialUpdateRequestRelationships

        from fern import FernApi

        client = FernApi()
        client.nodes.contributors_partial_update(
            node_id="node_id",
            user_id="user_id",
            relationships=NodesContributorsPartialUpdateRequestRelationships(
                user="user",
            ),
        )
        """
        _response = self._raw_client.contributors_partial_update(
            node_id, user_id, relationships=relationships, attributes=attributes, request_options=request_options
        )
        return _response.data

    def draft_registrations_list(
        self, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NodesDraftRegistrationsListResponseItem]:
        """
        A paginated list of all of the draft registrations of a given node.

        Draft Registrations contain Registration questions that will become part of the Registration. A Registration is a frozen version of the project that can never be deleted, but can be withdrawn and have it's metadata edited.

        Your original project remains editable but will now have the draft registration linked to it.
        #### Permissions
        Only project administrators may view draft registrations.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of 10 draft registrations. Each resource in the array is a separate draft registration object and contains the full representation of the draft registration, meaning additional requests to a draft registration's detail view are not necessary.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NodesDraftRegistrationsListResponseItem]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.nodes.draft_registrations_list(
            node_id="node_id",
        )
        """
        _response = self._raw_client.draft_registrations_list(node_id, request_options=request_options)
        return _response.data

    def draft_registrations_create(
        self,
        node_id: str,
        *,
        attributes: NodesDraftRegistrationsCreateRequestAttributes,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Initiate a draft registration of the current node.
        Draft Registrations contain Registration questions that will become part of the Registration. A Registration is a frozen version of the project that can never be deleted, but can be withdrawn and have it's metadata edited.

        Your original project remains editable but will now have the draft registration linked to it.
        #### Permissions
        Only project administrators may view create registrations.
        #### Required
        Required fields for creating a draft registration include:

        &nbsp;&nbsp;&nbsp;&nbsp;`schema_id`
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the created draft registration, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        attributes : NodesDraftRegistrationsCreateRequestAttributes
            The properties of the Draft Registration entity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.nodes import NodesDraftRegistrationsCreateRequestAttributes

        from fern import FernApi

        client = FernApi()
        client.nodes.draft_registrations_create(
            node_id="node_id",
            attributes=NodesDraftRegistrationsCreateRequestAttributes(),
        )
        """
        _response = self._raw_client.draft_registrations_create(
            node_id, attributes=attributes, request_options=request_options
        )
        return _response.data

    def draft_registrations_delete(
        self, node_id: str, draft_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Permanently deletes a draft registration. A draft that has already been registered cannot be deleted.
        #### Permissions
        Only project administrators may delete draft registrations.
        #### Returns
        If the request is successful, no content is returned.

        If the request is unsuccessful, a JSON object with an `errors` key containing information about the failure will be returned. Refer to the [list of error codes]() to understand why this request may have failed.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        draft_id : str
            The unique identifier of the draft registration.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.nodes.draft_registrations_delete(
            node_id="node_id",
            draft_id="draft_id",
        )
        """
        _response = self._raw_client.draft_registrations_delete(node_id, draft_id, request_options=request_options)
        return _response.data

    def draft_registrations_partial_update(
        self,
        node_id: str,
        draft_id: str,
        *,
        attributes: NodesDraftRegistrationsPartialUpdateRequestAttributes,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates a draft registration by setting the values of the attributes specified in the request body. Any unspecified attributes will be left unchanged.

        Draft Registrations contain Registration questions that will become part of the Registration. Answer the questions in the draft registration supplement by sending update requests until you are ready to submit the draft.

        The registration supplement of a draft registration cannot be updated after the draft has been created.

        When updating a draft registration, `registration_metadata` is required. It must be a dictionary with keys as question ids in the registration form, and values as nested dictionaries matching the specific format in the [registration schema](TODO: link me pls).

        If a question is multiple-choice, the question response must exactly match one of the possible choices.
        #### Permissions
        Only project administrators may update draft registrations.
        #### Returns
        Returns a JSON object with a `data` key containing the new representation of the updated draft registration, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        draft_id : str
            The unique identifier of the draft registration.

        attributes : NodesDraftRegistrationsPartialUpdateRequestAttributes
            The properties of the Draft Registration entity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.nodes import NodesDraftRegistrationsPartialUpdateRequestAttributes

        from fern import FernApi

        client = FernApi()
        client.nodes.draft_registrations_partial_update(
            node_id="node_id",
            draft_id="draft_id",
            attributes=NodesDraftRegistrationsPartialUpdateRequestAttributes(),
        )
        """
        _response = self._raw_client.draft_registrations_partial_update(
            node_id, draft_id, attributes=attributes, request_options=request_options
        )
        return _response.data

    def providers_list(
        self, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NodesProvidersListResponseItem]:
        """
        List of all storage providers that are configured for this node

        Users of the OSF may access their data on a [number of cloud-storage services](https://api.osf.io/v2/#storage-providers) that have integrations with the OSF. We call these **providers**. By default, every node has access to the OSF-provided storage but may use as many of the supported providers as desired.


        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of files. Each resource in the array is a separate file object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        Note: In the OSF filesystem model, providers are treated as folders, but with special properties that distinguish them from regular folders. Every provider folder is considered a root folder, and may not be deleted through the regular file API.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NodesProvidersListResponseItem]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.nodes.providers_list(
            node_id="node_id",
        )
        """
        _response = self._raw_client.providers_list(node_id, request_options=request_options)
        return _response.data

    def providers_read(
        self, node_id: str, provider: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NodesProvidersReadResponse:
        """
        Retrieves the details of a storage provider enabled on this node.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested file object, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        provider : str
            The unique identifier of the storage provider.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NodesProvidersReadResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.nodes.providers_read(
            node_id="node_id",
            provider="provider",
        )
        """
        _response = self._raw_client.providers_read(node_id, provider, request_options=request_options)
        return _response.data

    def files_list(
        self, node_id: str, provider: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NodesFilesListResponseItem]:
        """
        List of all the files/folders that are attached to your project for a given storage provider.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of files. Each resource in the array is a separate file object and contains the full representation of the file.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        #### Filtering

        You can optionally request that the response only include files that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/nodes/ezcuj/files/osfstorage/?filter[kind]=file

        Node files may be filtered by `id`, `name`, `node`, `kind`, `path`, `provider`, `size`, and `last_touched`.

        ### Waterbutler API actions

        Files can be modified through the Waterbutler API routes found in `links` (`new_folder`, `move`, `upload`, `download`, and `delete`).

        #### Download (files)

        To download a file, issue a GET request against the download link. The response will have the Content-Disposition header set, which will will trigger a download in a browser.

        #### Create Subfolder (folders)

        You can create a subfolder of an existing folder by issuing a PUT request against the new_folder link. The ?kind=folder portion of the query parameter is already included in the new_folder link. The name of the new subfolder should be provided in the name query parameter. The response will contain a WaterButler folder entity. If a folder with that name already exists in the parent directory, the server will return a 409 Conflict error response.

        #### Upload New File (folders)

        To upload a file to a folder, issue a PUT request to the folder's upload link with the raw file data in the request body, and the kind and name query parameters set to 'file' and the desired name of the file. The response will contain a WaterButler file entity that describes the new file. If a file with the same name already exists in the folder, the server will return a 409 Conflict error response.

        #### Update Existing File (file)

        To update an existing file, issue a PUT request to the file's upload link with the raw file data in the request body and the kind query parameter set to "file". The update action will create a new version of the file. The response will contain a WaterButler file entity that describes the updated file.

        #### Rename (files, folders)

        To rename a file or folder, issue a POST request to the move link with the action body parameter set to "rename" and the rename body parameter set to the desired name. The response will contain either a folder entity or file entity with the new name.

        #### Move & Copy (files, folders)

        Move and copy actions both use the same request structure, a POST to the move url, but with different values for the action body parameters. The path parameter is also required and should be the OSF path attribute of the folder being written to. The rename and conflict parameters are optional. If you wish to change the name of the file or folder at its destination, set the rename parameter to the new name. The conflict param governs how name clashes are resolved. Possible values are replace and keep. replace is the default and will overwrite the file that already exists in the target folder. keep will attempt to keep both by adding a suffix to the new file's name until it no longer conflicts. The suffix will be ' (x)' where x is a increasing integer starting from 1. This behavior is intended to mimic that of the OS X Finder. The response will contain either a folder entity or file entity with the new name.
        Files and folders can also be moved between nodes and providers. The resource parameter is the id of the node under which the file/folder should be moved. It must agree with the path parameter, that is the path must identify a valid folder under the node identified by resource. Likewise, the provider parameter may be used to move the file/folder to another storage provider, but both the resource and path parameters must belong to a node and folder already extant on that provider. Both resource and provider default to the current node and providers.
        If a moved/copied file is overwriting an existing file, a 200 OK response will be returned. Otherwise, a 201 Created will be returned.

        #### Delete (file, folders)

        To delete a file or folder send a DELETE request to the delete link. Nothing will be returned in the response body.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        provider : str
            The unique identifier of the storage provider.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NodesFilesListResponseItem]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.nodes.files_list(
            node_id="node_id",
            provider="provider",
        )
        """
        _response = self._raw_client.files_list(node_id, provider, request_options=request_options)
        return _response.data

    def files_read(
        self, node_id: str, provider: str, path: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NodesFilesReadResponse:
        """
        Retrieves the details of a file attached to given node (project or component) for the given storage provider.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested file object, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        provider : str
            The unique identifier of the storage provider.

        path : str
            The unique identifier of the file path.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NodesFilesReadResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.nodes.files_read(
            node_id="node_id",
            provider="provider",
            path="path",
        )
        """
        _response = self._raw_client.files_read(node_id, provider, path, request_options=request_options)
        return _response.data

    def forks_list(
        self, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NodesForksListResponseItem]:
        """

        A paginated list of the current node's forks. The returned fork nodes are sorted by their `forked_date`, with the most recently forked nodes appearing first.

        Forking a project creates a copy of an existing node and all of its contents. The fork always points back to the original node, forming a network of nodes.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of up to 10 forked nodes. If the current node has zero forked nodes, the `data` key will contain an empty array. Each resource in the array is a separate node object and contains the full representation of the forked node, meaning additional requests to the forked node's detail view are not necessary.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        This request should never return an error.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NodesForksListResponseItem]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.nodes.forks_list(
            node_id="node_id",
        )
        """
        _response = self._raw_client.forks_list(node_id, request_options=request_options)
        return _response.data

    def forks_create(
        self,
        node_id: str,
        *,
        attributes: NodesForksCreateRequestAttributes,
        type: str,
        relationships: typing.Optional[NodesForksCreateRequestRelationships] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Creates a fork of the given node.

        Forking a project creates a copy of an existing node and all of its contents. The fork always points back to the original node, forming a network of nodes.

        You might use a fork to copy another's work to build on and extend. For example, a professor may create an OSF project of materials for individual student use. Each student forks the project to have his or her own copy of the materials to start his/her own work.

        When creating a fork, your fork will only contain public components of the current node and components for which you are a contributor. Private components that you do not have access to will not be forked.
        #### Required
        There are no required attributes when creating a fork, as all of the forked node's attributes will be copied from the current node.

        The `title` field is optional, with the default title being "Fork of " prepended to the current node's title.
        #### Returns
        Returns a JSON object with a `data` key containing the complete srepresentation of the forked node, if the request is successful.
        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        attributes : NodesForksCreateRequestAttributes
            The properties of the node entity.

        type : str
            The type identifier of the node entity (`nodes`).

        relationships : typing.Optional[NodesForksCreateRequestRelationships]
            URLs to other entities or entity collections that have a relationship to the node entity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.nodes import (
            NodesForksCreateRequestAttributes,
            NodesForksCreateRequestAttributesCategory,
        )

        from fern import FernApi

        client = FernApi()
        client.nodes.forks_create(
            node_id="node_id",
            attributes=NodesForksCreateRequestAttributes(
                category=NodesForksCreateRequestAttributesCategory.ANALYSIS,
                title="title",
            ),
            type="type",
        )
        """
        _response = self._raw_client.forks_create(
            node_id, attributes=attributes, type=type, relationships=relationships, request_options=request_options
        )
        return _response.data

    def identifiers_list(
        self, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NodesIdentifiersListResponseItem]:
        """
        List all identifiers associated with a given node.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of identifiers. Each resource in the array is a separate identifier object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
        #### Filtering

        You can optionally request that the response only include nodes that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/nodes/ezcuj/identifiers/?filter[category]=ark

        Identifiers may be filtered by their `category` e.g `ark` or `doi`.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NodesIdentifiersListResponseItem]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.nodes.identifiers_list(
            node_id="node_id",
        )
        """
        _response = self._raw_client.identifiers_list(node_id, request_options=request_options)
        return _response.data

    def institutions_list(
        self, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NodesInstitutionsListResponseItem]:
        """
        List of all institutions affiliated with this node.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of up to 10 affilited institutions. Each resource in the array is a separate institution object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NodesInstitutionsListResponseItem]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.nodes.institutions_list(
            node_id="node_id",
        )
        """
        _response = self._raw_client.institutions_list(node_id, request_options=request_options)
        return _response.data

    def linked_nodes_list(
        self, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NodesLinkedNodesListResponseItem]:
        """
        List of all nodes linked to the given node.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of up to 10 nodes. Each resource in the array is a separate node object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
        #### Filtering
        You can optionally request that the response only include nodes that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/nodes/?filter[title]=reproducibility.

        Nodes may be filtered by their `title`, `category`, `description`, `public`, `registration`, or `tags`. `title`, `description`, and `category` are string fields and will be filteres using simple substring matching. `public`, `registration` are boolean and can be filtered using truthy values, such as `true`, `false`, `0`, `1`. `tags` is an array of simple strings.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NodesLinkedNodesListResponseItem]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.nodes.linked_nodes_list(
            node_id="node_id",
        )
        """
        _response = self._raw_client.linked_nodes_list(node_id, request_options=request_options)
        return _response.data

    def logs_list(
        self, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NodesLogsListResponseItem]:
        """
        A paginated list of all logs associated with a given node.

        The returned logs are sorted by their `date`, with the most recents logs appearing first.

        This list includes the logs of the specified node as well as the logs of that node's children to which the current user has read-only access.

        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of up to 10 logs. Each resource in the array is a separate logs object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
        #### Filtering
        You can optionally request that the response only include logs that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/nodes/ezcuj/logs/?filter[action]=made_private.

        Nodes may be filtered by their `action`, and `date`.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NodesLogsListResponseItem]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.nodes.logs_list(
            node_id="node_id",
        )
        """
        _response = self._raw_client.logs_list(node_id, request_options=request_options)
        return _response.data

    def preprints_list(
        self, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NodesPreprintsListResponseItem]:
        """
        A paginated list of preprints related to a given node. The returned preprints are sorted by their creation date, with the most recent preprints appearing first.

        **Note: This API endpoint is under active development, and is subject to change in the future.**
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of up to 10 preprints. Each resource in the array is a separate preprint object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NodesPreprintsListResponseItem]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.nodes.preprints_list(
            node_id="node_id",
        )
        """
        _response = self._raw_client.preprints_list(node_id, request_options=request_options)
        return _response.data

    def registrations_list(
        self, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NodesRegistrationsListResponseItem]:
        """
        List of all registrations of the given node.
        #### Returns

        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of up to 10 registrations. Each resource in the array is a separate registrations object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
        #### Filtering

        You can optionally request that the response only include registrations that match your filters by utilizing the filter query parameter, e.g. https://api.osf.io/v2/registrations/?filter[title]=open.

        Registrations may be filtered by their `id`, `title`, `category`, `description`, `public`, `tags`, `date_created`, `date_modified`, `root`, `parent`, and `contributors`.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NodesRegistrationsListResponseItem]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.nodes.registrations_list(
            node_id="node_id",
        )
        """
        _response = self._raw_client.registrations_list(node_id, request_options=request_options)
        return _response.data

    def view_only_links_list(
        self, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NodesViewOnlyLinksListResponseItem]:
        """
        List of view only links on a node.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of up to 10 view only links. Each resource in the array is a view only link object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        #### Permissions

        View only links on a node, public or private, are readable and writeable only by users that are administrators on the node.

        #### Filtering

        You can optionally request that the response only include view only links that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/nodes/ezcuj/view_only_links/?filter[anonymous]=true.

        View Only Links may be filtered based on their `name`, `anonymous` and `date_created` fields. Possible comparison operators include 'gt' (greater than), 'gte'(greater than or equal to), 'lt' (less than) and 'lte' (less than or equal to). The date must be in the format YYYY-MM-DD and the time is optional.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NodesViewOnlyLinksListResponseItem]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.nodes.view_only_links_list(
            node_id="node_id",
        )
        """
        _response = self._raw_client.view_only_links_list(node_id, request_options=request_options)
        return _response.data

    def view_only_links_read(
        self, node_id: str, link_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NodesViewOnlyLinksReadResponse:
        """
        Retrieves the details of a view only link on a node.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested view only link, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
        #### Permissions

        View only links on a node, public or private, are readable and writeable only by users that are administrators on the node.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        link_id : str
            The unique identifier of the view only link.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NodesViewOnlyLinksReadResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.nodes.view_only_links_read(
            node_id="node_id",
            link_id="link_id",
        )
        """
        _response = self._raw_client.view_only_links_read(node_id, link_id, request_options=request_options)
        return _response.data

    def wikis_list(
        self, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NodesWikisListResponseItem]:
        """
        List of wiki pages on a node.
        #### Returns
        Paginated list of the node's current wiki page versions ordered by their date_modified. Each resource contains the full representation of the wiki, meaning additional requests to an individual wiki's detail view are not necessary.

        Note that if an anonymous view_only key is being used, the user relationship will not be exposed.

        If the request is unsuccessful, a JSON object with an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
        #### Filtering
        Wiki pages can be filtered based on their `name` and `date_modified` fields.
        + `filter[name]=<Str>` -- filter wiki pages by name
        + `filter[date_modified][comparison_operator]=YYYY-MM-DDTH:M:S` -- filter wiki pages based on date modified.

        Possible comparison operators include 'gt' (greater than), 'gte'(greater than or equal to), 'lt' (less than) and 'lte' (less than or equal to). The date must be in the format YYYY-MM-DD and the time is optional.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NodesWikisListResponseItem]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.nodes.wikis_list(
            node_id="node_id",
        )
        """
        _response = self._raw_client.wikis_list(node_id, request_options=request_options)
        return _response.data


class AsyncNodesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawNodesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawNodesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawNodesClient
        """
        return self._raw_client

    async def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NodesListResponseItem]:
        """

        A paginated list of nodes, representing projects and components, on the OSF.

        The returned nodes are those which are public or which the user has access to view.

        The returned nodes are sorted by their `date_modified`, with the most recently updated nodes appearing first.

        Registrations cannot be accessed through this endpoint (use the [registrations](#tag/Registrations) endpoints instead).
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of 10 nodes. Each resource in the array is a separate node object and contains the full representation of the node, meaning additional requests to a node's detail view are not necessary.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        This request should never return an error.
        #### Filtering
        You can optionally request that the response only include nodes that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/nodes/?filter[title]=reproducibility.

        Nodes may be filtered by their `id`, `title`, `category`, `description`, `public`, `tags`, `date_created`, `date_modified`, `root`, `parent`, `preprint`, and `contributors`.

        Most fields are string fields and will be filtered using simple substring matching. Public and preprint are boolean fields, and can be filtered using truthy values, such as **true**, **false**, **0** or **1**. Note that quoting true or false in the query will cause the match to fail.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NodesListResponseItem]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.nodes.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(request_options=request_options)
        return _response.data

    async def create(
        self,
        *,
        attributes: NodesCreateRequestAttributes,
        type: str,
        relationships: typing.Optional[NodesCreateRequestRelationships] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Creates a new node.

        On the OSF, nodes are considered **projects** or **components**. The difference between a project and a component is that a project is a top-level node, and a component is a child of a project.

        Additionally, nodes have a `category` field that includes **project** as an option. The categorization determines what icon is displayed with the node on the OSF, and helps with search organization. Projects (top-level nodes) may have a category other than project, and components (children) may have a category of **project**.
        #### Required
        Required fields for creating a node include:

        &nbsp;&nbsp;&nbsp;&nbsp`title`

        &nbsp;&nbsp;&nbsp;&nbsp`category`

        Note: Nodes default to **private** unless the `public` field is explicitly set to **true** in the request payload.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the created node, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        attributes : NodesCreateRequestAttributes
            The properties of the node entity.

        type : str
            The type identifier of the node entity (`nodes`).

        relationships : typing.Optional[NodesCreateRequestRelationships]
            URLs to other entities or entity collections that have a relationship to the node entity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.nodes import (
            NodesCreateRequestAttributes,
            NodesCreateRequestAttributesCategory,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.nodes.create(
                attributes=NodesCreateRequestAttributes(
                    category=NodesCreateRequestAttributesCategory.ANALYSIS,
                    title="title",
                ),
                type="type",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(
            attributes=attributes, type=type, relationships=relationships, request_options=request_options
        )
        return _response.data

    async def read(self, node_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> NodesReadResponse:
        """
        Retrieves the details of a given node (project or component).
        #### Permissions
        Only project contributors may retrieve the details of a private node. Attempting to retreive a private node for which you are not a contributor will result in a **403 Forbidden** response.

        Authentication is not required to view the details of a public node, as public nodes give read-only access to everyone.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested node, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NodesReadResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.nodes.read(
                node_id="node_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read(node_id, request_options=request_options)
        return _response.data

    async def delete(self, node_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """

        Permanently deletes a node. This action cannot be undone.
        #### Permissions
        Only project administrators may delete a node. Attempting to delete a node for which you are not an administrator will result in a **403 Forbidden** response.
        #### Returns
        If the request is successful, no content is returned.

        If the request is unsuccessful, a JSON object with an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.nodes.delete(
                node_id="node_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(node_id, request_options=request_options)
        return _response.data

    async def partial_update(
        self,
        node_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates a node by setting the values of the attributes specified in the request body. Any unspecified attributes will be left unchanged.

        Nodes can be updated with either a **PUT** or **PATCH** request. The `title` and `category` fields are mandatory in a **PUT** request, and optional in a **PATCH**.
        #### Permissions
        Only write contributors may update a node. Attempting to update a node for which you do not have write access will result in a **403 Forbidden** response.
        #### Returns
        Returns a JSON object with a `data` key containing the new representation of the updated node, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.nodes.partial_update(
                node_id="node_id",
                request={
                    "data": {
                        "attributes": {
                            "description": "An updated abstract.",
                            "public": True,
                            "tags": ["cancer biology", "reproducibility"],
                        },
                        "id": "{node_id}",
                        "type": "nodes",
                    }
                },
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.partial_update(node_id, request=request, request_options=request_options)
        return _response.data

    async def addons_list(
        self, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NodesAddonsListResponseItem]:
        """

        A paginated list of addons connected to the given node or project.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of at most 10 addon objects. Each resource in the array is a separate addon object and contains the full representation of the addon, meaning additional requests to a addon's detail view are not necessary.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NodesAddonsListResponseItem]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.nodes.addons_list(
                node_id="node_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.addons_list(node_id, request_options=request_options)
        return _response.data

    async def addon_read(
        self, node_id: str, provider: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NodesAddonReadResponse:
        """
        Retrieve details of an individual addon connected to this node.
        #### Permissions
        NodeSettings that are attached to public nodes will give read-only access to everyone. Private nodes require explicit read permission. Write and admin access are the same for public and private nodes. Administrators on a parent node have implicit read permissions for all child nodes.
        Any users with write or admin access to the node are able to deauthorize an enabled addon, but only the addon authorizer is able to change the configuration (i.e. selected folder) of an already-configured NodeSettings entity.
        #### Returns
        Returns a JSON object with a `data` key containing the details of the requested addon, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        provider : str
            The unique identifier of the addon.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NodesAddonReadResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.nodes.addon_read(
                node_id="node_id",
                provider="provider",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.addon_read(node_id, provider, request_options=request_options)
        return _response.data

    async def node_addon_update(
        self,
        node_id: str,
        provider: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates a node addon by setting the values of the attributes specified in the request body. Any unspecified attributes will be left unchanged.

        Node addon can be updated with either a **PUT** or **PATCH** request. The `external_account_id`, `enabled`, and `folder_id` fields are mandatory in a **PUT**, and optional in **PATCH**. Non-string values will be accepted and stringified, however we make no promises about the stringification output.

        To delete or deauthorize a node addon, issue a **PUT** with all fields set to `null` or `False`, or a **PATCH** with enabled set `False`.
        #### Permissions
        NodeSettings that are attached to public nodes will give read-only access to everyone. Private nodes require explicit read permission. Write and admin access are the same for public and private nodes. Administrators on a parent node have implicit read permissions for all child nodes.
        Any users with write or admin access to the node are able to deauthorize an enabled addon, but only the addon authorizer is able to change the configuration (i.e. selected folder) of an already-configured NodeSettings entity.

        #### Returns
        Returns a JSON object with a `data` key containing the new representation of the updated node addon, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        provider : str
            The unique identifier of the addon.

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.nodes.node_addon_update(
                node_id="node_id",
                provider="provider",
                request={
                    "data": {
                        "attributes": {
                            "external_account_id": "{account_id}",
                            "folder_id": "{folder_id}",
                            "folder_path": "{folder_path}",
                            "label": "{label}",
                            "url": "{url}",
                        },
                        "id": "{provider}",
                        "type": "node_addons",
                    }
                },
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.node_addon_update(
            node_id, provider, request=request, request_options=request_options
        )
        return _response.data

    async def addons_folders_list(
        self, node_id: str, provider: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NodesAddonsFoldersListResponseItem]:
        """

        A paginated list of folders retrieved from the associated third-party (provider) service.
        #### Permissions
        Folders are visible only to the user that authorized the addon.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of addon folder objects. Each resource in the array is a separate addon folder object and contains the full representation of the addon folder, meaning additional requests to a addon folder's detail view are not necessary.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        provider : str
            The unique identifier of the provider

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NodesAddonsFoldersListResponseItem]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.nodes.addons_folders_list(
                node_id="node_id",
                provider="provider",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.addons_folders_list(node_id, provider, request_options=request_options)
        return _response.data

    async def children_list(
        self, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NodesChildrenListResponseItem]:
        """

        A paginated list of the next level child nodes for the given node. The returned nodes are sorted by their `date_modified`, with the most recently updated child nodes appearing first.

        The list will include child nodes that are public, as well as child nodes that are private, if the authenticated user has permission to view them.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of up to 10 child nodes. If the given node has zero child nodes, the `data` key will contain an empty array. Each resource in the array is a separate node object and contains the full representation of the child node, meaning additional requests to the child node's detail view are not necessary.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        This request should never return an error.
        #### Filtering
        You can optionally request that the response only include nodes that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/nodes/ezcuj/children/?filter[title]=reproducibility.

        Nodes may be filtered by their `id`, `title`, `category`, `description`, `public`, `tags`, `date_created`, `date_modified`, `root`, `parent`, `preprint`, and `contributors`.

        Most fields are string fields and will be filtered using simple substring matching. Public and preprint are boolean fields, and can be filtered using truthy values, such as **true**, **false**, **0** or **1**. Note that quoting true or false in the query will cause the match to fail.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NodesChildrenListResponseItem]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.nodes.children_list(
                node_id="node_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.children_list(node_id, request_options=request_options)
        return _response.data

    async def children_create(
        self,
        node_id: str,
        *,
        attributes: NodesChildrenCreateRequestAttributes,
        type: str,
        relationships: typing.Optional[NodesChildrenCreateRequestRelationships] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Creates a new child node.

        Note: Creating a child node via this endpoint will function the same as creating a node via the node list endpoint, but the child node will have the given node set as its parent.
        #### Permissions
        Only write contributors may create children nodes.
        #### Required
        Required fields for creating a node include:

        &nbsp;&nbsp;&nbsp;&nbsp`title`

        &nbsp;&nbsp;&nbsp;&nbsp`category`

        Note: nodes default to **private** unless the `public` field is explicitly set to **true** in the request payload.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the created node, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        attributes : NodesChildrenCreateRequestAttributes
            The properties of the node entity.

        type : str
            The type identifier of the node entity (`nodes`).

        relationships : typing.Optional[NodesChildrenCreateRequestRelationships]
            URLs to other entities or entity collections that have a relationship to the node entity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.nodes import (
            NodesChildrenCreateRequestAttributes,
            NodesChildrenCreateRequestAttributesCategory,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.nodes.children_create(
                node_id="node_id",
                attributes=NodesChildrenCreateRequestAttributes(
                    category=NodesChildrenCreateRequestAttributesCategory.ANALYSIS,
                    title="title",
                ),
                type="type",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.children_create(
            node_id, attributes=attributes, type=type, relationships=relationships, request_options=request_options
        )
        return _response.data

    async def citation_list(
        self, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NodesCitationListResponse:
        """
        The citation details for a node, in CSL format.
        #### Returns
        Returns a JSON object with a `data` key that contains the representation of the details necessary for the node citation.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NodesCitationListResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.nodes.citation_list(
                node_id="node_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.citation_list(node_id, request_options=request_options)
        return _response.data

    async def citation_read(
        self, node_id: str, style_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NodesCitationReadResponse:
        """
        The citation for a node in a specific style.
        #### Returns
        Returns a JSON object with a `data` key that contains the representation of the node citation, in the requested style.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        style_id : str
            The unique identifier of the citation style.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NodesCitationReadResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.nodes.citation_read(
                node_id="node_id",
                style_id="style_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.citation_read(node_id, style_id, request_options=request_options)
        return _response.data

    async def comments_list(
        self, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NodesCommentsListResponseItem]:
        """

        A paginated list of comments related to a given node.

        The returned comments are sorted by their creation date, with the most recent comments appearing first.
        #### Permissions
        Comments on public nodes are given read-only access to everyone.

        If the node comment-level is `private`, only contributors have permission to comment.

        If the comment-level is `public`, any logged-in OSF user can comment.

        Comments on private nodes are only visible to contributors and administrators on the parent node.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of comment objects. Each resource in the array is a separate comment object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
        #### Filtering
        You can optionally request that the response only include comments that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/nodes/ezcuj/comments/?filter[target_id]=jg7sezmdnt93

        Nodes may be filtered by their `deleted`, `target_id`, `date_created`, `date_modified`.

        Most fields are string fields and will be filtered using simple substring matching. Public and preprint are boolean fields, and can be filtered using truthy values, such as **true**, **false**, **0** or **1**. Note that quoting `true` or `false` in the query will cause the match to fail.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NodesCommentsListResponseItem]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.nodes.comments_list(
                node_id="node_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.comments_list(node_id, request_options=request_options)
        return _response.data

    async def comment_create(
        self,
        node_id: str,
        *,
        attributes: typing.Optional[NodesCommentCreateRequestAttributes] = OMIT,
        relationships: typing.Optional[NodesCommentCreateRequestRelationships] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Create a comment on a given node overview page or a reply to a comment on that node.

        To create a comment on the node overview page, the target `type` would be "nodes" and the target `id` would be the node `id`.

        To reply to a comment on this node, the target `type` would be "comments" and the target `id` would be the `id` of the comment to reply to.
        #### Required
        A relationship object with a `data` key, containing the target (`comments` or `nodes`) type and a target `id` is required.
        In addition, the `content` attribute describing the relationship between the node and the comment is required.
        #### Returns
        Returns a JSON object with a data key containing the representation of the new comment, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node you want to comment on.

        attributes : typing.Optional[NodesCommentCreateRequestAttributes]
            The properties of the comment entity.

        relationships : typing.Optional[NodesCommentCreateRequestRelationships]
            URLs to other entities or entity collections that have a relationship to the comment entity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.nodes.comment_create(
                node_id="node_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.comment_create(
            node_id, attributes=attributes, relationships=relationships, request_options=request_options
        )
        return _response.data

    async def contributors_list(
        self, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NodesContributorsListResponseItem]:
        """
        A paginated list of the node's contributors, sorted by their index.

        Contributors are users who can make changes to the node or, in the case of private nodes, have read access to the node.

        Contributors are categorized as either "bibliographic" or "non-bibliographic". From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed on the project overview page on the OSF, while non-bibliographic contributors are not.

        Note that if an anonymous view_only key is being used to view the list of contributors, the user relationship will not be exposed and the contributor ID will be an empty string.

        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of 10 contributors. Each resource in the array contains the full representation of the contributor, meaning additional requests to a contributor's detail view are not necessary. Additionally, the full representation of the user this contributor represents is automatically embedded within the `data` key of the response.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
        #### Filtering
        You can optionally request that the response only include contributors that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/nodes/y9jdt/contributors/?filter[bibliographic]=true.

        Contributors may be filtered by their `bibliographic` and `permission` attributes.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NodesContributorsListResponseItem]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.nodes.contributors_list(
                node_id="node_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contributors_list(node_id, request_options=request_options)
        return _response.data

    async def contributors_create(
        self,
        node_id: str,
        *,
        relationships: NodesContributorsCreateRequestRelationships,
        attributes: typing.Optional[NodesContributorsCreateRequestAttributes] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Adds a contributor to a node, effectively creating a relationship between the node and a user.

        Contributors are users who can make changes to the node or, in the case of private nodes, have read access to the node.

        Contributors are categorized as either "bibliographic" or "non-bibliographic" contributors. From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed on the project overview page on the OSF, while non-bibliographic contributors are not.
        #### Permissions
        Only project administrators can add contributors to a node.
        #### Required
        A relationship object with a `data` key, containing the `users` type and valid user ID is required.

        All attributes describing the relationship between the node and the user are optional.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the new contributor, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        relationships : NodesContributorsCreateRequestRelationships
            URLs to other entities or entity collections that have a relationship to the contributor entity.

        attributes : typing.Optional[NodesContributorsCreateRequestAttributes]
            The properties of the contributor entity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.nodes import NodesContributorsCreateRequestRelationships

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.nodes.contributors_create(
                node_id="node_id",
                relationships=NodesContributorsCreateRequestRelationships(
                    user="user",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contributors_create(
            node_id, relationships=relationships, attributes=attributes, request_options=request_options
        )
        return _response.data

    async def contributors_read(
        self, node_id: str, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NodesContributorsReadResponseItem]:
        """
        Retrieves the details of a given contributor.

        Contributors are users who can make changes to the node or, in the case of private nodes, have read access to the node.

        Contributors are categorized as either "bibliographic" or "non-bibliographic". From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed on the project overview page on the OSF, while non-bibliographic contributors are not.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested contributor, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        user_id : str
            The unique identifier of the user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NodesContributorsReadResponseItem]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.nodes.contributors_read(
                node_id="node_id",
                user_id="user_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contributors_read(node_id, user_id, request_options=request_options)
        return _response.data

    async def contributors_delete(
        self, node_id: str, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Removes a contributor from a node. This request only removes the relationship between the node and the user, it does not delete the user itself.

        A node must always have at least one admin, and attempting to remove the only admin from a node will result in a **400 Bad Request** response.
        #### Permissions
        A user can remove themselves as a node contributor. Otherwise, only project administrators can remove contributors.
        #### Returns
        If the request is successful, no content is returned.

        If the request is unsuccessful, a JSON object with an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        user_id : str
            The unique identifier of the user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.nodes.contributors_delete(
                node_id="node_id",
                user_id="user_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contributors_delete(node_id, user_id, request_options=request_options)
        return _response.data

    async def contributors_partial_update(
        self,
        node_id: str,
        user_id: str,
        *,
        relationships: NodesContributorsPartialUpdateRequestRelationships,
        attributes: typing.Optional[NodesContributorsPartialUpdateRequestAttributes] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates a contributor by setting the values of the attributes specified in the request body. Any unspecified attributes will be left unchanged.

        Contributors can be updated with either a **PUT** or **PATCH** request. Since this endpoint has no mandatory attributes, PUT and PATCH are functionally the same.
        #### Permissions
        Only project administrators can update the contributors on a node.
        #### Returns
        Returns a JSON object with a `data` key containing the new representation of the updated contributor, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        If the given user is not already in the contributor list, a 404 Not Found error will be returned. A node must always have at least one admin, and any attempt to downgrade the permissions of a sole admin will result in a 400 Bad Request error.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        user_id : str
            The unique identifier of the user.

        relationships : NodesContributorsPartialUpdateRequestRelationships
            URLs to other entities or entity collections that have a relationship to the contributor entity.

        attributes : typing.Optional[NodesContributorsPartialUpdateRequestAttributes]
            The properties of the contributor entity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.nodes import NodesContributorsPartialUpdateRequestRelationships

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.nodes.contributors_partial_update(
                node_id="node_id",
                user_id="user_id",
                relationships=NodesContributorsPartialUpdateRequestRelationships(
                    user="user",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contributors_partial_update(
            node_id, user_id, relationships=relationships, attributes=attributes, request_options=request_options
        )
        return _response.data

    async def draft_registrations_list(
        self, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NodesDraftRegistrationsListResponseItem]:
        """
        A paginated list of all of the draft registrations of a given node.

        Draft Registrations contain Registration questions that will become part of the Registration. A Registration is a frozen version of the project that can never be deleted, but can be withdrawn and have it's metadata edited.

        Your original project remains editable but will now have the draft registration linked to it.
        #### Permissions
        Only project administrators may view draft registrations.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of 10 draft registrations. Each resource in the array is a separate draft registration object and contains the full representation of the draft registration, meaning additional requests to a draft registration's detail view are not necessary.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NodesDraftRegistrationsListResponseItem]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.nodes.draft_registrations_list(
                node_id="node_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.draft_registrations_list(node_id, request_options=request_options)
        return _response.data

    async def draft_registrations_create(
        self,
        node_id: str,
        *,
        attributes: NodesDraftRegistrationsCreateRequestAttributes,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Initiate a draft registration of the current node.
        Draft Registrations contain Registration questions that will become part of the Registration. A Registration is a frozen version of the project that can never be deleted, but can be withdrawn and have it's metadata edited.

        Your original project remains editable but will now have the draft registration linked to it.
        #### Permissions
        Only project administrators may view create registrations.
        #### Required
        Required fields for creating a draft registration include:

        &nbsp;&nbsp;&nbsp;&nbsp;`schema_id`
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the created draft registration, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        attributes : NodesDraftRegistrationsCreateRequestAttributes
            The properties of the Draft Registration entity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.nodes import NodesDraftRegistrationsCreateRequestAttributes

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.nodes.draft_registrations_create(
                node_id="node_id",
                attributes=NodesDraftRegistrationsCreateRequestAttributes(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.draft_registrations_create(
            node_id, attributes=attributes, request_options=request_options
        )
        return _response.data

    async def draft_registrations_delete(
        self, node_id: str, draft_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Permanently deletes a draft registration. A draft that has already been registered cannot be deleted.
        #### Permissions
        Only project administrators may delete draft registrations.
        #### Returns
        If the request is successful, no content is returned.

        If the request is unsuccessful, a JSON object with an `errors` key containing information about the failure will be returned. Refer to the [list of error codes]() to understand why this request may have failed.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        draft_id : str
            The unique identifier of the draft registration.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.nodes.draft_registrations_delete(
                node_id="node_id",
                draft_id="draft_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.draft_registrations_delete(
            node_id, draft_id, request_options=request_options
        )
        return _response.data

    async def draft_registrations_partial_update(
        self,
        node_id: str,
        draft_id: str,
        *,
        attributes: NodesDraftRegistrationsPartialUpdateRequestAttributes,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates a draft registration by setting the values of the attributes specified in the request body. Any unspecified attributes will be left unchanged.

        Draft Registrations contain Registration questions that will become part of the Registration. Answer the questions in the draft registration supplement by sending update requests until you are ready to submit the draft.

        The registration supplement of a draft registration cannot be updated after the draft has been created.

        When updating a draft registration, `registration_metadata` is required. It must be a dictionary with keys as question ids in the registration form, and values as nested dictionaries matching the specific format in the [registration schema](TODO: link me pls).

        If a question is multiple-choice, the question response must exactly match one of the possible choices.
        #### Permissions
        Only project administrators may update draft registrations.
        #### Returns
        Returns a JSON object with a `data` key containing the new representation of the updated draft registration, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        draft_id : str
            The unique identifier of the draft registration.

        attributes : NodesDraftRegistrationsPartialUpdateRequestAttributes
            The properties of the Draft Registration entity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.nodes import NodesDraftRegistrationsPartialUpdateRequestAttributes

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.nodes.draft_registrations_partial_update(
                node_id="node_id",
                draft_id="draft_id",
                attributes=NodesDraftRegistrationsPartialUpdateRequestAttributes(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.draft_registrations_partial_update(
            node_id, draft_id, attributes=attributes, request_options=request_options
        )
        return _response.data

    async def providers_list(
        self, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NodesProvidersListResponseItem]:
        """
        List of all storage providers that are configured for this node

        Users of the OSF may access their data on a [number of cloud-storage services](https://api.osf.io/v2/#storage-providers) that have integrations with the OSF. We call these **providers**. By default, every node has access to the OSF-provided storage but may use as many of the supported providers as desired.


        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of files. Each resource in the array is a separate file object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        Note: In the OSF filesystem model, providers are treated as folders, but with special properties that distinguish them from regular folders. Every provider folder is considered a root folder, and may not be deleted through the regular file API.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NodesProvidersListResponseItem]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.nodes.providers_list(
                node_id="node_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.providers_list(node_id, request_options=request_options)
        return _response.data

    async def providers_read(
        self, node_id: str, provider: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NodesProvidersReadResponse:
        """
        Retrieves the details of a storage provider enabled on this node.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested file object, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        provider : str
            The unique identifier of the storage provider.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NodesProvidersReadResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.nodes.providers_read(
                node_id="node_id",
                provider="provider",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.providers_read(node_id, provider, request_options=request_options)
        return _response.data

    async def files_list(
        self, node_id: str, provider: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NodesFilesListResponseItem]:
        """
        List of all the files/folders that are attached to your project for a given storage provider.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of files. Each resource in the array is a separate file object and contains the full representation of the file.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        #### Filtering

        You can optionally request that the response only include files that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/nodes/ezcuj/files/osfstorage/?filter[kind]=file

        Node files may be filtered by `id`, `name`, `node`, `kind`, `path`, `provider`, `size`, and `last_touched`.

        ### Waterbutler API actions

        Files can be modified through the Waterbutler API routes found in `links` (`new_folder`, `move`, `upload`, `download`, and `delete`).

        #### Download (files)

        To download a file, issue a GET request against the download link. The response will have the Content-Disposition header set, which will will trigger a download in a browser.

        #### Create Subfolder (folders)

        You can create a subfolder of an existing folder by issuing a PUT request against the new_folder link. The ?kind=folder portion of the query parameter is already included in the new_folder link. The name of the new subfolder should be provided in the name query parameter. The response will contain a WaterButler folder entity. If a folder with that name already exists in the parent directory, the server will return a 409 Conflict error response.

        #### Upload New File (folders)

        To upload a file to a folder, issue a PUT request to the folder's upload link with the raw file data in the request body, and the kind and name query parameters set to 'file' and the desired name of the file. The response will contain a WaterButler file entity that describes the new file. If a file with the same name already exists in the folder, the server will return a 409 Conflict error response.

        #### Update Existing File (file)

        To update an existing file, issue a PUT request to the file's upload link with the raw file data in the request body and the kind query parameter set to "file". The update action will create a new version of the file. The response will contain a WaterButler file entity that describes the updated file.

        #### Rename (files, folders)

        To rename a file or folder, issue a POST request to the move link with the action body parameter set to "rename" and the rename body parameter set to the desired name. The response will contain either a folder entity or file entity with the new name.

        #### Move & Copy (files, folders)

        Move and copy actions both use the same request structure, a POST to the move url, but with different values for the action body parameters. The path parameter is also required and should be the OSF path attribute of the folder being written to. The rename and conflict parameters are optional. If you wish to change the name of the file or folder at its destination, set the rename parameter to the new name. The conflict param governs how name clashes are resolved. Possible values are replace and keep. replace is the default and will overwrite the file that already exists in the target folder. keep will attempt to keep both by adding a suffix to the new file's name until it no longer conflicts. The suffix will be ' (x)' where x is a increasing integer starting from 1. This behavior is intended to mimic that of the OS X Finder. The response will contain either a folder entity or file entity with the new name.
        Files and folders can also be moved between nodes and providers. The resource parameter is the id of the node under which the file/folder should be moved. It must agree with the path parameter, that is the path must identify a valid folder under the node identified by resource. Likewise, the provider parameter may be used to move the file/folder to another storage provider, but both the resource and path parameters must belong to a node and folder already extant on that provider. Both resource and provider default to the current node and providers.
        If a moved/copied file is overwriting an existing file, a 200 OK response will be returned. Otherwise, a 201 Created will be returned.

        #### Delete (file, folders)

        To delete a file or folder send a DELETE request to the delete link. Nothing will be returned in the response body.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        provider : str
            The unique identifier of the storage provider.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NodesFilesListResponseItem]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.nodes.files_list(
                node_id="node_id",
                provider="provider",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.files_list(node_id, provider, request_options=request_options)
        return _response.data

    async def files_read(
        self, node_id: str, provider: str, path: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NodesFilesReadResponse:
        """
        Retrieves the details of a file attached to given node (project or component) for the given storage provider.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested file object, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        provider : str
            The unique identifier of the storage provider.

        path : str
            The unique identifier of the file path.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NodesFilesReadResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.nodes.files_read(
                node_id="node_id",
                provider="provider",
                path="path",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.files_read(node_id, provider, path, request_options=request_options)
        return _response.data

    async def forks_list(
        self, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NodesForksListResponseItem]:
        """

        A paginated list of the current node's forks. The returned fork nodes are sorted by their `forked_date`, with the most recently forked nodes appearing first.

        Forking a project creates a copy of an existing node and all of its contents. The fork always points back to the original node, forming a network of nodes.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of up to 10 forked nodes. If the current node has zero forked nodes, the `data` key will contain an empty array. Each resource in the array is a separate node object and contains the full representation of the forked node, meaning additional requests to the forked node's detail view are not necessary.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        This request should never return an error.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NodesForksListResponseItem]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.nodes.forks_list(
                node_id="node_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.forks_list(node_id, request_options=request_options)
        return _response.data

    async def forks_create(
        self,
        node_id: str,
        *,
        attributes: NodesForksCreateRequestAttributes,
        type: str,
        relationships: typing.Optional[NodesForksCreateRequestRelationships] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Creates a fork of the given node.

        Forking a project creates a copy of an existing node and all of its contents. The fork always points back to the original node, forming a network of nodes.

        You might use a fork to copy another's work to build on and extend. For example, a professor may create an OSF project of materials for individual student use. Each student forks the project to have his or her own copy of the materials to start his/her own work.

        When creating a fork, your fork will only contain public components of the current node and components for which you are a contributor. Private components that you do not have access to will not be forked.
        #### Required
        There are no required attributes when creating a fork, as all of the forked node's attributes will be copied from the current node.

        The `title` field is optional, with the default title being "Fork of " prepended to the current node's title.
        #### Returns
        Returns a JSON object with a `data` key containing the complete srepresentation of the forked node, if the request is successful.
        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        attributes : NodesForksCreateRequestAttributes
            The properties of the node entity.

        type : str
            The type identifier of the node entity (`nodes`).

        relationships : typing.Optional[NodesForksCreateRequestRelationships]
            URLs to other entities or entity collections that have a relationship to the node entity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.nodes import (
            NodesForksCreateRequestAttributes,
            NodesForksCreateRequestAttributesCategory,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.nodes.forks_create(
                node_id="node_id",
                attributes=NodesForksCreateRequestAttributes(
                    category=NodesForksCreateRequestAttributesCategory.ANALYSIS,
                    title="title",
                ),
                type="type",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.forks_create(
            node_id, attributes=attributes, type=type, relationships=relationships, request_options=request_options
        )
        return _response.data

    async def identifiers_list(
        self, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NodesIdentifiersListResponseItem]:
        """
        List all identifiers associated with a given node.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of identifiers. Each resource in the array is a separate identifier object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
        #### Filtering

        You can optionally request that the response only include nodes that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/nodes/ezcuj/identifiers/?filter[category]=ark

        Identifiers may be filtered by their `category` e.g `ark` or `doi`.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NodesIdentifiersListResponseItem]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.nodes.identifiers_list(
                node_id="node_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.identifiers_list(node_id, request_options=request_options)
        return _response.data

    async def institutions_list(
        self, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NodesInstitutionsListResponseItem]:
        """
        List of all institutions affiliated with this node.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of up to 10 affilited institutions. Each resource in the array is a separate institution object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NodesInstitutionsListResponseItem]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.nodes.institutions_list(
                node_id="node_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.institutions_list(node_id, request_options=request_options)
        return _response.data

    async def linked_nodes_list(
        self, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NodesLinkedNodesListResponseItem]:
        """
        List of all nodes linked to the given node.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of up to 10 nodes. Each resource in the array is a separate node object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
        #### Filtering
        You can optionally request that the response only include nodes that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/nodes/?filter[title]=reproducibility.

        Nodes may be filtered by their `title`, `category`, `description`, `public`, `registration`, or `tags`. `title`, `description`, and `category` are string fields and will be filteres using simple substring matching. `public`, `registration` are boolean and can be filtered using truthy values, such as `true`, `false`, `0`, `1`. `tags` is an array of simple strings.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NodesLinkedNodesListResponseItem]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.nodes.linked_nodes_list(
                node_id="node_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.linked_nodes_list(node_id, request_options=request_options)
        return _response.data

    async def logs_list(
        self, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NodesLogsListResponseItem]:
        """
        A paginated list of all logs associated with a given node.

        The returned logs are sorted by their `date`, with the most recents logs appearing first.

        This list includes the logs of the specified node as well as the logs of that node's children to which the current user has read-only access.

        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of up to 10 logs. Each resource in the array is a separate logs object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
        #### Filtering
        You can optionally request that the response only include logs that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/nodes/ezcuj/logs/?filter[action]=made_private.

        Nodes may be filtered by their `action`, and `date`.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NodesLogsListResponseItem]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.nodes.logs_list(
                node_id="node_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.logs_list(node_id, request_options=request_options)
        return _response.data

    async def preprints_list(
        self, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NodesPreprintsListResponseItem]:
        """
        A paginated list of preprints related to a given node. The returned preprints are sorted by their creation date, with the most recent preprints appearing first.

        **Note: This API endpoint is under active development, and is subject to change in the future.**
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of up to 10 preprints. Each resource in the array is a separate preprint object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NodesPreprintsListResponseItem]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.nodes.preprints_list(
                node_id="node_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.preprints_list(node_id, request_options=request_options)
        return _response.data

    async def registrations_list(
        self, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NodesRegistrationsListResponseItem]:
        """
        List of all registrations of the given node.
        #### Returns

        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of up to 10 registrations. Each resource in the array is a separate registrations object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
        #### Filtering

        You can optionally request that the response only include registrations that match your filters by utilizing the filter query parameter, e.g. https://api.osf.io/v2/registrations/?filter[title]=open.

        Registrations may be filtered by their `id`, `title`, `category`, `description`, `public`, `tags`, `date_created`, `date_modified`, `root`, `parent`, and `contributors`.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NodesRegistrationsListResponseItem]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.nodes.registrations_list(
                node_id="node_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.registrations_list(node_id, request_options=request_options)
        return _response.data

    async def view_only_links_list(
        self, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NodesViewOnlyLinksListResponseItem]:
        """
        List of view only links on a node.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of up to 10 view only links. Each resource in the array is a view only link object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        #### Permissions

        View only links on a node, public or private, are readable and writeable only by users that are administrators on the node.

        #### Filtering

        You can optionally request that the response only include view only links that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/nodes/ezcuj/view_only_links/?filter[anonymous]=true.

        View Only Links may be filtered based on their `name`, `anonymous` and `date_created` fields. Possible comparison operators include 'gt' (greater than), 'gte'(greater than or equal to), 'lt' (less than) and 'lte' (less than or equal to). The date must be in the format YYYY-MM-DD and the time is optional.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NodesViewOnlyLinksListResponseItem]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.nodes.view_only_links_list(
                node_id="node_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.view_only_links_list(node_id, request_options=request_options)
        return _response.data

    async def view_only_links_read(
        self, node_id: str, link_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NodesViewOnlyLinksReadResponse:
        """
        Retrieves the details of a view only link on a node.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested view only link, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
        #### Permissions

        View only links on a node, public or private, are readable and writeable only by users that are administrators on the node.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        link_id : str
            The unique identifier of the view only link.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NodesViewOnlyLinksReadResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.nodes.view_only_links_read(
                node_id="node_id",
                link_id="link_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.view_only_links_read(node_id, link_id, request_options=request_options)
        return _response.data

    async def wikis_list(
        self, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NodesWikisListResponseItem]:
        """
        List of wiki pages on a node.
        #### Returns
        Paginated list of the node's current wiki page versions ordered by their date_modified. Each resource contains the full representation of the wiki, meaning additional requests to an individual wiki's detail view are not necessary.

        Note that if an anonymous view_only key is being used, the user relationship will not be exposed.

        If the request is unsuccessful, a JSON object with an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
        #### Filtering
        Wiki pages can be filtered based on their `name` and `date_modified` fields.
        + `filter[name]=<Str>` -- filter wiki pages by name
        + `filter[date_modified][comparison_operator]=YYYY-MM-DDTH:M:S` -- filter wiki pages based on date modified.

        Possible comparison operators include 'gt' (greater than), 'gte'(greater than or equal to), 'lt' (less than) and 'lte' (less than or equal to). The date must be in the format YYYY-MM-DD and the time is optional.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NodesWikisListResponseItem]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.nodes.wikis_list(
                node_id="node_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.wikis_list(node_id, request_options=request_options)
        return _response.data

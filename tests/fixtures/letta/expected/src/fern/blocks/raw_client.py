

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.agent_state import AgentState
from ..types.block_response import BlockResponse
from ..types.http_validation_error import HttpValidationError
from .types.list_agents_for_block_request_include_item import ListAgentsForBlockRequestIncludeItem
from .types.list_agents_for_block_request_order import ListAgentsForBlockRequestOrder
from .types.list_agents_for_block_request_order_by import ListAgentsForBlockRequestOrderBy
from .types.list_blocks_request_order import ListBlocksRequestOrder
from .types.list_blocks_request_order_by import ListBlocksRequestOrderBy
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawBlocksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_blocks(
        self,
        *,
        label: typing.Optional[str] = None,
        templates_only: typing.Optional[bool] = None,
        name: typing.Optional[str] = None,
        identity_id: typing.Optional[str] = None,
        identifier_keys: typing.Optional[typing.Sequence[str]] = None,
        project_id: typing.Optional[str] = None,
        tags: typing.Optional[typing.Sequence[str]] = None,
        match_all_tags: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        order: typing.Optional[ListBlocksRequestOrder] = None,
        order_by: typing.Optional[ListBlocksRequestOrderBy] = None,
        label_search: typing.Optional[str] = None,
        description_search: typing.Optional[str] = None,
        value_search: typing.Optional[str] = None,
        connected_to_agents_count_gt: typing.Optional[int] = None,
        connected_to_agents_count_lt: typing.Optional[int] = None,
        connected_to_agents_count_eq: typing.Optional[typing.Sequence[int]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[BlockResponse]]:
        """
        Parameters
        ----------
        label : typing.Optional[str]
            Label to include (alphanumeric, hyphens, underscores, forward slashes)

        templates_only : typing.Optional[bool]
            Whether to include only templates

        name : typing.Optional[str]
            Name filter (alphanumeric, spaces, hyphens, underscores)

        identity_id : typing.Optional[str]
            The ID of the identity in the format 'identity-<uuid4>'

        identifier_keys : typing.Optional[typing.Sequence[str]]
            Search agents by identifier keys

        project_id : typing.Optional[str]
            Search blocks by project id

        tags : typing.Optional[typing.Sequence[str]]
            List of tags to filter blocks by

        match_all_tags : typing.Optional[bool]
            If True, only returns blocks that match ALL given tags. Otherwise, return blocks that have ANY of the passed-in tags.

        limit : typing.Optional[int]
            Number of blocks to return

        before : typing.Optional[str]
            Block ID cursor for pagination. Returns blocks that come before this block ID in the specified sort order

        after : typing.Optional[str]
            Block ID cursor for pagination. Returns blocks that come after this block ID in the specified sort order

        order : typing.Optional[ListBlocksRequestOrder]
            Sort order for blocks by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListBlocksRequestOrderBy]
            Field to sort by

        label_search : typing.Optional[str]
            Search blocks by label. If provided, returns blocks whose label matches the search query. This is a full-text search on block labels.

        description_search : typing.Optional[str]
            Search blocks by description. If provided, returns blocks whose description matches the search query. This is a full-text search on block descriptions.

        value_search : typing.Optional[str]
            Search blocks by value. If provided, returns blocks whose value matches the search query. This is a full-text search on block values.

        connected_to_agents_count_gt : typing.Optional[int]
            Filter blocks by the number of connected agents. If provided, returns blocks that have more than this number of connected agents.

        connected_to_agents_count_lt : typing.Optional[int]
            Filter blocks by the number of connected agents. If provided, returns blocks that have less than this number of connected agents.

        connected_to_agents_count_eq : typing.Optional[typing.Sequence[int]]
            Filter blocks by the exact number of connected agents. If provided, returns blocks that have exactly this number of connected agents.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[BlockResponse]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/blocks/",
            method="GET",
            params={
                "label": label,
                "templates_only": templates_only,
                "name": name,
                "identity_id": identity_id,
                "identifier_keys": identifier_keys,
                "project_id": project_id,
                "tags": tags,
                "match_all_tags": match_all_tags,
                "limit": limit,
                "before": before,
                "after": after,
                "order": order,
                "order_by": order_by,
                "label_search": label_search,
                "description_search": description_search,
                "value_search": value_search,
                "connected_to_agents_count_gt": connected_to_agents_count_gt,
                "connected_to_agents_count_lt": connected_to_agents_count_lt,
                "connected_to_agents_count_eq": connected_to_agents_count_eq,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[BlockResponse],
                    parse_obj_as(
                        type_=typing.List[BlockResponse],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_block(
        self,
        *,
        value: str,
        label: str,
        limit: typing.Optional[int] = OMIT,
        project_id: typing.Optional[str] = OMIT,
        template_name: typing.Optional[str] = OMIT,
        is_template: typing.Optional[bool] = OMIT,
        template_id: typing.Optional[str] = OMIT,
        base_template_id: typing.Optional[str] = OMIT,
        deployment_id: typing.Optional[str] = OMIT,
        entity_id: typing.Optional[str] = OMIT,
        preserve_on_migration: typing.Optional[bool] = OMIT,
        read_only: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        hidden: typing.Optional[bool] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BlockResponse]:
        """
        Parameters
        ----------
        value : str
            Value of the block.

        label : str
            Label of the block.

        limit : typing.Optional[int]
            Character limit of the block.

        project_id : typing.Optional[str]
            The associated project id.

        template_name : typing.Optional[str]
            Name of the block if it is a template.

        is_template : typing.Optional[bool]

        template_id : typing.Optional[str]
            The id of the template.

        base_template_id : typing.Optional[str]
            The base template id of the block.

        deployment_id : typing.Optional[str]
            The id of the deployment.

        entity_id : typing.Optional[str]
            The id of the entity within the template.

        preserve_on_migration : typing.Optional[bool]
            Preserve the block on template migration.

        read_only : typing.Optional[bool]
            Whether the agent has read-only access to the block.

        description : typing.Optional[str]
            Description of the block.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata of the block.

        hidden : typing.Optional[bool]
            If set to True, the block will be hidden.

        tags : typing.Optional[typing.Sequence[str]]
            The tags to associate with the block.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BlockResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/blocks/",
            method="POST",
            json={
                "value": value,
                "limit": limit,
                "project_id": project_id,
                "template_name": template_name,
                "is_template": is_template,
                "template_id": template_id,
                "base_template_id": base_template_id,
                "deployment_id": deployment_id,
                "entity_id": entity_id,
                "preserve_on_migration": preserve_on_migration,
                "label": label,
                "read_only": read_only,
                "description": description,
                "metadata": metadata,
                "hidden": hidden,
                "tags": tags,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BlockResponse,
                    parse_obj_as(
                        type_=BlockResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def count_blocks(
        self,
        *,
        label: typing.Optional[str] = None,
        templates_only: typing.Optional[bool] = None,
        name: typing.Optional[str] = None,
        tags: typing.Optional[typing.Sequence[str]] = None,
        match_all_tags: typing.Optional[bool] = None,
        project_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[int]:
        """
        Count all blocks with optional filtering.
        Supports the same filters as list_blocks for consistent querying.

        Parameters
        ----------
        label : typing.Optional[str]
            Label to include (alphanumeric, hyphens, underscores, forward slashes)

        templates_only : typing.Optional[bool]
            Whether to include only templates

        name : typing.Optional[str]
            Name filter (alphanumeric, spaces, hyphens, underscores)

        tags : typing.Optional[typing.Sequence[str]]
            List of tags to filter blocks by

        match_all_tags : typing.Optional[bool]
            If True, only counts blocks that match ALL given tags. Otherwise, counts blocks that have ANY of the passed-in tags.

        project_id : typing.Optional[str]
            Search blocks by project id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[int]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/blocks/count",
            method="GET",
            params={
                "label": label,
                "templates_only": templates_only,
                "name": name,
                "tags": tags,
                "match_all_tags": match_all_tags,
                "project_id": project_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    int,
                    parse_obj_as(
                        type_=int,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def retrieve_block(
        self, block_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[BlockResponse]:
        """
        Parameters
        ----------
        block_id : str
            The ID of the block in the format 'block-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BlockResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/blocks/{encode_path_param(block_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BlockResponse,
                    parse_obj_as(
                        type_=BlockResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_block(
        self, block_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Any]:
        """
        Parameters
        ----------
        block_id : str
            The ID of the block in the format 'block-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/blocks/{encode_path_param(block_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def modify_block(
        self,
        block_id: str,
        *,
        value: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        project_id: typing.Optional[str] = OMIT,
        template_name: typing.Optional[str] = OMIT,
        is_template: typing.Optional[bool] = OMIT,
        template_id: typing.Optional[str] = OMIT,
        base_template_id: typing.Optional[str] = OMIT,
        deployment_id: typing.Optional[str] = OMIT,
        entity_id: typing.Optional[str] = OMIT,
        preserve_on_migration: typing.Optional[bool] = OMIT,
        label: typing.Optional[str] = OMIT,
        read_only: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        hidden: typing.Optional[bool] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BlockResponse]:
        """
        Parameters
        ----------
        block_id : str
            The ID of the block in the format 'block-<uuid4>'

        value : typing.Optional[str]
            Value of the block.

        limit : typing.Optional[int]
            Character limit of the block.

        project_id : typing.Optional[str]
            The associated project id.

        template_name : typing.Optional[str]
            Name of the block if it is a template.

        is_template : typing.Optional[bool]
            Whether the block is a template (e.g. saved human/persona options).

        template_id : typing.Optional[str]
            The id of the template.

        base_template_id : typing.Optional[str]
            The base template id of the block.

        deployment_id : typing.Optional[str]
            The id of the deployment.

        entity_id : typing.Optional[str]
            The id of the entity within the template.

        preserve_on_migration : typing.Optional[bool]
            Preserve the block on template migration.

        label : typing.Optional[str]
            Label of the block (e.g. 'human', 'persona') in the context window.

        read_only : typing.Optional[bool]
            Whether the agent has read-only access to the block.

        description : typing.Optional[str]
            Description of the block.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata of the block.

        hidden : typing.Optional[bool]
            If set to True, the block will be hidden.

        tags : typing.Optional[typing.Sequence[str]]
            The tags to associate with the block.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BlockResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/blocks/{encode_path_param(block_id)}",
            method="PATCH",
            json={
                "value": value,
                "limit": limit,
                "project_id": project_id,
                "template_name": template_name,
                "is_template": is_template,
                "template_id": template_id,
                "base_template_id": base_template_id,
                "deployment_id": deployment_id,
                "entity_id": entity_id,
                "preserve_on_migration": preserve_on_migration,
                "label": label,
                "read_only": read_only,
                "description": description,
                "metadata": metadata,
                "hidden": hidden,
                "tags": tags,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BlockResponse,
                    parse_obj_as(
                        type_=BlockResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_agents_for_block(
        self,
        block_id: str,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListAgentsForBlockRequestOrder] = None,
        order_by: typing.Optional[ListAgentsForBlockRequestOrderBy] = None,
        include_relationships: typing.Optional[typing.Sequence[str]] = None,
        include: typing.Optional[
            typing.Union[ListAgentsForBlockRequestIncludeItem, typing.Sequence[ListAgentsForBlockRequestIncludeItem]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[AgentState]]:
        """
        Retrieves all agents associated with the specified block.
        Raises a 404 if the block does not exist.

        Parameters
        ----------
        block_id : str
            The ID of the block in the format 'block-<uuid4>'

        before : typing.Optional[str]
            Agent ID cursor for pagination. Returns agents that come before this agent ID in the specified sort order

        after : typing.Optional[str]
            Agent ID cursor for pagination. Returns agents that come after this agent ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of agents to return

        order : typing.Optional[ListAgentsForBlockRequestOrder]
            Sort order for agents by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListAgentsForBlockRequestOrderBy]
            Field to sort by

        include_relationships : typing.Optional[typing.Sequence[str]]
            Specify which relational fields (e.g., 'tools', 'sources', 'memory') to include in the response. If not provided, all relationships are loaded by default. Using this can optimize performance by reducing unnecessary joins.This is a legacy parameter, and no longer supported after 1.0.0 SDK versions.

        include : typing.Optional[typing.Union[ListAgentsForBlockRequestIncludeItem, typing.Sequence[ListAgentsForBlockRequestIncludeItem]]]
            Specify which relational fields to include in the response. No relationships are included by default.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[AgentState]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/blocks/{encode_path_param(block_id)}/agents",
            method="GET",
            params={
                "before": before,
                "after": after,
                "limit": limit,
                "order": order,
                "order_by": order_by,
                "include_relationships": include_relationships,
                "include": include,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[AgentState],
                    parse_obj_as(
                        type_=typing.List[AgentState],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def attach_identity_to_block(
        self, block_id: str, identity_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[BlockResponse]:
        """
        Attach an identity to a block.

        Parameters
        ----------
        block_id : str
            The ID of the block in the format 'block-<uuid4>'

        identity_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BlockResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/blocks/{encode_path_param(block_id)}/identities/attach/{encode_path_param(identity_id)}",
            method="PATCH",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BlockResponse,
                    parse_obj_as(
                        type_=BlockResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def detach_identity_from_block(
        self, block_id: str, identity_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[BlockResponse]:
        """
        Detach an identity from a block.

        Parameters
        ----------
        block_id : str
            The ID of the block in the format 'block-<uuid4>'

        identity_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BlockResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/blocks/{encode_path_param(block_id)}/identities/detach/{encode_path_param(identity_id)}",
            method="PATCH",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BlockResponse,
                    parse_obj_as(
                        type_=BlockResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawBlocksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_blocks(
        self,
        *,
        label: typing.Optional[str] = None,
        templates_only: typing.Optional[bool] = None,
        name: typing.Optional[str] = None,
        identity_id: typing.Optional[str] = None,
        identifier_keys: typing.Optional[typing.Sequence[str]] = None,
        project_id: typing.Optional[str] = None,
        tags: typing.Optional[typing.Sequence[str]] = None,
        match_all_tags: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        order: typing.Optional[ListBlocksRequestOrder] = None,
        order_by: typing.Optional[ListBlocksRequestOrderBy] = None,
        label_search: typing.Optional[str] = None,
        description_search: typing.Optional[str] = None,
        value_search: typing.Optional[str] = None,
        connected_to_agents_count_gt: typing.Optional[int] = None,
        connected_to_agents_count_lt: typing.Optional[int] = None,
        connected_to_agents_count_eq: typing.Optional[typing.Sequence[int]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[BlockResponse]]:
        """
        Parameters
        ----------
        label : typing.Optional[str]
            Label to include (alphanumeric, hyphens, underscores, forward slashes)

        templates_only : typing.Optional[bool]
            Whether to include only templates

        name : typing.Optional[str]
            Name filter (alphanumeric, spaces, hyphens, underscores)

        identity_id : typing.Optional[str]
            The ID of the identity in the format 'identity-<uuid4>'

        identifier_keys : typing.Optional[typing.Sequence[str]]
            Search agents by identifier keys

        project_id : typing.Optional[str]
            Search blocks by project id

        tags : typing.Optional[typing.Sequence[str]]
            List of tags to filter blocks by

        match_all_tags : typing.Optional[bool]
            If True, only returns blocks that match ALL given tags. Otherwise, return blocks that have ANY of the passed-in tags.

        limit : typing.Optional[int]
            Number of blocks to return

        before : typing.Optional[str]
            Block ID cursor for pagination. Returns blocks that come before this block ID in the specified sort order

        after : typing.Optional[str]
            Block ID cursor for pagination. Returns blocks that come after this block ID in the specified sort order

        order : typing.Optional[ListBlocksRequestOrder]
            Sort order for blocks by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListBlocksRequestOrderBy]
            Field to sort by

        label_search : typing.Optional[str]
            Search blocks by label. If provided, returns blocks whose label matches the search query. This is a full-text search on block labels.

        description_search : typing.Optional[str]
            Search blocks by description. If provided, returns blocks whose description matches the search query. This is a full-text search on block descriptions.

        value_search : typing.Optional[str]
            Search blocks by value. If provided, returns blocks whose value matches the search query. This is a full-text search on block values.

        connected_to_agents_count_gt : typing.Optional[int]
            Filter blocks by the number of connected agents. If provided, returns blocks that have more than this number of connected agents.

        connected_to_agents_count_lt : typing.Optional[int]
            Filter blocks by the number of connected agents. If provided, returns blocks that have less than this number of connected agents.

        connected_to_agents_count_eq : typing.Optional[typing.Sequence[int]]
            Filter blocks by the exact number of connected agents. If provided, returns blocks that have exactly this number of connected agents.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[BlockResponse]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/blocks/",
            method="GET",
            params={
                "label": label,
                "templates_only": templates_only,
                "name": name,
                "identity_id": identity_id,
                "identifier_keys": identifier_keys,
                "project_id": project_id,
                "tags": tags,
                "match_all_tags": match_all_tags,
                "limit": limit,
                "before": before,
                "after": after,
                "order": order,
                "order_by": order_by,
                "label_search": label_search,
                "description_search": description_search,
                "value_search": value_search,
                "connected_to_agents_count_gt": connected_to_agents_count_gt,
                "connected_to_agents_count_lt": connected_to_agents_count_lt,
                "connected_to_agents_count_eq": connected_to_agents_count_eq,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[BlockResponse],
                    parse_obj_as(
                        type_=typing.List[BlockResponse],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_block(
        self,
        *,
        value: str,
        label: str,
        limit: typing.Optional[int] = OMIT,
        project_id: typing.Optional[str] = OMIT,
        template_name: typing.Optional[str] = OMIT,
        is_template: typing.Optional[bool] = OMIT,
        template_id: typing.Optional[str] = OMIT,
        base_template_id: typing.Optional[str] = OMIT,
        deployment_id: typing.Optional[str] = OMIT,
        entity_id: typing.Optional[str] = OMIT,
        preserve_on_migration: typing.Optional[bool] = OMIT,
        read_only: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        hidden: typing.Optional[bool] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BlockResponse]:
        """
        Parameters
        ----------
        value : str
            Value of the block.

        label : str
            Label of the block.

        limit : typing.Optional[int]
            Character limit of the block.

        project_id : typing.Optional[str]
            The associated project id.

        template_name : typing.Optional[str]
            Name of the block if it is a template.

        is_template : typing.Optional[bool]

        template_id : typing.Optional[str]
            The id of the template.

        base_template_id : typing.Optional[str]
            The base template id of the block.

        deployment_id : typing.Optional[str]
            The id of the deployment.

        entity_id : typing.Optional[str]
            The id of the entity within the template.

        preserve_on_migration : typing.Optional[bool]
            Preserve the block on template migration.

        read_only : typing.Optional[bool]
            Whether the agent has read-only access to the block.

        description : typing.Optional[str]
            Description of the block.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata of the block.

        hidden : typing.Optional[bool]
            If set to True, the block will be hidden.

        tags : typing.Optional[typing.Sequence[str]]
            The tags to associate with the block.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BlockResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/blocks/",
            method="POST",
            json={
                "value": value,
                "limit": limit,
                "project_id": project_id,
                "template_name": template_name,
                "is_template": is_template,
                "template_id": template_id,
                "base_template_id": base_template_id,
                "deployment_id": deployment_id,
                "entity_id": entity_id,
                "preserve_on_migration": preserve_on_migration,
                "label": label,
                "read_only": read_only,
                "description": description,
                "metadata": metadata,
                "hidden": hidden,
                "tags": tags,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BlockResponse,
                    parse_obj_as(
                        type_=BlockResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def count_blocks(
        self,
        *,
        label: typing.Optional[str] = None,
        templates_only: typing.Optional[bool] = None,
        name: typing.Optional[str] = None,
        tags: typing.Optional[typing.Sequence[str]] = None,
        match_all_tags: typing.Optional[bool] = None,
        project_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[int]:
        """
        Count all blocks with optional filtering.
        Supports the same filters as list_blocks for consistent querying.

        Parameters
        ----------
        label : typing.Optional[str]
            Label to include (alphanumeric, hyphens, underscores, forward slashes)

        templates_only : typing.Optional[bool]
            Whether to include only templates

        name : typing.Optional[str]
            Name filter (alphanumeric, spaces, hyphens, underscores)

        tags : typing.Optional[typing.Sequence[str]]
            List of tags to filter blocks by

        match_all_tags : typing.Optional[bool]
            If True, only counts blocks that match ALL given tags. Otherwise, counts blocks that have ANY of the passed-in tags.

        project_id : typing.Optional[str]
            Search blocks by project id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[int]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/blocks/count",
            method="GET",
            params={
                "label": label,
                "templates_only": templates_only,
                "name": name,
                "tags": tags,
                "match_all_tags": match_all_tags,
                "project_id": project_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    int,
                    parse_obj_as(
                        type_=int,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def retrieve_block(
        self, block_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[BlockResponse]:
        """
        Parameters
        ----------
        block_id : str
            The ID of the block in the format 'block-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BlockResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/blocks/{encode_path_param(block_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BlockResponse,
                    parse_obj_as(
                        type_=BlockResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_block(
        self, block_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Parameters
        ----------
        block_id : str
            The ID of the block in the format 'block-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/blocks/{encode_path_param(block_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def modify_block(
        self,
        block_id: str,
        *,
        value: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        project_id: typing.Optional[str] = OMIT,
        template_name: typing.Optional[str] = OMIT,
        is_template: typing.Optional[bool] = OMIT,
        template_id: typing.Optional[str] = OMIT,
        base_template_id: typing.Optional[str] = OMIT,
        deployment_id: typing.Optional[str] = OMIT,
        entity_id: typing.Optional[str] = OMIT,
        preserve_on_migration: typing.Optional[bool] = OMIT,
        label: typing.Optional[str] = OMIT,
        read_only: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        hidden: typing.Optional[bool] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BlockResponse]:
        """
        Parameters
        ----------
        block_id : str
            The ID of the block in the format 'block-<uuid4>'

        value : typing.Optional[str]
            Value of the block.

        limit : typing.Optional[int]
            Character limit of the block.

        project_id : typing.Optional[str]
            The associated project id.

        template_name : typing.Optional[str]
            Name of the block if it is a template.

        is_template : typing.Optional[bool]
            Whether the block is a template (e.g. saved human/persona options).

        template_id : typing.Optional[str]
            The id of the template.

        base_template_id : typing.Optional[str]
            The base template id of the block.

        deployment_id : typing.Optional[str]
            The id of the deployment.

        entity_id : typing.Optional[str]
            The id of the entity within the template.

        preserve_on_migration : typing.Optional[bool]
            Preserve the block on template migration.

        label : typing.Optional[str]
            Label of the block (e.g. 'human', 'persona') in the context window.

        read_only : typing.Optional[bool]
            Whether the agent has read-only access to the block.

        description : typing.Optional[str]
            Description of the block.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata of the block.

        hidden : typing.Optional[bool]
            If set to True, the block will be hidden.

        tags : typing.Optional[typing.Sequence[str]]
            The tags to associate with the block.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BlockResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/blocks/{encode_path_param(block_id)}",
            method="PATCH",
            json={
                "value": value,
                "limit": limit,
                "project_id": project_id,
                "template_name": template_name,
                "is_template": is_template,
                "template_id": template_id,
                "base_template_id": base_template_id,
                "deployment_id": deployment_id,
                "entity_id": entity_id,
                "preserve_on_migration": preserve_on_migration,
                "label": label,
                "read_only": read_only,
                "description": description,
                "metadata": metadata,
                "hidden": hidden,
                "tags": tags,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BlockResponse,
                    parse_obj_as(
                        type_=BlockResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_agents_for_block(
        self,
        block_id: str,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListAgentsForBlockRequestOrder] = None,
        order_by: typing.Optional[ListAgentsForBlockRequestOrderBy] = None,
        include_relationships: typing.Optional[typing.Sequence[str]] = None,
        include: typing.Optional[
            typing.Union[ListAgentsForBlockRequestIncludeItem, typing.Sequence[ListAgentsForBlockRequestIncludeItem]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[AgentState]]:
        """
        Retrieves all agents associated with the specified block.
        Raises a 404 if the block does not exist.

        Parameters
        ----------
        block_id : str
            The ID of the block in the format 'block-<uuid4>'

        before : typing.Optional[str]
            Agent ID cursor for pagination. Returns agents that come before this agent ID in the specified sort order

        after : typing.Optional[str]
            Agent ID cursor for pagination. Returns agents that come after this agent ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of agents to return

        order : typing.Optional[ListAgentsForBlockRequestOrder]
            Sort order for agents by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListAgentsForBlockRequestOrderBy]
            Field to sort by

        include_relationships : typing.Optional[typing.Sequence[str]]
            Specify which relational fields (e.g., 'tools', 'sources', 'memory') to include in the response. If not provided, all relationships are loaded by default. Using this can optimize performance by reducing unnecessary joins.This is a legacy parameter, and no longer supported after 1.0.0 SDK versions.

        include : typing.Optional[typing.Union[ListAgentsForBlockRequestIncludeItem, typing.Sequence[ListAgentsForBlockRequestIncludeItem]]]
            Specify which relational fields to include in the response. No relationships are included by default.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[AgentState]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/blocks/{encode_path_param(block_id)}/agents",
            method="GET",
            params={
                "before": before,
                "after": after,
                "limit": limit,
                "order": order,
                "order_by": order_by,
                "include_relationships": include_relationships,
                "include": include,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[AgentState],
                    parse_obj_as(
                        type_=typing.List[AgentState],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def attach_identity_to_block(
        self, block_id: str, identity_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[BlockResponse]:
        """
        Attach an identity to a block.

        Parameters
        ----------
        block_id : str
            The ID of the block in the format 'block-<uuid4>'

        identity_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BlockResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/blocks/{encode_path_param(block_id)}/identities/attach/{encode_path_param(identity_id)}",
            method="PATCH",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BlockResponse,
                    parse_obj_as(
                        type_=BlockResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def detach_identity_from_block(
        self, block_id: str, identity_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[BlockResponse]:
        """
        Detach an identity from a block.

        Parameters
        ----------
        block_id : str
            The ID of the block in the format 'block-<uuid4>'

        identity_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BlockResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/blocks/{encode_path_param(block_id)}/identities/detach/{encode_path_param(identity_id)}",
            method="PATCH",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BlockResponse,
                    parse_obj_as(
                        type_=BlockResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

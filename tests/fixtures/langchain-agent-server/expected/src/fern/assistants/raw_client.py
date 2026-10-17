

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.conflict_error import ConflictError
from ..errors.not_found_error import NotFoundError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.assistant import Assistant
from ..types.error_response import ErrorResponse
from ..types.get_assistant_graph_assistants_assistant_id_graph_get_request_xray import (
    GetAssistantGraphAssistantsAssistantIdGraphGetRequestXray,
)
from ..types.graph_schema import GraphSchema
from ..types.subgraphs import Subgraphs
from .types.assistant_create_if_exists import AssistantCreateIfExists
from .types.assistant_search_request_select_item import AssistantSearchRequestSelectItem
from .types.assistant_search_request_sort_by import AssistantSearchRequestSortBy
from .types.assistant_search_request_sort_order import AssistantSearchRequestSortOrder
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawAssistantsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_assistant(
        self,
        *,
        graph_id: str,
        assistant_id: typing.Optional[str] = OMIT,
        config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        context: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        if_exists: typing.Optional[AssistantCreateIfExists] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Assistant]:
        """
        Create an assistant.

        An initial version of the assistant will be created and the assistant is set to that version. To change versions, use the `POST /assistants/{assistant_id}/latest` endpoint.

        Parameters
        ----------
        graph_id : str
            The ID of the graph the assistant should use. The graph ID is normally set in your langgraph.json configuration.

        assistant_id : typing.Optional[str]
            The ID of the assistant. If not provided, a random UUID will be generated.

        config : typing.Optional[typing.Dict[str, typing.Any]]
            Configuration to use for the graph. Useful when graph is configurable and you want to create different assistants based on different configurations.

        context : typing.Optional[typing.Dict[str, typing.Any]]
            Static context added to the assistant.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to add to assistant.

        if_exists : typing.Optional[AssistantCreateIfExists]
            How to handle duplicate creation. Must be either 'raise' (raise error if duplicate), or 'do_nothing' (return existing assistant).

        name : typing.Optional[str]
            The name of the assistant. Defaults to 'Untitled'.

        description : typing.Optional[str]
            The description of the assistant. Defaults to null.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Assistant]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "assistants",
            method="POST",
            json={
                "assistant_id": assistant_id,
                "graph_id": graph_id,
                "config": config,
                "context": context,
                "metadata": metadata,
                "if_exists": if_exists,
                "name": name,
                "description": description,
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
                    Assistant,
                    parse_obj_as(
                        type_=Assistant,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def search_assistants(
        self,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        graph_id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        sort_by: typing.Optional[AssistantSearchRequestSortBy] = OMIT,
        sort_order: typing.Optional[AssistantSearchRequestSortOrder] = OMIT,
        select: typing.Optional[typing.Sequence[AssistantSearchRequestSelectItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Assistant]]:
        """
        Search for assistants.

        This endpoint also functions as the endpoint to list all assistants.

        Parameters
        ----------
        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to filter by. Exact match filter for each KV pair.

        graph_id : typing.Optional[str]
            The ID of the graph to filter by. The graph ID is normally set in your langgraph.json configuration.

        name : typing.Optional[str]
            Name of the assistant to filter by. The filtering logic will match (case insensitive) assistants where 'name' is a substring of the assistant name.

        limit : typing.Optional[int]
            The maximum number of results to return.

        offset : typing.Optional[int]
            The number of results to skip.

        sort_by : typing.Optional[AssistantSearchRequestSortBy]
            The field to sort by.

        sort_order : typing.Optional[AssistantSearchRequestSortOrder]
            The order to sort by.

        select : typing.Optional[typing.Sequence[AssistantSearchRequestSelectItem]]
            Specify which fields to return. If not provided, all fields are returned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Assistant]]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "assistants/search",
            method="POST",
            json={
                "metadata": metadata,
                "graph_id": graph_id,
                "name": name,
                "limit": limit,
                "offset": offset,
                "sort_by": sort_by,
                "sort_order": sort_order,
                "select": select,
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
                    typing.List[Assistant],
                    parse_obj_as(
                        type_=typing.List[Assistant],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def count_assistants(
        self,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        graph_id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[int]:
        """
        Get the count of assistants matching the specified criteria.

        Parameters
        ----------
        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to filter by. Exact match filter for each KV pair.

        graph_id : typing.Optional[str]
            The ID of the graph to filter by. The graph ID is normally set in your langgraph.json configuration.

        name : typing.Optional[str]
            Name of the assistant to filter by. The filtering logic will match (case insensitive) assistants where 'name' is a substring of the assistant name.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[int]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "assistants/count",
            method="POST",
            json={
                "metadata": metadata,
                "graph_id": graph_id,
                "name": name,
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
                    int,
                    parse_obj_as(
                        type_=int,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def get_assistant(
        self, assistant_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Assistant]:
        """
        Get an assistant by ID.

        Parameters
        ----------
        assistant_id : str
            The ID of the assistant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Assistant]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"assistants/{encode_path_param(assistant_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Assistant,
                    parse_obj_as(
                        type_=Assistant,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def delete_assistant(
        self,
        assistant_id: str,
        *,
        delete_threads: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
        """
        Delete an assistant by ID.

        All versions of the assistant will be deleted as well.

        Parameters
        ----------
        assistant_id : str
            The ID of the assistant.

        delete_threads : typing.Optional[bool]
            If true, delete all threads with metadata.assistant_id matching this assistant, along with runs and checkpoints belonging to those threads. Auth filters are applied, so threads not visible to the user will not be deleted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"assistants/{encode_path_param(assistant_id)}",
            method="DELETE",
            params={
                "delete_threads": delete_threads,
            },
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def patch_assistant(
        self,
        assistant_id: str,
        *,
        graph_id: typing.Optional[str] = OMIT,
        config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        context: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Assistant]:
        """
        Update an assistant.

        Parameters
        ----------
        assistant_id : str
            The ID of the assistant.

        graph_id : typing.Optional[str]
            The ID of the graph the assistant should use. The graph ID is normally set in your langgraph.json configuration. If not provided, assistant will keep pointing to same graph.

        config : typing.Optional[typing.Dict[str, typing.Any]]
            Configuration to use for the graph. Useful when graph is configurable and you want to update the assistant's configuration.

        context : typing.Optional[typing.Dict[str, typing.Any]]
            Static context added to the assistant.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to merge with existing assistant metadata.

        name : typing.Optional[str]
            The new name for the assistant. If not provided, assistant will keep its current name.

        description : typing.Optional[str]
            The new description for the assistant. If not provided, assistant will keep its current description.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Assistant]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"assistants/{encode_path_param(assistant_id)}",
            method="PATCH",
            json={
                "graph_id": graph_id,
                "config": config,
                "context": context,
                "metadata": metadata,
                "name": name,
                "description": description,
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
                    Assistant,
                    parse_obj_as(
                        type_=Assistant,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def get_assistant_graph(
        self,
        assistant_id: str,
        *,
        xray: typing.Optional[GetAssistantGraphAssistantsAssistantIdGraphGetRequestXray] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, typing.List[typing.Dict[str, typing.Any]]]]:
        """
        Get an assistant by ID.

        Parameters
        ----------
        assistant_id : str
            The ID of the assistant.

        xray : typing.Optional[GetAssistantGraphAssistantsAssistantIdGraphGetRequestXray]
            Include graph representation of subgraphs. If an integer value is provided, only subgraphs with a depth less than or equal to the value will be included.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.List[typing.Dict[str, typing.Any]]]]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"assistants/{encode_path_param(assistant_id)}/graph",
            method="GET",
            params={
                "xray": xray,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.List[typing.Dict[str, typing.Any]]],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.List[typing.Dict[str, typing.Any]]],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def get_assistant_subgraphs(
        self,
        assistant_id: str,
        namespace: str,
        *,
        recurse: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Subgraphs]:
        """
        Get an assistant's subgraphs filtered by namespace.

        Parameters
        ----------
        assistant_id : str
            The ID of the assistant.

        namespace : str
            Namespace of the subgraph to filter by.

        recurse : typing.Optional[bool]
            Recursively retrieve subgraphs of subgraphs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Subgraphs]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"assistants/{encode_path_param(assistant_id)}/subgraphs/{encode_path_param(namespace)}",
            method="GET",
            params={
                "recurse": recurse,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Subgraphs,
                    parse_obj_as(
                        type_=Subgraphs,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def get_assistant_schemas(
        self, assistant_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GraphSchema]:
        """
        Get an assistant by ID.

        Parameters
        ----------
        assistant_id : str
            The ID of the assistant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GraphSchema]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"assistants/{encode_path_param(assistant_id)}/schemas",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GraphSchema,
                    parse_obj_as(
                        type_=GraphSchema,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def get_assistant_versions_assistants_assistant_id_versions_get(
        self, assistant_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[Assistant]]:
        """
        Get all versions of an assistant.

        Parameters
        ----------
        assistant_id : str
            The ID of the assistant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Assistant]]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"assistants/{encode_path_param(assistant_id)}/versions",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Assistant],
                    parse_obj_as(
                        type_=typing.List[Assistant],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def set_latest_assistant_version_assistants_assistant_id_versions_post(
        self, assistant_id: str, *, version: int, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Assistant]:
        """
        Set the latest version for an assistant.

        Parameters
        ----------
        assistant_id : str
            The ID of the assistant.

        version : int
            The version to change to.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Assistant]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"assistants/{encode_path_param(assistant_id)}/latest",
            method="POST",
            params={
                "version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Assistant,
                    parse_obj_as(
                        type_=Assistant,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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


class AsyncRawAssistantsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_assistant(
        self,
        *,
        graph_id: str,
        assistant_id: typing.Optional[str] = OMIT,
        config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        context: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        if_exists: typing.Optional[AssistantCreateIfExists] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Assistant]:
        """
        Create an assistant.

        An initial version of the assistant will be created and the assistant is set to that version. To change versions, use the `POST /assistants/{assistant_id}/latest` endpoint.

        Parameters
        ----------
        graph_id : str
            The ID of the graph the assistant should use. The graph ID is normally set in your langgraph.json configuration.

        assistant_id : typing.Optional[str]
            The ID of the assistant. If not provided, a random UUID will be generated.

        config : typing.Optional[typing.Dict[str, typing.Any]]
            Configuration to use for the graph. Useful when graph is configurable and you want to create different assistants based on different configurations.

        context : typing.Optional[typing.Dict[str, typing.Any]]
            Static context added to the assistant.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to add to assistant.

        if_exists : typing.Optional[AssistantCreateIfExists]
            How to handle duplicate creation. Must be either 'raise' (raise error if duplicate), or 'do_nothing' (return existing assistant).

        name : typing.Optional[str]
            The name of the assistant. Defaults to 'Untitled'.

        description : typing.Optional[str]
            The description of the assistant. Defaults to null.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Assistant]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "assistants",
            method="POST",
            json={
                "assistant_id": assistant_id,
                "graph_id": graph_id,
                "config": config,
                "context": context,
                "metadata": metadata,
                "if_exists": if_exists,
                "name": name,
                "description": description,
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
                    Assistant,
                    parse_obj_as(
                        type_=Assistant,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def search_assistants(
        self,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        graph_id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        sort_by: typing.Optional[AssistantSearchRequestSortBy] = OMIT,
        sort_order: typing.Optional[AssistantSearchRequestSortOrder] = OMIT,
        select: typing.Optional[typing.Sequence[AssistantSearchRequestSelectItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Assistant]]:
        """
        Search for assistants.

        This endpoint also functions as the endpoint to list all assistants.

        Parameters
        ----------
        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to filter by. Exact match filter for each KV pair.

        graph_id : typing.Optional[str]
            The ID of the graph to filter by. The graph ID is normally set in your langgraph.json configuration.

        name : typing.Optional[str]
            Name of the assistant to filter by. The filtering logic will match (case insensitive) assistants where 'name' is a substring of the assistant name.

        limit : typing.Optional[int]
            The maximum number of results to return.

        offset : typing.Optional[int]
            The number of results to skip.

        sort_by : typing.Optional[AssistantSearchRequestSortBy]
            The field to sort by.

        sort_order : typing.Optional[AssistantSearchRequestSortOrder]
            The order to sort by.

        select : typing.Optional[typing.Sequence[AssistantSearchRequestSelectItem]]
            Specify which fields to return. If not provided, all fields are returned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Assistant]]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "assistants/search",
            method="POST",
            json={
                "metadata": metadata,
                "graph_id": graph_id,
                "name": name,
                "limit": limit,
                "offset": offset,
                "sort_by": sort_by,
                "sort_order": sort_order,
                "select": select,
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
                    typing.List[Assistant],
                    parse_obj_as(
                        type_=typing.List[Assistant],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def count_assistants(
        self,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        graph_id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[int]:
        """
        Get the count of assistants matching the specified criteria.

        Parameters
        ----------
        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to filter by. Exact match filter for each KV pair.

        graph_id : typing.Optional[str]
            The ID of the graph to filter by. The graph ID is normally set in your langgraph.json configuration.

        name : typing.Optional[str]
            Name of the assistant to filter by. The filtering logic will match (case insensitive) assistants where 'name' is a substring of the assistant name.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[int]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "assistants/count",
            method="POST",
            json={
                "metadata": metadata,
                "graph_id": graph_id,
                "name": name,
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
                    int,
                    parse_obj_as(
                        type_=int,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def get_assistant(
        self, assistant_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Assistant]:
        """
        Get an assistant by ID.

        Parameters
        ----------
        assistant_id : str
            The ID of the assistant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Assistant]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"assistants/{encode_path_param(assistant_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Assistant,
                    parse_obj_as(
                        type_=Assistant,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def delete_assistant(
        self,
        assistant_id: str,
        *,
        delete_threads: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Delete an assistant by ID.

        All versions of the assistant will be deleted as well.

        Parameters
        ----------
        assistant_id : str
            The ID of the assistant.

        delete_threads : typing.Optional[bool]
            If true, delete all threads with metadata.assistant_id matching this assistant, along with runs and checkpoints belonging to those threads. Auth filters are applied, so threads not visible to the user will not be deleted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"assistants/{encode_path_param(assistant_id)}",
            method="DELETE",
            params={
                "delete_threads": delete_threads,
            },
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def patch_assistant(
        self,
        assistant_id: str,
        *,
        graph_id: typing.Optional[str] = OMIT,
        config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        context: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Assistant]:
        """
        Update an assistant.

        Parameters
        ----------
        assistant_id : str
            The ID of the assistant.

        graph_id : typing.Optional[str]
            The ID of the graph the assistant should use. The graph ID is normally set in your langgraph.json configuration. If not provided, assistant will keep pointing to same graph.

        config : typing.Optional[typing.Dict[str, typing.Any]]
            Configuration to use for the graph. Useful when graph is configurable and you want to update the assistant's configuration.

        context : typing.Optional[typing.Dict[str, typing.Any]]
            Static context added to the assistant.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to merge with existing assistant metadata.

        name : typing.Optional[str]
            The new name for the assistant. If not provided, assistant will keep its current name.

        description : typing.Optional[str]
            The new description for the assistant. If not provided, assistant will keep its current description.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Assistant]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"assistants/{encode_path_param(assistant_id)}",
            method="PATCH",
            json={
                "graph_id": graph_id,
                "config": config,
                "context": context,
                "metadata": metadata,
                "name": name,
                "description": description,
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
                    Assistant,
                    parse_obj_as(
                        type_=Assistant,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def get_assistant_graph(
        self,
        assistant_id: str,
        *,
        xray: typing.Optional[GetAssistantGraphAssistantsAssistantIdGraphGetRequestXray] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, typing.List[typing.Dict[str, typing.Any]]]]:
        """
        Get an assistant by ID.

        Parameters
        ----------
        assistant_id : str
            The ID of the assistant.

        xray : typing.Optional[GetAssistantGraphAssistantsAssistantIdGraphGetRequestXray]
            Include graph representation of subgraphs. If an integer value is provided, only subgraphs with a depth less than or equal to the value will be included.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.List[typing.Dict[str, typing.Any]]]]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"assistants/{encode_path_param(assistant_id)}/graph",
            method="GET",
            params={
                "xray": xray,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.List[typing.Dict[str, typing.Any]]],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.List[typing.Dict[str, typing.Any]]],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def get_assistant_subgraphs(
        self,
        assistant_id: str,
        namespace: str,
        *,
        recurse: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Subgraphs]:
        """
        Get an assistant's subgraphs filtered by namespace.

        Parameters
        ----------
        assistant_id : str
            The ID of the assistant.

        namespace : str
            Namespace of the subgraph to filter by.

        recurse : typing.Optional[bool]
            Recursively retrieve subgraphs of subgraphs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Subgraphs]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"assistants/{encode_path_param(assistant_id)}/subgraphs/{encode_path_param(namespace)}",
            method="GET",
            params={
                "recurse": recurse,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Subgraphs,
                    parse_obj_as(
                        type_=Subgraphs,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def get_assistant_schemas(
        self, assistant_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GraphSchema]:
        """
        Get an assistant by ID.

        Parameters
        ----------
        assistant_id : str
            The ID of the assistant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GraphSchema]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"assistants/{encode_path_param(assistant_id)}/schemas",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GraphSchema,
                    parse_obj_as(
                        type_=GraphSchema,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def get_assistant_versions_assistants_assistant_id_versions_get(
        self, assistant_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[Assistant]]:
        """
        Get all versions of an assistant.

        Parameters
        ----------
        assistant_id : str
            The ID of the assistant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Assistant]]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"assistants/{encode_path_param(assistant_id)}/versions",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Assistant],
                    parse_obj_as(
                        type_=typing.List[Assistant],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def set_latest_assistant_version_assistants_assistant_id_versions_post(
        self, assistant_id: str, *, version: int, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Assistant]:
        """
        Set the latest version for an assistant.

        Parameters
        ----------
        assistant_id : str
            The ID of the assistant.

        version : int
            The version to change to.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Assistant]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"assistants/{encode_path_param(assistant_id)}/latest",
            method="POST",
            params={
                "version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Assistant,
                    parse_obj_as(
                        type_=Assistant,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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



import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.agent_state import AgentState
from ..types.archive import Archive
from ..types.embedding_config import EmbeddingConfig
from ..types.http_validation_error import HttpValidationError
from ..types.passage import Passage
from .types.list_agents_for_archive_request_include_item import ListAgentsForArchiveRequestIncludeItem
from .types.list_agents_for_archive_request_order import ListAgentsForArchiveRequestOrder
from .types.list_archives_request_order import ListArchivesRequestOrder
from .types.list_archives_request_order_by import ListArchivesRequestOrderBy
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawArchivesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_archives(
        self,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListArchivesRequestOrder] = None,
        order_by: typing.Optional[ListArchivesRequestOrderBy] = None,
        name: typing.Optional[str] = None,
        agent_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Archive]]:
        """
        Get a list of all archives for the current organization with optional filters and pagination.

        Parameters
        ----------
        before : typing.Optional[str]
            Archive ID cursor for pagination. Returns archives that come before this archive ID in the specified sort order

        after : typing.Optional[str]
            Archive ID cursor for pagination. Returns archives that come after this archive ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of archives to return

        order : typing.Optional[ListArchivesRequestOrder]
            Sort order for archives by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListArchivesRequestOrderBy]
            Field to sort by

        name : typing.Optional[str]
            Filter by archive name (exact match)

        agent_id : typing.Optional[str]
            Only archives attached to this agent ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Archive]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/archives/",
            method="GET",
            params={
                "before": before,
                "after": after,
                "limit": limit,
                "order": order,
                "order_by": order_by,
                "name": name,
                "agent_id": agent_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Archive],
                    parse_obj_as(
                        type_=typing.List[Archive],
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

    def create_archive(
        self,
        *,
        name: str,
        embedding_config: typing.Optional[EmbeddingConfig] = OMIT,
        embedding: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Archive]:
        """
        Create a new archive.

        Parameters
        ----------
        name : str

        embedding_config : typing.Optional[EmbeddingConfig]
            Deprecated: Use `embedding` field instead. Embedding configuration for the archive

        embedding : typing.Optional[str]
            Embedding model handle for the archive

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Archive]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/archives/",
            method="POST",
            json={
                "name": name,
                "embedding_config": convert_and_respect_annotation_metadata(
                    object_=embedding_config, annotation=typing.Optional[EmbeddingConfig], direction="write"
                ),
                "embedding": embedding,
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
                    Archive,
                    parse_obj_as(
                        type_=Archive,
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

    def retrieve_archive(
        self, archive_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Archive]:
        """
        Get a single archive by its ID.

        Parameters
        ----------
        archive_id : str
            The ID of the archive in the format 'archive-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Archive]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/archives/{encode_path_param(archive_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Archive,
                    parse_obj_as(
                        type_=Archive,
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

    def delete_archive(
        self, archive_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Delete an archive by its ID.

        Parameters
        ----------
        archive_id : str
            The ID of the archive in the format 'archive-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/archives/{encode_path_param(archive_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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

    def modify_archive(
        self,
        archive_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Archive]:
        """
        Update an existing archive's name and/or description.

        Parameters
        ----------
        archive_id : str
            The ID of the archive in the format 'archive-<uuid4>'

        name : typing.Optional[str]

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Archive]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/archives/{encode_path_param(archive_id)}",
            method="PATCH",
            json={
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
                    Archive,
                    parse_obj_as(
                        type_=Archive,
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

    def list_agents_for_archive(
        self,
        archive_id: str,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListAgentsForArchiveRequestOrder] = None,
        include: typing.Optional[
            typing.Union[
                ListAgentsForArchiveRequestIncludeItem, typing.Sequence[ListAgentsForArchiveRequestIncludeItem]
            ]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[AgentState]]:
        """
        Get a list of agents that have access to an archive with pagination support.

        Parameters
        ----------
        archive_id : str
            The ID of the archive in the format 'archive-<uuid4>'

        before : typing.Optional[str]
            Agent ID cursor for pagination. Returns agents that come before this agent ID in the specified sort order

        after : typing.Optional[str]
            Agent ID cursor for pagination. Returns agents that come after this agent ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of agents to return

        order : typing.Optional[ListAgentsForArchiveRequestOrder]
            Sort order for agents by creation time. 'asc' for oldest first, 'desc' for newest first

        include : typing.Optional[typing.Union[ListAgentsForArchiveRequestIncludeItem, typing.Sequence[ListAgentsForArchiveRequestIncludeItem]]]
            Specify which relational fields to include in the response. No relationships are included by default.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[AgentState]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/archives/{encode_path_param(archive_id)}/agents",
            method="GET",
            params={
                "before": before,
                "after": after,
                "limit": limit,
                "order": order,
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

    def create_passage_in_archive(
        self,
        archive_id: str,
        *,
        text: str,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Passage]:
        """
        Create a new passage in an archive.

        This adds a passage to the archive and creates embeddings for vector storage.

        Parameters
        ----------
        archive_id : str
            The ID of the archive in the format 'archive-<uuid4>'

        text : str
            The text content of the passage

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Optional metadata for the passage

        tags : typing.Optional[typing.Sequence[str]]
            Optional tags for categorizing the passage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Passage]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/archives/{encode_path_param(archive_id)}/passages",
            method="POST",
            json={
                "text": text,
                "metadata": metadata,
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
                    Passage,
                    parse_obj_as(
                        type_=Passage,
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

    def delete_passage_from_archive(
        self, archive_id: str, passage_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Delete a passage from an archive.

        This permanently removes the passage from both the database and vector storage (if applicable).

        Parameters
        ----------
        archive_id : str
            The ID of the archive in the format 'archive-<uuid4>'

        passage_id : str
            The ID of the passage in the format 'passage-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/archives/{encode_path_param(archive_id)}/passages/{encode_path_param(passage_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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


class AsyncRawArchivesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_archives(
        self,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListArchivesRequestOrder] = None,
        order_by: typing.Optional[ListArchivesRequestOrderBy] = None,
        name: typing.Optional[str] = None,
        agent_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Archive]]:
        """
        Get a list of all archives for the current organization with optional filters and pagination.

        Parameters
        ----------
        before : typing.Optional[str]
            Archive ID cursor for pagination. Returns archives that come before this archive ID in the specified sort order

        after : typing.Optional[str]
            Archive ID cursor for pagination. Returns archives that come after this archive ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of archives to return

        order : typing.Optional[ListArchivesRequestOrder]
            Sort order for archives by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListArchivesRequestOrderBy]
            Field to sort by

        name : typing.Optional[str]
            Filter by archive name (exact match)

        agent_id : typing.Optional[str]
            Only archives attached to this agent ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Archive]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/archives/",
            method="GET",
            params={
                "before": before,
                "after": after,
                "limit": limit,
                "order": order,
                "order_by": order_by,
                "name": name,
                "agent_id": agent_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Archive],
                    parse_obj_as(
                        type_=typing.List[Archive],
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

    async def create_archive(
        self,
        *,
        name: str,
        embedding_config: typing.Optional[EmbeddingConfig] = OMIT,
        embedding: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Archive]:
        """
        Create a new archive.

        Parameters
        ----------
        name : str

        embedding_config : typing.Optional[EmbeddingConfig]
            Deprecated: Use `embedding` field instead. Embedding configuration for the archive

        embedding : typing.Optional[str]
            Embedding model handle for the archive

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Archive]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/archives/",
            method="POST",
            json={
                "name": name,
                "embedding_config": convert_and_respect_annotation_metadata(
                    object_=embedding_config, annotation=typing.Optional[EmbeddingConfig], direction="write"
                ),
                "embedding": embedding,
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
                    Archive,
                    parse_obj_as(
                        type_=Archive,
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

    async def retrieve_archive(
        self, archive_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Archive]:
        """
        Get a single archive by its ID.

        Parameters
        ----------
        archive_id : str
            The ID of the archive in the format 'archive-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Archive]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/archives/{encode_path_param(archive_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Archive,
                    parse_obj_as(
                        type_=Archive,
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

    async def delete_archive(
        self, archive_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Delete an archive by its ID.

        Parameters
        ----------
        archive_id : str
            The ID of the archive in the format 'archive-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/archives/{encode_path_param(archive_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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

    async def modify_archive(
        self,
        archive_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Archive]:
        """
        Update an existing archive's name and/or description.

        Parameters
        ----------
        archive_id : str
            The ID of the archive in the format 'archive-<uuid4>'

        name : typing.Optional[str]

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Archive]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/archives/{encode_path_param(archive_id)}",
            method="PATCH",
            json={
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
                    Archive,
                    parse_obj_as(
                        type_=Archive,
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

    async def list_agents_for_archive(
        self,
        archive_id: str,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListAgentsForArchiveRequestOrder] = None,
        include: typing.Optional[
            typing.Union[
                ListAgentsForArchiveRequestIncludeItem, typing.Sequence[ListAgentsForArchiveRequestIncludeItem]
            ]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[AgentState]]:
        """
        Get a list of agents that have access to an archive with pagination support.

        Parameters
        ----------
        archive_id : str
            The ID of the archive in the format 'archive-<uuid4>'

        before : typing.Optional[str]
            Agent ID cursor for pagination. Returns agents that come before this agent ID in the specified sort order

        after : typing.Optional[str]
            Agent ID cursor for pagination. Returns agents that come after this agent ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of agents to return

        order : typing.Optional[ListAgentsForArchiveRequestOrder]
            Sort order for agents by creation time. 'asc' for oldest first, 'desc' for newest first

        include : typing.Optional[typing.Union[ListAgentsForArchiveRequestIncludeItem, typing.Sequence[ListAgentsForArchiveRequestIncludeItem]]]
            Specify which relational fields to include in the response. No relationships are included by default.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[AgentState]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/archives/{encode_path_param(archive_id)}/agents",
            method="GET",
            params={
                "before": before,
                "after": after,
                "limit": limit,
                "order": order,
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

    async def create_passage_in_archive(
        self,
        archive_id: str,
        *,
        text: str,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Passage]:
        """
        Create a new passage in an archive.

        This adds a passage to the archive and creates embeddings for vector storage.

        Parameters
        ----------
        archive_id : str
            The ID of the archive in the format 'archive-<uuid4>'

        text : str
            The text content of the passage

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Optional metadata for the passage

        tags : typing.Optional[typing.Sequence[str]]
            Optional tags for categorizing the passage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Passage]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/archives/{encode_path_param(archive_id)}/passages",
            method="POST",
            json={
                "text": text,
                "metadata": metadata,
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
                    Passage,
                    parse_obj_as(
                        type_=Passage,
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

    async def delete_passage_from_archive(
        self, archive_id: str, passage_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Delete a passage from an archive.

        This permanently removes the passage from both the database and vector storage (if applicable).

        Parameters
        ----------
        archive_id : str
            The ID of the archive in the format 'archive-<uuid4>'

        passage_id : str
            The ID of the passage in the format 'passage-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/archives/{encode_path_param(archive_id)}/passages/{encode_path_param(passage_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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

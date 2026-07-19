

import typing
from json.decoder import JSONDecodeError

from .. import core
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.duplicate_file_handling import DuplicateFileHandling
from ..types.embedding_config import EmbeddingConfig
from ..types.file_metadata import FileMetadata
from ..types.folder import Folder
from ..types.http_validation_error import HttpValidationError
from ..types.organization_sources_stats import OrganizationSourcesStats
from ..types.passage import Passage
from .types.list_agents_for_folder_request_order import ListAgentsForFolderRequestOrder
from .types.list_agents_for_folder_request_order_by import ListAgentsForFolderRequestOrderBy
from .types.list_files_for_folder_request_order import ListFilesForFolderRequestOrder
from .types.list_files_for_folder_request_order_by import ListFilesForFolderRequestOrderBy
from .types.list_folder_passages_request_order import ListFolderPassagesRequestOrder
from .types.list_folder_passages_request_order_by import ListFolderPassagesRequestOrderBy
from .types.list_folders_request_order import ListFoldersRequestOrder
from .types.list_folders_request_order_by import ListFoldersRequestOrderBy
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFoldersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def count_folders(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[int]:
        """
        Count all data folders created by a user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[int]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/folders/count",
            method="GET",
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

    def retrieve_folder(
        self, folder_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Folder]:
        """
        Get a folder by ID

        Parameters
        ----------
        folder_id : str
            The ID of the source in the format 'source-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Folder]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/folders/{encode_path_param(folder_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Folder,
                    parse_obj_as(
                        type_=Folder,
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

    def delete_folder(
        self, folder_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Any]:
        """
        Delete a data folder.

        Parameters
        ----------
        folder_id : str
            The ID of the source in the format 'source-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/folders/{encode_path_param(folder_id)}",
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

    def modify_folder(
        self,
        folder_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        instructions: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        embedding_config: typing.Optional[EmbeddingConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Folder]:
        """
        Update the name or documentation of an existing data folder.

        Parameters
        ----------
        folder_id : str
            The ID of the source in the format 'source-<uuid4>'

        name : typing.Optional[str]
            The name of the source.

        description : typing.Optional[str]
            The description of the source.

        instructions : typing.Optional[str]
            Instructions for how to use the source.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata associated with the source.

        embedding_config : typing.Optional[EmbeddingConfig]
            The embedding configuration used by the source.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Folder]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/folders/{encode_path_param(folder_id)}",
            method="PATCH",
            json={
                "name": name,
                "description": description,
                "instructions": instructions,
                "metadata": metadata,
                "embedding_config": convert_and_respect_annotation_metadata(
                    object_=embedding_config, annotation=typing.Optional[EmbeddingConfig], direction="write"
                ),
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
                    Folder,
                    parse_obj_as(
                        type_=Folder,
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

    def get_folder_by_name(
        self, folder_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[str]:
        """
        **Deprecated**: Please use the list endpoint `GET /v1/folders?name=` instead.


        Get a folder by name.

        Parameters
        ----------
        folder_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/folders/name/{encode_path_param(folder_name)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_=str,
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

    def retrieve_metadata(
        self,
        *,
        include_detailed_per_source_metadata: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[OrganizationSourcesStats]:
        """
        Get aggregated metadata for all folders in an organization.

        Returns structured metadata including:
        - Total number of folders
        - Total number of files across all folders
        - Total size of all files
        - Per-source breakdown with file details (file_name, file_size per file) if include_detailed_per_source_metadata is True

        Parameters
        ----------
        include_detailed_per_source_metadata : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OrganizationSourcesStats]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/folders/metadata",
            method="GET",
            params={
                "include_detailed_per_source_metadata": include_detailed_per_source_metadata,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OrganizationSourcesStats,
                    parse_obj_as(
                        type_=OrganizationSourcesStats,
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

    def list_folders(
        self,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListFoldersRequestOrder] = None,
        order_by: typing.Optional[ListFoldersRequestOrderBy] = None,
        name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Folder]]:
        """
        List all data folders created by a user.

        Parameters
        ----------
        before : typing.Optional[str]
            Folder ID cursor for pagination. Returns folders that come before this folder ID in the specified sort order

        after : typing.Optional[str]
            Folder ID cursor for pagination. Returns folders that come after this folder ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of folders to return

        order : typing.Optional[ListFoldersRequestOrder]
            Sort order for folders by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListFoldersRequestOrderBy]
            Field to sort by

        name : typing.Optional[str]
            Folder name to filter by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Folder]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/folders/",
            method="GET",
            params={
                "before": before,
                "after": after,
                "limit": limit,
                "order": order,
                "order_by": order_by,
                "name": name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Folder],
                    parse_obj_as(
                        type_=typing.List[Folder],
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

    def create_folder(
        self,
        *,
        name: str,
        description: typing.Optional[str] = OMIT,
        instructions: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        embedding: typing.Optional[str] = OMIT,
        embedding_chunk_size: typing.Optional[int] = OMIT,
        embedding_config: typing.Optional[EmbeddingConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Folder]:
        """
        Create a new data folder.

        Parameters
        ----------
        name : str
            The name of the source.

        description : typing.Optional[str]
            The description of the source.

        instructions : typing.Optional[str]
            Instructions for how to use the source.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata associated with the source.

        embedding : typing.Optional[str]
            The handle for the embedding config used by the source.

        embedding_chunk_size : typing.Optional[int]
            The chunk size of the embedding.

        embedding_config : typing.Optional[EmbeddingConfig]
            (Legacy) The embedding configuration used by the source.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Folder]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/folders/",
            method="POST",
            json={
                "name": name,
                "description": description,
                "instructions": instructions,
                "metadata": metadata,
                "embedding": embedding,
                "embedding_chunk_size": embedding_chunk_size,
                "embedding_config": convert_and_respect_annotation_metadata(
                    object_=embedding_config, annotation=typing.Optional[EmbeddingConfig], direction="write"
                ),
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
                    Folder,
                    parse_obj_as(
                        type_=Folder,
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

    def upload_file_to_folder(
        self,
        folder_id: str,
        *,
        file: core.File,
        duplicate_handling: typing.Optional[DuplicateFileHandling] = None,
        name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FileMetadata]:
        """
        Upload a file to a data folder.

        Parameters
        ----------
        folder_id : str
            The ID of the source in the format 'source-<uuid4>'

        file : core.File
            See core.File for more documentation

        duplicate_handling : typing.Optional[DuplicateFileHandling]
            How to handle duplicate filenames

        name : typing.Optional[str]
            Optional custom name to override the uploaded file's name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FileMetadata]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/folders/{encode_path_param(folder_id)}/upload",
            method="POST",
            params={
                "duplicate_handling": duplicate_handling,
                "name": name,
            },
            data={},
            files={
                "file": file,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FileMetadata,
                    parse_obj_as(
                        type_=FileMetadata,
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

    def list_agents_for_folder(
        self,
        folder_id: str,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListAgentsForFolderRequestOrder] = None,
        order_by: typing.Optional[ListAgentsForFolderRequestOrderBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[str]]:
        """
        Get all agent IDs that have the specified folder attached.

        Parameters
        ----------
        folder_id : str
            The ID of the source in the format 'source-<uuid4>'

        before : typing.Optional[str]
            Agent ID cursor for pagination. Returns agents that come before this agent ID in the specified sort order

        after : typing.Optional[str]
            Agent ID cursor for pagination. Returns agents that come after this agent ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of agents to return

        order : typing.Optional[ListAgentsForFolderRequestOrder]
            Sort order for agents by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListAgentsForFolderRequestOrderBy]
            Field to sort by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[str]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/folders/{encode_path_param(folder_id)}/agents",
            method="GET",
            params={
                "before": before,
                "after": after,
                "limit": limit,
                "order": order,
                "order_by": order_by,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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

    def list_folder_passages(
        self,
        folder_id: str,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListFolderPassagesRequestOrder] = None,
        order_by: typing.Optional[ListFolderPassagesRequestOrderBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Passage]]:
        """
        List all passages associated with a data folder.

        Parameters
        ----------
        folder_id : str
            The ID of the source in the format 'source-<uuid4>'

        before : typing.Optional[str]
            Passage ID cursor for pagination. Returns passages that come before this passage ID in the specified sort order

        after : typing.Optional[str]
            Passage ID cursor for pagination. Returns passages that come after this passage ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of passages to return

        order : typing.Optional[ListFolderPassagesRequestOrder]
            Sort order for passages by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListFolderPassagesRequestOrderBy]
            Field to sort by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Passage]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/folders/{encode_path_param(folder_id)}/passages",
            method="GET",
            params={
                "before": before,
                "after": after,
                "limit": limit,
                "order": order,
                "order_by": order_by,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Passage],
                    parse_obj_as(
                        type_=typing.List[Passage],
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

    def list_files_for_folder(
        self,
        folder_id: str,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListFilesForFolderRequestOrder] = None,
        order_by: typing.Optional[ListFilesForFolderRequestOrderBy] = None,
        include_content: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[FileMetadata]]:
        """
        List paginated files associated with a data folder.

        Parameters
        ----------
        folder_id : str
            The ID of the source in the format 'source-<uuid4>'

        before : typing.Optional[str]
            File ID cursor for pagination. Returns files that come before this file ID in the specified sort order

        after : typing.Optional[str]
            File ID cursor for pagination. Returns files that come after this file ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of files to return

        order : typing.Optional[ListFilesForFolderRequestOrder]
            Sort order for files by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListFilesForFolderRequestOrderBy]
            Field to sort by

        include_content : typing.Optional[bool]
            Whether to include full file content

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[FileMetadata]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/folders/{encode_path_param(folder_id)}/files",
            method="GET",
            params={
                "before": before,
                "after": after,
                "limit": limit,
                "order": order,
                "order_by": order_by,
                "include_content": include_content,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[FileMetadata],
                    parse_obj_as(
                        type_=typing.List[FileMetadata],
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

    def retrieve_file(
        self,
        folder_id: str,
        file_id: str,
        *,
        include_content: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FileMetadata]:
        """
        Retrieve a file from a folder by ID.

        Parameters
        ----------
        folder_id : str
            The ID of the source in the format 'source-<uuid4>'

        file_id : str
            The ID of the file in the format 'file-<uuid4>'

        include_content : typing.Optional[bool]
            Whether to include full file content

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FileMetadata]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/folders/{encode_path_param(folder_id)}/files/{encode_path_param(file_id)}",
            method="GET",
            params={
                "include_content": include_content,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FileMetadata,
                    parse_obj_as(
                        type_=FileMetadata,
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

    def delete_file_from_folder(
        self, folder_id: str, file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Delete a file from a folder.

        Parameters
        ----------
        folder_id : str
            The ID of the source in the format 'source-<uuid4>'

        file_id : str
            The ID of the file in the format 'file-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/folders/{encode_path_param(folder_id)}/{encode_path_param(file_id)}",
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


class AsyncRawFoldersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def count_folders(self, *, request_options: typing.Optional[RequestOptions] = None) -> AsyncHttpResponse[int]:
        """
        Count all data folders created by a user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[int]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/folders/count",
            method="GET",
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

    async def retrieve_folder(
        self, folder_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Folder]:
        """
        Get a folder by ID

        Parameters
        ----------
        folder_id : str
            The ID of the source in the format 'source-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Folder]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/folders/{encode_path_param(folder_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Folder,
                    parse_obj_as(
                        type_=Folder,
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

    async def delete_folder(
        self, folder_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Delete a data folder.

        Parameters
        ----------
        folder_id : str
            The ID of the source in the format 'source-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/folders/{encode_path_param(folder_id)}",
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

    async def modify_folder(
        self,
        folder_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        instructions: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        embedding_config: typing.Optional[EmbeddingConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Folder]:
        """
        Update the name or documentation of an existing data folder.

        Parameters
        ----------
        folder_id : str
            The ID of the source in the format 'source-<uuid4>'

        name : typing.Optional[str]
            The name of the source.

        description : typing.Optional[str]
            The description of the source.

        instructions : typing.Optional[str]
            Instructions for how to use the source.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata associated with the source.

        embedding_config : typing.Optional[EmbeddingConfig]
            The embedding configuration used by the source.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Folder]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/folders/{encode_path_param(folder_id)}",
            method="PATCH",
            json={
                "name": name,
                "description": description,
                "instructions": instructions,
                "metadata": metadata,
                "embedding_config": convert_and_respect_annotation_metadata(
                    object_=embedding_config, annotation=typing.Optional[EmbeddingConfig], direction="write"
                ),
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
                    Folder,
                    parse_obj_as(
                        type_=Folder,
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

    async def get_folder_by_name(
        self, folder_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[str]:
        """
        **Deprecated**: Please use the list endpoint `GET /v1/folders?name=` instead.


        Get a folder by name.

        Parameters
        ----------
        folder_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/folders/name/{encode_path_param(folder_name)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_=str,
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

    async def retrieve_metadata(
        self,
        *,
        include_detailed_per_source_metadata: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[OrganizationSourcesStats]:
        """
        Get aggregated metadata for all folders in an organization.

        Returns structured metadata including:
        - Total number of folders
        - Total number of files across all folders
        - Total size of all files
        - Per-source breakdown with file details (file_name, file_size per file) if include_detailed_per_source_metadata is True

        Parameters
        ----------
        include_detailed_per_source_metadata : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OrganizationSourcesStats]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/folders/metadata",
            method="GET",
            params={
                "include_detailed_per_source_metadata": include_detailed_per_source_metadata,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OrganizationSourcesStats,
                    parse_obj_as(
                        type_=OrganizationSourcesStats,
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

    async def list_folders(
        self,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListFoldersRequestOrder] = None,
        order_by: typing.Optional[ListFoldersRequestOrderBy] = None,
        name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Folder]]:
        """
        List all data folders created by a user.

        Parameters
        ----------
        before : typing.Optional[str]
            Folder ID cursor for pagination. Returns folders that come before this folder ID in the specified sort order

        after : typing.Optional[str]
            Folder ID cursor for pagination. Returns folders that come after this folder ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of folders to return

        order : typing.Optional[ListFoldersRequestOrder]
            Sort order for folders by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListFoldersRequestOrderBy]
            Field to sort by

        name : typing.Optional[str]
            Folder name to filter by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Folder]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/folders/",
            method="GET",
            params={
                "before": before,
                "after": after,
                "limit": limit,
                "order": order,
                "order_by": order_by,
                "name": name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Folder],
                    parse_obj_as(
                        type_=typing.List[Folder],
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

    async def create_folder(
        self,
        *,
        name: str,
        description: typing.Optional[str] = OMIT,
        instructions: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        embedding: typing.Optional[str] = OMIT,
        embedding_chunk_size: typing.Optional[int] = OMIT,
        embedding_config: typing.Optional[EmbeddingConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Folder]:
        """
        Create a new data folder.

        Parameters
        ----------
        name : str
            The name of the source.

        description : typing.Optional[str]
            The description of the source.

        instructions : typing.Optional[str]
            Instructions for how to use the source.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata associated with the source.

        embedding : typing.Optional[str]
            The handle for the embedding config used by the source.

        embedding_chunk_size : typing.Optional[int]
            The chunk size of the embedding.

        embedding_config : typing.Optional[EmbeddingConfig]
            (Legacy) The embedding configuration used by the source.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Folder]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/folders/",
            method="POST",
            json={
                "name": name,
                "description": description,
                "instructions": instructions,
                "metadata": metadata,
                "embedding": embedding,
                "embedding_chunk_size": embedding_chunk_size,
                "embedding_config": convert_and_respect_annotation_metadata(
                    object_=embedding_config, annotation=typing.Optional[EmbeddingConfig], direction="write"
                ),
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
                    Folder,
                    parse_obj_as(
                        type_=Folder,
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

    async def upload_file_to_folder(
        self,
        folder_id: str,
        *,
        file: core.File,
        duplicate_handling: typing.Optional[DuplicateFileHandling] = None,
        name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FileMetadata]:
        """
        Upload a file to a data folder.

        Parameters
        ----------
        folder_id : str
            The ID of the source in the format 'source-<uuid4>'

        file : core.File
            See core.File for more documentation

        duplicate_handling : typing.Optional[DuplicateFileHandling]
            How to handle duplicate filenames

        name : typing.Optional[str]
            Optional custom name to override the uploaded file's name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FileMetadata]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/folders/{encode_path_param(folder_id)}/upload",
            method="POST",
            params={
                "duplicate_handling": duplicate_handling,
                "name": name,
            },
            data={},
            files={
                "file": file,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FileMetadata,
                    parse_obj_as(
                        type_=FileMetadata,
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

    async def list_agents_for_folder(
        self,
        folder_id: str,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListAgentsForFolderRequestOrder] = None,
        order_by: typing.Optional[ListAgentsForFolderRequestOrderBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[str]]:
        """
        Get all agent IDs that have the specified folder attached.

        Parameters
        ----------
        folder_id : str
            The ID of the source in the format 'source-<uuid4>'

        before : typing.Optional[str]
            Agent ID cursor for pagination. Returns agents that come before this agent ID in the specified sort order

        after : typing.Optional[str]
            Agent ID cursor for pagination. Returns agents that come after this agent ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of agents to return

        order : typing.Optional[ListAgentsForFolderRequestOrder]
            Sort order for agents by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListAgentsForFolderRequestOrderBy]
            Field to sort by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[str]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/folders/{encode_path_param(folder_id)}/agents",
            method="GET",
            params={
                "before": before,
                "after": after,
                "limit": limit,
                "order": order,
                "order_by": order_by,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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

    async def list_folder_passages(
        self,
        folder_id: str,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListFolderPassagesRequestOrder] = None,
        order_by: typing.Optional[ListFolderPassagesRequestOrderBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Passage]]:
        """
        List all passages associated with a data folder.

        Parameters
        ----------
        folder_id : str
            The ID of the source in the format 'source-<uuid4>'

        before : typing.Optional[str]
            Passage ID cursor for pagination. Returns passages that come before this passage ID in the specified sort order

        after : typing.Optional[str]
            Passage ID cursor for pagination. Returns passages that come after this passage ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of passages to return

        order : typing.Optional[ListFolderPassagesRequestOrder]
            Sort order for passages by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListFolderPassagesRequestOrderBy]
            Field to sort by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Passage]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/folders/{encode_path_param(folder_id)}/passages",
            method="GET",
            params={
                "before": before,
                "after": after,
                "limit": limit,
                "order": order,
                "order_by": order_by,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Passage],
                    parse_obj_as(
                        type_=typing.List[Passage],
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

    async def list_files_for_folder(
        self,
        folder_id: str,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListFilesForFolderRequestOrder] = None,
        order_by: typing.Optional[ListFilesForFolderRequestOrderBy] = None,
        include_content: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[FileMetadata]]:
        """
        List paginated files associated with a data folder.

        Parameters
        ----------
        folder_id : str
            The ID of the source in the format 'source-<uuid4>'

        before : typing.Optional[str]
            File ID cursor for pagination. Returns files that come before this file ID in the specified sort order

        after : typing.Optional[str]
            File ID cursor for pagination. Returns files that come after this file ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of files to return

        order : typing.Optional[ListFilesForFolderRequestOrder]
            Sort order for files by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListFilesForFolderRequestOrderBy]
            Field to sort by

        include_content : typing.Optional[bool]
            Whether to include full file content

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[FileMetadata]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/folders/{encode_path_param(folder_id)}/files",
            method="GET",
            params={
                "before": before,
                "after": after,
                "limit": limit,
                "order": order,
                "order_by": order_by,
                "include_content": include_content,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[FileMetadata],
                    parse_obj_as(
                        type_=typing.List[FileMetadata],
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

    async def retrieve_file(
        self,
        folder_id: str,
        file_id: str,
        *,
        include_content: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FileMetadata]:
        """
        Retrieve a file from a folder by ID.

        Parameters
        ----------
        folder_id : str
            The ID of the source in the format 'source-<uuid4>'

        file_id : str
            The ID of the file in the format 'file-<uuid4>'

        include_content : typing.Optional[bool]
            Whether to include full file content

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FileMetadata]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/folders/{encode_path_param(folder_id)}/files/{encode_path_param(file_id)}",
            method="GET",
            params={
                "include_content": include_content,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FileMetadata,
                    parse_obj_as(
                        type_=FileMetadata,
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

    async def delete_file_from_folder(
        self, folder_id: str, file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Delete a file from a folder.

        Parameters
        ----------
        folder_id : str
            The ID of the source in the format 'source-<uuid4>'

        file_id : str
            The ID of the file in the format 'file-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/folders/{encode_path_param(folder_id)}/{encode_path_param(file_id)}",
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

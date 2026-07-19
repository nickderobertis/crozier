

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
from ..types.http_validation_error import HttpValidationError
from ..types.organization_sources_stats import OrganizationSourcesStats
from ..types.passage import Passage
from ..types.source import Source
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawSourcesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def count_sources(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[int]:
        """
        Count all data sources created by a user.

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
            "v1/sources/count",
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

    def retrieve_source(
        self, source_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Source]:
        """
        Get all sources

        Parameters
        ----------
        source_id : str
            The ID of the source in the format 'source-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Source]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/sources/{encode_path_param(source_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Source,
                    parse_obj_as(
                        type_=Source,
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

    def delete_source(
        self, source_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Any]:
        """
        Delete a data source.

        Parameters
        ----------
        source_id : str
            The ID of the source in the format 'source-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/sources/{encode_path_param(source_id)}",
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

    def modify_source(
        self,
        source_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        instructions: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        embedding_config: typing.Optional[EmbeddingConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Source]:
        """
        Update the name or documentation of an existing data source.

        Parameters
        ----------
        source_id : str
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
        HttpResponse[Source]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/sources/{encode_path_param(source_id)}",
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
                    Source,
                    parse_obj_as(
                        type_=Source,
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

    def get_source_id_by_name(
        self, source_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[str]:
        """
        Get a source by name

        Parameters
        ----------
        source_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/sources/name/{encode_path_param(source_name)}",
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

    def get_sources_metadata(
        self,
        *,
        include_detailed_per_source_metadata: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[OrganizationSourcesStats]:
        """
        Get aggregated metadata for all sources in an organization.

        Returns structured metadata including:
        - Total number of sources
        - Total number of files across all sources
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
            "v1/sources/metadata",
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

    def list_sources(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[Source]]:
        """
        List all data sources created by a user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Source]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/sources/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Source],
                    parse_obj_as(
                        type_=typing.List[Source],
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

    def create_source(
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
    ) -> HttpResponse[Source]:
        """
        Create a new data source.

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
        HttpResponse[Source]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/sources/",
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
                    Source,
                    parse_obj_as(
                        type_=Source,
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

    def upload_file_to_source(
        self,
        source_id: str,
        *,
        file: core.File,
        duplicate_handling: typing.Optional[DuplicateFileHandling] = None,
        name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FileMetadata]:
        """
        Upload a file to a data source.

        Parameters
        ----------
        source_id : str
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
            f"v1/sources/{encode_path_param(source_id)}/upload",
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

    def get_agents_for_source(
        self, source_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[str]]:
        """
        Get all agent IDs that have the specified source attached.

        Parameters
        ----------
        source_id : str
            The ID of the source in the format 'source-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[str]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/sources/{encode_path_param(source_id)}/agents",
            method="GET",
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

    def list_source_passages(
        self,
        source_id: str,
        *,
        after: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Passage]]:
        """
        List all passages associated with a data source.

        Parameters
        ----------
        source_id : str
            The ID of the source in the format 'source-<uuid4>'

        after : typing.Optional[str]
            Message after which to retrieve the returned messages.

        before : typing.Optional[str]
            Message before which to retrieve the returned messages.

        limit : typing.Optional[int]
            Maximum number of messages to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Passage]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/sources/{encode_path_param(source_id)}/passages",
            method="GET",
            params={
                "after": after,
                "before": before,
                "limit": limit,
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

    def list_source_files(
        self,
        source_id: str,
        *,
        limit: typing.Optional[int] = None,
        after: typing.Optional[str] = None,
        include_content: typing.Optional[bool] = None,
        check_status_updates: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[FileMetadata]]:
        """
        List paginated files associated with a data source.

        Parameters
        ----------
        source_id : str
            The ID of the source in the format 'source-<uuid4>'

        limit : typing.Optional[int]
            Number of files to return

        after : typing.Optional[str]
            Pagination cursor to fetch the next set of results

        include_content : typing.Optional[bool]
            Whether to include full file content

        check_status_updates : typing.Optional[bool]
            Whether to check and update file processing status (from the vector db service). If False, will not fetch and update the status, which may lead to performance gains.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[FileMetadata]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/sources/{encode_path_param(source_id)}/files",
            method="GET",
            params={
                "limit": limit,
                "after": after,
                "include_content": include_content,
                "check_status_updates": check_status_updates,
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

    def get_file_metadata(
        self,
        source_id: str,
        file_id: str,
        *,
        include_content: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FileMetadata]:
        """
        Retrieve metadata for a specific file by its ID.

        Parameters
        ----------
        source_id : str
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
            f"v1/sources/{encode_path_param(source_id)}/files/{encode_path_param(file_id)}",
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

    def delete_file_from_source(
        self, source_id: str, file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Delete a data source.

        Parameters
        ----------
        source_id : str
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
            f"v1/sources/{encode_path_param(source_id)}/{encode_path_param(file_id)}",
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


class AsyncRawSourcesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def count_sources(self, *, request_options: typing.Optional[RequestOptions] = None) -> AsyncHttpResponse[int]:
        """
        Count all data sources created by a user.

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
            "v1/sources/count",
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

    async def retrieve_source(
        self, source_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Source]:
        """
        Get all sources

        Parameters
        ----------
        source_id : str
            The ID of the source in the format 'source-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Source]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/sources/{encode_path_param(source_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Source,
                    parse_obj_as(
                        type_=Source,
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

    async def delete_source(
        self, source_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Delete a data source.

        Parameters
        ----------
        source_id : str
            The ID of the source in the format 'source-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/sources/{encode_path_param(source_id)}",
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

    async def modify_source(
        self,
        source_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        instructions: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        embedding_config: typing.Optional[EmbeddingConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Source]:
        """
        Update the name or documentation of an existing data source.

        Parameters
        ----------
        source_id : str
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
        AsyncHttpResponse[Source]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/sources/{encode_path_param(source_id)}",
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
                    Source,
                    parse_obj_as(
                        type_=Source,
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

    async def get_source_id_by_name(
        self, source_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[str]:
        """
        Get a source by name

        Parameters
        ----------
        source_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/sources/name/{encode_path_param(source_name)}",
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

    async def get_sources_metadata(
        self,
        *,
        include_detailed_per_source_metadata: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[OrganizationSourcesStats]:
        """
        Get aggregated metadata for all sources in an organization.

        Returns structured metadata including:
        - Total number of sources
        - Total number of files across all sources
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
            "v1/sources/metadata",
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

    async def list_sources(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[Source]]:
        """
        List all data sources created by a user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Source]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/sources/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Source],
                    parse_obj_as(
                        type_=typing.List[Source],
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

    async def create_source(
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
    ) -> AsyncHttpResponse[Source]:
        """
        Create a new data source.

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
        AsyncHttpResponse[Source]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/sources/",
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
                    Source,
                    parse_obj_as(
                        type_=Source,
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

    async def upload_file_to_source(
        self,
        source_id: str,
        *,
        file: core.File,
        duplicate_handling: typing.Optional[DuplicateFileHandling] = None,
        name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FileMetadata]:
        """
        Upload a file to a data source.

        Parameters
        ----------
        source_id : str
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
            f"v1/sources/{encode_path_param(source_id)}/upload",
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

    async def get_agents_for_source(
        self, source_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[str]]:
        """
        Get all agent IDs that have the specified source attached.

        Parameters
        ----------
        source_id : str
            The ID of the source in the format 'source-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[str]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/sources/{encode_path_param(source_id)}/agents",
            method="GET",
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

    async def list_source_passages(
        self,
        source_id: str,
        *,
        after: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Passage]]:
        """
        List all passages associated with a data source.

        Parameters
        ----------
        source_id : str
            The ID of the source in the format 'source-<uuid4>'

        after : typing.Optional[str]
            Message after which to retrieve the returned messages.

        before : typing.Optional[str]
            Message before which to retrieve the returned messages.

        limit : typing.Optional[int]
            Maximum number of messages to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Passage]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/sources/{encode_path_param(source_id)}/passages",
            method="GET",
            params={
                "after": after,
                "before": before,
                "limit": limit,
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

    async def list_source_files(
        self,
        source_id: str,
        *,
        limit: typing.Optional[int] = None,
        after: typing.Optional[str] = None,
        include_content: typing.Optional[bool] = None,
        check_status_updates: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[FileMetadata]]:
        """
        List paginated files associated with a data source.

        Parameters
        ----------
        source_id : str
            The ID of the source in the format 'source-<uuid4>'

        limit : typing.Optional[int]
            Number of files to return

        after : typing.Optional[str]
            Pagination cursor to fetch the next set of results

        include_content : typing.Optional[bool]
            Whether to include full file content

        check_status_updates : typing.Optional[bool]
            Whether to check and update file processing status (from the vector db service). If False, will not fetch and update the status, which may lead to performance gains.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[FileMetadata]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/sources/{encode_path_param(source_id)}/files",
            method="GET",
            params={
                "limit": limit,
                "after": after,
                "include_content": include_content,
                "check_status_updates": check_status_updates,
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

    async def get_file_metadata(
        self,
        source_id: str,
        file_id: str,
        *,
        include_content: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FileMetadata]:
        """
        Retrieve metadata for a specific file by its ID.

        Parameters
        ----------
        source_id : str
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
            f"v1/sources/{encode_path_param(source_id)}/files/{encode_path_param(file_id)}",
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

    async def delete_file_from_source(
        self, source_id: str, file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Delete a data source.

        Parameters
        ----------
        source_id : str
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
            f"v1/sources/{encode_path_param(source_id)}/{encode_path_param(file_id)}",
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

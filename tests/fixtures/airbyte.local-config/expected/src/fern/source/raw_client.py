

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.not_found_error import NotFoundError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.actor_catalog_with_updated_at import ActorCatalogWithUpdatedAt
from ..types.airbyte_catalog import AirbyteCatalog
from ..types.check_connection_read import CheckConnectionRead
from ..types.discover_catalog_result import DiscoverCatalogResult
from ..types.invalid_input_exception_info import InvalidInputExceptionInfo
from ..types.not_found_known_exception_info import NotFoundKnownExceptionInfo
from ..types.source_clone_configuration import SourceCloneConfiguration
from ..types.source_configuration import SourceConfiguration
from ..types.source_definition_id import SourceDefinitionId
from ..types.source_discover_schema_read import SourceDiscoverSchemaRead
from ..types.source_id import SourceId
from ..types.source_read import SourceRead
from ..types.source_read_list import SourceReadList
from ..types.workspace_id import WorkspaceId
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawSourceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def check_connection_to_source(
        self, *, source_id: SourceId, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CheckConnectionRead]:
        """
        Parameters
        ----------
        source_id : SourceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CheckConnectionRead]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/sources/check_connection",
            method="POST",
            json={
                "sourceId": source_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CheckConnectionRead,
                    parse_obj_as(
                        type_=CheckConnectionRead,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundKnownExceptionInfo,
                        parse_obj_as(
                            type_=NotFoundKnownExceptionInfo,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InvalidInputExceptionInfo,
                        parse_obj_as(
                            type_=InvalidInputExceptionInfo,
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

    def check_connection_to_source_for_update(
        self,
        *,
        connection_configuration: SourceConfiguration,
        name: str,
        source_id: SourceId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CheckConnectionRead]:
        """
        Parameters
        ----------
        connection_configuration : SourceConfiguration

        name : str

        source_id : SourceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CheckConnectionRead]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/sources/check_connection_for_update",
            method="POST",
            json={
                "connectionConfiguration": connection_configuration,
                "name": name,
                "sourceId": source_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CheckConnectionRead,
                    parse_obj_as(
                        type_=CheckConnectionRead,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundKnownExceptionInfo,
                        parse_obj_as(
                            type_=NotFoundKnownExceptionInfo,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InvalidInputExceptionInfo,
                        parse_obj_as(
                            type_=InvalidInputExceptionInfo,
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

    def clone_source(
        self,
        *,
        source_clone_id: SourceId,
        source_configuration: typing.Optional[SourceCloneConfiguration] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SourceRead]:
        """
        Parameters
        ----------
        source_clone_id : SourceId

        source_configuration : typing.Optional[SourceCloneConfiguration]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SourceRead]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/sources/clone",
            method="POST",
            json={
                "sourceCloneId": source_clone_id,
                "sourceConfiguration": convert_and_respect_annotation_metadata(
                    object_=source_configuration, annotation=SourceCloneConfiguration, direction="write"
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
                    SourceRead,
                    parse_obj_as(
                        type_=SourceRead,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundKnownExceptionInfo,
                        parse_obj_as(
                            type_=NotFoundKnownExceptionInfo,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InvalidInputExceptionInfo,
                        parse_obj_as(
                            type_=InvalidInputExceptionInfo,
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
        connection_configuration: SourceConfiguration,
        name: str,
        source_definition_id: SourceDefinitionId,
        workspace_id: WorkspaceId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SourceRead]:
        """
        Parameters
        ----------
        connection_configuration : SourceConfiguration

        name : str

        source_definition_id : SourceDefinitionId

        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SourceRead]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/sources/create",
            method="POST",
            json={
                "connectionConfiguration": connection_configuration,
                "name": name,
                "sourceDefinitionId": source_definition_id,
                "workspaceId": workspace_id,
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
                    SourceRead,
                    parse_obj_as(
                        type_=SourceRead,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InvalidInputExceptionInfo,
                        parse_obj_as(
                            type_=InvalidInputExceptionInfo,
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
        self, *, source_id: SourceId, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        source_id : SourceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/sources/delete",
            method="POST",
            json={
                "sourceId": source_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundKnownExceptionInfo,
                        parse_obj_as(
                            type_=NotFoundKnownExceptionInfo,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InvalidInputExceptionInfo,
                        parse_obj_as(
                            type_=InvalidInputExceptionInfo,
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

    def discover_schema_for_source(
        self,
        *,
        source_id: SourceId,
        connection_id: typing.Optional[str] = OMIT,
        disable_cache: typing.Optional[bool] = OMIT,
        notify_schema_change: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SourceDiscoverSchemaRead]:
        """
        Parameters
        ----------
        source_id : SourceId

        connection_id : typing.Optional[str]

        disable_cache : typing.Optional[bool]

        notify_schema_change : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SourceDiscoverSchemaRead]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/sources/discover_schema",
            method="POST",
            json={
                "connectionId": connection_id,
                "disable_cache": disable_cache,
                "notifySchemaChange": notify_schema_change,
                "sourceId": source_id,
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
                    SourceDiscoverSchemaRead,
                    parse_obj_as(
                        type_=SourceDiscoverSchemaRead,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundKnownExceptionInfo,
                        parse_obj_as(
                            type_=NotFoundKnownExceptionInfo,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InvalidInputExceptionInfo,
                        parse_obj_as(
                            type_=InvalidInputExceptionInfo,
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

    def get_source(
        self, *, source_id: SourceId, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SourceRead]:
        """
        Parameters
        ----------
        source_id : SourceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SourceRead]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/sources/get",
            method="POST",
            json={
                "sourceId": source_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SourceRead,
                    parse_obj_as(
                        type_=SourceRead,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundKnownExceptionInfo,
                        parse_obj_as(
                            type_=NotFoundKnownExceptionInfo,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InvalidInputExceptionInfo,
                        parse_obj_as(
                            type_=InvalidInputExceptionInfo,
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

    def list_sources_for_workspace(
        self, *, workspace_id: WorkspaceId, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SourceReadList]:
        """
        List sources for workspace. Does not return deleted sources.

        Parameters
        ----------
        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SourceReadList]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/sources/list",
            method="POST",
            json={
                "workspaceId": workspace_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SourceReadList,
                    parse_obj_as(
                        type_=SourceReadList,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundKnownExceptionInfo,
                        parse_obj_as(
                            type_=NotFoundKnownExceptionInfo,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InvalidInputExceptionInfo,
                        parse_obj_as(
                            type_=InvalidInputExceptionInfo,
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

    def get_most_recent_source_actor_catalog(
        self, *, source_id: SourceId, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ActorCatalogWithUpdatedAt]:
        """
        Parameters
        ----------
        source_id : SourceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ActorCatalogWithUpdatedAt]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/sources/most_recent_source_actor_catalog",
            method="POST",
            json={
                "sourceId": source_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ActorCatalogWithUpdatedAt,
                    parse_obj_as(
                        type_=ActorCatalogWithUpdatedAt,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundKnownExceptionInfo,
                        parse_obj_as(
                            type_=NotFoundKnownExceptionInfo,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InvalidInputExceptionInfo,
                        parse_obj_as(
                            type_=InvalidInputExceptionInfo,
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

    def search_sources(
        self,
        *,
        connection_configuration: typing.Optional[SourceConfiguration] = OMIT,
        name: typing.Optional[str] = OMIT,
        source_definition_id: typing.Optional[SourceDefinitionId] = OMIT,
        source_id: typing.Optional[SourceId] = OMIT,
        source_name: typing.Optional[str] = OMIT,
        workspace_id: typing.Optional[WorkspaceId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SourceReadList]:
        """
        Parameters
        ----------
        connection_configuration : typing.Optional[SourceConfiguration]

        name : typing.Optional[str]

        source_definition_id : typing.Optional[SourceDefinitionId]

        source_id : typing.Optional[SourceId]

        source_name : typing.Optional[str]

        workspace_id : typing.Optional[WorkspaceId]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SourceReadList]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/sources/search",
            method="POST",
            json={
                "connectionConfiguration": connection_configuration,
                "name": name,
                "sourceDefinitionId": source_definition_id,
                "sourceId": source_id,
                "sourceName": source_name,
                "workspaceId": workspace_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SourceReadList,
                    parse_obj_as(
                        type_=SourceReadList,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InvalidInputExceptionInfo,
                        parse_obj_as(
                            type_=InvalidInputExceptionInfo,
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

    def update_source(
        self,
        *,
        connection_configuration: SourceConfiguration,
        name: str,
        source_id: SourceId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SourceRead]:
        """
        Parameters
        ----------
        connection_configuration : SourceConfiguration

        name : str

        source_id : SourceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SourceRead]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/sources/update",
            method="POST",
            json={
                "connectionConfiguration": connection_configuration,
                "name": name,
                "sourceId": source_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SourceRead,
                    parse_obj_as(
                        type_=SourceRead,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundKnownExceptionInfo,
                        parse_obj_as(
                            type_=NotFoundKnownExceptionInfo,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InvalidInputExceptionInfo,
                        parse_obj_as(
                            type_=InvalidInputExceptionInfo,
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

    def write_discover_catalog_result(
        self,
        *,
        catalog: AirbyteCatalog,
        configuration_hash: typing.Optional[str] = OMIT,
        connector_version: typing.Optional[str] = OMIT,
        source_id: typing.Optional[SourceId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DiscoverCatalogResult]:
        """
        Parameters
        ----------
        catalog : AirbyteCatalog

        configuration_hash : typing.Optional[str]

        connector_version : typing.Optional[str]

        source_id : typing.Optional[SourceId]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DiscoverCatalogResult]
            Successful Operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/sources/write_discover_catalog_result",
            method="POST",
            json={
                "catalog": convert_and_respect_annotation_metadata(
                    object_=catalog, annotation=AirbyteCatalog, direction="write"
                ),
                "configurationHash": configuration_hash,
                "connectorVersion": connector_version,
                "sourceId": source_id,
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
                    DiscoverCatalogResult,
                    parse_obj_as(
                        type_=DiscoverCatalogResult,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawSourceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def check_connection_to_source(
        self, *, source_id: SourceId, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CheckConnectionRead]:
        """
        Parameters
        ----------
        source_id : SourceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CheckConnectionRead]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/sources/check_connection",
            method="POST",
            json={
                "sourceId": source_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CheckConnectionRead,
                    parse_obj_as(
                        type_=CheckConnectionRead,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundKnownExceptionInfo,
                        parse_obj_as(
                            type_=NotFoundKnownExceptionInfo,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InvalidInputExceptionInfo,
                        parse_obj_as(
                            type_=InvalidInputExceptionInfo,
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

    async def check_connection_to_source_for_update(
        self,
        *,
        connection_configuration: SourceConfiguration,
        name: str,
        source_id: SourceId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CheckConnectionRead]:
        """
        Parameters
        ----------
        connection_configuration : SourceConfiguration

        name : str

        source_id : SourceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CheckConnectionRead]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/sources/check_connection_for_update",
            method="POST",
            json={
                "connectionConfiguration": connection_configuration,
                "name": name,
                "sourceId": source_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CheckConnectionRead,
                    parse_obj_as(
                        type_=CheckConnectionRead,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundKnownExceptionInfo,
                        parse_obj_as(
                            type_=NotFoundKnownExceptionInfo,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InvalidInputExceptionInfo,
                        parse_obj_as(
                            type_=InvalidInputExceptionInfo,
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

    async def clone_source(
        self,
        *,
        source_clone_id: SourceId,
        source_configuration: typing.Optional[SourceCloneConfiguration] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SourceRead]:
        """
        Parameters
        ----------
        source_clone_id : SourceId

        source_configuration : typing.Optional[SourceCloneConfiguration]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SourceRead]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/sources/clone",
            method="POST",
            json={
                "sourceCloneId": source_clone_id,
                "sourceConfiguration": convert_and_respect_annotation_metadata(
                    object_=source_configuration, annotation=SourceCloneConfiguration, direction="write"
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
                    SourceRead,
                    parse_obj_as(
                        type_=SourceRead,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundKnownExceptionInfo,
                        parse_obj_as(
                            type_=NotFoundKnownExceptionInfo,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InvalidInputExceptionInfo,
                        parse_obj_as(
                            type_=InvalidInputExceptionInfo,
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
        connection_configuration: SourceConfiguration,
        name: str,
        source_definition_id: SourceDefinitionId,
        workspace_id: WorkspaceId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SourceRead]:
        """
        Parameters
        ----------
        connection_configuration : SourceConfiguration

        name : str

        source_definition_id : SourceDefinitionId

        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SourceRead]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/sources/create",
            method="POST",
            json={
                "connectionConfiguration": connection_configuration,
                "name": name,
                "sourceDefinitionId": source_definition_id,
                "workspaceId": workspace_id,
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
                    SourceRead,
                    parse_obj_as(
                        type_=SourceRead,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InvalidInputExceptionInfo,
                        parse_obj_as(
                            type_=InvalidInputExceptionInfo,
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
        self, *, source_id: SourceId, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        source_id : SourceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/sources/delete",
            method="POST",
            json={
                "sourceId": source_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundKnownExceptionInfo,
                        parse_obj_as(
                            type_=NotFoundKnownExceptionInfo,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InvalidInputExceptionInfo,
                        parse_obj_as(
                            type_=InvalidInputExceptionInfo,
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

    async def discover_schema_for_source(
        self,
        *,
        source_id: SourceId,
        connection_id: typing.Optional[str] = OMIT,
        disable_cache: typing.Optional[bool] = OMIT,
        notify_schema_change: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SourceDiscoverSchemaRead]:
        """
        Parameters
        ----------
        source_id : SourceId

        connection_id : typing.Optional[str]

        disable_cache : typing.Optional[bool]

        notify_schema_change : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SourceDiscoverSchemaRead]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/sources/discover_schema",
            method="POST",
            json={
                "connectionId": connection_id,
                "disable_cache": disable_cache,
                "notifySchemaChange": notify_schema_change,
                "sourceId": source_id,
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
                    SourceDiscoverSchemaRead,
                    parse_obj_as(
                        type_=SourceDiscoverSchemaRead,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundKnownExceptionInfo,
                        parse_obj_as(
                            type_=NotFoundKnownExceptionInfo,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InvalidInputExceptionInfo,
                        parse_obj_as(
                            type_=InvalidInputExceptionInfo,
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

    async def get_source(
        self, *, source_id: SourceId, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SourceRead]:
        """
        Parameters
        ----------
        source_id : SourceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SourceRead]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/sources/get",
            method="POST",
            json={
                "sourceId": source_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SourceRead,
                    parse_obj_as(
                        type_=SourceRead,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundKnownExceptionInfo,
                        parse_obj_as(
                            type_=NotFoundKnownExceptionInfo,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InvalidInputExceptionInfo,
                        parse_obj_as(
                            type_=InvalidInputExceptionInfo,
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

    async def list_sources_for_workspace(
        self, *, workspace_id: WorkspaceId, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SourceReadList]:
        """
        List sources for workspace. Does not return deleted sources.

        Parameters
        ----------
        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SourceReadList]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/sources/list",
            method="POST",
            json={
                "workspaceId": workspace_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SourceReadList,
                    parse_obj_as(
                        type_=SourceReadList,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundKnownExceptionInfo,
                        parse_obj_as(
                            type_=NotFoundKnownExceptionInfo,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InvalidInputExceptionInfo,
                        parse_obj_as(
                            type_=InvalidInputExceptionInfo,
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

    async def get_most_recent_source_actor_catalog(
        self, *, source_id: SourceId, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ActorCatalogWithUpdatedAt]:
        """
        Parameters
        ----------
        source_id : SourceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ActorCatalogWithUpdatedAt]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/sources/most_recent_source_actor_catalog",
            method="POST",
            json={
                "sourceId": source_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ActorCatalogWithUpdatedAt,
                    parse_obj_as(
                        type_=ActorCatalogWithUpdatedAt,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundKnownExceptionInfo,
                        parse_obj_as(
                            type_=NotFoundKnownExceptionInfo,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InvalidInputExceptionInfo,
                        parse_obj_as(
                            type_=InvalidInputExceptionInfo,
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

    async def search_sources(
        self,
        *,
        connection_configuration: typing.Optional[SourceConfiguration] = OMIT,
        name: typing.Optional[str] = OMIT,
        source_definition_id: typing.Optional[SourceDefinitionId] = OMIT,
        source_id: typing.Optional[SourceId] = OMIT,
        source_name: typing.Optional[str] = OMIT,
        workspace_id: typing.Optional[WorkspaceId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SourceReadList]:
        """
        Parameters
        ----------
        connection_configuration : typing.Optional[SourceConfiguration]

        name : typing.Optional[str]

        source_definition_id : typing.Optional[SourceDefinitionId]

        source_id : typing.Optional[SourceId]

        source_name : typing.Optional[str]

        workspace_id : typing.Optional[WorkspaceId]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SourceReadList]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/sources/search",
            method="POST",
            json={
                "connectionConfiguration": connection_configuration,
                "name": name,
                "sourceDefinitionId": source_definition_id,
                "sourceId": source_id,
                "sourceName": source_name,
                "workspaceId": workspace_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SourceReadList,
                    parse_obj_as(
                        type_=SourceReadList,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InvalidInputExceptionInfo,
                        parse_obj_as(
                            type_=InvalidInputExceptionInfo,
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

    async def update_source(
        self,
        *,
        connection_configuration: SourceConfiguration,
        name: str,
        source_id: SourceId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SourceRead]:
        """
        Parameters
        ----------
        connection_configuration : SourceConfiguration

        name : str

        source_id : SourceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SourceRead]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/sources/update",
            method="POST",
            json={
                "connectionConfiguration": connection_configuration,
                "name": name,
                "sourceId": source_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SourceRead,
                    parse_obj_as(
                        type_=SourceRead,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundKnownExceptionInfo,
                        parse_obj_as(
                            type_=NotFoundKnownExceptionInfo,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InvalidInputExceptionInfo,
                        parse_obj_as(
                            type_=InvalidInputExceptionInfo,
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

    async def write_discover_catalog_result(
        self,
        *,
        catalog: AirbyteCatalog,
        configuration_hash: typing.Optional[str] = OMIT,
        connector_version: typing.Optional[str] = OMIT,
        source_id: typing.Optional[SourceId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DiscoverCatalogResult]:
        """
        Parameters
        ----------
        catalog : AirbyteCatalog

        configuration_hash : typing.Optional[str]

        connector_version : typing.Optional[str]

        source_id : typing.Optional[SourceId]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DiscoverCatalogResult]
            Successful Operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/sources/write_discover_catalog_result",
            method="POST",
            json={
                "catalog": convert_and_respect_annotation_metadata(
                    object_=catalog, annotation=AirbyteCatalog, direction="write"
                ),
                "configurationHash": configuration_hash,
                "connectorVersion": connector_version,
                "sourceId": source_id,
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
                    DiscoverCatalogResult,
                    parse_obj_as(
                        type_=DiscoverCatalogResult,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

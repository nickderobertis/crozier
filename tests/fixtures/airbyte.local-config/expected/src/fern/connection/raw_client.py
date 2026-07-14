

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.not_found_error import NotFoundError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.airbyte_catalog import AirbyteCatalog
from ..types.connection_id import ConnectionId
from ..types.connection_read import ConnectionRead
from ..types.connection_read_list import ConnectionReadList
from ..types.connection_schedule import ConnectionSchedule
from ..types.connection_schedule_data import ConnectionScheduleData
from ..types.connection_schedule_type import ConnectionScheduleType
from ..types.connection_status import ConnectionStatus
from ..types.destination_id import DestinationId
from ..types.destination_search import DestinationSearch
from ..types.geography import Geography
from ..types.invalid_input_exception_info import InvalidInputExceptionInfo
from ..types.job_info_read import JobInfoRead
from ..types.namespace_definition_type import NamespaceDefinitionType
from ..types.non_breaking_changes_preference import NonBreakingChangesPreference
from ..types.not_found_known_exception_info import NotFoundKnownExceptionInfo
from ..types.operation_id import OperationId
from ..types.resource_requirements import ResourceRequirements
from ..types.source_id import SourceId
from ..types.source_search import SourceSearch
from ..types.workspace_id import WorkspaceId


OMIT = typing.cast(typing.Any, ...)


class RawConnectionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_connection(
        self,
        *,
        destination_id: DestinationId,
        source_id: SourceId,
        status: ConnectionStatus,
        geography: typing.Optional[Geography] = OMIT,
        name: typing.Optional[str] = OMIT,
        namespace_definition: typing.Optional[NamespaceDefinitionType] = OMIT,
        namespace_format: typing.Optional[str] = OMIT,
        non_breaking_changes_preference: typing.Optional[NonBreakingChangesPreference] = OMIT,
        notify_schema_changes: typing.Optional[bool] = OMIT,
        operation_ids: typing.Optional[typing.Sequence[OperationId]] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        resource_requirements: typing.Optional[ResourceRequirements] = OMIT,
        schedule: typing.Optional[ConnectionSchedule] = OMIT,
        schedule_data: typing.Optional[ConnectionScheduleData] = OMIT,
        schedule_type: typing.Optional[ConnectionScheduleType] = OMIT,
        source_catalog_id: typing.Optional[str] = OMIT,
        sync_catalog: typing.Optional[AirbyteCatalog] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ConnectionRead]:
        """
        Parameters
        ----------
        destination_id : DestinationId

        source_id : SourceId

        status : ConnectionStatus

        geography : typing.Optional[Geography]

        name : typing.Optional[str]
            Optional name of the connection

        namespace_definition : typing.Optional[NamespaceDefinitionType]

        namespace_format : typing.Optional[str]
            Used when namespaceDefinition is 'customformat'. If blank then behaves like namespaceDefinition = 'destination'. If "${SOURCE_NAMESPACE}" then behaves like namespaceDefinition = 'source'.

        non_breaking_changes_preference : typing.Optional[NonBreakingChangesPreference]

        notify_schema_changes : typing.Optional[bool]

        operation_ids : typing.Optional[typing.Sequence[OperationId]]

        prefix : typing.Optional[str]
            Prefix that will be prepended to the name of each stream when it is written to the destination.

        resource_requirements : typing.Optional[ResourceRequirements]

        schedule : typing.Optional[ConnectionSchedule]

        schedule_data : typing.Optional[ConnectionScheduleData]

        schedule_type : typing.Optional[ConnectionScheduleType]

        source_catalog_id : typing.Optional[str]

        sync_catalog : typing.Optional[AirbyteCatalog]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ConnectionRead]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/connections/create",
            method="POST",
            json={
                "destinationId": destination_id,
                "geography": geography,
                "name": name,
                "namespaceDefinition": namespace_definition,
                "namespaceFormat": namespace_format,
                "nonBreakingChangesPreference": non_breaking_changes_preference,
                "notifySchemaChanges": notify_schema_changes,
                "operationIds": operation_ids,
                "prefix": prefix,
                "resourceRequirements": convert_and_respect_annotation_metadata(
                    object_=resource_requirements, annotation=ResourceRequirements, direction="write"
                ),
                "schedule": convert_and_respect_annotation_metadata(
                    object_=schedule, annotation=ConnectionSchedule, direction="write"
                ),
                "scheduleData": convert_and_respect_annotation_metadata(
                    object_=schedule_data, annotation=ConnectionScheduleData, direction="write"
                ),
                "scheduleType": schedule_type,
                "sourceCatalogId": source_catalog_id,
                "sourceId": source_id,
                "status": status,
                "syncCatalog": convert_and_respect_annotation_metadata(
                    object_=sync_catalog, annotation=AirbyteCatalog, direction="write"
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
                    ConnectionRead,
                    parse_obj_as(
                        type_=ConnectionRead,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_connection(
        self, *, connection_id: ConnectionId, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        connection_id : ConnectionId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/connections/delete",
            method="POST",
            json={
                "connectionId": connection_id,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_connection(
        self, *, connection_id: ConnectionId, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ConnectionRead]:
        """
        Parameters
        ----------
        connection_id : ConnectionId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ConnectionRead]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/connections/get",
            method="POST",
            json={
                "connectionId": connection_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConnectionRead,
                    parse_obj_as(
                        type_=ConnectionRead,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_connections_for_workspace(
        self, *, workspace_id: WorkspaceId, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ConnectionReadList]:
        """
        List connections for workspace. Does not return deleted connections.

        Parameters
        ----------
        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ConnectionReadList]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/connections/list",
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
                    ConnectionReadList,
                    parse_obj_as(
                        type_=ConnectionReadList,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_all_connections_for_workspace(
        self, *, workspace_id: WorkspaceId, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ConnectionReadList]:
        """
        List connections for workspace, including deleted connections.

        Parameters
        ----------
        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ConnectionReadList]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/connections/list_all",
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
                    ConnectionReadList,
                    parse_obj_as(
                        type_=ConnectionReadList,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def reset_connection(
        self, *, connection_id: ConnectionId, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[JobInfoRead]:
        """
        Parameters
        ----------
        connection_id : ConnectionId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JobInfoRead]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/connections/reset",
            method="POST",
            json={
                "connectionId": connection_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JobInfoRead,
                    parse_obj_as(
                        type_=JobInfoRead,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def search_connections(
        self,
        *,
        connection_id: typing.Optional[ConnectionId] = OMIT,
        destination: typing.Optional[DestinationSearch] = OMIT,
        destination_id: typing.Optional[DestinationId] = OMIT,
        name: typing.Optional[str] = OMIT,
        namespace_definition: typing.Optional[NamespaceDefinitionType] = OMIT,
        namespace_format: typing.Optional[str] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        schedule: typing.Optional[ConnectionSchedule] = OMIT,
        schedule_data: typing.Optional[ConnectionScheduleData] = OMIT,
        schedule_type: typing.Optional[ConnectionScheduleType] = OMIT,
        source: typing.Optional[SourceSearch] = OMIT,
        source_id: typing.Optional[SourceId] = OMIT,
        status: typing.Optional[ConnectionStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ConnectionReadList]:
        """
        Parameters
        ----------
        connection_id : typing.Optional[ConnectionId]

        destination : typing.Optional[DestinationSearch]

        destination_id : typing.Optional[DestinationId]

        name : typing.Optional[str]

        namespace_definition : typing.Optional[NamespaceDefinitionType]

        namespace_format : typing.Optional[str]
            Used when namespaceDefinition is 'customformat'. If blank then behaves like namespaceDefinition = 'destination'. If "${SOURCE_NAMESPACE}" then behaves like namespaceDefinition = 'source'.

        prefix : typing.Optional[str]
            Prefix that will be prepended to the name of each stream when it is written to the destination.

        schedule : typing.Optional[ConnectionSchedule]

        schedule_data : typing.Optional[ConnectionScheduleData]

        schedule_type : typing.Optional[ConnectionScheduleType]

        source : typing.Optional[SourceSearch]

        source_id : typing.Optional[SourceId]

        status : typing.Optional[ConnectionStatus]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ConnectionReadList]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/connections/search",
            method="POST",
            json={
                "connectionId": connection_id,
                "destination": convert_and_respect_annotation_metadata(
                    object_=destination, annotation=DestinationSearch, direction="write"
                ),
                "destinationId": destination_id,
                "name": name,
                "namespaceDefinition": namespace_definition,
                "namespaceFormat": namespace_format,
                "prefix": prefix,
                "schedule": convert_and_respect_annotation_metadata(
                    object_=schedule, annotation=ConnectionSchedule, direction="write"
                ),
                "scheduleData": convert_and_respect_annotation_metadata(
                    object_=schedule_data, annotation=ConnectionScheduleData, direction="write"
                ),
                "scheduleType": schedule_type,
                "source": convert_and_respect_annotation_metadata(
                    object_=source, annotation=SourceSearch, direction="write"
                ),
                "sourceId": source_id,
                "status": status,
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
                    ConnectionReadList,
                    parse_obj_as(
                        type_=ConnectionReadList,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def sync_connection(
        self, *, connection_id: ConnectionId, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[JobInfoRead]:
        """
        Parameters
        ----------
        connection_id : ConnectionId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JobInfoRead]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/connections/sync",
            method="POST",
            json={
                "connectionId": connection_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JobInfoRead,
                    parse_obj_as(
                        type_=JobInfoRead,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_connection(
        self,
        *,
        connection_id: ConnectionId,
        breaking_change: typing.Optional[bool] = OMIT,
        geography: typing.Optional[Geography] = OMIT,
        name: typing.Optional[str] = OMIT,
        namespace_definition: typing.Optional[NamespaceDefinitionType] = OMIT,
        namespace_format: typing.Optional[str] = OMIT,
        non_breaking_changes_preference: typing.Optional[NonBreakingChangesPreference] = OMIT,
        notify_schema_changes: typing.Optional[bool] = OMIT,
        operation_ids: typing.Optional[typing.Sequence[OperationId]] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        resource_requirements: typing.Optional[ResourceRequirements] = OMIT,
        schedule: typing.Optional[ConnectionSchedule] = OMIT,
        schedule_data: typing.Optional[ConnectionScheduleData] = OMIT,
        schedule_type: typing.Optional[ConnectionScheduleType] = OMIT,
        source_catalog_id: typing.Optional[str] = OMIT,
        status: typing.Optional[ConnectionStatus] = OMIT,
        sync_catalog: typing.Optional[AirbyteCatalog] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ConnectionRead]:
        """
        Apply a patch-style update to a connection. Only fields present on the update request body will be updated.
        Note that if a catalog is present in the request body, the connection's entire catalog will be replaced
        with the catalog from the request. This means that to modify a single stream, the entire new catalog
        containing the updated stream needs to be sent.

        Parameters
        ----------
        connection_id : ConnectionId

        breaking_change : typing.Optional[bool]

        geography : typing.Optional[Geography]

        name : typing.Optional[str]
            Name that will be set to this connection

        namespace_definition : typing.Optional[NamespaceDefinitionType]

        namespace_format : typing.Optional[str]
            Used when namespaceDefinition is 'customformat'. If blank then behaves like namespaceDefinition = 'destination'. If "${SOURCE_NAMESPACE}" then behaves like namespaceDefinition = 'source'.

        non_breaking_changes_preference : typing.Optional[NonBreakingChangesPreference]

        notify_schema_changes : typing.Optional[bool]

        operation_ids : typing.Optional[typing.Sequence[OperationId]]

        prefix : typing.Optional[str]
            Prefix that will be prepended to the name of each stream when it is written to the destination.

        resource_requirements : typing.Optional[ResourceRequirements]

        schedule : typing.Optional[ConnectionSchedule]

        schedule_data : typing.Optional[ConnectionScheduleData]

        schedule_type : typing.Optional[ConnectionScheduleType]

        source_catalog_id : typing.Optional[str]

        status : typing.Optional[ConnectionStatus]

        sync_catalog : typing.Optional[AirbyteCatalog]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ConnectionRead]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/connections/update",
            method="POST",
            json={
                "breakingChange": breaking_change,
                "connectionId": connection_id,
                "geography": geography,
                "name": name,
                "namespaceDefinition": namespace_definition,
                "namespaceFormat": namespace_format,
                "nonBreakingChangesPreference": non_breaking_changes_preference,
                "notifySchemaChanges": notify_schema_changes,
                "operationIds": operation_ids,
                "prefix": prefix,
                "resourceRequirements": convert_and_respect_annotation_metadata(
                    object_=resource_requirements, annotation=ResourceRequirements, direction="write"
                ),
                "schedule": convert_and_respect_annotation_metadata(
                    object_=schedule, annotation=ConnectionSchedule, direction="write"
                ),
                "scheduleData": convert_and_respect_annotation_metadata(
                    object_=schedule_data, annotation=ConnectionScheduleData, direction="write"
                ),
                "scheduleType": schedule_type,
                "sourceCatalogId": source_catalog_id,
                "status": status,
                "syncCatalog": convert_and_respect_annotation_metadata(
                    object_=sync_catalog, annotation=AirbyteCatalog, direction="write"
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
                    ConnectionRead,
                    parse_obj_as(
                        type_=ConnectionRead,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawConnectionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_connection(
        self,
        *,
        destination_id: DestinationId,
        source_id: SourceId,
        status: ConnectionStatus,
        geography: typing.Optional[Geography] = OMIT,
        name: typing.Optional[str] = OMIT,
        namespace_definition: typing.Optional[NamespaceDefinitionType] = OMIT,
        namespace_format: typing.Optional[str] = OMIT,
        non_breaking_changes_preference: typing.Optional[NonBreakingChangesPreference] = OMIT,
        notify_schema_changes: typing.Optional[bool] = OMIT,
        operation_ids: typing.Optional[typing.Sequence[OperationId]] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        resource_requirements: typing.Optional[ResourceRequirements] = OMIT,
        schedule: typing.Optional[ConnectionSchedule] = OMIT,
        schedule_data: typing.Optional[ConnectionScheduleData] = OMIT,
        schedule_type: typing.Optional[ConnectionScheduleType] = OMIT,
        source_catalog_id: typing.Optional[str] = OMIT,
        sync_catalog: typing.Optional[AirbyteCatalog] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ConnectionRead]:
        """
        Parameters
        ----------
        destination_id : DestinationId

        source_id : SourceId

        status : ConnectionStatus

        geography : typing.Optional[Geography]

        name : typing.Optional[str]
            Optional name of the connection

        namespace_definition : typing.Optional[NamespaceDefinitionType]

        namespace_format : typing.Optional[str]
            Used when namespaceDefinition is 'customformat'. If blank then behaves like namespaceDefinition = 'destination'. If "${SOURCE_NAMESPACE}" then behaves like namespaceDefinition = 'source'.

        non_breaking_changes_preference : typing.Optional[NonBreakingChangesPreference]

        notify_schema_changes : typing.Optional[bool]

        operation_ids : typing.Optional[typing.Sequence[OperationId]]

        prefix : typing.Optional[str]
            Prefix that will be prepended to the name of each stream when it is written to the destination.

        resource_requirements : typing.Optional[ResourceRequirements]

        schedule : typing.Optional[ConnectionSchedule]

        schedule_data : typing.Optional[ConnectionScheduleData]

        schedule_type : typing.Optional[ConnectionScheduleType]

        source_catalog_id : typing.Optional[str]

        sync_catalog : typing.Optional[AirbyteCatalog]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ConnectionRead]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/connections/create",
            method="POST",
            json={
                "destinationId": destination_id,
                "geography": geography,
                "name": name,
                "namespaceDefinition": namespace_definition,
                "namespaceFormat": namespace_format,
                "nonBreakingChangesPreference": non_breaking_changes_preference,
                "notifySchemaChanges": notify_schema_changes,
                "operationIds": operation_ids,
                "prefix": prefix,
                "resourceRequirements": convert_and_respect_annotation_metadata(
                    object_=resource_requirements, annotation=ResourceRequirements, direction="write"
                ),
                "schedule": convert_and_respect_annotation_metadata(
                    object_=schedule, annotation=ConnectionSchedule, direction="write"
                ),
                "scheduleData": convert_and_respect_annotation_metadata(
                    object_=schedule_data, annotation=ConnectionScheduleData, direction="write"
                ),
                "scheduleType": schedule_type,
                "sourceCatalogId": source_catalog_id,
                "sourceId": source_id,
                "status": status,
                "syncCatalog": convert_and_respect_annotation_metadata(
                    object_=sync_catalog, annotation=AirbyteCatalog, direction="write"
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
                    ConnectionRead,
                    parse_obj_as(
                        type_=ConnectionRead,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_connection(
        self, *, connection_id: ConnectionId, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        connection_id : ConnectionId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/connections/delete",
            method="POST",
            json={
                "connectionId": connection_id,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_connection(
        self, *, connection_id: ConnectionId, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ConnectionRead]:
        """
        Parameters
        ----------
        connection_id : ConnectionId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ConnectionRead]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/connections/get",
            method="POST",
            json={
                "connectionId": connection_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConnectionRead,
                    parse_obj_as(
                        type_=ConnectionRead,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_connections_for_workspace(
        self, *, workspace_id: WorkspaceId, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ConnectionReadList]:
        """
        List connections for workspace. Does not return deleted connections.

        Parameters
        ----------
        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ConnectionReadList]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/connections/list",
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
                    ConnectionReadList,
                    parse_obj_as(
                        type_=ConnectionReadList,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_all_connections_for_workspace(
        self, *, workspace_id: WorkspaceId, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ConnectionReadList]:
        """
        List connections for workspace, including deleted connections.

        Parameters
        ----------
        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ConnectionReadList]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/connections/list_all",
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
                    ConnectionReadList,
                    parse_obj_as(
                        type_=ConnectionReadList,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def reset_connection(
        self, *, connection_id: ConnectionId, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[JobInfoRead]:
        """
        Parameters
        ----------
        connection_id : ConnectionId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JobInfoRead]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/connections/reset",
            method="POST",
            json={
                "connectionId": connection_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JobInfoRead,
                    parse_obj_as(
                        type_=JobInfoRead,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def search_connections(
        self,
        *,
        connection_id: typing.Optional[ConnectionId] = OMIT,
        destination: typing.Optional[DestinationSearch] = OMIT,
        destination_id: typing.Optional[DestinationId] = OMIT,
        name: typing.Optional[str] = OMIT,
        namespace_definition: typing.Optional[NamespaceDefinitionType] = OMIT,
        namespace_format: typing.Optional[str] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        schedule: typing.Optional[ConnectionSchedule] = OMIT,
        schedule_data: typing.Optional[ConnectionScheduleData] = OMIT,
        schedule_type: typing.Optional[ConnectionScheduleType] = OMIT,
        source: typing.Optional[SourceSearch] = OMIT,
        source_id: typing.Optional[SourceId] = OMIT,
        status: typing.Optional[ConnectionStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ConnectionReadList]:
        """
        Parameters
        ----------
        connection_id : typing.Optional[ConnectionId]

        destination : typing.Optional[DestinationSearch]

        destination_id : typing.Optional[DestinationId]

        name : typing.Optional[str]

        namespace_definition : typing.Optional[NamespaceDefinitionType]

        namespace_format : typing.Optional[str]
            Used when namespaceDefinition is 'customformat'. If blank then behaves like namespaceDefinition = 'destination'. If "${SOURCE_NAMESPACE}" then behaves like namespaceDefinition = 'source'.

        prefix : typing.Optional[str]
            Prefix that will be prepended to the name of each stream when it is written to the destination.

        schedule : typing.Optional[ConnectionSchedule]

        schedule_data : typing.Optional[ConnectionScheduleData]

        schedule_type : typing.Optional[ConnectionScheduleType]

        source : typing.Optional[SourceSearch]

        source_id : typing.Optional[SourceId]

        status : typing.Optional[ConnectionStatus]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ConnectionReadList]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/connections/search",
            method="POST",
            json={
                "connectionId": connection_id,
                "destination": convert_and_respect_annotation_metadata(
                    object_=destination, annotation=DestinationSearch, direction="write"
                ),
                "destinationId": destination_id,
                "name": name,
                "namespaceDefinition": namespace_definition,
                "namespaceFormat": namespace_format,
                "prefix": prefix,
                "schedule": convert_and_respect_annotation_metadata(
                    object_=schedule, annotation=ConnectionSchedule, direction="write"
                ),
                "scheduleData": convert_and_respect_annotation_metadata(
                    object_=schedule_data, annotation=ConnectionScheduleData, direction="write"
                ),
                "scheduleType": schedule_type,
                "source": convert_and_respect_annotation_metadata(
                    object_=source, annotation=SourceSearch, direction="write"
                ),
                "sourceId": source_id,
                "status": status,
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
                    ConnectionReadList,
                    parse_obj_as(
                        type_=ConnectionReadList,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def sync_connection(
        self, *, connection_id: ConnectionId, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[JobInfoRead]:
        """
        Parameters
        ----------
        connection_id : ConnectionId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JobInfoRead]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/connections/sync",
            method="POST",
            json={
                "connectionId": connection_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JobInfoRead,
                    parse_obj_as(
                        type_=JobInfoRead,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_connection(
        self,
        *,
        connection_id: ConnectionId,
        breaking_change: typing.Optional[bool] = OMIT,
        geography: typing.Optional[Geography] = OMIT,
        name: typing.Optional[str] = OMIT,
        namespace_definition: typing.Optional[NamespaceDefinitionType] = OMIT,
        namespace_format: typing.Optional[str] = OMIT,
        non_breaking_changes_preference: typing.Optional[NonBreakingChangesPreference] = OMIT,
        notify_schema_changes: typing.Optional[bool] = OMIT,
        operation_ids: typing.Optional[typing.Sequence[OperationId]] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        resource_requirements: typing.Optional[ResourceRequirements] = OMIT,
        schedule: typing.Optional[ConnectionSchedule] = OMIT,
        schedule_data: typing.Optional[ConnectionScheduleData] = OMIT,
        schedule_type: typing.Optional[ConnectionScheduleType] = OMIT,
        source_catalog_id: typing.Optional[str] = OMIT,
        status: typing.Optional[ConnectionStatus] = OMIT,
        sync_catalog: typing.Optional[AirbyteCatalog] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ConnectionRead]:
        """
        Apply a patch-style update to a connection. Only fields present on the update request body will be updated.
        Note that if a catalog is present in the request body, the connection's entire catalog will be replaced
        with the catalog from the request. This means that to modify a single stream, the entire new catalog
        containing the updated stream needs to be sent.

        Parameters
        ----------
        connection_id : ConnectionId

        breaking_change : typing.Optional[bool]

        geography : typing.Optional[Geography]

        name : typing.Optional[str]
            Name that will be set to this connection

        namespace_definition : typing.Optional[NamespaceDefinitionType]

        namespace_format : typing.Optional[str]
            Used when namespaceDefinition is 'customformat'. If blank then behaves like namespaceDefinition = 'destination'. If "${SOURCE_NAMESPACE}" then behaves like namespaceDefinition = 'source'.

        non_breaking_changes_preference : typing.Optional[NonBreakingChangesPreference]

        notify_schema_changes : typing.Optional[bool]

        operation_ids : typing.Optional[typing.Sequence[OperationId]]

        prefix : typing.Optional[str]
            Prefix that will be prepended to the name of each stream when it is written to the destination.

        resource_requirements : typing.Optional[ResourceRequirements]

        schedule : typing.Optional[ConnectionSchedule]

        schedule_data : typing.Optional[ConnectionScheduleData]

        schedule_type : typing.Optional[ConnectionScheduleType]

        source_catalog_id : typing.Optional[str]

        status : typing.Optional[ConnectionStatus]

        sync_catalog : typing.Optional[AirbyteCatalog]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ConnectionRead]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/connections/update",
            method="POST",
            json={
                "breakingChange": breaking_change,
                "connectionId": connection_id,
                "geography": geography,
                "name": name,
                "namespaceDefinition": namespace_definition,
                "namespaceFormat": namespace_format,
                "nonBreakingChangesPreference": non_breaking_changes_preference,
                "notifySchemaChanges": notify_schema_changes,
                "operationIds": operation_ids,
                "prefix": prefix,
                "resourceRequirements": convert_and_respect_annotation_metadata(
                    object_=resource_requirements, annotation=ResourceRequirements, direction="write"
                ),
                "schedule": convert_and_respect_annotation_metadata(
                    object_=schedule, annotation=ConnectionSchedule, direction="write"
                ),
                "scheduleData": convert_and_respect_annotation_metadata(
                    object_=schedule_data, annotation=ConnectionScheduleData, direction="write"
                ),
                "scheduleType": schedule_type,
                "sourceCatalogId": source_catalog_id,
                "status": status,
                "syncCatalog": convert_and_respect_annotation_metadata(
                    object_=sync_catalog, annotation=AirbyteCatalog, direction="write"
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
                    ConnectionRead,
                    parse_obj_as(
                        type_=ConnectionRead,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

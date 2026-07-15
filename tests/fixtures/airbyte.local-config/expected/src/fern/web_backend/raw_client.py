

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
from ..types.connection_schedule import ConnectionSchedule
from ..types.connection_schedule_data import ConnectionScheduleData
from ..types.connection_schedule_type import ConnectionScheduleType
from ..types.connection_state_type import ConnectionStateType
from ..types.connection_status import ConnectionStatus
from ..types.destination_id import DestinationId
from ..types.geography import Geography
from ..types.invalid_input_exception_info import InvalidInputExceptionInfo
from ..types.namespace_definition_type import NamespaceDefinitionType
from ..types.non_breaking_changes_preference import NonBreakingChangesPreference
from ..types.not_found_known_exception_info import NotFoundKnownExceptionInfo
from ..types.operation_create import OperationCreate
from ..types.operation_id import OperationId
from ..types.resource_requirements import ResourceRequirements
from ..types.source_id import SourceId
from ..types.web_backend_check_updates_read import WebBackendCheckUpdatesRead
from ..types.web_backend_connection_read import WebBackendConnectionRead
from ..types.web_backend_connection_read_list import WebBackendConnectionReadList
from ..types.web_backend_geographies_list_result import WebBackendGeographiesListResult
from ..types.web_backend_operation_create_or_update import WebBackendOperationCreateOrUpdate
from ..types.web_backend_workspace_state_result import WebBackendWorkspaceStateResult
from ..types.workspace_id import WorkspaceId


OMIT = typing.cast(typing.Any, ...)


class RawWebBackendClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def check_updates(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[WebBackendCheckUpdatesRead]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WebBackendCheckUpdatesRead]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/web_backend/check_updates",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WebBackendCheckUpdatesRead,
                    parse_obj_as(
                        type_=WebBackendCheckUpdatesRead,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
        operation_ids: typing.Optional[typing.Sequence[OperationId]] = OMIT,
        operations: typing.Optional[typing.Sequence[OperationCreate]] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        resource_requirements: typing.Optional[ResourceRequirements] = OMIT,
        schedule: typing.Optional[ConnectionSchedule] = OMIT,
        schedule_data: typing.Optional[ConnectionScheduleData] = OMIT,
        schedule_type: typing.Optional[ConnectionScheduleType] = OMIT,
        source_catalog_id: typing.Optional[str] = OMIT,
        sync_catalog: typing.Optional[AirbyteCatalog] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WebBackendConnectionRead]:
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

        operation_ids : typing.Optional[typing.Sequence[OperationId]]

        operations : typing.Optional[typing.Sequence[OperationCreate]]

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
        HttpResponse[WebBackendConnectionRead]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/web_backend/connections/create",
            method="POST",
            json={
                "destinationId": destination_id,
                "geography": geography,
                "name": name,
                "namespaceDefinition": namespace_definition,
                "namespaceFormat": namespace_format,
                "nonBreakingChangesPreference": non_breaking_changes_preference,
                "operationIds": operation_ids,
                "operations": convert_and_respect_annotation_metadata(
                    object_=operations, annotation=typing.Sequence[OperationCreate], direction="write"
                ),
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
                    WebBackendConnectionRead,
                    parse_obj_as(
                        type_=WebBackendConnectionRead,
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

    def get_connection(
        self,
        *,
        connection_id: ConnectionId,
        with_refreshed_catalog: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WebBackendConnectionRead]:
        """
        Parameters
        ----------
        connection_id : ConnectionId

        with_refreshed_catalog : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WebBackendConnectionRead]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/web_backend/connections/get",
            method="POST",
            json={
                "connectionId": connection_id,
                "withRefreshedCatalog": with_refreshed_catalog,
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
                    WebBackendConnectionRead,
                    parse_obj_as(
                        type_=WebBackendConnectionRead,
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
        self,
        *,
        workspace_id: WorkspaceId,
        destination_id: typing.Optional[typing.Sequence[DestinationId]] = OMIT,
        source_id: typing.Optional[typing.Sequence[SourceId]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WebBackendConnectionReadList]:
        """
        Parameters
        ----------
        workspace_id : WorkspaceId

        destination_id : typing.Optional[typing.Sequence[DestinationId]]

        source_id : typing.Optional[typing.Sequence[SourceId]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WebBackendConnectionReadList]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/web_backend/connections/list",
            method="POST",
            json={
                "destinationId": destination_id,
                "sourceId": source_id,
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
                    WebBackendConnectionReadList,
                    parse_obj_as(
                        type_=WebBackendConnectionReadList,
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
        geography: typing.Optional[Geography] = OMIT,
        name: typing.Optional[str] = OMIT,
        namespace_definition: typing.Optional[NamespaceDefinitionType] = OMIT,
        namespace_format: typing.Optional[str] = OMIT,
        non_breaking_changes_preference: typing.Optional[NonBreakingChangesPreference] = OMIT,
        notify_schema_changes: typing.Optional[bool] = OMIT,
        operations: typing.Optional[typing.Sequence[WebBackendOperationCreateOrUpdate]] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        resource_requirements: typing.Optional[ResourceRequirements] = OMIT,
        schedule: typing.Optional[ConnectionSchedule] = OMIT,
        schedule_data: typing.Optional[ConnectionScheduleData] = OMIT,
        schedule_type: typing.Optional[ConnectionScheduleType] = OMIT,
        skip_reset: typing.Optional[bool] = OMIT,
        source_catalog_id: typing.Optional[str] = OMIT,
        status: typing.Optional[ConnectionStatus] = OMIT,
        sync_catalog: typing.Optional[AirbyteCatalog] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WebBackendConnectionRead]:
        """
        Apply a patch-style update to a connection. Only fields present on the update request body will be updated.
        Any operations that lack an ID will be created. Then, the newly created operationId will be applied to the
        connection along with the rest of the operationIds in the request body.
        Apply a patch-style update to a connection. Only fields present on the update request body will be updated.
        Note that if a catalog is present in the request body, the connection's entire catalog will be replaced
        with the catalog from the request. This means that to modify a single stream, the entire new catalog
        containing the updated stream needs to be sent.

        Parameters
        ----------
        connection_id : ConnectionId

        geography : typing.Optional[Geography]

        name : typing.Optional[str]
            Name that will be set to the connection

        namespace_definition : typing.Optional[NamespaceDefinitionType]

        namespace_format : typing.Optional[str]
            Used when namespaceDefinition is 'customformat'. If blank then behaves like namespaceDefinition = 'destination'. If "${SOURCE_NAMESPACE}" then behaves like namespaceDefinition = 'source'.

        non_breaking_changes_preference : typing.Optional[NonBreakingChangesPreference]

        notify_schema_changes : typing.Optional[bool]

        operations : typing.Optional[typing.Sequence[WebBackendOperationCreateOrUpdate]]

        prefix : typing.Optional[str]
            Prefix that will be prepended to the name of each stream when it is written to the destination.

        resource_requirements : typing.Optional[ResourceRequirements]

        schedule : typing.Optional[ConnectionSchedule]

        schedule_data : typing.Optional[ConnectionScheduleData]

        schedule_type : typing.Optional[ConnectionScheduleType]

        skip_reset : typing.Optional[bool]

        source_catalog_id : typing.Optional[str]

        status : typing.Optional[ConnectionStatus]

        sync_catalog : typing.Optional[AirbyteCatalog]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WebBackendConnectionRead]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/web_backend/connections/update",
            method="POST",
            json={
                "connectionId": connection_id,
                "geography": geography,
                "name": name,
                "namespaceDefinition": namespace_definition,
                "namespaceFormat": namespace_format,
                "nonBreakingChangesPreference": non_breaking_changes_preference,
                "notifySchemaChanges": notify_schema_changes,
                "operations": convert_and_respect_annotation_metadata(
                    object_=operations, annotation=typing.Sequence[WebBackendOperationCreateOrUpdate], direction="write"
                ),
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
                "skipReset": skip_reset,
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
                    WebBackendConnectionRead,
                    parse_obj_as(
                        type_=WebBackendConnectionRead,
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

    def list_geographies(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[WebBackendGeographiesListResult]:
        """
        Returns all available geographies in which a data sync can run.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WebBackendGeographiesListResult]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/web_backend/geographies/list",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WebBackendGeographiesListResult,
                    parse_obj_as(
                        type_=WebBackendGeographiesListResult,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_state_type(
        self, *, connection_id: ConnectionId, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ConnectionStateType]:
        """
        Parameters
        ----------
        connection_id : ConnectionId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ConnectionStateType]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/web_backend/state/get_type",
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
                    ConnectionStateType,
                    parse_obj_as(
                        type_=ConnectionStateType,
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

    def get_workspace_state(
        self, *, workspace_id: WorkspaceId, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[WebBackendWorkspaceStateResult]:
        """
        Parameters
        ----------
        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WebBackendWorkspaceStateResult]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/web_backend/workspace/state",
            method="POST",
            json={
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
                    WebBackendWorkspaceStateResult,
                    parse_obj_as(
                        type_=WebBackendWorkspaceStateResult,
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


class AsyncRawWebBackendClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def check_updates(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[WebBackendCheckUpdatesRead]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WebBackendCheckUpdatesRead]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/web_backend/check_updates",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WebBackendCheckUpdatesRead,
                    parse_obj_as(
                        type_=WebBackendCheckUpdatesRead,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
        operation_ids: typing.Optional[typing.Sequence[OperationId]] = OMIT,
        operations: typing.Optional[typing.Sequence[OperationCreate]] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        resource_requirements: typing.Optional[ResourceRequirements] = OMIT,
        schedule: typing.Optional[ConnectionSchedule] = OMIT,
        schedule_data: typing.Optional[ConnectionScheduleData] = OMIT,
        schedule_type: typing.Optional[ConnectionScheduleType] = OMIT,
        source_catalog_id: typing.Optional[str] = OMIT,
        sync_catalog: typing.Optional[AirbyteCatalog] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WebBackendConnectionRead]:
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

        operation_ids : typing.Optional[typing.Sequence[OperationId]]

        operations : typing.Optional[typing.Sequence[OperationCreate]]

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
        AsyncHttpResponse[WebBackendConnectionRead]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/web_backend/connections/create",
            method="POST",
            json={
                "destinationId": destination_id,
                "geography": geography,
                "name": name,
                "namespaceDefinition": namespace_definition,
                "namespaceFormat": namespace_format,
                "nonBreakingChangesPreference": non_breaking_changes_preference,
                "operationIds": operation_ids,
                "operations": convert_and_respect_annotation_metadata(
                    object_=operations, annotation=typing.Sequence[OperationCreate], direction="write"
                ),
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
                    WebBackendConnectionRead,
                    parse_obj_as(
                        type_=WebBackendConnectionRead,
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

    async def get_connection(
        self,
        *,
        connection_id: ConnectionId,
        with_refreshed_catalog: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WebBackendConnectionRead]:
        """
        Parameters
        ----------
        connection_id : ConnectionId

        with_refreshed_catalog : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WebBackendConnectionRead]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/web_backend/connections/get",
            method="POST",
            json={
                "connectionId": connection_id,
                "withRefreshedCatalog": with_refreshed_catalog,
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
                    WebBackendConnectionRead,
                    parse_obj_as(
                        type_=WebBackendConnectionRead,
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
        self,
        *,
        workspace_id: WorkspaceId,
        destination_id: typing.Optional[typing.Sequence[DestinationId]] = OMIT,
        source_id: typing.Optional[typing.Sequence[SourceId]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WebBackendConnectionReadList]:
        """
        Parameters
        ----------
        workspace_id : WorkspaceId

        destination_id : typing.Optional[typing.Sequence[DestinationId]]

        source_id : typing.Optional[typing.Sequence[SourceId]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WebBackendConnectionReadList]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/web_backend/connections/list",
            method="POST",
            json={
                "destinationId": destination_id,
                "sourceId": source_id,
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
                    WebBackendConnectionReadList,
                    parse_obj_as(
                        type_=WebBackendConnectionReadList,
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
        geography: typing.Optional[Geography] = OMIT,
        name: typing.Optional[str] = OMIT,
        namespace_definition: typing.Optional[NamespaceDefinitionType] = OMIT,
        namespace_format: typing.Optional[str] = OMIT,
        non_breaking_changes_preference: typing.Optional[NonBreakingChangesPreference] = OMIT,
        notify_schema_changes: typing.Optional[bool] = OMIT,
        operations: typing.Optional[typing.Sequence[WebBackendOperationCreateOrUpdate]] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        resource_requirements: typing.Optional[ResourceRequirements] = OMIT,
        schedule: typing.Optional[ConnectionSchedule] = OMIT,
        schedule_data: typing.Optional[ConnectionScheduleData] = OMIT,
        schedule_type: typing.Optional[ConnectionScheduleType] = OMIT,
        skip_reset: typing.Optional[bool] = OMIT,
        source_catalog_id: typing.Optional[str] = OMIT,
        status: typing.Optional[ConnectionStatus] = OMIT,
        sync_catalog: typing.Optional[AirbyteCatalog] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WebBackendConnectionRead]:
        """
        Apply a patch-style update to a connection. Only fields present on the update request body will be updated.
        Any operations that lack an ID will be created. Then, the newly created operationId will be applied to the
        connection along with the rest of the operationIds in the request body.
        Apply a patch-style update to a connection. Only fields present on the update request body will be updated.
        Note that if a catalog is present in the request body, the connection's entire catalog will be replaced
        with the catalog from the request. This means that to modify a single stream, the entire new catalog
        containing the updated stream needs to be sent.

        Parameters
        ----------
        connection_id : ConnectionId

        geography : typing.Optional[Geography]

        name : typing.Optional[str]
            Name that will be set to the connection

        namespace_definition : typing.Optional[NamespaceDefinitionType]

        namespace_format : typing.Optional[str]
            Used when namespaceDefinition is 'customformat'. If blank then behaves like namespaceDefinition = 'destination'. If "${SOURCE_NAMESPACE}" then behaves like namespaceDefinition = 'source'.

        non_breaking_changes_preference : typing.Optional[NonBreakingChangesPreference]

        notify_schema_changes : typing.Optional[bool]

        operations : typing.Optional[typing.Sequence[WebBackendOperationCreateOrUpdate]]

        prefix : typing.Optional[str]
            Prefix that will be prepended to the name of each stream when it is written to the destination.

        resource_requirements : typing.Optional[ResourceRequirements]

        schedule : typing.Optional[ConnectionSchedule]

        schedule_data : typing.Optional[ConnectionScheduleData]

        schedule_type : typing.Optional[ConnectionScheduleType]

        skip_reset : typing.Optional[bool]

        source_catalog_id : typing.Optional[str]

        status : typing.Optional[ConnectionStatus]

        sync_catalog : typing.Optional[AirbyteCatalog]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WebBackendConnectionRead]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/web_backend/connections/update",
            method="POST",
            json={
                "connectionId": connection_id,
                "geography": geography,
                "name": name,
                "namespaceDefinition": namespace_definition,
                "namespaceFormat": namespace_format,
                "nonBreakingChangesPreference": non_breaking_changes_preference,
                "notifySchemaChanges": notify_schema_changes,
                "operations": convert_and_respect_annotation_metadata(
                    object_=operations, annotation=typing.Sequence[WebBackendOperationCreateOrUpdate], direction="write"
                ),
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
                "skipReset": skip_reset,
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
                    WebBackendConnectionRead,
                    parse_obj_as(
                        type_=WebBackendConnectionRead,
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

    async def list_geographies(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[WebBackendGeographiesListResult]:
        """
        Returns all available geographies in which a data sync can run.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WebBackendGeographiesListResult]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/web_backend/geographies/list",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WebBackendGeographiesListResult,
                    parse_obj_as(
                        type_=WebBackendGeographiesListResult,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_state_type(
        self, *, connection_id: ConnectionId, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ConnectionStateType]:
        """
        Parameters
        ----------
        connection_id : ConnectionId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ConnectionStateType]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/web_backend/state/get_type",
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
                    ConnectionStateType,
                    parse_obj_as(
                        type_=ConnectionStateType,
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

    async def get_workspace_state(
        self, *, workspace_id: WorkspaceId, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[WebBackendWorkspaceStateResult]:
        """
        Parameters
        ----------
        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WebBackendWorkspaceStateResult]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/web_backend/workspace/state",
            method="POST",
            json={
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
                    WebBackendWorkspaceStateResult,
                    parse_obj_as(
                        type_=WebBackendWorkspaceStateResult,
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

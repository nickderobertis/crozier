

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.datetime_utils import serialize_datetime
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.not_found_error import NotFoundError
from ..types.entity_change_meta import EntityChangeMeta
from ..types.entity_transaction_response import EntityTransactionResponse
from ..types.json_node import JsonNode
from ..types.model_state_stats_dto import ModelStateStatsDto
from ..types.model_stats_dto import ModelStatsDto
from ..types.single_delete_result import SingleDeleteResult
from ..types.stream_delete_result import StreamDeleteResult
from .types.create_collection_request_format import CreateCollectionRequestFormat
from .types.create_request_format import CreateRequestFormat
from .types.update_collection_request_body_item import UpdateCollectionRequestBodyItem
from .types.update_collection_request_format import UpdateCollectionRequestFormat
from .types.update_single_request_format import UpdateSingleRequestFormat
from .types.update_single_with_loopback_request_format import UpdateSingleWithLoopbackRequestFormat
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawEntityManagementClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_entity_statistics(
        self,
        *,
        point_in_time: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ModelStatsDto]:
        """
        Returns statistics for entities grouped by model name and version.

        Parameters
        ----------
        point_in_time : typing.Optional[dt.datetime]
            The point-in-time for statistics in ISO 8601 format (e.g., '2035-01-01T12:00:00Z'). Defaults to current consistency time if not provided

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ModelStatsDto]
            Statistics retrieved successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "entity/stats",
            method="GET",
            params={
                "pointInTime": serialize_datetime(point_in_time) if point_in_time is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ModelStatsDto,
                    parse_obj_as(
                        type_=ModelStatsDto,
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

    def get_entity_statistics_by_state(
        self,
        *,
        point_in_time: typing.Optional[dt.datetime] = None,
        states: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ModelStateStatsDto]:
        """
        Returns statistics for entities grouped by model name, version, and state.

        Parameters
        ----------
        point_in_time : typing.Optional[dt.datetime]
            The point-in-time for statistics in ISO 8601 format (e.g., '2035-01-01T12:00:00Z'). Defaults to current consistency time if not provided

        states : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Optional list of states for which to calculate statistics. If not provided, statistics will be calculated for all current workflow states

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ModelStateStatsDto]
            Statistics by state retrieved successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "entity/stats/states",
            method="GET",
            params={
                "pointInTime": serialize_datetime(point_in_time) if point_in_time is not None else None,
                "states": states,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ModelStateStatsDto,
                    parse_obj_as(
                        type_=ModelStateStatsDto,
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

    def get_entity_statistics_by_state_for_model(
        self,
        entity_name: str,
        model_version: int,
        *,
        point_in_time: typing.Optional[dt.datetime] = None,
        states: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ModelStateStatsDto]:
        """
        Returns statistics for entities of a specific model name and version, grouped by state.

        Parameters
        ----------
        entity_name : str
            Name of the entity model

        model_version : int
            Version number of the entity model

        point_in_time : typing.Optional[dt.datetime]
            The point-in-time for statistics in ISO 8601 format (e.g., '2035-01-01T12:00:00Z'). Defaults to current consistency time if not provided

        states : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Optional list of states for which to calculate statistics. If not provided, statistics will be calculated for all current workflow states

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ModelStateStatsDto]
            Statistics by state retrieved successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"entity/stats/states/{encode_path_param(entity_name)}/{encode_path_param(model_version)}",
            method="GET",
            params={
                "pointInTime": serialize_datetime(point_in_time) if point_in_time is not None else None,
                "states": states,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ModelStateStatsDto,
                    parse_obj_as(
                        type_=ModelStateStatsDto,
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

    def get_entity_statistics_for_model(
        self,
        entity_name: str,
        model_version: int,
        *,
        point_in_time: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ModelStatsDto]:
        """
        Returns statistics for entities of a specific model name and version.

        Parameters
        ----------
        entity_name : str
            Name of the entity model

        model_version : int
            Version number of the entity model

        point_in_time : typing.Optional[dt.datetime]
            The point-in-time for statistics in ISO 8601 format (e.g., '2035-01-01T12:00:00Z'). Defaults to current consistency time if not provided

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ModelStatsDto]
            Statistics retrieved successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"entity/stats/{encode_path_param(entity_name)}/{encode_path_param(model_version)}",
            method="GET",
            params={
                "pointInTime": serialize_datetime(point_in_time) if point_in_time is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ModelStatsDto,
                    parse_obj_as(
                        type_=ModelStatsDto,
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

    def get_one_entity(
        self,
        entity_id: str,
        *,
        point_in_time: typing.Optional[dt.datetime] = None,
        transaction_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Get a single entity by id

        Parameters
        ----------
        entity_id : str
            The unique identifier (UUID) of the entity to get

        point_in_time : typing.Optional[dt.datetime]
            The point-in-time for loading the entity, in ISO 8601 format (e.g., '2035-01-01T12:00:00Z'). Defaults to the current consistency time of the system if not provided.

        transaction_id : typing.Optional[str]
            Load the entity as it was at the end of the specified transaction with the given transactionId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            Successfully retrieved the entity
        """
        _response = self._client_wrapper.httpx_client.request(
            f"entity/{encode_path_param(entity_id)}",
            method="GET",
            params={
                "pointInTime": serialize_datetime(point_in_time) if point_in_time is not None else None,
                "transactionId": transaction_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
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

    def delete_single_entity(
        self, entity_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SingleDeleteResult]:
        """
        Deletes a single entity by Id

        Parameters
        ----------
        entity_id : str
            The unique identifier (UUID) of the entity to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SingleDeleteResult]
            Successfully deleted the entity
        """
        _response = self._client_wrapper.httpx_client.request(
            f"entity/{encode_path_param(entity_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SingleDeleteResult,
                    parse_obj_as(
                        type_=SingleDeleteResult,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
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

    def get_entity_changes_metadata(
        self,
        entity_id: str,
        *,
        point_in_time: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EntityChangeMeta]:
        """

        Retrieves the change history metadata for a specific entity.

        Returns a stream of metadata records describing each change made to the entity, including:
        - Transaction ID that made the change
        - Timestamp when the change occurred
        - User who made the change
        - Type of change (CREATE, UPDATE, DELETE)
        - Number of fields changed

        Common use cases:
        - Audit trail review
        - Change tracking
        - Compliance reporting
        - Debugging entity state changes

        Note:
        - Changes are returned in chronological order
        - The pointInTime parameter allows viewing the change history as it existed at a specific time


        Parameters
        ----------
        entity_id : str
            The unique identifier (UUID) of the entity to get change history for

        point_in_time : typing.Optional[dt.datetime]
            The point-in-time for loading the entity changes, in ISO 8601 format (e.g., '2035-01-01T12:00:00Z'). Defaults to the current consistency time of the system if not provided.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EntityChangeMeta]
            Successfully retrieved entity changes metadata
        """
        _response = self._client_wrapper.httpx_client.request(
            f"entity/{encode_path_param(entity_id)}/changes",
            method="GET",
            params={
                "pointInTime": serialize_datetime(point_in_time) if point_in_time is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EntityChangeMeta,
                    parse_obj_as(
                        type_=EntityChangeMeta,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
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

    def get_all_entities(
        self,
        entity_name: str,
        model_version: int,
        *,
        page_size: typing.Optional[int] = None,
        page_number: typing.Optional[int] = None,
        point_in_time: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[JsonNode]:
        """

        Retrieves all entities for a given model name and version, with pagination support.
        Results are returned as a stream of JSON objects.

        Common use cases:
        - Bulk data retrieval
        - Data migration
        - Reporting

        Note:
        - For large datasets, consider using the search API with snapshots instead.
        - To find out how many entities there are, use the entity statistics endpoints.


        Parameters
        ----------
        entity_name : str
            Name of the entity model to retrieve.

        model_version : int
            Version number of the entity model

        page_size : typing.Optional[int]
            Number of entities to return per page. Must be greater than 0.

        page_number : typing.Optional[int]
            Page number to retrieve, starting from 0. Must be greater than or equal to 0.

        point_in_time : typing.Optional[dt.datetime]
            The point-in-time for loading the entities, in ISO 8601 format (e.g., '2035-01-01T12:00:00Z'). Defaults to the current consistency time of the system if not provided.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JsonNode]
            Successfully retrieved entities
        """
        _response = self._client_wrapper.httpx_client.request(
            f"entity/{encode_path_param(entity_name)}/{encode_path_param(model_version)}",
            method="GET",
            params={
                "pageSize": page_size,
                "pageNumber": page_number,
                "pointInTime": serialize_datetime(point_in_time) if point_in_time is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JsonNode,
                    parse_obj_as(
                        type_=JsonNode,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
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

    def delete_entities(
        self,
        entity_name: str,
        model_version: int,
        *,
        type: str,
        transaction_size: typing.Optional[int] = None,
        point_in_time: typing.Optional[dt.datetime] = None,
        verbose: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[StreamDeleteResult]:
        """
        Deletes entities for a given model name and version which existed at the consistency time of the system when the request is launched by provided condition or all entities if condition is not provided.

        Parameters
        ----------
        entity_name : str
            Name of the entity model to delete

        model_version : int
            Version number of the entity model

        type : str

        transaction_size : typing.Optional[int]
            Maximum number of entities to delete in a single transaction. Higher values may improve performance but increase memory usage.

        point_in_time : typing.Optional[dt.datetime]
            The point-in-time for selecting the entities for deletion, in ISO 8601 format (e.g., '2035-01-01T12:00:00Z'). Defaults to the consistency time of the system if not provided.

        verbose : typing.Optional[bool]
            Include the list of deleted entity IDs in the response. When false, only returns statistics.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[StreamDeleteResult]
            Deletion process was successful. In case there were entities that could not be deletedthe response will contain information about that
        """
        _response = self._client_wrapper.httpx_client.request(
            f"entity/{encode_path_param(entity_name)}/{encode_path_param(model_version)}",
            method="DELETE",
            params={
                "transactionSize": transaction_size,
                "pointInTime": serialize_datetime(point_in_time) if point_in_time is not None else None,
                "verbose": verbose,
            },
            json={
                "type": type,
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
                    StreamDeleteResult,
                    parse_obj_as(
                        type_=StreamDeleteResult,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
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

    def create_collection(
        self,
        format: CreateCollectionRequestFormat,
        *,
        request: typing.Dict[str, typing.Any],
        transaction_window: typing.Optional[int] = None,
        transaction_timeout_millis: typing.Optional[int] = None,
        wait_for_consistency_after: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EntityTransactionResponse]:
        """

        Saves a collection of entities. Each entity can be from a different model and version.

        Path Parameters:
        - format: The format of the input payload (e.g., JSON, XML)

        Request Body:
        - A list of CreatePayload objects, each containing entity data and model information


        Parameters
        ----------
        format : CreateCollectionRequestFormat
            Format of the input payload

        request : typing.Dict[str, typing.Any]

        transaction_window : typing.Optional[int]
            Maximum number of entities per transactional batch. Default 100,
            maximum 1000; values outside (0, 1000] are rejected with 400
            BAD_REQUEST. Collections exceeding the window are split into
            multiple transactional batches committed sequentially. The
            response is an array with one element per chunk in commit order;
            chunks committed before any later failure remain durable.

        transaction_timeout_millis : typing.Optional[int]
            Maximum time in milliseconds allowed for transaction completion.
            Accepted for Cyoda Cloud API parity. Behavior is
            storage-engine-plugin dependent — not every plugin honors this
            field; consult the runtime plugin's documentation for the
            supported behavior.

        wait_for_consistency_after : typing.Optional[bool]
            If true, waits for consistency after operation completes.
            Accepted for Cyoda Cloud API parity. Behavior is
            storage-engine-plugin dependent — not every plugin honors this
            field; consult the runtime plugin's documentation for the
            supported behavior.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EntityTransactionResponse]
            Collection created successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"entity/{encode_path_param(format)}",
            method="POST",
            params={
                "transactionWindow": transaction_window,
                "transactionTimeoutMillis": transaction_timeout_millis,
                "waitForConsistencyAfter": wait_for_consistency_after,
            },
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EntityTransactionResponse,
                    parse_obj_as(
                        type_=EntityTransactionResponse,
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

    def update_collection(
        self,
        format: UpdateCollectionRequestFormat,
        *,
        request: typing.Sequence[UpdateCollectionRequestBodyItem],
        transaction_window: typing.Optional[int] = None,
        transaction_timeout_millis: typing.Optional[int] = None,
        wait_for_consistency_after: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EntityTransactionResponse]:
        """

        Updates a collection of entities. If any of the entities are not found,
        the request will fail and no entities will be updated.


        Parameters
        ----------
        format : UpdateCollectionRequestFormat
            Format of the input payload

        request : typing.Sequence[UpdateCollectionRequestBodyItem]

        transaction_window : typing.Optional[int]
            Maximum number of entities per transactional batch. Default 100,
            maximum 1000; values outside (0, 1000] are rejected with 400
            BAD_REQUEST. Collections exceeding the window are split into
            multiple transactional batches committed sequentially. The
            response is an array with one element per chunk in commit order;
            chunks committed before any later failure remain durable.

        transaction_timeout_millis : typing.Optional[int]
            Maximum time in milliseconds allowed for transaction completion.
            Accepted for Cyoda Cloud API parity. Behavior is
            storage-engine-plugin dependent — not every plugin honors this
            field; consult the runtime plugin's documentation for the
            supported behavior.

        wait_for_consistency_after : typing.Optional[bool]
            If true, waits for consistency after operation completes.
            Accepted for Cyoda Cloud API parity. Behavior is
            storage-engine-plugin dependent — not every plugin honors this
            field; consult the runtime plugin's documentation for the
            supported behavior.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EntityTransactionResponse]
            Collection updated successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"entity/{encode_path_param(format)}",
            method="PUT",
            params={
                "transactionWindow": transaction_window,
                "transactionTimeoutMillis": transaction_timeout_millis,
                "waitForConsistencyAfter": wait_for_consistency_after,
            },
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[UpdateCollectionRequestBodyItem], direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EntityTransactionResponse,
                    parse_obj_as(
                        type_=EntityTransactionResponse,
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

    def update_single_with_loopback(
        self,
        format: UpdateSingleWithLoopbackRequestFormat,
        entity_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        transaction_timeout_millis: typing.Optional[int] = None,
        wait_for_consistency_after: typing.Optional[bool] = None,
        if_match: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EntityTransactionResponse]:
        """

        Updates a single entity with a loopback transition.

        Path Parameters:
        - format: The format of the input payload (e.g., JSON, XML)
        - entityId: The UUID of the entity to update

        Request Body:
        - Entity data in the specified format


        Parameters
        ----------
        format : UpdateSingleWithLoopbackRequestFormat
            Format of the input payload

        entity_id : str
            The unique identifier (UUID) of the entity to update

        request : typing.Dict[str, typing.Any]

        transaction_timeout_millis : typing.Optional[int]
            Maximum time in milliseconds allowed for transaction completion.
            Operation will fail if it takes longer than this timeout.
            Accepted for Cyoda Cloud API parity. Behavior is
            storage-engine-plugin dependent — not every plugin honors this
            field; consult the runtime plugin's documentation for the
            supported behavior.

        wait_for_consistency_after : typing.Optional[bool]
            If true, waits for the consistency time to pass before responding.
            May increase response time but guarantees data consistency when
            returning, so that subsequent calls will see the updated data.
            Accepted for Cyoda Cloud API parity. Behavior is
            storage-engine-plugin dependent — not every plugin honors this
            field; consult the runtime plugin's documentation for the
            supported behavior.

        if_match : typing.Optional[str]
            Transaction ID of the entity version the client last read. If the entity has been modified since, returns 412 Precondition Failed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EntityTransactionResponse]
            Entity updated successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"entity/{encode_path_param(format)}/{encode_path_param(entity_id)}",
            method="PUT",
            params={
                "transactionTimeoutMillis": transaction_timeout_millis,
                "waitForConsistencyAfter": wait_for_consistency_after,
            },
            json=request,
            headers={
                "content-type": "application/json",
                "If-Match": str(if_match) if if_match is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EntityTransactionResponse,
                    parse_obj_as(
                        type_=EntityTransactionResponse,
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

    def update_single(
        self,
        format: UpdateSingleRequestFormat,
        entity_id: str,
        transition: str,
        *,
        request: typing.Dict[str, typing.Any],
        transaction_timeout_millis: typing.Optional[int] = None,
        wait_for_consistency_after: typing.Optional[bool] = None,
        if_match: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EntityTransactionResponse]:
        """

        Updates a single entity.

        Path Parameters:
        - format: The format of the input payload (e.g., JSON, XML)
        - entityId: The UUID of the entity to update
        - transition: The transition to apply to the entity

        Request Body:
        - Entity data in the specified format


        Parameters
        ----------
        format : UpdateSingleRequestFormat
            Format of the input payload

        entity_id : str
            The unique identifier (UUID) of the entity to update

        transition : str
            The transition state to apply to the entity (e.g., 'UPDATE', 'PUBLISH')

        request : typing.Dict[str, typing.Any]

        transaction_timeout_millis : typing.Optional[int]
            Maximum time in milliseconds allowed for transaction completion.
            Operation will fail if it takes longer than this timeout.
            Accepted for Cyoda Cloud API parity. Behavior is
            storage-engine-plugin dependent — not every plugin honors this
            field; consult the runtime plugin's documentation for the
            supported behavior.

        wait_for_consistency_after : typing.Optional[bool]
            If true, waits for the consistency time to pass before responding.
            May increase response time but guarantees data consistency when
            returning, so that subsequent calls will see the updated data.
            Accepted for Cyoda Cloud API parity. Behavior is
            storage-engine-plugin dependent — not every plugin honors this
            field; consult the runtime plugin's documentation for the
            supported behavior.

        if_match : typing.Optional[str]
            Transaction ID of the entity version the client last read. If the entity has been modified since, returns 412 Precondition Failed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EntityTransactionResponse]
            Entity updated successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"entity/{encode_path_param(format)}/{encode_path_param(entity_id)}/{encode_path_param(transition)}",
            method="PUT",
            params={
                "transactionTimeoutMillis": transaction_timeout_millis,
                "waitForConsistencyAfter": wait_for_consistency_after,
            },
            json=request,
            headers={
                "content-type": "application/json",
                "If-Match": str(if_match) if if_match is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EntityTransactionResponse,
                    parse_obj_as(
                        type_=EntityTransactionResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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

    def create(
        self,
        format: CreateRequestFormat,
        entity_name: str,
        model_version: int,
        *,
        request: typing.Dict[str, typing.Any],
        transaction_window: typing.Optional[int] = None,
        transaction_timeout_millis: typing.Optional[int] = None,
        wait_for_consistency_after: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EntityTransactionResponse]:
        """

        Saves a new entity or a collection of entities of the same type.

        Path Parameters:
        * format: The format of the input payload (e.g., JSON, XML)
        * entityName: The name of the entity model
        * modelVersion: The version number of the entity model

        Request Body:
        - A string containing the entity data in the specified format


        Parameters
        ----------
        format : CreateRequestFormat
            Format of the input payload

        entity_name : str
            Name of the entity model

        model_version : int
            Version number of the entity model

        request : typing.Dict[str, typing.Any]

        transaction_window : typing.Optional[int]
            Maximum number of entities per transactional batch. Applies only
            when the request body is a JSON array; ignored for single-object
            bodies. Default 100, maximum 1000; values outside (0, 1000] are
            rejected with 400 BAD_REQUEST. Array bodies exceeding the window
            are split into multiple transactional batches committed
            sequentially. The response is then an array with one element per
            chunk in commit order; chunks committed before any later failure
            remain durable.

        transaction_timeout_millis : typing.Optional[int]
            Maximum time in milliseconds for transaction completion.
            Accepted for Cyoda Cloud API parity. Behavior is
            storage-engine-plugin dependent — not every plugin honors this
            field; consult the runtime plugin's documentation for the
            supported behavior.

        wait_for_consistency_after : typing.Optional[bool]
            If true, waits for consistency after the operation completes.
            Accepted for Cyoda Cloud API parity. Behavior is
            storage-engine-plugin dependent — not every plugin honors this
            field; consult the runtime plugin's documentation for the
            supported behavior.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EntityTransactionResponse]
            Entity created successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"entity/{encode_path_param(format)}/{encode_path_param(entity_name)}/{encode_path_param(model_version)}",
            method="POST",
            params={
                "transactionWindow": transaction_window,
                "transactionTimeoutMillis": transaction_timeout_millis,
                "waitForConsistencyAfter": wait_for_consistency_after,
            },
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EntityTransactionResponse,
                    parse_obj_as(
                        type_=EntityTransactionResponse,
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


class AsyncRawEntityManagementClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_entity_statistics(
        self,
        *,
        point_in_time: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ModelStatsDto]:
        """
        Returns statistics for entities grouped by model name and version.

        Parameters
        ----------
        point_in_time : typing.Optional[dt.datetime]
            The point-in-time for statistics in ISO 8601 format (e.g., '2035-01-01T12:00:00Z'). Defaults to current consistency time if not provided

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ModelStatsDto]
            Statistics retrieved successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "entity/stats",
            method="GET",
            params={
                "pointInTime": serialize_datetime(point_in_time) if point_in_time is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ModelStatsDto,
                    parse_obj_as(
                        type_=ModelStatsDto,
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

    async def get_entity_statistics_by_state(
        self,
        *,
        point_in_time: typing.Optional[dt.datetime] = None,
        states: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ModelStateStatsDto]:
        """
        Returns statistics for entities grouped by model name, version, and state.

        Parameters
        ----------
        point_in_time : typing.Optional[dt.datetime]
            The point-in-time for statistics in ISO 8601 format (e.g., '2035-01-01T12:00:00Z'). Defaults to current consistency time if not provided

        states : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Optional list of states for which to calculate statistics. If not provided, statistics will be calculated for all current workflow states

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ModelStateStatsDto]
            Statistics by state retrieved successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "entity/stats/states",
            method="GET",
            params={
                "pointInTime": serialize_datetime(point_in_time) if point_in_time is not None else None,
                "states": states,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ModelStateStatsDto,
                    parse_obj_as(
                        type_=ModelStateStatsDto,
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

    async def get_entity_statistics_by_state_for_model(
        self,
        entity_name: str,
        model_version: int,
        *,
        point_in_time: typing.Optional[dt.datetime] = None,
        states: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ModelStateStatsDto]:
        """
        Returns statistics for entities of a specific model name and version, grouped by state.

        Parameters
        ----------
        entity_name : str
            Name of the entity model

        model_version : int
            Version number of the entity model

        point_in_time : typing.Optional[dt.datetime]
            The point-in-time for statistics in ISO 8601 format (e.g., '2035-01-01T12:00:00Z'). Defaults to current consistency time if not provided

        states : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Optional list of states for which to calculate statistics. If not provided, statistics will be calculated for all current workflow states

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ModelStateStatsDto]
            Statistics by state retrieved successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"entity/stats/states/{encode_path_param(entity_name)}/{encode_path_param(model_version)}",
            method="GET",
            params={
                "pointInTime": serialize_datetime(point_in_time) if point_in_time is not None else None,
                "states": states,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ModelStateStatsDto,
                    parse_obj_as(
                        type_=ModelStateStatsDto,
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

    async def get_entity_statistics_for_model(
        self,
        entity_name: str,
        model_version: int,
        *,
        point_in_time: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ModelStatsDto]:
        """
        Returns statistics for entities of a specific model name and version.

        Parameters
        ----------
        entity_name : str
            Name of the entity model

        model_version : int
            Version number of the entity model

        point_in_time : typing.Optional[dt.datetime]
            The point-in-time for statistics in ISO 8601 format (e.g., '2035-01-01T12:00:00Z'). Defaults to current consistency time if not provided

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ModelStatsDto]
            Statistics retrieved successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"entity/stats/{encode_path_param(entity_name)}/{encode_path_param(model_version)}",
            method="GET",
            params={
                "pointInTime": serialize_datetime(point_in_time) if point_in_time is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ModelStatsDto,
                    parse_obj_as(
                        type_=ModelStatsDto,
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

    async def get_one_entity(
        self,
        entity_id: str,
        *,
        point_in_time: typing.Optional[dt.datetime] = None,
        transaction_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Get a single entity by id

        Parameters
        ----------
        entity_id : str
            The unique identifier (UUID) of the entity to get

        point_in_time : typing.Optional[dt.datetime]
            The point-in-time for loading the entity, in ISO 8601 format (e.g., '2035-01-01T12:00:00Z'). Defaults to the current consistency time of the system if not provided.

        transaction_id : typing.Optional[str]
            Load the entity as it was at the end of the specified transaction with the given transactionId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            Successfully retrieved the entity
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"entity/{encode_path_param(entity_id)}",
            method="GET",
            params={
                "pointInTime": serialize_datetime(point_in_time) if point_in_time is not None else None,
                "transactionId": transaction_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
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

    async def delete_single_entity(
        self, entity_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SingleDeleteResult]:
        """
        Deletes a single entity by Id

        Parameters
        ----------
        entity_id : str
            The unique identifier (UUID) of the entity to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SingleDeleteResult]
            Successfully deleted the entity
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"entity/{encode_path_param(entity_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SingleDeleteResult,
                    parse_obj_as(
                        type_=SingleDeleteResult,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
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

    async def get_entity_changes_metadata(
        self,
        entity_id: str,
        *,
        point_in_time: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EntityChangeMeta]:
        """

        Retrieves the change history metadata for a specific entity.

        Returns a stream of metadata records describing each change made to the entity, including:
        - Transaction ID that made the change
        - Timestamp when the change occurred
        - User who made the change
        - Type of change (CREATE, UPDATE, DELETE)
        - Number of fields changed

        Common use cases:
        - Audit trail review
        - Change tracking
        - Compliance reporting
        - Debugging entity state changes

        Note:
        - Changes are returned in chronological order
        - The pointInTime parameter allows viewing the change history as it existed at a specific time


        Parameters
        ----------
        entity_id : str
            The unique identifier (UUID) of the entity to get change history for

        point_in_time : typing.Optional[dt.datetime]
            The point-in-time for loading the entity changes, in ISO 8601 format (e.g., '2035-01-01T12:00:00Z'). Defaults to the current consistency time of the system if not provided.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EntityChangeMeta]
            Successfully retrieved entity changes metadata
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"entity/{encode_path_param(entity_id)}/changes",
            method="GET",
            params={
                "pointInTime": serialize_datetime(point_in_time) if point_in_time is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EntityChangeMeta,
                    parse_obj_as(
                        type_=EntityChangeMeta,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
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

    async def get_all_entities(
        self,
        entity_name: str,
        model_version: int,
        *,
        page_size: typing.Optional[int] = None,
        page_number: typing.Optional[int] = None,
        point_in_time: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[JsonNode]:
        """

        Retrieves all entities for a given model name and version, with pagination support.
        Results are returned as a stream of JSON objects.

        Common use cases:
        - Bulk data retrieval
        - Data migration
        - Reporting

        Note:
        - For large datasets, consider using the search API with snapshots instead.
        - To find out how many entities there are, use the entity statistics endpoints.


        Parameters
        ----------
        entity_name : str
            Name of the entity model to retrieve.

        model_version : int
            Version number of the entity model

        page_size : typing.Optional[int]
            Number of entities to return per page. Must be greater than 0.

        page_number : typing.Optional[int]
            Page number to retrieve, starting from 0. Must be greater than or equal to 0.

        point_in_time : typing.Optional[dt.datetime]
            The point-in-time for loading the entities, in ISO 8601 format (e.g., '2035-01-01T12:00:00Z'). Defaults to the current consistency time of the system if not provided.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JsonNode]
            Successfully retrieved entities
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"entity/{encode_path_param(entity_name)}/{encode_path_param(model_version)}",
            method="GET",
            params={
                "pageSize": page_size,
                "pageNumber": page_number,
                "pointInTime": serialize_datetime(point_in_time) if point_in_time is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JsonNode,
                    parse_obj_as(
                        type_=JsonNode,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
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

    async def delete_entities(
        self,
        entity_name: str,
        model_version: int,
        *,
        type: str,
        transaction_size: typing.Optional[int] = None,
        point_in_time: typing.Optional[dt.datetime] = None,
        verbose: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[StreamDeleteResult]:
        """
        Deletes entities for a given model name and version which existed at the consistency time of the system when the request is launched by provided condition or all entities if condition is not provided.

        Parameters
        ----------
        entity_name : str
            Name of the entity model to delete

        model_version : int
            Version number of the entity model

        type : str

        transaction_size : typing.Optional[int]
            Maximum number of entities to delete in a single transaction. Higher values may improve performance but increase memory usage.

        point_in_time : typing.Optional[dt.datetime]
            The point-in-time for selecting the entities for deletion, in ISO 8601 format (e.g., '2035-01-01T12:00:00Z'). Defaults to the consistency time of the system if not provided.

        verbose : typing.Optional[bool]
            Include the list of deleted entity IDs in the response. When false, only returns statistics.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[StreamDeleteResult]
            Deletion process was successful. In case there were entities that could not be deletedthe response will contain information about that
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"entity/{encode_path_param(entity_name)}/{encode_path_param(model_version)}",
            method="DELETE",
            params={
                "transactionSize": transaction_size,
                "pointInTime": serialize_datetime(point_in_time) if point_in_time is not None else None,
                "verbose": verbose,
            },
            json={
                "type": type,
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
                    StreamDeleteResult,
                    parse_obj_as(
                        type_=StreamDeleteResult,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
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

    async def create_collection(
        self,
        format: CreateCollectionRequestFormat,
        *,
        request: typing.Dict[str, typing.Any],
        transaction_window: typing.Optional[int] = None,
        transaction_timeout_millis: typing.Optional[int] = None,
        wait_for_consistency_after: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EntityTransactionResponse]:
        """

        Saves a collection of entities. Each entity can be from a different model and version.

        Path Parameters:
        - format: The format of the input payload (e.g., JSON, XML)

        Request Body:
        - A list of CreatePayload objects, each containing entity data and model information


        Parameters
        ----------
        format : CreateCollectionRequestFormat
            Format of the input payload

        request : typing.Dict[str, typing.Any]

        transaction_window : typing.Optional[int]
            Maximum number of entities per transactional batch. Default 100,
            maximum 1000; values outside (0, 1000] are rejected with 400
            BAD_REQUEST. Collections exceeding the window are split into
            multiple transactional batches committed sequentially. The
            response is an array with one element per chunk in commit order;
            chunks committed before any later failure remain durable.

        transaction_timeout_millis : typing.Optional[int]
            Maximum time in milliseconds allowed for transaction completion.
            Accepted for Cyoda Cloud API parity. Behavior is
            storage-engine-plugin dependent — not every plugin honors this
            field; consult the runtime plugin's documentation for the
            supported behavior.

        wait_for_consistency_after : typing.Optional[bool]
            If true, waits for consistency after operation completes.
            Accepted for Cyoda Cloud API parity. Behavior is
            storage-engine-plugin dependent — not every plugin honors this
            field; consult the runtime plugin's documentation for the
            supported behavior.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EntityTransactionResponse]
            Collection created successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"entity/{encode_path_param(format)}",
            method="POST",
            params={
                "transactionWindow": transaction_window,
                "transactionTimeoutMillis": transaction_timeout_millis,
                "waitForConsistencyAfter": wait_for_consistency_after,
            },
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EntityTransactionResponse,
                    parse_obj_as(
                        type_=EntityTransactionResponse,
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

    async def update_collection(
        self,
        format: UpdateCollectionRequestFormat,
        *,
        request: typing.Sequence[UpdateCollectionRequestBodyItem],
        transaction_window: typing.Optional[int] = None,
        transaction_timeout_millis: typing.Optional[int] = None,
        wait_for_consistency_after: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EntityTransactionResponse]:
        """

        Updates a collection of entities. If any of the entities are not found,
        the request will fail and no entities will be updated.


        Parameters
        ----------
        format : UpdateCollectionRequestFormat
            Format of the input payload

        request : typing.Sequence[UpdateCollectionRequestBodyItem]

        transaction_window : typing.Optional[int]
            Maximum number of entities per transactional batch. Default 100,
            maximum 1000; values outside (0, 1000] are rejected with 400
            BAD_REQUEST. Collections exceeding the window are split into
            multiple transactional batches committed sequentially. The
            response is an array with one element per chunk in commit order;
            chunks committed before any later failure remain durable.

        transaction_timeout_millis : typing.Optional[int]
            Maximum time in milliseconds allowed for transaction completion.
            Accepted for Cyoda Cloud API parity. Behavior is
            storage-engine-plugin dependent — not every plugin honors this
            field; consult the runtime plugin's documentation for the
            supported behavior.

        wait_for_consistency_after : typing.Optional[bool]
            If true, waits for consistency after operation completes.
            Accepted for Cyoda Cloud API parity. Behavior is
            storage-engine-plugin dependent — not every plugin honors this
            field; consult the runtime plugin's documentation for the
            supported behavior.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EntityTransactionResponse]
            Collection updated successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"entity/{encode_path_param(format)}",
            method="PUT",
            params={
                "transactionWindow": transaction_window,
                "transactionTimeoutMillis": transaction_timeout_millis,
                "waitForConsistencyAfter": wait_for_consistency_after,
            },
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[UpdateCollectionRequestBodyItem], direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EntityTransactionResponse,
                    parse_obj_as(
                        type_=EntityTransactionResponse,
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

    async def update_single_with_loopback(
        self,
        format: UpdateSingleWithLoopbackRequestFormat,
        entity_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        transaction_timeout_millis: typing.Optional[int] = None,
        wait_for_consistency_after: typing.Optional[bool] = None,
        if_match: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EntityTransactionResponse]:
        """

        Updates a single entity with a loopback transition.

        Path Parameters:
        - format: The format of the input payload (e.g., JSON, XML)
        - entityId: The UUID of the entity to update

        Request Body:
        - Entity data in the specified format


        Parameters
        ----------
        format : UpdateSingleWithLoopbackRequestFormat
            Format of the input payload

        entity_id : str
            The unique identifier (UUID) of the entity to update

        request : typing.Dict[str, typing.Any]

        transaction_timeout_millis : typing.Optional[int]
            Maximum time in milliseconds allowed for transaction completion.
            Operation will fail if it takes longer than this timeout.
            Accepted for Cyoda Cloud API parity. Behavior is
            storage-engine-plugin dependent — not every plugin honors this
            field; consult the runtime plugin's documentation for the
            supported behavior.

        wait_for_consistency_after : typing.Optional[bool]
            If true, waits for the consistency time to pass before responding.
            May increase response time but guarantees data consistency when
            returning, so that subsequent calls will see the updated data.
            Accepted for Cyoda Cloud API parity. Behavior is
            storage-engine-plugin dependent — not every plugin honors this
            field; consult the runtime plugin's documentation for the
            supported behavior.

        if_match : typing.Optional[str]
            Transaction ID of the entity version the client last read. If the entity has been modified since, returns 412 Precondition Failed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EntityTransactionResponse]
            Entity updated successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"entity/{encode_path_param(format)}/{encode_path_param(entity_id)}",
            method="PUT",
            params={
                "transactionTimeoutMillis": transaction_timeout_millis,
                "waitForConsistencyAfter": wait_for_consistency_after,
            },
            json=request,
            headers={
                "content-type": "application/json",
                "If-Match": str(if_match) if if_match is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EntityTransactionResponse,
                    parse_obj_as(
                        type_=EntityTransactionResponse,
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

    async def update_single(
        self,
        format: UpdateSingleRequestFormat,
        entity_id: str,
        transition: str,
        *,
        request: typing.Dict[str, typing.Any],
        transaction_timeout_millis: typing.Optional[int] = None,
        wait_for_consistency_after: typing.Optional[bool] = None,
        if_match: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EntityTransactionResponse]:
        """

        Updates a single entity.

        Path Parameters:
        - format: The format of the input payload (e.g., JSON, XML)
        - entityId: The UUID of the entity to update
        - transition: The transition to apply to the entity

        Request Body:
        - Entity data in the specified format


        Parameters
        ----------
        format : UpdateSingleRequestFormat
            Format of the input payload

        entity_id : str
            The unique identifier (UUID) of the entity to update

        transition : str
            The transition state to apply to the entity (e.g., 'UPDATE', 'PUBLISH')

        request : typing.Dict[str, typing.Any]

        transaction_timeout_millis : typing.Optional[int]
            Maximum time in milliseconds allowed for transaction completion.
            Operation will fail if it takes longer than this timeout.
            Accepted for Cyoda Cloud API parity. Behavior is
            storage-engine-plugin dependent — not every plugin honors this
            field; consult the runtime plugin's documentation for the
            supported behavior.

        wait_for_consistency_after : typing.Optional[bool]
            If true, waits for the consistency time to pass before responding.
            May increase response time but guarantees data consistency when
            returning, so that subsequent calls will see the updated data.
            Accepted for Cyoda Cloud API parity. Behavior is
            storage-engine-plugin dependent — not every plugin honors this
            field; consult the runtime plugin's documentation for the
            supported behavior.

        if_match : typing.Optional[str]
            Transaction ID of the entity version the client last read. If the entity has been modified since, returns 412 Precondition Failed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EntityTransactionResponse]
            Entity updated successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"entity/{encode_path_param(format)}/{encode_path_param(entity_id)}/{encode_path_param(transition)}",
            method="PUT",
            params={
                "transactionTimeoutMillis": transaction_timeout_millis,
                "waitForConsistencyAfter": wait_for_consistency_after,
            },
            json=request,
            headers={
                "content-type": "application/json",
                "If-Match": str(if_match) if if_match is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EntityTransactionResponse,
                    parse_obj_as(
                        type_=EntityTransactionResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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

    async def create(
        self,
        format: CreateRequestFormat,
        entity_name: str,
        model_version: int,
        *,
        request: typing.Dict[str, typing.Any],
        transaction_window: typing.Optional[int] = None,
        transaction_timeout_millis: typing.Optional[int] = None,
        wait_for_consistency_after: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EntityTransactionResponse]:
        """

        Saves a new entity or a collection of entities of the same type.

        Path Parameters:
        * format: The format of the input payload (e.g., JSON, XML)
        * entityName: The name of the entity model
        * modelVersion: The version number of the entity model

        Request Body:
        - A string containing the entity data in the specified format


        Parameters
        ----------
        format : CreateRequestFormat
            Format of the input payload

        entity_name : str
            Name of the entity model

        model_version : int
            Version number of the entity model

        request : typing.Dict[str, typing.Any]

        transaction_window : typing.Optional[int]
            Maximum number of entities per transactional batch. Applies only
            when the request body is a JSON array; ignored for single-object
            bodies. Default 100, maximum 1000; values outside (0, 1000] are
            rejected with 400 BAD_REQUEST. Array bodies exceeding the window
            are split into multiple transactional batches committed
            sequentially. The response is then an array with one element per
            chunk in commit order; chunks committed before any later failure
            remain durable.

        transaction_timeout_millis : typing.Optional[int]
            Maximum time in milliseconds for transaction completion.
            Accepted for Cyoda Cloud API parity. Behavior is
            storage-engine-plugin dependent — not every plugin honors this
            field; consult the runtime plugin's documentation for the
            supported behavior.

        wait_for_consistency_after : typing.Optional[bool]
            If true, waits for consistency after the operation completes.
            Accepted for Cyoda Cloud API parity. Behavior is
            storage-engine-plugin dependent — not every plugin honors this
            field; consult the runtime plugin's documentation for the
            supported behavior.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EntityTransactionResponse]
            Entity created successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"entity/{encode_path_param(format)}/{encode_path_param(entity_name)}/{encode_path_param(model_version)}",
            method="POST",
            params={
                "transactionWindow": transaction_window,
                "transactionTimeoutMillis": transaction_timeout_millis,
                "waitForConsistencyAfter": wait_for_consistency_after,
            },
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EntityTransactionResponse,
                    parse_obj_as(
                        type_=EntityTransactionResponse,
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

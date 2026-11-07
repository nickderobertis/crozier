

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.entity_change_meta import EntityChangeMeta
from ..types.entity_transaction_response import EntityTransactionResponse
from ..types.json_node import JsonNode
from ..types.model_state_stats_dto import ModelStateStatsDto
from ..types.model_stats_dto import ModelStatsDto
from ..types.single_delete_result import SingleDeleteResult
from ..types.stream_delete_result import StreamDeleteResult
from .raw_client import AsyncRawEntityManagementClient, RawEntityManagementClient
from .types.create_collection_request_format import CreateCollectionRequestFormat
from .types.create_request_format import CreateRequestFormat
from .types.update_collection_request_body_item import UpdateCollectionRequestBodyItem
from .types.update_collection_request_format import UpdateCollectionRequestFormat
from .types.update_single_request_format import UpdateSingleRequestFormat
from .types.update_single_with_loopback_request_format import UpdateSingleWithLoopbackRequestFormat


OMIT = typing.cast(typing.Any, ...)


class EntityManagementClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEntityManagementClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEntityManagementClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEntityManagementClient
        """
        return self._raw_client

    def get_entity_statistics(
        self,
        *,
        point_in_time: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ModelStatsDto:
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
        ModelStatsDto
            Statistics retrieved successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.entity_management.get_entity_statistics()
        """
        _response = self._raw_client.get_entity_statistics(point_in_time=point_in_time, request_options=request_options)
        return _response.data

    def get_entity_statistics_by_state(
        self,
        *,
        point_in_time: typing.Optional[dt.datetime] = None,
        states: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ModelStateStatsDto:
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
        ModelStateStatsDto
            Statistics by state retrieved successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.entity_management.get_entity_statistics_by_state()
        """
        _response = self._raw_client.get_entity_statistics_by_state(
            point_in_time=point_in_time, states=states, request_options=request_options
        )
        return _response.data

    def get_entity_statistics_by_state_for_model(
        self,
        entity_name: str,
        model_version: int,
        *,
        point_in_time: typing.Optional[dt.datetime] = None,
        states: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ModelStateStatsDto:
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
        ModelStateStatsDto
            Statistics by state retrieved successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.entity_management.get_entity_statistics_by_state_for_model(
            entity_name="entityName",
            model_version=1,
        )
        """
        _response = self._raw_client.get_entity_statistics_by_state_for_model(
            entity_name, model_version, point_in_time=point_in_time, states=states, request_options=request_options
        )
        return _response.data

    def get_entity_statistics_for_model(
        self,
        entity_name: str,
        model_version: int,
        *,
        point_in_time: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ModelStatsDto:
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
        ModelStatsDto
            Statistics retrieved successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.entity_management.get_entity_statistics_for_model(
            entity_name="entityName",
            model_version=1,
        )
        """
        _response = self._raw_client.get_entity_statistics_for_model(
            entity_name, model_version, point_in_time=point_in_time, request_options=request_options
        )
        return _response.data

    def get_one_entity(
        self,
        entity_id: str,
        *,
        point_in_time: typing.Optional[dt.datetime] = None,
        transaction_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
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
        typing.Dict[str, typing.Any]
            Successfully retrieved the entity

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.entity_management.get_one_entity(
            entity_id="1d1e1b10-1155-11f0-bcd5-ae468cd3ed16",
            transaction_id="1d1e1b10-1155-11f0-bcd5-ae468cd3ed16",
        )
        """
        _response = self._raw_client.get_one_entity(
            entity_id, point_in_time=point_in_time, transaction_id=transaction_id, request_options=request_options
        )
        return _response.data

    def delete_single_entity(
        self, entity_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SingleDeleteResult:
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
        SingleDeleteResult
            Successfully deleted the entity

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.entity_management.delete_single_entity(
            entity_id="123e4567-e89b-12d3-a456-426614174000",
        )
        """
        _response = self._raw_client.delete_single_entity(entity_id, request_options=request_options)
        return _response.data

    def get_entity_changes_metadata(
        self,
        entity_id: str,
        *,
        point_in_time: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EntityChangeMeta:
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
        EntityChangeMeta
            Successfully retrieved entity changes metadata

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.entity_management.get_entity_changes_metadata(
            entity_id="1d1e1b10-1155-11f0-bcd5-ae468cd3ed16",
        )
        """
        _response = self._raw_client.get_entity_changes_metadata(
            entity_id, point_in_time=point_in_time, request_options=request_options
        )
        return _response.data

    def get_all_entities(
        self,
        entity_name: str,
        model_version: int,
        *,
        page_size: typing.Optional[int] = None,
        page_number: typing.Optional[int] = None,
        point_in_time: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JsonNode:
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
        JsonNode
            Successfully retrieved entities

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.entity_management.get_all_entities(
            entity_name="entityName",
            model_version=1,
        )
        """
        _response = self._raw_client.get_all_entities(
            entity_name,
            model_version,
            page_size=page_size,
            page_number=page_number,
            point_in_time=point_in_time,
            request_options=request_options,
        )
        return _response.data

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
    ) -> StreamDeleteResult:
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
        StreamDeleteResult
            Deletion process was successful. In case there were entities that could not be deletedthe response will contain information about that

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.entity_management.delete_entities(
            entity_name="nobel-prize",
            model_version=1,
            type="group",
        )
        """
        _response = self._raw_client.delete_entities(
            entity_name,
            model_version,
            type=type,
            transaction_size=transaction_size,
            point_in_time=point_in_time,
            verbose=verbose,
            request_options=request_options,
        )
        return _response.data

    def create_collection(
        self,
        format: CreateCollectionRequestFormat,
        *,
        request: typing.Dict[str, typing.Any],
        transaction_window: typing.Optional[int] = None,
        transaction_timeout_millis: typing.Optional[int] = None,
        wait_for_consistency_after: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EntityTransactionResponse:
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
        EntityTransactionResponse
            Collection created successfully

        Examples
        --------
        from fern.entity_management import CreateCollectionRequestFormat

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.entity_management.create_collection(
            format=CreateCollectionRequestFormat.JSON,
            request={
                "0": {
                    "model": {"name": "family", "version": 1},
                    "payload": '{\n  "firstName" : "John",\n  "middleName" : "Henry",\n  "lastName" : "Doe",\n  "birthdate" : "1964-04-18",\n  "married" : true,\n  "children" : [ {\n    "firstName" : "Jane",\n    "middleName" : "Marie",\n    "lastName" : "Doe",\n    "birthdate" : "1990-08-25",\n    "married" : false\n  }, {\n    "firstName" : "James",\n    "middleName" : "Robert",\n    "lastName" : "Doe",\n    "birthdate" : "1992-03-15",\n    "married" : true\n  } ]\n}',
                },
                "1": {
                    "model": {"name": "nobel-prize", "version": 1},
                    "payload": '{\n  "category" : "economics",\n  "laureates" : [ {\n    "firstname" : "Daron",\n    "surname" : "Acemoglu",\n    "id" : "1044",\n    "motivation" : "\\"for studies of how institutions are formed and affect prosperity\\"",\n    "share" : "3"\n  }, {\n    "firstname" : "Simon",\n    "surname" : "Johnson",\n    "id" : "1045",\n    "motivation" : "\\"for studies of how institutions are formed and affect prosperity\\"",\n    "share" : "3"\n  }, {\n    "firstname" : "James",\n    "surname" : "Robinson",\n    "id" : "1046",\n    "motivation" : "\\"for studies of how institutions are formed and affect prosperity\\"",\n    "share" : "3"\n  } ],\n  "year" : "2024"\n}',
                },
            },
        )
        """
        _response = self._raw_client.create_collection(
            format,
            request=request,
            transaction_window=transaction_window,
            transaction_timeout_millis=transaction_timeout_millis,
            wait_for_consistency_after=wait_for_consistency_after,
            request_options=request_options,
        )
        return _response.data

    def update_collection(
        self,
        format: UpdateCollectionRequestFormat,
        *,
        request: typing.Sequence[UpdateCollectionRequestBodyItem],
        transaction_window: typing.Optional[int] = None,
        transaction_timeout_millis: typing.Optional[int] = None,
        wait_for_consistency_after: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EntityTransactionResponse:
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
        EntityTransactionResponse
            Collection updated successfully

        Examples
        --------
        from fern.entity_management import (
            UpdateCollectionRequestBodyItem,
            UpdateCollectionRequestFormat,
        )

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.entity_management.update_collection(
            format=UpdateCollectionRequestFormat.JSON,
            request=[
                UpdateCollectionRequestBodyItem(
                    id="8824c480-c166-11ee-9e63-ae468cd3ed16",
                    payload='{\n  "firstName" : "John",\n  "middleName" : "Henry",\n  "lastName" : "Doe",\n  "birthdate" : "1964-04-18",\n  "married" : true,\n  "children" : [ {\n    "firstName" : "Jane",\n    "middleName" : "Marie",\n    "lastName" : "Doe",\n    "birthdate" : "1990-08-25",\n    "married" : false\n  }, {\n    "firstName" : "James",\n    "middleName" : "Robert",\n    "lastName" : "Doe",\n    "birthdate" : "1992-03-15",\n    "married" : true\n  } ]\n}',
                    transition="UPDATE",
                ),
                UpdateCollectionRequestBodyItem(
                    id="31134900-d9cb-11ee-9e63-ae468cd3ed16",
                    payload='{\n  "category" : "economics",\n  "laureates" : [ {\n    "firstname" : "Daron",\n    "surname" : "Acemoglu",\n    "id" : "1044",\n    "motivation" : "\\"for studies of how institutions are formed and affect prosperity\\"",\n    "share" : "3"\n  }, {\n    "firstname" : "Simon",\n    "surname" : "Johnson",\n    "id" : "1045",\n    "motivation" : "\\"for studies of how institutions are formed and affect prosperity\\"",\n    "share" : "3"\n  }, {\n    "firstname" : "James",\n    "surname" : "Robinson",\n    "id" : "1046",\n    "motivation" : "\\"for studies of how institutions are formed and affect prosperity\\"",\n    "share" : "3"\n  } ],\n  "year" : "2024"\n}',
                    transition="UPDATE",
                ),
            ],
        )
        """
        _response = self._raw_client.update_collection(
            format,
            request=request,
            transaction_window=transaction_window,
            transaction_timeout_millis=transaction_timeout_millis,
            wait_for_consistency_after=wait_for_consistency_after,
            request_options=request_options,
        )
        return _response.data

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
    ) -> EntityTransactionResponse:
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
        EntityTransactionResponse
            Entity updated successfully

        Examples
        --------
        from fern.entity_management import UpdateSingleWithLoopbackRequestFormat

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.entity_management.update_single_with_loopback(
            format=UpdateSingleWithLoopbackRequestFormat.JSON,
            entity_id="1d1e1b10-1155-11f0-bcd5-ae468cd3ed16",
            request={
                "category": "physics",
                "laureates": [
                    {
                        "firstname": "John",
                        "surname": "Hopfield",
                        "id": "1037",
                        "motivation": '"for foundational discoveries and inventions that enable machine learning with artificial neural networks"',
                        "share": "2",
                    },
                    {
                        "firstname": "Geoffrey",
                        "surname": "Hinton",
                        "id": "1038",
                        "motivation": '"for foundational discoveries and inventions that enable machine learning with artificial neural networks"',
                        "share": "2",
                    },
                ],
                "year": "2024",
            },
        )
        """
        _response = self._raw_client.update_single_with_loopback(
            format,
            entity_id,
            request=request,
            transaction_timeout_millis=transaction_timeout_millis,
            wait_for_consistency_after=wait_for_consistency_after,
            if_match=if_match,
            request_options=request_options,
        )
        return _response.data

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
    ) -> EntityTransactionResponse:
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
        EntityTransactionResponse
            Entity updated successfully

        Examples
        --------
        from fern.entity_management import UpdateSingleRequestFormat

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.entity_management.update_single(
            format=UpdateSingleRequestFormat.JSON,
            entity_id="1d1e1b10-1155-11f0-bcd5-ae468cd3ed16",
            transition="UPDATE",
            request={
                "category": "physics",
                "laureates": [
                    {
                        "firstname": "John",
                        "surname": "Hopfield",
                        "id": "1037",
                        "motivation": '"for foundational discoveries and inventions that enable machine learning with artificial neural networks"',
                        "share": "2",
                    },
                    {
                        "firstname": "Geoffrey",
                        "surname": "Hinton",
                        "id": "1038",
                        "motivation": '"for foundational discoveries and inventions that enable machine learning with artificial neural networks"',
                        "share": "2",
                    },
                ],
                "year": "2024",
            },
        )
        """
        _response = self._raw_client.update_single(
            format,
            entity_id,
            transition,
            request=request,
            transaction_timeout_millis=transaction_timeout_millis,
            wait_for_consistency_after=wait_for_consistency_after,
            if_match=if_match,
            request_options=request_options,
        )
        return _response.data

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
    ) -> EntityTransactionResponse:
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
        EntityTransactionResponse
            Entity created successfully

        Examples
        --------
        from fern.entity_management import CreateRequestFormat

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.entity_management.create(
            format=CreateRequestFormat.JSON,
            entity_name="entityName",
            model_version=1,
            request={
                "category": "physics",
                "laureates": [
                    {
                        "firstname": "John",
                        "surname": "Hopfield",
                        "id": "1037",
                        "motivation": '"for foundational discoveries and inventions that enable machine learning with artificial neural networks"',
                        "share": "2",
                    },
                    {
                        "firstname": "Geoffrey",
                        "surname": "Hinton",
                        "id": "1038",
                        "motivation": '"for foundational discoveries and inventions that enable machine learning with artificial neural networks"',
                        "share": "2",
                    },
                ],
                "year": "2024",
            },
        )
        """
        _response = self._raw_client.create(
            format,
            entity_name,
            model_version,
            request=request,
            transaction_window=transaction_window,
            transaction_timeout_millis=transaction_timeout_millis,
            wait_for_consistency_after=wait_for_consistency_after,
            request_options=request_options,
        )
        return _response.data


class AsyncEntityManagementClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEntityManagementClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEntityManagementClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEntityManagementClient
        """
        return self._raw_client

    async def get_entity_statistics(
        self,
        *,
        point_in_time: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ModelStatsDto:
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
        ModelStatsDto
            Statistics retrieved successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.entity_management.get_entity_statistics()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_entity_statistics(
            point_in_time=point_in_time, request_options=request_options
        )
        return _response.data

    async def get_entity_statistics_by_state(
        self,
        *,
        point_in_time: typing.Optional[dt.datetime] = None,
        states: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ModelStateStatsDto:
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
        ModelStateStatsDto
            Statistics by state retrieved successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.entity_management.get_entity_statistics_by_state()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_entity_statistics_by_state(
            point_in_time=point_in_time, states=states, request_options=request_options
        )
        return _response.data

    async def get_entity_statistics_by_state_for_model(
        self,
        entity_name: str,
        model_version: int,
        *,
        point_in_time: typing.Optional[dt.datetime] = None,
        states: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ModelStateStatsDto:
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
        ModelStateStatsDto
            Statistics by state retrieved successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.entity_management.get_entity_statistics_by_state_for_model(
                entity_name="entityName",
                model_version=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_entity_statistics_by_state_for_model(
            entity_name, model_version, point_in_time=point_in_time, states=states, request_options=request_options
        )
        return _response.data

    async def get_entity_statistics_for_model(
        self,
        entity_name: str,
        model_version: int,
        *,
        point_in_time: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ModelStatsDto:
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
        ModelStatsDto
            Statistics retrieved successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.entity_management.get_entity_statistics_for_model(
                entity_name="entityName",
                model_version=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_entity_statistics_for_model(
            entity_name, model_version, point_in_time=point_in_time, request_options=request_options
        )
        return _response.data

    async def get_one_entity(
        self,
        entity_id: str,
        *,
        point_in_time: typing.Optional[dt.datetime] = None,
        transaction_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
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
        typing.Dict[str, typing.Any]
            Successfully retrieved the entity

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.entity_management.get_one_entity(
                entity_id="1d1e1b10-1155-11f0-bcd5-ae468cd3ed16",
                transaction_id="1d1e1b10-1155-11f0-bcd5-ae468cd3ed16",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_one_entity(
            entity_id, point_in_time=point_in_time, transaction_id=transaction_id, request_options=request_options
        )
        return _response.data

    async def delete_single_entity(
        self, entity_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SingleDeleteResult:
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
        SingleDeleteResult
            Successfully deleted the entity

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.entity_management.delete_single_entity(
                entity_id="123e4567-e89b-12d3-a456-426614174000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_single_entity(entity_id, request_options=request_options)
        return _response.data

    async def get_entity_changes_metadata(
        self,
        entity_id: str,
        *,
        point_in_time: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EntityChangeMeta:
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
        EntityChangeMeta
            Successfully retrieved entity changes metadata

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.entity_management.get_entity_changes_metadata(
                entity_id="1d1e1b10-1155-11f0-bcd5-ae468cd3ed16",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_entity_changes_metadata(
            entity_id, point_in_time=point_in_time, request_options=request_options
        )
        return _response.data

    async def get_all_entities(
        self,
        entity_name: str,
        model_version: int,
        *,
        page_size: typing.Optional[int] = None,
        page_number: typing.Optional[int] = None,
        point_in_time: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JsonNode:
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
        JsonNode
            Successfully retrieved entities

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.entity_management.get_all_entities(
                entity_name="entityName",
                model_version=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_all_entities(
            entity_name,
            model_version,
            page_size=page_size,
            page_number=page_number,
            point_in_time=point_in_time,
            request_options=request_options,
        )
        return _response.data

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
    ) -> StreamDeleteResult:
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
        StreamDeleteResult
            Deletion process was successful. In case there were entities that could not be deletedthe response will contain information about that

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.entity_management.delete_entities(
                entity_name="nobel-prize",
                model_version=1,
                type="group",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_entities(
            entity_name,
            model_version,
            type=type,
            transaction_size=transaction_size,
            point_in_time=point_in_time,
            verbose=verbose,
            request_options=request_options,
        )
        return _response.data

    async def create_collection(
        self,
        format: CreateCollectionRequestFormat,
        *,
        request: typing.Dict[str, typing.Any],
        transaction_window: typing.Optional[int] = None,
        transaction_timeout_millis: typing.Optional[int] = None,
        wait_for_consistency_after: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EntityTransactionResponse:
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
        EntityTransactionResponse
            Collection created successfully

        Examples
        --------
        import asyncio

        from fern.entity_management import CreateCollectionRequestFormat

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.entity_management.create_collection(
                format=CreateCollectionRequestFormat.JSON,
                request={
                    "0": {
                        "model": {"name": "family", "version": 1},
                        "payload": '{\n  "firstName" : "John",\n  "middleName" : "Henry",\n  "lastName" : "Doe",\n  "birthdate" : "1964-04-18",\n  "married" : true,\n  "children" : [ {\n    "firstName" : "Jane",\n    "middleName" : "Marie",\n    "lastName" : "Doe",\n    "birthdate" : "1990-08-25",\n    "married" : false\n  }, {\n    "firstName" : "James",\n    "middleName" : "Robert",\n    "lastName" : "Doe",\n    "birthdate" : "1992-03-15",\n    "married" : true\n  } ]\n}',
                    },
                    "1": {
                        "model": {"name": "nobel-prize", "version": 1},
                        "payload": '{\n  "category" : "economics",\n  "laureates" : [ {\n    "firstname" : "Daron",\n    "surname" : "Acemoglu",\n    "id" : "1044",\n    "motivation" : "\\"for studies of how institutions are formed and affect prosperity\\"",\n    "share" : "3"\n  }, {\n    "firstname" : "Simon",\n    "surname" : "Johnson",\n    "id" : "1045",\n    "motivation" : "\\"for studies of how institutions are formed and affect prosperity\\"",\n    "share" : "3"\n  }, {\n    "firstname" : "James",\n    "surname" : "Robinson",\n    "id" : "1046",\n    "motivation" : "\\"for studies of how institutions are formed and affect prosperity\\"",\n    "share" : "3"\n  } ],\n  "year" : "2024"\n}',
                    },
                },
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_collection(
            format,
            request=request,
            transaction_window=transaction_window,
            transaction_timeout_millis=transaction_timeout_millis,
            wait_for_consistency_after=wait_for_consistency_after,
            request_options=request_options,
        )
        return _response.data

    async def update_collection(
        self,
        format: UpdateCollectionRequestFormat,
        *,
        request: typing.Sequence[UpdateCollectionRequestBodyItem],
        transaction_window: typing.Optional[int] = None,
        transaction_timeout_millis: typing.Optional[int] = None,
        wait_for_consistency_after: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EntityTransactionResponse:
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
        EntityTransactionResponse
            Collection updated successfully

        Examples
        --------
        import asyncio

        from fern.entity_management import (
            UpdateCollectionRequestBodyItem,
            UpdateCollectionRequestFormat,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.entity_management.update_collection(
                format=UpdateCollectionRequestFormat.JSON,
                request=[
                    UpdateCollectionRequestBodyItem(
                        id="8824c480-c166-11ee-9e63-ae468cd3ed16",
                        payload='{\n  "firstName" : "John",\n  "middleName" : "Henry",\n  "lastName" : "Doe",\n  "birthdate" : "1964-04-18",\n  "married" : true,\n  "children" : [ {\n    "firstName" : "Jane",\n    "middleName" : "Marie",\n    "lastName" : "Doe",\n    "birthdate" : "1990-08-25",\n    "married" : false\n  }, {\n    "firstName" : "James",\n    "middleName" : "Robert",\n    "lastName" : "Doe",\n    "birthdate" : "1992-03-15",\n    "married" : true\n  } ]\n}',
                        transition="UPDATE",
                    ),
                    UpdateCollectionRequestBodyItem(
                        id="31134900-d9cb-11ee-9e63-ae468cd3ed16",
                        payload='{\n  "category" : "economics",\n  "laureates" : [ {\n    "firstname" : "Daron",\n    "surname" : "Acemoglu",\n    "id" : "1044",\n    "motivation" : "\\"for studies of how institutions are formed and affect prosperity\\"",\n    "share" : "3"\n  }, {\n    "firstname" : "Simon",\n    "surname" : "Johnson",\n    "id" : "1045",\n    "motivation" : "\\"for studies of how institutions are formed and affect prosperity\\"",\n    "share" : "3"\n  }, {\n    "firstname" : "James",\n    "surname" : "Robinson",\n    "id" : "1046",\n    "motivation" : "\\"for studies of how institutions are formed and affect prosperity\\"",\n    "share" : "3"\n  } ],\n  "year" : "2024"\n}',
                        transition="UPDATE",
                    ),
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_collection(
            format,
            request=request,
            transaction_window=transaction_window,
            transaction_timeout_millis=transaction_timeout_millis,
            wait_for_consistency_after=wait_for_consistency_after,
            request_options=request_options,
        )
        return _response.data

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
    ) -> EntityTransactionResponse:
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
        EntityTransactionResponse
            Entity updated successfully

        Examples
        --------
        import asyncio

        from fern.entity_management import UpdateSingleWithLoopbackRequestFormat

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.entity_management.update_single_with_loopback(
                format=UpdateSingleWithLoopbackRequestFormat.JSON,
                entity_id="1d1e1b10-1155-11f0-bcd5-ae468cd3ed16",
                request={
                    "category": "physics",
                    "laureates": [
                        {
                            "firstname": "John",
                            "surname": "Hopfield",
                            "id": "1037",
                            "motivation": '"for foundational discoveries and inventions that enable machine learning with artificial neural networks"',
                            "share": "2",
                        },
                        {
                            "firstname": "Geoffrey",
                            "surname": "Hinton",
                            "id": "1038",
                            "motivation": '"for foundational discoveries and inventions that enable machine learning with artificial neural networks"',
                            "share": "2",
                        },
                    ],
                    "year": "2024",
                },
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_single_with_loopback(
            format,
            entity_id,
            request=request,
            transaction_timeout_millis=transaction_timeout_millis,
            wait_for_consistency_after=wait_for_consistency_after,
            if_match=if_match,
            request_options=request_options,
        )
        return _response.data

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
    ) -> EntityTransactionResponse:
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
        EntityTransactionResponse
            Entity updated successfully

        Examples
        --------
        import asyncio

        from fern.entity_management import UpdateSingleRequestFormat

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.entity_management.update_single(
                format=UpdateSingleRequestFormat.JSON,
                entity_id="1d1e1b10-1155-11f0-bcd5-ae468cd3ed16",
                transition="UPDATE",
                request={
                    "category": "physics",
                    "laureates": [
                        {
                            "firstname": "John",
                            "surname": "Hopfield",
                            "id": "1037",
                            "motivation": '"for foundational discoveries and inventions that enable machine learning with artificial neural networks"',
                            "share": "2",
                        },
                        {
                            "firstname": "Geoffrey",
                            "surname": "Hinton",
                            "id": "1038",
                            "motivation": '"for foundational discoveries and inventions that enable machine learning with artificial neural networks"',
                            "share": "2",
                        },
                    ],
                    "year": "2024",
                },
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_single(
            format,
            entity_id,
            transition,
            request=request,
            transaction_timeout_millis=transaction_timeout_millis,
            wait_for_consistency_after=wait_for_consistency_after,
            if_match=if_match,
            request_options=request_options,
        )
        return _response.data

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
    ) -> EntityTransactionResponse:
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
        EntityTransactionResponse
            Entity created successfully

        Examples
        --------
        import asyncio

        from fern.entity_management import CreateRequestFormat

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.entity_management.create(
                format=CreateRequestFormat.JSON,
                entity_name="entityName",
                model_version=1,
                request={
                    "category": "physics",
                    "laureates": [
                        {
                            "firstname": "John",
                            "surname": "Hopfield",
                            "id": "1037",
                            "motivation": '"for foundational discoveries and inventions that enable machine learning with artificial neural networks"',
                            "share": "2",
                        },
                        {
                            "firstname": "Geoffrey",
                            "surname": "Hinton",
                            "id": "1038",
                            "motivation": '"for foundational discoveries and inventions that enable machine learning with artificial neural networks"',
                            "share": "2",
                        },
                    ],
                    "year": "2024",
                },
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(
            format,
            entity_name,
            model_version,
            request=request,
            transaction_window=transaction_window,
            transaction_timeout_millis=transaction_timeout_millis,
            wait_for_consistency_after=wait_for_consistency_after,
            request_options=request_options,
        )
        return _response.data

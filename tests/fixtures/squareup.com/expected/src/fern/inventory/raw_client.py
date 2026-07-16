

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.batch_change_inventory_response import BatchChangeInventoryResponse
from ..types.batch_retrieve_inventory_changes_response import BatchRetrieveInventoryChangesResponse
from ..types.batch_retrieve_inventory_counts_response import BatchRetrieveInventoryCountsResponse
from ..types.inventory_change import InventoryChange
from ..types.retrieve_inventory_adjustment_response import RetrieveInventoryAdjustmentResponse
from ..types.retrieve_inventory_changes_response import RetrieveInventoryChangesResponse
from ..types.retrieve_inventory_count_response import RetrieveInventoryCountResponse
from ..types.retrieve_inventory_physical_count_response import RetrieveInventoryPhysicalCountResponse
from ..types.retrieve_inventory_transfer_response import RetrieveInventoryTransferResponse


OMIT = typing.cast(typing.Any, ...)


class RawInventoryClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def deprecated_retrieve_inventory_adjustment(
        self, adjustment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RetrieveInventoryAdjustmentResponse]:
        """
        Deprecated version of [RetrieveInventoryAdjustment](https://developer.squareup.com/reference/square_2021-08-18/inventory-api/retrieve-inventory-adjustment) after the endpoint URL
        is updated to conform to the standard convention.

        Parameters
        ----------
        adjustment_id : str
            ID of the [InventoryAdjustment](https://developer.squareup.com/reference/square_2021-08-18/objects/InventoryAdjustment) to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RetrieveInventoryAdjustmentResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/inventory/adjustment/{jsonable_encoder(adjustment_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveInventoryAdjustmentResponse,
                    parse_obj_as(
                        type_=RetrieveInventoryAdjustmentResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def retrieve_inventory_adjustment(
        self, adjustment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RetrieveInventoryAdjustmentResponse]:
        """
        Returns the [InventoryAdjustment](https://developer.squareup.com/reference/square_2021-08-18/objects/InventoryAdjustment) object
        with the provided `adjustment_id`.

        Parameters
        ----------
        adjustment_id : str
            ID of the [InventoryAdjustment](https://developer.squareup.com/reference/square_2021-08-18/objects/InventoryAdjustment) to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RetrieveInventoryAdjustmentResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/inventory/adjustments/{jsonable_encoder(adjustment_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveInventoryAdjustmentResponse,
                    parse_obj_as(
                        type_=RetrieveInventoryAdjustmentResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def deprecated_batch_change_inventory(
        self,
        *,
        idempotency_key: str,
        changes: typing.Optional[typing.Sequence[InventoryChange]] = OMIT,
        ignore_unchanged_counts: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BatchChangeInventoryResponse]:
        """
        Deprecated version of [BatchChangeInventory](https://developer.squareup.com/reference/square_2021-08-18/inventory-api/batch-change-inventory) after the endpoint URL
        is updated to conform to the standard convention.

        Parameters
        ----------
        idempotency_key : str
            A client-supplied, universally unique identifier (UUID) for the
            request.

            See [Idempotency](https://developer.squareup.com/docs/basics/api101/idempotency) in the
            [API Development 101](https://developer.squareup.com/docs/basics/api101/overview) section for more
            information.

        changes : typing.Optional[typing.Sequence[InventoryChange]]
            The set of physical counts and inventory adjustments to be made.
            Changes are applied based on the client-supplied timestamp and may be sent
            out of order.

        ignore_unchanged_counts : typing.Optional[bool]
            Indicates whether the current physical count should be ignored if
            the quantity is unchanged since the last physical count. Default: `true`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BatchChangeInventoryResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/inventory/batch-change",
            method="POST",
            json={
                "changes": convert_and_respect_annotation_metadata(
                    object_=changes, annotation=typing.Sequence[InventoryChange], direction="write"
                ),
                "idempotency_key": idempotency_key,
                "ignore_unchanged_counts": ignore_unchanged_counts,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BatchChangeInventoryResponse,
                    parse_obj_as(
                        type_=BatchChangeInventoryResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def deprecated_batch_retrieve_inventory_changes(
        self,
        *,
        catalog_object_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        cursor: typing.Optional[str] = OMIT,
        location_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        states: typing.Optional[typing.Sequence[str]] = OMIT,
        types: typing.Optional[typing.Sequence[str]] = OMIT,
        updated_after: typing.Optional[str] = OMIT,
        updated_before: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BatchRetrieveInventoryChangesResponse]:
        """
        Deprecated version of [BatchRetrieveInventoryChanges](https://developer.squareup.com/reference/square_2021-08-18/inventory-api/batch-retrieve-inventory-changes) after the endpoint URL
        is updated to conform to the standard convention.

        Parameters
        ----------
        catalog_object_ids : typing.Optional[typing.Sequence[str]]
            The filter to return results by `CatalogObject` ID.
            The filter is only applicable when set. The default value is null.

        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this to retrieve the next set of results for the original query.

            See the [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination) guide for more information.

        location_ids : typing.Optional[typing.Sequence[str]]
            The filter to return results by `Location` ID.
            The filter is only applicable when set. The default value is null.

        states : typing.Optional[typing.Sequence[str]]
            The filter to return `ADJUSTMENT` query results by
            `InventoryState`. This filter is only applied when set.
            The default value is null.

        types : typing.Optional[typing.Sequence[str]]
            The filter to return results by `InventoryChangeType` values other than `TRANSFER`.
            The default value is `[PHYSICAL_COUNT, ADJUSTMENT]`.

        updated_after : typing.Optional[str]
            The filter to return results with their `calculated_at` value
            after the given time as specified in an RFC 3339 timestamp.
            The default value is the UNIX epoch of (`1970-01-01T00:00:00Z`).

        updated_before : typing.Optional[str]
            The filter to return results with their `created_at` or `calculated_at` value
            strictly before the given time as specified in an RFC 3339 timestamp.
            The default value is the UNIX epoch of (`1970-01-01T00:00:00Z`).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BatchRetrieveInventoryChangesResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/inventory/batch-retrieve-changes",
            method="POST",
            json={
                "catalog_object_ids": catalog_object_ids,
                "cursor": cursor,
                "location_ids": location_ids,
                "states": states,
                "types": types,
                "updated_after": updated_after,
                "updated_before": updated_before,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BatchRetrieveInventoryChangesResponse,
                    parse_obj_as(
                        type_=BatchRetrieveInventoryChangesResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def deprecated_batch_retrieve_inventory_counts(
        self,
        *,
        catalog_object_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        cursor: typing.Optional[str] = OMIT,
        location_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        states: typing.Optional[typing.Sequence[str]] = OMIT,
        updated_after: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BatchRetrieveInventoryCountsResponse]:
        """
        Deprecated version of [BatchRetrieveInventoryCounts](https://developer.squareup.com/reference/square_2021-08-18/inventory-api/batch-retrieve-inventory-counts) after the endpoint URL
        is updated to conform to the standard convention.

        Parameters
        ----------
        catalog_object_ids : typing.Optional[typing.Sequence[str]]
            The filter to return results by `CatalogObject` ID.
            The filter is applicable only when set.  The default is null.

        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this to retrieve the next set of results for the original query.

            See the [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination) guide for more information.

        location_ids : typing.Optional[typing.Sequence[str]]
            The filter to return results by `Location` ID.
            This filter is applicable only when set. The default is null.

        states : typing.Optional[typing.Sequence[str]]
            The filter to return results by `InventoryState`. The filter is only applicable when set.
            Ignored are untracked states of `NONE`, `SOLD`, and `UNLINKED_RETURN`.
            The default is null.

        updated_after : typing.Optional[str]
            The filter to return results with their `calculated_at` value
            after the given time as specified in an RFC 3339 timestamp.
            The default value is the UNIX epoch of (`1970-01-01T00:00:00Z`).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BatchRetrieveInventoryCountsResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/inventory/batch-retrieve-counts",
            method="POST",
            json={
                "catalog_object_ids": catalog_object_ids,
                "cursor": cursor,
                "location_ids": location_ids,
                "states": states,
                "updated_after": updated_after,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BatchRetrieveInventoryCountsResponse,
                    parse_obj_as(
                        type_=BatchRetrieveInventoryCountsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def batch_change_inventory(
        self,
        *,
        idempotency_key: str,
        changes: typing.Optional[typing.Sequence[InventoryChange]] = OMIT,
        ignore_unchanged_counts: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BatchChangeInventoryResponse]:
        """
        Applies adjustments and counts to the provided item quantities.

        On success: returns the current calculated counts for all objects
        referenced in the request.
        On failure: returns a list of related errors.

        Parameters
        ----------
        idempotency_key : str
            A client-supplied, universally unique identifier (UUID) for the
            request.

            See [Idempotency](https://developer.squareup.com/docs/basics/api101/idempotency) in the
            [API Development 101](https://developer.squareup.com/docs/basics/api101/overview) section for more
            information.

        changes : typing.Optional[typing.Sequence[InventoryChange]]
            The set of physical counts and inventory adjustments to be made.
            Changes are applied based on the client-supplied timestamp and may be sent
            out of order.

        ignore_unchanged_counts : typing.Optional[bool]
            Indicates whether the current physical count should be ignored if
            the quantity is unchanged since the last physical count. Default: `true`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BatchChangeInventoryResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/inventory/changes/batch-create",
            method="POST",
            json={
                "changes": convert_and_respect_annotation_metadata(
                    object_=changes, annotation=typing.Sequence[InventoryChange], direction="write"
                ),
                "idempotency_key": idempotency_key,
                "ignore_unchanged_counts": ignore_unchanged_counts,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BatchChangeInventoryResponse,
                    parse_obj_as(
                        type_=BatchChangeInventoryResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def batch_retrieve_inventory_changes(
        self,
        *,
        catalog_object_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        cursor: typing.Optional[str] = OMIT,
        location_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        states: typing.Optional[typing.Sequence[str]] = OMIT,
        types: typing.Optional[typing.Sequence[str]] = OMIT,
        updated_after: typing.Optional[str] = OMIT,
        updated_before: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BatchRetrieveInventoryChangesResponse]:
        """
        Returns historical physical counts and adjustments based on the
        provided filter criteria.

        Results are paginated and sorted in ascending order according their
        `occurred_at` timestamp (oldest first).

        BatchRetrieveInventoryChanges is a catch-all query endpoint for queries
        that cannot be handled by other, simpler endpoints.

        Parameters
        ----------
        catalog_object_ids : typing.Optional[typing.Sequence[str]]
            The filter to return results by `CatalogObject` ID.
            The filter is only applicable when set. The default value is null.

        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this to retrieve the next set of results for the original query.

            See the [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination) guide for more information.

        location_ids : typing.Optional[typing.Sequence[str]]
            The filter to return results by `Location` ID.
            The filter is only applicable when set. The default value is null.

        states : typing.Optional[typing.Sequence[str]]
            The filter to return `ADJUSTMENT` query results by
            `InventoryState`. This filter is only applied when set.
            The default value is null.

        types : typing.Optional[typing.Sequence[str]]
            The filter to return results by `InventoryChangeType` values other than `TRANSFER`.
            The default value is `[PHYSICAL_COUNT, ADJUSTMENT]`.

        updated_after : typing.Optional[str]
            The filter to return results with their `calculated_at` value
            after the given time as specified in an RFC 3339 timestamp.
            The default value is the UNIX epoch of (`1970-01-01T00:00:00Z`).

        updated_before : typing.Optional[str]
            The filter to return results with their `created_at` or `calculated_at` value
            strictly before the given time as specified in an RFC 3339 timestamp.
            The default value is the UNIX epoch of (`1970-01-01T00:00:00Z`).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BatchRetrieveInventoryChangesResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/inventory/changes/batch-retrieve",
            method="POST",
            json={
                "catalog_object_ids": catalog_object_ids,
                "cursor": cursor,
                "location_ids": location_ids,
                "states": states,
                "types": types,
                "updated_after": updated_after,
                "updated_before": updated_before,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BatchRetrieveInventoryChangesResponse,
                    parse_obj_as(
                        type_=BatchRetrieveInventoryChangesResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def batch_retrieve_inventory_counts(
        self,
        *,
        catalog_object_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        cursor: typing.Optional[str] = OMIT,
        location_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        states: typing.Optional[typing.Sequence[str]] = OMIT,
        updated_after: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BatchRetrieveInventoryCountsResponse]:
        """
        Returns current counts for the provided
        [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject)s at the requested
        [Location](https://developer.squareup.com/reference/square_2021-08-18/objects/Location)s.

        Results are paginated and sorted in descending order according to their
        `calculated_at` timestamp (newest first).

        When `updated_after` is specified, only counts that have changed since that
        time (based on the server timestamp for the most recent change) are
        returned. This allows clients to perform a "sync" operation, for example
        in response to receiving a Webhook notification.

        Parameters
        ----------
        catalog_object_ids : typing.Optional[typing.Sequence[str]]
            The filter to return results by `CatalogObject` ID.
            The filter is applicable only when set.  The default is null.

        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this to retrieve the next set of results for the original query.

            See the [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination) guide for more information.

        location_ids : typing.Optional[typing.Sequence[str]]
            The filter to return results by `Location` ID.
            This filter is applicable only when set. The default is null.

        states : typing.Optional[typing.Sequence[str]]
            The filter to return results by `InventoryState`. The filter is only applicable when set.
            Ignored are untracked states of `NONE`, `SOLD`, and `UNLINKED_RETURN`.
            The default is null.

        updated_after : typing.Optional[str]
            The filter to return results with their `calculated_at` value
            after the given time as specified in an RFC 3339 timestamp.
            The default value is the UNIX epoch of (`1970-01-01T00:00:00Z`).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BatchRetrieveInventoryCountsResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/inventory/counts/batch-retrieve",
            method="POST",
            json={
                "catalog_object_ids": catalog_object_ids,
                "cursor": cursor,
                "location_ids": location_ids,
                "states": states,
                "updated_after": updated_after,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BatchRetrieveInventoryCountsResponse,
                    parse_obj_as(
                        type_=BatchRetrieveInventoryCountsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def deprecated_retrieve_inventory_physical_count(
        self, physical_count_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RetrieveInventoryPhysicalCountResponse]:
        """
        Deprecated version of [RetrieveInventoryPhysicalCount](https://developer.squareup.com/reference/square_2021-08-18/inventory-api/retrieve-inventory-physical-count) after the endpoint URL
        is updated to conform to the standard convention.

        Parameters
        ----------
        physical_count_id : str
            ID of the
            [InventoryPhysicalCount](https://developer.squareup.com/reference/square_2021-08-18/objects/InventoryPhysicalCount) to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RetrieveInventoryPhysicalCountResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/inventory/physical-count/{jsonable_encoder(physical_count_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveInventoryPhysicalCountResponse,
                    parse_obj_as(
                        type_=RetrieveInventoryPhysicalCountResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def retrieve_inventory_physical_count(
        self, physical_count_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RetrieveInventoryPhysicalCountResponse]:
        """
        Returns the [InventoryPhysicalCount](https://developer.squareup.com/reference/square_2021-08-18/objects/InventoryPhysicalCount)
        object with the provided `physical_count_id`.

        Parameters
        ----------
        physical_count_id : str
            ID of the
            [InventoryPhysicalCount](https://developer.squareup.com/reference/square_2021-08-18/objects/InventoryPhysicalCount) to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RetrieveInventoryPhysicalCountResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/inventory/physical-counts/{jsonable_encoder(physical_count_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveInventoryPhysicalCountResponse,
                    parse_obj_as(
                        type_=RetrieveInventoryPhysicalCountResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def retrieve_inventory_transfer(
        self, transfer_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RetrieveInventoryTransferResponse]:
        """
        Returns the [InventoryTransfer](https://developer.squareup.com/reference/square_2021-08-18/objects/InventoryTransfer) object
        with the provided `transfer_id`.

        Parameters
        ----------
        transfer_id : str
            ID of the [InventoryTransfer](https://developer.squareup.com/reference/square_2021-08-18/objects/InventoryTransfer) to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RetrieveInventoryTransferResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/inventory/transfers/{jsonable_encoder(transfer_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveInventoryTransferResponse,
                    parse_obj_as(
                        type_=RetrieveInventoryTransferResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def retrieve_inventory_count(
        self,
        catalog_object_id: str,
        *,
        location_ids: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[RetrieveInventoryCountResponse]:
        """
        Retrieves the current calculated stock count for a given
        [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject) at a given set of
        [Location](https://developer.squareup.com/reference/square_2021-08-18/objects/Location)s. Responses are paginated and unsorted.
        For more sophisticated queries, use a batch endpoint.

        Parameters
        ----------
        catalog_object_id : str
            ID of the [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject) to retrieve.

        location_ids : typing.Optional[str]
            The [Location](https://developer.squareup.com/reference/square_2021-08-18/objects/Location) IDs to look up as a comma-separated
            list. An empty list queries all locations.

        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this to retrieve the next set of results for the original query.

            See the [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination) guide for more information.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RetrieveInventoryCountResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/inventory/{jsonable_encoder(catalog_object_id)}",
            method="GET",
            params={
                "location_ids": location_ids,
                "cursor": cursor,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveInventoryCountResponse,
                    parse_obj_as(
                        type_=RetrieveInventoryCountResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def retrieve_inventory_changes(
        self,
        catalog_object_id: str,
        *,
        location_ids: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[RetrieveInventoryChangesResponse]:
        """
        Returns a set of physical counts and inventory adjustments for the
        provided [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject) at the requested
        [Location](https://developer.squareup.com/reference/square_2021-08-18/objects/Location)s.

        You can achieve the same result by calling [BatchRetrieveInventoryChanges](https://developer.squareup.com/reference/square_2021-08-18/inventory-api/batch-retrieve-inventory-changes)
        and having the `catalog_object_ids` list contain a single element of the `CatalogObject` ID.

        Results are paginated and sorted in descending order according to their
        `occurred_at` timestamp (newest first).

        There are no limits on how far back the caller can page. This endpoint can be
        used to display recent changes for a specific item. For more
        sophisticated queries, use a batch endpoint.

        Parameters
        ----------
        catalog_object_id : str
            ID of the [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject) to retrieve.

        location_ids : typing.Optional[str]
            The [Location](https://developer.squareup.com/reference/square_2021-08-18/objects/Location) IDs to look up as a comma-separated
            list. An empty list queries all locations.

        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this to retrieve the next set of results for the original query.

            See the [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination) guide for more information.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RetrieveInventoryChangesResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/inventory/{jsonable_encoder(catalog_object_id)}/changes",
            method="GET",
            params={
                "location_ids": location_ids,
                "cursor": cursor,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveInventoryChangesResponse,
                    parse_obj_as(
                        type_=RetrieveInventoryChangesResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawInventoryClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def deprecated_retrieve_inventory_adjustment(
        self, adjustment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RetrieveInventoryAdjustmentResponse]:
        """
        Deprecated version of [RetrieveInventoryAdjustment](https://developer.squareup.com/reference/square_2021-08-18/inventory-api/retrieve-inventory-adjustment) after the endpoint URL
        is updated to conform to the standard convention.

        Parameters
        ----------
        adjustment_id : str
            ID of the [InventoryAdjustment](https://developer.squareup.com/reference/square_2021-08-18/objects/InventoryAdjustment) to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RetrieveInventoryAdjustmentResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/inventory/adjustment/{jsonable_encoder(adjustment_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveInventoryAdjustmentResponse,
                    parse_obj_as(
                        type_=RetrieveInventoryAdjustmentResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def retrieve_inventory_adjustment(
        self, adjustment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RetrieveInventoryAdjustmentResponse]:
        """
        Returns the [InventoryAdjustment](https://developer.squareup.com/reference/square_2021-08-18/objects/InventoryAdjustment) object
        with the provided `adjustment_id`.

        Parameters
        ----------
        adjustment_id : str
            ID of the [InventoryAdjustment](https://developer.squareup.com/reference/square_2021-08-18/objects/InventoryAdjustment) to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RetrieveInventoryAdjustmentResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/inventory/adjustments/{jsonable_encoder(adjustment_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveInventoryAdjustmentResponse,
                    parse_obj_as(
                        type_=RetrieveInventoryAdjustmentResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def deprecated_batch_change_inventory(
        self,
        *,
        idempotency_key: str,
        changes: typing.Optional[typing.Sequence[InventoryChange]] = OMIT,
        ignore_unchanged_counts: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BatchChangeInventoryResponse]:
        """
        Deprecated version of [BatchChangeInventory](https://developer.squareup.com/reference/square_2021-08-18/inventory-api/batch-change-inventory) after the endpoint URL
        is updated to conform to the standard convention.

        Parameters
        ----------
        idempotency_key : str
            A client-supplied, universally unique identifier (UUID) for the
            request.

            See [Idempotency](https://developer.squareup.com/docs/basics/api101/idempotency) in the
            [API Development 101](https://developer.squareup.com/docs/basics/api101/overview) section for more
            information.

        changes : typing.Optional[typing.Sequence[InventoryChange]]
            The set of physical counts and inventory adjustments to be made.
            Changes are applied based on the client-supplied timestamp and may be sent
            out of order.

        ignore_unchanged_counts : typing.Optional[bool]
            Indicates whether the current physical count should be ignored if
            the quantity is unchanged since the last physical count. Default: `true`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BatchChangeInventoryResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/inventory/batch-change",
            method="POST",
            json={
                "changes": convert_and_respect_annotation_metadata(
                    object_=changes, annotation=typing.Sequence[InventoryChange], direction="write"
                ),
                "idempotency_key": idempotency_key,
                "ignore_unchanged_counts": ignore_unchanged_counts,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BatchChangeInventoryResponse,
                    parse_obj_as(
                        type_=BatchChangeInventoryResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def deprecated_batch_retrieve_inventory_changes(
        self,
        *,
        catalog_object_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        cursor: typing.Optional[str] = OMIT,
        location_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        states: typing.Optional[typing.Sequence[str]] = OMIT,
        types: typing.Optional[typing.Sequence[str]] = OMIT,
        updated_after: typing.Optional[str] = OMIT,
        updated_before: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BatchRetrieveInventoryChangesResponse]:
        """
        Deprecated version of [BatchRetrieveInventoryChanges](https://developer.squareup.com/reference/square_2021-08-18/inventory-api/batch-retrieve-inventory-changes) after the endpoint URL
        is updated to conform to the standard convention.

        Parameters
        ----------
        catalog_object_ids : typing.Optional[typing.Sequence[str]]
            The filter to return results by `CatalogObject` ID.
            The filter is only applicable when set. The default value is null.

        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this to retrieve the next set of results for the original query.

            See the [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination) guide for more information.

        location_ids : typing.Optional[typing.Sequence[str]]
            The filter to return results by `Location` ID.
            The filter is only applicable when set. The default value is null.

        states : typing.Optional[typing.Sequence[str]]
            The filter to return `ADJUSTMENT` query results by
            `InventoryState`. This filter is only applied when set.
            The default value is null.

        types : typing.Optional[typing.Sequence[str]]
            The filter to return results by `InventoryChangeType` values other than `TRANSFER`.
            The default value is `[PHYSICAL_COUNT, ADJUSTMENT]`.

        updated_after : typing.Optional[str]
            The filter to return results with their `calculated_at` value
            after the given time as specified in an RFC 3339 timestamp.
            The default value is the UNIX epoch of (`1970-01-01T00:00:00Z`).

        updated_before : typing.Optional[str]
            The filter to return results with their `created_at` or `calculated_at` value
            strictly before the given time as specified in an RFC 3339 timestamp.
            The default value is the UNIX epoch of (`1970-01-01T00:00:00Z`).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BatchRetrieveInventoryChangesResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/inventory/batch-retrieve-changes",
            method="POST",
            json={
                "catalog_object_ids": catalog_object_ids,
                "cursor": cursor,
                "location_ids": location_ids,
                "states": states,
                "types": types,
                "updated_after": updated_after,
                "updated_before": updated_before,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BatchRetrieveInventoryChangesResponse,
                    parse_obj_as(
                        type_=BatchRetrieveInventoryChangesResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def deprecated_batch_retrieve_inventory_counts(
        self,
        *,
        catalog_object_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        cursor: typing.Optional[str] = OMIT,
        location_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        states: typing.Optional[typing.Sequence[str]] = OMIT,
        updated_after: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BatchRetrieveInventoryCountsResponse]:
        """
        Deprecated version of [BatchRetrieveInventoryCounts](https://developer.squareup.com/reference/square_2021-08-18/inventory-api/batch-retrieve-inventory-counts) after the endpoint URL
        is updated to conform to the standard convention.

        Parameters
        ----------
        catalog_object_ids : typing.Optional[typing.Sequence[str]]
            The filter to return results by `CatalogObject` ID.
            The filter is applicable only when set.  The default is null.

        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this to retrieve the next set of results for the original query.

            See the [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination) guide for more information.

        location_ids : typing.Optional[typing.Sequence[str]]
            The filter to return results by `Location` ID.
            This filter is applicable only when set. The default is null.

        states : typing.Optional[typing.Sequence[str]]
            The filter to return results by `InventoryState`. The filter is only applicable when set.
            Ignored are untracked states of `NONE`, `SOLD`, and `UNLINKED_RETURN`.
            The default is null.

        updated_after : typing.Optional[str]
            The filter to return results with their `calculated_at` value
            after the given time as specified in an RFC 3339 timestamp.
            The default value is the UNIX epoch of (`1970-01-01T00:00:00Z`).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BatchRetrieveInventoryCountsResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/inventory/batch-retrieve-counts",
            method="POST",
            json={
                "catalog_object_ids": catalog_object_ids,
                "cursor": cursor,
                "location_ids": location_ids,
                "states": states,
                "updated_after": updated_after,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BatchRetrieveInventoryCountsResponse,
                    parse_obj_as(
                        type_=BatchRetrieveInventoryCountsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def batch_change_inventory(
        self,
        *,
        idempotency_key: str,
        changes: typing.Optional[typing.Sequence[InventoryChange]] = OMIT,
        ignore_unchanged_counts: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BatchChangeInventoryResponse]:
        """
        Applies adjustments and counts to the provided item quantities.

        On success: returns the current calculated counts for all objects
        referenced in the request.
        On failure: returns a list of related errors.

        Parameters
        ----------
        idempotency_key : str
            A client-supplied, universally unique identifier (UUID) for the
            request.

            See [Idempotency](https://developer.squareup.com/docs/basics/api101/idempotency) in the
            [API Development 101](https://developer.squareup.com/docs/basics/api101/overview) section for more
            information.

        changes : typing.Optional[typing.Sequence[InventoryChange]]
            The set of physical counts and inventory adjustments to be made.
            Changes are applied based on the client-supplied timestamp and may be sent
            out of order.

        ignore_unchanged_counts : typing.Optional[bool]
            Indicates whether the current physical count should be ignored if
            the quantity is unchanged since the last physical count. Default: `true`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BatchChangeInventoryResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/inventory/changes/batch-create",
            method="POST",
            json={
                "changes": convert_and_respect_annotation_metadata(
                    object_=changes, annotation=typing.Sequence[InventoryChange], direction="write"
                ),
                "idempotency_key": idempotency_key,
                "ignore_unchanged_counts": ignore_unchanged_counts,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BatchChangeInventoryResponse,
                    parse_obj_as(
                        type_=BatchChangeInventoryResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def batch_retrieve_inventory_changes(
        self,
        *,
        catalog_object_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        cursor: typing.Optional[str] = OMIT,
        location_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        states: typing.Optional[typing.Sequence[str]] = OMIT,
        types: typing.Optional[typing.Sequence[str]] = OMIT,
        updated_after: typing.Optional[str] = OMIT,
        updated_before: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BatchRetrieveInventoryChangesResponse]:
        """
        Returns historical physical counts and adjustments based on the
        provided filter criteria.

        Results are paginated and sorted in ascending order according their
        `occurred_at` timestamp (oldest first).

        BatchRetrieveInventoryChanges is a catch-all query endpoint for queries
        that cannot be handled by other, simpler endpoints.

        Parameters
        ----------
        catalog_object_ids : typing.Optional[typing.Sequence[str]]
            The filter to return results by `CatalogObject` ID.
            The filter is only applicable when set. The default value is null.

        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this to retrieve the next set of results for the original query.

            See the [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination) guide for more information.

        location_ids : typing.Optional[typing.Sequence[str]]
            The filter to return results by `Location` ID.
            The filter is only applicable when set. The default value is null.

        states : typing.Optional[typing.Sequence[str]]
            The filter to return `ADJUSTMENT` query results by
            `InventoryState`. This filter is only applied when set.
            The default value is null.

        types : typing.Optional[typing.Sequence[str]]
            The filter to return results by `InventoryChangeType` values other than `TRANSFER`.
            The default value is `[PHYSICAL_COUNT, ADJUSTMENT]`.

        updated_after : typing.Optional[str]
            The filter to return results with their `calculated_at` value
            after the given time as specified in an RFC 3339 timestamp.
            The default value is the UNIX epoch of (`1970-01-01T00:00:00Z`).

        updated_before : typing.Optional[str]
            The filter to return results with their `created_at` or `calculated_at` value
            strictly before the given time as specified in an RFC 3339 timestamp.
            The default value is the UNIX epoch of (`1970-01-01T00:00:00Z`).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BatchRetrieveInventoryChangesResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/inventory/changes/batch-retrieve",
            method="POST",
            json={
                "catalog_object_ids": catalog_object_ids,
                "cursor": cursor,
                "location_ids": location_ids,
                "states": states,
                "types": types,
                "updated_after": updated_after,
                "updated_before": updated_before,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BatchRetrieveInventoryChangesResponse,
                    parse_obj_as(
                        type_=BatchRetrieveInventoryChangesResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def batch_retrieve_inventory_counts(
        self,
        *,
        catalog_object_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        cursor: typing.Optional[str] = OMIT,
        location_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        states: typing.Optional[typing.Sequence[str]] = OMIT,
        updated_after: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BatchRetrieveInventoryCountsResponse]:
        """
        Returns current counts for the provided
        [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject)s at the requested
        [Location](https://developer.squareup.com/reference/square_2021-08-18/objects/Location)s.

        Results are paginated and sorted in descending order according to their
        `calculated_at` timestamp (newest first).

        When `updated_after` is specified, only counts that have changed since that
        time (based on the server timestamp for the most recent change) are
        returned. This allows clients to perform a "sync" operation, for example
        in response to receiving a Webhook notification.

        Parameters
        ----------
        catalog_object_ids : typing.Optional[typing.Sequence[str]]
            The filter to return results by `CatalogObject` ID.
            The filter is applicable only when set.  The default is null.

        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this to retrieve the next set of results for the original query.

            See the [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination) guide for more information.

        location_ids : typing.Optional[typing.Sequence[str]]
            The filter to return results by `Location` ID.
            This filter is applicable only when set. The default is null.

        states : typing.Optional[typing.Sequence[str]]
            The filter to return results by `InventoryState`. The filter is only applicable when set.
            Ignored are untracked states of `NONE`, `SOLD`, and `UNLINKED_RETURN`.
            The default is null.

        updated_after : typing.Optional[str]
            The filter to return results with their `calculated_at` value
            after the given time as specified in an RFC 3339 timestamp.
            The default value is the UNIX epoch of (`1970-01-01T00:00:00Z`).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BatchRetrieveInventoryCountsResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/inventory/counts/batch-retrieve",
            method="POST",
            json={
                "catalog_object_ids": catalog_object_ids,
                "cursor": cursor,
                "location_ids": location_ids,
                "states": states,
                "updated_after": updated_after,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BatchRetrieveInventoryCountsResponse,
                    parse_obj_as(
                        type_=BatchRetrieveInventoryCountsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def deprecated_retrieve_inventory_physical_count(
        self, physical_count_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RetrieveInventoryPhysicalCountResponse]:
        """
        Deprecated version of [RetrieveInventoryPhysicalCount](https://developer.squareup.com/reference/square_2021-08-18/inventory-api/retrieve-inventory-physical-count) after the endpoint URL
        is updated to conform to the standard convention.

        Parameters
        ----------
        physical_count_id : str
            ID of the
            [InventoryPhysicalCount](https://developer.squareup.com/reference/square_2021-08-18/objects/InventoryPhysicalCount) to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RetrieveInventoryPhysicalCountResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/inventory/physical-count/{jsonable_encoder(physical_count_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveInventoryPhysicalCountResponse,
                    parse_obj_as(
                        type_=RetrieveInventoryPhysicalCountResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def retrieve_inventory_physical_count(
        self, physical_count_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RetrieveInventoryPhysicalCountResponse]:
        """
        Returns the [InventoryPhysicalCount](https://developer.squareup.com/reference/square_2021-08-18/objects/InventoryPhysicalCount)
        object with the provided `physical_count_id`.

        Parameters
        ----------
        physical_count_id : str
            ID of the
            [InventoryPhysicalCount](https://developer.squareup.com/reference/square_2021-08-18/objects/InventoryPhysicalCount) to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RetrieveInventoryPhysicalCountResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/inventory/physical-counts/{jsonable_encoder(physical_count_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveInventoryPhysicalCountResponse,
                    parse_obj_as(
                        type_=RetrieveInventoryPhysicalCountResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def retrieve_inventory_transfer(
        self, transfer_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RetrieveInventoryTransferResponse]:
        """
        Returns the [InventoryTransfer](https://developer.squareup.com/reference/square_2021-08-18/objects/InventoryTransfer) object
        with the provided `transfer_id`.

        Parameters
        ----------
        transfer_id : str
            ID of the [InventoryTransfer](https://developer.squareup.com/reference/square_2021-08-18/objects/InventoryTransfer) to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RetrieveInventoryTransferResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/inventory/transfers/{jsonable_encoder(transfer_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveInventoryTransferResponse,
                    parse_obj_as(
                        type_=RetrieveInventoryTransferResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def retrieve_inventory_count(
        self,
        catalog_object_id: str,
        *,
        location_ids: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[RetrieveInventoryCountResponse]:
        """
        Retrieves the current calculated stock count for a given
        [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject) at a given set of
        [Location](https://developer.squareup.com/reference/square_2021-08-18/objects/Location)s. Responses are paginated and unsorted.
        For more sophisticated queries, use a batch endpoint.

        Parameters
        ----------
        catalog_object_id : str
            ID of the [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject) to retrieve.

        location_ids : typing.Optional[str]
            The [Location](https://developer.squareup.com/reference/square_2021-08-18/objects/Location) IDs to look up as a comma-separated
            list. An empty list queries all locations.

        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this to retrieve the next set of results for the original query.

            See the [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination) guide for more information.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RetrieveInventoryCountResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/inventory/{jsonable_encoder(catalog_object_id)}",
            method="GET",
            params={
                "location_ids": location_ids,
                "cursor": cursor,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveInventoryCountResponse,
                    parse_obj_as(
                        type_=RetrieveInventoryCountResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def retrieve_inventory_changes(
        self,
        catalog_object_id: str,
        *,
        location_ids: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[RetrieveInventoryChangesResponse]:
        """
        Returns a set of physical counts and inventory adjustments for the
        provided [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject) at the requested
        [Location](https://developer.squareup.com/reference/square_2021-08-18/objects/Location)s.

        You can achieve the same result by calling [BatchRetrieveInventoryChanges](https://developer.squareup.com/reference/square_2021-08-18/inventory-api/batch-retrieve-inventory-changes)
        and having the `catalog_object_ids` list contain a single element of the `CatalogObject` ID.

        Results are paginated and sorted in descending order according to their
        `occurred_at` timestamp (newest first).

        There are no limits on how far back the caller can page. This endpoint can be
        used to display recent changes for a specific item. For more
        sophisticated queries, use a batch endpoint.

        Parameters
        ----------
        catalog_object_id : str
            ID of the [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject) to retrieve.

        location_ids : typing.Optional[str]
            The [Location](https://developer.squareup.com/reference/square_2021-08-18/objects/Location) IDs to look up as a comma-separated
            list. An empty list queries all locations.

        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this to retrieve the next set of results for the original query.

            See the [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination) guide for more information.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RetrieveInventoryChangesResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/inventory/{jsonable_encoder(catalog_object_id)}/changes",
            method="GET",
            params={
                "location_ids": location_ids,
                "cursor": cursor,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveInventoryChangesResponse,
                    parse_obj_as(
                        type_=RetrieveInventoryChangesResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)



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
from ..types.v1bulk_hours_import_create_item import V1BulkHoursImportCreateItem
from ..types.v1bulk_hours_import_update_item import V1BulkHoursImportUpdateItem
from ..types.v1bulk_import_response import V1BulkImportResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawBulkOperationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def bulk_import_hours(
        self,
        account_id: int,
        *,
        create: typing.Optional[typing.Sequence[V1BulkHoursImportCreateItem]] = OMIT,
        update: typing.Optional[typing.Sequence[V1BulkHoursImportUpdateItem]] = OMIT,
        delete: typing.Optional[typing.Sequence[int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V1BulkImportResponse]:
        """
        Create, update, or delete multiple time entries in a single request. For large operations (100+ records), the operation runs asynchronously and returns a job ID.

        Parameters
        ----------
        account_id : int
            Workspace id

        create : typing.Optional[typing.Sequence[V1BulkHoursImportCreateItem]]
            Array of time entries to create. Each item accepts all standard event/time entry fields from PayloadSchema.

        update : typing.Optional[typing.Sequence[V1BulkHoursImportUpdateItem]]
            Array of time entries to update. Must include id field. All other fields from UpdatePayloadSchema are optional.

        delete : typing.Optional[typing.Sequence[int]]
            Array of time entry IDs to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[V1BulkImportResponse]
            Time entries imported successfully (synchronous)
        """
        _response = self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/bulk/hours",
            method="POST",
            json={
                "create": convert_and_respect_annotation_metadata(
                    object_=create, annotation=typing.Sequence[V1BulkHoursImportCreateItem], direction="write"
                ),
                "update": convert_and_respect_annotation_metadata(
                    object_=update, annotation=typing.Sequence[V1BulkHoursImportUpdateItem], direction="write"
                ),
                "delete": delete,
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
                    V1BulkImportResponse,
                    parse_obj_as(
                        type_=V1BulkImportResponse,
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

    def bulk_import_events(
        self,
        account_id: int,
        *,
        create: typing.Optional[typing.Sequence[V1BulkHoursImportCreateItem]] = OMIT,
        update: typing.Optional[typing.Sequence[V1BulkHoursImportUpdateItem]] = OMIT,
        delete: typing.Optional[typing.Sequence[int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V1BulkImportResponse]:
        """
        Create, update, or delete multiple events in a single request. Events are the same as time entries - this is an alias endpoint. For large operations (100+ records), the operation runs asynchronously and returns a job ID.

        Parameters
        ----------
        account_id : int
            Workspace id

        create : typing.Optional[typing.Sequence[V1BulkHoursImportCreateItem]]
            Array of time entries to create. Each item accepts all standard event/time entry fields from PayloadSchema.

        update : typing.Optional[typing.Sequence[V1BulkHoursImportUpdateItem]]
            Array of time entries to update. Must include id field. All other fields from UpdatePayloadSchema are optional.

        delete : typing.Optional[typing.Sequence[int]]
            Array of time entry IDs to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[V1BulkImportResponse]
            Events imported successfully (synchronous)
        """
        _response = self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/bulk/events",
            method="POST",
            json={
                "create": convert_and_respect_annotation_metadata(
                    object_=create, annotation=typing.Sequence[V1BulkHoursImportCreateItem], direction="write"
                ),
                "update": convert_and_respect_annotation_metadata(
                    object_=update, annotation=typing.Sequence[V1BulkHoursImportUpdateItem], direction="write"
                ),
                "delete": delete,
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
                    V1BulkImportResponse,
                    parse_obj_as(
                        type_=V1BulkImportResponse,
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


class AsyncRawBulkOperationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def bulk_import_hours(
        self,
        account_id: int,
        *,
        create: typing.Optional[typing.Sequence[V1BulkHoursImportCreateItem]] = OMIT,
        update: typing.Optional[typing.Sequence[V1BulkHoursImportUpdateItem]] = OMIT,
        delete: typing.Optional[typing.Sequence[int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V1BulkImportResponse]:
        """
        Create, update, or delete multiple time entries in a single request. For large operations (100+ records), the operation runs asynchronously and returns a job ID.

        Parameters
        ----------
        account_id : int
            Workspace id

        create : typing.Optional[typing.Sequence[V1BulkHoursImportCreateItem]]
            Array of time entries to create. Each item accepts all standard event/time entry fields from PayloadSchema.

        update : typing.Optional[typing.Sequence[V1BulkHoursImportUpdateItem]]
            Array of time entries to update. Must include id field. All other fields from UpdatePayloadSchema are optional.

        delete : typing.Optional[typing.Sequence[int]]
            Array of time entry IDs to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[V1BulkImportResponse]
            Time entries imported successfully (synchronous)
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/bulk/hours",
            method="POST",
            json={
                "create": convert_and_respect_annotation_metadata(
                    object_=create, annotation=typing.Sequence[V1BulkHoursImportCreateItem], direction="write"
                ),
                "update": convert_and_respect_annotation_metadata(
                    object_=update, annotation=typing.Sequence[V1BulkHoursImportUpdateItem], direction="write"
                ),
                "delete": delete,
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
                    V1BulkImportResponse,
                    parse_obj_as(
                        type_=V1BulkImportResponse,
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

    async def bulk_import_events(
        self,
        account_id: int,
        *,
        create: typing.Optional[typing.Sequence[V1BulkHoursImportCreateItem]] = OMIT,
        update: typing.Optional[typing.Sequence[V1BulkHoursImportUpdateItem]] = OMIT,
        delete: typing.Optional[typing.Sequence[int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V1BulkImportResponse]:
        """
        Create, update, or delete multiple events in a single request. Events are the same as time entries - this is an alias endpoint. For large operations (100+ records), the operation runs asynchronously and returns a job ID.

        Parameters
        ----------
        account_id : int
            Workspace id

        create : typing.Optional[typing.Sequence[V1BulkHoursImportCreateItem]]
            Array of time entries to create. Each item accepts all standard event/time entry fields from PayloadSchema.

        update : typing.Optional[typing.Sequence[V1BulkHoursImportUpdateItem]]
            Array of time entries to update. Must include id field. All other fields from UpdatePayloadSchema are optional.

        delete : typing.Optional[typing.Sequence[int]]
            Array of time entry IDs to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[V1BulkImportResponse]
            Events imported successfully (synchronous)
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/bulk/events",
            method="POST",
            json={
                "create": convert_and_respect_annotation_metadata(
                    object_=create, annotation=typing.Sequence[V1BulkHoursImportCreateItem], direction="write"
                ),
                "update": convert_and_respect_annotation_metadata(
                    object_=update, annotation=typing.Sequence[V1BulkHoursImportUpdateItem], direction="write"
                ),
                "delete": delete,
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
                    V1BulkImportResponse,
                    parse_obj_as(
                        type_=V1BulkImportResponse,
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

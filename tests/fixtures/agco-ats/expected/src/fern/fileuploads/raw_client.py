

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.api_paged_response_communication_models_file_upload import ApiPagedResponseCommunicationModelsFileUpload
from ..types.communication_models_field_filter import CommunicationModelsFieldFilter
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFileuploadsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def postreport(
        self,
        *,
        field_filters: typing.Optional[typing.Sequence[CommunicationModelsFieldFilter]] = OMIT,
        include_index_fields: typing.Optional[typing.Sequence[str]] = OMIT,
        include_stored_data_fields: typing.Optional[typing.Sequence[str]] = OMIT,
        limit: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiPagedResponseCommunicationModelsFileUpload]:
        """
        No Documentation Found.

        Parameters
        ----------
        field_filters : typing.Optional[typing.Sequence[CommunicationModelsFieldFilter]]
            Optional. Filter results by field values. Multiple filters are combined with 'AND' logic.

        include_index_fields : typing.Optional[typing.Sequence[str]]
            Optional. The index data fields to include in the results.
                        By default any index data fields included in FieldFilters will be included.

        include_stored_data_fields : typing.Optional[typing.Sequence[str]]
            Optional. The stored data fields to include in the results.
                        By default stored data fields are omitted in the result.
                        Limit must be 25 or less to return stored data fields.

        limit : typing.Optional[int]
            Optional. Limit number of results returned. The default value is 10.

        offset : typing.Optional[int]
            Optional. Offset for the results returned. The default value is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiPagedResponseCommunicationModelsFileUpload]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/FileUploads/Report",
            method="POST",
            json={
                "FieldFilters": convert_and_respect_annotation_metadata(
                    object_=field_filters, annotation=typing.Sequence[CommunicationModelsFieldFilter], direction="write"
                ),
                "IncludeIndexFields": include_index_fields,
                "IncludeStoredDataFields": include_stored_data_fields,
                "Limit": limit,
                "Offset": offset,
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
                    ApiPagedResponseCommunicationModelsFileUpload,
                    parse_obj_as(
                        type_=ApiPagedResponseCommunicationModelsFileUpload,
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


class AsyncRawFileuploadsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def postreport(
        self,
        *,
        field_filters: typing.Optional[typing.Sequence[CommunicationModelsFieldFilter]] = OMIT,
        include_index_fields: typing.Optional[typing.Sequence[str]] = OMIT,
        include_stored_data_fields: typing.Optional[typing.Sequence[str]] = OMIT,
        limit: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiPagedResponseCommunicationModelsFileUpload]:
        """
        No Documentation Found.

        Parameters
        ----------
        field_filters : typing.Optional[typing.Sequence[CommunicationModelsFieldFilter]]
            Optional. Filter results by field values. Multiple filters are combined with 'AND' logic.

        include_index_fields : typing.Optional[typing.Sequence[str]]
            Optional. The index data fields to include in the results.
                        By default any index data fields included in FieldFilters will be included.

        include_stored_data_fields : typing.Optional[typing.Sequence[str]]
            Optional. The stored data fields to include in the results.
                        By default stored data fields are omitted in the result.
                        Limit must be 25 or less to return stored data fields.

        limit : typing.Optional[int]
            Optional. Limit number of results returned. The default value is 10.

        offset : typing.Optional[int]
            Optional. Offset for the results returned. The default value is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiPagedResponseCommunicationModelsFileUpload]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/FileUploads/Report",
            method="POST",
            json={
                "FieldFilters": convert_and_respect_annotation_metadata(
                    object_=field_filters, annotation=typing.Sequence[CommunicationModelsFieldFilter], direction="write"
                ),
                "IncludeIndexFields": include_index_fields,
                "IncludeStoredDataFields": include_stored_data_fields,
                "Limit": limit,
                "Offset": offset,
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
                    ApiPagedResponseCommunicationModelsFileUpload,
                    parse_obj_as(
                        type_=ApiPagedResponseCommunicationModelsFileUpload,
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

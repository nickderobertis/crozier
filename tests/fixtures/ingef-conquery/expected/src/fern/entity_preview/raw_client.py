

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
from ..errors.unauthorized_error import UnauthorizedError
from ..types.connector_id import ConnectorId
from ..types.dataset_id import DatasetId
from ..types.date_range import DateRange
from ..types.entity_history_execution_status import EntityHistoryExecutionStatus
from ..types.error import Error
from ..types.filter_value import FilterValue
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawEntityPreviewClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def resolve_entities(
        self,
        dataset: DatasetId,
        *,
        request: typing.Sequence[FilterValue],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, str]]:
        """
        Parameters
        ----------
        dataset : DatasetId

        request : typing.Sequence[FilterValue]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, str]]
            List of tuple of ids.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"datasets/{encode_path_param(dataset)}/queries/resolve-entities",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[FilterValue], direction="write"
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
                    typing.Dict[str, str],
                    parse_obj_as(
                        type_=typing.Dict[str, str],
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

    def get_entity_preview(
        self,
        dataset: DatasetId,
        *,
        id_kind: typing.Optional[str] = OMIT,
        entity_id: typing.Optional[str] = OMIT,
        time: typing.Optional[DateRange] = OMIT,
        sources: typing.Optional[typing.Sequence[ConnectorId]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EntityHistoryExecutionStatus]:
        """
        Parameters
        ----------
        dataset : DatasetId

        id_kind : typing.Optional[str]
            The kind of the entity Id. Options are made available through `ColumnConfig#name`

        entity_id : typing.Optional[str]
            The Id of the entity.

        time : typing.Optional[DateRange]

        sources : typing.Optional[typing.Sequence[ConnectorId]]
            List of connectorIds to export their backing tables.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EntityHistoryExecutionStatus]
            Description of the history of the entity.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"datasets/{encode_path_param(dataset)}/queries/entity",
            method="POST",
            json={
                "idKind": id_kind,
                "entityId": entity_id,
                "time": convert_and_respect_annotation_metadata(object_=time, annotation=DateRange, direction="write"),
                "sources": sources,
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
                    EntityHistoryExecutionStatus,
                    parse_obj_as(
                        type_=EntityHistoryExecutionStatus,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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


class AsyncRawEntityPreviewClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def resolve_entities(
        self,
        dataset: DatasetId,
        *,
        request: typing.Sequence[FilterValue],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, str]]:
        """
        Parameters
        ----------
        dataset : DatasetId

        request : typing.Sequence[FilterValue]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, str]]
            List of tuple of ids.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"datasets/{encode_path_param(dataset)}/queries/resolve-entities",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[FilterValue], direction="write"
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
                    typing.Dict[str, str],
                    parse_obj_as(
                        type_=typing.Dict[str, str],
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

    async def get_entity_preview(
        self,
        dataset: DatasetId,
        *,
        id_kind: typing.Optional[str] = OMIT,
        entity_id: typing.Optional[str] = OMIT,
        time: typing.Optional[DateRange] = OMIT,
        sources: typing.Optional[typing.Sequence[ConnectorId]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EntityHistoryExecutionStatus]:
        """
        Parameters
        ----------
        dataset : DatasetId

        id_kind : typing.Optional[str]
            The kind of the entity Id. Options are made available through `ColumnConfig#name`

        entity_id : typing.Optional[str]
            The Id of the entity.

        time : typing.Optional[DateRange]

        sources : typing.Optional[typing.Sequence[ConnectorId]]
            List of connectorIds to export their backing tables.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EntityHistoryExecutionStatus]
            Description of the history of the entity.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"datasets/{encode_path_param(dataset)}/queries/entity",
            method="POST",
            json={
                "idKind": id_kind,
                "entityId": entity_id,
                "time": convert_and_respect_annotation_metadata(object_=time, annotation=DateRange, direction="write"),
                "sources": sources,
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
                    EntityHistoryExecutionStatus,
                    parse_obj_as(
                        type_=EntityHistoryExecutionStatus,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

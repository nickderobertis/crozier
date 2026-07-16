

import contextlib
import typing
from json.decoder import JSONDecodeError

from .. import core
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.internal_server_error import InternalServerError
from ..types.counter import Counter
from ..types.labels_map import LabelsMap
from ..types.parameter_constraint import ParameterConstraint
from ..types.service import Service
from .types.get_service_response import GetServiceResponse


OMIT = typing.cast(typing.Any, ...)


class RawMockClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    @contextlib.contextmanager
    def export_snapshot(
        self,
        *,
        service_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
        """
        Export a repostiory snapshot with requested services

        Parameters
        ----------
        service_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            List of service identifiers to export

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[HttpResponse[typing.Iterator[bytes]]]
            Snapshot file representing the export of requested services
        """
        with self._client_wrapper.httpx_client.stream(
            "export",
            method="GET",
            params={
                "serviceIds": service_ids,
            },
            request_options=request_options,
        ) as _response:

            def _stream() -> HttpResponse[typing.Iterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return HttpResponse(
                            response=_response, data=(_chunk for _chunk in _response.iter_bytes(chunk_size=_chunk_size))
                        )
                    _response.read()
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield _stream()

    def import_snapshot(
        self, *, file: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Import a repository snapshot previsouly exported into Microcks

        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "import",
            method="POST",
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
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_services(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Service]:
        """
        Parameters
        ----------
        page : typing.Optional[int]
            Page of Services to retrieve (starts at and defaults to 0)

        size : typing.Optional[int]
            Size of a page. Maximum number of Services to include in a response (defaults to 20)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Service]
            List of found Services
        """
        _response = self._client_wrapper.httpx_client.request(
            "services",
            method="GET",
            params={
                "page": page,
                "size": size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Service,
                    parse_obj_as(
                        type_=Service,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_services_counter(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[Counter]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Counter]
            Number of Services in datastore
        """
        _response = self._client_wrapper.httpx_client.request(
            "services/count",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Counter,
                    parse_obj_as(
                        type_=Counter,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_services_labels(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[LabelsMap]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[LabelsMap]
            Already used labels: keys are label Keys, values are array of label Values
        """
        _response = self._client_wrapper.httpx_client.request(
            "services/labels",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LabelsMap,
                    parse_obj_as(
                        type_=LabelsMap,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def search_services(
        self, *, query_map: typing.Dict[str, str], request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[Service]]:
        """
        Parameters
        ----------
        query_map : typing.Dict[str, str]
            Map of criterion. Key can be simply 'name' with value as the searched string. You can also search by label using keys like 'labels.x' where 'x' is the label and value the label value

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Service]]
            List of found Services (filtered according search criteria)
        """
        _response = self._client_wrapper.httpx_client.request(
            "services/search",
            method="GET",
            params={
                "queryMap": query_map,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Service],
                    parse_obj_as(
                        type_=typing.List[Service],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_service(
        self,
        id: str,
        *,
        messages: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetServiceResponse]:
        """
        Parameters
        ----------
        id : str
            Unique identifier of Service to managed

        messages : typing.Optional[bool]
            Whether to include details on services messages into result. Default is false

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetServiceResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"services/{jsonable_encoder(id)}",
            method="GET",
            params={
                "messages": messages,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetServiceResponse,
                    parse_obj_as(
                        type_=GetServiceResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_service(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """
        Delete a Service

        Parameters
        ----------
        id : str
            Unique identifier of Service to managed

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"services/{jsonable_encoder(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_service_metadata(
        self,
        id: str,
        *,
        created_on: int,
        last_update: int,
        annotations: typing.Optional[typing.Dict[str, str]] = OMIT,
        labels: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        id : str
            Unique identifier of Service to managed

        created_on : int
            Creation date of attached object

        last_update : int
            Last update of attached object

        annotations : typing.Optional[typing.Dict[str, str]]
            Annotations of attached object

        labels : typing.Optional[typing.Dict[str, str]]
            Labels put on attached object

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"services/{jsonable_encoder(id)}/metadata",
            method="PUT",
            json={
                "annotations": annotations,
                "createdOn": created_on,
                "labels": labels,
                "lastUpdate": last_update,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def override_service_operation(
        self,
        id: str,
        *,
        operation_name: str,
        default_delay: typing.Optional[int] = OMIT,
        dispatcher: typing.Optional[str] = OMIT,
        dispatcher_rules: typing.Optional[str] = OMIT,
        parameter_constraints: typing.Optional[typing.Sequence[ParameterConstraint]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        id : str
            Unique identifier of Service to managed

        operation_name : str
            Name of operation to update

        default_delay : typing.Optional[int]
            Default delay in milliseconds to apply to mock responses on this operation

        dispatcher : typing.Optional[str]
            Type of dispatcher to apply for this operation

        dispatcher_rules : typing.Optional[str]
            Rules of dispatcher for this operation

        parameter_constraints : typing.Optional[typing.Sequence[ParameterConstraint]]
            Constraints that may apply to incoming parameters on this operation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"services/{jsonable_encoder(id)}/operation",
            method="PUT",
            params={
                "operationName": operation_name,
            },
            json={
                "defaultDelay": default_delay,
                "dispatcher": dispatcher,
                "dispatcherRules": dispatcher_rules,
                "parameterConstraints": convert_and_respect_annotation_metadata(
                    object_=parameter_constraints, annotation=typing.Sequence[ParameterConstraint], direction="write"
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
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawMockClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    @contextlib.asynccontextmanager
    async def export_snapshot(
        self,
        *,
        service_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
        """
        Export a repostiory snapshot with requested services

        Parameters
        ----------
        service_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            List of service identifiers to export

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]
            Snapshot file representing the export of requested services
        """
        async with self._client_wrapper.httpx_client.stream(
            "export",
            method="GET",
            params={
                "serviceIds": service_ids,
            },
            request_options=request_options,
        ) as _response:

            async def _stream() -> AsyncHttpResponse[typing.AsyncIterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return AsyncHttpResponse(
                            response=_response,
                            data=(_chunk async for _chunk in _response.aiter_bytes(chunk_size=_chunk_size)),
                        )
                    await _response.aread()
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield await _stream()

    async def import_snapshot(
        self, *, file: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Import a repository snapshot previsouly exported into Microcks

        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "import",
            method="POST",
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
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_services(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Service]:
        """
        Parameters
        ----------
        page : typing.Optional[int]
            Page of Services to retrieve (starts at and defaults to 0)

        size : typing.Optional[int]
            Size of a page. Maximum number of Services to include in a response (defaults to 20)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Service]
            List of found Services
        """
        _response = await self._client_wrapper.httpx_client.request(
            "services",
            method="GET",
            params={
                "page": page,
                "size": size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Service,
                    parse_obj_as(
                        type_=Service,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_services_counter(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Counter]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Counter]
            Number of Services in datastore
        """
        _response = await self._client_wrapper.httpx_client.request(
            "services/count",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Counter,
                    parse_obj_as(
                        type_=Counter,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_services_labels(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[LabelsMap]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[LabelsMap]
            Already used labels: keys are label Keys, values are array of label Values
        """
        _response = await self._client_wrapper.httpx_client.request(
            "services/labels",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LabelsMap,
                    parse_obj_as(
                        type_=LabelsMap,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def search_services(
        self, *, query_map: typing.Dict[str, str], request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[Service]]:
        """
        Parameters
        ----------
        query_map : typing.Dict[str, str]
            Map of criterion. Key can be simply 'name' with value as the searched string. You can also search by label using keys like 'labels.x' where 'x' is the label and value the label value

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Service]]
            List of found Services (filtered according search criteria)
        """
        _response = await self._client_wrapper.httpx_client.request(
            "services/search",
            method="GET",
            params={
                "queryMap": query_map,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Service],
                    parse_obj_as(
                        type_=typing.List[Service],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_service(
        self,
        id: str,
        *,
        messages: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetServiceResponse]:
        """
        Parameters
        ----------
        id : str
            Unique identifier of Service to managed

        messages : typing.Optional[bool]
            Whether to include details on services messages into result. Default is false

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetServiceResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"services/{jsonable_encoder(id)}",
            method="GET",
            params={
                "messages": messages,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetServiceResponse,
                    parse_obj_as(
                        type_=GetServiceResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_service(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Delete a Service

        Parameters
        ----------
        id : str
            Unique identifier of Service to managed

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"services/{jsonable_encoder(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_service_metadata(
        self,
        id: str,
        *,
        created_on: int,
        last_update: int,
        annotations: typing.Optional[typing.Dict[str, str]] = OMIT,
        labels: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        id : str
            Unique identifier of Service to managed

        created_on : int
            Creation date of attached object

        last_update : int
            Last update of attached object

        annotations : typing.Optional[typing.Dict[str, str]]
            Annotations of attached object

        labels : typing.Optional[typing.Dict[str, str]]
            Labels put on attached object

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"services/{jsonable_encoder(id)}/metadata",
            method="PUT",
            json={
                "annotations": annotations,
                "createdOn": created_on,
                "labels": labels,
                "lastUpdate": last_update,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def override_service_operation(
        self,
        id: str,
        *,
        operation_name: str,
        default_delay: typing.Optional[int] = OMIT,
        dispatcher: typing.Optional[str] = OMIT,
        dispatcher_rules: typing.Optional[str] = OMIT,
        parameter_constraints: typing.Optional[typing.Sequence[ParameterConstraint]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        id : str
            Unique identifier of Service to managed

        operation_name : str
            Name of operation to update

        default_delay : typing.Optional[int]
            Default delay in milliseconds to apply to mock responses on this operation

        dispatcher : typing.Optional[str]
            Type of dispatcher to apply for this operation

        dispatcher_rules : typing.Optional[str]
            Rules of dispatcher for this operation

        parameter_constraints : typing.Optional[typing.Sequence[ParameterConstraint]]
            Constraints that may apply to incoming parameters on this operation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"services/{jsonable_encoder(id)}/operation",
            method="PUT",
            params={
                "operationName": operation_name,
            },
            json={
                "defaultDelay": default_delay,
                "dispatcher": dispatcher,
                "dispatcherRules": dispatcher_rules,
                "parameterConstraints": convert_and_respect_annotation_metadata(
                    object_=parameter_constraints, annotation=typing.Sequence[ParameterConstraint], direction="write"
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
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

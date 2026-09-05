

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.envelope_app_status_check import EnvelopeAppStatusCheck
from ..types.envelope_dict_str_any import EnvelopeDictStrAny
from ..types.envelope_health_info_dict import EnvelopeHealthInfoDict
from ..types.envelope_status_diagnostics_get import EnvelopeStatusDiagnosticsGet
from ..types.envelope_str import EnvelopeStr
from pydantic import ValidationError


class RawMaintenanceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def healthcheck_readiness_probe(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeHealthInfoDict]:
        """
        Readiness probe: check if the container is ready to receive traffic

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeHealthInfoDict]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeHealthInfoDict,
                    parse_obj_as(
                        type_=EnvelopeHealthInfoDict,
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

    def healthcheck_liveness_probe(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeDictStrAny]:
        """
        Liveness probe: check if the container is alive

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeDictStrAny]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/health",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeDictStrAny,
                    parse_obj_as(
                        type_=EnvelopeDictStrAny,
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

    def get_config(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeDictStrAny]:
        """
        Front end runtime configuration

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeDictStrAny]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/config",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeDictStrAny,
                    parse_obj_as(
                        type_=EnvelopeDictStrAny,
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

    def get_scheduled_maintenance(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeStr]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeStr]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/scheduled_maintenance",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeStr,
                    parse_obj_as(
                        type_=EnvelopeStr,
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

    def get_app_status(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeAppStatusCheck]:
        """
        checks status of self and connected services

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeAppStatusCheck]
            Returns app status check
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/status",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeAppStatusCheck,
                    parse_obj_as(
                        type_=EnvelopeAppStatusCheck,
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

    def get_app_diagnostics(
        self, *, top_tracemalloc: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeStatusDiagnosticsGet]:
        """
        Parameters
        ----------
        top_tracemalloc : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeStatusDiagnosticsGet]
            Returns app diagnostics report
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/status/diagnostics",
            method="GET",
            params={
                "top_tracemalloc": top_tracemalloc,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeStatusDiagnosticsGet,
                    parse_obj_as(
                        type_=EnvelopeStatusDiagnosticsGet,
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

    def get_service_status(
        self, service_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeAppStatusCheck]:
        """
        Parameters
        ----------
        service_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeAppStatusCheck]
            Returns app status check
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/status/{encode_path_param(service_name)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeAppStatusCheck,
                    parse_obj_as(
                        type_=EnvelopeAppStatusCheck,
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


class AsyncRawMaintenanceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def healthcheck_readiness_probe(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeHealthInfoDict]:
        """
        Readiness probe: check if the container is ready to receive traffic

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeHealthInfoDict]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeHealthInfoDict,
                    parse_obj_as(
                        type_=EnvelopeHealthInfoDict,
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

    async def healthcheck_liveness_probe(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeDictStrAny]:
        """
        Liveness probe: check if the container is alive

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeDictStrAny]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/health",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeDictStrAny,
                    parse_obj_as(
                        type_=EnvelopeDictStrAny,
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

    async def get_config(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeDictStrAny]:
        """
        Front end runtime configuration

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeDictStrAny]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/config",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeDictStrAny,
                    parse_obj_as(
                        type_=EnvelopeDictStrAny,
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

    async def get_scheduled_maintenance(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeStr]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeStr]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/scheduled_maintenance",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeStr,
                    parse_obj_as(
                        type_=EnvelopeStr,
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

    async def get_app_status(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeAppStatusCheck]:
        """
        checks status of self and connected services

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeAppStatusCheck]
            Returns app status check
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/status",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeAppStatusCheck,
                    parse_obj_as(
                        type_=EnvelopeAppStatusCheck,
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

    async def get_app_diagnostics(
        self, *, top_tracemalloc: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeStatusDiagnosticsGet]:
        """
        Parameters
        ----------
        top_tracemalloc : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeStatusDiagnosticsGet]
            Returns app diagnostics report
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/status/diagnostics",
            method="GET",
            params={
                "top_tracemalloc": top_tracemalloc,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeStatusDiagnosticsGet,
                    parse_obj_as(
                        type_=EnvelopeStatusDiagnosticsGet,
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

    async def get_service_status(
        self, service_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeAppStatusCheck]:
        """
        Parameters
        ----------
        service_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeAppStatusCheck]
            Returns app status check
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/status/{encode_path_param(service_name)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeAppStatusCheck,
                    parse_obj_as(
                        type_=EnvelopeAppStatusCheck,
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

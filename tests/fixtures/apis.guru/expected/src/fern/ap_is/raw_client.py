

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.ap_is import ApIs
from ..types.api import Api
from ..types.metrics import Metrics
from .types.get_providers_response import GetProvidersResponse
from .types.get_services_response import GetServicesResponse


class RawApIsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_ap_is(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[ApIs]:
        """
        List all APIs in the directory.
        Returns links to the OpenAPI definitions for each API in the directory.
        If API exist in multiple versions `preferred` one is explicitly marked.
        Some basic info from the OpenAPI definition is cached inside each object.
        This allows you to generate some simple views without needing to fetch the OpenAPI definition for each API.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApIs]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "list.json",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApIs,
                    parse_obj_as(
                        type_=ApIs,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_metrics(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[Metrics]:
        """
        Some basic metrics for the entire directory.
        Just stunning numbers to put on a front page and are intended purely for WoW effect :)

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Metrics]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "metrics.json",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Metrics,
                    parse_obj_as(
                        type_=Metrics,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_providers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetProvidersResponse]:
        """
        List all the providers in the directory

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetProvidersResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "providers.json",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetProvidersResponse,
                    parse_obj_as(
                        type_=GetProvidersResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_api(
        self, provider: str, api: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Api]:
        """
        Returns the API entry for one specific version of an API where there is no serviceName.

        Parameters
        ----------
        provider : str

        api : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Api]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"specs/{jsonable_encoder(provider)}/{jsonable_encoder(api)}.json",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Api,
                    parse_obj_as(
                        type_=Api,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_service_api(
        self, provider: str, service: str, api: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Api]:
        """
        Returns the API entry for one specific version of an API where there is a serviceName.

        Parameters
        ----------
        provider : str

        service : str

        api : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Api]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"specs/{jsonable_encoder(provider)}/{jsonable_encoder(service)}/{jsonable_encoder(api)}.json",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Api,
                    parse_obj_as(
                        type_=Api,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_provider(
        self, provider: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ApIs]:
        """
        List all APIs in the directory for a particular providerName
        Returns links to the individual API entry for each API.

        Parameters
        ----------
        provider : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApIs]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"{jsonable_encoder(provider)}.json",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApIs,
                    parse_obj_as(
                        type_=ApIs,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_services(
        self, provider: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetServicesResponse]:
        """
        List all serviceNames in the directory for a particular providerName

        Parameters
        ----------
        provider : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetServicesResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"{jsonable_encoder(provider)}/services.json",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetServicesResponse,
                    parse_obj_as(
                        type_=GetServicesResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawApIsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_ap_is(self, *, request_options: typing.Optional[RequestOptions] = None) -> AsyncHttpResponse[ApIs]:
        """
        List all APIs in the directory.
        Returns links to the OpenAPI definitions for each API in the directory.
        If API exist in multiple versions `preferred` one is explicitly marked.
        Some basic info from the OpenAPI definition is cached inside each object.
        This allows you to generate some simple views without needing to fetch the OpenAPI definition for each API.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApIs]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "list.json",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApIs,
                    parse_obj_as(
                        type_=ApIs,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_metrics(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Metrics]:
        """
        Some basic metrics for the entire directory.
        Just stunning numbers to put on a front page and are intended purely for WoW effect :)

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Metrics]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "metrics.json",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Metrics,
                    parse_obj_as(
                        type_=Metrics,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_providers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetProvidersResponse]:
        """
        List all the providers in the directory

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetProvidersResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "providers.json",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetProvidersResponse,
                    parse_obj_as(
                        type_=GetProvidersResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_api(
        self, provider: str, api: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Api]:
        """
        Returns the API entry for one specific version of an API where there is no serviceName.

        Parameters
        ----------
        provider : str

        api : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Api]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"specs/{jsonable_encoder(provider)}/{jsonable_encoder(api)}.json",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Api,
                    parse_obj_as(
                        type_=Api,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_service_api(
        self, provider: str, service: str, api: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Api]:
        """
        Returns the API entry for one specific version of an API where there is a serviceName.

        Parameters
        ----------
        provider : str

        service : str

        api : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Api]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"specs/{jsonable_encoder(provider)}/{jsonable_encoder(service)}/{jsonable_encoder(api)}.json",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Api,
                    parse_obj_as(
                        type_=Api,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_provider(
        self, provider: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ApIs]:
        """
        List all APIs in the directory for a particular providerName
        Returns links to the individual API entry for each API.

        Parameters
        ----------
        provider : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApIs]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"{jsonable_encoder(provider)}.json",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApIs,
                    parse_obj_as(
                        type_=ApIs,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_services(
        self, provider: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetServicesResponse]:
        """
        List all serviceNames in the directory for a particular providerName

        Parameters
        ----------
        provider : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetServicesResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"{jsonable_encoder(provider)}/services.json",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetServicesResponse,
                    parse_obj_as(
                        type_=GetServicesResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

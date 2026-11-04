

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.core_navigation_get_apps_navigation200response import CoreNavigationGetAppsNavigation200Response
from pydantic import ValidationError


class RawCoreNavigationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_apps_navigation(
        self, *, absolute: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CoreNavigationGetAppsNavigation200Response]:
        """
        Parameters
        ----------
        absolute : typing.Optional[int]
            Rewrite URLs to absolute ones

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CoreNavigationGetAppsNavigation200Response]
            Apps navigation returned
        """
        _response = self._client_wrapper.httpx_client.request(
            "ocs/v2.php/core/navigation/apps",
            method="GET",
            params={
                "absolute": absolute,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CoreNavigationGetAppsNavigation200Response,
                    parse_obj_as(
                        type_=CoreNavigationGetAppsNavigation200Response,
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

    def get_settings_navigation(
        self, *, absolute: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CoreNavigationGetAppsNavigation200Response]:
        """
        Parameters
        ----------
        absolute : typing.Optional[int]
            Rewrite URLs to absolute ones

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CoreNavigationGetAppsNavigation200Response]
            Apps navigation returned
        """
        _response = self._client_wrapper.httpx_client.request(
            "ocs/v2.php/core/navigation/settings",
            method="GET",
            params={
                "absolute": absolute,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CoreNavigationGetAppsNavigation200Response,
                    parse_obj_as(
                        type_=CoreNavigationGetAppsNavigation200Response,
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


class AsyncRawCoreNavigationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_apps_navigation(
        self, *, absolute: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CoreNavigationGetAppsNavigation200Response]:
        """
        Parameters
        ----------
        absolute : typing.Optional[int]
            Rewrite URLs to absolute ones

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CoreNavigationGetAppsNavigation200Response]
            Apps navigation returned
        """
        _response = await self._client_wrapper.httpx_client.request(
            "ocs/v2.php/core/navigation/apps",
            method="GET",
            params={
                "absolute": absolute,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CoreNavigationGetAppsNavigation200Response,
                    parse_obj_as(
                        type_=CoreNavigationGetAppsNavigation200Response,
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

    async def get_settings_navigation(
        self, *, absolute: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CoreNavigationGetAppsNavigation200Response]:
        """
        Parameters
        ----------
        absolute : typing.Optional[int]
            Rewrite URLs to absolute ones

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CoreNavigationGetAppsNavigation200Response]
            Apps navigation returned
        """
        _response = await self._client_wrapper.httpx_client.request(
            "ocs/v2.php/core/navigation/settings",
            method="GET",
            params={
                "absolute": absolute,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CoreNavigationGetAppsNavigation200Response,
                    parse_obj_as(
                        type_=CoreNavigationGetAppsNavigation200Response,
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

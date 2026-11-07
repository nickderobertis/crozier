

import typing
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.http_response import AsyncHttpResponse, HttpResponse
from ...core.parse_error import ParsingError
from ...core.pydantic_utilities import parse_obj_as
from ...core.request_options import RequestOptions
from ...errors.unauthorized_error import UnauthorizedError
from ...types.get_web_search_provider_catalog_response import GetWebSearchProviderCatalogResponse
from ...types.request_error_response import RequestErrorResponse
from pydantic import ValidationError


class RawWebSearchProvidersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetWebSearchProviderCatalogResponse]:
        """
        Shipped web-search provider presets.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetWebSearchProviderCatalogResponse]
            Shipped web-search provider presets.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/catalogs/web-search-providers",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetWebSearchProviderCatalogResponse,
                    parse_obj_as(
                        type_=GetWebSearchProviderCatalogResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        RequestErrorResponse,
                        parse_obj_as(
                            type_=RequestErrorResponse,
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


class AsyncRawWebSearchProvidersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetWebSearchProviderCatalogResponse]:
        """
        Shipped web-search provider presets.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetWebSearchProviderCatalogResponse]
            Shipped web-search provider presets.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/catalogs/web-search-providers",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetWebSearchProviderCatalogResponse,
                    parse_obj_as(
                        type_=GetWebSearchProviderCatalogResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        RequestErrorResponse,
                        parse_obj_as(
                            type_=RequestErrorResponse,
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

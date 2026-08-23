

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError as core_api_error_ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.internal_server_error import InternalServerError
from ..types.api_error import ApiError as types_api_error_ApiError
from ..types.capabilities import Capabilities
from pydantic import ValidationError


class RawCapabilitiesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_capabilities(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Capabilities]:
        """
        The landing page provides links to the:
          * The OpenAPI-definition (no fixed path),
          * The Conformance statements (path /conformance),
          * The processes metadata (path /processes),
          * The endpoint for job monitoring (path /jobs).

        For more information, see [OGC API — Processes — Part 1 Section 7.2](https://docs.ogc.org/is/18-062r2/18-062r2.html#sc_landing_page).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Capabilities]
            The landing page provides links to the API definition
            (link relations `service-desc` and `service-doc`),
            the Conformance declaration (path `/conformance`,
            link relation `http://www.opengis.net/def/rel/ogc/1.0/conformance`),
            and to other resources.
        """
        _response = self._client_wrapper.httpx_client.request(
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Capabilities,
                    parse_obj_as(
                        type_=Capabilities,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
            )
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise core_api_error_ApiError(
            status_code=_response.status_code, headers=dict(_response.headers), body=_response_json
        )


class AsyncRawCapabilitiesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_capabilities(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Capabilities]:
        """
        The landing page provides links to the:
          * The OpenAPI-definition (no fixed path),
          * The Conformance statements (path /conformance),
          * The processes metadata (path /processes),
          * The endpoint for job monitoring (path /jobs).

        For more information, see [OGC API — Processes — Part 1 Section 7.2](https://docs.ogc.org/is/18-062r2/18-062r2.html#sc_landing_page).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Capabilities]
            The landing page provides links to the API definition
            (link relations `service-desc` and `service-doc`),
            the Conformance declaration (path `/conformance`,
            link relation `http://www.opengis.net/def/rel/ogc/1.0/conformance`),
            and to other resources.
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Capabilities,
                    parse_obj_as(
                        type_=Capabilities,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
            )
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise core_api_error_ApiError(
            status_code=_response.status_code, headers=dict(_response.headers), body=_response_json
        )



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
from ..types.conformance_declaration import ConformanceDeclaration
from pydantic import ValidationError


class RawConformanceDeclarationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_conformance(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ConformanceDeclaration]:
        """
        A list of all conformance classes, specified in a standard, that the server conforms to.

        | Conformance class | URI |
        |-----------|-------|
        |Core|http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/core|
        |OGC Process Description|http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/ogc-process-description|
        |JSON|http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/json|
        |HTML|http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/html|
        |OpenAPI Specification 3.0|http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/oas30|
        |Job list|http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/job-list|
        |Callback|http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/callback|
        |Dismiss|http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/dismiss|

        For more information, see [OGC API — Processes — Part 1 Section 7.4](https://docs.ogc.org/is/18-062r2/18-062r2.html#sc_conformance_classes).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ConformanceDeclaration]
            The URIs of all conformance classes supported
            by the server. To support "generic" clients that want
            to access multiple OGC API - Processes implementations - and
            not "just" a specific API / server, the server declares
            the conformance classes it implements and conforms to.
        """
        _response = self._client_wrapper.httpx_client.request(
            "conformance",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConformanceDeclaration,
                    parse_obj_as(
                        type_=ConformanceDeclaration,
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


class AsyncRawConformanceDeclarationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_conformance(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ConformanceDeclaration]:
        """
        A list of all conformance classes, specified in a standard, that the server conforms to.

        | Conformance class | URI |
        |-----------|-------|
        |Core|http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/core|
        |OGC Process Description|http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/ogc-process-description|
        |JSON|http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/json|
        |HTML|http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/html|
        |OpenAPI Specification 3.0|http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/oas30|
        |Job list|http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/job-list|
        |Callback|http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/callback|
        |Dismiss|http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/dismiss|

        For more information, see [OGC API — Processes — Part 1 Section 7.4](https://docs.ogc.org/is/18-062r2/18-062r2.html#sc_conformance_classes).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ConformanceDeclaration]
            The URIs of all conformance classes supported
            by the server. To support "generic" clients that want
            to access multiple OGC API - Processes implementations - and
            not "just" a specific API / server, the server declares
            the conformance classes it implements and conforms to.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "conformance",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConformanceDeclaration,
                    parse_obj_as(
                        type_=ConformanceDeclaration,
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

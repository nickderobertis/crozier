

import typing
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.http_response import AsyncHttpResponse, HttpResponse
from ...core.parse_error import ParsingError
from ...core.pydantic_utilities import parse_obj_as
from ...core.request_options import RequestOptions
from ...errors.bad_request_error import BadRequestError
from ...errors.content_too_large_error import ContentTooLargeError
from ...errors.service_unavailable_error import ServiceUnavailableError
from ...errors.unauthorized_error import UnauthorizedError
from ...types.error_response import ErrorResponse
from ...types.service_unavailable_error_body import ServiceUnavailableErrorBody
from ...types.store_probe_request import StoreProbeRequest
from ...types.store_probe_response import StoreProbeResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawStoreClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def probe(
        self, *, request: StoreProbeRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[StoreProbeResponse]:
        """
        Checks that the configured object store supports the create-if-absent, compare-and-swap, visibility, listing, and ranged-read behavior that LoonFS depends on, and reports the result of each check. The probe runs only when a client calls this route, because it writes and deletes objects. It writes them all under a scratch prefix that isn't a durable object family, and its last check deletes them and confirms that the prefix is empty. If the store fails a check, the response is still 200, and it reports that check as `failed`. If the store declares that it doesn't support an optional capability, the response reports that check as `unsupported`, which isn't a failure. The probe doesn't control whether the deployment can serve presigned direct uploads. The endpoint allowlist controls that, because the probe tests only the server's own requests and never a presigned capability issued to a client.

        Parameters
        ----------
        request : StoreProbeRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[StoreProbeResponse]
            The probe completed, and the body reports each check's outcome
        """
        _request_options_with_retries_disabled: typing.Optional[RequestOptions] = (
            {**request_options, "max_retries": 0} if request_options is not None else {"max_retries": 0}
        )
        _response = self._client_wrapper.httpx_client.request(
            "v0/maintenance/store/probe",
            method="POST",
            json=request,
            request_options=_request_options_with_retries_disabled,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StoreProbeResponse,
                    parse_obj_as(
                        type_=StoreProbeResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ServiceUnavailableErrorBody,
                        parse_obj_as(
                            type_=ServiceUnavailableErrorBody,
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


class AsyncRawStoreClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def probe(
        self, *, request: StoreProbeRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[StoreProbeResponse]:
        """
        Checks that the configured object store supports the create-if-absent, compare-and-swap, visibility, listing, and ranged-read behavior that LoonFS depends on, and reports the result of each check. The probe runs only when a client calls this route, because it writes and deletes objects. It writes them all under a scratch prefix that isn't a durable object family, and its last check deletes them and confirms that the prefix is empty. If the store fails a check, the response is still 200, and it reports that check as `failed`. If the store declares that it doesn't support an optional capability, the response reports that check as `unsupported`, which isn't a failure. The probe doesn't control whether the deployment can serve presigned direct uploads. The endpoint allowlist controls that, because the probe tests only the server's own requests and never a presigned capability issued to a client.

        Parameters
        ----------
        request : StoreProbeRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[StoreProbeResponse]
            The probe completed, and the body reports each check's outcome
        """
        _request_options_with_retries_disabled: typing.Optional[RequestOptions] = (
            {**request_options, "max_retries": 0} if request_options is not None else {"max_retries": 0}
        )
        _response = await self._client_wrapper.httpx_client.request(
            "v0/maintenance/store/probe",
            method="POST",
            json=request,
            request_options=_request_options_with_retries_disabled,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StoreProbeResponse,
                    parse_obj_as(
                        type_=StoreProbeResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ServiceUnavailableErrorBody,
                        parse_obj_as(
                            type_=ServiceUnavailableErrorBody,
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

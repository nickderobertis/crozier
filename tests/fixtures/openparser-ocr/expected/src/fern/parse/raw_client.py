

import json
import typing
from json.decoder import JSONDecodeError

from .. import core
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.conflict_error import ConflictError
from ..errors.content_too_large_error import ContentTooLargeError
from ..errors.forbidden_error import ForbiddenError
from ..errors.gateway_timeout_error import GatewayTimeoutError
from ..errors.payment_required_error import PaymentRequiredError
from ..errors.service_unavailable_error import ServiceUnavailableError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..errors.unsupported_media_type_error import UnsupportedMediaTypeError
from ..types.batch_job_accepted import BatchJobAccepted
from ..types.error_response import ErrorResponse
from ..types.job_accepted import JobAccepted
from ..types.parse_batch_request import ParseBatchRequest
from ..types.parse_request import ParseRequest
from ..types.parse_result import ParseResult
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawParseClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def sync(
        self,
        *,
        idempotency_key: str,
        request: ParseRequest,
        file: typing.Optional[core.File] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ParseResult]:
        """
        Admit a parse job, wait up to the sync wait limit, and return the selected terminal parse
        representation when ready. `output_format` defaults to the versioned provider-neutral
        `openparser@1`; `raw` returns a stable provider envelope around the selected provider's
        untouched successful result. Terminal `failed` within the wait window returns `422`
        `ErrorResponse`; terminal `indeterminate` returns `504` `ErrorResponse`. Returns `202`
        with a durable job reference and `Location` if the wait limit expires first.
        
        Example (`multipart/form-data`):
        
        ```bash
        curl -X POST 'https://api.openparser.dev/parse' \\
          -H 'Authorization: Bearer YOUR_API_KEY' \\
          -H "Idempotency-Key: $(uuidgen 2>/dev/null || openssl rand -hex 16)" \\
          -F 'request={"ocr_model":"paddleocr-vl-1.6","output_format":"openparser@1"};type=application/json' \\
          -F 'file=@./document.pdf'
        ```
        
        Parameters
        ----------
        idempotency_key : str
            Client-supplied idempotency key. Required on every parse or extract `POST`. Must be unique per distinct
            request body for a given tenant and operation.
        
        request : ParseRequest
        
        file : typing.Optional[core.File]
            See core.File for more documentation
        
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.
        
        Returns
        -------
        HttpResponse[ParseResult]
            Terminal parse result in the selected `openparser@1` or `raw` representation
        """
        _response = self._client_wrapper.httpx_client.request(
            "parse",
            method="POST",
            data={},
            files={
                **({"file": file} if file is not None else {}),
                "request": (None, json.dumps(jsonable_encoder(request)), "application/json"),
            },
            headers={
                "Idempotency-Key": str(idempotency_key) if idempotency_key is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ParseResult,
                    parse_obj_as(
                        type_=ParseResult,
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
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
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
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
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
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 504:
                raise GatewayTimeoutError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def async_(
        self,
        *,
        idempotency_key: str,
        request: ParseRequest,
        file: typing.Optional[core.File] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[JobAccepted]:
        """
        Admit a durable parse job and return immediately.
        
        Example (`multipart/form-data`):
        
        ```bash
        curl -X POST 'https://api.openparser.dev/parse/async' \\
          -H 'Authorization: Bearer YOUR_API_KEY' \\
          -H "Idempotency-Key: $(uuidgen 2>/dev/null || openssl rand -hex 16)" \\
          -F 'request={"ocr_model":"paddleocr-vl-1.6","output_format":"openparser@1"};type=application/json' \\
          -F 'file=@./document.pdf'
        ```
        
        Parameters
        ----------
        idempotency_key : str
            Client-supplied idempotency key. Required on every parse or extract `POST`. Must be unique per distinct
            request body for a given tenant and operation.
        
        request : ParseRequest
        
        file : typing.Optional[core.File]
            See core.File for more documentation
        
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.
        
        Returns
        -------
        HttpResponse[JobAccepted]
            Durable non-terminal job admitted. Returned by async endpoints and by sync endpoints when
            the wait limit expires before a terminal status.
        """
        _response = self._client_wrapper.httpx_client.request(
            "parse/async",
            method="POST",
            data={},
            files={
                **({"file": file} if file is not None else {}),
                "request": (None, json.dumps(jsonable_encoder(request)), "application/json"),
            },
            headers={
                "Idempotency-Key": str(idempotency_key) if idempotency_key is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JobAccepted,
                    parse_obj_as(
                        type_=JobAccepted,
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
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
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
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
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
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def batch(
        self,
        *,
        idempotency_key: str,
        request: ParseBatchRequest,
        files: typing.Optional[typing.List[core.File]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BatchJobAccepted]:
        """
        Admit up to 100 parse child jobs in one durable batch. Every uploaded file must be mapped
        exactly once by `file_index`. Partial child failures are preserved in batch results.
        Parent status derivation for mixed outcomes is defined on `JobStatus`.

        Parameters
        ----------
        idempotency_key : str
            Client-supplied idempotency key. Required on every parse or extract `POST`. Must be unique per distinct
            request body for a given tenant and operation.

        request : ParseBatchRequest

        files : typing.Optional[typing.List[core.File]]
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BatchJobAccepted]
            Durable batch job admitted. `Location` points at the parent batch job resource.
        """
        _response = self._client_wrapper.httpx_client.request(
            "parse/batch",
            method="POST",
            data={},
            files={
                **({"files": files} if files is not None else {}),
                "request": (None, json.dumps(jsonable_encoder(request)), "application/json"),
            },
            headers={
                "Idempotency-Key": str(idempotency_key) if idempotency_key is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BatchJobAccepted,
                    parse_obj_as(
                        type_=BatchJobAccepted,
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
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
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
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
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
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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


class AsyncRawParseClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def sync(
        self,
        *,
        idempotency_key: str,
        request: ParseRequest,
        file: typing.Optional[core.File] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ParseResult]:
        """
        Admit a parse job, wait up to the sync wait limit, and return the selected terminal parse
        representation when ready. `output_format` defaults to the versioned provider-neutral
        `openparser@1`; `raw` returns a stable provider envelope around the selected provider's
        untouched successful result. Terminal `failed` within the wait window returns `422`
        `ErrorResponse`; terminal `indeterminate` returns `504` `ErrorResponse`. Returns `202`
        with a durable job reference and `Location` if the wait limit expires first.
        
        Example (`multipart/form-data`):
        
        ```bash
        curl -X POST 'https://api.openparser.dev/parse' \\
          -H 'Authorization: Bearer YOUR_API_KEY' \\
          -H "Idempotency-Key: $(uuidgen 2>/dev/null || openssl rand -hex 16)" \\
          -F 'request={"ocr_model":"paddleocr-vl-1.6","output_format":"openparser@1"};type=application/json' \\
          -F 'file=@./document.pdf'
        ```
        
        Parameters
        ----------
        idempotency_key : str
            Client-supplied idempotency key. Required on every parse or extract `POST`. Must be unique per distinct
            request body for a given tenant and operation.
        
        request : ParseRequest
        
        file : typing.Optional[core.File]
            See core.File for more documentation
        
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.
        
        Returns
        -------
        AsyncHttpResponse[ParseResult]
            Terminal parse result in the selected `openparser@1` or `raw` representation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "parse",
            method="POST",
            data={},
            files={
                **({"file": file} if file is not None else {}),
                "request": (None, json.dumps(jsonable_encoder(request)), "application/json"),
            },
            headers={
                "Idempotency-Key": str(idempotency_key) if idempotency_key is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ParseResult,
                    parse_obj_as(
                        type_=ParseResult,
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
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
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
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
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
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 504:
                raise GatewayTimeoutError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def async_(
        self,
        *,
        idempotency_key: str,
        request: ParseRequest,
        file: typing.Optional[core.File] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[JobAccepted]:
        """
        Admit a durable parse job and return immediately.
        
        Example (`multipart/form-data`):
        
        ```bash
        curl -X POST 'https://api.openparser.dev/parse/async' \\
          -H 'Authorization: Bearer YOUR_API_KEY' \\
          -H "Idempotency-Key: $(uuidgen 2>/dev/null || openssl rand -hex 16)" \\
          -F 'request={"ocr_model":"paddleocr-vl-1.6","output_format":"openparser@1"};type=application/json' \\
          -F 'file=@./document.pdf'
        ```
        
        Parameters
        ----------
        idempotency_key : str
            Client-supplied idempotency key. Required on every parse or extract `POST`. Must be unique per distinct
            request body for a given tenant and operation.
        
        request : ParseRequest
        
        file : typing.Optional[core.File]
            See core.File for more documentation
        
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.
        
        Returns
        -------
        AsyncHttpResponse[JobAccepted]
            Durable non-terminal job admitted. Returned by async endpoints and by sync endpoints when
            the wait limit expires before a terminal status.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "parse/async",
            method="POST",
            data={},
            files={
                **({"file": file} if file is not None else {}),
                "request": (None, json.dumps(jsonable_encoder(request)), "application/json"),
            },
            headers={
                "Idempotency-Key": str(idempotency_key) if idempotency_key is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JobAccepted,
                    parse_obj_as(
                        type_=JobAccepted,
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
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
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
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
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
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def batch(
        self,
        *,
        idempotency_key: str,
        request: ParseBatchRequest,
        files: typing.Optional[typing.List[core.File]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BatchJobAccepted]:
        """
        Admit up to 100 parse child jobs in one durable batch. Every uploaded file must be mapped
        exactly once by `file_index`. Partial child failures are preserved in batch results.
        Parent status derivation for mixed outcomes is defined on `JobStatus`.

        Parameters
        ----------
        idempotency_key : str
            Client-supplied idempotency key. Required on every parse or extract `POST`. Must be unique per distinct
            request body for a given tenant and operation.

        request : ParseBatchRequest

        files : typing.Optional[typing.List[core.File]]
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BatchJobAccepted]
            Durable batch job admitted. `Location` points at the parent batch job resource.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "parse/batch",
            method="POST",
            data={},
            files={
                **({"files": files} if files is not None else {}),
                "request": (None, json.dumps(jsonable_encoder(request)), "application/json"),
            },
            headers={
                "Idempotency-Key": str(idempotency_key) if idempotency_key is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BatchJobAccepted,
                    parse_obj_as(
                        type_=BatchJobAccepted,
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
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
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
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
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
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

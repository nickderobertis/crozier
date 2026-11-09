

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..types.error_response import ErrorResponse
from .types.append_audit_response import AppendAuditResponse
from .types.compact_audit_request_compaction import CompactAuditRequestCompaction
from .types.compact_audit_response import CompactAuditResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawAuditClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def append_audit(
        self,
        *,
        audit_event: typing.Dict[str, typing.Any],
        signature: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AppendAuditResponse]:
        """
        Appends a signed audit event to the agent's audit chain, verifying prev_hash continuity.

        Parameters
        ----------
        audit_event : typing.Dict[str, typing.Any]

        signature : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AppendAuditResponse]
            Audit event appended
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/audit/append",
            method="POST",
            json={
                "audit_event": audit_event,
                "signature": signature,
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
                    AppendAuditResponse,
                    parse_obj_as(
                        type_=AppendAuditResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def compact_audit(
        self, *, compaction: CompactAuditRequestCompaction, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CompactAuditResponse]:
        """
        Submits an audit compaction with a Merkle root covering a range of events.

        Parameters
        ----------
        compaction : CompactAuditRequestCompaction

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CompactAuditResponse]
            Compaction accepted
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/audit/compact",
            method="POST",
            json={
                "compaction": convert_and_respect_annotation_metadata(
                    object_=compaction, annotation=CompactAuditRequestCompaction, direction="write"
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
                _data = typing.cast(
                    CompactAuditResponse,
                    parse_obj_as(
                        type_=CompactAuditResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawAuditClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def append_audit(
        self,
        *,
        audit_event: typing.Dict[str, typing.Any],
        signature: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AppendAuditResponse]:
        """
        Appends a signed audit event to the agent's audit chain, verifying prev_hash continuity.

        Parameters
        ----------
        audit_event : typing.Dict[str, typing.Any]

        signature : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AppendAuditResponse]
            Audit event appended
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/audit/append",
            method="POST",
            json={
                "audit_event": audit_event,
                "signature": signature,
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
                    AppendAuditResponse,
                    parse_obj_as(
                        type_=AppendAuditResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def compact_audit(
        self, *, compaction: CompactAuditRequestCompaction, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CompactAuditResponse]:
        """
        Submits an audit compaction with a Merkle root covering a range of events.

        Parameters
        ----------
        compaction : CompactAuditRequestCompaction

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CompactAuditResponse]
            Compaction accepted
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/audit/compact",
            method="POST",
            json={
                "compaction": convert_and_respect_annotation_metadata(
                    object_=compaction, annotation=CompactAuditRequestCompaction, direction="write"
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
                _data = typing.cast(
                    CompactAuditResponse,
                    parse_obj_as(
                        type_=CompactAuditResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

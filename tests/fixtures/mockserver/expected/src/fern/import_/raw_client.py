

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
from ..types.expectation import Expectation
from ..types.request_definition import RequestDefinition
from .types.put_mockserver_import_request_format import PutMockserverImportRequestFormat
from .types.put_mockserver_import_request_source import PutMockserverImportRequestSource
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawImportClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def import_expectations_from_a_har_or_postman_collection_or_re_import_recorded_traffic(
        self,
        *,
        request: typing.Dict[str, typing.Any],
        format: typing.Optional[PutMockserverImportRequestFormat] = None,
        source: typing.Optional[PutMockserverImportRequestSource] = None,
        redact_sensitive_data: typing.Optional[bool] = None,
        additional_redacted_headers: typing.Optional[str] = None,
        additional_redacted_body_fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Expectation]]:
        """
        Converts an HTTP Archive (HAR) export or a Postman collection into MockServer expectations and adds them. The format is auto-detected from the document structure or can be forced with the format query parameter.

        With format=recording this instead re-imports a persisted NDJSON archive of recorded request/response pairs (one per line) back into the event log, so they become retrievable like in-memory recordings. That mode creates log entries rather than expectations.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        format : typing.Optional[PutMockserverImportRequestFormat]
            forces the import format, supported values are "har", "postman" and "recording"; when omitted the format is auto-detected from the request body. "recording" selects the recorded-traffic NDJSON re-import rather than expectation import.

        source : typing.Optional[PutMockserverImportRequestSource]
            only used with format=recording. When "disk" - or whenever the request body is empty - the NDJSON archive is read from the path configured by persistedRecordedRequestsPath instead of from the request body; a missing archive file is a 400.

        redact_sensitive_data : typing.Optional[bool]
            redact sensitive headers and body fields from the imported document; enabled unless set to the literal "false"

        additional_redacted_headers : typing.Optional[str]
            comma-separated header names to redact in addition to the built-in set

        additional_redacted_body_fields : typing.Optional[str]
            comma-separated body field names to redact in addition to the built-in set

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Expectation]]
            expectations created from the imported document
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/import",
            method="PUT",
            params={
                "format": format,
                "source": source,
                "redactSensitiveData": redact_sensitive_data,
                "additionalRedactedHeaders": additional_redacted_headers,
                "additionalRedactedBodyFields": additional_redacted_body_fields,
            },
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Expectation],
                    parse_obj_as(
                        type_=typing.List[Expectation],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def promote_recorded_traffic_to_active_expectations(
        self,
        *,
        request: RequestDefinition,
        consolidate: typing.Optional[bool] = None,
        parameterize: typing.Optional[bool] = None,
        redact_sensitive_data: typing.Optional[bool] = None,
        additional_redacted_headers: typing.Optional[str] = None,
        additional_redacted_body_fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Expectation]]:
        """
        Retrieves recorded (forwarded) exchanges matching an optional request-matcher filter, consolidates them into reusable mocks and ACTIVATES them by adding them to the expectation set. Redaction is on by default so promoted mocks never carry captured credentials; consolidation and parameterization are also on by default, so a single recorded id does not pin the mock. The request body is optional — omit it to promote every recorded exchange.

        Parameters
        ----------
        request : RequestDefinition

        consolidate : typing.Optional[bool]
            collapse matching exchanges into unlimited-times expectations; set false to promote verbatim

        parameterize : typing.Optional[bool]
            generalise volatile path, query, header and body values

        redact_sensitive_data : typing.Optional[bool]
            redact credentials captured in the recorded traffic

        additional_redacted_headers : typing.Optional[str]
            comma-separated additional header names to redact

        additional_redacted_body_fields : typing.Optional[str]
            comma-separated additional body field names to redact

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Expectation]]
            recordings promoted to active expectations
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/recordings/promote",
            method="PUT",
            params={
                "consolidate": consolidate,
                "parameterize": parameterize,
                "redactSensitiveData": redact_sensitive_data,
                "additionalRedactedHeaders": additional_redacted_headers,
                "additionalRedactedBodyFields": additional_redacted_body_fields,
            },
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=RequestDefinition, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Expectation],
                    parse_obj_as(
                        type_=typing.List[Expectation],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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


class AsyncRawImportClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def import_expectations_from_a_har_or_postman_collection_or_re_import_recorded_traffic(
        self,
        *,
        request: typing.Dict[str, typing.Any],
        format: typing.Optional[PutMockserverImportRequestFormat] = None,
        source: typing.Optional[PutMockserverImportRequestSource] = None,
        redact_sensitive_data: typing.Optional[bool] = None,
        additional_redacted_headers: typing.Optional[str] = None,
        additional_redacted_body_fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Expectation]]:
        """
        Converts an HTTP Archive (HAR) export or a Postman collection into MockServer expectations and adds them. The format is auto-detected from the document structure or can be forced with the format query parameter.

        With format=recording this instead re-imports a persisted NDJSON archive of recorded request/response pairs (one per line) back into the event log, so they become retrievable like in-memory recordings. That mode creates log entries rather than expectations.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        format : typing.Optional[PutMockserverImportRequestFormat]
            forces the import format, supported values are "har", "postman" and "recording"; when omitted the format is auto-detected from the request body. "recording" selects the recorded-traffic NDJSON re-import rather than expectation import.

        source : typing.Optional[PutMockserverImportRequestSource]
            only used with format=recording. When "disk" - or whenever the request body is empty - the NDJSON archive is read from the path configured by persistedRecordedRequestsPath instead of from the request body; a missing archive file is a 400.

        redact_sensitive_data : typing.Optional[bool]
            redact sensitive headers and body fields from the imported document; enabled unless set to the literal "false"

        additional_redacted_headers : typing.Optional[str]
            comma-separated header names to redact in addition to the built-in set

        additional_redacted_body_fields : typing.Optional[str]
            comma-separated body field names to redact in addition to the built-in set

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Expectation]]
            expectations created from the imported document
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/import",
            method="PUT",
            params={
                "format": format,
                "source": source,
                "redactSensitiveData": redact_sensitive_data,
                "additionalRedactedHeaders": additional_redacted_headers,
                "additionalRedactedBodyFields": additional_redacted_body_fields,
            },
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Expectation],
                    parse_obj_as(
                        type_=typing.List[Expectation],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def promote_recorded_traffic_to_active_expectations(
        self,
        *,
        request: RequestDefinition,
        consolidate: typing.Optional[bool] = None,
        parameterize: typing.Optional[bool] = None,
        redact_sensitive_data: typing.Optional[bool] = None,
        additional_redacted_headers: typing.Optional[str] = None,
        additional_redacted_body_fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Expectation]]:
        """
        Retrieves recorded (forwarded) exchanges matching an optional request-matcher filter, consolidates them into reusable mocks and ACTIVATES them by adding them to the expectation set. Redaction is on by default so promoted mocks never carry captured credentials; consolidation and parameterization are also on by default, so a single recorded id does not pin the mock. The request body is optional — omit it to promote every recorded exchange.

        Parameters
        ----------
        request : RequestDefinition

        consolidate : typing.Optional[bool]
            collapse matching exchanges into unlimited-times expectations; set false to promote verbatim

        parameterize : typing.Optional[bool]
            generalise volatile path, query, header and body values

        redact_sensitive_data : typing.Optional[bool]
            redact credentials captured in the recorded traffic

        additional_redacted_headers : typing.Optional[str]
            comma-separated additional header names to redact

        additional_redacted_body_fields : typing.Optional[str]
            comma-separated additional body field names to redact

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Expectation]]
            recordings promoted to active expectations
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/recordings/promote",
            method="PUT",
            params={
                "consolidate": consolidate,
                "parameterize": parameterize,
                "redactSensitiveData": redact_sensitive_data,
                "additionalRedactedHeaders": additional_redacted_headers,
                "additionalRedactedBodyFields": additional_redacted_body_fields,
            },
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=RequestDefinition, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Expectation],
                    parse_obj_as(
                        type_=typing.List[Expectation],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

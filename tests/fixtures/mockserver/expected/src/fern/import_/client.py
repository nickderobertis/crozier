

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.expectation import Expectation
from ..types.request_definition import RequestDefinition
from .raw_client import AsyncRawImportClient, RawImportClient
from .types.put_mockserver_import_request_format import PutMockserverImportRequestFormat
from .types.put_mockserver_import_request_source import PutMockserverImportRequestSource


OMIT = typing.cast(typing.Any, ...)


class ImportClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawImportClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawImportClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawImportClient
        """
        return self._raw_client

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
    ) -> typing.List[Expectation]:
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
        typing.List[Expectation]
            expectations created from the imported document

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.import_.import_expectations_from_a_har_or_postman_collection_or_re_import_recorded_traffic(
            request={
                "log": {
                    "version": "1.2",
                    "entries": [
                        {
                            "request": {
                                "method": "GET",
                                "url": "http://example.com/api/users",
                            },
                            "response": {
                                "status": 200,
                                "content": {
                                    "text": '{"users":[{"id":1,"name":"Alice"}]}'
                                },
                            },
                        }
                    ],
                }
            },
        )
        """
        _response = self._raw_client.import_expectations_from_a_har_or_postman_collection_or_re_import_recorded_traffic(
            request=request,
            format=format,
            source=source,
            redact_sensitive_data=redact_sensitive_data,
            additional_redacted_headers=additional_redacted_headers,
            additional_redacted_body_fields=additional_redacted_body_fields,
            request_options=request_options,
        )
        return _response.data

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
    ) -> typing.List[Expectation]:
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
        typing.List[Expectation]
            recordings promoted to active expectations

        Examples
        --------
        from fern import FernApi, HttpRequest

        client = FernApi()
        client.import_.promote_recorded_traffic_to_active_expectations(
            request=HttpRequest(),
        )
        """
        _response = self._raw_client.promote_recorded_traffic_to_active_expectations(
            request=request,
            consolidate=consolidate,
            parameterize=parameterize,
            redact_sensitive_data=redact_sensitive_data,
            additional_redacted_headers=additional_redacted_headers,
            additional_redacted_body_fields=additional_redacted_body_fields,
            request_options=request_options,
        )
        return _response.data


class AsyncImportClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawImportClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawImportClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawImportClient
        """
        return self._raw_client

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
    ) -> typing.List[Expectation]:
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
        typing.List[Expectation]
            expectations created from the imported document

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.import_.import_expectations_from_a_har_or_postman_collection_or_re_import_recorded_traffic(
                request={
                    "log": {
                        "version": "1.2",
                        "entries": [
                            {
                                "request": {
                                    "method": "GET",
                                    "url": "http://example.com/api/users",
                                },
                                "response": {
                                    "status": 200,
                                    "content": {
                                        "text": '{"users":[{"id":1,"name":"Alice"}]}'
                                    },
                                },
                            }
                        ],
                    }
                },
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.import_expectations_from_a_har_or_postman_collection_or_re_import_recorded_traffic(
                request=request,
                format=format,
                source=source,
                redact_sensitive_data=redact_sensitive_data,
                additional_redacted_headers=additional_redacted_headers,
                additional_redacted_body_fields=additional_redacted_body_fields,
                request_options=request_options,
            )
        )
        return _response.data

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
    ) -> typing.List[Expectation]:
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
        typing.List[Expectation]
            recordings promoted to active expectations

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, HttpRequest

        client = AsyncFernApi()


        async def main() -> None:
            await client.import_.promote_recorded_traffic_to_active_expectations(
                request=HttpRequest(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.promote_recorded_traffic_to_active_expectations(
            request=request,
            consolidate=consolidate,
            parameterize=parameterize,
            redact_sensitive_data=redact_sensitive_data,
            additional_redacted_headers=additional_redacted_headers,
            additional_redacted_body_fields=additional_redacted_body_fields,
            request_options=request_options,
        )
        return _response.data

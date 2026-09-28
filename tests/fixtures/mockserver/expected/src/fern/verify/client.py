

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.http_request import HttpRequest
from ..types.verification import Verification
from ..types.verification_sequence import VerificationSequence
from .raw_client import AsyncRawVerifyClient, RawVerifyClient
from .types.put_mockserver_diff_response import PutMockserverDiffResponse


OMIT = typing.cast(typing.Any, ...)


class VerifyClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawVerifyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawVerifyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawVerifyClient
        """
        return self._raw_client

    def verify_a_request_has_been_received_a_specific_number_of_times(
        self, *, request: Verification, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : Verification

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.verify.verify_a_request_has_been_received_a_specific_number_of_times(
            request={
                "httpRequest": {"method": "GET", "path": "/api/users"},
                "times": {"atLeast": 1},
            },
        )
        """
        _response = self._raw_client.verify_a_request_has_been_received_a_specific_number_of_times(
            request=request, request_options=request_options
        )
        return _response.data

    def verify_a_sequence_of_request_has_been_received_in_the_specific_order(
        self, *, request: VerificationSequence, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : VerificationSequence

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.verify.verify_a_sequence_of_request_has_been_received_in_the_specific_order(
            request={
                "httpRequests": [
                    {"method": "POST", "path": "/api/login"},
                    {"method": "GET", "path": "/api/dashboard"},
                ]
            },
        )
        """
        _response = self._raw_client.verify_a_sequence_of_request_has_been_received_in_the_specific_order(
            request=request, request_options=request_options
        )
        return _response.data

    def compare_two_http_requests_field_by_field(
        self, *, expected: HttpRequest, actual: HttpRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> PutMockserverDiffResponse:
        """
        Diffs an 'expected' against an 'actual' HttpRequest and returns the per-field differences, a total diff count and whether the two requests are identical.

        Parameters
        ----------
        expected : HttpRequest

        actual : HttpRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PutMockserverDiffResponse
            diff computed

        Examples
        --------
        from fern import FernApi, HttpRequest, KeyToMultiValueZeroItem

        client = FernApi()
        client.verify.compare_two_http_requests_field_by_field(
            expected=HttpRequest(
                method="GET",
                path="/api/pets",
                headers=[KeyToMultiValueZeroItem()],
            ),
            actual=HttpRequest(
                method="GET",
                path="/api/pets",
                headers=[KeyToMultiValueZeroItem()],
            ),
        )
        """
        _response = self._raw_client.compare_two_http_requests_field_by_field(
            expected=expected, actual=actual, request_options=request_options
        )
        return _response.data


class AsyncVerifyClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawVerifyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawVerifyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawVerifyClient
        """
        return self._raw_client

    async def verify_a_request_has_been_received_a_specific_number_of_times(
        self, *, request: Verification, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : Verification

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.verify.verify_a_request_has_been_received_a_specific_number_of_times(
                request={
                    "httpRequest": {"method": "GET", "path": "/api/users"},
                    "times": {"atLeast": 1},
                },
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.verify_a_request_has_been_received_a_specific_number_of_times(
            request=request, request_options=request_options
        )
        return _response.data

    async def verify_a_sequence_of_request_has_been_received_in_the_specific_order(
        self, *, request: VerificationSequence, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : VerificationSequence

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.verify.verify_a_sequence_of_request_has_been_received_in_the_specific_order(
                request={
                    "httpRequests": [
                        {"method": "POST", "path": "/api/login"},
                        {"method": "GET", "path": "/api/dashboard"},
                    ]
                },
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.verify_a_sequence_of_request_has_been_received_in_the_specific_order(
            request=request, request_options=request_options
        )
        return _response.data

    async def compare_two_http_requests_field_by_field(
        self, *, expected: HttpRequest, actual: HttpRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> PutMockserverDiffResponse:
        """
        Diffs an 'expected' against an 'actual' HttpRequest and returns the per-field differences, a total diff count and whether the two requests are identical.

        Parameters
        ----------
        expected : HttpRequest

        actual : HttpRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PutMockserverDiffResponse
            diff computed

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, HttpRequest, KeyToMultiValueZeroItem

        client = AsyncFernApi()


        async def main() -> None:
            await client.verify.compare_two_http_requests_field_by_field(
                expected=HttpRequest(
                    method="GET",
                    path="/api/pets",
                    headers=[KeyToMultiValueZeroItem()],
                ),
                actual=HttpRequest(
                    method="GET",
                    path="/api/pets",
                    headers=[KeyToMultiValueZeroItem()],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.compare_two_http_requests_field_by_field(
            expected=expected, actual=actual, request_options=request_options
        )
        return _response.data

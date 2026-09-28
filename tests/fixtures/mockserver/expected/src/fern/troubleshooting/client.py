

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.expectation import Expectation
from ..types.request_definition import RequestDefinition
from .raw_client import AsyncRawTroubleshootingClient, RawTroubleshootingClient
from .types.put_mockserver_traffic_validate_response import PutMockserverTrafficValidateResponse


OMIT = typing.cast(typing.Any, ...)


class TroubleshootingClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTroubleshootingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTroubleshootingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTroubleshootingClient
        """
        return self._raw_client

    def explain_why_recent_requests_did_not_match_any_expectation(
        self, *, limit: typing.Optional[int] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Returns a diagnostic report for recently recorded unmatched requests, including the closest-matching expectations and the per-field differences that prevented a match. An optional 'limit' in the body bounds how many unmatched requests are analysed (default 10).

        Parameters
        ----------
        limit : typing.Optional[int]
            maximum number of recent unmatched requests to analyse

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            unmatched-request explanation returned

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.troubleshooting.explain_why_recent_requests_did_not_match_any_expectation(
            limit=5,
        )
        """
        _response = self._raw_client.explain_why_recent_requests_did_not_match_any_expectation(
            limit=limit, request_options=request_options
        )
        return _response.data

    def return_per_expectation_mismatch_debug_information_for_a_request(
        self, *, request: RequestDefinition, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Evaluates the supplied HttpRequest against every active expectation and returns, for each, whether it matched and the per-field differences, plus a closest match. Only HttpRequest definitions are supported (not OpenAPI definitions).

        Parameters
        ----------
        request : RequestDefinition

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            mismatch debug information returned

        Examples
        --------
        from fern import FernApi, HttpRequest

        client = FernApi()
        client.troubleshooting.return_per_expectation_mismatch_debug_information_for_a_request(
            request=HttpRequest(),
        )
        """
        _response = self._raw_client.return_per_expectation_mismatch_debug_information_for_a_request(
            request=request, request_options=request_options
        )
        return _response.data

    def diff_a_baseline_set_of_expectations_against_another(
        self,
        *,
        baseline: typing.Sequence[Expectation],
        current: typing.Optional[typing.Sequence[Expectation]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Compares a "baseline" array of expectations against a "current" array and returns a structured diff of what was added, removed and changed. When "current" is omitted the baseline is diffed against the instance's live active expectations, which makes this usable as a drift check against a committed baseline.

        Parameters
        ----------
        baseline : typing.Sequence[Expectation]

        current : typing.Optional[typing.Sequence[Expectation]]
            optional; when omitted the live active expectations are used

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            baseline diff report returned

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.troubleshooting.diff_a_baseline_set_of_expectations_against_another(
            baseline=[
                {
                    "httpRequest": {"method": "GET", "path": "/api/orders"},
                    "httpResponse": {"statusCode": 200, "body": '{"orders":[]}'},
                }
            ],
        )
        """
        _response = self._raw_client.diff_a_baseline_set_of_expectations_against_another(
            baseline=baseline, current=current, request_options=request_options
        )
        return _response.data

    def validate_recorded_traffic_against_an_open_api_specification(
        self,
        *,
        spec: typing.Optional[str] = OMIT,
        spec_url_or_payload: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PutMockserverTrafficValidateResponse:
        """
        Validates the request/response pairs already recorded in the event log against an OpenAPI specification, and reports per-exchange which operation it matched and any request or response violations. Supply the spec as a URL, file path or inline JSON/YAML under "spec" (or its alias "specUrlOrPayload"). A spec fetched by URL is subject to the SSRF policy (forwardProxyBlockPrivateNetworks). The traffic validated comes from the recorded event log, not from the request body.

        Parameters
        ----------
        spec : typing.Optional[str]
            OpenAPI spec as a URL, file path or inline JSON/YAML

        spec_url_or_payload : typing.Optional[str]
            accepted alias for "spec"

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PutMockserverTrafficValidateResponse
            validation completed (inspect allPassed and the per-request results)

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.troubleshooting.validate_recorded_traffic_against_an_open_api_specification(
            spec='{"openapi":"3.0.0","info":{"title":"orders","version":"1.0.0"},"paths":{"/api/orders":{"get":{"responses":{"200":{"description":"orders"}}}}}}',
        )
        """
        _response = self._raw_client.validate_recorded_traffic_against_an_open_api_specification(
            spec=spec, spec_url_or_payload=spec_url_or_payload, request_options=request_options
        )
        return _response.data


class AsyncTroubleshootingClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTroubleshootingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTroubleshootingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTroubleshootingClient
        """
        return self._raw_client

    async def explain_why_recent_requests_did_not_match_any_expectation(
        self, *, limit: typing.Optional[int] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Returns a diagnostic report for recently recorded unmatched requests, including the closest-matching expectations and the per-field differences that prevented a match. An optional 'limit' in the body bounds how many unmatched requests are analysed (default 10).

        Parameters
        ----------
        limit : typing.Optional[int]
            maximum number of recent unmatched requests to analyse

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            unmatched-request explanation returned

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.troubleshooting.explain_why_recent_requests_did_not_match_any_expectation(
                limit=5,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.explain_why_recent_requests_did_not_match_any_expectation(
            limit=limit, request_options=request_options
        )
        return _response.data

    async def return_per_expectation_mismatch_debug_information_for_a_request(
        self, *, request: RequestDefinition, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Evaluates the supplied HttpRequest against every active expectation and returns, for each, whether it matched and the per-field differences, plus a closest match. Only HttpRequest definitions are supported (not OpenAPI definitions).

        Parameters
        ----------
        request : RequestDefinition

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            mismatch debug information returned

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, HttpRequest

        client = AsyncFernApi()


        async def main() -> None:
            await client.troubleshooting.return_per_expectation_mismatch_debug_information_for_a_request(
                request=HttpRequest(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.return_per_expectation_mismatch_debug_information_for_a_request(
            request=request, request_options=request_options
        )
        return _response.data

    async def diff_a_baseline_set_of_expectations_against_another(
        self,
        *,
        baseline: typing.Sequence[Expectation],
        current: typing.Optional[typing.Sequence[Expectation]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Compares a "baseline" array of expectations against a "current" array and returns a structured diff of what was added, removed and changed. When "current" is omitted the baseline is diffed against the instance's live active expectations, which makes this usable as a drift check against a committed baseline.

        Parameters
        ----------
        baseline : typing.Sequence[Expectation]

        current : typing.Optional[typing.Sequence[Expectation]]
            optional; when omitted the live active expectations are used

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            baseline diff report returned

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.troubleshooting.diff_a_baseline_set_of_expectations_against_another(
                baseline=[
                    {
                        "httpRequest": {"method": "GET", "path": "/api/orders"},
                        "httpResponse": {"statusCode": 200, "body": '{"orders":[]}'},
                    }
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.diff_a_baseline_set_of_expectations_against_another(
            baseline=baseline, current=current, request_options=request_options
        )
        return _response.data

    async def validate_recorded_traffic_against_an_open_api_specification(
        self,
        *,
        spec: typing.Optional[str] = OMIT,
        spec_url_or_payload: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PutMockserverTrafficValidateResponse:
        """
        Validates the request/response pairs already recorded in the event log against an OpenAPI specification, and reports per-exchange which operation it matched and any request or response violations. Supply the spec as a URL, file path or inline JSON/YAML under "spec" (or its alias "specUrlOrPayload"). A spec fetched by URL is subject to the SSRF policy (forwardProxyBlockPrivateNetworks). The traffic validated comes from the recorded event log, not from the request body.

        Parameters
        ----------
        spec : typing.Optional[str]
            OpenAPI spec as a URL, file path or inline JSON/YAML

        spec_url_or_payload : typing.Optional[str]
            accepted alias for "spec"

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PutMockserverTrafficValidateResponse
            validation completed (inspect allPassed and the per-request results)

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.troubleshooting.validate_recorded_traffic_against_an_open_api_specification(
                spec='{"openapi":"3.0.0","info":{"title":"orders","version":"1.0.0"},"paths":{"/api/orders":{"get":{"responses":{"200":{"description":"orders"}}}}}}',
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.validate_recorded_traffic_against_an_open_api_specification(
            spec=spec, spec_url_or_payload=spec_url_or_payload, request_options=request_options
        )
        return _response.data

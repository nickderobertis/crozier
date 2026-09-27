

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.expectation import Expectation
from .raw_client import AsyncRawPactClient, RawPactClient


OMIT = typing.cast(typing.Any, ...)


class PactClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPactClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPactClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPactClient
        """
        return self._raw_client

    def export_active_expectations_as_a_pact_contract(
        self,
        *,
        consumer: typing.Optional[str] = None,
        provider: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Exports the current active expectations as a Pact consumer-driven contract (JSON). The optional 'consumer' and 'provider' query parameters set the contract's consumer and provider names.

        Parameters
        ----------
        consumer : typing.Optional[str]
            consumer name to record in the exported Pact contract

        provider : typing.Optional[str]
            provider name to record in the exported Pact contract

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Pact contract exported

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.pact.export_active_expectations_as_a_pact_contract()
        """
        _response = self._raw_client.export_active_expectations_as_a_pact_contract(
            consumer=consumer, provider=provider, request_options=request_options
        )
        return _response.data

    def verify_active_expectations_against_a_pact_contract(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Verifies the supplied Pact contract (JSON) against the current expectations and returns the verification result. Returns 202 when verification passes and 406 when it fails.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Pact verification passed

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.pact.verify_active_expectations_against_a_pact_contract(
            request={
                "consumer": {"name": "web-app"},
                "provider": {"name": "api-service"},
                "interactions": [
                    {
                        "description": "a health check request",
                        "request": {"method": "GET", "path": "/api/health"},
                        "response": {
                            "status": 200,
                            "headers": {"content-type": "application/json"},
                            "body": {"status": "ok"},
                        },
                    }
                ],
            },
        )
        """
        _response = self._raw_client.verify_active_expectations_against_a_pact_contract(
            request=request, request_options=request_options
        )
        return _response.data

    def import_a_pact_contract_as_expectations(
        self,
        *,
        request: typing.Dict[str, typing.Any],
        redact_sensitive_data: typing.Optional[bool] = None,
        additional_redacted_headers: typing.Optional[str] = None,
        additional_redacted_body_fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Expectation]:
        """
        Parses a Pact v3 consumer-driven contract and adds the interactions it describes to the active expectation set. Redaction is applied on import so credentials present in the contract are not retained.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        redact_sensitive_data : typing.Optional[bool]
            redact credentials found in the imported contract

        additional_redacted_headers : typing.Optional[str]
            comma-separated additional header names to redact

        additional_redacted_body_fields : typing.Optional[str]
            comma-separated additional body field names to redact

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Expectation]
            Pact contract imported as expectations

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.pact.import_a_pact_contract_as_expectations(
            request={
                "consumer": {"name": "checkout-service"},
                "provider": {"name": "orders-service"},
                "interactions": [
                    {
                        "description": "a request for all orders",
                        "request": {"method": "GET", "path": "/api/orders"},
                        "response": {
                            "status": 200,
                            "headers": {"Content-Type": "application/json"},
                            "body": {},
                        },
                    }
                ],
                "metadata": {"pactSpecification": {"version": "3.0.0"}},
            },
        )
        """
        _response = self._raw_client.import_a_pact_contract_as_expectations(
            request=request,
            redact_sensitive_data=redact_sensitive_data,
            additional_redacted_headers=additional_redacted_headers,
            additional_redacted_body_fields=additional_redacted_body_fields,
            request_options=request_options,
        )
        return _response.data


class AsyncPactClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPactClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPactClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPactClient
        """
        return self._raw_client

    async def export_active_expectations_as_a_pact_contract(
        self,
        *,
        consumer: typing.Optional[str] = None,
        provider: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Exports the current active expectations as a Pact consumer-driven contract (JSON). The optional 'consumer' and 'provider' query parameters set the contract's consumer and provider names.

        Parameters
        ----------
        consumer : typing.Optional[str]
            consumer name to record in the exported Pact contract

        provider : typing.Optional[str]
            provider name to record in the exported Pact contract

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Pact contract exported

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.pact.export_active_expectations_as_a_pact_contract()


        asyncio.run(main())
        """
        _response = await self._raw_client.export_active_expectations_as_a_pact_contract(
            consumer=consumer, provider=provider, request_options=request_options
        )
        return _response.data

    async def verify_active_expectations_against_a_pact_contract(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Verifies the supplied Pact contract (JSON) against the current expectations and returns the verification result. Returns 202 when verification passes and 406 when it fails.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Pact verification passed

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.pact.verify_active_expectations_against_a_pact_contract(
                request={
                    "consumer": {"name": "web-app"},
                    "provider": {"name": "api-service"},
                    "interactions": [
                        {
                            "description": "a health check request",
                            "request": {"method": "GET", "path": "/api/health"},
                            "response": {
                                "status": 200,
                                "headers": {"content-type": "application/json"},
                                "body": {"status": "ok"},
                            },
                        }
                    ],
                },
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.verify_active_expectations_against_a_pact_contract(
            request=request, request_options=request_options
        )
        return _response.data

    async def import_a_pact_contract_as_expectations(
        self,
        *,
        request: typing.Dict[str, typing.Any],
        redact_sensitive_data: typing.Optional[bool] = None,
        additional_redacted_headers: typing.Optional[str] = None,
        additional_redacted_body_fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Expectation]:
        """
        Parses a Pact v3 consumer-driven contract and adds the interactions it describes to the active expectation set. Redaction is applied on import so credentials present in the contract are not retained.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        redact_sensitive_data : typing.Optional[bool]
            redact credentials found in the imported contract

        additional_redacted_headers : typing.Optional[str]
            comma-separated additional header names to redact

        additional_redacted_body_fields : typing.Optional[str]
            comma-separated additional body field names to redact

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Expectation]
            Pact contract imported as expectations

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.pact.import_a_pact_contract_as_expectations(
                request={
                    "consumer": {"name": "checkout-service"},
                    "provider": {"name": "orders-service"},
                    "interactions": [
                        {
                            "description": "a request for all orders",
                            "request": {"method": "GET", "path": "/api/orders"},
                            "response": {
                                "status": 200,
                                "headers": {"Content-Type": "application/json"},
                                "body": {},
                            },
                        }
                    ],
                    "metadata": {"pactSpecification": {"version": "3.0.0"}},
                },
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.import_a_pact_contract_as_expectations(
            request=request,
            redact_sensitive_data=redact_sensitive_data,
            additional_redacted_headers=additional_redacted_headers,
            additional_redacted_body_fields=additional_redacted_body_fields,
            request_options=request_options,
        )
        return _response.data

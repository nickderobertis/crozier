

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.contract_test_report import ContractTestReport
from .raw_client import AsyncRawContractClient, RawContractClient


OMIT = typing.cast(typing.Any, ...)


class ContractClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawContractClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawContractClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawContractClient
        """
        return self._raw_client

    def run_an_open_api_spec_as_a_contract_test_against_a_live_service(
        self,
        *,
        spec: str,
        base_url: str,
        spec_url_or_payload: typing.Optional[str] = OMIT,
        operation_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContractTestReport:
        """
        Runs each operation of an OpenAPI specification against a live service and validates that the actual responses conform to the spec. Supply the spec as a URL, file path or inline JSON/YAML ("spec", or its alias "specUrlOrPayload"), the base URL of the service under test ("baseUrl"), and optionally a single "operationId" to restrict the run. The target host is subject to the SSRF policy (forwardProxyBlockPrivateNetworks). Returns a per-operation pass/fail report.

        Parameters
        ----------
        spec : str
            the OpenAPI spec as a URL, file path, or inline JSON/YAML (alias: specUrlOrPayload)

        base_url : str
            base URL of the live service under test; any path prefix is prepended to each operation path

        spec_url_or_payload : typing.Optional[str]
            alias for spec

        operation_id : typing.Optional[str]
            optional — restrict the run to a single operation; when absent all operations are tested

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContractTestReport
            contract test completed (inspect allPassed and per-operation results)

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.contract.run_an_open_api_spec_as_a_contract_test_against_a_live_service(
            spec='openapi: 3.0.0\ninfo:\n  title: Petstore\n  version: 1.0.0\npaths:\n  /pets:\n    get:\n      operationId: listPets\n      responses:\n        "200":\n          description: a list of pets',
            base_url="http://localhost:8080",
            operation_id="listPets",
        )
        """
        _response = self._raw_client.run_an_open_api_spec_as_a_contract_test_against_a_live_service(
            spec=spec,
            base_url=base_url,
            spec_url_or_payload=spec_url_or_payload,
            operation_id=operation_id,
            request_options=request_options,
        )
        return _response.data


class AsyncContractClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawContractClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawContractClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawContractClient
        """
        return self._raw_client

    async def run_an_open_api_spec_as_a_contract_test_against_a_live_service(
        self,
        *,
        spec: str,
        base_url: str,
        spec_url_or_payload: typing.Optional[str] = OMIT,
        operation_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContractTestReport:
        """
        Runs each operation of an OpenAPI specification against a live service and validates that the actual responses conform to the spec. Supply the spec as a URL, file path or inline JSON/YAML ("spec", or its alias "specUrlOrPayload"), the base URL of the service under test ("baseUrl"), and optionally a single "operationId" to restrict the run. The target host is subject to the SSRF policy (forwardProxyBlockPrivateNetworks). Returns a per-operation pass/fail report.

        Parameters
        ----------
        spec : str
            the OpenAPI spec as a URL, file path, or inline JSON/YAML (alias: specUrlOrPayload)

        base_url : str
            base URL of the live service under test; any path prefix is prepended to each operation path

        spec_url_or_payload : typing.Optional[str]
            alias for spec

        operation_id : typing.Optional[str]
            optional — restrict the run to a single operation; when absent all operations are tested

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContractTestReport
            contract test completed (inspect allPassed and per-operation results)

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.contract.run_an_open_api_spec_as_a_contract_test_against_a_live_service(
                spec='openapi: 3.0.0\ninfo:\n  title: Petstore\n  version: 1.0.0\npaths:\n  /pets:\n    get:\n      operationId: listPets\n      responses:\n        "200":\n          description: a list of pets',
                base_url="http://localhost:8080",
                operation_id="listPets",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.run_an_open_api_spec_as_a_contract_test_against_a_live_service(
            spec=spec,
            base_url=base_url,
            spec_url_or_payload=spec_url_or_payload,
            operation_id=operation_id,
            request_options=request_options,
        )
        return _response.data



import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.access_token import AccessToken
from ..types.consent_id import ConsentId
from ..types.contract_id import ContractId
from ..types.data_id import DataId
from ..types.execution_result import ExecutionResult
from ..types.function_id import FunctionId
from ..types.private_execution_result import PrivateExecutionResult
from .raw_client import AsyncRawCustomerApiClient, RawCustomerApiClient


OMIT = typing.cast(typing.Any, ...)


class CustomerApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCustomerApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCustomerApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCustomerApiClient
        """
        return self._raw_client

    def request_edge_proc(
        self,
        *,
        function: typing.Optional[FunctionId] = OMIT,
        data: typing.Optional[DataId] = OMIT,
        data_contract: typing.Optional[ContractId] = OMIT,
        func_contract: typing.Optional[ContractId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExecutionResult:
        """


        Parameters
        ----------
        function : typing.Optional[FunctionId]

        data : typing.Optional[DataId]

        data_contract : typing.Optional[ContractId]

        func_contract : typing.Optional[ContractId]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExecutionResult
            Successful function deployment

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.customer_api.request_edge_proc()
        """
        _response = self._raw_client.request_edge_proc(
            function=function,
            data=data,
            data_contract=data_contract,
            func_contract=func_contract,
            request_options=request_options,
        )
        return _response.data

    def request_privacy_edge_proc(
        self,
        *,
        function: typing.Optional[FunctionId] = OMIT,
        private_data: typing.Optional[DataId] = OMIT,
        data_contract: typing.Optional[ContractId] = OMIT,
        func_contract: typing.Optional[ContractId] = OMIT,
        consent: typing.Optional[ConsentId] = OMIT,
        token: typing.Optional[AccessToken] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PrivateExecutionResult:
        """


        Parameters
        ----------
        function : typing.Optional[FunctionId]

        private_data : typing.Optional[DataId]

        data_contract : typing.Optional[ContractId]

        func_contract : typing.Optional[ContractId]

        consent : typing.Optional[ConsentId]

        token : typing.Optional[AccessToken]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PrivateExecutionResult
            Successful function deployment

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.customer_api.request_privacy_edge_proc()
        """
        _response = self._raw_client.request_privacy_edge_proc(
            function=function,
            private_data=private_data,
            data_contract=data_contract,
            func_contract=func_contract,
            consent=consent,
            token=token,
            request_options=request_options,
        )
        return _response.data


class AsyncCustomerApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCustomerApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCustomerApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCustomerApiClient
        """
        return self._raw_client

    async def request_edge_proc(
        self,
        *,
        function: typing.Optional[FunctionId] = OMIT,
        data: typing.Optional[DataId] = OMIT,
        data_contract: typing.Optional[ContractId] = OMIT,
        func_contract: typing.Optional[ContractId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExecutionResult:
        """


        Parameters
        ----------
        function : typing.Optional[FunctionId]

        data : typing.Optional[DataId]

        data_contract : typing.Optional[ContractId]

        func_contract : typing.Optional[ContractId]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExecutionResult
            Successful function deployment

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.customer_api.request_edge_proc()


        asyncio.run(main())
        """
        _response = await self._raw_client.request_edge_proc(
            function=function,
            data=data,
            data_contract=data_contract,
            func_contract=func_contract,
            request_options=request_options,
        )
        return _response.data

    async def request_privacy_edge_proc(
        self,
        *,
        function: typing.Optional[FunctionId] = OMIT,
        private_data: typing.Optional[DataId] = OMIT,
        data_contract: typing.Optional[ContractId] = OMIT,
        func_contract: typing.Optional[ContractId] = OMIT,
        consent: typing.Optional[ConsentId] = OMIT,
        token: typing.Optional[AccessToken] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PrivateExecutionResult:
        """


        Parameters
        ----------
        function : typing.Optional[FunctionId]

        private_data : typing.Optional[DataId]

        data_contract : typing.Optional[ContractId]

        func_contract : typing.Optional[ContractId]

        consent : typing.Optional[ConsentId]

        token : typing.Optional[AccessToken]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PrivateExecutionResult
            Successful function deployment

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.customer_api.request_privacy_edge_proc()


        asyncio.run(main())
        """
        _response = await self._raw_client.request_privacy_edge_proc(
            function=function,
            private_data=private_data,
            data_contract=data_contract,
            func_contract=func_contract,
            consent=consent,
            token=token,
            request_options=request_options,
        )
        return _response.data

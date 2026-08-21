

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.consent_id import ConsentId
from ..types.contract_id import ContractId
from ..types.data_id import DataId
from ..types.data_provider_id import DataProviderId
from ..types.function import Function
from ..types.function_id import FunctionId
from ..types.privacy_zone_data import PrivacyZoneData
from ..types.private_data import PrivateData
from .raw_client import AsyncRawConnectorApiClient, RawConnectorApiClient


OMIT = typing.cast(typing.Any, ...)


class ConnectorApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawConnectorApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawConnectorApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawConnectorApiClient
        """
        return self._raw_client

    def get_pz_data(
        self,
        *,
        data_provider: typing.Optional[DataProviderId] = OMIT,
        private_data: typing.Optional[DataId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PrivacyZoneData:
        """


        Parameters
        ----------
        data_provider : typing.Optional[DataProviderId]

        private_data : typing.Optional[DataId]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PrivacyZoneData
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.connector_api.get_pz_data()
        """
        _response = self._raw_client.get_pz_data(
            data_provider=data_provider, private_data=private_data, request_options=request_options
        )
        return _response.data

    def request_function(
        self,
        *,
        function: typing.Optional[FunctionId] = OMIT,
        func_contract: typing.Optional[ContractId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Function:
        """


        Parameters
        ----------
        function : typing.Optional[FunctionId]

        func_contract : typing.Optional[ContractId]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Function
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.connector_api.request_function()
        """
        _response = self._raw_client.request_function(
            function=function, func_contract=func_contract, request_options=request_options
        )
        return _response.data

    def request_privacy_preserving_data(
        self,
        *,
        private_data: typing.Optional[DataId] = OMIT,
        data_contract: typing.Optional[ContractId] = OMIT,
        consent: typing.Optional[ConsentId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PrivateData:
        """


        Parameters
        ----------
        private_data : typing.Optional[DataId]

        data_contract : typing.Optional[ContractId]

        consent : typing.Optional[ConsentId]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PrivateData
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.connector_api.request_privacy_preserving_data()
        """
        _response = self._raw_client.request_privacy_preserving_data(
            private_data=private_data, data_contract=data_contract, consent=consent, request_options=request_options
        )
        return _response.data


class AsyncConnectorApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawConnectorApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawConnectorApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawConnectorApiClient
        """
        return self._raw_client

    async def get_pz_data(
        self,
        *,
        data_provider: typing.Optional[DataProviderId] = OMIT,
        private_data: typing.Optional[DataId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PrivacyZoneData:
        """


        Parameters
        ----------
        data_provider : typing.Optional[DataProviderId]

        private_data : typing.Optional[DataId]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PrivacyZoneData
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.connector_api.get_pz_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_pz_data(
            data_provider=data_provider, private_data=private_data, request_options=request_options
        )
        return _response.data

    async def request_function(
        self,
        *,
        function: typing.Optional[FunctionId] = OMIT,
        func_contract: typing.Optional[ContractId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Function:
        """


        Parameters
        ----------
        function : typing.Optional[FunctionId]

        func_contract : typing.Optional[ContractId]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Function
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.connector_api.request_function()


        asyncio.run(main())
        """
        _response = await self._raw_client.request_function(
            function=function, func_contract=func_contract, request_options=request_options
        )
        return _response.data

    async def request_privacy_preserving_data(
        self,
        *,
        private_data: typing.Optional[DataId] = OMIT,
        data_contract: typing.Optional[ContractId] = OMIT,
        consent: typing.Optional[ConsentId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PrivateData:
        """


        Parameters
        ----------
        private_data : typing.Optional[DataId]

        data_contract : typing.Optional[ContractId]

        consent : typing.Optional[ConsentId]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PrivateData
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.connector_api.request_privacy_preserving_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.request_privacy_preserving_data(
            private_data=private_data, data_contract=data_contract, consent=consent, request_options=request_options
        )
        return _response.data



import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.register_result import RegisterResult
from .raw_client import AsyncRawRegistryApiClient, RawRegistryApiClient


OMIT = typing.cast(typing.Any, ...)


class RegistryApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRegistryApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRegistryApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRegistryApiClient
        """
        return self._raw_client

    def register_product_dpp(
        self,
        *,
        unique_product_identifier: str,
        digital_product_passport_id: str,
        unique_economic_operator_identifier: str,
        dpp_api_endpoint: str,
        backup_unique_economic_operator_identifier: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RegisterResult:
        """
        Registers a new DPP at the DPP registry (served by the registry server) and returns a unique registration identifier.

        Parameters
        ----------
        unique_product_identifier : str
            Unique product identifier per EN 18219.

        digital_product_passport_id : str
            The DPP instance identifier.

        unique_economic_operator_identifier : str
            Economic operator identifier per EN 18219.

        dpp_api_endpoint : str
            URL of the DPP API service hosting this DPP.

        backup_unique_economic_operator_identifier : typing.Optional[str]
            Economic operator identifier of the back-up operator per EN 18219.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RegisterResult
            DPP registered.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            api_key="YOUR_API_KEY",
            api_key_secret="YOUR_API_KEY_SECRET",
            token="YOUR_TOKEN",
        )
        client.registry_api.register_product_dpp(
            unique_product_identifier="uniqueProductIdentifier",
            digital_product_passport_id="digitalProductPassportId",
            unique_economic_operator_identifier="uniqueEconomicOperatorIdentifier",
            dpp_api_endpoint="dppApiEndpoint",
        )
        """
        _response = self._raw_client.register_product_dpp(
            unique_product_identifier=unique_product_identifier,
            digital_product_passport_id=digital_product_passport_id,
            unique_economic_operator_identifier=unique_economic_operator_identifier,
            dpp_api_endpoint=dpp_api_endpoint,
            backup_unique_economic_operator_identifier=backup_unique_economic_operator_identifier,
            request_options=request_options,
        )
        return _response.data


class AsyncRegistryApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRegistryApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRegistryApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRegistryApiClient
        """
        return self._raw_client

    async def register_product_dpp(
        self,
        *,
        unique_product_identifier: str,
        digital_product_passport_id: str,
        unique_economic_operator_identifier: str,
        dpp_api_endpoint: str,
        backup_unique_economic_operator_identifier: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RegisterResult:
        """
        Registers a new DPP at the DPP registry (served by the registry server) and returns a unique registration identifier.

        Parameters
        ----------
        unique_product_identifier : str
            Unique product identifier per EN 18219.

        digital_product_passport_id : str
            The DPP instance identifier.

        unique_economic_operator_identifier : str
            Economic operator identifier per EN 18219.

        dpp_api_endpoint : str
            URL of the DPP API service hosting this DPP.

        backup_unique_economic_operator_identifier : typing.Optional[str]
            Economic operator identifier of the back-up operator per EN 18219.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RegisterResult
            DPP registered.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            api_key="YOUR_API_KEY",
            api_key_secret="YOUR_API_KEY_SECRET",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.registry_api.register_product_dpp(
                unique_product_identifier="uniqueProductIdentifier",
                digital_product_passport_id="digitalProductPassportId",
                unique_economic_operator_identifier="uniqueEconomicOperatorIdentifier",
                dpp_api_endpoint="dppApiEndpoint",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.register_product_dpp(
            unique_product_identifier=unique_product_identifier,
            digital_product_passport_id=digital_product_passport_id,
            unique_economic_operator_identifier=unique_economic_operator_identifier,
            dpp_api_endpoint=dpp_api_endpoint,
            backup_unique_economic_operator_identifier=backup_unique_economic_operator_identifier,
            request_options=request_options,
        )
        return _response.data



import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.vault import Vault
from .raw_client import AsyncRawVaultsClient, RawVaultsClient


class VaultsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawVaultsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawVaultsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawVaultsClient
        """
        return self._raw_client

    def get_vault(self, vault_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Vault:
        """
        Parameters
        ----------
        vault_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Vault
            The vault.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.vaults.get_vault(
            vault_id="vaultId",
        )
        """
        _response = self._raw_client.get_vault(vault_id, request_options=request_options)
        return _response.data


class AsyncVaultsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawVaultsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawVaultsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawVaultsClient
        """
        return self._raw_client

    async def get_vault(self, vault_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Vault:
        """
        Parameters
        ----------
        vault_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Vault
            The vault.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.vaults.get_vault(
                vault_id="vaultId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_vault(vault_id, request_options=request_options)
        return _response.data

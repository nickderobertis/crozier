

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.vault_response import VaultResponse
from .raw_client import AsyncRawVaultsClient, RawVaultsClient


OMIT = typing.cast(typing.Any, ...)


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

    def returns_all_available_vaults(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[VaultResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[VaultResponse]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.vaults.returns_all_available_vaults()
        """
        _response = self._raw_client.returns_all_available_vaults(request_options=request_options)
        return _response.data

    def creates_new_vault(
        self,
        *,
        name: str,
        plaintext: typing.Optional[bool] = OMIT,
        items: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Parameters
        ----------
        name : str

        plaintext : typing.Optional[bool]

        items : typing.Optional[typing.Dict[str, str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.vaults.creates_new_vault(
            name="name",
        )
        """
        _response = self._raw_client.creates_new_vault(
            name=name, plaintext=plaintext, items=items, request_options=request_options
        )
        return _response.data

    def returns_a_vault_with_given_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> VaultResponse:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VaultResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.vaults.returns_a_vault_with_given_id(
            id=1000000,
        )
        """
        _response = self._raw_client.returns_a_vault_with_given_id(id, request_options=request_options)
        return _response.data

    def updates_an_existing_vault(
        self,
        id: int,
        *,
        name: str,
        plaintext: typing.Optional[bool] = OMIT,
        items: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VaultResponse:
        """
        Parameters
        ----------
        id : int

        name : str

        plaintext : typing.Optional[bool]

        items : typing.Optional[typing.Dict[str, str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VaultResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.vaults.updates_an_existing_vault(
            id=1000000,
            name="name",
        )
        """
        _response = self._raw_client.updates_an_existing_vault(
            id, name=name, plaintext=plaintext, items=items, request_options=request_options
        )
        return _response.data

    def deletes_an_existing_vault(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.vaults.deletes_an_existing_vault(
            id=1000000,
        )
        """
        _response = self._raw_client.deletes_an_existing_vault(id, request_options=request_options)
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

    async def returns_all_available_vaults(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[VaultResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[VaultResponse]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.vaults.returns_all_available_vaults()


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_all_available_vaults(request_options=request_options)
        return _response.data

    async def creates_new_vault(
        self,
        *,
        name: str,
        plaintext: typing.Optional[bool] = OMIT,
        items: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Parameters
        ----------
        name : str

        plaintext : typing.Optional[bool]

        items : typing.Optional[typing.Dict[str, str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.vaults.creates_new_vault(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.creates_new_vault(
            name=name, plaintext=plaintext, items=items, request_options=request_options
        )
        return _response.data

    async def returns_a_vault_with_given_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> VaultResponse:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VaultResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.vaults.returns_a_vault_with_given_id(
                id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_a_vault_with_given_id(id, request_options=request_options)
        return _response.data

    async def updates_an_existing_vault(
        self,
        id: int,
        *,
        name: str,
        plaintext: typing.Optional[bool] = OMIT,
        items: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VaultResponse:
        """
        Parameters
        ----------
        id : int

        name : str

        plaintext : typing.Optional[bool]

        items : typing.Optional[typing.Dict[str, str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VaultResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.vaults.updates_an_existing_vault(
                id=1000000,
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updates_an_existing_vault(
            id, name=name, plaintext=plaintext, items=items, request_options=request_options
        )
        return _response.data

    async def deletes_an_existing_vault(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.vaults.deletes_an_existing_vault(
                id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deletes_an_existing_vault(id, request_options=request_options)
        return _response.data

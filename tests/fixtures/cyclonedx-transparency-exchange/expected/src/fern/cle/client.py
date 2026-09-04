

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.cle import Cle
from ..types.uuid_ import Uuid
from .raw_client import AsyncRawCleClient, RawCleClient


class CleClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCleClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCleClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCleClient
        """
        return self._raw_client

    def get_cle_by_product_release_id(
        self, uuid_: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Cle:
        """
        Get the CLE (Common Lifecycle Enumeration) data for a TEA Product Release

        Parameters
        ----------
        uuid_ : Uuid
            UUID of TEA Product Release in the TEA server

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Cle
            CLE data for the requested TEA Product Release found and returned

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.cle.get_cle_by_product_release_id(
            uuid_="uuid",
        )
        """
        _response = self._raw_client.get_cle_by_product_release_id(uuid_, request_options=request_options)
        return _response.data

    def get_cle_by_product_id(self, uuid_: Uuid, *, request_options: typing.Optional[RequestOptions] = None) -> Cle:
        """
        Get the CLE (Common Lifecycle Enumeration) data for a TEA Product

        Parameters
        ----------
        uuid_ : Uuid
            UUID of TEA Product in the TEA server

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Cle
            CLE data for the requested TEA Product found and returned

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.cle.get_cle_by_product_id(
            uuid_="uuid",
        )
        """
        _response = self._raw_client.get_cle_by_product_id(uuid_, request_options=request_options)
        return _response.data

    def get_cle_by_component_id(self, uuid_: Uuid, *, request_options: typing.Optional[RequestOptions] = None) -> Cle:
        """
        Get the CLE (Common Lifecycle Enumeration) data for a TEA Component

        Parameters
        ----------
        uuid_ : Uuid
            UUID of TEA Component in the TEA server

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Cle
            CLE data for the requested TEA Component found and returned

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.cle.get_cle_by_component_id(
            uuid_="uuid",
        )
        """
        _response = self._raw_client.get_cle_by_component_id(uuid_, request_options=request_options)
        return _response.data

    def get_cle_by_component_release_id(
        self, uuid_: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Cle:
        """
        Get the CLE (Common Lifecycle Enumeration) data for a TEA Component Release

        Parameters
        ----------
        uuid_ : Uuid
            UUID of TEA Component Release in the TEA server

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Cle
            CLE data for the requested TEA Component Release found and returned

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.cle.get_cle_by_component_release_id(
            uuid_="uuid",
        )
        """
        _response = self._raw_client.get_cle_by_component_release_id(uuid_, request_options=request_options)
        return _response.data


class AsyncCleClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCleClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCleClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCleClient
        """
        return self._raw_client

    async def get_cle_by_product_release_id(
        self, uuid_: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Cle:
        """
        Get the CLE (Common Lifecycle Enumeration) data for a TEA Product Release

        Parameters
        ----------
        uuid_ : Uuid
            UUID of TEA Product Release in the TEA server

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Cle
            CLE data for the requested TEA Product Release found and returned

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.cle.get_cle_by_product_release_id(
                uuid_="uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_cle_by_product_release_id(uuid_, request_options=request_options)
        return _response.data

    async def get_cle_by_product_id(
        self, uuid_: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Cle:
        """
        Get the CLE (Common Lifecycle Enumeration) data for a TEA Product

        Parameters
        ----------
        uuid_ : Uuid
            UUID of TEA Product in the TEA server

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Cle
            CLE data for the requested TEA Product found and returned

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.cle.get_cle_by_product_id(
                uuid_="uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_cle_by_product_id(uuid_, request_options=request_options)
        return _response.data

    async def get_cle_by_component_id(
        self, uuid_: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Cle:
        """
        Get the CLE (Common Lifecycle Enumeration) data for a TEA Component

        Parameters
        ----------
        uuid_ : Uuid
            UUID of TEA Component in the TEA server

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Cle
            CLE data for the requested TEA Component found and returned

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.cle.get_cle_by_component_id(
                uuid_="uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_cle_by_component_id(uuid_, request_options=request_options)
        return _response.data

    async def get_cle_by_component_release_id(
        self, uuid_: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Cle:
        """
        Get the CLE (Common Lifecycle Enumeration) data for a TEA Component Release

        Parameters
        ----------
        uuid_ : Uuid
            UUID of TEA Component Release in the TEA server

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Cle
            CLE data for the requested TEA Component Release found and returned

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.cle.get_cle_by_component_release_id(
                uuid_="uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_cle_by_component_release_id(uuid_, request_options=request_options)
        return _response.data

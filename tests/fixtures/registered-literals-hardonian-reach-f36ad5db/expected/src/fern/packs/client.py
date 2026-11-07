

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.install_pack_response import InstallPackResponse
from ..types.packs_response import PacksResponse
from ..types.verification_result import VerificationResult
from .raw_client import AsyncRawPacksClient, RawPacksClient


OMIT = typing.cast(typing.Any, ...)


class PacksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPacksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPacksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPacksClient
        """
        return self._raw_client

    def list_packs(
        self, *, q: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> PacksResponse:
        """
        Search and list available execution packs in the registry

        Parameters
        ----------
        q : typing.Optional[str]
            Search query string

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PacksResponse
            List of packs

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.packs.list_packs()
        """
        _response = self._raw_client.list_packs(q=q, request_options=request_options)
        return _response.data

    def install_pack(
        self, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> InstallPackResponse:
        """
        Install a pack from the registry

        Parameters
        ----------
        name : str
            Name of the pack to install

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InstallPackResponse
            Pack installed successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.packs.install_pack(
            name="name",
        )
        """
        _response = self._raw_client.install_pack(name=name, request_options=request_options)
        return _response.data

    def verify_pack(self, *, name: str, request_options: typing.Optional[RequestOptions] = None) -> VerificationResult:
        """
        Verify pack signature and compatibility

        Parameters
        ----------
        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VerificationResult
            Verification result

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.packs.verify_pack(
            name="name",
        )
        """
        _response = self._raw_client.verify_pack(name=name, request_options=request_options)
        return _response.data


class AsyncPacksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPacksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPacksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPacksClient
        """
        return self._raw_client

    async def list_packs(
        self, *, q: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> PacksResponse:
        """
        Search and list available execution packs in the registry

        Parameters
        ----------
        q : typing.Optional[str]
            Search query string

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PacksResponse
            List of packs

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.packs.list_packs()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_packs(q=q, request_options=request_options)
        return _response.data

    async def install_pack(
        self, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> InstallPackResponse:
        """
        Install a pack from the registry

        Parameters
        ----------
        name : str
            Name of the pack to install

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InstallPackResponse
            Pack installed successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.packs.install_pack(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.install_pack(name=name, request_options=request_options)
        return _response.data

    async def verify_pack(
        self, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> VerificationResult:
        """
        Verify pack signature and compatibility

        Parameters
        ----------
        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VerificationResult
            Verification result

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.packs.verify_pack(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.verify_pack(name=name, request_options=request_options)
        return _response.data

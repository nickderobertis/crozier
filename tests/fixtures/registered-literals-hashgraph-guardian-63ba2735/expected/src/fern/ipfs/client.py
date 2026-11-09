

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawIpfsClient, RawIpfsClient


class IpfsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawIpfsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawIpfsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawIpfsClient
        """
        return self._raw_client

    def ipfs_api_post_file(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Add file from ipfs.

        Parameters
        ----------
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
        client.ipfs.ipfs_api_post_file()
        """
        _response = self._raw_client.ipfs_api_post_file(request_options=request_options)
        return _response.data

    def ipfs_api_post_file_dry_run(
        self, policy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Add file from ipfs for dry run mode.

        Parameters
        ----------
        policy_id : str
            Policy identifier

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
        client.ipfs.ipfs_api_post_file_dry_run(
            policy_id="652745597a7b53526de37c05",
        )
        """
        _response = self._raw_client.ipfs_api_post_file_dry_run(policy_id, request_options=request_options)
        return _response.data

    def get_file_from_ipfs(
        self, cid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Get file from ipfs.

        Parameters
        ----------
        cid : str
            File CID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Created.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.ipfs.get_file_from_ipfs(
            cid="cid",
        )
        """
        with self._raw_client.get_file_from_ipfs(cid, request_options=request_options) as r:
            yield from r.data

    def ipfs_api_get_file_dry_run(self, cid: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get file from ipfs for dry run mode.

        Parameters
        ----------
        cid : str

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
        client.ipfs.ipfs_api_get_file_dry_run(
            cid="cid",
        )
        """
        _response = self._raw_client.ipfs_api_get_file_dry_run(cid, request_options=request_options)
        return _response.data

    def add_file_to_ipfs(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Add file to ipfs.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Created.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.ipfs.add_file_to_ipfs()
        """
        _response = self._raw_client.add_file_to_ipfs(request_options=request_options)
        return _response.data


class AsyncIpfsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawIpfsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawIpfsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawIpfsClient
        """
        return self._raw_client

    async def ipfs_api_post_file(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Add file from ipfs.

        Parameters
        ----------
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
            await client.ipfs.ipfs_api_post_file()


        asyncio.run(main())
        """
        _response = await self._raw_client.ipfs_api_post_file(request_options=request_options)
        return _response.data

    async def ipfs_api_post_file_dry_run(
        self, policy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Add file from ipfs for dry run mode.

        Parameters
        ----------
        policy_id : str
            Policy identifier

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
            await client.ipfs.ipfs_api_post_file_dry_run(
                policy_id="652745597a7b53526de37c05",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ipfs_api_post_file_dry_run(policy_id, request_options=request_options)
        return _response.data

    async def get_file_from_ipfs(
        self, cid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Get file from ipfs.

        Parameters
        ----------
        cid : str
            File CID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Created.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ipfs.get_file_from_ipfs(
                cid="cid",
            )


        asyncio.run(main())
        """
        async with self._raw_client.get_file_from_ipfs(cid, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def ipfs_api_get_file_dry_run(
        self, cid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Get file from ipfs for dry run mode.

        Parameters
        ----------
        cid : str

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
            await client.ipfs.ipfs_api_get_file_dry_run(
                cid="cid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ipfs_api_get_file_dry_run(cid, request_options=request_options)
        return _response.data

    async def add_file_to_ipfs(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Add file to ipfs.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Created.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ipfs.add_file_to_ipfs()


        asyncio.run(main())
        """
        _response = await self._raw_client.add_file_to_ipfs(request_options=request_options)
        return _response.data

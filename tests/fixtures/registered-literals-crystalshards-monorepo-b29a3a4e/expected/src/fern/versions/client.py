

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawVersionsClient, RawVersionsClient
from .types.get_api_shards_host_owner_repo_version_response import GetApiShardsHostOwnerRepoVersionResponse
from .types.get_api_shards_host_owner_repo_versions_response import GetApiShardsHostOwnerRepoVersionsResponse


class VersionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawVersionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawVersionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawVersionsClient
        """
        return self._raw_client

    def list_shard_versions(
        self, host: str, owner: str, repo: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetApiShardsHostOwnerRepoVersionsResponse:
        """
        Get all versions of a specific shard

        Parameters
        ----------
        host : str
            Repository host

        owner : str
            Owner or organisation on that host

        repo : str
            Repository name on that host

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetApiShardsHostOwnerRepoVersionsResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.versions.list_shard_versions(
            host="github.com",
            owner="kemalcr",
            repo="kemal",
        )
        """
        _response = self._raw_client.list_shard_versions(host, owner, repo, request_options=request_options)
        return _response.data

    def get_specific_version(
        self, host: str, owner: str, repo: str, version: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetApiShardsHostOwnerRepoVersionResponse:
        """
        Get detailed information about a specific version of a shard

        Parameters
        ----------
        host : str
            Repository host

        owner : str
            Owner or organisation on that host

        repo : str
            Repository name on that host

        version : str
            Version string (e.g., 1.0.0)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetApiShardsHostOwnerRepoVersionResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.versions.get_specific_version(
            host="github.com",
            owner="kemalcr",
            repo="kemal",
            version="version",
        )
        """
        _response = self._raw_client.get_specific_version(host, owner, repo, version, request_options=request_options)
        return _response.data


class AsyncVersionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawVersionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawVersionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawVersionsClient
        """
        return self._raw_client

    async def list_shard_versions(
        self, host: str, owner: str, repo: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetApiShardsHostOwnerRepoVersionsResponse:
        """
        Get all versions of a specific shard

        Parameters
        ----------
        host : str
            Repository host

        owner : str
            Owner or organisation on that host

        repo : str
            Repository name on that host

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetApiShardsHostOwnerRepoVersionsResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.versions.list_shard_versions(
                host="github.com",
                owner="kemalcr",
                repo="kemal",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_shard_versions(host, owner, repo, request_options=request_options)
        return _response.data

    async def get_specific_version(
        self, host: str, owner: str, repo: str, version: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetApiShardsHostOwnerRepoVersionResponse:
        """
        Get detailed information about a specific version of a shard

        Parameters
        ----------
        host : str
            Repository host

        owner : str
            Owner or organisation on that host

        repo : str
            Repository name on that host

        version : str
            Version string (e.g., 1.0.0)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetApiShardsHostOwnerRepoVersionResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.versions.get_specific_version(
                host="github.com",
                owner="kemalcr",
                repo="kemal",
                version="version",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_specific_version(
            host, owner, repo, version, request_options=request_options
        )
        return _response.data

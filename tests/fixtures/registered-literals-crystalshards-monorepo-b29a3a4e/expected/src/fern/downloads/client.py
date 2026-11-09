

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawDownloadsClient, RawDownloadsClient
from .types.post_api_shards_host_owner_repo_version_download_response import (
    PostApiShardsHostOwnerRepoVersionDownloadResponse,
)


class DownloadsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDownloadsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDownloadsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDownloadsClient
        """
        return self._raw_client

    def track_download(
        self, host: str, owner: str, repo: str, version: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PostApiShardsHostOwnerRepoVersionDownloadResponse:
        """
        Record a download of a specific shard version. Downloads are attributed
        to the repository, never to a name, so this endpoint takes the identity
        only.

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
        PostApiShardsHostOwnerRepoVersionDownloadResponse
            Download tracked successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.downloads.track_download(
            host="github.com",
            owner="kemalcr",
            repo="kemal",
            version="version",
        )
        """
        _response = self._raw_client.track_download(host, owner, repo, version, request_options=request_options)
        return _response.data


class AsyncDownloadsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDownloadsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDownloadsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDownloadsClient
        """
        return self._raw_client

    async def track_download(
        self, host: str, owner: str, repo: str, version: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PostApiShardsHostOwnerRepoVersionDownloadResponse:
        """
        Record a download of a specific shard version. Downloads are attributed
        to the repository, never to a name, so this endpoint takes the identity
        only.

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
        PostApiShardsHostOwnerRepoVersionDownloadResponse
            Download tracked successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.downloads.track_download(
                host="github.com",
                owner="kemalcr",
                repo="kemal",
                version="version",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.track_download(host, owner, repo, version, request_options=request_options)
        return _response.data

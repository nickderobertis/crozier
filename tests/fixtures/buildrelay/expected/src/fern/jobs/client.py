

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.job_response import JobResponse
from .raw_client import AsyncRawJobsClient, RawJobsClient


OMIT = typing.cast(typing.Any, ...)


class JobsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawJobsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawJobsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawJobsClient
        """
        return self._raw_client

    def submit_filesystem_job(
        self,
        *,
        project: str,
        platform: str,
        ingest_path: str,
        description: typing.Optional[str] = OMIT,
        steam_channel_labels: typing.Optional[typing.Sequence[str]] = OMIT,
        cdn_channel_labels: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JobResponse:
        """
        Submit a build job from files on the filesystem to be uploaded to configured channels

        Parameters
        ----------
        project : str
            Name of the project being built

        platform : str
            Target platform (e.g., windows, linux, macos)

        ingest_path : str
            Relative path within /builds directory containing build files. Cannot be absolute or contain '..'

        description : typing.Optional[str]
            Description of the build (e.g., version number)

        steam_channel_labels : typing.Optional[typing.Sequence[str]]
            Labels of Steam channels to upload to

        cdn_channel_labels : typing.Optional[typing.Sequence[str]]
            Labels of CDN channels to upload to

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobResponse
            Job successfully created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.jobs.submit_filesystem_job(
            project="Test Project",
            platform="windows",
            ingest_path="build",
            cdn_channel_labels=["CDN Label"],
        )
        """
        _response = self._raw_client.submit_filesystem_job(
            project=project,
            platform=platform,
            ingest_path=ingest_path,
            description=description,
            steam_channel_labels=steam_channel_labels,
            cdn_channel_labels=cdn_channel_labels,
            request_options=request_options,
        )
        return _response.data


class AsyncJobsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawJobsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawJobsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawJobsClient
        """
        return self._raw_client

    async def submit_filesystem_job(
        self,
        *,
        project: str,
        platform: str,
        ingest_path: str,
        description: typing.Optional[str] = OMIT,
        steam_channel_labels: typing.Optional[typing.Sequence[str]] = OMIT,
        cdn_channel_labels: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JobResponse:
        """
        Submit a build job from files on the filesystem to be uploaded to configured channels

        Parameters
        ----------
        project : str
            Name of the project being built

        platform : str
            Target platform (e.g., windows, linux, macos)

        ingest_path : str
            Relative path within /builds directory containing build files. Cannot be absolute or contain '..'

        description : typing.Optional[str]
            Description of the build (e.g., version number)

        steam_channel_labels : typing.Optional[typing.Sequence[str]]
            Labels of Steam channels to upload to

        cdn_channel_labels : typing.Optional[typing.Sequence[str]]
            Labels of CDN channels to upload to

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobResponse
            Job successfully created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.jobs.submit_filesystem_job(
                project="Test Project",
                platform="windows",
                ingest_path="build",
                cdn_channel_labels=["CDN Label"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.submit_filesystem_job(
            project=project,
            platform=platform,
            ingest_path=ingest_path,
            description=description,
            steam_channel_labels=steam_channel_labels,
            cdn_channel_labels=cdn_channel_labels,
            request_options=request_options,
        )
        return _response.data



import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.artifact_response import ArtifactResponse
from .raw_client import AsyncRawArtifactsClient, RawArtifactsClient


class ArtifactsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawArtifactsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawArtifactsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawArtifactsClient
        """
        return self._raw_client

    def get_artifact(
        self, artifact_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ArtifactResponse:
        """
        Parameters
        ----------
        artifact_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ArtifactResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.artifacts.get_artifact(
            artifact_id="artifact_id",
        )
        """
        _response = self._raw_client.get_artifact(artifact_id, request_options=request_options)
        return _response.data

    def download_artifact(self, artifact_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        artifact_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.artifacts.download_artifact(
            artifact_id="artifact_id",
        )
        """
        _response = self._raw_client.download_artifact(artifact_id, request_options=request_options)
        return _response.data


class AsyncArtifactsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawArtifactsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawArtifactsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawArtifactsClient
        """
        return self._raw_client

    async def get_artifact(
        self, artifact_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ArtifactResponse:
        """
        Parameters
        ----------
        artifact_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ArtifactResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.artifacts.get_artifact(
                artifact_id="artifact_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_artifact(artifact_id, request_options=request_options)
        return _response.data

    async def download_artifact(
        self, artifact_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        artifact_id : str

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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.artifacts.download_artifact(
                artifact_id="artifact_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.download_artifact(artifact_id, request_options=request_options)
        return _response.data

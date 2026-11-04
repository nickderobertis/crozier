

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
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

    def get_artifact_content(
        self, artifact_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Download the raw content of an artifact (supports bundled artifacts).

        Parameters
        ----------
        artifact_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Raw artifact content

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.artifacts.get_artifact_content(
            artifact_id="artifact_id",
        )
        """
        _response = self._raw_client.get_artifact_content(artifact_id, request_options=request_options)
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

    async def get_artifact_content(
        self, artifact_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Download the raw content of an artifact (supports bundled artifacts).

        Parameters
        ----------
        artifact_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Raw artifact content

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.artifacts.get_artifact_content(
                artifact_id="artifact_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_artifact_content(artifact_id, request_options=request_options)
        return _response.data



import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.artifact import Artifact
from ..types.uuid_ import Uuid
from .raw_client import AsyncRawTeaArtifactClient, RawTeaArtifactClient


class TeaArtifactClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTeaArtifactClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTeaArtifactClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTeaArtifactClient
        """
        return self._raw_client

    def get_latest_artifact(self, uuid_: Uuid, *, request_options: typing.Optional[RequestOptions] = None) -> Artifact:
        """
        Get metadata for latest revision of a specific TEA Artifact

        Parameters
        ----------
        uuid_ : Uuid
            UUID of TEA Artifact in the TEA server

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Artifact
            Requested TEA Artifact metadata found and returned

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tea_artifact.get_latest_artifact(
            uuid_="uuid",
        )
        """
        _response = self._raw_client.get_latest_artifact(uuid_, request_options=request_options)
        return _response.data

    def get_artifact_by_version(
        self, uuid_: Uuid, artifact_version: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Artifact:
        """
        Get metadata for a specific revision of a specific TEA Artifact

        Parameters
        ----------
        uuid_ : Uuid
            UUID of TEA Artifact in the TEA server

        artifact_version : int
            Version of TEA Artifact

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Artifact
            Requested TEA Artifact metadata found and returned

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tea_artifact.get_artifact_by_version(
            uuid_="uuid",
            artifact_version=1,
        )
        """
        _response = self._raw_client.get_artifact_by_version(uuid_, artifact_version, request_options=request_options)
        return _response.data


class AsyncTeaArtifactClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTeaArtifactClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTeaArtifactClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTeaArtifactClient
        """
        return self._raw_client

    async def get_latest_artifact(
        self, uuid_: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Artifact:
        """
        Get metadata for latest revision of a specific TEA Artifact

        Parameters
        ----------
        uuid_ : Uuid
            UUID of TEA Artifact in the TEA server

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Artifact
            Requested TEA Artifact metadata found and returned

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tea_artifact.get_latest_artifact(
                uuid_="uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_latest_artifact(uuid_, request_options=request_options)
        return _response.data

    async def get_artifact_by_version(
        self, uuid_: Uuid, artifact_version: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Artifact:
        """
        Get metadata for a specific revision of a specific TEA Artifact

        Parameters
        ----------
        uuid_ : Uuid
            UUID of TEA Artifact in the TEA server

        artifact_version : int
            Version of TEA Artifact

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Artifact
            Requested TEA Artifact metadata found and returned

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tea_artifact.get_artifact_by_version(
                uuid_="uuid",
                artifact_version=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_artifact_by_version(
            uuid_, artifact_version, request_options=request_options
        )
        return _response.data

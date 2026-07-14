

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.artifact_type_info import ArtifactTypeInfo
from .raw_client import AsyncRawArtifactTypeClient, RawArtifactTypeClient


class ArtifactTypeClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawArtifactTypeClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawArtifactTypeClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawArtifactTypeClient
        """
        return self._raw_client

    def list_artifact_types(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ArtifactTypeInfo]:
        """
        Gets a list of all the configured artifact types.

        This operation can fail for the following reasons:

        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ArtifactTypeInfo]
            The list of available artifact types.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.artifact_type.list_artifact_types()
        """
        _response = self._raw_client.list_artifact_types(request_options=request_options)
        return _response.data


class AsyncArtifactTypeClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawArtifactTypeClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawArtifactTypeClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawArtifactTypeClient
        """
        return self._raw_client

    async def list_artifact_types(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ArtifactTypeInfo]:
        """
        Gets a list of all the configured artifact types.

        This operation can fail for the following reasons:

        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ArtifactTypeInfo]
            The list of available artifact types.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.artifact_type.list_artifact_types()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_artifact_types(request_options=request_options)
        return _response.data

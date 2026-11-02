

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawManifestsClient, RawManifestsClient
from .types.import_manifest_request_task import ImportManifestRequestTask
from .types.import_manifest_response import ImportManifestResponse


OMIT = typing.cast(typing.Any, ...)


class ManifestsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawManifestsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawManifestsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawManifestsClient
        """
        return self._raw_client

    def import_manifest(
        self,
        *,
        sheet: core.File,
        task: ImportManifestRequestTask,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ImportManifestResponse:
        """
        A multipart object part whose property declares an example.

        Parameters
        ----------
        sheet : core.File
            See core.File for more documentation

        task : ImportManifestRequestTask

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImportManifestResponse
            Imported

        Examples
        --------
        from fern.manifests import ImportManifestRequestTask

        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.manifests.import_manifest(
            task=ImportManifestRequestTask(
                label="label",
            ),
        )
        """
        _response = self._raw_client.import_manifest(sheet=sheet, task=task, request_options=request_options)
        return _response.data


class AsyncManifestsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawManifestsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawManifestsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawManifestsClient
        """
        return self._raw_client

    async def import_manifest(
        self,
        *,
        sheet: core.File,
        task: ImportManifestRequestTask,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ImportManifestResponse:
        """
        A multipart object part whose property declares an example.

        Parameters
        ----------
        sheet : core.File
            See core.File for more documentation

        task : ImportManifestRequestTask

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImportManifestResponse
            Imported

        Examples
        --------
        import asyncio

        from fern.manifests import ImportManifestRequestTask

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.manifests.import_manifest(
                task=ImportManifestRequestTask(
                    label="label",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.import_manifest(sheet=sheet, task=task, request_options=request_options)
        return _response.data



import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.core_whats_new_dismiss200response import CoreWhatsNewDismiss200Response
from ..types.files_sharing_deleted_shareapi_list200response import FilesSharingDeletedShareapiList200Response
from .raw_client import AsyncRawFilesSharingDeletedShareapiClient, RawFilesSharingDeletedShareapiClient


class FilesSharingDeletedShareapiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFilesSharingDeletedShareapiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFilesSharingDeletedShareapiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFilesSharingDeletedShareapiClient
        """
        return self._raw_client

    def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FilesSharingDeletedShareapiList200Response:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilesSharingDeletedShareapiList200Response


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.files_sharing_deleted_shareapi.list()
        """
        _response = self._raw_client.list(request_options=request_options)
        return _response.data

    def undelete(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreWhatsNewDismiss200Response:
        """
        Parameters
        ----------
        id : str
            ID of the share

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreWhatsNewDismiss200Response
            Share undeleted successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.files_sharing_deleted_shareapi.undelete(
            id="id",
        )
        """
        _response = self._raw_client.undelete(id, request_options=request_options)
        return _response.data


class AsyncFilesSharingDeletedShareapiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFilesSharingDeletedShareapiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFilesSharingDeletedShareapiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFilesSharingDeletedShareapiClient
        """
        return self._raw_client

    async def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FilesSharingDeletedShareapiList200Response:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilesSharingDeletedShareapiList200Response


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.files_sharing_deleted_shareapi.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(request_options=request_options)
        return _response.data

    async def undelete(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreWhatsNewDismiss200Response:
        """
        Parameters
        ----------
        id : str
            ID of the share

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreWhatsNewDismiss200Response
            Share undeleted successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.files_sharing_deleted_shareapi.undelete(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.undelete(id, request_options=request_options)
        return _response.data

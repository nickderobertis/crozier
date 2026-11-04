

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.core_whats_new_dismiss200response import CoreWhatsNewDismiss200Response
from ..types.files_sharing_remote_get_share200response import FilesSharingRemoteGetShare200Response
from ..types.files_sharing_remote_get_shares200response import FilesSharingRemoteGetShares200Response
from .raw_client import AsyncRawFilesSharingRemoteClient, RawFilesSharingRemoteClient


class FilesSharingRemoteClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFilesSharingRemoteClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFilesSharingRemoteClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFilesSharingRemoteClient
        """
        return self._raw_client

    def get_shares(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FilesSharingRemoteGetShares200Response:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilesSharingRemoteGetShares200Response


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.files_sharing_remote.get_shares()
        """
        _response = self._raw_client.get_shares(request_options=request_options)
        return _response.data

    def get_open_shares(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FilesSharingRemoteGetShares200Response:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilesSharingRemoteGetShares200Response


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.files_sharing_remote.get_open_shares()
        """
        _response = self._raw_client.get_open_shares(request_options=request_options)
        return _response.data

    def accept_share(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreWhatsNewDismiss200Response:
        """
        Parameters
        ----------
        id : int
            ID of the share

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreWhatsNewDismiss200Response
            Share accepted successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.files_sharing_remote.accept_share(
            id=1000000,
        )
        """
        _response = self._raw_client.accept_share(id, request_options=request_options)
        return _response.data

    def decline_share(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreWhatsNewDismiss200Response:
        """
        Parameters
        ----------
        id : int
            ID of the share

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreWhatsNewDismiss200Response
            Share declined successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.files_sharing_remote.decline_share(
            id=1000000,
        )
        """
        _response = self._raw_client.decline_share(id, request_options=request_options)
        return _response.data

    def get_share(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FilesSharingRemoteGetShare200Response:
        """
        Parameters
        ----------
        id : int
            ID of the share

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilesSharingRemoteGetShare200Response
            Share returned

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.files_sharing_remote.get_share(
            id=1000000,
        )
        """
        _response = self._raw_client.get_share(id, request_options=request_options)
        return _response.data

    def unshare(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreWhatsNewDismiss200Response:
        """
        Parameters
        ----------
        id : int
            ID of the share

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreWhatsNewDismiss200Response
            Share unshared successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.files_sharing_remote.unshare(
            id=1000000,
        )
        """
        _response = self._raw_client.unshare(id, request_options=request_options)
        return _response.data


class AsyncFilesSharingRemoteClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFilesSharingRemoteClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFilesSharingRemoteClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFilesSharingRemoteClient
        """
        return self._raw_client

    async def get_shares(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FilesSharingRemoteGetShares200Response:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilesSharingRemoteGetShares200Response


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
            await client.files_sharing_remote.get_shares()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_shares(request_options=request_options)
        return _response.data

    async def get_open_shares(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FilesSharingRemoteGetShares200Response:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilesSharingRemoteGetShares200Response


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
            await client.files_sharing_remote.get_open_shares()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_open_shares(request_options=request_options)
        return _response.data

    async def accept_share(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreWhatsNewDismiss200Response:
        """
        Parameters
        ----------
        id : int
            ID of the share

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreWhatsNewDismiss200Response
            Share accepted successfully

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
            await client.files_sharing_remote.accept_share(
                id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.accept_share(id, request_options=request_options)
        return _response.data

    async def decline_share(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreWhatsNewDismiss200Response:
        """
        Parameters
        ----------
        id : int
            ID of the share

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreWhatsNewDismiss200Response
            Share declined successfully

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
            await client.files_sharing_remote.decline_share(
                id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.decline_share(id, request_options=request_options)
        return _response.data

    async def get_share(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FilesSharingRemoteGetShare200Response:
        """
        Parameters
        ----------
        id : int
            ID of the share

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilesSharingRemoteGetShare200Response
            Share returned

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
            await client.files_sharing_remote.get_share(
                id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_share(id, request_options=request_options)
        return _response.data

    async def unshare(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreWhatsNewDismiss200Response:
        """
        Parameters
        ----------
        id : int
            ID of the share

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreWhatsNewDismiss200Response
            Share unshared successfully

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
            await client.files_sharing_remote.unshare(
                id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.unshare(id, request_options=request_options)
        return _response.data

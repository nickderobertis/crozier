

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawBackupsClient, RawBackupsClient
from .types.create_backup_response import CreateBackupResponse
from .types.get_backups_response_item import GetBackupsResponseItem


OMIT = typing.cast(typing.Any, ...)


class BackupsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBackupsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBackupsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBackupsClient
        """
        return self._raw_client

    def get_backups(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GetBackupsResponseItem]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GetBackupsResponseItem]
            success response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.backups.get_backups()
        """
        _response = self._raw_client.get_backups(request_options=request_options)
        return _response.data

    def create_backup(
        self, *, with_uploads: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> CreateBackupResponse:
        """
        Parameters
        ----------
        with_uploads : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateBackupResponse
            success response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.backups.create_backup(
            with_uploads=True,
        )
        """
        _response = self._raw_client.create_backup(with_uploads=with_uploads, request_options=request_options)
        return _response.data

    def download_backup(
        self, filename: str, *, token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        filename : str

        token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.backups.download_backup(
            filename="filename",
            token="token",
        )
        """
        _response = self._raw_client.download_backup(filename, token=token, request_options=request_options)
        return _response.data

    def send_download_backup_email(
        self, filename: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        filename : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.backups.send_download_backup_email(
            filename="filename",
        )
        """
        _response = self._raw_client.send_download_backup_email(filename, request_options=request_options)
        return _response.data


class AsyncBackupsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBackupsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBackupsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBackupsClient
        """
        return self._raw_client

    async def get_backups(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GetBackupsResponseItem]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GetBackupsResponseItem]
            success response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.backups.get_backups()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_backups(request_options=request_options)
        return _response.data

    async def create_backup(
        self, *, with_uploads: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> CreateBackupResponse:
        """
        Parameters
        ----------
        with_uploads : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateBackupResponse
            success response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.backups.create_backup(
                with_uploads=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_backup(with_uploads=with_uploads, request_options=request_options)
        return _response.data

    async def download_backup(
        self, filename: str, *, token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        filename : str

        token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.backups.download_backup(
                filename="filename",
                token="token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.download_backup(filename, token=token, request_options=request_options)
        return _response.data

    async def send_download_backup_email(
        self, filename: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        filename : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.backups.send_download_backup_email(
                filename="filename",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.send_download_backup_email(filename, request_options=request_options)
        return _response.data

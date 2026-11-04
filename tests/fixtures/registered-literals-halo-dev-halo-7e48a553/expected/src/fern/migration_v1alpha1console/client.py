

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.backup_file import BackupFile
from .raw_client import AsyncRawMigrationV1Alpha1ConsoleClient, RawMigrationV1Alpha1ConsoleClient


OMIT = typing.cast(typing.Any, ...)


class MigrationV1Alpha1ConsoleClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMigrationV1Alpha1ConsoleClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMigrationV1Alpha1ConsoleClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMigrationV1Alpha1ConsoleClient
        """
        return self._raw_client

    def get_backup_files(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[BackupFile]:
        """
        Get backup files from backup root.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[BackupFile]
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.migration_v1alpha1console.get_backup_files()
        """
        _response = self._raw_client.get_backup_files(request_options=request_options)
        return _response.data

    def download_backups(
        self, name: str, filename: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Download a file from the specified backup as an octet-stream attachment.

        Parameters
        ----------
        name : str
            Backup metadata.name.

        filename : str
            Backup filename.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.migration_v1alpha1console.download_backups(
            name="name",
            filename="filename",
        )
        """
        _response = self._raw_client.download_backups(name, filename, request_options=request_options)
        return _response.data

    def restore_backup(
        self,
        *,
        backup_name: typing.Optional[str] = OMIT,
        download_url: typing.Optional[str] = OMIT,
        file: typing.Optional[core.File] = OMIT,
        filename: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Restore backup by uploading file or providing download link or backup name.

        Parameters
        ----------
        backup_name : typing.Optional[str]
            Backup <code>metadata.name</code>.

        download_url : typing.Optional[str]
            Remote backup HTTP URL.

        file : typing.Optional[core.File]
            See core.File for more documentation

        filename : typing.Optional[str]
            Filename of backup file in backups root.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Backup restored successfully.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.migration_v1alpha1console.restore_backup()
        """
        _response = self._raw_client.restore_backup(
            backup_name=backup_name,
            download_url=download_url,
            file=file,
            filename=filename,
            request_options=request_options,
        )
        return _response.data


class AsyncMigrationV1Alpha1ConsoleClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMigrationV1Alpha1ConsoleClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMigrationV1Alpha1ConsoleClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMigrationV1Alpha1ConsoleClient
        """
        return self._raw_client

    async def get_backup_files(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[BackupFile]:
        """
        Get backup files from backup root.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[BackupFile]
            default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.migration_v1alpha1console.get_backup_files()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_backup_files(request_options=request_options)
        return _response.data

    async def download_backups(
        self, name: str, filename: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Download a file from the specified backup as an octet-stream attachment.

        Parameters
        ----------
        name : str
            Backup metadata.name.

        filename : str
            Backup filename.

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
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.migration_v1alpha1console.download_backups(
                name="name",
                filename="filename",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.download_backups(name, filename, request_options=request_options)
        return _response.data

    async def restore_backup(
        self,
        *,
        backup_name: typing.Optional[str] = OMIT,
        download_url: typing.Optional[str] = OMIT,
        file: typing.Optional[core.File] = OMIT,
        filename: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Restore backup by uploading file or providing download link or backup name.

        Parameters
        ----------
        backup_name : typing.Optional[str]
            Backup <code>metadata.name</code>.

        download_url : typing.Optional[str]
            Remote backup HTTP URL.

        file : typing.Optional[core.File]
            See core.File for more documentation

        filename : typing.Optional[str]
            Filename of backup file in backups root.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Backup restored successfully.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.migration_v1alpha1console.restore_backup()


        asyncio.run(main())
        """
        _response = await self._raw_client.restore_backup(
            backup_name=backup_name,
            download_url=download_url,
            file=file,
            filename=filename,
            request_options=request_options,
        )
        return _response.data

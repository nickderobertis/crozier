

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_response import ApiResponse
from ..types.base_virtual_folder import BaseVirtualFolder
from ..types.filesystem_config import FilesystemConfig
from .raw_client import AsyncRawFoldersClient, RawFoldersClient
from .types.get_folders_request_order import GetFoldersRequestOrder


OMIT = typing.cast(typing.Any, ...)


class FoldersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFoldersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFoldersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFoldersClient
        """
        return self._raw_client

    def get_folders(
        self,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[GetFoldersRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[BaseVirtualFolder]:
        """
        Returns an array with one or more folders

        Parameters
        ----------
        offset : typing.Optional[int]

        limit : typing.Optional[int]
            The maximum number of items to return. Max value is 500, default is 100

        order : typing.Optional[GetFoldersRequestOrder]
            Ordering folders by name. Default ASC

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[BaseVirtualFolder]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.folders.get_folders()
        """
        _response = self._raw_client.get_folders(
            offset=offset, limit=limit, order=order, request_options=request_options
        )
        return _response.data

    def add_folder(
        self,
        *,
        confidential_data: typing.Optional[int] = None,
        id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        mapped_path: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        used_quota_size: typing.Optional[int] = OMIT,
        used_quota_files: typing.Optional[int] = OMIT,
        last_quota_update: typing.Optional[int] = OMIT,
        users: typing.Optional[typing.Sequence[str]] = OMIT,
        filesystem: typing.Optional[FilesystemConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BaseVirtualFolder:
        """
        Adds a new folder. A quota scan is required to update the used files/size

        Parameters
        ----------
        confidential_data : typing.Optional[int]
            If set to 1 confidential data will not be hidden. This means that the response will contain the key and additional data for secrets. If a master key is not set or an external KMS is used, the data returned are enough to get the secrets in cleartext. Ignored if the * permission is not granted.

        id : typing.Optional[int]

        name : typing.Optional[str]
            unique name for this virtual folder

        mapped_path : typing.Optional[str]
            absolute filesystem path to use as virtual folder

        description : typing.Optional[str]
            optional description

        used_quota_size : typing.Optional[int]

        used_quota_files : typing.Optional[int]

        last_quota_update : typing.Optional[int]
            Last quota update as unix timestamp in milliseconds

        users : typing.Optional[typing.Sequence[str]]
            list of usernames associated with this virtual folder

        filesystem : typing.Optional[FilesystemConfig]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BaseVirtualFolder
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.folders.add_folder()
        """
        _response = self._raw_client.add_folder(
            confidential_data=confidential_data,
            id=id,
            name=name,
            mapped_path=mapped_path,
            description=description,
            used_quota_size=used_quota_size,
            used_quota_files=used_quota_files,
            last_quota_update=last_quota_update,
            users=users,
            filesystem=filesystem,
            request_options=request_options,
        )
        return _response.data

    def get_folder_by_name(
        self,
        name: str,
        *,
        confidential_data: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BaseVirtualFolder:
        """
        Returns the folder with the given name if it exists.

        Parameters
        ----------
        name : str
            folder name

        confidential_data : typing.Optional[int]
            If set to 1 confidential data will not be hidden. This means that the response will contain the key and additional data for secrets. If a master key is not set or an external KMS is used, the data returned are enough to get the secrets in cleartext. Ignored if the * permission is not granted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BaseVirtualFolder
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.folders.get_folder_by_name(
            name="name",
        )
        """
        _response = self._raw_client.get_folder_by_name(
            name, confidential_data=confidential_data, request_options=request_options
        )
        return _response.data

    def update_folder(
        self,
        name_: str,
        *,
        id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        mapped_path: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        used_quota_size: typing.Optional[int] = OMIT,
        used_quota_files: typing.Optional[int] = OMIT,
        last_quota_update: typing.Optional[int] = OMIT,
        users: typing.Optional[typing.Sequence[str]] = OMIT,
        filesystem: typing.Optional[FilesystemConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        Updates an existing folder

        Parameters
        ----------
        name_ : str
            folder name

        id : typing.Optional[int]

        name : typing.Optional[str]
            unique name for this virtual folder

        mapped_path : typing.Optional[str]
            absolute filesystem path to use as virtual folder

        description : typing.Optional[str]
            optional description

        used_quota_size : typing.Optional[int]

        used_quota_files : typing.Optional[int]

        last_quota_update : typing.Optional[int]
            Last quota update as unix timestamp in milliseconds

        users : typing.Optional[typing.Sequence[str]]
            list of usernames associated with this virtual folder

        filesystem : typing.Optional[FilesystemConfig]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.folders.update_folder(
            name_="name",
        )
        """
        _response = self._raw_client.update_folder(
            name_,
            id=id,
            name=name,
            mapped_path=mapped_path,
            description=description,
            used_quota_size=used_quota_size,
            used_quota_files=used_quota_files,
            last_quota_update=last_quota_update,
            users=users,
            filesystem=filesystem,
            request_options=request_options,
        )
        return _response.data

    def delete_folder(self, name: str, *, request_options: typing.Optional[RequestOptions] = None) -> ApiResponse:
        """
        Deletes an existing folder. A folder referenced by users or groups cannot be deleted, remove the references first

        Parameters
        ----------
        name : str
            folder name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.folders.delete_folder(
            name="name",
        )
        """
        _response = self._raw_client.delete_folder(name, request_options=request_options)
        return _response.data


class AsyncFoldersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFoldersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFoldersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFoldersClient
        """
        return self._raw_client

    async def get_folders(
        self,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[GetFoldersRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[BaseVirtualFolder]:
        """
        Returns an array with one or more folders

        Parameters
        ----------
        offset : typing.Optional[int]

        limit : typing.Optional[int]
            The maximum number of items to return. Max value is 500, default is 100

        order : typing.Optional[GetFoldersRequestOrder]
            Ordering folders by name. Default ASC

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[BaseVirtualFolder]
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.folders.get_folders()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_folders(
            offset=offset, limit=limit, order=order, request_options=request_options
        )
        return _response.data

    async def add_folder(
        self,
        *,
        confidential_data: typing.Optional[int] = None,
        id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        mapped_path: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        used_quota_size: typing.Optional[int] = OMIT,
        used_quota_files: typing.Optional[int] = OMIT,
        last_quota_update: typing.Optional[int] = OMIT,
        users: typing.Optional[typing.Sequence[str]] = OMIT,
        filesystem: typing.Optional[FilesystemConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BaseVirtualFolder:
        """
        Adds a new folder. A quota scan is required to update the used files/size

        Parameters
        ----------
        confidential_data : typing.Optional[int]
            If set to 1 confidential data will not be hidden. This means that the response will contain the key and additional data for secrets. If a master key is not set or an external KMS is used, the data returned are enough to get the secrets in cleartext. Ignored if the * permission is not granted.

        id : typing.Optional[int]

        name : typing.Optional[str]
            unique name for this virtual folder

        mapped_path : typing.Optional[str]
            absolute filesystem path to use as virtual folder

        description : typing.Optional[str]
            optional description

        used_quota_size : typing.Optional[int]

        used_quota_files : typing.Optional[int]

        last_quota_update : typing.Optional[int]
            Last quota update as unix timestamp in milliseconds

        users : typing.Optional[typing.Sequence[str]]
            list of usernames associated with this virtual folder

        filesystem : typing.Optional[FilesystemConfig]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BaseVirtualFolder
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.folders.add_folder()


        asyncio.run(main())
        """
        _response = await self._raw_client.add_folder(
            confidential_data=confidential_data,
            id=id,
            name=name,
            mapped_path=mapped_path,
            description=description,
            used_quota_size=used_quota_size,
            used_quota_files=used_quota_files,
            last_quota_update=last_quota_update,
            users=users,
            filesystem=filesystem,
            request_options=request_options,
        )
        return _response.data

    async def get_folder_by_name(
        self,
        name: str,
        *,
        confidential_data: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BaseVirtualFolder:
        """
        Returns the folder with the given name if it exists.

        Parameters
        ----------
        name : str
            folder name

        confidential_data : typing.Optional[int]
            If set to 1 confidential data will not be hidden. This means that the response will contain the key and additional data for secrets. If a master key is not set or an external KMS is used, the data returned are enough to get the secrets in cleartext. Ignored if the * permission is not granted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BaseVirtualFolder
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.folders.get_folder_by_name(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_folder_by_name(
            name, confidential_data=confidential_data, request_options=request_options
        )
        return _response.data

    async def update_folder(
        self,
        name_: str,
        *,
        id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        mapped_path: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        used_quota_size: typing.Optional[int] = OMIT,
        used_quota_files: typing.Optional[int] = OMIT,
        last_quota_update: typing.Optional[int] = OMIT,
        users: typing.Optional[typing.Sequence[str]] = OMIT,
        filesystem: typing.Optional[FilesystemConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        Updates an existing folder

        Parameters
        ----------
        name_ : str
            folder name

        id : typing.Optional[int]

        name : typing.Optional[str]
            unique name for this virtual folder

        mapped_path : typing.Optional[str]
            absolute filesystem path to use as virtual folder

        description : typing.Optional[str]
            optional description

        used_quota_size : typing.Optional[int]

        used_quota_files : typing.Optional[int]

        last_quota_update : typing.Optional[int]
            Last quota update as unix timestamp in milliseconds

        users : typing.Optional[typing.Sequence[str]]
            list of usernames associated with this virtual folder

        filesystem : typing.Optional[FilesystemConfig]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.folders.update_folder(
                name_="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_folder(
            name_,
            id=id,
            name=name,
            mapped_path=mapped_path,
            description=description,
            used_quota_size=used_quota_size,
            used_quota_files=used_quota_files,
            last_quota_update=last_quota_update,
            users=users,
            filesystem=filesystem,
            request_options=request_options,
        )
        return _response.data

    async def delete_folder(self, name: str, *, request_options: typing.Optional[RequestOptions] = None) -> ApiResponse:
        """
        Deletes an existing folder. A folder referenced by users or groups cannot be deleted, remove the references first

        Parameters
        ----------
        name : str
            folder name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.folders.delete_folder(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_folder(name, request_options=request_options)
        return _response.data

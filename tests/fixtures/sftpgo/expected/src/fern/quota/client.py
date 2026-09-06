

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_response import ApiResponse
from ..types.folder_quota_scan import FolderQuotaScan
from ..types.quota_scan import QuotaScan
from .raw_client import AsyncRawQuotaClient, RawQuotaClient
from .types.folder_quota_update_usage_request_mode import FolderQuotaUpdateUsageRequestMode
from .types.user_quota_update_usage_request_mode import UserQuotaUpdateUsageRequestMode
from .types.user_transfer_quota_update_usage_request_mode import UserTransferQuotaUpdateUsageRequestMode


OMIT = typing.cast(typing.Any, ...)


class QuotaClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawQuotaClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawQuotaClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawQuotaClient
        """
        return self._raw_client

    def get_users_quota_scans(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[QuotaScan]:
        """
        Returns the active user quota scans

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[QuotaScan]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.quota.get_users_quota_scans()
        """
        _response = self._raw_client.get_users_quota_scans(request_options=request_options)
        return _response.data

    def start_user_quota_scan(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiResponse:
        """
        Starts a new quota scan for the given user. A quota scan updates the number of files and their total size for the specified user and the virtual folders, if any, included in his quota

        Parameters
        ----------
        username : str
            the username

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
        client.quota.start_user_quota_scan(
            username="username",
        )
        """
        _response = self._raw_client.start_user_quota_scan(username, request_options=request_options)
        return _response.data

    def user_quota_update_usage(
        self,
        username: str,
        *,
        mode: typing.Optional[UserQuotaUpdateUsageRequestMode] = None,
        used_quota_size: typing.Optional[int] = OMIT,
        used_quota_files: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        Sets the current used quota limits for the given user

        Parameters
        ----------
        username : str
            the username

        mode : typing.Optional[UserQuotaUpdateUsageRequestMode]
            the update mode specifies if the given quota usage values should be added or replace the current ones

        used_quota_size : typing.Optional[int]

        used_quota_files : typing.Optional[int]

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
        client.quota.user_quota_update_usage(
            username="username",
        )
        """
        _response = self._raw_client.user_quota_update_usage(
            username,
            mode=mode,
            used_quota_size=used_quota_size,
            used_quota_files=used_quota_files,
            request_options=request_options,
        )
        return _response.data

    def user_transfer_quota_update_usage(
        self,
        username: str,
        *,
        mode: typing.Optional[UserTransferQuotaUpdateUsageRequestMode] = None,
        used_upload_data_transfer: typing.Optional[int] = OMIT,
        used_download_data_transfer: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        Sets the current used transfer quota limits for the given user

        Parameters
        ----------
        username : str
            the username

        mode : typing.Optional[UserTransferQuotaUpdateUsageRequestMode]
            the update mode specifies if the given quota usage values should be added or replace the current ones

        used_upload_data_transfer : typing.Optional[int]
            The value must be specified as bytes

        used_download_data_transfer : typing.Optional[int]
            The value must be specified as bytes

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
        client.quota.user_transfer_quota_update_usage(
            username="username",
        )
        """
        _response = self._raw_client.user_transfer_quota_update_usage(
            username,
            mode=mode,
            used_upload_data_transfer=used_upload_data_transfer,
            used_download_data_transfer=used_download_data_transfer,
            request_options=request_options,
        )
        return _response.data

    def get_folders_quota_scans(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[FolderQuotaScan]:
        """
        Returns the active folder quota scans

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FolderQuotaScan]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.quota.get_folders_quota_scans()
        """
        _response = self._raw_client.get_folders_quota_scans(request_options=request_options)
        return _response.data

    def start_folder_quota_scan(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiResponse:
        """
        Starts a new quota scan for the given folder. A quota scan update the number of files and their total size for the specified folder

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
        client.quota.start_folder_quota_scan(
            name="name",
        )
        """
        _response = self._raw_client.start_folder_quota_scan(name, request_options=request_options)
        return _response.data

    def folder_quota_update_usage(
        self,
        name: str,
        *,
        mode: typing.Optional[FolderQuotaUpdateUsageRequestMode] = None,
        used_quota_size: typing.Optional[int] = OMIT,
        used_quota_files: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        Sets the current used quota limits for the given folder

        Parameters
        ----------
        name : str
            folder name

        mode : typing.Optional[FolderQuotaUpdateUsageRequestMode]
            the update mode specifies if the given quota usage values should be added or replace the current ones

        used_quota_size : typing.Optional[int]

        used_quota_files : typing.Optional[int]

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
        client.quota.folder_quota_update_usage(
            name="name",
        )
        """
        _response = self._raw_client.folder_quota_update_usage(
            name,
            mode=mode,
            used_quota_size=used_quota_size,
            used_quota_files=used_quota_files,
            request_options=request_options,
        )
        return _response.data


class AsyncQuotaClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawQuotaClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawQuotaClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawQuotaClient
        """
        return self._raw_client

    async def get_users_quota_scans(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[QuotaScan]:
        """
        Returns the active user quota scans

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[QuotaScan]
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
            await client.quota.get_users_quota_scans()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_users_quota_scans(request_options=request_options)
        return _response.data

    async def start_user_quota_scan(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiResponse:
        """
        Starts a new quota scan for the given user. A quota scan updates the number of files and their total size for the specified user and the virtual folders, if any, included in his quota

        Parameters
        ----------
        username : str
            the username

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
            await client.quota.start_user_quota_scan(
                username="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.start_user_quota_scan(username, request_options=request_options)
        return _response.data

    async def user_quota_update_usage(
        self,
        username: str,
        *,
        mode: typing.Optional[UserQuotaUpdateUsageRequestMode] = None,
        used_quota_size: typing.Optional[int] = OMIT,
        used_quota_files: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        Sets the current used quota limits for the given user

        Parameters
        ----------
        username : str
            the username

        mode : typing.Optional[UserQuotaUpdateUsageRequestMode]
            the update mode specifies if the given quota usage values should be added or replace the current ones

        used_quota_size : typing.Optional[int]

        used_quota_files : typing.Optional[int]

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
            await client.quota.user_quota_update_usage(
                username="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.user_quota_update_usage(
            username,
            mode=mode,
            used_quota_size=used_quota_size,
            used_quota_files=used_quota_files,
            request_options=request_options,
        )
        return _response.data

    async def user_transfer_quota_update_usage(
        self,
        username: str,
        *,
        mode: typing.Optional[UserTransferQuotaUpdateUsageRequestMode] = None,
        used_upload_data_transfer: typing.Optional[int] = OMIT,
        used_download_data_transfer: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        Sets the current used transfer quota limits for the given user

        Parameters
        ----------
        username : str
            the username

        mode : typing.Optional[UserTransferQuotaUpdateUsageRequestMode]
            the update mode specifies if the given quota usage values should be added or replace the current ones

        used_upload_data_transfer : typing.Optional[int]
            The value must be specified as bytes

        used_download_data_transfer : typing.Optional[int]
            The value must be specified as bytes

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
            await client.quota.user_transfer_quota_update_usage(
                username="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.user_transfer_quota_update_usage(
            username,
            mode=mode,
            used_upload_data_transfer=used_upload_data_transfer,
            used_download_data_transfer=used_download_data_transfer,
            request_options=request_options,
        )
        return _response.data

    async def get_folders_quota_scans(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[FolderQuotaScan]:
        """
        Returns the active folder quota scans

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FolderQuotaScan]
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
            await client.quota.get_folders_quota_scans()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_folders_quota_scans(request_options=request_options)
        return _response.data

    async def start_folder_quota_scan(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiResponse:
        """
        Starts a new quota scan for the given folder. A quota scan update the number of files and their total size for the specified folder

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
            await client.quota.start_folder_quota_scan(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.start_folder_quota_scan(name, request_options=request_options)
        return _response.data

    async def folder_quota_update_usage(
        self,
        name: str,
        *,
        mode: typing.Optional[FolderQuotaUpdateUsageRequestMode] = None,
        used_quota_size: typing.Optional[int] = OMIT,
        used_quota_files: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        Sets the current used quota limits for the given folder

        Parameters
        ----------
        name : str
            folder name

        mode : typing.Optional[FolderQuotaUpdateUsageRequestMode]
            the update mode specifies if the given quota usage values should be added or replace the current ones

        used_quota_size : typing.Optional[int]

        used_quota_files : typing.Optional[int]

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
            await client.quota.folder_quota_update_usage(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.folder_quota_update_usage(
            name,
            mode=mode,
            used_quota_size=used_quota_size,
            used_quota_files=used_quota_files,
            request_options=request_options,
        )
        return _response.data

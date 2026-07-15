

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.create_folder_response import CreateFolderResponse
from ..types.delete_folder_response import DeleteFolderResponse
from ..types.get_folder_response import GetFolderResponse
from ..types.parent_folder_id import ParentFolderId
from ..types.update_folder_response import UpdateFolderResponse
from .raw_client import AsyncRawFoldersClient, RawFoldersClient


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

    def add(
        self,
        *,
        name: str,
        parent_folder_id: ParentFolderId,
        raw: typing.Optional[bool] = None,
        fields: typing.Optional[str] = None,
        description: typing.Optional[str] = OMIT,
        drive_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateFolderResponse:
        """
        Create Folder

        Parameters
        ----------
        name : str
            The name of the folder.

        parent_folder_id : ParentFolderId

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        description : typing.Optional[str]
            Optional description of the folder.

        drive_id : typing.Optional[str]
            ID of the drive to create the folder in.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateFolderResponse
            Folders

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.folders.add(
            fields="id,updated_at",
            name="Documents",
            parent_folder_id="1234",
        )
        """
        _response = self._raw_client.add(
            name=name,
            parent_folder_id=parent_folder_id,
            raw=raw,
            fields=fields,
            description=description,
            drive_id=drive_id,
            request_options=request_options,
        )
        return _response.data

    def one(
        self,
        id: str,
        *,
        raw: typing.Optional[bool] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetFolderResponse:
        """
        Get Folder

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetFolderResponse
            Folders

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.folders.one(
            id="id",
            fields="id,updated_at",
        )
        """
        _response = self._raw_client.one(id, raw=raw, fields=fields, request_options=request_options)
        return _response.data

    def delete(
        self, id: str, *, raw: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteFolderResponse:
        """
        Delete Folder

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteFolderResponse
            Folders

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.folders.delete(
            id="id",
        )
        """
        _response = self._raw_client.delete(id, raw=raw, request_options=request_options)
        return _response.data

    def update(
        self,
        id: str,
        *,
        raw: typing.Optional[bool] = None,
        description: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        parent_folder_id: typing.Optional[ParentFolderId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateFolderResponse:
        """
        Rename or move Folder

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        description : typing.Optional[str]
            Optional description of the folder.

        name : typing.Optional[str]
            The name of the folder.

        parent_folder_id : typing.Optional[ParentFolderId]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateFolderResponse
            Folders

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.folders.update(
            id="id",
        )
        """
        _response = self._raw_client.update(
            id,
            raw=raw,
            description=description,
            name=name,
            parent_folder_id=parent_folder_id,
            request_options=request_options,
        )
        return _response.data

    def copy(
        self,
        id: str,
        *,
        parent_folder_id: ParentFolderId,
        raw: typing.Optional[bool] = None,
        fields: typing.Optional[str] = None,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateFolderResponse:
        """
        Copy Folder

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        parent_folder_id : ParentFolderId

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        name : typing.Optional[str]
            The name of the folder.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateFolderResponse
            Folders

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.folders.copy(
            id="id",
            fields="id,updated_at",
            parent_folder_id="1234",
        )
        """
        _response = self._raw_client.copy(
            id, parent_folder_id=parent_folder_id, raw=raw, fields=fields, name=name, request_options=request_options
        )
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

    async def add(
        self,
        *,
        name: str,
        parent_folder_id: ParentFolderId,
        raw: typing.Optional[bool] = None,
        fields: typing.Optional[str] = None,
        description: typing.Optional[str] = OMIT,
        drive_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateFolderResponse:
        """
        Create Folder

        Parameters
        ----------
        name : str
            The name of the folder.

        parent_folder_id : ParentFolderId

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        description : typing.Optional[str]
            Optional description of the folder.

        drive_id : typing.Optional[str]
            ID of the drive to create the folder in.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateFolderResponse
            Folders

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.folders.add(
                fields="id,updated_at",
                name="Documents",
                parent_folder_id="1234",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add(
            name=name,
            parent_folder_id=parent_folder_id,
            raw=raw,
            fields=fields,
            description=description,
            drive_id=drive_id,
            request_options=request_options,
        )
        return _response.data

    async def one(
        self,
        id: str,
        *,
        raw: typing.Optional[bool] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetFolderResponse:
        """
        Get Folder

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetFolderResponse
            Folders

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.folders.one(
                id="id",
                fields="id,updated_at",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.one(id, raw=raw, fields=fields, request_options=request_options)
        return _response.data

    async def delete(
        self, id: str, *, raw: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteFolderResponse:
        """
        Delete Folder

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteFolderResponse
            Folders

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.folders.delete(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(id, raw=raw, request_options=request_options)
        return _response.data

    async def update(
        self,
        id: str,
        *,
        raw: typing.Optional[bool] = None,
        description: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        parent_folder_id: typing.Optional[ParentFolderId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateFolderResponse:
        """
        Rename or move Folder

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        description : typing.Optional[str]
            Optional description of the folder.

        name : typing.Optional[str]
            The name of the folder.

        parent_folder_id : typing.Optional[ParentFolderId]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateFolderResponse
            Folders

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.folders.update(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(
            id,
            raw=raw,
            description=description,
            name=name,
            parent_folder_id=parent_folder_id,
            request_options=request_options,
        )
        return _response.data

    async def copy(
        self,
        id: str,
        *,
        parent_folder_id: ParentFolderId,
        raw: typing.Optional[bool] = None,
        fields: typing.Optional[str] = None,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateFolderResponse:
        """
        Copy Folder

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        parent_folder_id : ParentFolderId

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        name : typing.Optional[str]
            The name of the folder.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateFolderResponse
            Folders

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.folders.copy(
                id="id",
                fields="id,updated_at",
                parent_folder_id="1234",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.copy(
            id, parent_folder_id=parent_folder_id, raw=raw, fields=fields, name=name, request_options=request_options
        )
        return _response.data



import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.file import File
from ..types.file_list import FileList
from .raw_client import AsyncRawStorageClient, RawStorageClient


OMIT = typing.cast(typing.Any, ...)


class StorageClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawStorageClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawStorageClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawStorageClient
        """
        return self._raw_client

    def list_files(
        self,
        *,
        search: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order_type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FileList:
        """
        Get a list of all the user files. You can use the query params to filter your results. On admin mode, this endpoint will return a list of all of the project's files. [Learn more about different API modes](/docs/admin).

        Parameters
        ----------
        search : typing.Optional[str]
            Search term to filter your list results. Max length: 256 chars.

        limit : typing.Optional[int]
            Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request.

        offset : typing.Optional[int]
            Results offset. The default value is 0. Use this param to manage pagination.

        order_type : typing.Optional[str]
            Order result by ASC or DESC order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FileList
            Files List

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.storage.list_files()
        """
        _response = self._raw_client.list_files(
            search=search, limit=limit, offset=offset, order_type=order_type, request_options=request_options
        )
        return _response.data

    def create_file(
        self,
        *,
        file: str,
        read: typing.Optional[typing.List[str]] = OMIT,
        write: typing.Optional[typing.List[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> File:
        """
        Create a new file. The user who creates the file will automatically be assigned to read and write access unless he has passed custom values for read and write arguments.

        Parameters
        ----------
        file : str
            Binary file.

        read : typing.Optional[typing.List[str]]
            An array of strings with read permissions. By default only the current user is granted with read permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions.

        write : typing.Optional[typing.List[str]]
            An array of strings with write permissions. By default only the current user is granted with write permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        File
            File

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.storage.create_file(
            file="file",
        )
        """
        _response = self._raw_client.create_file(file=file, read=read, write=write, request_options=request_options)
        return _response.data

    def get_file(self, file_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> File:
        """
        Get a file by its unique ID. This endpoint response returns a JSON object with the file metadata.

        Parameters
        ----------
        file_id : str
            File unique ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        File
            File

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.storage.get_file(
            file_id="fileId",
        )
        """
        _response = self._raw_client.get_file(file_id, request_options=request_options)
        return _response.data

    def update_file(
        self,
        file_id: str,
        *,
        read: typing.Sequence[str],
        write: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> File:
        """
        Update a file by its unique ID. Only users with write permissions have access to update this resource.

        Parameters
        ----------
        file_id : str
            File unique ID.

        read : typing.Sequence[str]
            An array of strings with read permissions. By default no user is granted with any read permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions.

        write : typing.Sequence[str]
            An array of strings with write permissions. By default no user is granted with any write permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        File
            File

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.storage.update_file(
            file_id="fileId",
            read=["read"],
            write=["write"],
        )
        """
        _response = self._raw_client.update_file(file_id, read=read, write=write, request_options=request_options)
        return _response.data

    def delete_file(self, file_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a file by its unique ID. Only users with write permissions have access to delete this resource.

        Parameters
        ----------
        file_id : str
            File unique ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.storage.delete_file(
            file_id="fileId",
        )
        """
        _response = self._raw_client.delete_file(file_id, request_options=request_options)
        return _response.data

    def get_file_download(self, file_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get a file content by its unique ID. The endpoint response return with a 'Content-Disposition: attachment' header that tells the browser to start downloading the file to user downloads directory.

        Parameters
        ----------
        file_id : str
            File unique ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.storage.get_file_download(
            file_id="fileId",
        )
        """
        _response = self._raw_client.get_file_download(file_id, request_options=request_options)
        return _response.data

    def get_file_preview(
        self,
        file_id: str,
        *,
        width: typing.Optional[int] = None,
        height: typing.Optional[int] = None,
        gravity: typing.Optional[str] = None,
        quality: typing.Optional[int] = None,
        border_width: typing.Optional[int] = None,
        border_color: typing.Optional[str] = None,
        border_radius: typing.Optional[int] = None,
        opacity: typing.Optional[float] = None,
        rotation: typing.Optional[int] = None,
        background: typing.Optional[str] = None,
        output: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Get a file preview image. Currently, this method supports preview for image files (jpg, png, and gif), other supported formats, like pdf, docs, slides, and spreadsheets, will return the file icon image. You can also pass query string arguments for cutting and resizing your preview image.

        Parameters
        ----------
        file_id : str
            File unique ID

        width : typing.Optional[int]
            Resize preview image width, Pass an integer between 0 to 4000.

        height : typing.Optional[int]
            Resize preview image height, Pass an integer between 0 to 4000.

        gravity : typing.Optional[str]
            Image crop gravity. Can be one of center,top-left,top,top-right,left,right,bottom-left,bottom,bottom-right

        quality : typing.Optional[int]
            Preview image quality. Pass an integer between 0 to 100. Defaults to 100.

        border_width : typing.Optional[int]
            Preview image border in pixels. Pass an integer between 0 to 100. Defaults to 0.

        border_color : typing.Optional[str]
            Preview image border color. Use a valid HEX color, no # is needed for prefix.

        border_radius : typing.Optional[int]
            Preview image border radius in pixels. Pass an integer between 0 to 4000.

        opacity : typing.Optional[float]
            Preview image opacity. Only works with images having an alpha channel (like png). Pass a number between 0 to 1.

        rotation : typing.Optional[int]
            Preview image rotation in degrees. Pass an integer between 0 and 360.

        background : typing.Optional[str]
            Preview image background color. Only works with transparent images (png). Use a valid HEX color, no # is needed for prefix.

        output : typing.Optional[str]
            Output format type (jpeg, jpg, png, gif and webp).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.storage.get_file_preview(
            file_id="fileId",
        )
        """
        _response = self._raw_client.get_file_preview(
            file_id,
            width=width,
            height=height,
            gravity=gravity,
            quality=quality,
            border_width=border_width,
            border_color=border_color,
            border_radius=border_radius,
            opacity=opacity,
            rotation=rotation,
            background=background,
            output=output,
            request_options=request_options,
        )
        return _response.data

    def get_file_view(self, file_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get a file content by its unique ID. This endpoint is similar to the download method but returns with no  'Content-Disposition: attachment' header.

        Parameters
        ----------
        file_id : str
            File unique ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.storage.get_file_view(
            file_id="fileId",
        )
        """
        _response = self._raw_client.get_file_view(file_id, request_options=request_options)
        return _response.data


class AsyncStorageClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawStorageClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawStorageClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawStorageClient
        """
        return self._raw_client

    async def list_files(
        self,
        *,
        search: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order_type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FileList:
        """
        Get a list of all the user files. You can use the query params to filter your results. On admin mode, this endpoint will return a list of all of the project's files. [Learn more about different API modes](/docs/admin).

        Parameters
        ----------
        search : typing.Optional[str]
            Search term to filter your list results. Max length: 256 chars.

        limit : typing.Optional[int]
            Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request.

        offset : typing.Optional[int]
            Results offset. The default value is 0. Use this param to manage pagination.

        order_type : typing.Optional[str]
            Order result by ASC or DESC order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FileList
            Files List

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.storage.list_files()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_files(
            search=search, limit=limit, offset=offset, order_type=order_type, request_options=request_options
        )
        return _response.data

    async def create_file(
        self,
        *,
        file: str,
        read: typing.Optional[typing.List[str]] = OMIT,
        write: typing.Optional[typing.List[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> File:
        """
        Create a new file. The user who creates the file will automatically be assigned to read and write access unless he has passed custom values for read and write arguments.

        Parameters
        ----------
        file : str
            Binary file.

        read : typing.Optional[typing.List[str]]
            An array of strings with read permissions. By default only the current user is granted with read permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions.

        write : typing.Optional[typing.List[str]]
            An array of strings with write permissions. By default only the current user is granted with write permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        File
            File

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.storage.create_file(
                file="file",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_file(
            file=file, read=read, write=write, request_options=request_options
        )
        return _response.data

    async def get_file(self, file_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> File:
        """
        Get a file by its unique ID. This endpoint response returns a JSON object with the file metadata.

        Parameters
        ----------
        file_id : str
            File unique ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        File
            File

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.storage.get_file(
                file_id="fileId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_file(file_id, request_options=request_options)
        return _response.data

    async def update_file(
        self,
        file_id: str,
        *,
        read: typing.Sequence[str],
        write: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> File:
        """
        Update a file by its unique ID. Only users with write permissions have access to update this resource.

        Parameters
        ----------
        file_id : str
            File unique ID.

        read : typing.Sequence[str]
            An array of strings with read permissions. By default no user is granted with any read permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions.

        write : typing.Sequence[str]
            An array of strings with write permissions. By default no user is granted with any write permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        File
            File

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.storage.update_file(
                file_id="fileId",
                read=["read"],
                write=["write"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_file(file_id, read=read, write=write, request_options=request_options)
        return _response.data

    async def delete_file(self, file_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a file by its unique ID. Only users with write permissions have access to delete this resource.

        Parameters
        ----------
        file_id : str
            File unique ID.

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
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.storage.delete_file(
                file_id="fileId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_file(file_id, request_options=request_options)
        return _response.data

    async def get_file_download(self, file_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get a file content by its unique ID. The endpoint response return with a 'Content-Disposition: attachment' header that tells the browser to start downloading the file to user downloads directory.

        Parameters
        ----------
        file_id : str
            File unique ID.

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
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.storage.get_file_download(
                file_id="fileId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_file_download(file_id, request_options=request_options)
        return _response.data

    async def get_file_preview(
        self,
        file_id: str,
        *,
        width: typing.Optional[int] = None,
        height: typing.Optional[int] = None,
        gravity: typing.Optional[str] = None,
        quality: typing.Optional[int] = None,
        border_width: typing.Optional[int] = None,
        border_color: typing.Optional[str] = None,
        border_radius: typing.Optional[int] = None,
        opacity: typing.Optional[float] = None,
        rotation: typing.Optional[int] = None,
        background: typing.Optional[str] = None,
        output: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Get a file preview image. Currently, this method supports preview for image files (jpg, png, and gif), other supported formats, like pdf, docs, slides, and spreadsheets, will return the file icon image. You can also pass query string arguments for cutting and resizing your preview image.

        Parameters
        ----------
        file_id : str
            File unique ID

        width : typing.Optional[int]
            Resize preview image width, Pass an integer between 0 to 4000.

        height : typing.Optional[int]
            Resize preview image height, Pass an integer between 0 to 4000.

        gravity : typing.Optional[str]
            Image crop gravity. Can be one of center,top-left,top,top-right,left,right,bottom-left,bottom,bottom-right

        quality : typing.Optional[int]
            Preview image quality. Pass an integer between 0 to 100. Defaults to 100.

        border_width : typing.Optional[int]
            Preview image border in pixels. Pass an integer between 0 to 100. Defaults to 0.

        border_color : typing.Optional[str]
            Preview image border color. Use a valid HEX color, no # is needed for prefix.

        border_radius : typing.Optional[int]
            Preview image border radius in pixels. Pass an integer between 0 to 4000.

        opacity : typing.Optional[float]
            Preview image opacity. Only works with images having an alpha channel (like png). Pass a number between 0 to 1.

        rotation : typing.Optional[int]
            Preview image rotation in degrees. Pass an integer between 0 and 360.

        background : typing.Optional[str]
            Preview image background color. Only works with transparent images (png). Use a valid HEX color, no # is needed for prefix.

        output : typing.Optional[str]
            Output format type (jpeg, jpg, png, gif and webp).

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
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.storage.get_file_preview(
                file_id="fileId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_file_preview(
            file_id,
            width=width,
            height=height,
            gravity=gravity,
            quality=quality,
            border_width=border_width,
            border_color=border_color,
            border_radius=border_radius,
            opacity=opacity,
            rotation=rotation,
            background=background,
            output=output,
            request_options=request_options,
        )
        return _response.data

    async def get_file_view(self, file_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get a file content by its unique ID. This endpoint is similar to the download method but returns with no  'Content-Disposition: attachment' header.

        Parameters
        ----------
        file_id : str
            File unique ID.

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
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.storage.get_file_view(
                file_id="fileId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_file_view(file_id, request_options=request_options)
        return _response.data

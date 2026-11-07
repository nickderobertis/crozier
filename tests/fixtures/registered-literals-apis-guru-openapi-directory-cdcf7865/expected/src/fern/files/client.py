

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawFilesClient, RawFilesClient
from .types.files_detail_response_item import FilesDetailResponseItem
from .types.files_version_detail_response_item import FilesVersionDetailResponseItem
from .types.files_versions_response_item import FilesVersionsResponseItem


OMIT = typing.cast(typing.Any, ...)


class FilesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFilesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFilesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFilesClient
        """
        return self._raw_client

    def detail(
        self, file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[FilesDetailResponseItem]:
        """
        Retrieves the details of a file (or folder)
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested file, if the request was successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
        ### Waterbutler API actions

        Files can be modified through the Waterbutler API routes found in `links` (`new_folder`, `move`, `upload`, `download`, and `delete`).

        #### Download (files)

        To download a file, issue a GET request against the download link. The response will have the Content-Disposition header set, which will will trigger a download in a browser.

        #### Create Subfolder (folders)

        You can create a subfolder of an existing folder by issuing a PUT request against the new_folder link. The ?kind=folder portion of the query parameter is already included in the new_folder link. The name of the new subfolder should be provided in the name query parameter. The response will contain a WaterButler folder entity. If a folder with that name already exists in the parent directory, the server will return a 409 Conflict error response.

        #### Upload New File (folders)


          To upload a file to a folder, issue a PUT request to the folder's upload link with the raw file data in the request body, and the kind and name query parameters set to 'file' and the desired name of the file. The response will contain a WaterButler file entity that describes the new file. If a file with the same name already exists in the folder, the server will return a 409 Conflict error response.


        #### Update Existing File (file)

        To update an existing file, issue a PUT request to the file's upload link with the raw file data in the request body and the kind query parameter set to "file". The update action will create a new version of the file. The response will contain a WaterButler file entity that describes the updated file.

        #### Rename (files, folders)

        To rename a file or folder, issue a POST request to the move link with the action body parameter set to "rename" and the rename body parameter set to the desired name. The response will contain either a folder entity or file entity with the new name.

        #### Move & Copy (files, folders)

        Move and copy actions both use the same request structure, a POST to the move url, but with different values for the action body parameters. The path parameter is also required and should be the OSF path attribute of the folder being written to. The rename and conflict parameters are optional. If you wish to change the name of the file or folder at its destination, set the rename parameter to the new name. The conflict param governs how name clashes are resolved. Possible values are replace and keep. replace is the default and will overwrite the file that already exists in the target folder. keep will attempt to keep both by adding a suffix to the new file's name until it no longer conflicts. The suffix will be ' (x)' where x is a increasing integer starting from 1. This behavior is intended to mimic that of the OS X Finder. The response will contain either a folder entity or file entity with the new name.
        Files and folders can also be moved between nodes and providers. The resource parameter is the id of the node under which the file/folder should be moved. It must agree with the path parameter, that is the path must identify a valid folder under the node identified by resource. Likewise, the provider parameter may be used to move the file/folder to another storage provider, but both the resource and path parameters must belong to a node and folder already extant on that provider. Both resource and provider default to the current node and providers.
        If a moved/copied file is overwriting an existing file, a 200 OK response will be returned. Otherwise, a 201 Created will be returned.

        #### Delete (file, folders)

        To delete a file or folder send a DELETE request to the delete link. Nothing will be returned in the response body.

        Parameters
        ----------
        file_id : str
            The unique identifier of the file you wish to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FilesDetailResponseItem]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.files.detail(
            file_id="file_id",
        )
        """
        _response = self._raw_client.detail(file_id, request_options=request_options)
        return _response.data

    def patch(
        self,
        file_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates the specified file by setting the values of the parameters passed. Any parameters not provided will be left unchanged.
        #### Returns
        Returns JSON with a `data` key containing the new representation of the updated file, if the request is successful.

        If the request is unsuccessful, JSON with an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        file_id : str
            The unique identifier of the file you wish to update.

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.files.patch(
            file_id="file_id",
            request={
                "data": {
                    "attributes": {"name": "new file name.jpg"},
                    "id": "{file_id}",
                    "type": "files",
                }
            },
        )
        """
        _response = self._raw_client.patch(file_id, request=request, request_options=request_options)
        return _response.data

    def versions(
        self, file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[FilesVersionsResponseItem]:
        """

        A paginated list of all file versions.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of 10 file versions. Each resource in the array is a separate file version object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        file_id : str
            The unique identifier of the file from which you want to retrieve versions.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FilesVersionsResponseItem]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.files.versions(
            file_id="file_id",
        )
        """
        _response = self._raw_client.versions(file_id, request_options=request_options)
        return _response.data

    def version_detail(
        self, file_id: str, version_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[FilesVersionDetailResponseItem]:
        """
        Retrieves the details of a file version
        #### Returns

        Returns a JSON object with a `data` key containing the representation of the requested file, if the request was successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        file_id : str
            The unique identifier of the file from which you want to retrieve versions.

        version_id : str
            The file version number you want to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FilesVersionDetailResponseItem]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.files.version_detail(
            file_id="file_id",
            version_id="version_id",
        )
        """
        _response = self._raw_client.version_detail(file_id, version_id, request_options=request_options)
        return _response.data


class AsyncFilesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFilesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFilesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFilesClient
        """
        return self._raw_client

    async def detail(
        self, file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[FilesDetailResponseItem]:
        """
        Retrieves the details of a file (or folder)
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested file, if the request was successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
        ### Waterbutler API actions

        Files can be modified through the Waterbutler API routes found in `links` (`new_folder`, `move`, `upload`, `download`, and `delete`).

        #### Download (files)

        To download a file, issue a GET request against the download link. The response will have the Content-Disposition header set, which will will trigger a download in a browser.

        #### Create Subfolder (folders)

        You can create a subfolder of an existing folder by issuing a PUT request against the new_folder link. The ?kind=folder portion of the query parameter is already included in the new_folder link. The name of the new subfolder should be provided in the name query parameter. The response will contain a WaterButler folder entity. If a folder with that name already exists in the parent directory, the server will return a 409 Conflict error response.

        #### Upload New File (folders)


          To upload a file to a folder, issue a PUT request to the folder's upload link with the raw file data in the request body, and the kind and name query parameters set to 'file' and the desired name of the file. The response will contain a WaterButler file entity that describes the new file. If a file with the same name already exists in the folder, the server will return a 409 Conflict error response.


        #### Update Existing File (file)

        To update an existing file, issue a PUT request to the file's upload link with the raw file data in the request body and the kind query parameter set to "file". The update action will create a new version of the file. The response will contain a WaterButler file entity that describes the updated file.

        #### Rename (files, folders)

        To rename a file or folder, issue a POST request to the move link with the action body parameter set to "rename" and the rename body parameter set to the desired name. The response will contain either a folder entity or file entity with the new name.

        #### Move & Copy (files, folders)

        Move and copy actions both use the same request structure, a POST to the move url, but with different values for the action body parameters. The path parameter is also required and should be the OSF path attribute of the folder being written to. The rename and conflict parameters are optional. If you wish to change the name of the file or folder at its destination, set the rename parameter to the new name. The conflict param governs how name clashes are resolved. Possible values are replace and keep. replace is the default and will overwrite the file that already exists in the target folder. keep will attempt to keep both by adding a suffix to the new file's name until it no longer conflicts. The suffix will be ' (x)' where x is a increasing integer starting from 1. This behavior is intended to mimic that of the OS X Finder. The response will contain either a folder entity or file entity with the new name.
        Files and folders can also be moved between nodes and providers. The resource parameter is the id of the node under which the file/folder should be moved. It must agree with the path parameter, that is the path must identify a valid folder under the node identified by resource. Likewise, the provider parameter may be used to move the file/folder to another storage provider, but both the resource and path parameters must belong to a node and folder already extant on that provider. Both resource and provider default to the current node and providers.
        If a moved/copied file is overwriting an existing file, a 200 OK response will be returned. Otherwise, a 201 Created will be returned.

        #### Delete (file, folders)

        To delete a file or folder send a DELETE request to the delete link. Nothing will be returned in the response body.

        Parameters
        ----------
        file_id : str
            The unique identifier of the file you wish to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FilesDetailResponseItem]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.files.detail(
                file_id="file_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.detail(file_id, request_options=request_options)
        return _response.data

    async def patch(
        self,
        file_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates the specified file by setting the values of the parameters passed. Any parameters not provided will be left unchanged.
        #### Returns
        Returns JSON with a `data` key containing the new representation of the updated file, if the request is successful.

        If the request is unsuccessful, JSON with an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        file_id : str
            The unique identifier of the file you wish to update.

        request : typing.Dict[str, typing.Any]

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
            await client.files.patch(
                file_id="file_id",
                request={
                    "data": {
                        "attributes": {"name": "new file name.jpg"},
                        "id": "{file_id}",
                        "type": "files",
                    }
                },
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch(file_id, request=request, request_options=request_options)
        return _response.data

    async def versions(
        self, file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[FilesVersionsResponseItem]:
        """

        A paginated list of all file versions.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of 10 file versions. Each resource in the array is a separate file version object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        file_id : str
            The unique identifier of the file from which you want to retrieve versions.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FilesVersionsResponseItem]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.files.versions(
                file_id="file_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.versions(file_id, request_options=request_options)
        return _response.data

    async def version_detail(
        self, file_id: str, version_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[FilesVersionDetailResponseItem]:
        """
        Retrieves the details of a file version
        #### Returns

        Returns a JSON object with a `data` key containing the representation of the requested file, if the request was successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        file_id : str
            The unique identifier of the file from which you want to retrieve versions.

        version_id : str
            The file version number you want to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FilesVersionDetailResponseItem]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.files.version_detail(
                file_id="file_id",
                version_id="version_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.version_detail(file_id, version_id, request_options=request_options)
        return _response.data

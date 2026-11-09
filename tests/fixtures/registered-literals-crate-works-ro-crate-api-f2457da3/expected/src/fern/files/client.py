

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.id import Id
from ..types.order import Order
from .raw_client import AsyncRawFilesClient, RawFilesClient
from .types.get_file_request_disposition import GetFileRequestDisposition
from .types.head_file_request_disposition import HeadFileRequestDisposition
from .types.list_files_request_sort import ListFilesRequestSort
from .types.list_files_response import ListFilesResponse


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

    def list_files(
        self,
        *,
        member_of: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        sort: typing.Optional[ListFilesRequestSort] = None,
        order: typing.Optional[Order] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListFilesResponse:
        """
        Retrieve and list file in the repository. This endpoint returns key metadata describing each file. The response can be filtered by memberOf to show files attached to a specific entity, and supports pagination and sorting.

        Parameters
        ----------
        member_of : typing.Optional[str]
            Filter to only files that are directly attached to a specific entity (e.g., files within a collection or object).

        limit : typing.Optional[int]
            Maximum number of entities to return.

        offset : typing.Optional[int]
            Number of items to skip before returning the results, useful for pagination.

        sort : typing.Optional[ListFilesRequestSort]
            Field to sort by, such as `filename` or `createdAt`.

        order : typing.Optional[Order]
            Sort order:
            * `asc` - Ascending, from A to Z
            * `desc` - Descending, from Z to A

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListFilesResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.files.list_files(
            member_of="https://catalog.paradisec.org.au/repository/NT1/001",
        )
        """
        _response = self._raw_client.list_files(
            member_of=member_of, limit=limit, offset=offset, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    def get_file(
        self,
        id: Id,
        *,
        disposition: typing.Optional[GetFileRequestDisposition] = None,
        filename: typing.Optional[str] = None,
        no_redirect: typing.Optional[bool] = None,
        range: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Retrieve a file. The file can be returned inline (e.g., displayed in the browser) or as an attachment for download (e.g., prompting a save dialog), based on the disposition parameter.
        The API can serve the file directly or redirect to the location of the file.

        Parameters
        ----------
        id : Id
            The ID of the file.

        disposition : typing.Optional[GetFileRequestDisposition]
            The HTTP Content-Disposition for how the file should be handled by the client.

        filename : typing.Optional[str]
            When the file is served as an attachment, the name to use when saving.

        no_redirect : typing.Optional[bool]
            Return the location as JSON instead of a 302 redirect.

        range : typing.Optional[str]
            Request specific byte range(s) of the file. Supports standard HTTP Range header syntax.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.files.get_file(
            id="https://catalog.paradisec.org.au/repository/NT1/001",
            range="bytes=0-1023",
            filename="foo.wav",
        )
        """
        _response = self._raw_client.get_file(
            id,
            disposition=disposition,
            filename=filename,
            no_redirect=no_redirect,
            range=range,
            request_options=request_options,
        )
        return _response.data

    def head_file(
        self,
        id: Id,
        *,
        disposition: typing.Optional[HeadFileRequestDisposition] = None,
        filename: typing.Optional[str] = None,
        no_redirect: typing.Optional[bool] = None,
        range: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, str]:
        """
        Retrieve file metadata headers without downloading the file content. Returns the same headers as GET but with no response body, useful for checking file availability, size, type, and caching information.

        Parameters
        ----------
        id : Id
            The ID of the file.

        disposition : typing.Optional[HeadFileRequestDisposition]
            The HTTP Content-Disposition for how the file should be handled by the client.

        filename : typing.Optional[str]
            When the file is served as an attachment, the name to use when saving.

        no_redirect : typing.Optional[bool]
            Return the location as JSON instead of a 302 redirect.

        range : typing.Optional[str]
            Request specific byte range(s) of the file. Supports standard HTTP Range header syntax.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.files.head_file(
            id="https://catalog.paradisec.org.au/repository/NT1/001",
            range="bytes=0-1023",
            filename="foo.wav",
        )
        """
        _response = self._raw_client.head_file(
            id,
            disposition=disposition,
            filename=filename,
            no_redirect=no_redirect,
            range=range,
            request_options=request_options,
        )
        return _response.headers


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

    async def list_files(
        self,
        *,
        member_of: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        sort: typing.Optional[ListFilesRequestSort] = None,
        order: typing.Optional[Order] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListFilesResponse:
        """
        Retrieve and list file in the repository. This endpoint returns key metadata describing each file. The response can be filtered by memberOf to show files attached to a specific entity, and supports pagination and sorting.

        Parameters
        ----------
        member_of : typing.Optional[str]
            Filter to only files that are directly attached to a specific entity (e.g., files within a collection or object).

        limit : typing.Optional[int]
            Maximum number of entities to return.

        offset : typing.Optional[int]
            Number of items to skip before returning the results, useful for pagination.

        sort : typing.Optional[ListFilesRequestSort]
            Field to sort by, such as `filename` or `createdAt`.

        order : typing.Optional[Order]
            Sort order:
            * `asc` - Ascending, from A to Z
            * `desc` - Descending, from Z to A

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListFilesResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.files.list_files(
                member_of="https://catalog.paradisec.org.au/repository/NT1/001",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_files(
            member_of=member_of, limit=limit, offset=offset, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    async def get_file(
        self,
        id: Id,
        *,
        disposition: typing.Optional[GetFileRequestDisposition] = None,
        filename: typing.Optional[str] = None,
        no_redirect: typing.Optional[bool] = None,
        range: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Retrieve a file. The file can be returned inline (e.g., displayed in the browser) or as an attachment for download (e.g., prompting a save dialog), based on the disposition parameter.
        The API can serve the file directly or redirect to the location of the file.

        Parameters
        ----------
        id : Id
            The ID of the file.

        disposition : typing.Optional[GetFileRequestDisposition]
            The HTTP Content-Disposition for how the file should be handled by the client.

        filename : typing.Optional[str]
            When the file is served as an attachment, the name to use when saving.

        no_redirect : typing.Optional[bool]
            Return the location as JSON instead of a 302 redirect.

        range : typing.Optional[str]
            Request specific byte range(s) of the file. Supports standard HTTP Range header syntax.

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.files.get_file(
                id="https://catalog.paradisec.org.au/repository/NT1/001",
                range="bytes=0-1023",
                filename="foo.wav",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_file(
            id,
            disposition=disposition,
            filename=filename,
            no_redirect=no_redirect,
            range=range,
            request_options=request_options,
        )
        return _response.data

    async def head_file(
        self,
        id: Id,
        *,
        disposition: typing.Optional[HeadFileRequestDisposition] = None,
        filename: typing.Optional[str] = None,
        no_redirect: typing.Optional[bool] = None,
        range: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, str]:
        """
        Retrieve file metadata headers without downloading the file content. Returns the same headers as GET but with no response body, useful for checking file availability, size, type, and caching information.

        Parameters
        ----------
        id : Id
            The ID of the file.

        disposition : typing.Optional[HeadFileRequestDisposition]
            The HTTP Content-Disposition for how the file should be handled by the client.

        filename : typing.Optional[str]
            When the file is served as an attachment, the name to use when saving.

        no_redirect : typing.Optional[bool]
            Return the location as JSON instead of a 302 redirect.

        range : typing.Optional[str]
            Request specific byte range(s) of the file. Supports standard HTTP Range header syntax.

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.files.head_file(
                id="https://catalog.paradisec.org.au/repository/NT1/001",
                range="bytes=0-1023",
                filename="foo.wav",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.head_file(
            id,
            disposition=disposition,
            filename=filename,
            no_redirect=no_redirect,
            range=range,
            request_options=request_options,
        )
        return _response.headers



import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.document import Document
from ..types.paginated_response_of_document import PaginatedResponseOfDocument
from ..types.visibility_update import VisibilityUpdate
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

    def list_all_documents(
        self,
        id4n: str,
        *,
        owner: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResponseOfDocument:
        """
        Listing all documents of an id4n

        Parameters
        ----------
        id4n : str
            id4n

        owner : typing.Optional[str]
            Filter by owner organization

        offset : typing.Optional[int]
            Start with the n-th element

        limit : typing.Optional[int]
            The maximum count of returned elements

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedResponseOfDocument
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.storage.list_all_documents(
            id4n="id4n",
        )
        """
        _response = self._raw_client.list_all_documents(
            id4n, owner=owner, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    def list_documents(
        self,
        id4n: str,
        organization_id: str,
        *,
        owner: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResponseOfDocument:
        """
        Listing documents of an id4n seen by a specified organization

        Parameters
        ----------
        id4n : str
            id4n

        organization_id : str
            organizationId

        owner : typing.Optional[str]
            Filter by owner organization

        offset : typing.Optional[int]
            Start with the n-th element

        limit : typing.Optional[int]
            The maximum count of returned elements

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedResponseOfDocument
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.storage.list_documents(
            id4n="id4n",
            organization_id="organizationId",
        )
        """
        _response = self._raw_client.list_documents(
            id4n, organization_id, owner=owner, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    def create_document(
        self,
        id4n: str,
        organization_id: str,
        *,
        content: core.File,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Document:
        """
        The documents' mime type is suggested on octet-stream data. Otherwise the specified content mime type is used.

        Parameters
        ----------
        id4n : str
            id4n

        organization_id : str
            organizationId

        content : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Document
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.storage.create_document(
            id4n="id4n",
            organization_id="organizationId",
        )
        """
        _response = self._raw_client.create_document(
            id4n, organization_id, content=content, request_options=request_options
        )
        return _response.data

    def put_document(
        self,
        id4n: str,
        organization_id: str,
        *,
        content: core.File,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Document:
        """
        Creating or overwriting an existing document

        Parameters
        ----------
        id4n : str
            id4n

        organization_id : str
            organizationId

        content : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Document
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.storage.put_document(
            id4n="id4n",
            organization_id="organizationId",
        )
        """
        _response = self._raw_client.put_document(
            id4n, organization_id, content=content, request_options=request_options
        )
        return _response.data

    def read_document(
        self,
        id4n: str,
        organization_id: str,
        file_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Parameters
        ----------
        id4n : str
            id4n

        organization_id : str
            organizationId

        file_name : str
            fileName

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.storage.read_document(
            id4n="id4n",
            organization_id="organizationId",
            file_name="fileName",
        )
        """
        _response = self._raw_client.read_document(id4n, organization_id, file_name, request_options=request_options)
        return _response.data

    def delete_document(
        self,
        id4n: str,
        organization_id: str,
        file_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id4n : str
            id4n

        organization_id : str
            organizationId

        file_name : str
            fileName

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
        client.storage.delete_document(
            id4n="id4n",
            organization_id="organizationId",
            file_name="fileName",
        )
        """
        _response = self._raw_client.delete_document(id4n, organization_id, file_name, request_options=request_options)
        return _response.data

    def get_document(
        self,
        id4n: str,
        organization_id: str,
        file_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Document:
        """
        Parameters
        ----------
        id4n : str
            id4n

        organization_id : str
            organizationId

        file_name : str
            fileName

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Document
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.storage.get_document(
            id4n="id4n",
            organization_id="organizationId",
            file_name="fileName",
        )
        """
        _response = self._raw_client.get_document(id4n, organization_id, file_name, request_options=request_options)
        return _response.data

    def update_document_metadata(
        self,
        id4n: str,
        organization_id: str,
        file_name: str,
        *,
        filename: typing.Optional[str] = OMIT,
        mime_type: typing.Optional[str] = OMIT,
        visibility: typing.Optional[VisibilityUpdate] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[Document]:
        """
        Parameters
        ----------
        id4n : str
            id4n

        organization_id : str
            organizationId

        file_name : str
            fileName

        filename : typing.Optional[str]
            File Name

        mime_type : typing.Optional[str]
            Mime Type

        visibility : typing.Optional[VisibilityUpdate]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[Document]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.storage.update_document_metadata(
            id4n="id4n",
            organization_id="organizationId",
            file_name="fileName",
        )
        """
        _response = self._raw_client.update_document_metadata(
            id4n,
            organization_id,
            file_name,
            filename=filename,
            mime_type=mime_type,
            visibility=visibility,
            request_options=request_options,
        )
        return _response.data

    def read_from_microstorage(
        self, id4n: str, organization: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Parameters
        ----------
        id4n : str
            id4n

        organization : str
            organization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.storage.read_from_microstorage(
            id4n="id4n",
            organization="organization",
        )
        """
        _response = self._raw_client.read_from_microstorage(id4n, organization, request_options=request_options)
        return _response.data

    def write_to_microstorage(
        self, id4n: str, organization: str, *, request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        id4n : str
            id4n

        organization : str
            organization

        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.storage.write_to_microstorage(
            id4n="id4n",
            organization="organization",
            request="string",
        )
        """
        _response = self._raw_client.write_to_microstorage(
            id4n, organization, request=request, request_options=request_options
        )
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

    async def list_all_documents(
        self,
        id4n: str,
        *,
        owner: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResponseOfDocument:
        """
        Listing all documents of an id4n

        Parameters
        ----------
        id4n : str
            id4n

        owner : typing.Optional[str]
            Filter by owner organization

        offset : typing.Optional[int]
            Start with the n-th element

        limit : typing.Optional[int]
            The maximum count of returned elements

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedResponseOfDocument
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.storage.list_all_documents(
                id4n="id4n",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_documents(
            id4n, owner=owner, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    async def list_documents(
        self,
        id4n: str,
        organization_id: str,
        *,
        owner: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResponseOfDocument:
        """
        Listing documents of an id4n seen by a specified organization

        Parameters
        ----------
        id4n : str
            id4n

        organization_id : str
            organizationId

        owner : typing.Optional[str]
            Filter by owner organization

        offset : typing.Optional[int]
            Start with the n-th element

        limit : typing.Optional[int]
            The maximum count of returned elements

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedResponseOfDocument
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.storage.list_documents(
                id4n="id4n",
                organization_id="organizationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_documents(
            id4n, organization_id, owner=owner, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    async def create_document(
        self,
        id4n: str,
        organization_id: str,
        *,
        content: core.File,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Document:
        """
        The documents' mime type is suggested on octet-stream data. Otherwise the specified content mime type is used.

        Parameters
        ----------
        id4n : str
            id4n

        organization_id : str
            organizationId

        content : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Document
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.storage.create_document(
                id4n="id4n",
                organization_id="organizationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_document(
            id4n, organization_id, content=content, request_options=request_options
        )
        return _response.data

    async def put_document(
        self,
        id4n: str,
        organization_id: str,
        *,
        content: core.File,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Document:
        """
        Creating or overwriting an existing document

        Parameters
        ----------
        id4n : str
            id4n

        organization_id : str
            organizationId

        content : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Document
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.storage.put_document(
                id4n="id4n",
                organization_id="organizationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_document(
            id4n, organization_id, content=content, request_options=request_options
        )
        return _response.data

    async def read_document(
        self,
        id4n: str,
        organization_id: str,
        file_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Parameters
        ----------
        id4n : str
            id4n

        organization_id : str
            organizationId

        file_name : str
            fileName

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.storage.read_document(
                id4n="id4n",
                organization_id="organizationId",
                file_name="fileName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_document(
            id4n, organization_id, file_name, request_options=request_options
        )
        return _response.data

    async def delete_document(
        self,
        id4n: str,
        organization_id: str,
        file_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id4n : str
            id4n

        organization_id : str
            organizationId

        file_name : str
            fileName

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
            await client.storage.delete_document(
                id4n="id4n",
                organization_id="organizationId",
                file_name="fileName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_document(
            id4n, organization_id, file_name, request_options=request_options
        )
        return _response.data

    async def get_document(
        self,
        id4n: str,
        organization_id: str,
        file_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Document:
        """
        Parameters
        ----------
        id4n : str
            id4n

        organization_id : str
            organizationId

        file_name : str
            fileName

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Document
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.storage.get_document(
                id4n="id4n",
                organization_id="organizationId",
                file_name="fileName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_document(
            id4n, organization_id, file_name, request_options=request_options
        )
        return _response.data

    async def update_document_metadata(
        self,
        id4n: str,
        organization_id: str,
        file_name: str,
        *,
        filename: typing.Optional[str] = OMIT,
        mime_type: typing.Optional[str] = OMIT,
        visibility: typing.Optional[VisibilityUpdate] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[Document]:
        """
        Parameters
        ----------
        id4n : str
            id4n

        organization_id : str
            organizationId

        file_name : str
            fileName

        filename : typing.Optional[str]
            File Name

        mime_type : typing.Optional[str]
            Mime Type

        visibility : typing.Optional[VisibilityUpdate]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[Document]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.storage.update_document_metadata(
                id4n="id4n",
                organization_id="organizationId",
                file_name="fileName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_document_metadata(
            id4n,
            organization_id,
            file_name,
            filename=filename,
            mime_type=mime_type,
            visibility=visibility,
            request_options=request_options,
        )
        return _response.data

    async def read_from_microstorage(
        self, id4n: str, organization: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Parameters
        ----------
        id4n : str
            id4n

        organization : str
            organization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.storage.read_from_microstorage(
                id4n="id4n",
                organization="organization",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_from_microstorage(id4n, organization, request_options=request_options)
        return _response.data

    async def write_to_microstorage(
        self, id4n: str, organization: str, *, request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        id4n : str
            id4n

        organization : str
            organization

        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.storage.write_to_microstorage(
                id4n="id4n",
                organization="organization",
                request="string",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_to_microstorage(
            id4n, organization, request=request, request_options=request_options
        )
        return _response.data

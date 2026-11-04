

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.document import Document
from ..types.organization import Organization
from ..types.paginated_response_of_document import PaginatedResponseOfDocument
from ..types.paginated_response_of_history_item import PaginatedResponseOfHistoryItem
from ..types.route import Route
from ..types.who_is_response import WhoIsResponse
from .raw_client import AsyncRawPublicServicesClient, RawPublicServicesClient


class PublicServicesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPublicServicesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPublicServicesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPublicServicesClient
        """
        return self._raw_client

    def list_all_public_documents(
        self,
        id4n: str,
        *,
        organization_id: typing.Optional[str] = None,
        owner: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResponseOfDocument:
        """
        Listing all public documents of an id4n

        Parameters
        ----------
        id4n : str
            id4n

        organization_id : typing.Optional[str]
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
        client.public_services.list_all_public_documents(
            id4n="id4n",
        )
        """
        _response = self._raw_client.list_all_public_documents(
            id4n,
            organization_id=organization_id,
            owner=owner,
            offset=offset,
            limit=limit,
            request_options=request_options,
        )
        return _response.data

    def read_public_document(
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
        client.public_services.read_public_document(
            id4n="id4n",
            organization_id="organizationId",
            file_name="fileName",
        )
        """
        _response = self._raw_client.read_public_document(
            id4n, organization_id, file_name, request_options=request_options
        )
        return _response.data

    def get_public_document(
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
        client.public_services.get_public_document(
            id4n="id4n",
            organization_id="organizationId",
            file_name="fileName",
        )
        """
        _response = self._raw_client.get_public_document(
            id4n, organization_id, file_name, request_options=request_options
        )
        return _response.data

    def list_public_history(
        self,
        id4n: str,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResponseOfHistoryItem:
        """
        Only contains public history items

        Parameters
        ----------
        id4n : str
            GUID to retrieve the history for

        offset : typing.Optional[int]
            Start with the n-th element

        limit : typing.Optional[int]
            The maximum count of returned elements

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedResponseOfHistoryItem
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.public_services.list_public_history(
            id4n="id4n",
        )
        """
        _response = self._raw_client.list_public_history(
            id4n, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    def read_organization_info(
        self, organization_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Organization:
        """
        Parameters
        ----------
        organization_id : str
            Organization ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Organization
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.public_services.read_organization_info(
            organization_id="organizationId",
        )
        """
        _response = self._raw_client.read_organization_info(organization_id, request_options=request_options)
        return _response.data

    def get_routes(
        self,
        id4n: str,
        *,
        type: str,
        interpolate: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Route]:
        """
        Parameters
        ----------
        id4n : str
            id4n

        type : str
            type

        interpolate : typing.Optional[bool]
            interpolate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Route]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.public_services.get_routes(
            id4n="id4n",
            type="type",
        )
        """
        _response = self._raw_client.get_routes(
            id4n, type=type, interpolate=interpolate, request_options=request_options
        )
        return _response.data

    def go(self, guid: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Forwarding to the designated route defined in the routing,

        Parameters
        ----------
        guid : str
            guid

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
        client.public_services.go(
            guid="guid",
        )
        """
        _response = self._raw_client.go(guid, request_options=request_options)
        return _response.data

    def resolve_who_is_entry(
        self, id4n: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WhoIsResponse:
        """
        Parameters
        ----------
        id4n : str
            id4n

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WhoIsResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.public_services.resolve_who_is_entry(
            id4n="id4n",
        )
        """
        _response = self._raw_client.resolve_who_is_entry(id4n, request_options=request_options)
        return _response.data


class AsyncPublicServicesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPublicServicesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPublicServicesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPublicServicesClient
        """
        return self._raw_client

    async def list_all_public_documents(
        self,
        id4n: str,
        *,
        organization_id: typing.Optional[str] = None,
        owner: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResponseOfDocument:
        """
        Listing all public documents of an id4n

        Parameters
        ----------
        id4n : str
            id4n

        organization_id : typing.Optional[str]
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
            await client.public_services.list_all_public_documents(
                id4n="id4n",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_public_documents(
            id4n,
            organization_id=organization_id,
            owner=owner,
            offset=offset,
            limit=limit,
            request_options=request_options,
        )
        return _response.data

    async def read_public_document(
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
            await client.public_services.read_public_document(
                id4n="id4n",
                organization_id="organizationId",
                file_name="fileName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_public_document(
            id4n, organization_id, file_name, request_options=request_options
        )
        return _response.data

    async def get_public_document(
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
            await client.public_services.get_public_document(
                id4n="id4n",
                organization_id="organizationId",
                file_name="fileName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_public_document(
            id4n, organization_id, file_name, request_options=request_options
        )
        return _response.data

    async def list_public_history(
        self,
        id4n: str,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResponseOfHistoryItem:
        """
        Only contains public history items

        Parameters
        ----------
        id4n : str
            GUID to retrieve the history for

        offset : typing.Optional[int]
            Start with the n-th element

        limit : typing.Optional[int]
            The maximum count of returned elements

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedResponseOfHistoryItem
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.public_services.list_public_history(
                id4n="id4n",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_public_history(
            id4n, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    async def read_organization_info(
        self, organization_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Organization:
        """
        Parameters
        ----------
        organization_id : str
            Organization ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Organization
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.public_services.read_organization_info(
                organization_id="organizationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_organization_info(organization_id, request_options=request_options)
        return _response.data

    async def get_routes(
        self,
        id4n: str,
        *,
        type: str,
        interpolate: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Route]:
        """
        Parameters
        ----------
        id4n : str
            id4n

        type : str
            type

        interpolate : typing.Optional[bool]
            interpolate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Route]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.public_services.get_routes(
                id4n="id4n",
                type="type",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_routes(
            id4n, type=type, interpolate=interpolate, request_options=request_options
        )
        return _response.data

    async def go(self, guid: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Forwarding to the designated route defined in the routing,

        Parameters
        ----------
        guid : str
            guid

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
            await client.public_services.go(
                guid="guid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.go(guid, request_options=request_options)
        return _response.data

    async def resolve_who_is_entry(
        self, id4n: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WhoIsResponse:
        """
        Parameters
        ----------
        id4n : str
            id4n

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WhoIsResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.public_services.resolve_who_is_entry(
                id4n="id4n",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.resolve_who_is_entry(id4n, request_options=request_options)
        return _response.data

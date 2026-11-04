

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.guid import Guid
from ..types.guid_physical_state import GuidPhysicalState
from ..types.id4n_presentation import Id4NPresentation
from ..types.list_of_gs1s import ListOfGs1S
from ..types.list_of_id4ns import ListOfId4Ns
from ..types.paginated_response_of_guid import PaginatedResponseOfGuid
from ..types.paginated_response_of_guid_collection import PaginatedResponseOfGuidCollection
from .raw_client import AsyncRawGuidsClient, RawGuidsClient


OMIT = typing.cast(typing.Any, ...)


class GuidsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawGuidsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawGuidsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawGuidsClient
        """
        return self._raw_client

    def create_guid(
        self, *, count: int, length: int, organization_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ListOfId4Ns:
        """
        Creating one or more GUIDs with a specified length.

        Parameters
        ----------
        count : int
            The total number of GUIDs to create

        length : int
            The charactersequence length of the GUID

        organization_id : str
            The namespace of the organization where the generated GUIDs should be assigned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListOfId4Ns
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.guids.create_guid(
            count=1,
            length=40,
            organization_id="de.acme",
        )
        """
        _response = self._raw_client.create_guid(
            count=count, length=length, organization_id=organization_id, request_options=request_options
        )
        return _response.data

    def get_guids_without_collection(
        self,
        *,
        organization_id: str,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResponseOfGuid:
        """
        Parameters
        ----------
        organization_id : str
            The namespace of the organization to search GUIDs for

        offset : typing.Optional[int]
            Start with the n-th element

        limit : typing.Optional[int]
            The maximum count of returned elements

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedResponseOfGuid
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.guids.get_guids_without_collection(
            organization_id="organizationId",
        )
        """
        _response = self._raw_client.get_guids_without_collection(
            organization_id=organization_id, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    def get_guid(
        self,
        id4n: str,
        *,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Guid:
        """
        Parameters
        ----------
        id4n : str
            The GUID number

        organization_id : typing.Optional[str]
            The organization namespace to resolve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Guid
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.guids.get_guid(
            id4n="id4n",
        )
        """
        _response = self._raw_client.get_guid(id4n, organization_id=organization_id, request_options=request_options)
        return _response.data

    def update_guid(
        self,
        id4n_: str,
        *,
        created_timestamp: typing.Optional[int] = OMIT,
        holder_organization_id: typing.Optional[str] = OMIT,
        id4n: typing.Optional[str] = OMIT,
        owner_organization_id: typing.Optional[str] = OMIT,
        physical_state: typing.Optional[GuidPhysicalState] = OMIT,
        properties: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[typing.Dict[str, typing.Any]]:
        """
        Allows ownership transfer.

        Parameters
        ----------
        id4n_ : str
            The GUID number

        created_timestamp : typing.Optional[int]
            The UTC unix timestamp of when this GUID has been created

        holder_organization_id : typing.Optional[str]
            Organization namespace of the GUID holder

        id4n : typing.Optional[str]
            The ID

        owner_organization_id : typing.Optional[str]
            Organization namespace of the GUID owner

        physical_state : typing.Optional[GuidPhysicalState]
            Physical attachment state of the GUID

        properties : typing.Optional[typing.Dict[str, str]]
            The properties of the organization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.Dict[str, typing.Any]]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.guids.update_guid(
            id4n_="id4n",
        )
        """
        _response = self._raw_client.update_guid(
            id4n_,
            created_timestamp=created_timestamp,
            holder_organization_id=holder_organization_id,
            id4n=id4n,
            owner_organization_id=owner_organization_id,
            physical_state=physical_state,
            properties=properties,
            request_options=request_options,
        )
        return _response.data

    def get_id4n(
        self,
        id4n: str,
        *,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Id4NPresentation:
        """
        Retrieving basic information about an ID like the type and the creation time.

        Parameters
        ----------
        id4n : str
            The ID to resolve to

        organization_id : typing.Optional[str]
            The organization namespace to resolve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Id4NPresentation
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.guids.get_id4n(
            id4n="id4n",
        )
        """
        _response = self._raw_client.get_id4n(id4n, organization_id=organization_id, request_options=request_options)
        return _response.data

    def get_collections(
        self,
        id4n: str,
        *,
        organization_id: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResponseOfGuidCollection:
        """
        Retrieving all owned or holding collections the specified id4n is assigned to.

        Parameters
        ----------
        id4n : str
            The ID which the collections should contain

        organization_id : typing.Optional[str]
            The organization holding the collections.

        offset : typing.Optional[int]
            Start with the n-th element

        limit : typing.Optional[int]
            The maximum count of returned elements

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedResponseOfGuidCollection
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.guids.get_collections(
            id4n="id4n",
        )
        """
        _response = self._raw_client.get_collections(
            id4n, organization_id=organization_id, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    def import_gs1codes(
        self, *, list_of_gs1s: ListOfGs1S, organization_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Importing GS1/MAPP codes that contain unique components.

        Parameters
        ----------
        list_of_gs1s : ListOfGs1S

        organization_id : str
            The organization where the GS1/Mapp code is imported.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, ListOfGs1S

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.guids.import_gs1codes(
            list_of_gs1s=ListOfGs1S(),
            organization_id="de.acme",
        )
        """
        _response = self._raw_client.import_gs1codes(
            list_of_gs1s=list_of_gs1s, organization_id=organization_id, request_options=request_options
        )
        return _response.data


class AsyncGuidsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawGuidsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawGuidsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawGuidsClient
        """
        return self._raw_client

    async def create_guid(
        self, *, count: int, length: int, organization_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ListOfId4Ns:
        """
        Creating one or more GUIDs with a specified length.

        Parameters
        ----------
        count : int
            The total number of GUIDs to create

        length : int
            The charactersequence length of the GUID

        organization_id : str
            The namespace of the organization where the generated GUIDs should be assigned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListOfId4Ns
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.guids.create_guid(
                count=1,
                length=40,
                organization_id="de.acme",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_guid(
            count=count, length=length, organization_id=organization_id, request_options=request_options
        )
        return _response.data

    async def get_guids_without_collection(
        self,
        *,
        organization_id: str,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResponseOfGuid:
        """
        Parameters
        ----------
        organization_id : str
            The namespace of the organization to search GUIDs for

        offset : typing.Optional[int]
            Start with the n-th element

        limit : typing.Optional[int]
            The maximum count of returned elements

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedResponseOfGuid
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.guids.get_guids_without_collection(
                organization_id="organizationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_guids_without_collection(
            organization_id=organization_id, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    async def get_guid(
        self,
        id4n: str,
        *,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Guid:
        """
        Parameters
        ----------
        id4n : str
            The GUID number

        organization_id : typing.Optional[str]
            The organization namespace to resolve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Guid
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.guids.get_guid(
                id4n="id4n",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_guid(
            id4n, organization_id=organization_id, request_options=request_options
        )
        return _response.data

    async def update_guid(
        self,
        id4n_: str,
        *,
        created_timestamp: typing.Optional[int] = OMIT,
        holder_organization_id: typing.Optional[str] = OMIT,
        id4n: typing.Optional[str] = OMIT,
        owner_organization_id: typing.Optional[str] = OMIT,
        physical_state: typing.Optional[GuidPhysicalState] = OMIT,
        properties: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[typing.Dict[str, typing.Any]]:
        """
        Allows ownership transfer.

        Parameters
        ----------
        id4n_ : str
            The GUID number

        created_timestamp : typing.Optional[int]
            The UTC unix timestamp of when this GUID has been created

        holder_organization_id : typing.Optional[str]
            Organization namespace of the GUID holder

        id4n : typing.Optional[str]
            The ID

        owner_organization_id : typing.Optional[str]
            Organization namespace of the GUID owner

        physical_state : typing.Optional[GuidPhysicalState]
            Physical attachment state of the GUID

        properties : typing.Optional[typing.Dict[str, str]]
            The properties of the organization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.Dict[str, typing.Any]]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.guids.update_guid(
                id4n_="id4n",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_guid(
            id4n_,
            created_timestamp=created_timestamp,
            holder_organization_id=holder_organization_id,
            id4n=id4n,
            owner_organization_id=owner_organization_id,
            physical_state=physical_state,
            properties=properties,
            request_options=request_options,
        )
        return _response.data

    async def get_id4n(
        self,
        id4n: str,
        *,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Id4NPresentation:
        """
        Retrieving basic information about an ID like the type and the creation time.

        Parameters
        ----------
        id4n : str
            The ID to resolve to

        organization_id : typing.Optional[str]
            The organization namespace to resolve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Id4NPresentation
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.guids.get_id4n(
                id4n="id4n",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_id4n(
            id4n, organization_id=organization_id, request_options=request_options
        )
        return _response.data

    async def get_collections(
        self,
        id4n: str,
        *,
        organization_id: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResponseOfGuidCollection:
        """
        Retrieving all owned or holding collections the specified id4n is assigned to.

        Parameters
        ----------
        id4n : str
            The ID which the collections should contain

        organization_id : typing.Optional[str]
            The organization holding the collections.

        offset : typing.Optional[int]
            Start with the n-th element

        limit : typing.Optional[int]
            The maximum count of returned elements

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedResponseOfGuidCollection
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.guids.get_collections(
                id4n="id4n",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_collections(
            id4n, organization_id=organization_id, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    async def import_gs1codes(
        self, *, list_of_gs1s: ListOfGs1S, organization_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Importing GS1/MAPP codes that contain unique components.

        Parameters
        ----------
        list_of_gs1s : ListOfGs1S

        organization_id : str
            The organization where the GS1/Mapp code is imported.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ListOfGs1S

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.guids.import_gs1codes(
                list_of_gs1s=ListOfGs1S(),
                organization_id="de.acme",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.import_gs1codes(
            list_of_gs1s=list_of_gs1s, organization_id=organization_id, request_options=request_options
        )
        return _response.data

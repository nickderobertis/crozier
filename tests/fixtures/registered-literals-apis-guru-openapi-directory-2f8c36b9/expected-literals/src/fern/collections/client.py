

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.guid_collection import GuidCollection
from ..types.guid_collection_physical_state import GuidCollectionPhysicalState
from ..types.guid_collection_type import GuidCollectionType
from ..types.id4n import Id4N
from ..types.list_of_id4n_properties import ListOfId4NProperties
from ..types.paginated_response_of_guid import PaginatedResponseOfGuid
from ..types.paginated_response_of_guid_collection import PaginatedResponseOfGuidCollection
from .raw_client import AsyncRawCollectionsClient, RawCollectionsClient
from .types.create_collection_request_type import CreateCollectionRequestType
from .types.get_all_collections_of_organization_request_type import GetAllCollectionsOfOrganizationRequestType


OMIT = typing.cast(typing.Any, ...)


class CollectionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCollectionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCollectionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCollectionsClient
        """
        return self._raw_client

    def create_collection(
        self,
        *,
        length: int,
        organization_id: str,
        type: CreateCollectionRequestType,
        label: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Id4N:
        """
        Parameters
        ----------
        length : int

        organization_id : str

        type : CreateCollectionRequestType

        label : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Id4N
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.collections.create_collection(
            length=1,
            organization_id="de.acme",
            type="ROUTING_COLLECTION",
        )
        """
        _response = self._raw_client.create_collection(
            length=length, organization_id=organization_id, type=type, label=label, request_options=request_options
        )
        return _response.data

    def find_collection(self, id4n: str, *, request_options: typing.Optional[RequestOptions] = None) -> GuidCollection:
        """
        Parameters
        ----------
        id4n : str
            id4n

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuidCollection
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.collections.find_collection(
            id4n="id4n",
        )
        """
        _response = self._raw_client.find_collection(id4n, request_options=request_options)
        return _response.data

    def delete_collection(self, id4n: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id4n : str
            id4n

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
        client.collections.delete_collection(
            id4n="id4n",
        )
        """
        _response = self._raw_client.delete_collection(id4n, request_options=request_options)
        return _response.data

    def update_collection(
        self,
        id4n_: str,
        *,
        created_timestamp: typing.Optional[int] = OMIT,
        holder_organization_id: typing.Optional[str] = OMIT,
        id4n: typing.Optional[str] = OMIT,
        label: typing.Optional[str] = OMIT,
        owner_organization_id: typing.Optional[str] = OMIT,
        physical_state: typing.Optional[GuidCollectionPhysicalState] = OMIT,
        type: typing.Optional[GuidCollectionType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[typing.Dict[str, typing.Any]]:
        """
        Update collection changing only the given values

        Parameters
        ----------
        id4n_ : str
            id4n

        created_timestamp : typing.Optional[int]
            The UTC unix timestamp of when this collection has been created

        holder_organization_id : typing.Optional[str]
            Organization namespace of the holder of the collection

        id4n : typing.Optional[str]
            The ID

        label : typing.Optional[str]

        owner_organization_id : typing.Optional[str]
            Organization namespace of the collection owner

        physical_state : typing.Optional[GuidCollectionPhysicalState]
            Physical attachment state of the collection

        type : typing.Optional[GuidCollectionType]

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
        client.collections.update_collection(
            id4n_="id4n",
        )
        """
        _response = self._raw_client.update_collection(
            id4n_,
            created_timestamp=created_timestamp,
            holder_organization_id=holder_organization_id,
            id4n=id4n,
            label=label,
            owner_organization_id=owner_organization_id,
            physical_state=physical_state,
            type=type,
            request_options=request_options,
        )
        return _response.data

    def list_elements_of_collection(
        self,
        id4n: str,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResponseOfGuid:
        """
        Parameters
        ----------
        id4n : str
            id4n

        offset : typing.Optional[int]
            Start with the n-th element

        limit : typing.Optional[int]
            The maximum count of returned elements

        organization_id : typing.Optional[str]
            The organization namespace.

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
        client.collections.list_elements_of_collection(
            id4n="id4n",
        )
        """
        _response = self._raw_client.list_elements_of_collection(
            id4n, offset=offset, limit=limit, organization_id=organization_id, request_options=request_options
        )
        return _response.data

    def add_elements_to_collection(
        self,
        id4n: str,
        *,
        id4ns: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id4n : str
            id4n

        id4ns : typing.Optional[typing.Sequence[str]]
            A list of id4ns.

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
        client.collections.add_elements_to_collection(
            id4n="id4n",
        )
        """
        _response = self._raw_client.add_elements_to_collection(id4n, id4ns=id4ns, request_options=request_options)
        return _response.data

    def remove_elements_from_collection(
        self,
        id4n: str,
        *,
        id4ns: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id4n : str
            id4n

        id4ns : typing.Optional[typing.Sequence[str]]
            A list of id4ns.

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
        client.collections.remove_elements_from_collection(
            id4n="id4n",
        )
        """
        _response = self._raw_client.remove_elements_from_collection(id4n, id4ns=id4ns, request_options=request_options)
        return _response.data

    def get_properties(
        self,
        id4n: str,
        *,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, str]:
        """
        List all properties of an id4n.

        Parameters
        ----------
        id4n : str
            The id4n

        organization_id : typing.Optional[str]
            The organization namespace.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.collections.get_properties(
            id4n="id4n",
        )
        """
        _response = self._raw_client.get_properties(
            id4n, organization_id=organization_id, request_options=request_options
        )
        return _response.data

    def delete_properties(
        self,
        id4n: str,
        *,
        organization_id: str,
        request: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Partial deletion of id4n properties. If the property does not exist, it will be ignored.

        Parameters
        ----------
        id4n : str
            The id4n

        organization_id : str
            The organization namespace to work on while deleting the properties.

        request : typing.Sequence[str]

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
        client.collections.delete_properties(
            id4n="id4n",
            organization_id="organizationId",
            request=["string"],
        )
        """
        _response = self._raw_client.delete_properties(
            id4n, organization_id=organization_id, request=request, request_options=request_options
        )
        return _response.data

    def patch_properties(
        self,
        id4n: str,
        *,
        organization_id: str,
        request: typing.Dict[str, str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Partial updating of id4n properties. If a property contains a null value the property will be deleted other values will be saved and overwritten if they already exist.

        Parameters
        ----------
        id4n : str
            The id4n

        organization_id : str
            The organization namespace to work on while patching the properties.

        request : typing.Dict[str, str]

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
        client.collections.patch_properties(
            id4n="id4n",
            organization_id="organizationId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.patch_properties(
            id4n, organization_id=organization_id, request=request, request_options=request_options
        )
        return _response.data

    def get_multiple_properties(
        self,
        *,
        id4ns: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListOfId4NProperties:
        """
        Get a list of ID4n properties for the specified ID4ns.

        Parameters
        ----------
        id4ns : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The list of ID4ns to resolve.

        organization_id : typing.Optional[str]
            The organization namespace.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListOfId4NProperties
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.collections.get_multiple_properties(
            id4ns=["id4ns"],
        )
        """
        _response = self._raw_client.get_multiple_properties(
            id4ns=id4ns, organization_id=organization_id, request_options=request_options
        )
        return _response.data

    def get_all_collections_of_organization(
        self,
        organization_id: str,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        type: typing.Optional[GetAllCollectionsOfOrganizationRequestType] = None,
        label: typing.Optional[str] = None,
        label_prefix: typing.Optional[str] = None,
        property: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResponseOfGuidCollection:
        """
        Retrieving all collections of an organization in a paginated manner. You may filter the results by specifying id4n properties with filter operations (eq, in, ne) in the query parameters. e.g. `com.yourcompany.orderId.eq=1234`

        Parameters
        ----------
        organization_id : str
            The namespace of the organization

        offset : typing.Optional[int]
            Start with the n-th element

        limit : typing.Optional[int]
            The maximum count of returned elements

        type : typing.Optional[GetAllCollectionsOfOrganizationRequestType]
            Filter by this type

        label : typing.Optional[str]
            Filter by this label

        label_prefix : typing.Optional[str]
            Filter by this label prefix

        property : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            List of i4dn property filter. e.g. "com.myorga.state:IN:waiting|processing" or "com.myorga.orderId:EQ:SAP001"

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
        client.collections.get_all_collections_of_organization(
            organization_id="organizationId",
        )
        """
        _response = self._raw_client.get_all_collections_of_organization(
            organization_id,
            offset=offset,
            limit=limit,
            type=type,
            label=label,
            label_prefix=label_prefix,
            property=property,
            request_options=request_options,
        )
        return _response.data


class AsyncCollectionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCollectionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCollectionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCollectionsClient
        """
        return self._raw_client

    async def create_collection(
        self,
        *,
        length: int,
        organization_id: str,
        type: CreateCollectionRequestType,
        label: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Id4N:
        """
        Parameters
        ----------
        length : int

        organization_id : str

        type : CreateCollectionRequestType

        label : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Id4N
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.collections.create_collection(
                length=1,
                organization_id="de.acme",
                type="ROUTING_COLLECTION",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_collection(
            length=length, organization_id=organization_id, type=type, label=label, request_options=request_options
        )
        return _response.data

    async def find_collection(
        self, id4n: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GuidCollection:
        """
        Parameters
        ----------
        id4n : str
            id4n

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuidCollection
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.collections.find_collection(
                id4n="id4n",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.find_collection(id4n, request_options=request_options)
        return _response.data

    async def delete_collection(self, id4n: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id4n : str
            id4n

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
            await client.collections.delete_collection(
                id4n="id4n",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_collection(id4n, request_options=request_options)
        return _response.data

    async def update_collection(
        self,
        id4n_: str,
        *,
        created_timestamp: typing.Optional[int] = OMIT,
        holder_organization_id: typing.Optional[str] = OMIT,
        id4n: typing.Optional[str] = OMIT,
        label: typing.Optional[str] = OMIT,
        owner_organization_id: typing.Optional[str] = OMIT,
        physical_state: typing.Optional[GuidCollectionPhysicalState] = OMIT,
        type: typing.Optional[GuidCollectionType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[typing.Dict[str, typing.Any]]:
        """
        Update collection changing only the given values

        Parameters
        ----------
        id4n_ : str
            id4n

        created_timestamp : typing.Optional[int]
            The UTC unix timestamp of when this collection has been created

        holder_organization_id : typing.Optional[str]
            Organization namespace of the holder of the collection

        id4n : typing.Optional[str]
            The ID

        label : typing.Optional[str]

        owner_organization_id : typing.Optional[str]
            Organization namespace of the collection owner

        physical_state : typing.Optional[GuidCollectionPhysicalState]
            Physical attachment state of the collection

        type : typing.Optional[GuidCollectionType]

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
            await client.collections.update_collection(
                id4n_="id4n",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_collection(
            id4n_,
            created_timestamp=created_timestamp,
            holder_organization_id=holder_organization_id,
            id4n=id4n,
            label=label,
            owner_organization_id=owner_organization_id,
            physical_state=physical_state,
            type=type,
            request_options=request_options,
        )
        return _response.data

    async def list_elements_of_collection(
        self,
        id4n: str,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResponseOfGuid:
        """
        Parameters
        ----------
        id4n : str
            id4n

        offset : typing.Optional[int]
            Start with the n-th element

        limit : typing.Optional[int]
            The maximum count of returned elements

        organization_id : typing.Optional[str]
            The organization namespace.

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
            await client.collections.list_elements_of_collection(
                id4n="id4n",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_elements_of_collection(
            id4n, offset=offset, limit=limit, organization_id=organization_id, request_options=request_options
        )
        return _response.data

    async def add_elements_to_collection(
        self,
        id4n: str,
        *,
        id4ns: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id4n : str
            id4n

        id4ns : typing.Optional[typing.Sequence[str]]
            A list of id4ns.

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
            await client.collections.add_elements_to_collection(
                id4n="id4n",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_elements_to_collection(
            id4n, id4ns=id4ns, request_options=request_options
        )
        return _response.data

    async def remove_elements_from_collection(
        self,
        id4n: str,
        *,
        id4ns: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id4n : str
            id4n

        id4ns : typing.Optional[typing.Sequence[str]]
            A list of id4ns.

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
            await client.collections.remove_elements_from_collection(
                id4n="id4n",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_elements_from_collection(
            id4n, id4ns=id4ns, request_options=request_options
        )
        return _response.data

    async def get_properties(
        self,
        id4n: str,
        *,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, str]:
        """
        List all properties of an id4n.

        Parameters
        ----------
        id4n : str
            The id4n

        organization_id : typing.Optional[str]
            The organization namespace.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.collections.get_properties(
                id4n="id4n",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_properties(
            id4n, organization_id=organization_id, request_options=request_options
        )
        return _response.data

    async def delete_properties(
        self,
        id4n: str,
        *,
        organization_id: str,
        request: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Partial deletion of id4n properties. If the property does not exist, it will be ignored.

        Parameters
        ----------
        id4n : str
            The id4n

        organization_id : str
            The organization namespace to work on while deleting the properties.

        request : typing.Sequence[str]

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
            await client.collections.delete_properties(
                id4n="id4n",
                organization_id="organizationId",
                request=["string"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_properties(
            id4n, organization_id=organization_id, request=request, request_options=request_options
        )
        return _response.data

    async def patch_properties(
        self,
        id4n: str,
        *,
        organization_id: str,
        request: typing.Dict[str, str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Partial updating of id4n properties. If a property contains a null value the property will be deleted other values will be saved and overwritten if they already exist.

        Parameters
        ----------
        id4n : str
            The id4n

        organization_id : str
            The organization namespace to work on while patching the properties.

        request : typing.Dict[str, str]

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
            await client.collections.patch_properties(
                id4n="id4n",
                organization_id="organizationId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_properties(
            id4n, organization_id=organization_id, request=request, request_options=request_options
        )
        return _response.data

    async def get_multiple_properties(
        self,
        *,
        id4ns: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListOfId4NProperties:
        """
        Get a list of ID4n properties for the specified ID4ns.

        Parameters
        ----------
        id4ns : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The list of ID4ns to resolve.

        organization_id : typing.Optional[str]
            The organization namespace.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListOfId4NProperties
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.collections.get_multiple_properties(
                id4ns=["id4ns"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_multiple_properties(
            id4ns=id4ns, organization_id=organization_id, request_options=request_options
        )
        return _response.data

    async def get_all_collections_of_organization(
        self,
        organization_id: str,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        type: typing.Optional[GetAllCollectionsOfOrganizationRequestType] = None,
        label: typing.Optional[str] = None,
        label_prefix: typing.Optional[str] = None,
        property: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResponseOfGuidCollection:
        """
        Retrieving all collections of an organization in a paginated manner. You may filter the results by specifying id4n properties with filter operations (eq, in, ne) in the query parameters. e.g. `com.yourcompany.orderId.eq=1234`

        Parameters
        ----------
        organization_id : str
            The namespace of the organization

        offset : typing.Optional[int]
            Start with the n-th element

        limit : typing.Optional[int]
            The maximum count of returned elements

        type : typing.Optional[GetAllCollectionsOfOrganizationRequestType]
            Filter by this type

        label : typing.Optional[str]
            Filter by this label

        label_prefix : typing.Optional[str]
            Filter by this label prefix

        property : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            List of i4dn property filter. e.g. "com.myorga.state:IN:waiting|processing" or "com.myorga.orderId:EQ:SAP001"

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
            await client.collections.get_all_collections_of_organization(
                organization_id="organizationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_all_collections_of_organization(
            organization_id,
            offset=offset,
            limit=limit,
            type=type,
            label=label,
            label_prefix=label_prefix,
            property=property,
            request_options=request_options,
        )
        return _response.data

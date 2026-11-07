

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.paginated_response_of_guid import PaginatedResponseOfGuid
from .raw_client import AsyncRawAliasClient, RawAliasClient
from .types.add_guid_alias_request_alias_type import AddGuidAliasRequestAliasType
from .types.get_guid_alias_types_response_item import GetGuidAliasTypesResponseItem
from .types.remove_guid_alias_request_alias_type import RemoveGuidAliasRequestAliasType
from .types.search_by_alias_request_alias_type import SearchByAliasRequestAliasType


OMIT = typing.cast(typing.Any, ...)


class AliasClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAliasClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAliasClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAliasClient
        """
        return self._raw_client

    def get_guid_aliases(
        self, id4n: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Looks up the alias for each alias type (group and single) and returns a map of all aliases found.

        Parameters
        ----------
        id4n : str
            The GUID or Collection to operate on

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
        client.alias.get_guid_aliases(
            id4n="id4n",
        )
        """
        _response = self._raw_client.get_guid_aliases(id4n, request_options=request_options)
        return _response.data

    def add_guid_alias(
        self,
        id4n: str,
        alias_type: AddGuidAliasRequestAliasType,
        *,
        alias: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Adds or replaces aliases for single ID4ns (alias type item and mapp) or groups of ID4ns (alias types gtin, ean and article)

        Parameters
        ----------
        id4n : str
            The GUID or Collection to operate on

        alias_type : AddGuidAliasRequestAliasType
            Alias type, see the corresponding API model

        alias : str
            An alias

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
        client.alias.add_guid_alias(
            id4n="id4n",
            alias_type="gtin",
            alias="alias",
        )
        """
        _response = self._raw_client.add_guid_alias(id4n, alias_type, alias=alias, request_options=request_options)
        return _response.data

    def remove_guid_alias(
        self,
        id4n: str,
        alias_type: RemoveGuidAliasRequestAliasType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Remove the alias of the given type

        Parameters
        ----------
        id4n : str
            The GUID or Collection to operate on

        alias_type : RemoveGuidAliasRequestAliasType
            Alias type, see the corresponding API model

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
        client.alias.remove_guid_alias(
            id4n="id4n",
            alias_type="gtin",
        )
        """
        _response = self._raw_client.remove_guid_alias(id4n, alias_type, request_options=request_options)
        return _response.data

    def search_by_alias(
        self,
        *,
        alias: str,
        alias_type: SearchByAliasRequestAliasType,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResponseOfGuid:
        """
        Parameters
        ----------
        alias : str
            The alias to search for

        alias_type : SearchByAliasRequestAliasType
            Alias type type to search for

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
        client.alias.search_by_alias(
            alias="alias",
            alias_type="gtin",
        )
        """
        _response = self._raw_client.search_by_alias(
            alias=alias, alias_type=alias_type, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    def get_guid_alias_types(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GetGuidAliasTypesResponseItem]:
        """
        Retrieve this list to find out all alias types to use with alias search and change operations

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GetGuidAliasTypesResponseItem]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.alias.get_guid_alias_types()
        """
        _response = self._raw_client.get_guid_alias_types(request_options=request_options)
        return _response.data


class AsyncAliasClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAliasClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAliasClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAliasClient
        """
        return self._raw_client

    async def get_guid_aliases(
        self, id4n: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Looks up the alias for each alias type (group and single) and returns a map of all aliases found.

        Parameters
        ----------
        id4n : str
            The GUID or Collection to operate on

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
            await client.alias.get_guid_aliases(
                id4n="id4n",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_guid_aliases(id4n, request_options=request_options)
        return _response.data

    async def add_guid_alias(
        self,
        id4n: str,
        alias_type: AddGuidAliasRequestAliasType,
        *,
        alias: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Adds or replaces aliases for single ID4ns (alias type item and mapp) or groups of ID4ns (alias types gtin, ean and article)

        Parameters
        ----------
        id4n : str
            The GUID or Collection to operate on

        alias_type : AddGuidAliasRequestAliasType
            Alias type, see the corresponding API model

        alias : str
            An alias

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
            await client.alias.add_guid_alias(
                id4n="id4n",
                alias_type="gtin",
                alias="alias",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_guid_alias(
            id4n, alias_type, alias=alias, request_options=request_options
        )
        return _response.data

    async def remove_guid_alias(
        self,
        id4n: str,
        alias_type: RemoveGuidAliasRequestAliasType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Remove the alias of the given type

        Parameters
        ----------
        id4n : str
            The GUID or Collection to operate on

        alias_type : RemoveGuidAliasRequestAliasType
            Alias type, see the corresponding API model

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
            await client.alias.remove_guid_alias(
                id4n="id4n",
                alias_type="gtin",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_guid_alias(id4n, alias_type, request_options=request_options)
        return _response.data

    async def search_by_alias(
        self,
        *,
        alias: str,
        alias_type: SearchByAliasRequestAliasType,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResponseOfGuid:
        """
        Parameters
        ----------
        alias : str
            The alias to search for

        alias_type : SearchByAliasRequestAliasType
            Alias type type to search for

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
            await client.alias.search_by_alias(
                alias="alias",
                alias_type="gtin",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.search_by_alias(
            alias=alias, alias_type=alias_type, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    async def get_guid_alias_types(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GetGuidAliasTypesResponseItem]:
        """
        Retrieve this list to find out all alias types to use with alias search and change operations

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GetGuidAliasTypesResponseItem]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.alias.get_guid_alias_types()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_guid_alias_types(request_options=request_options)
        return _response.data

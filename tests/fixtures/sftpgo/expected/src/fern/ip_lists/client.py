

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_response import ApiResponse
from ..types.ip_list_entry import IpListEntry
from ..types.ip_list_mode import IpListMode
from ..types.ip_list_type import IpListType
from .raw_client import AsyncRawIpListsClient, RawIpListsClient
from .types.get_ip_list_entries_request_order import GetIpListEntriesRequestOrder


OMIT = typing.cast(typing.Any, ...)


class IpListsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawIpListsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawIpListsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawIpListsClient
        """
        return self._raw_client

    def get_ip_list_entries(
        self,
        type: IpListType,
        *,
        filter: typing.Optional[str] = None,
        from_: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[GetIpListEntriesRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[IpListEntry]:
        """
        Returns an array with one or more IP list entry

        Parameters
        ----------
        type : IpListType
            IP list type

        filter : typing.Optional[str]
            restrict results to ipornet matching or starting with this filter

        from_ : typing.Optional[str]
            ipornet to start from

        limit : typing.Optional[int]
            The maximum number of items to return. Max value is 500, default is 100

        order : typing.Optional[GetIpListEntriesRequestOrder]
            Ordering entries by ipornet field. Default ASC

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[IpListEntry]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.ip_lists.get_ip_list_entries(
            type=1,
        )
        """
        _response = self._raw_client.get_ip_list_entries(
            type, filter=filter, from_=from_, limit=limit, order=order, request_options=request_options
        )
        return _response.data

    def add_ip_list_entry(
        self,
        type_: IpListType,
        *,
        ipornet: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        type: typing.Optional[IpListType] = OMIT,
        mode: typing.Optional[IpListMode] = OMIT,
        protocols: typing.Optional[int] = OMIT,
        created_at: typing.Optional[int] = OMIT,
        updated_at: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        Add an IP address or a CIDR network to a supported list

        Parameters
        ----------
        type_ : IpListType
            IP list type

        ipornet : typing.Optional[str]
            IP address or network in CIDR format, for example `192.168.1.2/32`, `192.168.0.0/24`, `2001:db8::/32`

        description : typing.Optional[str]
            optional description

        type : typing.Optional[IpListType]

        mode : typing.Optional[IpListMode]

        protocols : typing.Optional[int]
            Defines the protocol the entry applies to. `0` means all the supported protocols, 1 SSH, 2 FTP, 4 WebDAV, 8 HTTP. Protocols can be combined, for example 3 means SSH and FTP

        created_at : typing.Optional[int]
            creation time as unix timestamp in milliseconds

        updated_at : typing.Optional[int]
            last update time as unix timestamp in millisecond

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
        client.ip_lists.add_ip_list_entry(
            type_=1,
        )
        """
        _response = self._raw_client.add_ip_list_entry(
            type_,
            ipornet=ipornet,
            description=description,
            type=type,
            mode=mode,
            protocols=protocols,
            created_at=created_at,
            updated_at=updated_at,
            request_options=request_options,
        )
        return _response.data

    def get_ip_list_by_ipornet(
        self, type: IpListType, ipornet: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> IpListEntry:
        """
        Returns the entry with the given ipornet if it exists.

        Parameters
        ----------
        type : IpListType
            IP list type

        ipornet : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IpListEntry
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.ip_lists.get_ip_list_by_ipornet(
            type=1,
            ipornet="ipornet",
        )
        """
        _response = self._raw_client.get_ip_list_by_ipornet(type, ipornet, request_options=request_options)
        return _response.data

    def update_ip_list_entry(
        self,
        type_: IpListType,
        ipornet_: str,
        *,
        ipornet: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        type: typing.Optional[IpListType] = OMIT,
        mode: typing.Optional[IpListMode] = OMIT,
        protocols: typing.Optional[int] = OMIT,
        created_at: typing.Optional[int] = OMIT,
        updated_at: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        Updates an existing IP list entry

        Parameters
        ----------
        type_ : IpListType
            IP list type

        ipornet_ : str

        ipornet : typing.Optional[str]
            IP address or network in CIDR format, for example `192.168.1.2/32`, `192.168.0.0/24`, `2001:db8::/32`

        description : typing.Optional[str]
            optional description

        type : typing.Optional[IpListType]

        mode : typing.Optional[IpListMode]

        protocols : typing.Optional[int]
            Defines the protocol the entry applies to. `0` means all the supported protocols, 1 SSH, 2 FTP, 4 WebDAV, 8 HTTP. Protocols can be combined, for example 3 means SSH and FTP

        created_at : typing.Optional[int]
            creation time as unix timestamp in milliseconds

        updated_at : typing.Optional[int]
            last update time as unix timestamp in millisecond

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
        client.ip_lists.update_ip_list_entry(
            type_=1,
            ipornet_="ipornet",
        )
        """
        _response = self._raw_client.update_ip_list_entry(
            type_,
            ipornet_,
            ipornet=ipornet,
            description=description,
            type=type,
            mode=mode,
            protocols=protocols,
            created_at=created_at,
            updated_at=updated_at,
            request_options=request_options,
        )
        return _response.data

    def delete_ip_list_entry(
        self, type: IpListType, ipornet: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiResponse:
        """
        Deletes an existing IP list entry

        Parameters
        ----------
        type : IpListType
            IP list type

        ipornet : str

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
        client.ip_lists.delete_ip_list_entry(
            type=1,
            ipornet="ipornet",
        )
        """
        _response = self._raw_client.delete_ip_list_entry(type, ipornet, request_options=request_options)
        return _response.data


class AsyncIpListsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawIpListsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawIpListsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawIpListsClient
        """
        return self._raw_client

    async def get_ip_list_entries(
        self,
        type: IpListType,
        *,
        filter: typing.Optional[str] = None,
        from_: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[GetIpListEntriesRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[IpListEntry]:
        """
        Returns an array with one or more IP list entry

        Parameters
        ----------
        type : IpListType
            IP list type

        filter : typing.Optional[str]
            restrict results to ipornet matching or starting with this filter

        from_ : typing.Optional[str]
            ipornet to start from

        limit : typing.Optional[int]
            The maximum number of items to return. Max value is 500, default is 100

        order : typing.Optional[GetIpListEntriesRequestOrder]
            Ordering entries by ipornet field. Default ASC

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[IpListEntry]
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
            await client.ip_lists.get_ip_list_entries(
                type=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_ip_list_entries(
            type, filter=filter, from_=from_, limit=limit, order=order, request_options=request_options
        )
        return _response.data

    async def add_ip_list_entry(
        self,
        type_: IpListType,
        *,
        ipornet: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        type: typing.Optional[IpListType] = OMIT,
        mode: typing.Optional[IpListMode] = OMIT,
        protocols: typing.Optional[int] = OMIT,
        created_at: typing.Optional[int] = OMIT,
        updated_at: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        Add an IP address or a CIDR network to a supported list

        Parameters
        ----------
        type_ : IpListType
            IP list type

        ipornet : typing.Optional[str]
            IP address or network in CIDR format, for example `192.168.1.2/32`, `192.168.0.0/24`, `2001:db8::/32`

        description : typing.Optional[str]
            optional description

        type : typing.Optional[IpListType]

        mode : typing.Optional[IpListMode]

        protocols : typing.Optional[int]
            Defines the protocol the entry applies to. `0` means all the supported protocols, 1 SSH, 2 FTP, 4 WebDAV, 8 HTTP. Protocols can be combined, for example 3 means SSH and FTP

        created_at : typing.Optional[int]
            creation time as unix timestamp in milliseconds

        updated_at : typing.Optional[int]
            last update time as unix timestamp in millisecond

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
            await client.ip_lists.add_ip_list_entry(
                type_=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_ip_list_entry(
            type_,
            ipornet=ipornet,
            description=description,
            type=type,
            mode=mode,
            protocols=protocols,
            created_at=created_at,
            updated_at=updated_at,
            request_options=request_options,
        )
        return _response.data

    async def get_ip_list_by_ipornet(
        self, type: IpListType, ipornet: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> IpListEntry:
        """
        Returns the entry with the given ipornet if it exists.

        Parameters
        ----------
        type : IpListType
            IP list type

        ipornet : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IpListEntry
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
            await client.ip_lists.get_ip_list_by_ipornet(
                type=1,
                ipornet="ipornet",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_ip_list_by_ipornet(type, ipornet, request_options=request_options)
        return _response.data

    async def update_ip_list_entry(
        self,
        type_: IpListType,
        ipornet_: str,
        *,
        ipornet: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        type: typing.Optional[IpListType] = OMIT,
        mode: typing.Optional[IpListMode] = OMIT,
        protocols: typing.Optional[int] = OMIT,
        created_at: typing.Optional[int] = OMIT,
        updated_at: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        Updates an existing IP list entry

        Parameters
        ----------
        type_ : IpListType
            IP list type

        ipornet_ : str

        ipornet : typing.Optional[str]
            IP address or network in CIDR format, for example `192.168.1.2/32`, `192.168.0.0/24`, `2001:db8::/32`

        description : typing.Optional[str]
            optional description

        type : typing.Optional[IpListType]

        mode : typing.Optional[IpListMode]

        protocols : typing.Optional[int]
            Defines the protocol the entry applies to. `0` means all the supported protocols, 1 SSH, 2 FTP, 4 WebDAV, 8 HTTP. Protocols can be combined, for example 3 means SSH and FTP

        created_at : typing.Optional[int]
            creation time as unix timestamp in milliseconds

        updated_at : typing.Optional[int]
            last update time as unix timestamp in millisecond

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
            await client.ip_lists.update_ip_list_entry(
                type_=1,
                ipornet_="ipornet",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_ip_list_entry(
            type_,
            ipornet_,
            ipornet=ipornet,
            description=description,
            type=type,
            mode=mode,
            protocols=protocols,
            created_at=created_at,
            updated_at=updated_at,
            request_options=request_options,
        )
        return _response.data

    async def delete_ip_list_entry(
        self, type: IpListType, ipornet: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiResponse:
        """
        Deletes an existing IP list entry

        Parameters
        ----------
        type : IpListType
            IP list type

        ipornet : str

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
            await client.ip_lists.delete_ip_list_entry(
                type=1,
                ipornet="ipornet",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_ip_list_entry(type, ipornet, request_options=request_options)
        return _response.data

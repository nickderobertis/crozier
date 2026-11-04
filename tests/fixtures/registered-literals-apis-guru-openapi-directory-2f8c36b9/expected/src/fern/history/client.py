

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.history_item import HistoryItem
from ..types.history_item_type import HistoryItemType
from ..types.paginated_response_of_history_item import PaginatedResponseOfHistoryItem
from ..types.visibility import Visibility
from .raw_client import AsyncRawHistoryClient, RawHistoryClient
from .types.filtered_list_request_type_item import FilteredListRequestTypeItem


OMIT = typing.cast(typing.Any, ...)


class HistoryClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawHistoryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawHistoryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawHistoryClient
        """
        return self._raw_client

    def filtered_list(
        self,
        id4n: str,
        *,
        include_private: typing.Optional[bool] = None,
        organization: typing.Optional[str] = None,
        type: typing.Optional[
            typing.Union[FilteredListRequestTypeItem, typing.Sequence[FilteredListRequestTypeItem]]
        ] = None,
        qualifier: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        from_date: typing.Optional[dt.datetime] = None,
        to_date: typing.Optional[dt.datetime] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResponseOfHistoryItem:
        """
        Lists the history of a GUID

        Parameters
        ----------
        id4n : str
            GUID to retrieve the history for

        include_private : typing.Optional[bool]
            Also return private history entries

        organization : typing.Optional[str]
            Show only entries created by one of the given organizations. This parameter can be used multiple times.

        type : typing.Optional[typing.Union[FilteredListRequestTypeItem, typing.Sequence[FilteredListRequestTypeItem]]]
            Show only entries matching one of the given history item types. This parameter can be used multiple times.

        qualifier : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Show only entries matching one of the given history item qualifiers (additional property de.id4i.history.item.qualifier). This parameter can be used multiple times.

        from_date : typing.Optional[dt.datetime]
            From date time as UTC Date-Time format

        to_date : typing.Optional[dt.datetime]
            To date time as UTC Date-Time format

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
        client.history.filtered_list(
            id4n="id4n",
        )
        """
        _response = self._raw_client.filtered_list(
            id4n,
            include_private=include_private,
            organization=organization,
            type=type,
            qualifier=qualifier,
            from_date=from_date,
            to_date=to_date,
            offset=offset,
            limit=limit,
            request_options=request_options,
        )
        return _response.data

    def add_item(
        self,
        id4n: str,
        *,
        organization_id: str,
        type: HistoryItemType,
        additional_properties: typing.Optional[typing.Dict[str, str]] = OMIT,
        owner_organization_id: typing.Optional[str] = OMIT,
        sequence_id: typing.Optional[int] = OMIT,
        timestamp: typing.Optional[int] = OMIT,
        visibility: typing.Optional[Visibility] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Add a new history item

        Parameters
        ----------
        id4n : str
            GUID to retrieve the history for

        organization_id : str
            Originator of the history item

        type : HistoryItemType
            Type of the history item

        additional_properties : typing.Optional[typing.Dict[str, str]]
            History items custom additional properties

        owner_organization_id : typing.Optional[str]
            Owner of the history item

        sequence_id : typing.Optional[int]
            Forms the primary key of the history item together with the GUID and the organizationId

        timestamp : typing.Optional[int]
            History item timestamp

        visibility : typing.Optional[Visibility]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, HistoryItemType

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.history.add_item(
            id4n="id4n",
            organization_id="org.acme",
            type=HistoryItemType.CREATED,
        )
        """
        _response = self._raw_client.add_item(
            id4n,
            organization_id=organization_id,
            type=type,
            additional_properties=additional_properties,
            owner_organization_id=owner_organization_id,
            sequence_id=sequence_id,
            timestamp=timestamp,
            visibility=visibility,
            request_options=request_options,
        )
        return _response.data

    def list(
        self,
        id4n: str,
        organization_id: str,
        *,
        include_private: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResponseOfHistoryItem:
        """
        DEPRECATED - please use filteredList with organization parameter to achieve the same functionality

        Parameters
        ----------
        id4n : str
            GUID to retrieve the history for

        organization_id : str
            organizationId

        include_private : typing.Optional[bool]
            Also return private history entries

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
        client.history.list(
            id4n="id4n",
            organization_id="organizationId",
        )
        """
        _response = self._raw_client.list(
            id4n,
            organization_id,
            include_private=include_private,
            offset=offset,
            limit=limit,
            request_options=request_options,
        )
        return _response.data

    def retrieve_item(
        self,
        id4n: str,
        organization_id: str,
        sequence_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HistoryItem:
        """
        Parameters
        ----------
        id4n : str
            GUID to retrieve the history for

        organization_id : str
            organizationId

        sequence_id : int
            sequenceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HistoryItem
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.history.retrieve_item(
            id4n="id4n",
            organization_id="organizationId",
            sequence_id=1,
        )
        """
        _response = self._raw_client.retrieve_item(id4n, organization_id, sequence_id, request_options=request_options)
        return _response.data

    def update_item(
        self,
        id4n: str,
        organization_id_path_param: str,
        sequence_id: int,
        *,
        organization_id: typing.Optional[str] = OMIT,
        visibility: typing.Optional[Visibility] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[HistoryItem]:
        """
        Parameters
        ----------
        id4n : str
            GUID to retrieve the history for

        organization_id_path_param : str
            organizationId

        sequence_id : int
            sequenceId

        organization_id : typing.Optional[str]
            New organization id displayed for this item. If given, must match the holder of GUID and the organization the history item is found under.

        visibility : typing.Optional[Visibility]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[HistoryItem]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.history.update_item(
            id4n="id4n",
            organization_id_path_param="organizationId",
            sequence_id=1,
        )
        """
        _response = self._raw_client.update_item(
            id4n,
            organization_id_path_param,
            sequence_id,
            organization_id=organization_id,
            visibility=visibility,
            request_options=request_options,
        )
        return _response.data

    def update_item_visibility(
        self,
        id4n: str,
        organization_id: str,
        sequence_id: int,
        *,
        public: typing.Optional[bool] = OMIT,
        shared_organization_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HistoryItem:
        """
        Parameters
        ----------
        id4n : str
            GUID to retrieve the history for

        organization_id : str
            organizationId

        sequence_id : int
            sequenceId

        public : typing.Optional[bool]
            Document is publicly readable (if ID4N is owned by the same organization)

        shared_organization_ids : typing.Optional[typing.Sequence[str]]
            Document is readable by these organizations (independend of ID4N ownership)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HistoryItem
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.history.update_item_visibility(
            id4n="id4n",
            organization_id="organizationId",
            sequence_id=1,
        )
        """
        _response = self._raw_client.update_item_visibility(
            id4n,
            organization_id,
            sequence_id,
            public=public,
            shared_organization_ids=shared_organization_ids,
            request_options=request_options,
        )
        return _response.data


class AsyncHistoryClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawHistoryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawHistoryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawHistoryClient
        """
        return self._raw_client

    async def filtered_list(
        self,
        id4n: str,
        *,
        include_private: typing.Optional[bool] = None,
        organization: typing.Optional[str] = None,
        type: typing.Optional[
            typing.Union[FilteredListRequestTypeItem, typing.Sequence[FilteredListRequestTypeItem]]
        ] = None,
        qualifier: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        from_date: typing.Optional[dt.datetime] = None,
        to_date: typing.Optional[dt.datetime] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResponseOfHistoryItem:
        """
        Lists the history of a GUID

        Parameters
        ----------
        id4n : str
            GUID to retrieve the history for

        include_private : typing.Optional[bool]
            Also return private history entries

        organization : typing.Optional[str]
            Show only entries created by one of the given organizations. This parameter can be used multiple times.

        type : typing.Optional[typing.Union[FilteredListRequestTypeItem, typing.Sequence[FilteredListRequestTypeItem]]]
            Show only entries matching one of the given history item types. This parameter can be used multiple times.

        qualifier : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Show only entries matching one of the given history item qualifiers (additional property de.id4i.history.item.qualifier). This parameter can be used multiple times.

        from_date : typing.Optional[dt.datetime]
            From date time as UTC Date-Time format

        to_date : typing.Optional[dt.datetime]
            To date time as UTC Date-Time format

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
            await client.history.filtered_list(
                id4n="id4n",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.filtered_list(
            id4n,
            include_private=include_private,
            organization=organization,
            type=type,
            qualifier=qualifier,
            from_date=from_date,
            to_date=to_date,
            offset=offset,
            limit=limit,
            request_options=request_options,
        )
        return _response.data

    async def add_item(
        self,
        id4n: str,
        *,
        organization_id: str,
        type: HistoryItemType,
        additional_properties: typing.Optional[typing.Dict[str, str]] = OMIT,
        owner_organization_id: typing.Optional[str] = OMIT,
        sequence_id: typing.Optional[int] = OMIT,
        timestamp: typing.Optional[int] = OMIT,
        visibility: typing.Optional[Visibility] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Add a new history item

        Parameters
        ----------
        id4n : str
            GUID to retrieve the history for

        organization_id : str
            Originator of the history item

        type : HistoryItemType
            Type of the history item

        additional_properties : typing.Optional[typing.Dict[str, str]]
            History items custom additional properties

        owner_organization_id : typing.Optional[str]
            Owner of the history item

        sequence_id : typing.Optional[int]
            Forms the primary key of the history item together with the GUID and the organizationId

        timestamp : typing.Optional[int]
            History item timestamp

        visibility : typing.Optional[Visibility]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, HistoryItemType

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.history.add_item(
                id4n="id4n",
                organization_id="org.acme",
                type=HistoryItemType.CREATED,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_item(
            id4n,
            organization_id=organization_id,
            type=type,
            additional_properties=additional_properties,
            owner_organization_id=owner_organization_id,
            sequence_id=sequence_id,
            timestamp=timestamp,
            visibility=visibility,
            request_options=request_options,
        )
        return _response.data

    async def list(
        self,
        id4n: str,
        organization_id: str,
        *,
        include_private: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResponseOfHistoryItem:
        """
        DEPRECATED - please use filteredList with organization parameter to achieve the same functionality

        Parameters
        ----------
        id4n : str
            GUID to retrieve the history for

        organization_id : str
            organizationId

        include_private : typing.Optional[bool]
            Also return private history entries

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
            await client.history.list(
                id4n="id4n",
                organization_id="organizationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list(
            id4n,
            organization_id,
            include_private=include_private,
            offset=offset,
            limit=limit,
            request_options=request_options,
        )
        return _response.data

    async def retrieve_item(
        self,
        id4n: str,
        organization_id: str,
        sequence_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HistoryItem:
        """
        Parameters
        ----------
        id4n : str
            GUID to retrieve the history for

        organization_id : str
            organizationId

        sequence_id : int
            sequenceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HistoryItem
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.history.retrieve_item(
                id4n="id4n",
                organization_id="organizationId",
                sequence_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_item(
            id4n, organization_id, sequence_id, request_options=request_options
        )
        return _response.data

    async def update_item(
        self,
        id4n: str,
        organization_id_path_param: str,
        sequence_id: int,
        *,
        organization_id: typing.Optional[str] = OMIT,
        visibility: typing.Optional[Visibility] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[HistoryItem]:
        """
        Parameters
        ----------
        id4n : str
            GUID to retrieve the history for

        organization_id_path_param : str
            organizationId

        sequence_id : int
            sequenceId

        organization_id : typing.Optional[str]
            New organization id displayed for this item. If given, must match the holder of GUID and the organization the history item is found under.

        visibility : typing.Optional[Visibility]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[HistoryItem]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.history.update_item(
                id4n="id4n",
                organization_id_path_param="organizationId",
                sequence_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_item(
            id4n,
            organization_id_path_param,
            sequence_id,
            organization_id=organization_id,
            visibility=visibility,
            request_options=request_options,
        )
        return _response.data

    async def update_item_visibility(
        self,
        id4n: str,
        organization_id: str,
        sequence_id: int,
        *,
        public: typing.Optional[bool] = OMIT,
        shared_organization_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HistoryItem:
        """
        Parameters
        ----------
        id4n : str
            GUID to retrieve the history for

        organization_id : str
            organizationId

        sequence_id : int
            sequenceId

        public : typing.Optional[bool]
            Document is publicly readable (if ID4N is owned by the same organization)

        shared_organization_ids : typing.Optional[typing.Sequence[str]]
            Document is readable by these organizations (independend of ID4N ownership)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HistoryItem
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.history.update_item_visibility(
                id4n="id4n",
                organization_id="organizationId",
                sequence_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_item_visibility(
            id4n,
            organization_id,
            sequence_id,
            public=public,
            shared_organization_ids=shared_organization_ids,
            request_options=request_options,
        )
        return _response.data

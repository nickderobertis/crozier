

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.common_deal_association import CommonDealAssociation
from ..types.crm_create_or_update_deal_response import CrmCreateOrUpdateDealResponse
from ..types.crm_get_deal_response import CrmGetDealResponse
from ..types.crm_get_deals_response import CrmGetDealsResponse
from ..types.crm_search_deals_response import CrmSearchDealsResponse
from .raw_client import AsyncRawCrmDealClient, RawCrmDealClient


OMIT = typing.cast(typing.Any, ...)


class CrmDealClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCrmDealClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCrmDealClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCrmDealClient
        """
        return self._raw_client

    def crm_deal_get_deal(
        self,
        id: str,
        *,
        fields: typing.Optional[str] = None,
        associations: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmGetDealResponse:
        """
        Get details of a deal

        Parameters
        ----------
        id : str

        fields : typing.Optional[str]

        associations : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmGetDealResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.crm_deal.crm_deal_get_deal(
            id="id",
        )
        """
        _response = self._raw_client.crm_deal_get_deal(
            id, fields=fields, associations=associations, request_options=request_options
        )
        return _response.data

    def crm_deal_update_deal(
        self,
        id: str,
        *,
        additional: typing.Any,
        amount: int,
        stage: str,
        name: str,
        expected_close_date: typing.Any,
        is_won: bool,
        probability: int,
        associations: typing.Optional[CommonDealAssociation] = OMIT,
        priority: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmCreateOrUpdateDealResponse:
        """
        Update a deal

        Parameters
        ----------
        id : str

        additional : typing.Any

        amount : int
            The deal amount mentioned in the CRM for this deal.

        stage : str
            Deal stage in the CRM.

        name : str
            The name of the deal in a CRM.

        expected_close_date : typing.Any

        is_won : bool
            Is `true` if the deal is closed (won).

        probability : int
            Probability of the deal getting closed, a decimal number between 0 to 1 (inclusive).

        associations : typing.Optional[CommonDealAssociation]

        priority : typing.Optional[str]
            The priority attached to this deal. (not supported by pipedrive)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmCreateOrUpdateDealResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.crm_deal.crm_deal_update_deal(
            id="id",
            additional={"key": "value"},
            amount=1,
            stage="stage",
            name="name",
            expected_close_date={"key": "value"},
            is_won=True,
            probability=1,
        )
        """
        _response = self._raw_client.crm_deal_update_deal(
            id,
            additional=additional,
            amount=amount,
            stage=stage,
            name=name,
            expected_close_date=expected_close_date,
            is_won=is_won,
            probability=probability,
            associations=associations,
            priority=priority,
            request_options=request_options,
        )
        return _response.data

    def crm_deal_get_deals(
        self,
        *,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        associations: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmGetDealsResponse:
        """
        Get all the deals

        Parameters
        ----------
        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        associations : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmGetDealsResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.crm_deal.crm_deal_get_deals()
        """
        _response = self._raw_client.crm_deal_get_deals(
            fields=fields,
            page_size=page_size,
            cursor=cursor,
            associations=associations,
            request_options=request_options,
        )
        return _response.data

    def crm_deal_create_deal(
        self,
        *,
        additional: typing.Any,
        amount: int,
        stage: str,
        name: str,
        expected_close_date: typing.Any,
        is_won: bool,
        probability: int,
        associations: typing.Optional[CommonDealAssociation] = OMIT,
        priority: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmCreateOrUpdateDealResponse:
        """
        Create a new deal

        Parameters
        ----------
        additional : typing.Any

        amount : int
            The deal amount mentioned in the CRM for this deal.

        stage : str
            Deal stage in the CRM.

        name : str
            The name of the deal in a CRM.

        expected_close_date : typing.Any

        is_won : bool
            Is `true` if the deal is closed (won).

        probability : int
            Probability of the deal getting closed, a decimal number between 0 to 1 (inclusive).

        associations : typing.Optional[CommonDealAssociation]

        priority : typing.Optional[str]
            The priority attached to this deal. (not supported by pipedrive)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmCreateOrUpdateDealResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.crm_deal.crm_deal_create_deal(
            additional={"key": "value"},
            amount=1,
            stage="stage",
            name="name",
            expected_close_date={"key": "value"},
            is_won=True,
            probability=1,
        )
        """
        _response = self._raw_client.crm_deal_create_deal(
            additional=additional,
            amount=amount,
            stage=stage,
            name=name,
            expected_close_date=expected_close_date,
            is_won=is_won,
            probability=probability,
            associations=associations,
            priority=priority,
            request_options=request_options,
        )
        return _response.data

    def crm_deal_search_deals(
        self,
        *,
        search_criteria: typing.Any,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmSearchDealsResponse:
        """
        Search for deals

        Parameters
        ----------
        search_criteria : typing.Any

        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmSearchDealsResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.crm_deal.crm_deal_search_deals(
            search_criteria={"key": "value"},
        )
        """
        _response = self._raw_client.crm_deal_search_deals(
            search_criteria=search_criteria,
            fields=fields,
            page_size=page_size,
            cursor=cursor,
            request_options=request_options,
        )
        return _response.data


class AsyncCrmDealClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCrmDealClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCrmDealClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCrmDealClient
        """
        return self._raw_client

    async def crm_deal_get_deal(
        self,
        id: str,
        *,
        fields: typing.Optional[str] = None,
        associations: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmGetDealResponse:
        """
        Get details of a deal

        Parameters
        ----------
        id : str

        fields : typing.Optional[str]

        associations : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmGetDealResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.crm_deal.crm_deal_get_deal(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.crm_deal_get_deal(
            id, fields=fields, associations=associations, request_options=request_options
        )
        return _response.data

    async def crm_deal_update_deal(
        self,
        id: str,
        *,
        additional: typing.Any,
        amount: int,
        stage: str,
        name: str,
        expected_close_date: typing.Any,
        is_won: bool,
        probability: int,
        associations: typing.Optional[CommonDealAssociation] = OMIT,
        priority: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmCreateOrUpdateDealResponse:
        """
        Update a deal

        Parameters
        ----------
        id : str

        additional : typing.Any

        amount : int
            The deal amount mentioned in the CRM for this deal.

        stage : str
            Deal stage in the CRM.

        name : str
            The name of the deal in a CRM.

        expected_close_date : typing.Any

        is_won : bool
            Is `true` if the deal is closed (won).

        probability : int
            Probability of the deal getting closed, a decimal number between 0 to 1 (inclusive).

        associations : typing.Optional[CommonDealAssociation]

        priority : typing.Optional[str]
            The priority attached to this deal. (not supported by pipedrive)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmCreateOrUpdateDealResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.crm_deal.crm_deal_update_deal(
                id="id",
                additional={"key": "value"},
                amount=1,
                stage="stage",
                name="name",
                expected_close_date={"key": "value"},
                is_won=True,
                probability=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.crm_deal_update_deal(
            id,
            additional=additional,
            amount=amount,
            stage=stage,
            name=name,
            expected_close_date=expected_close_date,
            is_won=is_won,
            probability=probability,
            associations=associations,
            priority=priority,
            request_options=request_options,
        )
        return _response.data

    async def crm_deal_get_deals(
        self,
        *,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        associations: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmGetDealsResponse:
        """
        Get all the deals

        Parameters
        ----------
        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        associations : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmGetDealsResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.crm_deal.crm_deal_get_deals()


        asyncio.run(main())
        """
        _response = await self._raw_client.crm_deal_get_deals(
            fields=fields,
            page_size=page_size,
            cursor=cursor,
            associations=associations,
            request_options=request_options,
        )
        return _response.data

    async def crm_deal_create_deal(
        self,
        *,
        additional: typing.Any,
        amount: int,
        stage: str,
        name: str,
        expected_close_date: typing.Any,
        is_won: bool,
        probability: int,
        associations: typing.Optional[CommonDealAssociation] = OMIT,
        priority: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmCreateOrUpdateDealResponse:
        """
        Create a new deal

        Parameters
        ----------
        additional : typing.Any

        amount : int
            The deal amount mentioned in the CRM for this deal.

        stage : str
            Deal stage in the CRM.

        name : str
            The name of the deal in a CRM.

        expected_close_date : typing.Any

        is_won : bool
            Is `true` if the deal is closed (won).

        probability : int
            Probability of the deal getting closed, a decimal number between 0 to 1 (inclusive).

        associations : typing.Optional[CommonDealAssociation]

        priority : typing.Optional[str]
            The priority attached to this deal. (not supported by pipedrive)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmCreateOrUpdateDealResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.crm_deal.crm_deal_create_deal(
                additional={"key": "value"},
                amount=1,
                stage="stage",
                name="name",
                expected_close_date={"key": "value"},
                is_won=True,
                probability=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.crm_deal_create_deal(
            additional=additional,
            amount=amount,
            stage=stage,
            name=name,
            expected_close_date=expected_close_date,
            is_won=is_won,
            probability=probability,
            associations=associations,
            priority=priority,
            request_options=request_options,
        )
        return _response.data

    async def crm_deal_search_deals(
        self,
        *,
        search_criteria: typing.Any,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmSearchDealsResponse:
        """
        Search for deals

        Parameters
        ----------
        search_criteria : typing.Any

        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmSearchDealsResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.crm_deal.crm_deal_search_deals(
                search_criteria={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.crm_deal_search_deals(
            search_criteria=search_criteria,
            fields=fields,
            page_size=page_size,
            cursor=cursor,
            request_options=request_options,
        )
        return _response.data

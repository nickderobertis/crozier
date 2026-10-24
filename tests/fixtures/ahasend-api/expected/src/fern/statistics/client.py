

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.bounce_statistics_response import BounceStatisticsResponse
from ..types.deliverability_statistics_response import DeliverabilityStatisticsResponse
from ..types.delivery_time_statistics_response import DeliveryTimeStatisticsResponse
from .raw_client import AsyncRawStatisticsClient, RawStatisticsClient
from .types.get_bounce_statistics_request_group_by import GetBounceStatisticsRequestGroupBy
from .types.get_deliverability_statistics_request_group_by import GetDeliverabilityStatisticsRequestGroupBy
from .types.get_delivery_time_statistics_request_group_by import GetDeliveryTimeStatisticsRequestGroupBy


class StatisticsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawStatisticsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawStatisticsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawStatisticsClient
        """
        return self._raw_client

    def get_deliverability_statistics(
        self,
        account_id: str,
        *,
        from_time: typing.Optional[dt.datetime] = None,
        to_time: typing.Optional[dt.datetime] = None,
        sender_domain: typing.Optional[str] = None,
        recipient_domains: typing.Optional[str] = None,
        tags: typing.Optional[str] = None,
        group_by: typing.Optional[GetDeliverabilityStatisticsRequestGroupBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeliverabilityStatisticsResponse:
        """
        Returns transactional deliverability statistics grouped by status

        The global statistics role can query all sender domains. A
        domain-scoped key is limited to authorized domains and must authorize
        every comma-separated value supplied in `sender_domain`.

        **Query Parameters:**
        - `from_time`: Filter statistics after this date (RFC3339 format)
        - `to_time`: Filter statistics before this date (RFC3339 format)
        - `sender_domain`: Filter by sender domain
        - `recipient_domains`: Filter by recipient domain
        - `tags`: Filter by tags (comma-separated)
        - `group_by`: Group by time period (hour, day, week, month)

        Parameters
        ----------
        account_id : str
            Account ID

        from_time : typing.Optional[dt.datetime]
            Filter statistics after this datetime (RFC3339 format)

        to_time : typing.Optional[dt.datetime]
            Filter statistics before this datetime (RFC3339 format)

        sender_domain : typing.Optional[str]
            Comma-separated sender domains; the key must authorize every requested domain

        recipient_domains : typing.Optional[str]
            Filter by a comma separated list of recipient domains

        tags : typing.Optional[str]
            Filter by tags (comma-separated)

        group_by : typing.Optional[GetDeliverabilityStatisticsRequestGroupBy]
            Group by time period

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeliverabilityStatisticsResponse
            Deliverability statistics

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.statistics.get_deliverability_statistics(
            account_id="account_id",
            recipient_domains="gmail.com,googlemail.com",
        )
        """
        _response = self._raw_client.get_deliverability_statistics(
            account_id,
            from_time=from_time,
            to_time=to_time,
            sender_domain=sender_domain,
            recipient_domains=recipient_domains,
            tags=tags,
            group_by=group_by,
            request_options=request_options,
        )
        return _response.data

    def get_bounce_statistics(
        self,
        account_id: str,
        *,
        from_time: typing.Optional[dt.datetime] = None,
        to_time: typing.Optional[dt.datetime] = None,
        sender_domain: typing.Optional[str] = None,
        recipient_domains: typing.Optional[str] = None,
        tags: typing.Optional[str] = None,
        group_by: typing.Optional[GetBounceStatisticsRequestGroupBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BounceStatisticsResponse:
        """
        Returns transactional bounce statistics grouped by classification

        The global statistics role can query all sender domains. A
        domain-scoped key is limited to authorized domains and must authorize
        every comma-separated value supplied in `sender_domain`.

        **Query Parameters:**
        - `from_time`: Filter statistics after this date (RFC3339 format)
        - `to_time`: Filter statistics before this date (RFC3339 format)
        - `sender_domain`: Filter by sender domain
        - `recipient_domains`: Filter by recipient domain
        - `tags`: Filter by tags (comma-separated)
        - `group_by`: Group by time period (hour, day, week, month)

        Parameters
        ----------
        account_id : str
            Account ID

        from_time : typing.Optional[dt.datetime]
            Filter statistics after this datetime (RFC3339 format)

        to_time : typing.Optional[dt.datetime]
            Filter statistics before this datetime (RFC3339 format)

        sender_domain : typing.Optional[str]
            Comma-separated sender domains; the key must authorize every requested domain

        recipient_domains : typing.Optional[str]
            Filter by a comma separated list of recipient domains

        tags : typing.Optional[str]
            Filter by tags (comma-separated)

        group_by : typing.Optional[GetBounceStatisticsRequestGroupBy]
            Group by time period

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BounceStatisticsResponse
            Bounce statistics

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.statistics.get_bounce_statistics(
            account_id="account_id",
            recipient_domains="gmail.com,googlemail.com",
        )
        """
        _response = self._raw_client.get_bounce_statistics(
            account_id,
            from_time=from_time,
            to_time=to_time,
            sender_domain=sender_domain,
            recipient_domains=recipient_domains,
            tags=tags,
            group_by=group_by,
            request_options=request_options,
        )
        return _response.data

    def get_delivery_time_statistics(
        self,
        account_id: str,
        *,
        from_time: typing.Optional[dt.datetime] = None,
        to_time: typing.Optional[dt.datetime] = None,
        sender_domain: typing.Optional[str] = None,
        recipient_domains: typing.Optional[str] = None,
        tags: typing.Optional[str] = None,
        group_by: typing.Optional[GetDeliveryTimeStatisticsRequestGroupBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeliveryTimeStatisticsResponse:
        """
        Returns transactional delivery time statistics grouped by recipient domain

        The global statistics role can query all sender domains. A
        domain-scoped key is limited to authorized domains and must authorize
        every comma-separated value supplied in `sender_domain`.

        **Query Parameters:**
        - `from_time`: Filter statistics after this date (RFC3339 format)
        - `to_time`: Filter statistics before this date (RFC3339 format)
        - `sender_domain`: Filter by sender domain
        - `recipient_domains`: Filter by recipient domains
        - `tags`: Filter by tags (comma-separated)
        - `group_by`: Group by time period (hour, day, week, month)

        Parameters
        ----------
        account_id : str
            Account ID

        from_time : typing.Optional[dt.datetime]
            Filter statistics after this datetime (RFC3339 format)

        to_time : typing.Optional[dt.datetime]
            Filter statistics before this datetime (RFC3339 format)

        sender_domain : typing.Optional[str]
            Comma-separated sender domains; the key must authorize every requested domain

        recipient_domains : typing.Optional[str]
            Filter by a comma separated list of recipient domains

        tags : typing.Optional[str]
            Filter by tags (comma-separated)

        group_by : typing.Optional[GetDeliveryTimeStatisticsRequestGroupBy]
            Group by time period

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeliveryTimeStatisticsResponse
            Delivery time statistics

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.statistics.get_delivery_time_statistics(
            account_id="account_id",
            recipient_domains="gmail.com,googlemail.com",
        )
        """
        _response = self._raw_client.get_delivery_time_statistics(
            account_id,
            from_time=from_time,
            to_time=to_time,
            sender_domain=sender_domain,
            recipient_domains=recipient_domains,
            tags=tags,
            group_by=group_by,
            request_options=request_options,
        )
        return _response.data


class AsyncStatisticsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawStatisticsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawStatisticsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawStatisticsClient
        """
        return self._raw_client

    async def get_deliverability_statistics(
        self,
        account_id: str,
        *,
        from_time: typing.Optional[dt.datetime] = None,
        to_time: typing.Optional[dt.datetime] = None,
        sender_domain: typing.Optional[str] = None,
        recipient_domains: typing.Optional[str] = None,
        tags: typing.Optional[str] = None,
        group_by: typing.Optional[GetDeliverabilityStatisticsRequestGroupBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeliverabilityStatisticsResponse:
        """
        Returns transactional deliverability statistics grouped by status

        The global statistics role can query all sender domains. A
        domain-scoped key is limited to authorized domains and must authorize
        every comma-separated value supplied in `sender_domain`.

        **Query Parameters:**
        - `from_time`: Filter statistics after this date (RFC3339 format)
        - `to_time`: Filter statistics before this date (RFC3339 format)
        - `sender_domain`: Filter by sender domain
        - `recipient_domains`: Filter by recipient domain
        - `tags`: Filter by tags (comma-separated)
        - `group_by`: Group by time period (hour, day, week, month)

        Parameters
        ----------
        account_id : str
            Account ID

        from_time : typing.Optional[dt.datetime]
            Filter statistics after this datetime (RFC3339 format)

        to_time : typing.Optional[dt.datetime]
            Filter statistics before this datetime (RFC3339 format)

        sender_domain : typing.Optional[str]
            Comma-separated sender domains; the key must authorize every requested domain

        recipient_domains : typing.Optional[str]
            Filter by a comma separated list of recipient domains

        tags : typing.Optional[str]
            Filter by tags (comma-separated)

        group_by : typing.Optional[GetDeliverabilityStatisticsRequestGroupBy]
            Group by time period

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeliverabilityStatisticsResponse
            Deliverability statistics

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.statistics.get_deliverability_statistics(
                account_id="account_id",
                recipient_domains="gmail.com,googlemail.com",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_deliverability_statistics(
            account_id,
            from_time=from_time,
            to_time=to_time,
            sender_domain=sender_domain,
            recipient_domains=recipient_domains,
            tags=tags,
            group_by=group_by,
            request_options=request_options,
        )
        return _response.data

    async def get_bounce_statistics(
        self,
        account_id: str,
        *,
        from_time: typing.Optional[dt.datetime] = None,
        to_time: typing.Optional[dt.datetime] = None,
        sender_domain: typing.Optional[str] = None,
        recipient_domains: typing.Optional[str] = None,
        tags: typing.Optional[str] = None,
        group_by: typing.Optional[GetBounceStatisticsRequestGroupBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BounceStatisticsResponse:
        """
        Returns transactional bounce statistics grouped by classification

        The global statistics role can query all sender domains. A
        domain-scoped key is limited to authorized domains and must authorize
        every comma-separated value supplied in `sender_domain`.

        **Query Parameters:**
        - `from_time`: Filter statistics after this date (RFC3339 format)
        - `to_time`: Filter statistics before this date (RFC3339 format)
        - `sender_domain`: Filter by sender domain
        - `recipient_domains`: Filter by recipient domain
        - `tags`: Filter by tags (comma-separated)
        - `group_by`: Group by time period (hour, day, week, month)

        Parameters
        ----------
        account_id : str
            Account ID

        from_time : typing.Optional[dt.datetime]
            Filter statistics after this datetime (RFC3339 format)

        to_time : typing.Optional[dt.datetime]
            Filter statistics before this datetime (RFC3339 format)

        sender_domain : typing.Optional[str]
            Comma-separated sender domains; the key must authorize every requested domain

        recipient_domains : typing.Optional[str]
            Filter by a comma separated list of recipient domains

        tags : typing.Optional[str]
            Filter by tags (comma-separated)

        group_by : typing.Optional[GetBounceStatisticsRequestGroupBy]
            Group by time period

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BounceStatisticsResponse
            Bounce statistics

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.statistics.get_bounce_statistics(
                account_id="account_id",
                recipient_domains="gmail.com,googlemail.com",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_bounce_statistics(
            account_id,
            from_time=from_time,
            to_time=to_time,
            sender_domain=sender_domain,
            recipient_domains=recipient_domains,
            tags=tags,
            group_by=group_by,
            request_options=request_options,
        )
        return _response.data

    async def get_delivery_time_statistics(
        self,
        account_id: str,
        *,
        from_time: typing.Optional[dt.datetime] = None,
        to_time: typing.Optional[dt.datetime] = None,
        sender_domain: typing.Optional[str] = None,
        recipient_domains: typing.Optional[str] = None,
        tags: typing.Optional[str] = None,
        group_by: typing.Optional[GetDeliveryTimeStatisticsRequestGroupBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeliveryTimeStatisticsResponse:
        """
        Returns transactional delivery time statistics grouped by recipient domain

        The global statistics role can query all sender domains. A
        domain-scoped key is limited to authorized domains and must authorize
        every comma-separated value supplied in `sender_domain`.

        **Query Parameters:**
        - `from_time`: Filter statistics after this date (RFC3339 format)
        - `to_time`: Filter statistics before this date (RFC3339 format)
        - `sender_domain`: Filter by sender domain
        - `recipient_domains`: Filter by recipient domains
        - `tags`: Filter by tags (comma-separated)
        - `group_by`: Group by time period (hour, day, week, month)

        Parameters
        ----------
        account_id : str
            Account ID

        from_time : typing.Optional[dt.datetime]
            Filter statistics after this datetime (RFC3339 format)

        to_time : typing.Optional[dt.datetime]
            Filter statistics before this datetime (RFC3339 format)

        sender_domain : typing.Optional[str]
            Comma-separated sender domains; the key must authorize every requested domain

        recipient_domains : typing.Optional[str]
            Filter by a comma separated list of recipient domains

        tags : typing.Optional[str]
            Filter by tags (comma-separated)

        group_by : typing.Optional[GetDeliveryTimeStatisticsRequestGroupBy]
            Group by time period

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeliveryTimeStatisticsResponse
            Delivery time statistics

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.statistics.get_delivery_time_statistics(
                account_id="account_id",
                recipient_domains="gmail.com,googlemail.com",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_delivery_time_statistics(
            account_id,
            from_time=from_time,
            to_time=to_time,
            sender_domain=sender_domain,
            recipient_domains=recipient_domains,
            tags=tags,
            group_by=group_by,
            request_options=request_options,
        )
        return _response.data

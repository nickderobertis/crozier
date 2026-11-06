

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.badge_update import BadgeUpdate
from ..types.user_badges import UserBadges
from .raw_client import AsyncRawUserBadgesClient, RawUserBadgesClient


class UserBadgesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUserBadgesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUserBadgesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUserBadgesClient
        """
        return self._raw_client

    def list_badges(self, *, request_options: typing.Optional[RequestOptions] = None) -> UserBadges:
        """
        provides a list of all badges and the total amount of badges for the currently logged in user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserBadges
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.user_badges.list_badges()
        """
        _response = self._raw_client.list_badges(request_options=request_options)
        return _response.data

    def list_newest_badge(self, *, request_options: typing.Optional[RequestOptions] = None) -> BadgeUpdate:
        """
        If the last report generated badges, these will be returned

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BadgeUpdate
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.user_badges.list_newest_badge()
        """
        _response = self._raw_client.list_newest_badge(request_options=request_options)
        return _response.data


class AsyncUserBadgesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUserBadgesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUserBadgesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUserBadgesClient
        """
        return self._raw_client

    async def list_badges(self, *, request_options: typing.Optional[RequestOptions] = None) -> UserBadges:
        """
        provides a list of all badges and the total amount of badges for the currently logged in user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserBadges
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.user_badges.list_badges()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_badges(request_options=request_options)
        return _response.data

    async def list_newest_badge(self, *, request_options: typing.Optional[RequestOptions] = None) -> BadgeUpdate:
        """
        If the last report generated badges, these will be returned

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BadgeUpdate
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.user_badges.list_newest_badge()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_newest_badge(request_options=request_options)
        return _response.data

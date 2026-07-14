

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawBadgesClient, RawBadgesClient
from .types.admin_list_badges_response import AdminListBadgesResponse
from .types.create_badge_response import CreateBadgeResponse
from .types.list_user_badges_response import ListUserBadgesResponse
from .types.update_badge_response import UpdateBadgeResponse


OMIT = typing.cast(typing.Any, ...)


class BadgesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBadgesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBadgesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBadgesClient
        """
        return self._raw_client

    def admin_list_badges(self, *, request_options: typing.Optional[RequestOptions] = None) -> AdminListBadgesResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AdminListBadgesResponse
            success response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.badges.admin_list_badges()
        """
        _response = self._raw_client.admin_list_badges(request_options=request_options)
        return _response.data

    def create_badge(
        self, *, badge_type_id: int, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CreateBadgeResponse:
        """
        Parameters
        ----------
        badge_type_id : int
            The ID for the badge type. 1 for Gold, 2 for Silver,
            3 for Bronze.

        name : str
            The name for the new badge.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateBadgeResponse
            success response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.badges.create_badge(
            badge_type_id=1,
            name="name",
        )
        """
        _response = self._raw_client.create_badge(
            badge_type_id=badge_type_id, name=name, request_options=request_options
        )
        return _response.data

    def update_badge(
        self, id: int, *, badge_type_id: int, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateBadgeResponse:
        """
        Parameters
        ----------
        id : int

        badge_type_id : int
            The ID for the badge type. 1 for Gold, 2 for Silver,
            3 for Bronze.

        name : str
            The name for the new badge.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateBadgeResponse
            success response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.badges.update_badge(
            id=1,
            badge_type_id=1,
            name="name",
        )
        """
        _response = self._raw_client.update_badge(
            id, badge_type_id=badge_type_id, name=name, request_options=request_options
        )
        return _response.data

    def delete_badge(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.badges.delete_badge(
            id=1,
        )
        """
        _response = self._raw_client.delete_badge(id, request_options=request_options)
        return _response.data

    def list_user_badges(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListUserBadgesResponse:
        """
        Parameters
        ----------
        username : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListUserBadgesResponse
            success response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.badges.list_user_badges(
            username="username",
        )
        """
        _response = self._raw_client.list_user_badges(username, request_options=request_options)
        return _response.data


class AsyncBadgesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBadgesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBadgesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBadgesClient
        """
        return self._raw_client

    async def admin_list_badges(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AdminListBadgesResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AdminListBadgesResponse
            success response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.badges.admin_list_badges()


        asyncio.run(main())
        """
        _response = await self._raw_client.admin_list_badges(request_options=request_options)
        return _response.data

    async def create_badge(
        self, *, badge_type_id: int, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CreateBadgeResponse:
        """
        Parameters
        ----------
        badge_type_id : int
            The ID for the badge type. 1 for Gold, 2 for Silver,
            3 for Bronze.

        name : str
            The name for the new badge.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateBadgeResponse
            success response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.badges.create_badge(
                badge_type_id=1,
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_badge(
            badge_type_id=badge_type_id, name=name, request_options=request_options
        )
        return _response.data

    async def update_badge(
        self, id: int, *, badge_type_id: int, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateBadgeResponse:
        """
        Parameters
        ----------
        id : int

        badge_type_id : int
            The ID for the badge type. 1 for Gold, 2 for Silver,
            3 for Bronze.

        name : str
            The name for the new badge.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateBadgeResponse
            success response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.badges.update_badge(
                id=1,
                badge_type_id=1,
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_badge(
            id, badge_type_id=badge_type_id, name=name, request_options=request_options
        )
        return _response.data

    async def delete_badge(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.badges.delete_badge(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_badge(id, request_options=request_options)
        return _response.data

    async def list_user_badges(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListUserBadgesResponse:
        """
        Parameters
        ----------
        username : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListUserBadgesResponse
            success response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.badges.list_user_badges(
                username="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_user_badges(username, request_options=request_options)
        return _response.data

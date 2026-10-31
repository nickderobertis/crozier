

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.balloon import Balloon
from ..types.balloon_summary import BalloonSummary
from .raw_client import AsyncRawBalloonsClient, RawBalloonsClient
from .types.patch_users_user_id_balloons_id_request_color import PatchUsersUserIdBalloonsIdRequestColor
from .types.post_users_user_id_balloons_request_color import PostUsersUserIdBalloonsRequestColor
from .types.put_users_user_id_balloons_id_update_put_request_color import PutUsersUserIdBalloonsIdUpdatePutRequestColor


OMIT = typing.cast(typing.Any, ...)


class BalloonsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBalloonsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBalloonsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBalloonsClient
        """
        return self._raw_client

    def get_users_user_id_balloons(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[BalloonSummary]:
        """
        Fetch multiple Balloons

        Parameters
        ----------
        user_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[BalloonSummary]
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.balloons.get_users_user_id_balloons(
            user_id="userId",
        )
        """
        _response = self._raw_client.get_users_user_id_balloons(user_id, request_options=request_options)
        return _response.data

    def post_users_user_id_balloons(
        self,
        user_id: str,
        *,
        color: typing.Optional[PostUsersUserIdBalloonsRequestColor] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Balloon:
        """
        Create a Balloon

        Parameters
        ----------
        user_id : str

        color : typing.Optional[PostUsersUserIdBalloonsRequestColor]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Balloon
            Created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.balloons.post_users_user_id_balloons(
            user_id="userId",
        )
        """
        _response = self._raw_client.post_users_user_id_balloons(user_id, color=color, request_options=request_options)
        return _response.data

    def get_users_user_id_balloons_id(
        self, user_id: str, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Balloon:
        """
        Fetch a Balloon

        Parameters
        ----------
        user_id : str

        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Balloon
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.balloons.get_users_user_id_balloons_id(
            user_id="userId",
            id="id",
        )
        """
        _response = self._raw_client.get_users_user_id_balloons_id(user_id, id, request_options=request_options)
        return _response.data

    def delete_users_user_id_balloons_id(
        self, user_id: str, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Destroy a Balloon

        Parameters
        ----------
        user_id : str

        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.balloons.delete_users_user_id_balloons_id(
            user_id="userId",
            id="id",
        )
        """
        _response = self._raw_client.delete_users_user_id_balloons_id(user_id, id, request_options=request_options)
        return _response.data

    def patch_users_user_id_balloons_id(
        self,
        user_id: str,
        id: str,
        *,
        color: typing.Optional[PatchUsersUserIdBalloonsIdRequestColor] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update a Balloon

        Parameters
        ----------
        user_id : str

        id : str

        color : typing.Optional[PatchUsersUserIdBalloonsIdRequestColor]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.balloons.patch_users_user_id_balloons_id(
            user_id="userId",
            id="id",
        )
        """
        _response = self._raw_client.patch_users_user_id_balloons_id(
            user_id, id, color=color, request_options=request_options
        )
        return _response.data

    def put_users_user_id_balloons_id_update_put(
        self,
        user_id: str,
        id: str,
        *,
        color: typing.Optional[PutUsersUserIdBalloonsIdUpdatePutRequestColor] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update a Balloon

        Parameters
        ----------
        user_id : str

        id : str

        color : typing.Optional[PutUsersUserIdBalloonsIdUpdatePutRequestColor]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.balloons.put_users_user_id_balloons_id_update_put(
            user_id="userId",
            id="id",
        )
        """
        _response = self._raw_client.put_users_user_id_balloons_id_update_put(
            user_id, id, color=color, request_options=request_options
        )
        return _response.data


class AsyncBalloonsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBalloonsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBalloonsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBalloonsClient
        """
        return self._raw_client

    async def get_users_user_id_balloons(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[BalloonSummary]:
        """
        Fetch multiple Balloons

        Parameters
        ----------
        user_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[BalloonSummary]
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.balloons.get_users_user_id_balloons(
                user_id="userId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_users_user_id_balloons(user_id, request_options=request_options)
        return _response.data

    async def post_users_user_id_balloons(
        self,
        user_id: str,
        *,
        color: typing.Optional[PostUsersUserIdBalloonsRequestColor] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Balloon:
        """
        Create a Balloon

        Parameters
        ----------
        user_id : str

        color : typing.Optional[PostUsersUserIdBalloonsRequestColor]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Balloon
            Created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.balloons.post_users_user_id_balloons(
                user_id="userId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_users_user_id_balloons(
            user_id, color=color, request_options=request_options
        )
        return _response.data

    async def get_users_user_id_balloons_id(
        self, user_id: str, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Balloon:
        """
        Fetch a Balloon

        Parameters
        ----------
        user_id : str

        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Balloon
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.balloons.get_users_user_id_balloons_id(
                user_id="userId",
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_users_user_id_balloons_id(user_id, id, request_options=request_options)
        return _response.data

    async def delete_users_user_id_balloons_id(
        self, user_id: str, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Destroy a Balloon

        Parameters
        ----------
        user_id : str

        id : str

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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.balloons.delete_users_user_id_balloons_id(
                user_id="userId",
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_users_user_id_balloons_id(
            user_id, id, request_options=request_options
        )
        return _response.data

    async def patch_users_user_id_balloons_id(
        self,
        user_id: str,
        id: str,
        *,
        color: typing.Optional[PatchUsersUserIdBalloonsIdRequestColor] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update a Balloon

        Parameters
        ----------
        user_id : str

        id : str

        color : typing.Optional[PatchUsersUserIdBalloonsIdRequestColor]

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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.balloons.patch_users_user_id_balloons_id(
                user_id="userId",
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_users_user_id_balloons_id(
            user_id, id, color=color, request_options=request_options
        )
        return _response.data

    async def put_users_user_id_balloons_id_update_put(
        self,
        user_id: str,
        id: str,
        *,
        color: typing.Optional[PutUsersUserIdBalloonsIdUpdatePutRequestColor] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update a Balloon

        Parameters
        ----------
        user_id : str

        id : str

        color : typing.Optional[PutUsersUserIdBalloonsIdUpdatePutRequestColor]

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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.balloons.put_users_user_id_balloons_id_update_put(
                user_id="userId",
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_users_user_id_balloons_id_update_put(
            user_id, id, color=color, request_options=request_options
        )
        return _response.data

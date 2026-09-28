

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.channel import Channel
from ..types.display_name_user import DisplayNameUser
from ..types.image_url import ImageUrl
from ..types.name_user import NameUser
from .raw_client import AsyncRawUserClient, RawUserClient
from .types.create_user_response import CreateUserResponse
from .types.get_user_response import GetUserResponse
from .types.get_users_response_item import GetUsersResponseItem
from .types.getuser_conversations_response_item import GetuserConversationsResponseItem
from .types.update_user_response import UpdateUserResponse


OMIT = typing.cast(typing.Any, ...)


class UserClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUserClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUserClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUserClient
        """
        return self._raw_client

    def get_users(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GetUsersResponseItem]:
        """
        This endpoint is **DEPRECATED**. Please use [/v0.2/users](/api/conversation.v2#get-users).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GetUsersResponseItem]
            List of users

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.user.get_users()
        """
        _response = self._raw_client.get_users(request_options=request_options)
        return _response.data

    def create_user(
        self,
        *,
        display_name: typing.Optional[DisplayNameUser] = OMIT,
        image_url: typing.Optional[ImageUrl] = OMIT,
        name: typing.Optional[NameUser] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateUserResponse:
        """
        Note: Users must be created with an admin JWT.

        Parameters
        ----------
        display_name : typing.Optional[DisplayNameUser]

        image_url : typing.Optional[ImageUrl]

        name : typing.Optional[NameUser]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateUserResponse
            Create a user response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.user.create_user()
        """
        _response = self._raw_client.create_user(
            display_name=display_name, image_url=image_url, name=name, request_options=request_options
        )
        return _response.data

    def get_user(self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GetUserResponse:
        """
        Parameters
        ----------
        user_id : str
            User ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetUserResponse
            Retrieve a user

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.user.get_user(
            user_id="user_id",
        )
        """
        _response = self._raw_client.get_user(user_id, request_options=request_options)
        return _response.data

    def update_user(
        self,
        user_id: str,
        *,
        channels: typing.Optional[Channel] = OMIT,
        display_name: typing.Optional[DisplayNameUser] = OMIT,
        image_url: typing.Optional[ImageUrl] = OMIT,
        name: typing.Optional[NameUser] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateUserResponse:
        """
        Parameters
        ----------
        user_id : str
            User ID

        channels : typing.Optional[Channel]

        display_name : typing.Optional[DisplayNameUser]

        image_url : typing.Optional[ImageUrl]

        name : typing.Optional[NameUser]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateUserResponse
            Retrieve a user

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.user.update_user(
            user_id="user_id",
        )
        """
        _response = self._raw_client.update_user(
            user_id,
            channels=channels,
            display_name=display_name,
            image_url=image_url,
            name=name,
            request_options=request_options,
        )
        return _response.data

    def delete_user(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        user_id : str
            User ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Success response with empty JSON

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.user.delete_user(
            user_id="user_id",
        )
        """
        _response = self._raw_client.delete_user(user_id, request_options=request_options)
        return _response.data

    def getuser_conversations(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GetuserConversationsResponseItem]:
        """
        Parameters
        ----------
        user_id : str
            User ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GetuserConversationsResponseItem]
            List user conversations

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.user.getuser_conversations(
            user_id="user_id",
        )
        """
        _response = self._raw_client.getuser_conversations(user_id, request_options=request_options)
        return _response.data


class AsyncUserClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUserClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUserClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUserClient
        """
        return self._raw_client

    async def get_users(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GetUsersResponseItem]:
        """
        This endpoint is **DEPRECATED**. Please use [/v0.2/users](/api/conversation.v2#get-users).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GetUsersResponseItem]
            List of users

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.user.get_users()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_users(request_options=request_options)
        return _response.data

    async def create_user(
        self,
        *,
        display_name: typing.Optional[DisplayNameUser] = OMIT,
        image_url: typing.Optional[ImageUrl] = OMIT,
        name: typing.Optional[NameUser] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateUserResponse:
        """
        Note: Users must be created with an admin JWT.

        Parameters
        ----------
        display_name : typing.Optional[DisplayNameUser]

        image_url : typing.Optional[ImageUrl]

        name : typing.Optional[NameUser]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateUserResponse
            Create a user response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.user.create_user()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_user(
            display_name=display_name, image_url=image_url, name=name, request_options=request_options
        )
        return _response.data

    async def get_user(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetUserResponse:
        """
        Parameters
        ----------
        user_id : str
            User ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetUserResponse
            Retrieve a user

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.user.get_user(
                user_id="user_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_user(user_id, request_options=request_options)
        return _response.data

    async def update_user(
        self,
        user_id: str,
        *,
        channels: typing.Optional[Channel] = OMIT,
        display_name: typing.Optional[DisplayNameUser] = OMIT,
        image_url: typing.Optional[ImageUrl] = OMIT,
        name: typing.Optional[NameUser] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateUserResponse:
        """
        Parameters
        ----------
        user_id : str
            User ID

        channels : typing.Optional[Channel]

        display_name : typing.Optional[DisplayNameUser]

        image_url : typing.Optional[ImageUrl]

        name : typing.Optional[NameUser]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateUserResponse
            Retrieve a user

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.user.update_user(
                user_id="user_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_user(
            user_id,
            channels=channels,
            display_name=display_name,
            image_url=image_url,
            name=name,
            request_options=request_options,
        )
        return _response.data

    async def delete_user(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        user_id : str
            User ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Success response with empty JSON

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.user.delete_user(
                user_id="user_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_user(user_id, request_options=request_options)
        return _response.data

    async def getuser_conversations(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GetuserConversationsResponseItem]:
        """
        Parameters
        ----------
        user_id : str
            User ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GetuserConversationsResponseItem]
            List user conversations

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.user.getuser_conversations(
                user_id="user_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getuser_conversations(user_id, request_options=request_options)
        return _response.data

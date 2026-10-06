

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.deleted_avatar_response import DeletedAvatarResponse
from ..types.set_avatar_response import SetAvatarResponse
from .raw_client import AsyncRawAvatarsClient, RawAvatarsClient


OMIT = typing.cast(typing.Any, ...)


class AvatarsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAvatarsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAvatarsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAvatarsClient
        """
        return self._raw_client

    def set_avatar(
        self, *, authorization: str, avatar_data: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> SetAvatarResponse:
        """
        Установка аватарки у пользователя

        Parameters
        ----------
        authorization : str
            Enter the token with the 'Bearer:' prefix.

        avatar_data : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SetAvatarResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.avatars.set_avatar(
            authorization="Authorization",
        )
        """
        _response = self._raw_client.set_avatar(
            authorization=authorization, avatar_data=avatar_data, request_options=request_options
        )
        return _response.data

    def delete_avatar(
        self, *, authorization: str, request_options: typing.Optional[RequestOptions] = None
    ) -> DeletedAvatarResponse:
        """
        Удаление аватарки у пользователя

        Parameters
        ----------
        authorization : str
            Enter the token with the 'Bearer:' prefix.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeletedAvatarResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.avatars.delete_avatar(
            authorization="Authorization",
        )
        """
        _response = self._raw_client.delete_avatar(authorization=authorization, request_options=request_options)
        return _response.data


class AsyncAvatarsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAvatarsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAvatarsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAvatarsClient
        """
        return self._raw_client

    async def set_avatar(
        self, *, authorization: str, avatar_data: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> SetAvatarResponse:
        """
        Установка аватарки у пользователя

        Parameters
        ----------
        authorization : str
            Enter the token with the 'Bearer:' prefix.

        avatar_data : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SetAvatarResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.avatars.set_avatar(
                authorization="Authorization",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_avatar(
            authorization=authorization, avatar_data=avatar_data, request_options=request_options
        )
        return _response.data

    async def delete_avatar(
        self, *, authorization: str, request_options: typing.Optional[RequestOptions] = None
    ) -> DeletedAvatarResponse:
        """
        Удаление аватарки у пользователя

        Parameters
        ----------
        authorization : str
            Enter the token with the 'Bearer:' prefix.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeletedAvatarResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.avatars.delete_avatar(
                authorization="Authorization",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_avatar(authorization=authorization, request_options=request_options)
        return _response.data

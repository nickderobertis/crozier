

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.uc_user_vo import UcUserVo
from .raw_client import AsyncRawUserV1Alpha1UcClient, RawUserV1Alpha1UcClient


OMIT = typing.cast(typing.Any, ...)


class UserV1Alpha1UcClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUserV1Alpha1UcClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUserV1Alpha1UcClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUserV1Alpha1UcClient
        """
        return self._raw_client

    def get_my_user(self, *, request_options: typing.Optional[RequestOptions] = None) -> UcUserVo:
        """
        Get current user profile without password hash.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UcUserVo
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.user_v1alpha1uc.get_my_user()
        """
        _response = self._raw_client.get_my_user(request_options=request_options)
        return _response.data

    def change_my_password(
        self,
        *,
        password: str,
        old_password: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UcUserVo:
        """
        Set or change the password of the current user.

        Parameters
        ----------
        password : str
            new password of the current user

        old_password : typing.Optional[str]
            Old password. Required and verified only when the current user has a password; ignored otherwise.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UcUserVo
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.user_v1alpha1uc.change_my_password(
            password="password",
        )
        """
        _response = self._raw_client.change_my_password(
            password=password, old_password=old_password, request_options=request_options
        )
        return _response.data


class AsyncUserV1Alpha1UcClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUserV1Alpha1UcClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUserV1Alpha1UcClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUserV1Alpha1UcClient
        """
        return self._raw_client

    async def get_my_user(self, *, request_options: typing.Optional[RequestOptions] = None) -> UcUserVo:
        """
        Get current user profile without password hash.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UcUserVo
            default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.user_v1alpha1uc.get_my_user()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_my_user(request_options=request_options)
        return _response.data

    async def change_my_password(
        self,
        *,
        password: str,
        old_password: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UcUserVo:
        """
        Set or change the password of the current user.

        Parameters
        ----------
        password : str
            new password of the current user

        old_password : typing.Optional[str]
            Old password. Required and verified only when the current user has a password; ignored otherwise.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UcUserVo
            default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.user_v1alpha1uc.change_my_password(
                password="password",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.change_my_password(
            password=password, old_password=old_password, request_options=request_options
        )
        return _response.data

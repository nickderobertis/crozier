

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawUsersClient, RawUsersClient
from .types.delete_user_request_identification import DeleteUserRequestIdentification
from .types.delete_user_response import DeleteUserResponse
from .types.link_request_identification import LinkRequestIdentification
from .types.link_response import LinkResponse
from .types.upsert_user_request_identification import UpsertUserRequestIdentification
from .types.upsert_user_request_properties_value import UpsertUserRequestPropertiesValue
from .types.upsert_user_response import UpsertUserResponse


OMIT = typing.cast(typing.Any, ...)


class UsersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUsersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUsersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUsersClient
        """
        return self._raw_client

    def link(
        self,
        *,
        device_id: str,
        identification: LinkRequestIdentification,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LinkResponse:
        """
        💡 You don't need to use this endpoint if you use our JavaScript snippet in your application.

        This endpoint is used to link web activity to a user in your application. This will help you discover which channels and campaigns work best.

        When our JavaScript snippet is embedded on your website, blog or landing pages, a cookie named "__journey" will be set.

        This will only work if your website and application are under the same top level domain.

        Website, blog or landing pages
        * www.my-domain.tld
        * blog.my-domain.tld
        * landing-page.my-domain.tld

        Application
        * app.my-domain.tld

        The cookie on my-domain.tld will also be send to your app domain.

        You should call this endpoint after the user succesfully logged in (so that you know the user's ID). Use the value of the cookie as device ID.

        Parameters
        ----------
        device_id : str

        identification : LinkRequestIdentification
            User identification requires a userId, email or both

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LinkResponse
            Object was created

        Examples
        --------
        from fern.users import LinkRequestIdentification

        from fern import FernApi

        client = FernApi()
        client.users.link(
            device_id="deviceId",
            identification=LinkRequestIdentification(),
        )
        """
        _response = self._raw_client.link(
            device_id=device_id, identification=identification, request_options=request_options
        )
        return _response.data

    def delete_user(
        self,
        *,
        identification: DeleteUserRequestIdentification,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeleteUserResponse:
        """
        Endpoint to delete a user.

        Parameters
        ----------
        identification : DeleteUserRequestIdentification
            User identification requires a userId, email or both

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteUserResponse
            Accepted

        Examples
        --------
        from fern.users import DeleteUserRequestIdentification

        from fern import FernApi

        client = FernApi()
        client.users.delete_user(
            identification=DeleteUserRequestIdentification(),
        )
        """
        _response = self._raw_client.delete_user(identification=identification, request_options=request_options)
        return _response.data

    def upsert_user(
        self,
        *,
        identification: UpsertUserRequestIdentification,
        properties: typing.Optional[typing.Dict[str, UpsertUserRequestPropertiesValue]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpsertUserResponse:
        """
        Endpoint to create or update a user.

        Parameters
        ----------
        identification : UpsertUserRequestIdentification
            User identification requires a userId, email or both

        properties : typing.Optional[typing.Dict[str, UpsertUserRequestPropertiesValue]]
            The properties being set, possible values are strings, booleans, numbers and datetimes (ISO 8601)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpsertUserResponse
            User will be created

        Examples
        --------
        from fern.users import UpsertUserRequestIdentification

        from fern import FernApi

        client = FernApi()
        client.users.upsert_user(
            identification=UpsertUserRequestIdentification(),
        )
        """
        _response = self._raw_client.upsert_user(
            identification=identification, properties=properties, request_options=request_options
        )
        return _response.data


class AsyncUsersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUsersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUsersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUsersClient
        """
        return self._raw_client

    async def link(
        self,
        *,
        device_id: str,
        identification: LinkRequestIdentification,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LinkResponse:
        """
        💡 You don't need to use this endpoint if you use our JavaScript snippet in your application.

        This endpoint is used to link web activity to a user in your application. This will help you discover which channels and campaigns work best.

        When our JavaScript snippet is embedded on your website, blog or landing pages, a cookie named "__journey" will be set.

        This will only work if your website and application are under the same top level domain.

        Website, blog or landing pages
        * www.my-domain.tld
        * blog.my-domain.tld
        * landing-page.my-domain.tld

        Application
        * app.my-domain.tld

        The cookie on my-domain.tld will also be send to your app domain.

        You should call this endpoint after the user succesfully logged in (so that you know the user's ID). Use the value of the cookie as device ID.

        Parameters
        ----------
        device_id : str

        identification : LinkRequestIdentification
            User identification requires a userId, email or both

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LinkResponse
            Object was created

        Examples
        --------
        import asyncio

        from fern.users import LinkRequestIdentification

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.link(
                device_id="deviceId",
                identification=LinkRequestIdentification(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.link(
            device_id=device_id, identification=identification, request_options=request_options
        )
        return _response.data

    async def delete_user(
        self,
        *,
        identification: DeleteUserRequestIdentification,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeleteUserResponse:
        """
        Endpoint to delete a user.

        Parameters
        ----------
        identification : DeleteUserRequestIdentification
            User identification requires a userId, email or both

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteUserResponse
            Accepted

        Examples
        --------
        import asyncio

        from fern.users import DeleteUserRequestIdentification

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.delete_user(
                identification=DeleteUserRequestIdentification(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_user(identification=identification, request_options=request_options)
        return _response.data

    async def upsert_user(
        self,
        *,
        identification: UpsertUserRequestIdentification,
        properties: typing.Optional[typing.Dict[str, UpsertUserRequestPropertiesValue]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpsertUserResponse:
        """
        Endpoint to create or update a user.

        Parameters
        ----------
        identification : UpsertUserRequestIdentification
            User identification requires a userId, email or both

        properties : typing.Optional[typing.Dict[str, UpsertUserRequestPropertiesValue]]
            The properties being set, possible values are strings, booleans, numbers and datetimes (ISO 8601)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpsertUserResponse
            User will be created

        Examples
        --------
        import asyncio

        from fern.users import UpsertUserRequestIdentification

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.upsert_user(
                identification=UpsertUserRequestIdentification(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.upsert_user(
            identification=identification, properties=properties, request_options=request_options
        )
        return _response.data

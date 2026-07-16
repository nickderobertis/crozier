

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.create_mobile_authorization_code_response import CreateMobileAuthorizationCodeResponse
from .raw_client import AsyncRawMobileAuthorizationClient, RawMobileAuthorizationClient


OMIT = typing.cast(typing.Any, ...)


class MobileAuthorizationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMobileAuthorizationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMobileAuthorizationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMobileAuthorizationClient
        """
        return self._raw_client

    def create_mobile_authorization_code(
        self, *, location_id: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> CreateMobileAuthorizationCodeResponse:
        """
        Generates code to authorize a mobile application to connect to a Square card reader

        Authorization codes are one-time-use and expire __60 minutes__ after being issued.

        __Important:__ The `Authorization` header you provide to this endpoint must have the following format:

        ```
        Authorization: Bearer ACCESS_TOKEN
        ```

        Replace `ACCESS_TOKEN` with a
        [valid production authorization credential](https://developer.squareup.com/docs/build-basics/access-tokens).

        Parameters
        ----------
        location_id : typing.Optional[str]
            The Square location ID the authorization code should be tied to.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateMobileAuthorizationCodeResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.mobile_authorization.create_mobile_authorization_code()
        """
        _response = self._raw_client.create_mobile_authorization_code(
            location_id=location_id, request_options=request_options
        )
        return _response.data


class AsyncMobileAuthorizationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMobileAuthorizationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMobileAuthorizationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMobileAuthorizationClient
        """
        return self._raw_client

    async def create_mobile_authorization_code(
        self, *, location_id: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> CreateMobileAuthorizationCodeResponse:
        """
        Generates code to authorize a mobile application to connect to a Square card reader

        Authorization codes are one-time-use and expire __60 minutes__ after being issued.

        __Important:__ The `Authorization` header you provide to this endpoint must have the following format:

        ```
        Authorization: Bearer ACCESS_TOKEN
        ```

        Replace `ACCESS_TOKEN` with a
        [valid production authorization credential](https://developer.squareup.com/docs/build-basics/access-tokens).

        Parameters
        ----------
        location_id : typing.Optional[str]
            The Square location ID the authorization code should be tied to.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateMobileAuthorizationCodeResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.mobile_authorization.create_mobile_authorization_code()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_mobile_authorization_code(
            location_id=location_id, request_options=request_options
        )
        return _response.data

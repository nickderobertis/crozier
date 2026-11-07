

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.messenger_account_response import MessengerAccountResponse
from .raw_client import AsyncRawFacebookMessengerClient, RawFacebookMessengerClient
from .types.update_messenger_account_response import UpdateMessengerAccountResponse


OMIT = typing.cast(typing.Any, ...)


class FacebookMessengerClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFacebookMessengerClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFacebookMessengerClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFacebookMessengerClient
        """
        return self._raw_client

    def create_messenger_account(
        self,
        *,
        access_token: str,
        external_id: str,
        applications: typing.Optional[typing.Sequence[str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MessengerAccountResponse:
        """
        Parameters
        ----------
        access_token : str
            This is the Facebook Business Page token. You can obtain the token using one of the following methods:

            * Linking your Facebook Business Page to your account [with our Dashboard tool](https://dashboard.nexmo.com/messages/social-channels/facebook-connect)
            * Requesting a Page Access Token using the steps in the [Facebook token reference](https://developers.facebook.com/docs/pages/access-tokens/)

        external_id : str
            This is the unique identifier within the provider's domain. In this case it is the Page ID for your Facebook Page. Go to your Facebook Page, click "Settings", click "Messenger platform " scroll down to "Messenger link" to find your Page ID.

        applications : typing.Optional[typing.Sequence[str]]
            Contains a list of application IDs which are linked to the account. <ul> <li>There is just one application allowed per an account.</li> <li>The application type must be type "messages".</li> </ul> For more information see [Application API spec](https://developer.nexmo.com/api/application.v2)

        name : typing.Optional[str]
            Custom account name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessengerAccountResponse
            Created.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.facebook_messenger.create_messenger_account(
            access_token="myAccessToken",
            external_id="12345678",
        )
        """
        _response = self._raw_client.create_messenger_account(
            access_token=access_token,
            external_id=external_id,
            applications=applications,
            name=name,
            request_options=request_options,
        )
        return _response.data

    def get_messenger_account(
        self, external_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MessengerAccountResponse:
        """
        Parameters
        ----------
        external_id : str
            External id of the account you want to retrieve. In this case it is the Facebook Page ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessengerAccountResponse
            OK.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.facebook_messenger.get_messenger_account(
            external_id="external_id",
        )
        """
        _response = self._raw_client.get_messenger_account(external_id, request_options=request_options)
        return _response.data

    def delete_messenger_account(
        self, external_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        external_id : str
            External id of the account you want to delete. In this case it is the Facebook Page ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.facebook_messenger.delete_messenger_account(
            external_id="external_id",
        )
        """
        _response = self._raw_client.delete_messenger_account(external_id, request_options=request_options)
        return _response.data

    def update_messenger_account(
        self,
        external_id: str,
        *,
        access_token: typing.Optional[str] = OMIT,
        applications: typing.Optional[typing.Sequence[str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateMessengerAccountResponse:
        """
        Parameters
        ----------
        external_id : str
            External id of the account you want to update. In this case it is the Facebook Page ID.

        access_token : typing.Optional[str]

        applications : typing.Optional[typing.Sequence[str]]

        name : typing.Optional[str]
            The new account name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateMessengerAccountResponse
            OK.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.facebook_messenger.update_messenger_account(
            external_id="external_id",
        )
        """
        _response = self._raw_client.update_messenger_account(
            external_id,
            access_token=access_token,
            applications=applications,
            name=name,
            request_options=request_options,
        )
        return _response.data


class AsyncFacebookMessengerClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFacebookMessengerClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFacebookMessengerClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFacebookMessengerClient
        """
        return self._raw_client

    async def create_messenger_account(
        self,
        *,
        access_token: str,
        external_id: str,
        applications: typing.Optional[typing.Sequence[str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MessengerAccountResponse:
        """
        Parameters
        ----------
        access_token : str
            This is the Facebook Business Page token. You can obtain the token using one of the following methods:

            * Linking your Facebook Business Page to your account [with our Dashboard tool](https://dashboard.nexmo.com/messages/social-channels/facebook-connect)
            * Requesting a Page Access Token using the steps in the [Facebook token reference](https://developers.facebook.com/docs/pages/access-tokens/)

        external_id : str
            This is the unique identifier within the provider's domain. In this case it is the Page ID for your Facebook Page. Go to your Facebook Page, click "Settings", click "Messenger platform " scroll down to "Messenger link" to find your Page ID.

        applications : typing.Optional[typing.Sequence[str]]
            Contains a list of application IDs which are linked to the account. <ul> <li>There is just one application allowed per an account.</li> <li>The application type must be type "messages".</li> </ul> For more information see [Application API spec](https://developer.nexmo.com/api/application.v2)

        name : typing.Optional[str]
            Custom account name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessengerAccountResponse
            Created.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.facebook_messenger.create_messenger_account(
                access_token="myAccessToken",
                external_id="12345678",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_messenger_account(
            access_token=access_token,
            external_id=external_id,
            applications=applications,
            name=name,
            request_options=request_options,
        )
        return _response.data

    async def get_messenger_account(
        self, external_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MessengerAccountResponse:
        """
        Parameters
        ----------
        external_id : str
            External id of the account you want to retrieve. In this case it is the Facebook Page ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessengerAccountResponse
            OK.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.facebook_messenger.get_messenger_account(
                external_id="external_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_messenger_account(external_id, request_options=request_options)
        return _response.data

    async def delete_messenger_account(
        self, external_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        external_id : str
            External id of the account you want to delete. In this case it is the Facebook Page ID.

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
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.facebook_messenger.delete_messenger_account(
                external_id="external_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_messenger_account(external_id, request_options=request_options)
        return _response.data

    async def update_messenger_account(
        self,
        external_id: str,
        *,
        access_token: typing.Optional[str] = OMIT,
        applications: typing.Optional[typing.Sequence[str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateMessengerAccountResponse:
        """
        Parameters
        ----------
        external_id : str
            External id of the account you want to update. In this case it is the Facebook Page ID.

        access_token : typing.Optional[str]

        applications : typing.Optional[typing.Sequence[str]]

        name : typing.Optional[str]
            The new account name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateMessengerAccountResponse
            OK.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.facebook_messenger.update_messenger_account(
                external_id="external_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_messenger_account(
            external_id,
            access_token=access_token,
            applications=applications,
            name=name,
            request_options=request_options,
        )
        return _response.data

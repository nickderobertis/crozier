

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.log_list import LogList
from ..types.preferences import Preferences
from ..types.session import Session
from ..types.session_list import SessionList
from ..types.token import Token
from ..types.user import User
from .raw_client import AsyncRawAccountClient, RawAccountClient


OMIT = typing.cast(typing.Any, ...)


class AccountClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAccountClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAccountClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAccountClient
        """
        return self._raw_client

    def get(self, *, request_options: typing.Optional[RequestOptions] = None) -> User:
        """
        Get currently logged in user data as JSON object.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            User

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.account.get()
        """
        _response = self._raw_client.get(request_options=request_options)
        return _response.data

    def delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a currently logged in user account. Behind the scene, the user record is not deleted but permanently blocked from any access. This is done to avoid deleted accounts being overtaken by new users with the same email address. Any user-related resources like documents or storage files should be deleted separately.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.account.delete()
        """
        _response = self._raw_client.delete(request_options=request_options)
        return _response.data

    def update_email(
        self, *, email: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> User:
        """
        Update currently logged in user account email address. After changing user address, user confirmation status is being reset and a new confirmation mail is sent. For security measures, user password is required to complete this request.
        This endpoint can also be used to convert an anonymous account to a normal one, by passing an email address and a new password.

        Parameters
        ----------
        email : str
            User email.

        password : str
            User password. Must be between 6 to 32 chars.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            User

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.account.update_email(
            email="email",
            password="password",
        )
        """
        _response = self._raw_client.update_email(email=email, password=password, request_options=request_options)
        return _response.data

    def get_logs(self, *, request_options: typing.Optional[RequestOptions] = None) -> LogList:
        """
        Get currently logged in user list of latest security activity logs. Each log returns user IP address, location and date and time of log.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LogList
            Logs List

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.account.get_logs()
        """
        _response = self._raw_client.get_logs(request_options=request_options)
        return _response.data

    def update_name(self, *, name: str, request_options: typing.Optional[RequestOptions] = None) -> User:
        """
        Update currently logged in user account name.

        Parameters
        ----------
        name : str
            User name. Max length: 128 chars.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            User

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.account.update_name(
            name="name",
        )
        """
        _response = self._raw_client.update_name(name=name, request_options=request_options)
        return _response.data

    def update_password(
        self,
        *,
        password: str,
        old_password: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> User:
        """
        Update currently logged in user password. For validation, user is required to pass in the new password, and the old password. For users created with OAuth and Team Invites, oldPassword is optional.

        Parameters
        ----------
        password : str
            New user password. Must be between 6 to 32 chars.

        old_password : typing.Optional[str]
            Old user password. Must be between 6 to 32 chars.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            User

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.account.update_password(
            password="password",
        )
        """
        _response = self._raw_client.update_password(
            password=password, old_password=old_password, request_options=request_options
        )
        return _response.data

    def get_prefs(self, *, request_options: typing.Optional[RequestOptions] = None) -> Preferences:
        """
        Get currently logged in user preferences as a key-value object.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Preferences
            Preferences

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.account.get_prefs()
        """
        _response = self._raw_client.get_prefs(request_options=request_options)
        return _response.data

    def update_prefs(
        self,
        *,
        prefs: typing.Dict[str, typing.Optional[typing.Any]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> User:
        """
        Update currently logged in user account preferences. You can pass only the specific settings you wish to update.

        Parameters
        ----------
        prefs : typing.Dict[str, typing.Optional[typing.Any]]
            Prefs key-value JSON object.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            User

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.account.update_prefs(
            prefs={"key": "value"},
        )
        """
        _response = self._raw_client.update_prefs(prefs=prefs, request_options=request_options)
        return _response.data

    def create_recovery(
        self, *, email: str, url: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Token:
        """
        Sends the user an email with a temporary secret key for password reset. When the user clicks the confirmation link he is redirected back to your app password reset URL with the secret key and email address values attached to the URL query string. Use the query string params to submit a request to the [PUT /account/recovery](/docs/client/account#accountUpdateRecovery) endpoint to complete the process. The verification link sent to the user's email address is valid for 1 hour.

        Parameters
        ----------
        email : str
            User email.

        url : str
            URL to redirect the user back to your app from the recovery email. Only URLs from hostnames in your project platform list are allowed. This requirement helps to prevent an [open redirect](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html) attack against your project API.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Token
            Token

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.account.create_recovery(
            email="email",
            url="url",
        )
        """
        _response = self._raw_client.create_recovery(email=email, url=url, request_options=request_options)
        return _response.data

    def update_recovery(
        self,
        *,
        password: str,
        password_again: str,
        secret: str,
        user_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Token:
        """
        Use this endpoint to complete the user account password reset. Both the **userId** and **secret** arguments will be passed as query parameters to the redirect URL you have provided when sending your request to the [POST /account/recovery](/docs/client/account#accountCreateRecovery) endpoint.

        Please note that in order to avoid a [Redirect Attack](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.md) the only valid redirect URLs are the ones from domains you have set when adding your platforms in the console interface.

        Parameters
        ----------
        password : str
            New password. Must be between 6 to 32 chars.

        password_again : str
            New password again. Must be between 6 to 32 chars.

        secret : str
            Valid reset token.

        user_id : str
            User account UID address.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Token
            Token

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.account.update_recovery(
            password="password",
            password_again="passwordAgain",
            secret="secret",
            user_id="userId",
        )
        """
        _response = self._raw_client.update_recovery(
            password=password,
            password_again=password_again,
            secret=secret,
            user_id=user_id,
            request_options=request_options,
        )
        return _response.data

    def get_sessions(self, *, request_options: typing.Optional[RequestOptions] = None) -> SessionList:
        """
        Get currently logged in user list of active sessions across different devices.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SessionList
            Sessions List

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.account.get_sessions()
        """
        _response = self._raw_client.get_sessions(request_options=request_options)
        return _response.data

    def delete_sessions(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete all sessions from the user account and remove any sessions cookies from the end client.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.account.delete_sessions()
        """
        _response = self._raw_client.delete_sessions(request_options=request_options)
        return _response.data

    def get_session(self, session_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Session:
        """
        Use this endpoint to get a logged in user's session using a Session ID. Inputting 'current' will return the current session being used.

        Parameters
        ----------
        session_id : str
            Session unique ID. Use the string 'current' to get the current device session.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Session
            Session

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.account.get_session(
            session_id="sessionId",
        )
        """
        _response = self._raw_client.get_session(session_id, request_options=request_options)
        return _response.data

    def delete_session(self, session_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Use this endpoint to log out the currently logged in user from all their account sessions across all of their different devices. When using the option id argument, only the session unique ID provider will be deleted.

        Parameters
        ----------
        session_id : str
            Session unique ID. Use the string 'current' to delete the current device session.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.account.delete_session(
            session_id="sessionId",
        )
        """
        _response = self._raw_client.delete_session(session_id, request_options=request_options)
        return _response.data

    def create_verification(self, *, url: str, request_options: typing.Optional[RequestOptions] = None) -> Token:
        """
        Use this endpoint to send a verification message to your user email address to confirm they are the valid owners of that address. Both the **userId** and **secret** arguments will be passed as query parameters to the URL you have provided to be attached to the verification email. The provided URL should redirect the user back to your app and allow you to complete the verification process by verifying both the **userId** and **secret** parameters. Learn more about how to [complete the verification process](/docs/client/account#accountUpdateVerification). The verification link sent to the user's email address is valid for 7 days.

        Please note that in order to avoid a [Redirect Attack](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.md), the only valid redirect URLs are the ones from domains you have set when adding your platforms in the console interface.

        Parameters
        ----------
        url : str
            URL to redirect the user back to your app from the verification email. Only URLs from hostnames in your project platform list are allowed. This requirement helps to prevent an [open redirect](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html) attack against your project API.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Token
            Token

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.account.create_verification(
            url="url",
        )
        """
        _response = self._raw_client.create_verification(url=url, request_options=request_options)
        return _response.data

    def update_verification(
        self, *, secret: str, user_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Token:
        """
        Use this endpoint to complete the user email verification process. Use both the **userId** and **secret** parameters that were attached to your app URL to verify the user email ownership. If confirmed this route will return a 200 status code.

        Parameters
        ----------
        secret : str
            Valid verification token.

        user_id : str
            User unique ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Token
            Token

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.account.update_verification(
            secret="secret",
            user_id="userId",
        )
        """
        _response = self._raw_client.update_verification(
            secret=secret, user_id=user_id, request_options=request_options
        )
        return _response.data


class AsyncAccountClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAccountClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAccountClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAccountClient
        """
        return self._raw_client

    async def get(self, *, request_options: typing.Optional[RequestOptions] = None) -> User:
        """
        Get currently logged in user data as JSON object.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            User

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.account.get()


        asyncio.run(main())
        """
        _response = await self._raw_client.get(request_options=request_options)
        return _response.data

    async def delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a currently logged in user account. Behind the scene, the user record is not deleted but permanently blocked from any access. This is done to avoid deleted accounts being overtaken by new users with the same email address. Any user-related resources like documents or storage files should be deleted separately.

        Parameters
        ----------
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
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.account.delete()


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(request_options=request_options)
        return _response.data

    async def update_email(
        self, *, email: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> User:
        """
        Update currently logged in user account email address. After changing user address, user confirmation status is being reset and a new confirmation mail is sent. For security measures, user password is required to complete this request.
        This endpoint can also be used to convert an anonymous account to a normal one, by passing an email address and a new password.

        Parameters
        ----------
        email : str
            User email.

        password : str
            User password. Must be between 6 to 32 chars.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            User

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.account.update_email(
                email="email",
                password="password",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_email(email=email, password=password, request_options=request_options)
        return _response.data

    async def get_logs(self, *, request_options: typing.Optional[RequestOptions] = None) -> LogList:
        """
        Get currently logged in user list of latest security activity logs. Each log returns user IP address, location and date and time of log.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LogList
            Logs List

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.account.get_logs()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_logs(request_options=request_options)
        return _response.data

    async def update_name(self, *, name: str, request_options: typing.Optional[RequestOptions] = None) -> User:
        """
        Update currently logged in user account name.

        Parameters
        ----------
        name : str
            User name. Max length: 128 chars.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            User

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.account.update_name(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_name(name=name, request_options=request_options)
        return _response.data

    async def update_password(
        self,
        *,
        password: str,
        old_password: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> User:
        """
        Update currently logged in user password. For validation, user is required to pass in the new password, and the old password. For users created with OAuth and Team Invites, oldPassword is optional.

        Parameters
        ----------
        password : str
            New user password. Must be between 6 to 32 chars.

        old_password : typing.Optional[str]
            Old user password. Must be between 6 to 32 chars.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            User

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.account.update_password(
                password="password",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_password(
            password=password, old_password=old_password, request_options=request_options
        )
        return _response.data

    async def get_prefs(self, *, request_options: typing.Optional[RequestOptions] = None) -> Preferences:
        """
        Get currently logged in user preferences as a key-value object.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Preferences
            Preferences

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.account.get_prefs()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_prefs(request_options=request_options)
        return _response.data

    async def update_prefs(
        self,
        *,
        prefs: typing.Dict[str, typing.Optional[typing.Any]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> User:
        """
        Update currently logged in user account preferences. You can pass only the specific settings you wish to update.

        Parameters
        ----------
        prefs : typing.Dict[str, typing.Optional[typing.Any]]
            Prefs key-value JSON object.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            User

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.account.update_prefs(
                prefs={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_prefs(prefs=prefs, request_options=request_options)
        return _response.data

    async def create_recovery(
        self, *, email: str, url: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Token:
        """
        Sends the user an email with a temporary secret key for password reset. When the user clicks the confirmation link he is redirected back to your app password reset URL with the secret key and email address values attached to the URL query string. Use the query string params to submit a request to the [PUT /account/recovery](/docs/client/account#accountUpdateRecovery) endpoint to complete the process. The verification link sent to the user's email address is valid for 1 hour.

        Parameters
        ----------
        email : str
            User email.

        url : str
            URL to redirect the user back to your app from the recovery email. Only URLs from hostnames in your project platform list are allowed. This requirement helps to prevent an [open redirect](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html) attack against your project API.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Token
            Token

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.account.create_recovery(
                email="email",
                url="url",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_recovery(email=email, url=url, request_options=request_options)
        return _response.data

    async def update_recovery(
        self,
        *,
        password: str,
        password_again: str,
        secret: str,
        user_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Token:
        """
        Use this endpoint to complete the user account password reset. Both the **userId** and **secret** arguments will be passed as query parameters to the redirect URL you have provided when sending your request to the [POST /account/recovery](/docs/client/account#accountCreateRecovery) endpoint.

        Please note that in order to avoid a [Redirect Attack](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.md) the only valid redirect URLs are the ones from domains you have set when adding your platforms in the console interface.

        Parameters
        ----------
        password : str
            New password. Must be between 6 to 32 chars.

        password_again : str
            New password again. Must be between 6 to 32 chars.

        secret : str
            Valid reset token.

        user_id : str
            User account UID address.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Token
            Token

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.account.update_recovery(
                password="password",
                password_again="passwordAgain",
                secret="secret",
                user_id="userId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_recovery(
            password=password,
            password_again=password_again,
            secret=secret,
            user_id=user_id,
            request_options=request_options,
        )
        return _response.data

    async def get_sessions(self, *, request_options: typing.Optional[RequestOptions] = None) -> SessionList:
        """
        Get currently logged in user list of active sessions across different devices.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SessionList
            Sessions List

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.account.get_sessions()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_sessions(request_options=request_options)
        return _response.data

    async def delete_sessions(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete all sessions from the user account and remove any sessions cookies from the end client.

        Parameters
        ----------
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
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.account.delete_sessions()


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_sessions(request_options=request_options)
        return _response.data

    async def get_session(self, session_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Session:
        """
        Use this endpoint to get a logged in user's session using a Session ID. Inputting 'current' will return the current session being used.

        Parameters
        ----------
        session_id : str
            Session unique ID. Use the string 'current' to get the current device session.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Session
            Session

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.account.get_session(
                session_id="sessionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_session(session_id, request_options=request_options)
        return _response.data

    async def delete_session(self, session_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Use this endpoint to log out the currently logged in user from all their account sessions across all of their different devices. When using the option id argument, only the session unique ID provider will be deleted.

        Parameters
        ----------
        session_id : str
            Session unique ID. Use the string 'current' to delete the current device session.

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
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.account.delete_session(
                session_id="sessionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_session(session_id, request_options=request_options)
        return _response.data

    async def create_verification(self, *, url: str, request_options: typing.Optional[RequestOptions] = None) -> Token:
        """
        Use this endpoint to send a verification message to your user email address to confirm they are the valid owners of that address. Both the **userId** and **secret** arguments will be passed as query parameters to the URL you have provided to be attached to the verification email. The provided URL should redirect the user back to your app and allow you to complete the verification process by verifying both the **userId** and **secret** parameters. Learn more about how to [complete the verification process](/docs/client/account#accountUpdateVerification). The verification link sent to the user's email address is valid for 7 days.

        Please note that in order to avoid a [Redirect Attack](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.md), the only valid redirect URLs are the ones from domains you have set when adding your platforms in the console interface.

        Parameters
        ----------
        url : str
            URL to redirect the user back to your app from the verification email. Only URLs from hostnames in your project platform list are allowed. This requirement helps to prevent an [open redirect](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html) attack against your project API.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Token
            Token

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.account.create_verification(
                url="url",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_verification(url=url, request_options=request_options)
        return _response.data

    async def update_verification(
        self, *, secret: str, user_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Token:
        """
        Use this endpoint to complete the user email verification process. Use both the **userId** and **secret** parameters that were attached to your app URL to verify the user email ownership. If confirmed this route will return a 200 status code.

        Parameters
        ----------
        secret : str
            Valid verification token.

        user_id : str
            User unique ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Token
            Token

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.account.update_verification(
                secret="secret",
                user_id="userId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_verification(
            secret=secret, user_id=user_id, request_options=request_options
        )
        return _response.data

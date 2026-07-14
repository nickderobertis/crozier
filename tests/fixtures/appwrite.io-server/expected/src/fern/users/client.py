

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.log_list import LogList
from ..types.preferences import Preferences
from ..types.session_list import SessionList
from ..types.user import User
from ..types.user_list import UserList
from .raw_client import AsyncRawUsersClient, RawUsersClient


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

    def list(
        self,
        *,
        search: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order_type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UserList:
        """
        Get a list of all the project's users. You can use the query params to filter your results.

        Parameters
        ----------
        search : typing.Optional[str]
            Search term to filter your list results. Max length: 256 chars.

        limit : typing.Optional[int]
            Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request.

        offset : typing.Optional[int]
            Results offset. The default value is 0. Use this param to manage pagination.

        order_type : typing.Optional[str]
            Order result by ASC or DESC order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserList
            Users List

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.users.list()
        """
        _response = self._raw_client.list(
            search=search, limit=limit, offset=offset, order_type=order_type, request_options=request_options
        )
        return _response.data

    def create(
        self,
        *,
        email: str,
        password: str,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> User:
        """
        Create a new user.

        Parameters
        ----------
        email : str
            User email.

        password : str
            User password. Must be between 6 to 32 chars.

        name : typing.Optional[str]
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
        client.users.create(
            email="email",
            password="password",
        )
        """
        _response = self._raw_client.create(email=email, password=password, name=name, request_options=request_options)
        return _response.data

    def get(self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> User:
        """
        Get a user by its unique ID.

        Parameters
        ----------
        user_id : str
            User unique ID.

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
        client.users.get(
            user_id="userId",
        )
        """
        _response = self._raw_client.get(user_id, request_options=request_options)
        return _response.data

    def delete(self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a user by its unique ID.

        Parameters
        ----------
        user_id : str
            User unique ID.

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
        client.users.delete(
            user_id="userId",
        )
        """
        _response = self._raw_client.delete(user_id, request_options=request_options)
        return _response.data

    def get_logs(self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> LogList:
        """
        Get a user activity logs list by its unique ID.

        Parameters
        ----------
        user_id : str
            User unique ID.

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
        client.users.get_logs(
            user_id="userId",
        )
        """
        _response = self._raw_client.get_logs(user_id, request_options=request_options)
        return _response.data

    def get_prefs(self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Preferences:
        """
        Get the user preferences by its unique ID.

        Parameters
        ----------
        user_id : str
            User unique ID.

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
        client.users.get_prefs(
            user_id="userId",
        )
        """
        _response = self._raw_client.get_prefs(user_id, request_options=request_options)
        return _response.data

    def update_prefs(
        self,
        user_id: str,
        *,
        prefs: typing.Dict[str, typing.Optional[typing.Any]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Preferences:
        """
        Update the user preferences by its unique ID. You can pass only the specific settings you wish to update.

        Parameters
        ----------
        user_id : str
            User unique ID.

        prefs : typing.Dict[str, typing.Optional[typing.Any]]
            Prefs key-value JSON object.

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
        client.users.update_prefs(
            user_id="userId",
            prefs={"key": "value"},
        )
        """
        _response = self._raw_client.update_prefs(user_id, prefs=prefs, request_options=request_options)
        return _response.data

    def get_sessions(self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> SessionList:
        """
        Get the user sessions list by its unique ID.

        Parameters
        ----------
        user_id : str
            User unique ID.

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
        client.users.get_sessions(
            user_id="userId",
        )
        """
        _response = self._raw_client.get_sessions(user_id, request_options=request_options)
        return _response.data

    def delete_sessions(self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete all user's sessions by using the user's unique ID.

        Parameters
        ----------
        user_id : str
            User unique ID.

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
        client.users.delete_sessions(
            user_id="userId",
        )
        """
        _response = self._raw_client.delete_sessions(user_id, request_options=request_options)
        return _response.data

    def delete_session(
        self, user_id: str, session_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a user sessions by its unique ID.

        Parameters
        ----------
        user_id : str
            User unique ID.

        session_id : str
            User unique session ID.

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
        client.users.delete_session(
            user_id="userId",
            session_id="sessionId",
        )
        """
        _response = self._raw_client.delete_session(user_id, session_id, request_options=request_options)
        return _response.data

    def update_status(
        self, user_id: str, *, status: int, request_options: typing.Optional[RequestOptions] = None
    ) -> User:
        """
        Update the user status by its unique ID.

        Parameters
        ----------
        user_id : str
            User unique ID.

        status : int
            User Status code. To activate the user pass 1, to block the user pass 2 and for disabling the user pass 0

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
        client.users.update_status(
            user_id="userId",
            status=1,
        )
        """
        _response = self._raw_client.update_status(user_id, status=status, request_options=request_options)
        return _response.data

    def update_verification(
        self, user_id: str, *, email_verification: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> User:
        """
        Update the user email verification status by its unique ID.

        Parameters
        ----------
        user_id : str
            User unique ID.

        email_verification : bool
            User Email Verification Status.

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
        client.users.update_verification(
            user_id="userId",
            email_verification=True,
        )
        """
        _response = self._raw_client.update_verification(
            user_id, email_verification=email_verification, request_options=request_options
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

    async def list(
        self,
        *,
        search: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order_type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UserList:
        """
        Get a list of all the project's users. You can use the query params to filter your results.

        Parameters
        ----------
        search : typing.Optional[str]
            Search term to filter your list results. Max length: 256 chars.

        limit : typing.Optional[int]
            Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request.

        offset : typing.Optional[int]
            Results offset. The default value is 0. Use this param to manage pagination.

        order_type : typing.Optional[str]
            Order result by ASC or DESC order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserList
            Users List

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
            await client.users.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(
            search=search, limit=limit, offset=offset, order_type=order_type, request_options=request_options
        )
        return _response.data

    async def create(
        self,
        *,
        email: str,
        password: str,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> User:
        """
        Create a new user.

        Parameters
        ----------
        email : str
            User email.

        password : str
            User password. Must be between 6 to 32 chars.

        name : typing.Optional[str]
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
            await client.users.create(
                email="email",
                password="password",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(
            email=email, password=password, name=name, request_options=request_options
        )
        return _response.data

    async def get(self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> User:
        """
        Get a user by its unique ID.

        Parameters
        ----------
        user_id : str
            User unique ID.

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
            await client.users.get(
                user_id="userId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(user_id, request_options=request_options)
        return _response.data

    async def delete(self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a user by its unique ID.

        Parameters
        ----------
        user_id : str
            User unique ID.

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
            await client.users.delete(
                user_id="userId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(user_id, request_options=request_options)
        return _response.data

    async def get_logs(self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> LogList:
        """
        Get a user activity logs list by its unique ID.

        Parameters
        ----------
        user_id : str
            User unique ID.

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
            await client.users.get_logs(
                user_id="userId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_logs(user_id, request_options=request_options)
        return _response.data

    async def get_prefs(self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Preferences:
        """
        Get the user preferences by its unique ID.

        Parameters
        ----------
        user_id : str
            User unique ID.

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
            await client.users.get_prefs(
                user_id="userId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_prefs(user_id, request_options=request_options)
        return _response.data

    async def update_prefs(
        self,
        user_id: str,
        *,
        prefs: typing.Dict[str, typing.Optional[typing.Any]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Preferences:
        """
        Update the user preferences by its unique ID. You can pass only the specific settings you wish to update.

        Parameters
        ----------
        user_id : str
            User unique ID.

        prefs : typing.Dict[str, typing.Optional[typing.Any]]
            Prefs key-value JSON object.

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
            await client.users.update_prefs(
                user_id="userId",
                prefs={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_prefs(user_id, prefs=prefs, request_options=request_options)
        return _response.data

    async def get_sessions(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SessionList:
        """
        Get the user sessions list by its unique ID.

        Parameters
        ----------
        user_id : str
            User unique ID.

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
            await client.users.get_sessions(
                user_id="userId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_sessions(user_id, request_options=request_options)
        return _response.data

    async def delete_sessions(self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete all user's sessions by using the user's unique ID.

        Parameters
        ----------
        user_id : str
            User unique ID.

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
            await client.users.delete_sessions(
                user_id="userId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_sessions(user_id, request_options=request_options)
        return _response.data

    async def delete_session(
        self, user_id: str, session_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a user sessions by its unique ID.

        Parameters
        ----------
        user_id : str
            User unique ID.

        session_id : str
            User unique session ID.

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
            await client.users.delete_session(
                user_id="userId",
                session_id="sessionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_session(user_id, session_id, request_options=request_options)
        return _response.data

    async def update_status(
        self, user_id: str, *, status: int, request_options: typing.Optional[RequestOptions] = None
    ) -> User:
        """
        Update the user status by its unique ID.

        Parameters
        ----------
        user_id : str
            User unique ID.

        status : int
            User Status code. To activate the user pass 1, to block the user pass 2 and for disabling the user pass 0

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
            await client.users.update_status(
                user_id="userId",
                status=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_status(user_id, status=status, request_options=request_options)
        return _response.data

    async def update_verification(
        self, user_id: str, *, email_verification: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> User:
        """
        Update the user email verification status by its unique ID.

        Parameters
        ----------
        user_id : str
            User unique ID.

        email_verification : bool
            User Email Verification Status.

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
            await client.users.update_verification(
                user_id="userId",
                email_verification=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_verification(
            user_id, email_verification=email_verification, request_options=request_options
        )
        return _response.data

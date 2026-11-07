

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.login_step import LoginStep
from ..types.user_login_id import UserLoginId
from ..types.whoami import Whoami
from .raw_client import AsyncRawAuthClient, RawAuthClient
from .types.get_login_flows_response import GetLoginFlowsResponse
from .types.get_login_i_ds_response import GetLoginIDsResponse
from .types.logout_request_login_id import LogoutRequestLoginId


OMIT = typing.cast(typing.Any, ...)


class AuthClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAuthClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAuthClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAuthClient
        """
        return self._raw_client

    def whoami(self, *, request_options: typing.Optional[RequestOptions] = None) -> Whoami:
        """
        Get all info that is useful for presenting this bridge in a manager interface.
        * Server details: remote network details, available login flows, homeserver name, bridge bot user ID, command prefix
        * User details: management room ID, list of logins with current state and info

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Whoami
            Successfully fetched info

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.auth.whoami()
        """
        _response = self._raw_client.whoami(request_options=request_options)
        return _response.data

    def get_login_flows(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetLoginFlowsResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetLoginFlowsResponse
            Successfully fetched flows

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.auth.get_login_flows()
        """
        _response = self._raw_client.get_login_flows(request_options=request_options)
        return _response.data

    def get_login_i_ds(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetLoginIDsResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetLoginIDsResponse
            Successfully fetched list of logins

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.auth.get_login_i_ds()
        """
        _response = self._raw_client.get_login_i_ds(request_options=request_options)
        return _response.data

    def start_login(
        self,
        flow_id: str,
        *,
        login_id: typing.Optional[UserLoginId] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LoginStep:
        """
        This endpoint starts a new login process, which is used to log into the bridge.

        The basic flow of the entire login, including calling this endpoint, is:
        1. Call `GET /v3/login/flows` to get the list of available flows.
           If there's more than one flow, ask the user to pick which one they want to use.
        2. Call this endpoint with the chosen flow ID to start the login.
           The first login step will be returned.
        3. Render the information provided in the step.
        4. Call the `/login/step/...` endpoint corresponding to the step type:
           * For `user_input` and `cookies`, acquire the requested fields before calling the endpoint.
           * For `display_and_wait`, call the endpoint immediately
             (as there's nothing to acquire on the client side).
        5. Handle the data returned by the login step endpoint:
           * If an error is returned, the login has failed and must be restarted
             (from either step 1 or step 2) if the user wants to try again.
           * If step type `complete` is returned, the login finished successfully.
           * Otherwise, go to step 3 with the new data.

        Parameters
        ----------
        flow_id : str
            The login flow ID to use.

        login_id : typing.Optional[UserLoginId]
            An existing login ID to re-login as. If this is specified and the user logs into a different account, the provided ID will be logged out.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LoginStep
            Login successfully started

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.auth.start_login(
            flow_id="qr",
            login_id="bcc68892-b180-414f-9516-b4aadf7d0496",
        )
        """
        _response = self._raw_client.start_login(flow_id, login_id=login_id, request_options=request_options)
        return _response.data

    def submit_login_step_user_input(
        self,
        login_process_id: str,
        step_id: str,
        *,
        request: typing.Dict[str, str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LoginStep:
        """
        Parameters
        ----------
        login_process_id : str
            The ID of the login process, as returned in the `login_id` field of the start call.

        step_id : str
            The ID of the step being submitted, as returned in the `step_id` field of the start call or the previous submit call.

        request : typing.Dict[str, str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LoginStep
            Step submission successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.auth.submit_login_step_user_input(
            login_process_id="loginProcessID",
            step_id="stepID",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.submit_login_step_user_input(
            login_process_id, step_id, request=request, request_options=request_options
        )
        return _response.data

    def submit_login_step_cookies(
        self,
        login_process_id: str,
        step_id: str,
        *,
        request: typing.Dict[str, str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LoginStep:
        """
        Parameters
        ----------
        login_process_id : str
            The ID of the login process, as returned in the `login_id` field of the start call.

        step_id : str
            The ID of the step being submitted, as returned in the `step_id` field of the start call or the previous submit call.

        request : typing.Dict[str, str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LoginStep
            Step submission successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.auth.submit_login_step_cookies(
            login_process_id="loginProcessID",
            step_id="stepID",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.submit_login_step_cookies(
            login_process_id, step_id, request=request, request_options=request_options
        )
        return _response.data

    def submit_login_step_display_and_wait(
        self, login_process_id: str, step_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> LoginStep:
        """
        Parameters
        ----------
        login_process_id : str
            The ID of the login process, as returned in the `login_id` field of the start call.

        step_id : str
            The ID of the step being submitted, as returned in the `step_id` field of the start call or the previous submit call.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LoginStep
            Step submission successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.auth.submit_login_step_display_and_wait(
            login_process_id="loginProcessID",
            step_id="stepID",
        )
        """
        _response = self._raw_client.submit_login_step_display_and_wait(
            login_process_id, step_id, request_options=request_options
        )
        return _response.data

    def logout(
        self, login_id: LogoutRequestLoginId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        login_id : LogoutRequestLoginId
            The ID of the login to log out. Use `all` to log out of all logins.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Login was successfully deleted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.auth.logout(
            login_id="bcc68892-b180-414f-9516-b4aadf7d0496",
        )
        """
        _response = self._raw_client.logout(login_id, request_options=request_options)
        return _response.data


class AsyncAuthClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAuthClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAuthClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAuthClient
        """
        return self._raw_client

    async def whoami(self, *, request_options: typing.Optional[RequestOptions] = None) -> Whoami:
        """
        Get all info that is useful for presenting this bridge in a manager interface.
        * Server details: remote network details, available login flows, homeserver name, bridge bot user ID, command prefix
        * User details: management room ID, list of logins with current state and info

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Whoami
            Successfully fetched info

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.auth.whoami()


        asyncio.run(main())
        """
        _response = await self._raw_client.whoami(request_options=request_options)
        return _response.data

    async def get_login_flows(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetLoginFlowsResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetLoginFlowsResponse
            Successfully fetched flows

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.auth.get_login_flows()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_login_flows(request_options=request_options)
        return _response.data

    async def get_login_i_ds(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetLoginIDsResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetLoginIDsResponse
            Successfully fetched list of logins

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.auth.get_login_i_ds()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_login_i_ds(request_options=request_options)
        return _response.data

    async def start_login(
        self,
        flow_id: str,
        *,
        login_id: typing.Optional[UserLoginId] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LoginStep:
        """
        This endpoint starts a new login process, which is used to log into the bridge.

        The basic flow of the entire login, including calling this endpoint, is:
        1. Call `GET /v3/login/flows` to get the list of available flows.
           If there's more than one flow, ask the user to pick which one they want to use.
        2. Call this endpoint with the chosen flow ID to start the login.
           The first login step will be returned.
        3. Render the information provided in the step.
        4. Call the `/login/step/...` endpoint corresponding to the step type:
           * For `user_input` and `cookies`, acquire the requested fields before calling the endpoint.
           * For `display_and_wait`, call the endpoint immediately
             (as there's nothing to acquire on the client side).
        5. Handle the data returned by the login step endpoint:
           * If an error is returned, the login has failed and must be restarted
             (from either step 1 or step 2) if the user wants to try again.
           * If step type `complete` is returned, the login finished successfully.
           * Otherwise, go to step 3 with the new data.

        Parameters
        ----------
        flow_id : str
            The login flow ID to use.

        login_id : typing.Optional[UserLoginId]
            An existing login ID to re-login as. If this is specified and the user logs into a different account, the provided ID will be logged out.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LoginStep
            Login successfully started

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.auth.start_login(
                flow_id="qr",
                login_id="bcc68892-b180-414f-9516-b4aadf7d0496",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.start_login(flow_id, login_id=login_id, request_options=request_options)
        return _response.data

    async def submit_login_step_user_input(
        self,
        login_process_id: str,
        step_id: str,
        *,
        request: typing.Dict[str, str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LoginStep:
        """
        Parameters
        ----------
        login_process_id : str
            The ID of the login process, as returned in the `login_id` field of the start call.

        step_id : str
            The ID of the step being submitted, as returned in the `step_id` field of the start call or the previous submit call.

        request : typing.Dict[str, str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LoginStep
            Step submission successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.auth.submit_login_step_user_input(
                login_process_id="loginProcessID",
                step_id="stepID",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.submit_login_step_user_input(
            login_process_id, step_id, request=request, request_options=request_options
        )
        return _response.data

    async def submit_login_step_cookies(
        self,
        login_process_id: str,
        step_id: str,
        *,
        request: typing.Dict[str, str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LoginStep:
        """
        Parameters
        ----------
        login_process_id : str
            The ID of the login process, as returned in the `login_id` field of the start call.

        step_id : str
            The ID of the step being submitted, as returned in the `step_id` field of the start call or the previous submit call.

        request : typing.Dict[str, str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LoginStep
            Step submission successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.auth.submit_login_step_cookies(
                login_process_id="loginProcessID",
                step_id="stepID",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.submit_login_step_cookies(
            login_process_id, step_id, request=request, request_options=request_options
        )
        return _response.data

    async def submit_login_step_display_and_wait(
        self, login_process_id: str, step_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> LoginStep:
        """
        Parameters
        ----------
        login_process_id : str
            The ID of the login process, as returned in the `login_id` field of the start call.

        step_id : str
            The ID of the step being submitted, as returned in the `step_id` field of the start call or the previous submit call.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LoginStep
            Step submission successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.auth.submit_login_step_display_and_wait(
                login_process_id="loginProcessID",
                step_id="stepID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.submit_login_step_display_and_wait(
            login_process_id, step_id, request_options=request_options
        )
        return _response.data

    async def logout(
        self, login_id: LogoutRequestLoginId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        login_id : LogoutRequestLoginId
            The ID of the login to log out. Use `all` to log out of all logins.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Login was successfully deleted

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.auth.logout(
                login_id="bcc68892-b180-414f-9516-b4aadf7d0496",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.logout(login_id, request_options=request_options)
        return _response.data

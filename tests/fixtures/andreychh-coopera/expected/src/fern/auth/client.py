

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.code import Code
from ..types.code_delivery import CodeDelivery
from ..types.email import Email
from ..types.pass_ import Pass
from .raw_client import AsyncRawAuthClient, RawAuthClient


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

    def create_code(self, *, email: Email, request_options: typing.Optional[RequestOptions] = None) -> CodeDelivery:
        """
        Sends a one-time code to the given address. The answer is the same whether or not an account already exists behind that address: telling the two apart would turn this into a directory of registered people. The code travels by mail only and is never part of any response.

        Parameters
        ----------
        email : Email

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CodeDelivery
            The code was sent. Nothing here says whether an account exists, and nothing here promises the mail arrived — delivery is the only real test, and its outcome belongs to the mailbox, not to this answer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.auth.create_code(
            email="email",
        )
        """
        _response = self._raw_client.create_code(email=email, request_options=request_options)
        return _response.data

    def create_session(
        self, *, email: Email, code: Code, request_options: typing.Optional[RequestOptions] = None
    ) -> Pass:
        """
        Exchanges an emailed code for a pass. The account comes into being here if the address had none: signing in and signing up are one act, because separating them would mean saying whether the address is known, and that is what this API refuses to say. The code is checked together with the address it was issued for — six digits are not unique, and alone they identify nobody.

        Parameters
        ----------
        email : Email

        code : Code

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Pass
            Signed in. The answer does not say whether the account was born just now: that is a state, not an event, and it is read from the person, not from this moment.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.auth.create_session(
            email="email",
            code="code",
        )
        """
        _response = self._raw_client.create_session(email=email, code=code, request_options=request_options)
        return _response.data

    def delete_session(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Ends the session the presented token belongs to, on this device only — the other devices a person is signed in on know nothing of it.
        It takes effect at once, including for the access token just used. That token is not recalled and cannot be: it is believed on its signature alone. But every guarded operation asks after the session behind the token it was shown, and from here on the answer is that there is none. The refresh token goes the same way and for the same reason — it buys keys to a session, and there is no longer a session to buy them for. Neither is crossed out one by one; both die of what they point at.
        Signing out twice answers 401 rather than 204. The second attempt arrives holding a pass that no longer stands, and is turned away before it can be read as a request at all — the same answer every other operation now gives it.

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
            token="YOUR_TOKEN",
        )
        client.auth.delete_session()
        """
        _response = self._raw_client.delete_session(request_options=request_options)
        return _response.data

    def refresh_session(self, *, refresh_token: str, request_options: typing.Optional[RequestOptions] = None) -> Pass:
        """
        Issues new keys for the session the presented token belongs to. The session itself is not replaced: it lasts from signing in until signing out, and these are only its keys. The token presented here is spent in the act — a second use of the same one means a copy is loose, and then the session ends for everyone holding it, the rightful owner included.

        Parameters
        ----------
        refresh_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Pass
            Fresh pass issued

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.auth.refresh_session(
            refresh_token="refresh_token",
        )
        """
        _response = self._raw_client.refresh_session(refresh_token=refresh_token, request_options=request_options)
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

    async def create_code(
        self, *, email: Email, request_options: typing.Optional[RequestOptions] = None
    ) -> CodeDelivery:
        """
        Sends a one-time code to the given address. The answer is the same whether or not an account already exists behind that address: telling the two apart would turn this into a directory of registered people. The code travels by mail only and is never part of any response.

        Parameters
        ----------
        email : Email

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CodeDelivery
            The code was sent. Nothing here says whether an account exists, and nothing here promises the mail arrived — delivery is the only real test, and its outcome belongs to the mailbox, not to this answer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.auth.create_code(
                email="email",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_code(email=email, request_options=request_options)
        return _response.data

    async def create_session(
        self, *, email: Email, code: Code, request_options: typing.Optional[RequestOptions] = None
    ) -> Pass:
        """
        Exchanges an emailed code for a pass. The account comes into being here if the address had none: signing in and signing up are one act, because separating them would mean saying whether the address is known, and that is what this API refuses to say. The code is checked together with the address it was issued for — six digits are not unique, and alone they identify nobody.

        Parameters
        ----------
        email : Email

        code : Code

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Pass
            Signed in. The answer does not say whether the account was born just now: that is a state, not an event, and it is read from the person, not from this moment.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.auth.create_session(
                email="email",
                code="code",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_session(email=email, code=code, request_options=request_options)
        return _response.data

    async def delete_session(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Ends the session the presented token belongs to, on this device only — the other devices a person is signed in on know nothing of it.
        It takes effect at once, including for the access token just used. That token is not recalled and cannot be: it is believed on its signature alone. But every guarded operation asks after the session behind the token it was shown, and from here on the answer is that there is none. The refresh token goes the same way and for the same reason — it buys keys to a session, and there is no longer a session to buy them for. Neither is crossed out one by one; both die of what they point at.
        Signing out twice answers 401 rather than 204. The second attempt arrives holding a pass that no longer stands, and is turned away before it can be read as a request at all — the same answer every other operation now gives it.

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.auth.delete_session()


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_session(request_options=request_options)
        return _response.data

    async def refresh_session(
        self, *, refresh_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Pass:
        """
        Issues new keys for the session the presented token belongs to. The session itself is not replaced: it lasts from signing in until signing out, and these are only its keys. The token presented here is spent in the act — a second use of the same one means a copy is loose, and then the session ends for everyone holding it, the rightful owner included.

        Parameters
        ----------
        refresh_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Pass
            Fresh pass issued

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.auth.refresh_session(
                refresh_token="refresh_token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.refresh_session(refresh_token=refresh_token, request_options=request_options)
        return _response.data



import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.apple_session_request_user import AppleSessionRequestUser
from ..types.session_token_response import SessionTokenResponse
from .raw_client import AsyncRawSessionsClient, RawSessionsClient


OMIT = typing.cast(typing.Any, ...)


class SessionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSessionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSessionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSessionsClient
        """
        return self._raw_client

    def create_email_sign_in_code(self, *, email: str, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        email : str

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
        client.sessions.create_email_sign_in_code(
            email="email",
        )
        """
        _response = self._raw_client.create_email_sign_in_code(email=email, request_options=request_options)
        return _response.data

    def create_apple_session(
        self,
        *,
        authorization_code: str,
        id_token: str,
        nonce: str,
        user: typing.Optional[AppleSessionRequestUser] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SessionTokenResponse:
        """
        Parameters
        ----------
        authorization_code : str

        id_token : str

        nonce : str

        user : typing.Optional[AppleSessionRequestUser]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SessionTokenResponse
            Zoonk bearer session created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sessions.create_apple_session(
            authorization_code="authorizationCode",
            id_token="idToken",
            nonce="nonce",
        )
        """
        _response = self._raw_client.create_apple_session(
            authorization_code=authorization_code,
            id_token=id_token,
            nonce=nonce,
            user=user,
            request_options=request_options,
        )
        return _response.data

    def delete_current_session(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Deletes the supplied session. Repeating the request after deletion is a 204 no-op.

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
        client.sessions.delete_current_session()
        """
        _response = self._raw_client.delete_current_session(request_options=request_options)
        return _response.data

    def create_email_code_session(
        self, *, code: str, email: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SessionTokenResponse:
        """
        Parameters
        ----------
        code : str

        email : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SessionTokenResponse
            Zoonk bearer session created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sessions.create_email_code_session(
            code="code",
            email="email",
        )
        """
        _response = self._raw_client.create_email_code_session(code=code, email=email, request_options=request_options)
        return _response.data

    def create_google_session(
        self, *, id_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SessionTokenResponse:
        """
        Parameters
        ----------
        id_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SessionTokenResponse
            Zoonk bearer session created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sessions.create_google_session(
            id_token="idToken",
        )
        """
        _response = self._raw_client.create_google_session(id_token=id_token, request_options=request_options)
        return _response.data


class AsyncSessionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSessionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSessionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSessionsClient
        """
        return self._raw_client

    async def create_email_sign_in_code(
        self, *, email: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        email : str

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
            await client.sessions.create_email_sign_in_code(
                email="email",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_email_sign_in_code(email=email, request_options=request_options)
        return _response.data

    async def create_apple_session(
        self,
        *,
        authorization_code: str,
        id_token: str,
        nonce: str,
        user: typing.Optional[AppleSessionRequestUser] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SessionTokenResponse:
        """
        Parameters
        ----------
        authorization_code : str

        id_token : str

        nonce : str

        user : typing.Optional[AppleSessionRequestUser]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SessionTokenResponse
            Zoonk bearer session created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sessions.create_apple_session(
                authorization_code="authorizationCode",
                id_token="idToken",
                nonce="nonce",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_apple_session(
            authorization_code=authorization_code,
            id_token=id_token,
            nonce=nonce,
            user=user,
            request_options=request_options,
        )
        return _response.data

    async def delete_current_session(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Deletes the supplied session. Repeating the request after deletion is a 204 no-op.

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
            await client.sessions.delete_current_session()


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_current_session(request_options=request_options)
        return _response.data

    async def create_email_code_session(
        self, *, code: str, email: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SessionTokenResponse:
        """
        Parameters
        ----------
        code : str

        email : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SessionTokenResponse
            Zoonk bearer session created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sessions.create_email_code_session(
                code="code",
                email="email",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_email_code_session(
            code=code, email=email, request_options=request_options
        )
        return _response.data

    async def create_google_session(
        self, *, id_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SessionTokenResponse:
        """
        Parameters
        ----------
        id_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SessionTokenResponse
            Zoonk bearer session created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sessions.create_google_session(
                id_token="idToken",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_google_session(id_token=id_token, request_options=request_options)
        return _response.data

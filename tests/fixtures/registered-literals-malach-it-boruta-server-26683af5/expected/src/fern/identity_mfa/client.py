

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawIdentityMfaClient, RawIdentityMfaClient


OMIT = typing.cast(typing.Any, ...)


class IdentityMfaClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawIdentityMfaClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawIdentityMfaClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawIdentityMfaClient
        """
        return self._raw_client

    def display_totp_registration(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            HTML page

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.identity_mfa.display_totp_registration()
        """
        _response = self._raw_client.display_totp_registration(request_options=request_options)
        return _response.data

    def register_a_totp_authenticator(
        self, *, totp_code: str, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Parameters
        ----------
        totp_code : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            HTML page

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.identity_mfa.register_a_totp_authenticator(
            totp_code="totp[code]",
        )
        """
        _response = self._raw_client.register_a_totp_authenticator(totp_code=totp_code, request_options=request_options)
        return _response.data

    def display_web_authn_registration(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            HTML page

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.identity_mfa.display_web_authn_registration()
        """
        _response = self._raw_client.display_web_authn_registration(request_options=request_options)
        return _response.data

    def register_a_web_authn_credential(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            HTML page

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.identity_mfa.register_a_web_authn_credential(
            request={"string": {"key": "value"}},
        )
        """
        _response = self._raw_client.register_a_web_authn_credential(request=request, request_options=request_options)
        return _response.data

    def display_totp_authentication(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            HTML page

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.identity_mfa.display_totp_authentication()
        """
        _response = self._raw_client.display_totp_authentication(request_options=request_options)
        return _response.data

    def authenticate_with_totp(
        self, *, totp_code: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        totp_code : str

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
        client.identity_mfa.authenticate_with_totp(
            totp_code="totp[code]",
        )
        """
        _response = self._raw_client.authenticate_with_totp(totp_code=totp_code, request_options=request_options)
        return _response.data

    def display_web_authn_authentication(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            HTML page

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.identity_mfa.display_web_authn_authentication()
        """
        _response = self._raw_client.display_web_authn_authentication(request_options=request_options)
        return _response.data

    def authenticate_with_web_authn(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

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
        client.identity_mfa.authenticate_with_web_authn(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.authenticate_with_web_authn(request=request, request_options=request_options)
        return _response.data


class AsyncIdentityMfaClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawIdentityMfaClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawIdentityMfaClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawIdentityMfaClient
        """
        return self._raw_client

    async def display_totp_registration(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            HTML page

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.identity_mfa.display_totp_registration()


        asyncio.run(main())
        """
        _response = await self._raw_client.display_totp_registration(request_options=request_options)
        return _response.data

    async def register_a_totp_authenticator(
        self, *, totp_code: str, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Parameters
        ----------
        totp_code : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            HTML page

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.identity_mfa.register_a_totp_authenticator(
                totp_code="totp[code]",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.register_a_totp_authenticator(
            totp_code=totp_code, request_options=request_options
        )
        return _response.data

    async def display_web_authn_registration(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            HTML page

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.identity_mfa.display_web_authn_registration()


        asyncio.run(main())
        """
        _response = await self._raw_client.display_web_authn_registration(request_options=request_options)
        return _response.data

    async def register_a_web_authn_credential(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            HTML page

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.identity_mfa.register_a_web_authn_credential(
                request={"string": {"key": "value"}},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.register_a_web_authn_credential(
            request=request, request_options=request_options
        )
        return _response.data

    async def display_totp_authentication(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            HTML page

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.identity_mfa.display_totp_authentication()


        asyncio.run(main())
        """
        _response = await self._raw_client.display_totp_authentication(request_options=request_options)
        return _response.data

    async def authenticate_with_totp(
        self, *, totp_code: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        totp_code : str

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
            await client.identity_mfa.authenticate_with_totp(
                totp_code="totp[code]",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.authenticate_with_totp(totp_code=totp_code, request_options=request_options)
        return _response.data

    async def display_web_authn_authentication(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            HTML page

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.identity_mfa.display_web_authn_authentication()


        asyncio.run(main())
        """
        _response = await self._raw_client.display_web_authn_authentication(request_options=request_options)
        return _response.data

    async def authenticate_with_web_authn(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

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
            await client.identity_mfa.authenticate_with_web_authn(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.authenticate_with_web_authn(request=request, request_options=request_options)
        return _response.data

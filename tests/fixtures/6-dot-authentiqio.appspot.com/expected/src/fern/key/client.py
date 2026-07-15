

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawKeyClient, RawKeyClient
from .types.key_bind_response import KeyBindResponse
from .types.key_register_response import KeyRegisterResponse
from .types.key_retrieve_response import KeyRetrieveResponse
from .types.key_revoke_nosecret_response import KeyRevokeNosecretResponse
from .types.key_revoke_response import KeyRevokeResponse
from .types.key_update_response import KeyUpdateResponse


class KeyClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawKeyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawKeyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawKeyClient
        """
        return self._raw_client

    def register(self, *, request_options: typing.Optional[RequestOptions] = None) -> KeyRegisterResponse:
        """
        Register a new ID `JWT(sub, devtoken)`

        v5: `JWT(sub, pk, devtoken, ...)`

        See: https://github.com/skion/authentiq/wiki/JWT-Examples

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        KeyRegisterResponse
            Successfully registered

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.key.register()
        """
        _response = self._raw_client.register(request_options=request_options)
        return _response.data

    def revoke_nosecret(
        self,
        *,
        email: str,
        phone: str,
        code: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> KeyRevokeNosecretResponse:
        """
        Revoke an Authentiq ID using email & phone.

        If called with `email` and `phone` only, a verification code
        will be sent by email. Do a second call adding `code` to
        complete the revocation.

        Parameters
        ----------
        email : str
            primary email associated to Key (ID)

        phone : str
            primary phone number, international representation

        code : typing.Optional[str]
            verification code sent by email

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        KeyRevokeNosecretResponse
            Successfully deleted

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.key.revoke_nosecret(
            email="email",
            phone="phone",
        )
        """
        _response = self._raw_client.revoke_nosecret(
            email=email, phone=phone, code=code, request_options=request_options
        )
        return _response.data

    def retrieve(self, pk: str, *, request_options: typing.Optional[RequestOptions] = None) -> KeyRetrieveResponse:
        """
        Get public details of an Authentiq ID.

        Parameters
        ----------
        pk : str
            Public Signing Key - Authentiq ID (43 chars)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        KeyRetrieveResponse
            Successfully retrieved

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.key.retrieve(
            pk="PK",
        )
        """
        _response = self._raw_client.retrieve(pk, request_options=request_options)
        return _response.data

    def update(self, pk: str, *, request_options: typing.Optional[RequestOptions] = None) -> KeyUpdateResponse:
        """
        update properties of an Authentiq ID.
        (not operational in v4; use PUT for now)

        v5: POST issuer-signed email & phone scopes in
        a self-signed JWT

        See: https://github.com/skion/authentiq/wiki/JWT-Examples

        Parameters
        ----------
        pk : str
            Public Signing Key - Authentiq ID (43 chars)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        KeyUpdateResponse
            Successfully updated

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.key.update(
            pk="PK",
        )
        """
        _response = self._raw_client.update(pk, request_options=request_options)
        return _response.data

    def bind(self, pk: str, *, request_options: typing.Optional[RequestOptions] = None) -> KeyBindResponse:
        """
        Update Authentiq ID by replacing the object.

        v4: `JWT(sub,email,phone)` to bind email/phone hash;

        v5: POST issuer-signed email & phone scopes
        and PUT to update registration `JWT(sub, pk, devtoken, ...)`

        See: https://github.com/skion/authentiq/wiki/JWT-Examples

        Parameters
        ----------
        pk : str
            Public Signing Key - Authentiq ID (43 chars)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        KeyBindResponse
            Successfully updated

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.key.bind(
            pk="PK",
        )
        """
        _response = self._raw_client.bind(pk, request_options=request_options)
        return _response.data

    def revoke(
        self, pk: str, *, secret: str, request_options: typing.Optional[RequestOptions] = None
    ) -> KeyRevokeResponse:
        """
        Revoke an Identity (Key) with a revocation secret

        Parameters
        ----------
        pk : str
            Public Signing Key - Authentiq ID (43 chars)

        secret : str
            revokation secret

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        KeyRevokeResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.key.revoke(
            pk="PK",
            secret="secret",
        )
        """
        _response = self._raw_client.revoke(pk, secret=secret, request_options=request_options)
        return _response.data

    def head_key_pk(self, pk: str, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Dict[str, str]:
        """
        HEAD info on Authentiq ID

        Parameters
        ----------
        pk : str
            Public Signing Key - Authentiq ID (43 chars)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.key.head_key_pk(
            pk="PK",
        )
        """
        _response = self._raw_client.head_key_pk(pk, request_options=request_options)
        return _response.headers


class AsyncKeyClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawKeyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawKeyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawKeyClient
        """
        return self._raw_client

    async def register(self, *, request_options: typing.Optional[RequestOptions] = None) -> KeyRegisterResponse:
        """
        Register a new ID `JWT(sub, devtoken)`

        v5: `JWT(sub, pk, devtoken, ...)`

        See: https://github.com/skion/authentiq/wiki/JWT-Examples

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        KeyRegisterResponse
            Successfully registered

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.key.register()


        asyncio.run(main())
        """
        _response = await self._raw_client.register(request_options=request_options)
        return _response.data

    async def revoke_nosecret(
        self,
        *,
        email: str,
        phone: str,
        code: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> KeyRevokeNosecretResponse:
        """
        Revoke an Authentiq ID using email & phone.

        If called with `email` and `phone` only, a verification code
        will be sent by email. Do a second call adding `code` to
        complete the revocation.

        Parameters
        ----------
        email : str
            primary email associated to Key (ID)

        phone : str
            primary phone number, international representation

        code : typing.Optional[str]
            verification code sent by email

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        KeyRevokeNosecretResponse
            Successfully deleted

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.key.revoke_nosecret(
                email="email",
                phone="phone",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.revoke_nosecret(
            email=email, phone=phone, code=code, request_options=request_options
        )
        return _response.data

    async def retrieve(
        self, pk: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> KeyRetrieveResponse:
        """
        Get public details of an Authentiq ID.

        Parameters
        ----------
        pk : str
            Public Signing Key - Authentiq ID (43 chars)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        KeyRetrieveResponse
            Successfully retrieved

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.key.retrieve(
                pk="PK",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve(pk, request_options=request_options)
        return _response.data

    async def update(self, pk: str, *, request_options: typing.Optional[RequestOptions] = None) -> KeyUpdateResponse:
        """
        update properties of an Authentiq ID.
        (not operational in v4; use PUT for now)

        v5: POST issuer-signed email & phone scopes in
        a self-signed JWT

        See: https://github.com/skion/authentiq/wiki/JWT-Examples

        Parameters
        ----------
        pk : str
            Public Signing Key - Authentiq ID (43 chars)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        KeyUpdateResponse
            Successfully updated

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.key.update(
                pk="PK",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(pk, request_options=request_options)
        return _response.data

    async def bind(self, pk: str, *, request_options: typing.Optional[RequestOptions] = None) -> KeyBindResponse:
        """
        Update Authentiq ID by replacing the object.

        v4: `JWT(sub,email,phone)` to bind email/phone hash;

        v5: POST issuer-signed email & phone scopes
        and PUT to update registration `JWT(sub, pk, devtoken, ...)`

        See: https://github.com/skion/authentiq/wiki/JWT-Examples

        Parameters
        ----------
        pk : str
            Public Signing Key - Authentiq ID (43 chars)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        KeyBindResponse
            Successfully updated

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.key.bind(
                pk="PK",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.bind(pk, request_options=request_options)
        return _response.data

    async def revoke(
        self, pk: str, *, secret: str, request_options: typing.Optional[RequestOptions] = None
    ) -> KeyRevokeResponse:
        """
        Revoke an Identity (Key) with a revocation secret

        Parameters
        ----------
        pk : str
            Public Signing Key - Authentiq ID (43 chars)

        secret : str
            revokation secret

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        KeyRevokeResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.key.revoke(
                pk="PK",
                secret="secret",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.revoke(pk, secret=secret, request_options=request_options)
        return _response.data

    async def head_key_pk(
        self, pk: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        HEAD info on Authentiq ID

        Parameters
        ----------
        pk : str
            Public Signing Key - Authentiq ID (43 chars)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.key.head_key_pk(
                pk="PK",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.head_key_pk(pk, request_options=request_options)
        return _response.headers

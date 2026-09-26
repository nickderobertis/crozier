

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.shares_create200response import SharesCreate200Response
from ..types.shares_exchange200response import SharesExchange200Response
from ..types.shares_get200response import SharesGet200Response
from ..types.shares_list200response import SharesList200Response
from ..types.shares_update200response import SharesUpdate200Response
from .raw_client import AsyncRawSharesClient, RawSharesClient


OMIT = typing.cast(typing.Any, ...)


class SharesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSharesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSharesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSharesClient
        """
        return self._raw_client

    def exchange(
        self,
        *,
        share_token: str,
        password: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SharesExchange200Response:
        """
        Unauthenticated, but requires a browser Origin header, checked against the grant allowlist. Unknown, revoked, and disabled tokens are indistinguishable (404). Passphrase-protected grants return 422 SharePasswordRequired until `password` is supplied. Mounted only when the deployment can sign (HS256 mode).

        Parameters
        ----------
        share_token : str

        password : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SharesExchange200Response
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.shares.exchange(
            share_token="shareToken",
        )
        """
        _response = self._raw_client.exchange(
            share_token=share_token, password=password, request_options=request_options
        )
        return _response.data

    def list(
        self,
        tenant_id: str,
        *,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        doc_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SharesList200Response:
        """
        Parameters
        ----------
        tenant_id : str

        limit : typing.Optional[int]

        cursor : typing.Optional[str]

        doc_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SharesList200Response
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.shares.list(
            tenant_id="tenantId",
        )
        """
        _response = self._raw_client.list(
            tenant_id, limit=limit, cursor=cursor, doc_id=doc_id, request_options=request_options
        )
        return _response.data

    def create(
        self,
        tenant_id: str,
        *,
        doc_id: str,
        scope: typing.Sequence[str],
        layer_name: typing.Optional[str] = OMIT,
        origins: typing.Optional[typing.Sequence[str]] = OMIT,
        password: typing.Optional[str] = OMIT,
        session_ttl_seconds: typing.Optional[int] = OMIT,
        expires_at: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SharesCreate200Response:
        """
        The returned share id IS the public share token. Mounted only when the deployment can sign (HS256 mode) — exchange mints session JWTs, so grants exist only where minting does.

        Parameters
        ----------
        tenant_id : str

        doc_id : str

        scope : typing.Sequence[str]

        layer_name : typing.Optional[str]

        origins : typing.Optional[typing.Sequence[str]]

        password : typing.Optional[str]

        session_ttl_seconds : typing.Optional[int]

        expires_at : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SharesCreate200Response
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.shares.create(
            tenant_id="tenantId",
            doc_id="docId",
            scope=["scope"],
        )
        """
        _response = self._raw_client.create(
            tenant_id,
            doc_id=doc_id,
            scope=scope,
            layer_name=layer_name,
            origins=origins,
            password=password,
            session_ttl_seconds=session_ttl_seconds,
            expires_at=expires_at,
            request_options=request_options,
        )
        return _response.data

    def get(
        self, tenant_id: str, share_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SharesGet200Response:
        """
        Parameters
        ----------
        tenant_id : str

        share_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SharesGet200Response
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.shares.get(
            tenant_id="tenantId",
            share_id="shareId",
        )
        """
        _response = self._raw_client.get(tenant_id, share_id, request_options=request_options)
        return _response.data

    def delete(self, tenant_id: str, share_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        tenant_id : str

        share_id : str

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
            base_url="https://yourhost.com/path/to/api",
        )
        client.shares.delete(
            tenant_id="tenantId",
            share_id="shareId",
        )
        """
        _response = self._raw_client.delete(tenant_id, share_id, request_options=request_options)
        return _response.data

    def update(
        self,
        tenant_id: str,
        share_id: str,
        *,
        scope: typing.Optional[typing.Sequence[str]] = OMIT,
        origins: typing.Optional[typing.Sequence[str]] = OMIT,
        password: typing.Optional[str] = OMIT,
        session_ttl_seconds: typing.Optional[int] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        expires_at: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SharesUpdate200Response:
        """
        Parameters
        ----------
        tenant_id : str

        share_id : str

        scope : typing.Optional[typing.Sequence[str]]

        origins : typing.Optional[typing.Sequence[str]]

        password : typing.Optional[str]

        session_ttl_seconds : typing.Optional[int]

        disabled : typing.Optional[bool]

        expires_at : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SharesUpdate200Response
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.shares.update(
            tenant_id="tenantId",
            share_id="shareId",
        )
        """
        _response = self._raw_client.update(
            tenant_id,
            share_id,
            scope=scope,
            origins=origins,
            password=password,
            session_ttl_seconds=session_ttl_seconds,
            disabled=disabled,
            expires_at=expires_at,
            request_options=request_options,
        )
        return _response.data


class AsyncSharesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSharesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSharesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSharesClient
        """
        return self._raw_client

    async def exchange(
        self,
        *,
        share_token: str,
        password: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SharesExchange200Response:
        """
        Unauthenticated, but requires a browser Origin header, checked against the grant allowlist. Unknown, revoked, and disabled tokens are indistinguishable (404). Passphrase-protected grants return 422 SharePasswordRequired until `password` is supplied. Mounted only when the deployment can sign (HS256 mode).

        Parameters
        ----------
        share_token : str

        password : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SharesExchange200Response
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.shares.exchange(
                share_token="shareToken",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.exchange(
            share_token=share_token, password=password, request_options=request_options
        )
        return _response.data

    async def list(
        self,
        tenant_id: str,
        *,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        doc_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SharesList200Response:
        """
        Parameters
        ----------
        tenant_id : str

        limit : typing.Optional[int]

        cursor : typing.Optional[str]

        doc_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SharesList200Response
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.shares.list(
                tenant_id="tenantId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list(
            tenant_id, limit=limit, cursor=cursor, doc_id=doc_id, request_options=request_options
        )
        return _response.data

    async def create(
        self,
        tenant_id: str,
        *,
        doc_id: str,
        scope: typing.Sequence[str],
        layer_name: typing.Optional[str] = OMIT,
        origins: typing.Optional[typing.Sequence[str]] = OMIT,
        password: typing.Optional[str] = OMIT,
        session_ttl_seconds: typing.Optional[int] = OMIT,
        expires_at: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SharesCreate200Response:
        """
        The returned share id IS the public share token. Mounted only when the deployment can sign (HS256 mode) — exchange mints session JWTs, so grants exist only where minting does.

        Parameters
        ----------
        tenant_id : str

        doc_id : str

        scope : typing.Sequence[str]

        layer_name : typing.Optional[str]

        origins : typing.Optional[typing.Sequence[str]]

        password : typing.Optional[str]

        session_ttl_seconds : typing.Optional[int]

        expires_at : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SharesCreate200Response
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.shares.create(
                tenant_id="tenantId",
                doc_id="docId",
                scope=["scope"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(
            tenant_id,
            doc_id=doc_id,
            scope=scope,
            layer_name=layer_name,
            origins=origins,
            password=password,
            session_ttl_seconds=session_ttl_seconds,
            expires_at=expires_at,
            request_options=request_options,
        )
        return _response.data

    async def get(
        self, tenant_id: str, share_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SharesGet200Response:
        """
        Parameters
        ----------
        tenant_id : str

        share_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SharesGet200Response
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.shares.get(
                tenant_id="tenantId",
                share_id="shareId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(tenant_id, share_id, request_options=request_options)
        return _response.data

    async def delete(
        self, tenant_id: str, share_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        tenant_id : str

        share_id : str

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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.shares.delete(
                tenant_id="tenantId",
                share_id="shareId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(tenant_id, share_id, request_options=request_options)
        return _response.data

    async def update(
        self,
        tenant_id: str,
        share_id: str,
        *,
        scope: typing.Optional[typing.Sequence[str]] = OMIT,
        origins: typing.Optional[typing.Sequence[str]] = OMIT,
        password: typing.Optional[str] = OMIT,
        session_ttl_seconds: typing.Optional[int] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        expires_at: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SharesUpdate200Response:
        """
        Parameters
        ----------
        tenant_id : str

        share_id : str

        scope : typing.Optional[typing.Sequence[str]]

        origins : typing.Optional[typing.Sequence[str]]

        password : typing.Optional[str]

        session_ttl_seconds : typing.Optional[int]

        disabled : typing.Optional[bool]

        expires_at : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SharesUpdate200Response
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.shares.update(
                tenant_id="tenantId",
                share_id="shareId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(
            tenant_id,
            share_id,
            scope=scope,
            origins=origins,
            password=password,
            session_ttl_seconds=session_ttl_seconds,
            disabled=disabled,
            expires_at=expires_at,
            request_options=request_options,
        )
        return _response.data

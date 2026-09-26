

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.tenants_create200response import TenantsCreate200Response
from ..types.tenants_get200response import TenantsGet200Response
from ..types.tenants_list200response import TenantsList200Response
from ..types.tenants_usage200response import TenantsUsage200Response
from .raw_client import AsyncRawTenantsClient, RawTenantsClient


OMIT = typing.cast(typing.Any, ...)


class TenantsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTenantsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTenantsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTenantsClient
        """
        return self._raw_client

    def list(
        self,
        *,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TenantsList200Response:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TenantsList200Response
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.tenants.list()
        """
        _response = self._raw_client.list(limit=limit, cursor=cursor, request_options=request_options)
        return _response.data

    def create(
        self, *, id: str, name: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> TenantsCreate200Response:
        """
        Parameters
        ----------
        id : str

        name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TenantsCreate200Response
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.tenants.create(
            id="id",
        )
        """
        _response = self._raw_client.create(id=id, name=name, request_options=request_options)
        return _response.data

    def get(self, tenant_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> TenantsGet200Response:
        """
        Parameters
        ----------
        tenant_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TenantsGet200Response
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.tenants.get(
            tenant_id="tenantId",
        )
        """
        _response = self._raw_client.get(tenant_id, request_options=request_options)
        return _response.data

    def delete(self, tenant_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Destroys the tenant and everything in its namespace — documents, layers, stored bytes, audit history. Irreversible.

        Parameters
        ----------
        tenant_id : str

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
        client.tenants.delete(
            tenant_id="tenantId",
        )
        """
        _response = self._raw_client.delete(tenant_id, request_options=request_options)
        return _response.data

    def resume(self, tenant_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        tenant_id : str

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
        client.tenants.resume(
            tenant_id="tenantId",
        )
        """
        _response = self._raw_client.resume(tenant_id, request_options=request_options)
        return _response.data

    def suspend(
        self,
        tenant_id: str,
        *,
        reason: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Instantly reversible with resume. The API token is exempt, so a suspended tenant can still be inspected, exported, resumed, or deleted.

        Parameters
        ----------
        tenant_id : str

        reason : typing.Optional[str]

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
        client.tenants.suspend(
            tenant_id="tenantId",
        )
        """
        _response = self._raw_client.suspend(tenant_id, reason=reason, request_options=request_options)
        return _response.data

    def usage(
        self,
        tenant_id: str,
        *,
        period: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TenantsUsage200Response:
        """
        Facts only — no limits or billing state. Views count share exchanges plus authorized /v1/access grants, deduplicated across the two.

        Parameters
        ----------
        tenant_id : str

        period : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TenantsUsage200Response
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.tenants.usage(
            tenant_id="tenantId",
        )
        """
        _response = self._raw_client.usage(tenant_id, period=period, request_options=request_options)
        return _response.data


class AsyncTenantsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTenantsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTenantsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTenantsClient
        """
        return self._raw_client

    async def list(
        self,
        *,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TenantsList200Response:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TenantsList200Response
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
            await client.tenants.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(limit=limit, cursor=cursor, request_options=request_options)
        return _response.data

    async def create(
        self, *, id: str, name: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> TenantsCreate200Response:
        """
        Parameters
        ----------
        id : str

        name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TenantsCreate200Response
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
            await client.tenants.create(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(id=id, name=name, request_options=request_options)
        return _response.data

    async def get(
        self, tenant_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TenantsGet200Response:
        """
        Parameters
        ----------
        tenant_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TenantsGet200Response
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
            await client.tenants.get(
                tenant_id="tenantId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(tenant_id, request_options=request_options)
        return _response.data

    async def delete(self, tenant_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Destroys the tenant and everything in its namespace — documents, layers, stored bytes, audit history. Irreversible.

        Parameters
        ----------
        tenant_id : str

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
            await client.tenants.delete(
                tenant_id="tenantId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(tenant_id, request_options=request_options)
        return _response.data

    async def resume(self, tenant_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        tenant_id : str

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
            await client.tenants.resume(
                tenant_id="tenantId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.resume(tenant_id, request_options=request_options)
        return _response.data

    async def suspend(
        self,
        tenant_id: str,
        *,
        reason: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Instantly reversible with resume. The API token is exempt, so a suspended tenant can still be inspected, exported, resumed, or deleted.

        Parameters
        ----------
        tenant_id : str

        reason : typing.Optional[str]

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
            await client.tenants.suspend(
                tenant_id="tenantId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.suspend(tenant_id, reason=reason, request_options=request_options)
        return _response.data

    async def usage(
        self,
        tenant_id: str,
        *,
        period: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TenantsUsage200Response:
        """
        Facts only — no limits or billing state. Views count share exchanges plus authorized /v1/access grants, deduplicated across the two.

        Parameters
        ----------
        tenant_id : str

        period : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TenantsUsage200Response
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
            await client.tenants.usage(
                tenant_id="tenantId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.usage(tenant_id, period=period, request_options=request_options)
        return _response.data

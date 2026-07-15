

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.pool import Pool
from ..types.pool_collection import PoolCollection
from .raw_client import AsyncRawPoolClient, RawPoolClient


OMIT = typing.cast(typing.Any, ...)


class PoolClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPoolClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPoolClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPoolClient
        """
        return self._raw_client

    def get_pools(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order_by: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PoolCollection:
        """
        Parameters
        ----------
        limit : typing.Optional[int]
            The numbers of items to return.

        offset : typing.Optional[int]
            The number of items to skip before starting to collect the result set.

        order_by : typing.Optional[str]
            The name of the field to order the results by.
            Prefix a field name with `-` to reverse the sort order.

            *New in version 2.1.0*

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PoolCollection
            List of pools.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.pool.get_pools()
        """
        _response = self._raw_client.get_pools(
            limit=limit, offset=offset, order_by=order_by, request_options=request_options
        )
        return _response.data

    def post_pool(
        self,
        *,
        description: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        occupied_slots: typing.Optional[int] = OMIT,
        open_slots: typing.Optional[int] = OMIT,
        queued_slots: typing.Optional[int] = OMIT,
        slots: typing.Optional[int] = OMIT,
        used_slots: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Pool:
        """
        Parameters
        ----------
        description : typing.Optional[str]
            The description of the pool.

            *New in version 2.3.0*

        name : typing.Optional[str]
            The name of pool.

        occupied_slots : typing.Optional[int]
            The number of slots used by running/queued tasks at the moment.

        open_slots : typing.Optional[int]
            The number of free slots at the moment.

        queued_slots : typing.Optional[int]
            The number of slots used by queued tasks at the moment.

        slots : typing.Optional[int]
            The maximum number of slots that can be assigned to tasks. One job may occupy one or more slots.

        used_slots : typing.Optional[int]
            The number of slots used by running tasks at the moment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Pool
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.pool.post_pool()
        """
        _response = self._raw_client.post_pool(
            description=description,
            name=name,
            occupied_slots=occupied_slots,
            open_slots=open_slots,
            queued_slots=queued_slots,
            slots=slots,
            used_slots=used_slots,
            request_options=request_options,
        )
        return _response.data

    def get_pool(self, pool_name: str, *, request_options: typing.Optional[RequestOptions] = None) -> Pool:
        """
        Parameters
        ----------
        pool_name : str
            The pool name.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Pool
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.pool.get_pool(
            pool_name="pool_name",
        )
        """
        _response = self._raw_client.get_pool(pool_name, request_options=request_options)
        return _response.data

    def delete_pool(self, pool_name: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        pool_name : str
            The pool name.

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
        client.pool.delete_pool(
            pool_name="pool_name",
        )
        """
        _response = self._raw_client.delete_pool(pool_name, request_options=request_options)
        return _response.data

    def patch_pool(
        self,
        pool_name: str,
        *,
        update_mask: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        description: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        occupied_slots: typing.Optional[int] = OMIT,
        open_slots: typing.Optional[int] = OMIT,
        queued_slots: typing.Optional[int] = OMIT,
        slots: typing.Optional[int] = OMIT,
        used_slots: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Pool:
        """
        Parameters
        ----------
        pool_name : str
            The pool name.

        update_mask : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The fields to update on the resource. If absent or empty, all modifiable fields are updated.
            A comma-separated list of fully qualified names of fields.

        description : typing.Optional[str]
            The description of the pool.

            *New in version 2.3.0*

        name : typing.Optional[str]
            The name of pool.

        occupied_slots : typing.Optional[int]
            The number of slots used by running/queued tasks at the moment.

        open_slots : typing.Optional[int]
            The number of free slots at the moment.

        queued_slots : typing.Optional[int]
            The number of slots used by queued tasks at the moment.

        slots : typing.Optional[int]
            The maximum number of slots that can be assigned to tasks. One job may occupy one or more slots.

        used_slots : typing.Optional[int]
            The number of slots used by running tasks at the moment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Pool
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.pool.patch_pool(
            pool_name="pool_name",
        )
        """
        _response = self._raw_client.patch_pool(
            pool_name,
            update_mask=update_mask,
            description=description,
            name=name,
            occupied_slots=occupied_slots,
            open_slots=open_slots,
            queued_slots=queued_slots,
            slots=slots,
            used_slots=used_slots,
            request_options=request_options,
        )
        return _response.data


class AsyncPoolClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPoolClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPoolClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPoolClient
        """
        return self._raw_client

    async def get_pools(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order_by: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PoolCollection:
        """
        Parameters
        ----------
        limit : typing.Optional[int]
            The numbers of items to return.

        offset : typing.Optional[int]
            The number of items to skip before starting to collect the result set.

        order_by : typing.Optional[str]
            The name of the field to order the results by.
            Prefix a field name with `-` to reverse the sort order.

            *New in version 2.1.0*

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PoolCollection
            List of pools.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.pool.get_pools()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_pools(
            limit=limit, offset=offset, order_by=order_by, request_options=request_options
        )
        return _response.data

    async def post_pool(
        self,
        *,
        description: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        occupied_slots: typing.Optional[int] = OMIT,
        open_slots: typing.Optional[int] = OMIT,
        queued_slots: typing.Optional[int] = OMIT,
        slots: typing.Optional[int] = OMIT,
        used_slots: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Pool:
        """
        Parameters
        ----------
        description : typing.Optional[str]
            The description of the pool.

            *New in version 2.3.0*

        name : typing.Optional[str]
            The name of pool.

        occupied_slots : typing.Optional[int]
            The number of slots used by running/queued tasks at the moment.

        open_slots : typing.Optional[int]
            The number of free slots at the moment.

        queued_slots : typing.Optional[int]
            The number of slots used by queued tasks at the moment.

        slots : typing.Optional[int]
            The maximum number of slots that can be assigned to tasks. One job may occupy one or more slots.

        used_slots : typing.Optional[int]
            The number of slots used by running tasks at the moment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Pool
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.pool.post_pool()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_pool(
            description=description,
            name=name,
            occupied_slots=occupied_slots,
            open_slots=open_slots,
            queued_slots=queued_slots,
            slots=slots,
            used_slots=used_slots,
            request_options=request_options,
        )
        return _response.data

    async def get_pool(self, pool_name: str, *, request_options: typing.Optional[RequestOptions] = None) -> Pool:
        """
        Parameters
        ----------
        pool_name : str
            The pool name.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Pool
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.pool.get_pool(
                pool_name="pool_name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_pool(pool_name, request_options=request_options)
        return _response.data

    async def delete_pool(self, pool_name: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        pool_name : str
            The pool name.

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
            await client.pool.delete_pool(
                pool_name="pool_name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_pool(pool_name, request_options=request_options)
        return _response.data

    async def patch_pool(
        self,
        pool_name: str,
        *,
        update_mask: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        description: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        occupied_slots: typing.Optional[int] = OMIT,
        open_slots: typing.Optional[int] = OMIT,
        queued_slots: typing.Optional[int] = OMIT,
        slots: typing.Optional[int] = OMIT,
        used_slots: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Pool:
        """
        Parameters
        ----------
        pool_name : str
            The pool name.

        update_mask : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The fields to update on the resource. If absent or empty, all modifiable fields are updated.
            A comma-separated list of fully qualified names of fields.

        description : typing.Optional[str]
            The description of the pool.

            *New in version 2.3.0*

        name : typing.Optional[str]
            The name of pool.

        occupied_slots : typing.Optional[int]
            The number of slots used by running/queued tasks at the moment.

        open_slots : typing.Optional[int]
            The number of free slots at the moment.

        queued_slots : typing.Optional[int]
            The number of slots used by queued tasks at the moment.

        slots : typing.Optional[int]
            The maximum number of slots that can be assigned to tasks. One job may occupy one or more slots.

        used_slots : typing.Optional[int]
            The number of slots used by running tasks at the moment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Pool
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.pool.patch_pool(
                pool_name="pool_name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_pool(
            pool_name,
            update_mask=update_mask,
            description=description,
            name=name,
            occupied_slots=occupied_slots,
            open_slots=open_slots,
            queued_slots=queued_slots,
            slots=slots,
            used_slots=used_slots,
            request_options=request_options,
        )
        return _response.data

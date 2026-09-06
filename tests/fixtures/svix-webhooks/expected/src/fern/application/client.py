

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.application_out import ApplicationOut
from ..types.list_response_application_out import ListResponseApplicationOut
from ..types.ordering import Ordering
from .raw_client import AsyncRawApplicationClient, RawApplicationClient


OMIT = typing.cast(typing.Any, ...)


class ApplicationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawApplicationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawApplicationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawApplicationClient
        """
        return self._raw_client

    def v1application_list(
        self,
        *,
        limit: typing.Optional[int] = None,
        iterator: typing.Optional[str] = None,
        order: typing.Optional[Ordering] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListResponseApplicationOut:
        """
        List of all the organization's applications.

        Parameters
        ----------
        limit : typing.Optional[int]
            Limit the number of returned items

        iterator : typing.Optional[str]
            The iterator returned from a prior invocation

        order : typing.Optional[Ordering]
            The sorting order of the returned items

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListResponseApplicationOut


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.application.v1application_list(
            iterator="app_1srOrx2ZWZBpBUvZwXKQmoEYga2",
        )
        """
        _response = self._raw_client.v1application_list(
            limit=limit, iterator=iterator, order=order, request_options=request_options
        )
        return _response.data

    def v1application_create(
        self,
        *,
        name: str,
        get_if_exists: typing.Optional[bool] = None,
        idempotency_key: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        throttle_rate: typing.Optional[int] = OMIT,
        uid: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApplicationOut:
        """
        Create a new application.

        Parameters
        ----------
        name : str

        get_if_exists : typing.Optional[bool]
            Get an existing application, or create a new one if doesn't exist. It's two separate functions in the libs.

        idempotency_key : typing.Optional[str]
            The request's idempotency key

        metadata : typing.Optional[typing.Dict[str, str]]

        throttle_rate : typing.Optional[int]
            Maximum messages per second to send to this application's endpoints.

            Outgoing messages will be throttled to this rate.

        uid : typing.Optional[str]
            Optional unique identifier for the application

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplicationOut


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.application.v1application_create(
            name="My first application",
        )
        """
        _response = self._raw_client.v1application_create(
            name=name,
            get_if_exists=get_if_exists,
            idempotency_key=idempotency_key,
            metadata=metadata,
            throttle_rate=throttle_rate,
            uid=uid,
            request_options=request_options,
        )
        return _response.data

    def v1application_get(
        self, app_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApplicationOut:
        """
        Get an application.

        Parameters
        ----------
        app_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplicationOut


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.application.v1application_get(
            app_id="app_id",
        )
        """
        _response = self._raw_client.v1application_get(app_id, request_options=request_options)
        return _response.data

    def v1application_update(
        self,
        app_id: str,
        *,
        name: str,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        throttle_rate: typing.Optional[int] = OMIT,
        uid: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApplicationOut:
        """
        Update an application.

        Parameters
        ----------
        app_id : str

        name : str

        metadata : typing.Optional[typing.Dict[str, str]]

        throttle_rate : typing.Optional[int]
            Maximum messages per second to send to this application's endpoints.

            Outgoing messages will be throttled to this rate.

        uid : typing.Optional[str]
            Optional unique identifier for the application

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplicationOut


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.application.v1application_update(
            app_id="unique-app-identifier",
            name="My first application",
        )
        """
        _response = self._raw_client.v1application_update(
            app_id, name=name, metadata=metadata, throttle_rate=throttle_rate, uid=uid, request_options=request_options
        )
        return _response.data

    def v1application_delete(self, app_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete an application.

        Parameters
        ----------
        app_id : str

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
        client.application.v1application_delete(
            app_id="app_id",
        )
        """
        _response = self._raw_client.v1application_delete(app_id, request_options=request_options)
        return _response.data

    def patch_application(
        self,
        app_id: str,
        *,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        throttle_rate: typing.Optional[int] = OMIT,
        uid: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApplicationOut:
        """
        Partially update an application.

        Parameters
        ----------
        app_id : str

        metadata : typing.Optional[typing.Dict[str, str]]

        name : typing.Optional[str]

        throttle_rate : typing.Optional[int]
            Maximum messages per second to send to this application's endpoints.

            Outgoing messages will be throttled to this rate.

        uid : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplicationOut


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.application.patch_application(
            app_id="app_id",
        )
        """
        _response = self._raw_client.patch_application(
            app_id, metadata=metadata, name=name, throttle_rate=throttle_rate, uid=uid, request_options=request_options
        )
        return _response.data


class AsyncApplicationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawApplicationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawApplicationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawApplicationClient
        """
        return self._raw_client

    async def v1application_list(
        self,
        *,
        limit: typing.Optional[int] = None,
        iterator: typing.Optional[str] = None,
        order: typing.Optional[Ordering] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListResponseApplicationOut:
        """
        List of all the organization's applications.

        Parameters
        ----------
        limit : typing.Optional[int]
            Limit the number of returned items

        iterator : typing.Optional[str]
            The iterator returned from a prior invocation

        order : typing.Optional[Ordering]
            The sorting order of the returned items

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListResponseApplicationOut


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.application.v1application_list(
                iterator="app_1srOrx2ZWZBpBUvZwXKQmoEYga2",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1application_list(
            limit=limit, iterator=iterator, order=order, request_options=request_options
        )
        return _response.data

    async def v1application_create(
        self,
        *,
        name: str,
        get_if_exists: typing.Optional[bool] = None,
        idempotency_key: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        throttle_rate: typing.Optional[int] = OMIT,
        uid: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApplicationOut:
        """
        Create a new application.

        Parameters
        ----------
        name : str

        get_if_exists : typing.Optional[bool]
            Get an existing application, or create a new one if doesn't exist. It's two separate functions in the libs.

        idempotency_key : typing.Optional[str]
            The request's idempotency key

        metadata : typing.Optional[typing.Dict[str, str]]

        throttle_rate : typing.Optional[int]
            Maximum messages per second to send to this application's endpoints.

            Outgoing messages will be throttled to this rate.

        uid : typing.Optional[str]
            Optional unique identifier for the application

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplicationOut


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.application.v1application_create(
                name="My first application",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1application_create(
            name=name,
            get_if_exists=get_if_exists,
            idempotency_key=idempotency_key,
            metadata=metadata,
            throttle_rate=throttle_rate,
            uid=uid,
            request_options=request_options,
        )
        return _response.data

    async def v1application_get(
        self, app_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApplicationOut:
        """
        Get an application.

        Parameters
        ----------
        app_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplicationOut


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.application.v1application_get(
                app_id="app_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1application_get(app_id, request_options=request_options)
        return _response.data

    async def v1application_update(
        self,
        app_id: str,
        *,
        name: str,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        throttle_rate: typing.Optional[int] = OMIT,
        uid: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApplicationOut:
        """
        Update an application.

        Parameters
        ----------
        app_id : str

        name : str

        metadata : typing.Optional[typing.Dict[str, str]]

        throttle_rate : typing.Optional[int]
            Maximum messages per second to send to this application's endpoints.

            Outgoing messages will be throttled to this rate.

        uid : typing.Optional[str]
            Optional unique identifier for the application

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplicationOut


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.application.v1application_update(
                app_id="unique-app-identifier",
                name="My first application",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1application_update(
            app_id, name=name, metadata=metadata, throttle_rate=throttle_rate, uid=uid, request_options=request_options
        )
        return _response.data

    async def v1application_delete(
        self, app_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete an application.

        Parameters
        ----------
        app_id : str

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
            await client.application.v1application_delete(
                app_id="app_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1application_delete(app_id, request_options=request_options)
        return _response.data

    async def patch_application(
        self,
        app_id: str,
        *,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        throttle_rate: typing.Optional[int] = OMIT,
        uid: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApplicationOut:
        """
        Partially update an application.

        Parameters
        ----------
        app_id : str

        metadata : typing.Optional[typing.Dict[str, str]]

        name : typing.Optional[str]

        throttle_rate : typing.Optional[int]
            Maximum messages per second to send to this application's endpoints.

            Outgoing messages will be throttled to this rate.

        uid : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplicationOut


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.application.patch_application(
                app_id="app_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_application(
            app_id, metadata=metadata, name=name, throttle_rate=throttle_rate, uid=uid, request_options=request_options
        )
        return _response.data

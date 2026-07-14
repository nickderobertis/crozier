

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawHealthClient, RawHealthClient


class HealthClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawHealthClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawHealthClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawHealthClient
        """
        return self._raw_client

    def get(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Check the Appwrite HTTP server is up and responsive.

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
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.health.get()
        """
        _response = self._raw_client.get(request_options=request_options)
        return _response.data

    def get_anti_virus(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Check the Appwrite Anti Virus server is up and connection is successful.

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
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.health.get_anti_virus()
        """
        _response = self._raw_client.get_anti_virus(request_options=request_options)
        return _response.data

    def get_cache(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Check the Appwrite in-memory cache server is up and connection is successful.

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
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.health.get_cache()
        """
        _response = self._raw_client.get_cache(request_options=request_options)
        return _response.data

    def health_get_db(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Check the Appwrite database server is up and connection is successful.

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
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.health.health_get_db()
        """
        _response = self._raw_client.health_get_db(request_options=request_options)
        return _response.data

    def get_queue_certificates(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get the number of certificates that are waiting to be issued against [Letsencrypt](https://letsencrypt.org/) in the Appwrite internal queue server.

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
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.health.get_queue_certificates()
        """
        _response = self._raw_client.get_queue_certificates(request_options=request_options)
        return _response.data

    def get_queue_functions(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


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
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.health.get_queue_functions()
        """
        _response = self._raw_client.get_queue_functions(request_options=request_options)
        return _response.data

    def get_queue_logs(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get the number of logs that are waiting to be processed in the Appwrite internal queue server.

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
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.health.get_queue_logs()
        """
        _response = self._raw_client.get_queue_logs(request_options=request_options)
        return _response.data

    def get_queue_tasks(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get the number of tasks that are waiting to be processed in the Appwrite internal queue server.

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
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.health.get_queue_tasks()
        """
        _response = self._raw_client.get_queue_tasks(request_options=request_options)
        return _response.data

    def get_queue_usage(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get the number of usage stats that are waiting to be processed in the Appwrite internal queue server.

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
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.health.get_queue_usage()
        """
        _response = self._raw_client.get_queue_usage(request_options=request_options)
        return _response.data

    def get_queue_webhooks(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get the number of webhooks that are waiting to be processed in the Appwrite internal queue server.

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
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.health.get_queue_webhooks()
        """
        _response = self._raw_client.get_queue_webhooks(request_options=request_options)
        return _response.data

    def get_storage_local(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Check the Appwrite local storage device is up and connection is successful.

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
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.health.get_storage_local()
        """
        _response = self._raw_client.get_storage_local(request_options=request_options)
        return _response.data

    def get_time(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Check the Appwrite server time is synced with Google remote NTP server. We use this technology to smoothly handle leap seconds with no disruptive events. The [Network Time Protocol](https://en.wikipedia.org/wiki/Network_Time_Protocol) (NTP) is used by hundreds of millions of computers and devices to synchronize their clocks over the Internet. If your computer sets its own clock, it likely uses NTP.

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
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.health.get_time()
        """
        _response = self._raw_client.get_time(request_options=request_options)
        return _response.data


class AsyncHealthClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawHealthClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawHealthClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawHealthClient
        """
        return self._raw_client

    async def get(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Check the Appwrite HTTP server is up and responsive.

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
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.health.get()


        asyncio.run(main())
        """
        _response = await self._raw_client.get(request_options=request_options)
        return _response.data

    async def get_anti_virus(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Check the Appwrite Anti Virus server is up and connection is successful.

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
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.health.get_anti_virus()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_anti_virus(request_options=request_options)
        return _response.data

    async def get_cache(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Check the Appwrite in-memory cache server is up and connection is successful.

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
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.health.get_cache()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_cache(request_options=request_options)
        return _response.data

    async def health_get_db(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Check the Appwrite database server is up and connection is successful.

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
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.health.health_get_db()


        asyncio.run(main())
        """
        _response = await self._raw_client.health_get_db(request_options=request_options)
        return _response.data

    async def get_queue_certificates(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get the number of certificates that are waiting to be issued against [Letsencrypt](https://letsencrypt.org/) in the Appwrite internal queue server.

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
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.health.get_queue_certificates()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_queue_certificates(request_options=request_options)
        return _response.data

    async def get_queue_functions(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


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
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.health.get_queue_functions()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_queue_functions(request_options=request_options)
        return _response.data

    async def get_queue_logs(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get the number of logs that are waiting to be processed in the Appwrite internal queue server.

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
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.health.get_queue_logs()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_queue_logs(request_options=request_options)
        return _response.data

    async def get_queue_tasks(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get the number of tasks that are waiting to be processed in the Appwrite internal queue server.

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
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.health.get_queue_tasks()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_queue_tasks(request_options=request_options)
        return _response.data

    async def get_queue_usage(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get the number of usage stats that are waiting to be processed in the Appwrite internal queue server.

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
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.health.get_queue_usage()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_queue_usage(request_options=request_options)
        return _response.data

    async def get_queue_webhooks(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get the number of webhooks that are waiting to be processed in the Appwrite internal queue server.

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
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.health.get_queue_webhooks()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_queue_webhooks(request_options=request_options)
        return _response.data

    async def get_storage_local(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Check the Appwrite local storage device is up and connection is successful.

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
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.health.get_storage_local()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_storage_local(request_options=request_options)
        return _response.data

    async def get_time(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Check the Appwrite server time is synced with Google remote NTP server. We use this technology to smoothly handle leap seconds with no disruptive events. The [Network Time Protocol](https://en.wikipedia.org/wiki/Network_Time_Protocol) (NTP) is used by hundreds of millions of computers and devices to synchronize their clocks over the Internet. If your computer sets its own clock, it likely uses NTP.

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
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.health.get_time()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_time(request_options=request_options)
        return _response.data

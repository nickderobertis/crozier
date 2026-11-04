

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAssetsClient, RawAssetsClient


class AssetsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAssetsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAssetsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAssetsClient
        """
        return self._raw_client

    def serve_the_boruta_favicon(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Icon asset

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.assets.serve_the_boruta_favicon()
        """
        with self._raw_client.serve_the_boruta_favicon(request_options=request_options) as r:
            yield from r.data

    def serve_robots_txt(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Text asset

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.assets.serve_robots_txt()
        """
        _response = self._raw_client.serve_robots_txt(request_options=request_options)
        return _response.data

    def serve_an_authorization_server_stylesheet(
        self, filename: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Parameters
        ----------
        filename : str
            Static asset filename, optionally including a Phoenix digest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            CSS stylesheet

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.assets.serve_an_authorization_server_stylesheet(
            filename="filename",
        )
        """
        _response = self._raw_client.serve_an_authorization_server_stylesheet(filename, request_options=request_options)
        return _response.data

    def serve_an_authorization_server_font(
        self, filename: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        filename : str
            Static asset filename, optionally including a Phoenix digest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Font asset

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.assets.serve_an_authorization_server_font(
            filename="filename",
        )
        """
        with self._raw_client.serve_an_authorization_server_font(filename, request_options=request_options) as r:
            yield from r.data

    def serve_an_authorization_server_image(
        self, filename: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        filename : str
            Static asset filename, optionally including a Phoenix digest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Image asset

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.assets.serve_an_authorization_server_image(
            filename="filename",
        )
        """
        with self._raw_client.serve_an_authorization_server_image(filename, request_options=request_options) as r:
            yield from r.data

    def serve_an_authorization_server_java_script_asset(
        self, filename: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        filename : str
            Static asset filename, optionally including a Phoenix digest

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
        client.assets.serve_an_authorization_server_java_script_asset(
            filename="filename",
        )
        """
        _response = self._raw_client.serve_an_authorization_server_java_script_asset(
            filename, request_options=request_options
        )
        return _response.data

    def serve_an_authorization_server_admin_asset(
        self, filename: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        filename : str
            Static asset filename, optionally including a Phoenix digest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Static asset

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.assets.serve_an_authorization_server_admin_asset(
            filename="filename",
        )
        """
        with self._raw_client.serve_an_authorization_server_admin_asset(filename, request_options=request_options) as r:
            yield from r.data

    def serve_a_top_level_identity_asset(
        self, filename: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        filename : str
            Static asset filename, optionally including a Phoenix digest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Static asset

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.assets.serve_a_top_level_identity_asset(
            filename="filename",
        )
        """
        with self._raw_client.serve_a_top_level_identity_asset(filename, request_options=request_options) as r:
            yield from r.data

    def serve_an_identity_stylesheet(
        self, filename: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Parameters
        ----------
        filename : str
            Static asset filename, optionally including a Phoenix digest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            CSS stylesheet

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.assets.serve_an_identity_stylesheet(
            filename="filename",
        )
        """
        _response = self._raw_client.serve_an_identity_stylesheet(filename, request_options=request_options)
        return _response.data

    def serve_an_identity_java_script_asset(
        self, filename: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        filename : str
            Static asset filename, optionally including a Phoenix digest

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
        client.assets.serve_an_identity_java_script_asset(
            filename="filename",
        )
        """
        _response = self._raw_client.serve_an_identity_java_script_asset(filename, request_options=request_options)
        return _response.data

    def serve_an_identity_image(
        self, filename: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        filename : str
            Static asset filename, optionally including a Phoenix digest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Image asset

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.assets.serve_an_identity_image(
            filename="filename",
        )
        """
        with self._raw_client.serve_an_identity_image(filename, request_options=request_options) as r:
            yield from r.data

    def serve_the_identity_web_app_manifest(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Web app manifest

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.assets.serve_the_identity_web_app_manifest()
        """
        _response = self._raw_client.serve_the_identity_web_app_manifest(request_options=request_options)
        return _response.data

    def serve_the_identity_favicon(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Icon asset

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.assets.serve_the_identity_favicon()
        """
        with self._raw_client.serve_the_identity_favicon(request_options=request_options) as r:
            yield from r.data

    def serve_the_identity_robots_txt(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Text asset

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.assets.serve_the_identity_robots_txt()
        """
        _response = self._raw_client.serve_the_identity_robots_txt(request_options=request_options)
        return _response.data

    def serve_the_identity_semantic_ui_stylesheet(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            CSS stylesheet

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.assets.serve_the_identity_semantic_ui_stylesheet()
        """
        _response = self._raw_client.serve_the_identity_semantic_ui_stylesheet(request_options=request_options)
        return _response.data


class AsyncAssetsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAssetsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAssetsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAssetsClient
        """
        return self._raw_client

    async def serve_the_boruta_favicon(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Icon asset

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.assets.serve_the_boruta_favicon()


        asyncio.run(main())
        """
        async with self._raw_client.serve_the_boruta_favicon(request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def serve_robots_txt(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Text asset

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.assets.serve_robots_txt()


        asyncio.run(main())
        """
        _response = await self._raw_client.serve_robots_txt(request_options=request_options)
        return _response.data

    async def serve_an_authorization_server_stylesheet(
        self, filename: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Parameters
        ----------
        filename : str
            Static asset filename, optionally including a Phoenix digest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            CSS stylesheet

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.assets.serve_an_authorization_server_stylesheet(
                filename="filename",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.serve_an_authorization_server_stylesheet(
            filename, request_options=request_options
        )
        return _response.data

    async def serve_an_authorization_server_font(
        self, filename: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        filename : str
            Static asset filename, optionally including a Phoenix digest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Font asset

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.assets.serve_an_authorization_server_font(
                filename="filename",
            )


        asyncio.run(main())
        """
        async with self._raw_client.serve_an_authorization_server_font(filename, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def serve_an_authorization_server_image(
        self, filename: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        filename : str
            Static asset filename, optionally including a Phoenix digest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Image asset

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.assets.serve_an_authorization_server_image(
                filename="filename",
            )


        asyncio.run(main())
        """
        async with self._raw_client.serve_an_authorization_server_image(filename, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def serve_an_authorization_server_java_script_asset(
        self, filename: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        filename : str
            Static asset filename, optionally including a Phoenix digest

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
            await client.assets.serve_an_authorization_server_java_script_asset(
                filename="filename",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.serve_an_authorization_server_java_script_asset(
            filename, request_options=request_options
        )
        return _response.data

    async def serve_an_authorization_server_admin_asset(
        self, filename: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        filename : str
            Static asset filename, optionally including a Phoenix digest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Static asset

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.assets.serve_an_authorization_server_admin_asset(
                filename="filename",
            )


        asyncio.run(main())
        """
        async with self._raw_client.serve_an_authorization_server_admin_asset(
            filename, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def serve_a_top_level_identity_asset(
        self, filename: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        filename : str
            Static asset filename, optionally including a Phoenix digest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Static asset

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.assets.serve_a_top_level_identity_asset(
                filename="filename",
            )


        asyncio.run(main())
        """
        async with self._raw_client.serve_a_top_level_identity_asset(filename, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def serve_an_identity_stylesheet(
        self, filename: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Parameters
        ----------
        filename : str
            Static asset filename, optionally including a Phoenix digest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            CSS stylesheet

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.assets.serve_an_identity_stylesheet(
                filename="filename",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.serve_an_identity_stylesheet(filename, request_options=request_options)
        return _response.data

    async def serve_an_identity_java_script_asset(
        self, filename: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        filename : str
            Static asset filename, optionally including a Phoenix digest

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
            await client.assets.serve_an_identity_java_script_asset(
                filename="filename",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.serve_an_identity_java_script_asset(
            filename, request_options=request_options
        )
        return _response.data

    async def serve_an_identity_image(
        self, filename: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        filename : str
            Static asset filename, optionally including a Phoenix digest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Image asset

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.assets.serve_an_identity_image(
                filename="filename",
            )


        asyncio.run(main())
        """
        async with self._raw_client.serve_an_identity_image(filename, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def serve_the_identity_web_app_manifest(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Web app manifest

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.assets.serve_the_identity_web_app_manifest()


        asyncio.run(main())
        """
        _response = await self._raw_client.serve_the_identity_web_app_manifest(request_options=request_options)
        return _response.data

    async def serve_the_identity_favicon(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Icon asset

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.assets.serve_the_identity_favicon()


        asyncio.run(main())
        """
        async with self._raw_client.serve_the_identity_favicon(request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def serve_the_identity_robots_txt(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Text asset

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.assets.serve_the_identity_robots_txt()


        asyncio.run(main())
        """
        _response = await self._raw_client.serve_the_identity_robots_txt(request_options=request_options)
        return _response.data

    async def serve_the_identity_semantic_ui_stylesheet(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            CSS stylesheet

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.assets.serve_the_identity_semantic_ui_stylesheet()


        asyncio.run(main())
        """
        _response = await self._raw_client.serve_the_identity_semantic_ui_stylesheet(request_options=request_options)
        return _response.data

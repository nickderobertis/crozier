

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawSystemClient, RawSystemClient
from .types.health_response import HealthResponse


class SystemClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSystemClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSystemClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSystemClient
        """
        return self._raw_client

    def root(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            token="YOUR_TOKEN",
        )
        client.system.root()
        """
        _response = self._raw_client.root(request_options=request_options)
        return _response.data

    def api_swagger_ui(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            HTML

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.system.api_swagger_ui()
        """
        _response = self._raw_client.api_swagger_ui(request_options=request_options)
        return _response.data

    def api_openapi_spec(
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
            OpenAPI JSON

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.system.api_openapi_spec()
        """
        _response = self._raw_client.api_openapi_spec(request_options=request_options)
        return _response.data

    def health(self, *, request_options: typing.Optional[RequestOptions] = None) -> HealthResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HealthResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.system.health()
        """
        _response = self._raw_client.health(request_options=request_options)
        return _response.data

    def sw_js(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            token="YOUR_TOKEN",
        )
        client.system.sw_js()
        """
        _response = self._raw_client.sw_js(request_options=request_options)
        return _response.data

    def ui(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            token="YOUR_TOKEN",
        )
        client.system.ui()
        """
        _response = self._raw_client.ui(request_options=request_options)
        return _response.data

    def ui_trailing_slash(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            token="YOUR_TOKEN",
        )
        client.system.ui_trailing_slash()
        """
        _response = self._raw_client.ui_trailing_slash(request_options=request_options)
        return _response.data

    def web_swagger_ui(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            HTML

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.system.web_swagger_ui()
        """
        _response = self._raw_client.web_swagger_ui(request_options=request_options)
        return _response.data

    def web_meta_public(
        self, *, force: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        force : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.system.web_meta_public()
        """
        _response = self._raw_client.web_meta_public(force=force, request_options=request_options)
        return _response.data

    def web_openapi_spec(
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
            OpenAPI JSON

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.system.web_openapi_spec()
        """
        _response = self._raw_client.web_openapi_spec(request_options=request_options)
        return _response.data


class AsyncSystemClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSystemClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSystemClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSystemClient
        """
        return self._raw_client

    async def root(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.system.root()


        asyncio.run(main())
        """
        _response = await self._raw_client.root(request_options=request_options)
        return _response.data

    async def api_swagger_ui(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            HTML

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.system.api_swagger_ui()


        asyncio.run(main())
        """
        _response = await self._raw_client.api_swagger_ui(request_options=request_options)
        return _response.data

    async def api_openapi_spec(
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
            OpenAPI JSON

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.system.api_openapi_spec()


        asyncio.run(main())
        """
        _response = await self._raw_client.api_openapi_spec(request_options=request_options)
        return _response.data

    async def health(self, *, request_options: typing.Optional[RequestOptions] = None) -> HealthResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HealthResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.system.health()


        asyncio.run(main())
        """
        _response = await self._raw_client.health(request_options=request_options)
        return _response.data

    async def sw_js(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.system.sw_js()


        asyncio.run(main())
        """
        _response = await self._raw_client.sw_js(request_options=request_options)
        return _response.data

    async def ui(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.system.ui()


        asyncio.run(main())
        """
        _response = await self._raw_client.ui(request_options=request_options)
        return _response.data

    async def ui_trailing_slash(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.system.ui_trailing_slash()


        asyncio.run(main())
        """
        _response = await self._raw_client.ui_trailing_slash(request_options=request_options)
        return _response.data

    async def web_swagger_ui(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            HTML

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.system.web_swagger_ui()


        asyncio.run(main())
        """
        _response = await self._raw_client.web_swagger_ui(request_options=request_options)
        return _response.data

    async def web_meta_public(
        self, *, force: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        force : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.system.web_meta_public()


        asyncio.run(main())
        """
        _response = await self._raw_client.web_meta_public(force=force, request_options=request_options)
        return _response.data

    async def web_openapi_spec(
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
            OpenAPI JSON

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.system.web_openapi_spec()


        asyncio.run(main())
        """
        _response = await self._raw_client.web_openapi_spec(request_options=request_options)
        return _response.data

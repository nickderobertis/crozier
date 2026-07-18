

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.request_info import RequestInfo
from .raw_client import AsyncRawWildcardInspectionRoutesClient, RawWildcardInspectionRoutesClient


class WildcardInspectionRoutesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawWildcardInspectionRoutesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawWildcardInspectionRoutesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawWildcardInspectionRoutesClient
        """
        return self._raw_client

    def wildcard_inspect_anything(
        self, extra_path: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RequestInfo:
        """
        Any route or path that doesn't match other operations is automatically inspected, e.g. /blah/cheese/shoe will still return the details of the request

        Parameters
        ----------
        extra_path : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RequestInfo
            The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.wildcard_inspection_routes.wildcard_inspect_anything(
            extra_path="extraPath",
        )
        """
        _response = self._raw_client.wildcard_inspect_anything(extra_path, request_options=request_options)
        return _response.data

    def wildcard_inspect_anything_post(
        self, extra_path: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RequestInfo:
        """
        Any route or path that doesn't match other operations is automatically inspected, e.g. /blah/cheese/shoe will still return the details of the request

        Parameters
        ----------
        extra_path : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RequestInfo
            The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.wildcard_inspection_routes.wildcard_inspect_anything_post(
            extra_path="extraPath",
        )
        """
        _response = self._raw_client.wildcard_inspect_anything_post(extra_path, request_options=request_options)
        return _response.data

    def wildcard_inspect_anything_put(
        self, extra_path: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RequestInfo:
        """
        Any route or path that doesn't match other operations is automatically inspected, e.g. /blah/cheese/shoe will still return the details of the request

        Parameters
        ----------
        extra_path : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RequestInfo
            The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.wildcard_inspection_routes.wildcard_inspect_anything_put(
            extra_path="extraPath",
        )
        """
        _response = self._raw_client.wildcard_inspect_anything_put(extra_path, request_options=request_options)
        return _response.data

    def wildcard_inspect_anything_delete(
        self, extra_path: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RequestInfo:
        """
        Any route or path that doesn't match other operations is automatically inspected, e.g. /blah/cheese/shoe will still return the details of the request

        Parameters
        ----------
        extra_path : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RequestInfo
            The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.wildcard_inspection_routes.wildcard_inspect_anything_delete(
            extra_path="extraPath",
        )
        """
        _response = self._raw_client.wildcard_inspect_anything_delete(extra_path, request_options=request_options)
        return _response.data

    def wildcard_inspect_anything_patch(
        self, extra_path: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RequestInfo:
        """
        Any route or path that doesn't match other operations is automatically inspected, e.g. /blah/cheese/shoe will still return the details of the request

        Parameters
        ----------
        extra_path : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RequestInfo
            The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.wildcard_inspection_routes.wildcard_inspect_anything_patch(
            extra_path="extraPath",
        )
        """
        _response = self._raw_client.wildcard_inspect_anything_patch(extra_path, request_options=request_options)
        return _response.data


class AsyncWildcardInspectionRoutesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawWildcardInspectionRoutesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawWildcardInspectionRoutesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawWildcardInspectionRoutesClient
        """
        return self._raw_client

    async def wildcard_inspect_anything(
        self, extra_path: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RequestInfo:
        """
        Any route or path that doesn't match other operations is automatically inspected, e.g. /blah/cheese/shoe will still return the details of the request

        Parameters
        ----------
        extra_path : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RequestInfo
            The request has succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.wildcard_inspection_routes.wildcard_inspect_anything(
                extra_path="extraPath",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.wildcard_inspect_anything(extra_path, request_options=request_options)
        return _response.data

    async def wildcard_inspect_anything_post(
        self, extra_path: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RequestInfo:
        """
        Any route or path that doesn't match other operations is automatically inspected, e.g. /blah/cheese/shoe will still return the details of the request

        Parameters
        ----------
        extra_path : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RequestInfo
            The request has succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.wildcard_inspection_routes.wildcard_inspect_anything_post(
                extra_path="extraPath",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.wildcard_inspect_anything_post(extra_path, request_options=request_options)
        return _response.data

    async def wildcard_inspect_anything_put(
        self, extra_path: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RequestInfo:
        """
        Any route or path that doesn't match other operations is automatically inspected, e.g. /blah/cheese/shoe will still return the details of the request

        Parameters
        ----------
        extra_path : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RequestInfo
            The request has succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.wildcard_inspection_routes.wildcard_inspect_anything_put(
                extra_path="extraPath",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.wildcard_inspect_anything_put(extra_path, request_options=request_options)
        return _response.data

    async def wildcard_inspect_anything_delete(
        self, extra_path: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RequestInfo:
        """
        Any route or path that doesn't match other operations is automatically inspected, e.g. /blah/cheese/shoe will still return the details of the request

        Parameters
        ----------
        extra_path : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RequestInfo
            The request has succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.wildcard_inspection_routes.wildcard_inspect_anything_delete(
                extra_path="extraPath",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.wildcard_inspect_anything_delete(extra_path, request_options=request_options)
        return _response.data

    async def wildcard_inspect_anything_patch(
        self, extra_path: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RequestInfo:
        """
        Any route or path that doesn't match other operations is automatically inspected, e.g. /blah/cheese/shoe will still return the details of the request

        Parameters
        ----------
        extra_path : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RequestInfo
            The request has succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.wildcard_inspection_routes.wildcard_inspect_anything_patch(
                extra_path="extraPath",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.wildcard_inspect_anything_patch(extra_path, request_options=request_options)
        return _response.data

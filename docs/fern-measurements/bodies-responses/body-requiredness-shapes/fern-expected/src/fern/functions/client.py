

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawFunctionsClient, RawFunctionsClient


OMIT = typing.cast(typing.Any, ...)


class FunctionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFunctionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFunctionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFunctionsClient
        """
        return self._raw_client

    def validate_inputs(
        self,
        function_id: str,
        *,
        request: typing.Optional[typing.Dict[str, typing.Any]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Parameters
        ----------
        function_id : str

        request : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Validated.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.functions.validate_inputs(
            function_id="functionId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.validate_inputs(function_id, request=request, request_options=request_options)
        return _response.data

    def run_function(
        self,
        *,
        request: typing.Optional[typing.Dict[str, typing.Any]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        request : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.functions.run_function(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.run_function(request=request, request_options=request_options)
        return _response.data

    def schedule_function(
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

        client = FernApi()
        client.functions.schedule_function(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.schedule_function(request=request, request_options=request_options)
        return _response.data


class AsyncFunctionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFunctionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFunctionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFunctionsClient
        """
        return self._raw_client

    async def validate_inputs(
        self,
        function_id: str,
        *,
        request: typing.Optional[typing.Dict[str, typing.Any]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Parameters
        ----------
        function_id : str

        request : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Validated.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.functions.validate_inputs(
                function_id="functionId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.validate_inputs(
            function_id, request=request, request_options=request_options
        )
        return _response.data

    async def run_function(
        self,
        *,
        request: typing.Optional[typing.Dict[str, typing.Any]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        request : typing.Optional[typing.Dict[str, typing.Any]]

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
            await client.functions.run_function(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.run_function(request=request, request_options=request_options)
        return _response.data

    async def schedule_function(
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

        client = AsyncFernApi()


        async def main() -> None:
            await client.functions.schedule_function(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.schedule_function(request=request, request_options=request_options)
        return _response.data

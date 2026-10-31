

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawSimpleCasesClient, RawSimpleCasesClient
from .types.simple_cases_nullable_response import SimpleCasesNullableResponse
from .types.simple_cases_nullish_response import SimpleCasesNullishResponse
from .types.simple_cases_optional_response import SimpleCasesOptionalResponse


class SimpleCasesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSimpleCasesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSimpleCasesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSimpleCasesClient
        """
        return self._raw_client

    def simple_cases_nullish(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SimpleCasesNullishResponse:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SimpleCasesNullishResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.simple_cases.simple_cases_nullish(
            input="input",
        )
        """
        _response = self._raw_client.simple_cases_nullish(input=input, request_options=request_options)
        return _response.data

    def simple_cases_optional(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SimpleCasesOptionalResponse:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SimpleCasesOptionalResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.simple_cases.simple_cases_optional(
            input="input",
        )
        """
        _response = self._raw_client.simple_cases_optional(input=input, request_options=request_options)
        return _response.data

    def simple_cases_nullable(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SimpleCasesNullableResponse:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SimpleCasesNullableResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.simple_cases.simple_cases_nullable(
            input="input",
        )
        """
        _response = self._raw_client.simple_cases_nullable(input=input, request_options=request_options)
        return _response.data


class AsyncSimpleCasesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSimpleCasesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSimpleCasesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSimpleCasesClient
        """
        return self._raw_client

    async def simple_cases_nullish(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SimpleCasesNullishResponse:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SimpleCasesNullishResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.simple_cases.simple_cases_nullish(
                input="input",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.simple_cases_nullish(input=input, request_options=request_options)
        return _response.data

    async def simple_cases_optional(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SimpleCasesOptionalResponse:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SimpleCasesOptionalResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.simple_cases.simple_cases_optional(
                input="input",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.simple_cases_optional(input=input, request_options=request_options)
        return _response.data

    async def simple_cases_nullable(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SimpleCasesNullableResponse:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SimpleCasesNullableResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.simple_cases.simple_cases_nullable(
                input="input",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.simple_cases_nullable(input=input, request_options=request_options)
        return _response.data

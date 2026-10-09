

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawConversionClient, RawConversionClient
from .types.convert_request_validate import ConvertRequestValidate


OMIT = typing.cast(typing.Any, ...)


class ConversionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawConversionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawConversionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawConversionClient
        """
        return self._raw_client

    def convert_url(self, *, url: str, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """


        Parameters
        ----------
        url : str
            The URL to retrieve the OpenAPI 2.0 definition from

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            default

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.conversion.convert_url(
            url="https://raw.githubusercontent.com/Mermade/openapi-webconverter/master/contract/swagger.json",
        )
        """
        _response = self._raw_client.convert_url(url=url, request_options=request_options)
        return _response.data

    def convert(
        self,
        *,
        filename: typing.Optional[str] = OMIT,
        source: typing.Optional[str] = OMIT,
        validate: typing.Optional[ConvertRequestValidate] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """


        Parameters
        ----------
        filename : typing.Optional[str]
            The file to upload and convert

        source : typing.Optional[str]
            The text of a Swagger 2.0 definition to convert

        validate : typing.Optional[ConvertRequestValidate]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            default

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.conversion.convert()
        """
        _response = self._raw_client.convert(
            filename=filename, source=source, validate=validate, request_options=request_options
        )
        return _response.data


class AsyncConversionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawConversionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawConversionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawConversionClient
        """
        return self._raw_client

    async def convert_url(self, *, url: str, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """


        Parameters
        ----------
        url : str
            The URL to retrieve the OpenAPI 2.0 definition from

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            default

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.conversion.convert_url(
                url="https://raw.githubusercontent.com/Mermade/openapi-webconverter/master/contract/swagger.json",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.convert_url(url=url, request_options=request_options)
        return _response.data

    async def convert(
        self,
        *,
        filename: typing.Optional[str] = OMIT,
        source: typing.Optional[str] = OMIT,
        validate: typing.Optional[ConvertRequestValidate] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """


        Parameters
        ----------
        filename : typing.Optional[str]
            The file to upload and convert

        source : typing.Optional[str]
            The text of a Swagger 2.0 definition to convert

        validate : typing.Optional[ConvertRequestValidate]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            default

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.conversion.convert()


        asyncio.run(main())
        """
        _response = await self._raw_client.convert(
            filename=filename, source=source, validate=validate, request_options=request_options
        )
        return _response.data

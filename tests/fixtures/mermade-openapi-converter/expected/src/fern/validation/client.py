

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.validation_result import ValidationResult
from .raw_client import AsyncRawValidationClient, RawValidationClient


OMIT = typing.cast(typing.Any, ...)


class ValidationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawValidationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawValidationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawValidationClient
        """
        return self._raw_client

    def get_badge(self, *, url: str, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        url : str
            The URL to retrieve the OpenAPI 3.0.x definition from

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.validation.get_badge(
            url="https://raw.githubusercontent.com/Mermade/openapi-webconverter/master/contract/openapi.json",
        )
        """
        _response = self._raw_client.get_badge(url=url, request_options=request_options)
        return _response.data

    def validate_url(self, *, url: str, request_options: typing.Optional[RequestOptions] = None) -> ValidationResult:
        """


        Parameters
        ----------
        url : str
            The URL to retrieve the OpenAPI 3.0.x definition from

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ValidationResult
            default

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.validation.validate_url(
            url="https://raw.githubusercontent.com/Mermade/openapi-webconverter/master/contract/openapi.json",
        )
        """
        _response = self._raw_client.validate_url(url=url, request_options=request_options)
        return _response.data

    def validate(
        self,
        *,
        filename: typing.Optional[str] = OMIT,
        source: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ValidationResult:
        """


        Parameters
        ----------
        filename : typing.Optional[str]
            The file to upload and validate

        source : typing.Optional[str]
            The text of an OpenAPI 3.0.x definition to validate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ValidationResult
            default

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.validation.validate()
        """
        _response = self._raw_client.validate(filename=filename, source=source, request_options=request_options)
        return _response.data


class AsyncValidationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawValidationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawValidationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawValidationClient
        """
        return self._raw_client

    async def get_badge(self, *, url: str, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        url : str
            The URL to retrieve the OpenAPI 3.0.x definition from

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
            await client.validation.get_badge(
                url="https://raw.githubusercontent.com/Mermade/openapi-webconverter/master/contract/openapi.json",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_badge(url=url, request_options=request_options)
        return _response.data

    async def validate_url(
        self, *, url: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ValidationResult:
        """


        Parameters
        ----------
        url : str
            The URL to retrieve the OpenAPI 3.0.x definition from

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ValidationResult
            default

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.validation.validate_url(
                url="https://raw.githubusercontent.com/Mermade/openapi-webconverter/master/contract/openapi.json",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.validate_url(url=url, request_options=request_options)
        return _response.data

    async def validate(
        self,
        *,
        filename: typing.Optional[str] = OMIT,
        source: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ValidationResult:
        """


        Parameters
        ----------
        filename : typing.Optional[str]
            The file to upload and validate

        source : typing.Optional[str]
            The text of an OpenAPI 3.0.x definition to validate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ValidationResult
            default

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.validation.validate()


        asyncio.run(main())
        """
        _response = await self._raw_client.validate(filename=filename, source=source, request_options=request_options)
        return _response.data

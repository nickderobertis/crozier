

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_test_response import ApiTestResponse
from .raw_client import AsyncRawApiTestingClient, RawApiTestingClient
from .types.test_api_api_v1testapi_post_request_provider import TestApiApiV1TestapiPostRequestProvider


OMIT = typing.cast(typing.Any, ...)


class ApiTestingClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawApiTestingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawApiTestingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawApiTestingClient
        """
        return self._raw_client

    def test_api(
        self,
        *,
        base_url: str,
        output: typing.Optional[str] = OMIT,
        spec_file: typing.Optional[str] = OMIT,
        spec_upload: typing.Optional[core.File] = OMIT,
        provider: typing.Optional[TestApiApiV1TestapiPostRequestProvider] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiTestResponse:
        """
        Run API tests using either a spec file path or uploaded spec file

        Parameters
        ----------
        base_url : str
            Base URL for API testing

        output : typing.Optional[str]
            Output file path

        spec_file : typing.Optional[str]
            Path to OpenAPI spec file

        spec_upload : typing.Optional[core.File]
            See core.File for more documentation

        provider : typing.Optional[TestApiApiV1TestapiPostRequestProvider]
            LLM Provider

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiTestResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.api_testing.test_api(
            base_url="base_url",
        )
        """
        _response = self._raw_client.test_api(
            base_url=base_url,
            output=output,
            spec_file=spec_file,
            spec_upload=spec_upload,
            provider=provider,
            request_options=request_options,
        )
        return _response.data


class AsyncApiTestingClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawApiTestingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawApiTestingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawApiTestingClient
        """
        return self._raw_client

    async def test_api(
        self,
        *,
        base_url: str,
        output: typing.Optional[str] = OMIT,
        spec_file: typing.Optional[str] = OMIT,
        spec_upload: typing.Optional[core.File] = OMIT,
        provider: typing.Optional[TestApiApiV1TestapiPostRequestProvider] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiTestResponse:
        """
        Run API tests using either a spec file path or uploaded spec file

        Parameters
        ----------
        base_url : str
            Base URL for API testing

        output : typing.Optional[str]
            Output file path

        spec_file : typing.Optional[str]
            Path to OpenAPI spec file

        spec_upload : typing.Optional[core.File]
            See core.File for more documentation

        provider : typing.Optional[TestApiApiV1TestapiPostRequestProvider]
            LLM Provider

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiTestResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.api_testing.test_api(
                base_url="base_url",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.test_api(
            base_url=base_url,
            output=output,
            spec_file=spec_file,
            spec_upload=spec_upload,
            provider=provider,
            request_options=request_options,
        )
        return _response.data

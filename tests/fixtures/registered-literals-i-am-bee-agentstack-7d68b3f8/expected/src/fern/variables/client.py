

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.list_variables_schema import ListVariablesSchema
from .raw_client import AsyncRawVariablesClient, RawVariablesClient


OMIT = typing.cast(typing.Any, ...)


class VariablesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawVariablesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawVariablesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawVariablesClient
        """
        return self._raw_client

    def list_user_variables(self, *, request_options: typing.Optional[RequestOptions] = None) -> ListVariablesSchema:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListVariablesSchema
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.variables.list_user_variables()
        """
        _response = self._raw_client.list_user_variables(request_options=request_options)
        return _response.data

    def update_user_variables(
        self,
        *,
        variables: typing.Dict[str, typing.Optional[str]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Parameters
        ----------
        variables : typing.Dict[str, typing.Optional[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.variables.update_user_variables(
            variables={},
        )
        """
        _response = self._raw_client.update_user_variables(variables=variables, request_options=request_options)
        return _response.data


class AsyncVariablesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawVariablesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawVariablesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawVariablesClient
        """
        return self._raw_client

    async def list_user_variables(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListVariablesSchema:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListVariablesSchema
            Successful Response

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
            await client.variables.list_user_variables()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_user_variables(request_options=request_options)
        return _response.data

    async def update_user_variables(
        self,
        *,
        variables: typing.Dict[str, typing.Optional[str]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Parameters
        ----------
        variables : typing.Dict[str, typing.Optional[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

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
            await client.variables.update_user_variables(
                variables={},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_user_variables(variables=variables, request_options=request_options)
        return _response.data

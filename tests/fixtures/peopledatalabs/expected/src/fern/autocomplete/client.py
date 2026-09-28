

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAutocompleteClient, RawAutocompleteClient
from .types.post_v5autocomplete_request_field import PostV5AutocompleteRequestField


OMIT = typing.cast(typing.Any, ...)


class AutocompleteClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAutocompleteClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAutocompleteClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAutocompleteClient
        """
        return self._raw_client

    def autocomplete(
        self,
        *,
        field: typing.Optional[PostV5AutocompleteRequestField] = OMIT,
        text: typing.Optional[str] = OMIT,
        size: typing.Optional[int] = OMIT,
        titlecase: typing.Optional[bool] = OMIT,
        pretty: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        field : typing.Optional[PostV5AutocompleteRequestField]
            An enumerated field that will be used to calculate the autocompletion

        text : typing.Optional[str]
            Text that is used as the seed for autocompletion

        size : typing.Optional[int]
            The number of results returned for autocompletion

        titlecase : typing.Optional[bool]
            Setting titlecase to true will titlecase any records returned

        pretty : typing.Optional[bool]
            Whether the output should have human-readable indentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.autocomplete.autocomplete()
        """
        _response = self._raw_client.autocomplete(
            field=field, text=text, size=size, titlecase=titlecase, pretty=pretty, request_options=request_options
        )
        return _response.data


class AsyncAutocompleteClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAutocompleteClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAutocompleteClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAutocompleteClient
        """
        return self._raw_client

    async def autocomplete(
        self,
        *,
        field: typing.Optional[PostV5AutocompleteRequestField] = OMIT,
        text: typing.Optional[str] = OMIT,
        size: typing.Optional[int] = OMIT,
        titlecase: typing.Optional[bool] = OMIT,
        pretty: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        field : typing.Optional[PostV5AutocompleteRequestField]
            An enumerated field that will be used to calculate the autocompletion

        text : typing.Optional[str]
            Text that is used as the seed for autocompletion

        size : typing.Optional[int]
            The number of results returned for autocompletion

        titlecase : typing.Optional[bool]
            Setting titlecase to true will titlecase any records returned

        pretty : typing.Optional[bool]
            Whether the output should have human-readable indentation

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.autocomplete.autocomplete()


        asyncio.run(main())
        """
        _response = await self._raw_client.autocomplete(
            field=field, text=text, size=size, titlecase=titlecase, pretty=pretty, request_options=request_options
        )
        return _response.data

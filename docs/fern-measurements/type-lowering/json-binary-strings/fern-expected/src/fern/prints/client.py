

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.print import Print
from .raw_client import AsyncRawPrintsClient, RawPrintsClient


OMIT = typing.cast(typing.Any, ...)


class PrintsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPrintsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPrintsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPrintsClient
        """
        return self._raw_client

    def submit_print(
        self,
        *,
        instructions: str,
        negative: typing.Optional[bytes] = OMIT,
        contacts: typing.Optional[typing.Sequence[str]] = OMIT,
        layers: typing.Optional[typing.Dict[str, str]] = OMIT,
        mask: typing.Optional[bytes] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Print:
        """
        Parameters
        ----------
        instructions : str

        negative : typing.Optional[bytes]

        contacts : typing.Optional[typing.Sequence[str]]

        layers : typing.Optional[typing.Dict[str, str]]

        mask : typing.Optional[bytes]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Print
            The developed print.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.prints.submit_print(
            instructions="instructions",
        )
        """
        _response = self._raw_client.submit_print(
            instructions=instructions,
            negative=negative,
            contacts=contacts,
            layers=layers,
            mask=mask,
            request_options=request_options,
        )
        return _response.data


class AsyncPrintsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPrintsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPrintsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPrintsClient
        """
        return self._raw_client

    async def submit_print(
        self,
        *,
        instructions: str,
        negative: typing.Optional[bytes] = OMIT,
        contacts: typing.Optional[typing.Sequence[str]] = OMIT,
        layers: typing.Optional[typing.Dict[str, str]] = OMIT,
        mask: typing.Optional[bytes] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Print:
        """
        Parameters
        ----------
        instructions : str

        negative : typing.Optional[bytes]

        contacts : typing.Optional[typing.Sequence[str]]

        layers : typing.Optional[typing.Dict[str, str]]

        mask : typing.Optional[bytes]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Print
            The developed print.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.prints.submit_print(
                instructions="instructions",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.submit_print(
            instructions=instructions,
            negative=negative,
            contacts=contacts,
            layers=layers,
            mask=mask,
            request_options=request_options,
        )
        return _response.data

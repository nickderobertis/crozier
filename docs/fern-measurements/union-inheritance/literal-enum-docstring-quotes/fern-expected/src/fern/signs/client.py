

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawSignsClient, RawSignsClient
from .types.hang_signs_request_motto import HangSignsRequestMotto
from .types.hang_signs_request_wordings_item import HangSignsRequestWordingsItem


OMIT = typing.cast(typing.Any, ...)


class SignsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSignsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSignsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSignsClient
        """
        return self._raw_client

    def hang_signs(
        self,
        *,
        wordings: typing.Sequence[HangSignsRequestWordingsItem],
        motto: HangSignsRequestMotto,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        wordings : typing.Sequence[HangSignsRequestWordingsItem]

        motto : HangSignsRequestMotto

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.signs import HangSignsRequestMotto, HangSignsRequestWordingsItem

        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.signs.hang_signs(
            wordings=[HangSignsRequestWordingsItem.SAY_CHEESE],
            motto=HangSignsRequestMotto.THE_EARLY_BIRD,
        )
        """
        _response = self._raw_client.hang_signs(wordings=wordings, motto=motto, request_options=request_options)
        return _response.data


class AsyncSignsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSignsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSignsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSignsClient
        """
        return self._raw_client

    async def hang_signs(
        self,
        *,
        wordings: typing.Sequence[HangSignsRequestWordingsItem],
        motto: HangSignsRequestMotto,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        wordings : typing.Sequence[HangSignsRequestWordingsItem]

        motto : HangSignsRequestMotto

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.signs import HangSignsRequestMotto, HangSignsRequestWordingsItem

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.signs.hang_signs(
                wordings=[HangSignsRequestWordingsItem.SAY_CHEESE],
                motto=HangSignsRequestMotto.THE_EARLY_BIRD,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.hang_signs(wordings=wordings, motto=motto, request_options=request_options)
        return _response.data

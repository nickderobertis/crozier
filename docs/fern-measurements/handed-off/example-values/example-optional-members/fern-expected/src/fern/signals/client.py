

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.lamp_code import LampCode
from ..types.moment import Moment
from ..types.quoted_moment import QuotedMoment
from .raw_client import AsyncRawSignalsClient, RawSignalsClient


class SignalsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSignalsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSignalsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSignalsClient
        """
        return self._raw_client

    def list_signals(
        self,
        *,
        observed_to: Moment,
        observed_from: typing.Optional[Moment] = None,
        quoted_from: typing.Optional[QuotedMoment] = None,
        lamp: typing.Optional[LampCode] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        observed_to : Moment

        observed_from : typing.Optional[Moment]

        quoted_from : typing.Optional[QuotedMoment]

        lamp : typing.Optional[LampCode]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Signals

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.signals.list_signals(
            quoted_from=datetime.datetime.fromisoformat(
                "2032-06-02 04:30:00+00:00",
            ),
            lamp="lamp-east",
            observed_to=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
        )
        """
        _response = self._raw_client.list_signals(
            observed_to=observed_to,
            observed_from=observed_from,
            quoted_from=quoted_from,
            lamp=lamp,
            limit=limit,
            request_options=request_options,
        )
        return _response.data


class AsyncSignalsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSignalsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSignalsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSignalsClient
        """
        return self._raw_client

    async def list_signals(
        self,
        *,
        observed_to: Moment,
        observed_from: typing.Optional[Moment] = None,
        quoted_from: typing.Optional[QuotedMoment] = None,
        lamp: typing.Optional[LampCode] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        observed_to : Moment

        observed_from : typing.Optional[Moment]

        quoted_from : typing.Optional[QuotedMoment]

        lamp : typing.Optional[LampCode]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Signals

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.signals.list_signals(
                quoted_from=datetime.datetime.fromisoformat(
                    "2032-06-02 04:30:00+00:00",
                ),
                lamp="lamp-east",
                observed_to=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_signals(
            observed_to=observed_to,
            observed_from=observed_from,
            quoted_from=quoted_from,
            lamp=lamp,
            limit=limit,
            request_options=request_options,
        )
        return _response.data

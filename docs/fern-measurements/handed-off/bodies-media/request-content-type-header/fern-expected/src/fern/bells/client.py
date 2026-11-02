

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.bell import Bell
from .raw_client import AsyncRawBellsClient, RawBellsClient


OMIT = typing.cast(typing.Any, ...)


class BellsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBellsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBellsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBellsClient
        """
        return self._raw_client

    def tune_bell(
        self,
        bell_id: str,
        *,
        strike_note: str,
        hum: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        bell_id : str

        strike_note : str

        hum : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.bells.tune_bell(
            bell_id="bellId",
            strike_note="strikeNote",
        )
        """
        _response = self._raw_client.tune_bell(
            bell_id, strike_note=strike_note, hum=hum, request_options=request_options
        )
        return _response.data

    def inscribe_bell(
        self,
        bell_id: str,
        *,
        text: str,
        face: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        bell_id : str

        text : str

        face : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.bells.inscribe_bell(
            bell_id="bellId",
            text="text",
        )
        """
        _response = self._raw_client.inscribe_bell(bell_id, text=text, face=face, request_options=request_options)
        return _response.data

    def create_bell(
        self,
        *,
        name: typing.Optional[str] = OMIT,
        note: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Bell:
        """
        Parameters
        ----------
        name : typing.Optional[str]

        note : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Bell
            The bell as stored.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.bells.create_bell(
            name="Great Tom",
            note="E flat",
        )
        """
        _response = self._raw_client.create_bell(name=name, note=note, request_options=request_options)
        return _response.data

    def get_bell(self, bell_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Bell:
        """
        Parameters
        ----------
        bell_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Bell
            The bell.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.bells.get_bell(
            bell_id="bellId",
        )
        """
        _response = self._raw_client.get_bell(bell_id, request_options=request_options)
        return _response.data

    def replace_bell(
        self,
        bell_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        note: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Bell:
        """
        Parameters
        ----------
        bell_id : str

        name : typing.Optional[str]

        note : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Bell
            The bell as stored.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.bells.replace_bell(
            bell_id="bellId",
            name="Great Tom",
            note="E flat",
        )
        """
        _response = self._raw_client.replace_bell(bell_id, name=name, note=note, request_options=request_options)
        return _response.data


class AsyncBellsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBellsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBellsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBellsClient
        """
        return self._raw_client

    async def tune_bell(
        self,
        bell_id: str,
        *,
        strike_note: str,
        hum: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        bell_id : str

        strike_note : str

        hum : typing.Optional[str]

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
            await client.bells.tune_bell(
                bell_id="bellId",
                strike_note="strikeNote",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.tune_bell(
            bell_id, strike_note=strike_note, hum=hum, request_options=request_options
        )
        return _response.data

    async def inscribe_bell(
        self,
        bell_id: str,
        *,
        text: str,
        face: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        bell_id : str

        text : str

        face : typing.Optional[str]

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
            await client.bells.inscribe_bell(
                bell_id="bellId",
                text="text",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.inscribe_bell(bell_id, text=text, face=face, request_options=request_options)
        return _response.data

    async def create_bell(
        self,
        *,
        name: typing.Optional[str] = OMIT,
        note: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Bell:
        """
        Parameters
        ----------
        name : typing.Optional[str]

        note : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Bell
            The bell as stored.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.bells.create_bell(
                name="Great Tom",
                note="E flat",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_bell(name=name, note=note, request_options=request_options)
        return _response.data

    async def get_bell(self, bell_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Bell:
        """
        Parameters
        ----------
        bell_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Bell
            The bell.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.bells.get_bell(
                bell_id="bellId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_bell(bell_id, request_options=request_options)
        return _response.data

    async def replace_bell(
        self,
        bell_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        note: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Bell:
        """
        Parameters
        ----------
        bell_id : str

        name : typing.Optional[str]

        note : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Bell
            The bell as stored.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.bells.replace_bell(
                bell_id="bellId",
                name="Great Tom",
                note="E flat",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.replace_bell(bell_id, name=name, note=note, request_options=request_options)
        return _response.data

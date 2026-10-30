

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawRoomCorrectionClient, RawRoomCorrectionClient
from .types.room_corr_get_response import RoomCorrGetResponse


class RoomCorrectionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRoomCorrectionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRoomCorrectionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRoomCorrectionClient
        """
        return self._raw_client

    def room_corr_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> RoomCorrGetResponse:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=RoomCorrGet

        It returns a JSON object with the current room correction settings, including the EQ levels for each band, the source name, and other related information.
        The "EQBand" array contains objects for each EQ band, with parameters such as "mode", "freq", "q", and "gain".
        This information can be used to understand the current room correction configuration and make informed adjustments if needed.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RoomCorrGetResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.room_correction.room_corr_get()
        """
        _response = self._raw_client.room_corr_get(request_options=request_options)
        return _response.data

    def room_corr_get_mode(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=RoomCorrGetMode

        Same as RoomCorrGet?

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.room_correction.room_corr_get_mode()
        """
        _response = self._raw_client.room_corr_get_mode(request_options=request_options)
        return _response.data

    def room_corr_set(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=RoomCorrSet:{str}

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.room_correction.room_corr_set(
            str="str",
        )
        """
        _response = self._raw_client.room_corr_set(str, request_options=request_options)
        return _response.data

    def room_corr_set_lr(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=RoomCorrSetLR:{str}

        Same as RoomCorrSet?

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.room_correction.room_corr_set_lr(
            str="str",
        )
        """
        _response = self._raw_client.room_corr_set_lr(str, request_options=request_options)
        return _response.data

    def room_corr_set_mode(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.room_correction.room_corr_set_mode(
            str="str",
        )
        """
        _response = self._raw_client.room_corr_set_mode(str, request_options=request_options)
        return _response.data

    def set_room_correction(
        self, str: str, time: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        time : str
            Format yyyy:MM:dd HH:mm

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.room_correction.set_room_correction(
            str="str",
            time="time",
        )
        """
        _response = self._raw_client.set_room_correction(str, time, request_options=request_options)
        return _response.data


class AsyncRoomCorrectionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRoomCorrectionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRoomCorrectionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRoomCorrectionClient
        """
        return self._raw_client

    async def room_corr_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> RoomCorrGetResponse:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=RoomCorrGet

        It returns a JSON object with the current room correction settings, including the EQ levels for each band, the source name, and other related information.
        The "EQBand" array contains objects for each EQ band, with parameters such as "mode", "freq", "q", and "gain".
        This information can be used to understand the current room correction configuration and make informed adjustments if needed.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RoomCorrGetResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.room_correction.room_corr_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.room_corr_get(request_options=request_options)
        return _response.data

    async def room_corr_get_mode(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=RoomCorrGetMode

        Same as RoomCorrGet?

        Parameters
        ----------
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
            await client.room_correction.room_corr_get_mode()


        asyncio.run(main())
        """
        _response = await self._raw_client.room_corr_get_mode(request_options=request_options)
        return _response.data

    async def room_corr_set(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=RoomCorrSet:{str}

        Parameters
        ----------
        str : str
            Unknown

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
            await client.room_correction.room_corr_set(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.room_corr_set(str, request_options=request_options)
        return _response.data

    async def room_corr_set_lr(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=RoomCorrSetLR:{str}

        Same as RoomCorrSet?

        Parameters
        ----------
        str : str
            Unknown

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
            await client.room_correction.room_corr_set_lr(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.room_corr_set_lr(str, request_options=request_options)
        return _response.data

    async def room_corr_set_mode(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

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
            await client.room_correction.room_corr_set_mode(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.room_corr_set_mode(str, request_options=request_options)
        return _response.data

    async def set_room_correction(
        self, str: str, time: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        time : str
            Format yyyy:MM:dd HH:mm

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
            await client.room_correction.set_room_correction(
                str="str",
                time="time",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_room_correction(str, time, request_options=request_options)
        return _response.data

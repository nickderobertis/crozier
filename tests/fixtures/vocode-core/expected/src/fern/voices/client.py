

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.voice_page import VoicePage
from ..types.voice_params_request import VoiceParamsRequest
from ..types.voice_response_model import VoiceResponseModel
from ..types.voice_update_params_request import VoiceUpdateParamsRequest
from .raw_client import AsyncRawVoicesClient, RawVoicesClient


OMIT = typing.cast(typing.Any, ...)


class VoicesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawVoicesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawVoicesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawVoicesClient
        """
        return self._raw_client

    def get_voice(self, *, id: str, request_options: typing.Optional[RequestOptions] = None) -> VoiceResponseModel:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VoiceResponseModel
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.voices.get_voice(
            id="id",
        )
        """
        _response = self._raw_client.get_voice(id=id, request_options=request_options)
        return _response.data

    def list_voices(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort_column: typing.Optional[str] = None,
        sort_desc: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VoicePage:
        """
        Parameters
        ----------
        page : typing.Optional[int]

        size : typing.Optional[int]

        sort_column : typing.Optional[str]

        sort_desc : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VoicePage
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.voices.list_voices()
        """
        _response = self._raw_client.list_voices(
            page=page, size=size, sort_column=sort_column, sort_desc=sort_desc, request_options=request_options
        )
        return _response.data

    def create_voice(
        self, *, request: VoiceParamsRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> VoiceResponseModel:
        """
        Parameters
        ----------
        request : VoiceParamsRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VoiceResponseModel
            Successful Response

        Examples
        --------
        from fern import FernApi, VoiceParamsRequest_VoiceAzure

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.voices.create_voice(
            request=VoiceParamsRequest_VoiceAzure(
                voice_name="voice_name",
            ),
        )
        """
        _response = self._raw_client.create_voice(request=request, request_options=request_options)
        return _response.data

    def update_voice(
        self, *, id: str, request: VoiceUpdateParamsRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> VoiceResponseModel:
        """
        Parameters
        ----------
        id : str

        request : VoiceUpdateParamsRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VoiceResponseModel
            Successful Response

        Examples
        --------
        from fern import FernApi, VoiceUpdateParamsRequest_VoiceAzure

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.voices.update_voice(
            id="id",
            request=VoiceUpdateParamsRequest_VoiceAzure(),
        )
        """
        _response = self._raw_client.update_voice(id=id, request=request, request_options=request_options)
        return _response.data


class AsyncVoicesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawVoicesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawVoicesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawVoicesClient
        """
        return self._raw_client

    async def get_voice(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> VoiceResponseModel:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VoiceResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.voices.get_voice(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_voice(id=id, request_options=request_options)
        return _response.data

    async def list_voices(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort_column: typing.Optional[str] = None,
        sort_desc: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VoicePage:
        """
        Parameters
        ----------
        page : typing.Optional[int]

        size : typing.Optional[int]

        sort_column : typing.Optional[str]

        sort_desc : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VoicePage
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.voices.list_voices()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_voices(
            page=page, size=size, sort_column=sort_column, sort_desc=sort_desc, request_options=request_options
        )
        return _response.data

    async def create_voice(
        self, *, request: VoiceParamsRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> VoiceResponseModel:
        """
        Parameters
        ----------
        request : VoiceParamsRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VoiceResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, VoiceParamsRequest_VoiceAzure

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.voices.create_voice(
                request=VoiceParamsRequest_VoiceAzure(
                    voice_name="voice_name",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_voice(request=request, request_options=request_options)
        return _response.data

    async def update_voice(
        self, *, id: str, request: VoiceUpdateParamsRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> VoiceResponseModel:
        """
        Parameters
        ----------
        id : str

        request : VoiceUpdateParamsRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VoiceResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, VoiceUpdateParamsRequest_VoiceAzure

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.voices.update_voice(
                id="id",
                request=VoiceUpdateParamsRequest_VoiceAzure(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_voice(id=id, request=request, request_options=request_options)
        return _response.data

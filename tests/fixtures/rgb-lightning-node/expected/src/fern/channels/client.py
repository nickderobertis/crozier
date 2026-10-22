

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.empty_response import EmptyResponse
from ..types.get_channel_id_response import GetChannelIdResponse
from ..types.list_channels_response import ListChannelsResponse
from ..types.open_channel_response import OpenChannelResponse
from .raw_client import AsyncRawChannelsClient, RawChannelsClient


OMIT = typing.cast(typing.Any, ...)


class ChannelsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawChannelsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawChannelsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawChannelsClient
        """
        return self._raw_client

    def close_a_channel(
        self, *, channel_id: str, peer_pubkey: str, force: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> EmptyResponse:
        """
        Close a LN channel cooperatively or forcibly

        Parameters
        ----------
        channel_id : str

        peer_pubkey : str

        force : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmptyResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.channels.close_a_channel(
            channel_id="8129afe1b1d7cf60d5e1bf4c04b09bec925ed4df5417ceee0484e24f816a105a",
            peer_pubkey="03b79a4bc1ec365524b4fab9a39eb133753646babb5a1da5c4bc94c53110b7795d",
            force=False,
        )
        """
        _response = self._raw_client.close_a_channel(
            channel_id=channel_id, peer_pubkey=peer_pubkey, force=force, request_options=request_options
        )
        return _response.data

    def get_a_channels_id(
        self, *, temporary_channel_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetChannelIdResponse:
        """
        Get a channel's ID from its former temporary channel ID

        Parameters
        ----------
        temporary_channel_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetChannelIdResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.channels.get_a_channels_id(
            temporary_channel_id="a8b60c8ce3067b5fc881d4831323e24751daec3b64353c8df3205ec5d838f1c5",
        )
        """
        _response = self._raw_client.get_a_channels_id(
            temporary_channel_id=temporary_channel_id, request_options=request_options
        )
        return _response.data

    def list_channels(self, *, request_options: typing.Optional[RequestOptions] = None) -> ListChannelsResponse:
        """
        List the node's LN channels

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListChannelsResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.channels.list_channels()
        """
        _response = self._raw_client.list_channels(request_options=request_options)
        return _response.data

    def open_a_channel(
        self,
        *,
        peer_pubkey_and_opt_addr: str,
        capacity_sat: int,
        push_msat: int,
        public: bool,
        with_anchors: bool,
        asset_amount: typing.Optional[int] = OMIT,
        asset_id: typing.Optional[str] = OMIT,
        push_asset_amount: typing.Optional[int] = OMIT,
        fee_base_msat: typing.Optional[int] = OMIT,
        fee_proportional_millionths: typing.Optional[int] = OMIT,
        temporary_channel_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OpenChannelResponse:
        """
        Open a new LN channel (RGB-enabled when both asset_id and asset_amount are specified). You can optionally provide a 32 bytes temporary channel ID as a hex-encoded string.

        Parameters
        ----------
        peer_pubkey_and_opt_addr : str

        capacity_sat : int

        push_msat : int

        public : bool

        with_anchors : bool

        asset_amount : typing.Optional[int]

        asset_id : typing.Optional[str]

        push_asset_amount : typing.Optional[int]

        fee_base_msat : typing.Optional[int]

        fee_proportional_millionths : typing.Optional[int]

        temporary_channel_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OpenChannelResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.channels.open_a_channel(
            peer_pubkey_and_opt_addr="03b79a4bc1ec365524b4fab9a39eb133753646babb5a1da5c4bc94c53110b7795d@localhost:9736",
            capacity_sat=30010,
            push_msat=1394000,
            public=True,
            with_anchors=True,
        )
        """
        _response = self._raw_client.open_a_channel(
            peer_pubkey_and_opt_addr=peer_pubkey_and_opt_addr,
            capacity_sat=capacity_sat,
            push_msat=push_msat,
            public=public,
            with_anchors=with_anchors,
            asset_amount=asset_amount,
            asset_id=asset_id,
            push_asset_amount=push_asset_amount,
            fee_base_msat=fee_base_msat,
            fee_proportional_millionths=fee_proportional_millionths,
            temporary_channel_id=temporary_channel_id,
            request_options=request_options,
        )
        return _response.data


class AsyncChannelsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawChannelsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawChannelsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawChannelsClient
        """
        return self._raw_client

    async def close_a_channel(
        self, *, channel_id: str, peer_pubkey: str, force: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> EmptyResponse:
        """
        Close a LN channel cooperatively or forcibly

        Parameters
        ----------
        channel_id : str

        peer_pubkey : str

        force : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmptyResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.channels.close_a_channel(
                channel_id="8129afe1b1d7cf60d5e1bf4c04b09bec925ed4df5417ceee0484e24f816a105a",
                peer_pubkey="03b79a4bc1ec365524b4fab9a39eb133753646babb5a1da5c4bc94c53110b7795d",
                force=False,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.close_a_channel(
            channel_id=channel_id, peer_pubkey=peer_pubkey, force=force, request_options=request_options
        )
        return _response.data

    async def get_a_channels_id(
        self, *, temporary_channel_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetChannelIdResponse:
        """
        Get a channel's ID from its former temporary channel ID

        Parameters
        ----------
        temporary_channel_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetChannelIdResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.channels.get_a_channels_id(
                temporary_channel_id="a8b60c8ce3067b5fc881d4831323e24751daec3b64353c8df3205ec5d838f1c5",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_a_channels_id(
            temporary_channel_id=temporary_channel_id, request_options=request_options
        )
        return _response.data

    async def list_channels(self, *, request_options: typing.Optional[RequestOptions] = None) -> ListChannelsResponse:
        """
        List the node's LN channels

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListChannelsResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.channels.list_channels()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_channels(request_options=request_options)
        return _response.data

    async def open_a_channel(
        self,
        *,
        peer_pubkey_and_opt_addr: str,
        capacity_sat: int,
        push_msat: int,
        public: bool,
        with_anchors: bool,
        asset_amount: typing.Optional[int] = OMIT,
        asset_id: typing.Optional[str] = OMIT,
        push_asset_amount: typing.Optional[int] = OMIT,
        fee_base_msat: typing.Optional[int] = OMIT,
        fee_proportional_millionths: typing.Optional[int] = OMIT,
        temporary_channel_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OpenChannelResponse:
        """
        Open a new LN channel (RGB-enabled when both asset_id and asset_amount are specified). You can optionally provide a 32 bytes temporary channel ID as a hex-encoded string.

        Parameters
        ----------
        peer_pubkey_and_opt_addr : str

        capacity_sat : int

        push_msat : int

        public : bool

        with_anchors : bool

        asset_amount : typing.Optional[int]

        asset_id : typing.Optional[str]

        push_asset_amount : typing.Optional[int]

        fee_base_msat : typing.Optional[int]

        fee_proportional_millionths : typing.Optional[int]

        temporary_channel_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OpenChannelResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.channels.open_a_channel(
                peer_pubkey_and_opt_addr="03b79a4bc1ec365524b4fab9a39eb133753646babb5a1da5c4bc94c53110b7795d@localhost:9736",
                capacity_sat=30010,
                push_msat=1394000,
                public=True,
                with_anchors=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.open_a_channel(
            peer_pubkey_and_opt_addr=peer_pubkey_and_opt_addr,
            capacity_sat=capacity_sat,
            push_msat=push_msat,
            public=public,
            with_anchors=with_anchors,
            asset_amount=asset_amount,
            asset_id=asset_id,
            push_asset_amount=push_asset_amount,
            fee_base_msat=fee_base_msat,
            fee_proportional_millionths=fee_proportional_millionths,
            temporary_channel_id=temporary_channel_id,
            request_options=request_options,
        )
        return _response.data

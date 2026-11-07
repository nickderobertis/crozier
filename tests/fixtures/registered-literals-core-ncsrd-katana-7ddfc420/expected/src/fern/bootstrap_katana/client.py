

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.ems import Ems
from ..types.net_func import NetFunc
from ..types.nfvo import Nfvo
from ..types.vim import Vim
from ..types.wim import Wim
from .raw_client import AsyncRawBootstrapKatanaClient, RawBootstrapKatanaClient


OMIT = typing.cast(typing.Any, ...)


class BootstrapKatanaClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBootstrapKatanaClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBootstrapKatanaClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBootstrapKatanaClient
        """
        return self._raw_client

    def configure_katana_using_one_json_file_note_that_the_locations_must_be_already_added(
        self,
        *,
        vim: typing.Optional[typing.Sequence[Vim]] = OMIT,
        nfvo: typing.Optional[typing.Sequence[Nfvo]] = OMIT,
        wim: typing.Optional[typing.Sequence[Wim]] = OMIT,
        ems: typing.Optional[typing.Sequence[Ems]] = OMIT,
        function: typing.Optional[typing.Sequence[NetFunc]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        vim : typing.Optional[typing.Sequence[Vim]]
            A list with the VIM components to be added

        nfvo : typing.Optional[typing.Sequence[Nfvo]]
            A list with the NFVO components to be added

        wim : typing.Optional[typing.Sequence[Wim]]
            A list with the WIM components to be added

        ems : typing.Optional[typing.Sequence[Ems]]
            A list with the EMS components to be added

        function : typing.Optional[typing.Sequence[NetFunc]]
            A list with the Network Functions to be added

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.bootstrap_katana.configure_katana_using_one_json_file_note_that_the_locations_must_be_already_added()
        """
        _response = self._raw_client.configure_katana_using_one_json_file_note_that_the_locations_must_be_already_added(
            vim=vim, nfvo=nfvo, wim=wim, ems=ems, function=function, request_options=request_options
        )
        return _response.data


class AsyncBootstrapKatanaClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBootstrapKatanaClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBootstrapKatanaClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBootstrapKatanaClient
        """
        return self._raw_client

    async def configure_katana_using_one_json_file_note_that_the_locations_must_be_already_added(
        self,
        *,
        vim: typing.Optional[typing.Sequence[Vim]] = OMIT,
        nfvo: typing.Optional[typing.Sequence[Nfvo]] = OMIT,
        wim: typing.Optional[typing.Sequence[Wim]] = OMIT,
        ems: typing.Optional[typing.Sequence[Ems]] = OMIT,
        function: typing.Optional[typing.Sequence[NetFunc]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        vim : typing.Optional[typing.Sequence[Vim]]
            A list with the VIM components to be added

        nfvo : typing.Optional[typing.Sequence[Nfvo]]
            A list with the NFVO components to be added

        wim : typing.Optional[typing.Sequence[Wim]]
            A list with the WIM components to be added

        ems : typing.Optional[typing.Sequence[Ems]]
            A list with the EMS components to be added

        function : typing.Optional[typing.Sequence[NetFunc]]
            A list with the Network Functions to be added

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
            await client.bootstrap_katana.configure_katana_using_one_json_file_note_that_the_locations_must_be_already_added()


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.configure_katana_using_one_json_file_note_that_the_locations_must_be_already_added(
                vim=vim, nfvo=nfvo, wim=wim, ems=ems, function=function, request_options=request_options
            )
        )
        return _response.data

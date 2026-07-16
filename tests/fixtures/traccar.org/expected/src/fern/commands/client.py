

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.command import Command
from ..types.command_attributes import CommandAttributes
from ..types.command_type import CommandType
from .raw_client import AsyncRawCommandsClient, RawCommandsClient


OMIT = typing.cast(typing.Any, ...)


class CommandsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCommandsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCommandsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCommandsClient
        """
        return self._raw_client

    def fetch_a_list_of_saved_commands(
        self,
        *,
        all_: typing.Optional[bool] = None,
        user_id: typing.Optional[int] = None,
        device_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        refresh: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Command]:
        """
        Without params, it returns a list of Saved Commands the user has access to

        Parameters
        ----------
        all_ : typing.Optional[bool]
            Can only be used by admins or managers to fetch all entities

        user_id : typing.Optional[int]
            Standard users can use this only with their own _userId_

        device_id : typing.Optional[int]
            Standard users can use this only with _deviceId_s, they have access to

        group_id : typing.Optional[int]
            Standard users can use this only with _groupId_s, they have access to

        refresh : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Command]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.commands.fetch_a_list_of_saved_commands()
        """
        _response = self._raw_client.fetch_a_list_of_saved_commands(
            all_=all_,
            user_id=user_id,
            device_id=device_id,
            group_id=group_id,
            refresh=refresh,
            request_options=request_options,
        )
        return _response.data

    def create_a_saved_command(
        self,
        *,
        attributes: typing.Optional[CommandAttributes] = OMIT,
        description: typing.Optional[str] = OMIT,
        device_id: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Command:
        """
        Parameters
        ----------
        attributes : typing.Optional[CommandAttributes]

        description : typing.Optional[str]

        device_id : typing.Optional[int]

        id : typing.Optional[int]

        type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Command
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.commands.create_a_saved_command()
        """
        _response = self._raw_client.create_a_saved_command(
            attributes=attributes,
            description=description,
            device_id=device_id,
            id=id,
            type=type,
            request_options=request_options,
        )
        return _response.data

    def fetch_a_list_of_saved_commands_supported_by_device_at_the_moment(
        self, *, device_id: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Command]:
        """
        Return a list of saved commands linked to Device and its groups, filtered by current Device protocol support

        Parameters
        ----------
        device_id : typing.Optional[int]
            Standard users can use this only with _deviceId_s, they have access to

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Command]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.commands.fetch_a_list_of_saved_commands_supported_by_device_at_the_moment()
        """
        _response = self._raw_client.fetch_a_list_of_saved_commands_supported_by_device_at_the_moment(
            device_id=device_id, request_options=request_options
        )
        return _response.data

    def dispatch_commands_to_device(
        self,
        *,
        attributes: typing.Optional[CommandAttributes] = OMIT,
        description: typing.Optional[str] = OMIT,
        device_id: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Command:
        """
        Dispatch a new command or Saved Command if _body.id_ set

        Parameters
        ----------
        attributes : typing.Optional[CommandAttributes]

        description : typing.Optional[str]

        device_id : typing.Optional[int]

        id : typing.Optional[int]

        type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Command
            Command sent

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.commands.dispatch_commands_to_device()
        """
        _response = self._raw_client.dispatch_commands_to_device(
            attributes=attributes,
            description=description,
            device_id=device_id,
            id=id,
            type=type,
            request_options=request_options,
        )
        return _response.data

    def fetch_a_list_of_available_commands_for_the_device_or_all_possible_commands_if_device_ommited(
        self,
        *,
        device_id: typing.Optional[int] = None,
        protocol: typing.Optional[str] = None,
        text_channel: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[CommandType]:
        """
        Parameters
        ----------
        device_id : typing.Optional[int]
            Internal device identifier. Only works if device has already reported some locations

        protocol : typing.Optional[str]
            Protocol name. Can be used instead of device id

        text_channel : typing.Optional[bool]
            When `true` return SMS commands. If not specified or `false` return data commands

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[CommandType]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.commands.fetch_a_list_of_available_commands_for_the_device_or_all_possible_commands_if_device_ommited()
        """
        _response = self._raw_client.fetch_a_list_of_available_commands_for_the_device_or_all_possible_commands_if_device_ommited(
            device_id=device_id, protocol=protocol, text_channel=text_channel, request_options=request_options
        )
        return _response.data

    def update_a_saved_command(
        self,
        id_: int,
        *,
        attributes: typing.Optional[CommandAttributes] = OMIT,
        description: typing.Optional[str] = OMIT,
        device_id: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Command:
        """
        Parameters
        ----------
        id_ : int

        attributes : typing.Optional[CommandAttributes]

        description : typing.Optional[str]

        device_id : typing.Optional[int]

        id : typing.Optional[int]

        type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Command
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.commands.update_a_saved_command(
            id_=1,
        )
        """
        _response = self._raw_client.update_a_saved_command(
            id_,
            attributes=attributes,
            description=description,
            device_id=device_id,
            id=id,
            type=type,
            request_options=request_options,
        )
        return _response.data

    def delete_a_saved_command(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.commands.delete_a_saved_command(
            id=1,
        )
        """
        _response = self._raw_client.delete_a_saved_command(id, request_options=request_options)
        return _response.data


class AsyncCommandsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCommandsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCommandsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCommandsClient
        """
        return self._raw_client

    async def fetch_a_list_of_saved_commands(
        self,
        *,
        all_: typing.Optional[bool] = None,
        user_id: typing.Optional[int] = None,
        device_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        refresh: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Command]:
        """
        Without params, it returns a list of Saved Commands the user has access to

        Parameters
        ----------
        all_ : typing.Optional[bool]
            Can only be used by admins or managers to fetch all entities

        user_id : typing.Optional[int]
            Standard users can use this only with their own _userId_

        device_id : typing.Optional[int]
            Standard users can use this only with _deviceId_s, they have access to

        group_id : typing.Optional[int]
            Standard users can use this only with _groupId_s, they have access to

        refresh : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Command]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.commands.fetch_a_list_of_saved_commands()


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_a_list_of_saved_commands(
            all_=all_,
            user_id=user_id,
            device_id=device_id,
            group_id=group_id,
            refresh=refresh,
            request_options=request_options,
        )
        return _response.data

    async def create_a_saved_command(
        self,
        *,
        attributes: typing.Optional[CommandAttributes] = OMIT,
        description: typing.Optional[str] = OMIT,
        device_id: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Command:
        """
        Parameters
        ----------
        attributes : typing.Optional[CommandAttributes]

        description : typing.Optional[str]

        device_id : typing.Optional[int]

        id : typing.Optional[int]

        type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Command
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.commands.create_a_saved_command()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_a_saved_command(
            attributes=attributes,
            description=description,
            device_id=device_id,
            id=id,
            type=type,
            request_options=request_options,
        )
        return _response.data

    async def fetch_a_list_of_saved_commands_supported_by_device_at_the_moment(
        self, *, device_id: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Command]:
        """
        Return a list of saved commands linked to Device and its groups, filtered by current Device protocol support

        Parameters
        ----------
        device_id : typing.Optional[int]
            Standard users can use this only with _deviceId_s, they have access to

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Command]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.commands.fetch_a_list_of_saved_commands_supported_by_device_at_the_moment()


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_a_list_of_saved_commands_supported_by_device_at_the_moment(
            device_id=device_id, request_options=request_options
        )
        return _response.data

    async def dispatch_commands_to_device(
        self,
        *,
        attributes: typing.Optional[CommandAttributes] = OMIT,
        description: typing.Optional[str] = OMIT,
        device_id: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Command:
        """
        Dispatch a new command or Saved Command if _body.id_ set

        Parameters
        ----------
        attributes : typing.Optional[CommandAttributes]

        description : typing.Optional[str]

        device_id : typing.Optional[int]

        id : typing.Optional[int]

        type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Command
            Command sent

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.commands.dispatch_commands_to_device()


        asyncio.run(main())
        """
        _response = await self._raw_client.dispatch_commands_to_device(
            attributes=attributes,
            description=description,
            device_id=device_id,
            id=id,
            type=type,
            request_options=request_options,
        )
        return _response.data

    async def fetch_a_list_of_available_commands_for_the_device_or_all_possible_commands_if_device_ommited(
        self,
        *,
        device_id: typing.Optional[int] = None,
        protocol: typing.Optional[str] = None,
        text_channel: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[CommandType]:
        """
        Parameters
        ----------
        device_id : typing.Optional[int]
            Internal device identifier. Only works if device has already reported some locations

        protocol : typing.Optional[str]
            Protocol name. Can be used instead of device id

        text_channel : typing.Optional[bool]
            When `true` return SMS commands. If not specified or `false` return data commands

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[CommandType]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.commands.fetch_a_list_of_available_commands_for_the_device_or_all_possible_commands_if_device_ommited()


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_a_list_of_available_commands_for_the_device_or_all_possible_commands_if_device_ommited(
            device_id=device_id, protocol=protocol, text_channel=text_channel, request_options=request_options
        )
        return _response.data

    async def update_a_saved_command(
        self,
        id_: int,
        *,
        attributes: typing.Optional[CommandAttributes] = OMIT,
        description: typing.Optional[str] = OMIT,
        device_id: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Command:
        """
        Parameters
        ----------
        id_ : int

        attributes : typing.Optional[CommandAttributes]

        description : typing.Optional[str]

        device_id : typing.Optional[int]

        id : typing.Optional[int]

        type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Command
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.commands.update_a_saved_command(
                id_=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_a_saved_command(
            id_,
            attributes=attributes,
            description=description,
            device_id=device_id,
            id=id,
            type=type,
            request_options=request_options,
        )
        return _response.data

    async def delete_a_saved_command(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : int

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
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.commands.delete_a_saved_command(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_a_saved_command(id, request_options=request_options)
        return _response.data

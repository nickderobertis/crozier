

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.command_inputs import CommandInputs
from ..types.command_response import CommandResponse
from ..types.command_type import CommandType
from ..types.commands_list_response import CommandsListResponse
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

    def get_command_by_id(
        self, command_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CommandResponse:
        """
        Get a command by ID

        Parameters
        ----------
        command_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CommandResponse
            The command

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.commands.get_command_by_id(
            command_id=1,
        )
        """
        _response = self._raw_client.get_command_by_id(command_id, request_options=request_options)
        return _response.data

    def delete_command_by_id(self, command_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a command by ID

        Parameters
        ----------
        command_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.commands.delete_command_by_id(
            command_id=1,
        )
        """
        _response = self._raw_client.delete_command_by_id(command_id, request_options=request_options)
        return _response.data

    def list_commands(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sorts: typing.Optional[str] = None,
        statuses: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CommandsListResponse:
        """
        List all commands

        Parameters
        ----------
        page : typing.Optional[int]
            The page number

        page_size : typing.Optional[int]
            The number of items per page

        sorts : typing.Optional[str]
            Sort the commands by the given field. Use `-` to sort in descending order. Use `,` to sort by multiple fields. Example: `-created_at,status` Allowed fields:
              - type
              - status
              - source
              - created_at
              - updated_at
              - completed_at

        statuses : typing.Optional[str]
            Filter the commands by the given statuses. Use `,` to filter by multiple statuses. Example: `QUEUED,PROCESSING` Allowed values:
              - QUEUED
              - PROCESSING
              - SUCCEEDED
              - FAILED
              - CANCELED

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CommandsListResponse
            A list of commands

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.commands.list_commands()
        """
        _response = self._raw_client.list_commands(
            page=page, page_size=page_size, sorts=sorts, statuses=statuses, request_options=request_options
        )
        return _response.data

    def create_command(
        self, *, type: CommandType, inputs: CommandInputs, request_options: typing.Optional[RequestOptions] = None
    ) -> CommandResponse:
        """
        Create a command

        Parameters
        ----------
        type : CommandType
            The type of command

        inputs : CommandInputs
            The inputs of the command

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CommandResponse
            The created command

        Examples
        --------
        from fern import CommandType, FernApi

        client = FernApi()
        client.commands.create_command(
            type=CommandType.STOP_MOVEMENT,
            inputs={"key": "value"},
        )
        """
        _response = self._raw_client.create_command(type=type, inputs=inputs, request_options=request_options)
        return _response.data

    def get_current_processing_command(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CommandResponse:
        """
        Get the command that is currently being processed

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CommandResponse
            The command

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.commands.get_current_processing_command()
        """
        _response = self._raw_client.get_current_processing_command(request_options=request_options)
        return _response.data

    def cancel_current_processing_command(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Cancel the current processing command

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
        client.commands.cancel_current_processing_command()
        """
        _response = self._raw_client.cancel_current_processing_command(request_options=request_options)
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

    async def get_command_by_id(
        self, command_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CommandResponse:
        """
        Get a command by ID

        Parameters
        ----------
        command_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CommandResponse
            The command

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.commands.get_command_by_id(
                command_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_command_by_id(command_id, request_options=request_options)
        return _response.data

    async def delete_command_by_id(
        self, command_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a command by ID

        Parameters
        ----------
        command_id : int

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
            await client.commands.delete_command_by_id(
                command_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_command_by_id(command_id, request_options=request_options)
        return _response.data

    async def list_commands(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sorts: typing.Optional[str] = None,
        statuses: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CommandsListResponse:
        """
        List all commands

        Parameters
        ----------
        page : typing.Optional[int]
            The page number

        page_size : typing.Optional[int]
            The number of items per page

        sorts : typing.Optional[str]
            Sort the commands by the given field. Use `-` to sort in descending order. Use `,` to sort by multiple fields. Example: `-created_at,status` Allowed fields:
              - type
              - status
              - source
              - created_at
              - updated_at
              - completed_at

        statuses : typing.Optional[str]
            Filter the commands by the given statuses. Use `,` to filter by multiple statuses. Example: `QUEUED,PROCESSING` Allowed values:
              - QUEUED
              - PROCESSING
              - SUCCEEDED
              - FAILED
              - CANCELED

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CommandsListResponse
            A list of commands

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.commands.list_commands()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_commands(
            page=page, page_size=page_size, sorts=sorts, statuses=statuses, request_options=request_options
        )
        return _response.data

    async def create_command(
        self, *, type: CommandType, inputs: CommandInputs, request_options: typing.Optional[RequestOptions] = None
    ) -> CommandResponse:
        """
        Create a command

        Parameters
        ----------
        type : CommandType
            The type of command

        inputs : CommandInputs
            The inputs of the command

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CommandResponse
            The created command

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, CommandType

        client = AsyncFernApi()


        async def main() -> None:
            await client.commands.create_command(
                type=CommandType.STOP_MOVEMENT,
                inputs={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_command(type=type, inputs=inputs, request_options=request_options)
        return _response.data

    async def get_current_processing_command(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CommandResponse:
        """
        Get the command that is currently being processed

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CommandResponse
            The command

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.commands.get_current_processing_command()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_current_processing_command(request_options=request_options)
        return _response.data

    async def cancel_current_processing_command(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Cancel the current processing command

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
            await client.commands.cancel_current_processing_command()


        asyncio.run(main())
        """
        _response = await self._raw_client.cancel_current_processing_command(request_options=request_options)
        return _response.data

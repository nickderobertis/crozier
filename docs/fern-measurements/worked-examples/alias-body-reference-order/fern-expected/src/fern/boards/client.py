

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawBoardsClient, RawBoardsClient


OMIT = typing.cast(typing.Any, ...)


class BoardsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBoardsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBoardsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBoardsClient
        """
        return self._raw_client

    def update_board(
        self,
        board_id: str,
        *,
        visibility: typing.Optional[str] = None,
        crew_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        title: typing.Optional[str] = OMIT,
        overwrite: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        board_id : str

        visibility : typing.Optional[str]

        crew_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        title : typing.Optional[str]

        overwrite : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            The board.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.boards.update_board(
            board_id="boardId",
        )
        """
        _response = self._raw_client.update_board(
            board_id,
            visibility=visibility,
            crew_ids=crew_ids,
            title=title,
            overwrite=overwrite,
            request_options=request_options,
        )
        return _response.data

    def create_board(
        self,
        *,
        visibility: typing.Optional[str] = None,
        title: typing.Optional[str] = OMIT,
        overwrite: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        visibility : typing.Optional[str]

        title : typing.Optional[str]

        overwrite : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            The board.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.boards.create_board()
        """
        _response = self._raw_client.create_board(
            visibility=visibility, title=title, overwrite=overwrite, request_options=request_options
        )
        return _response.data

    def save_board(
        self,
        *,
        title: typing.Optional[str] = OMIT,
        overwrite: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        title : typing.Optional[str]

        overwrite : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Saved

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.boards.save_board()
        """
        _response = self._raw_client.save_board(title=title, overwrite=overwrite, request_options=request_options)
        return _response.data


class AsyncBoardsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBoardsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBoardsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBoardsClient
        """
        return self._raw_client

    async def update_board(
        self,
        board_id: str,
        *,
        visibility: typing.Optional[str] = None,
        crew_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        title: typing.Optional[str] = OMIT,
        overwrite: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        board_id : str

        visibility : typing.Optional[str]

        crew_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        title : typing.Optional[str]

        overwrite : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            The board.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.boards.update_board(
                board_id="boardId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_board(
            board_id,
            visibility=visibility,
            crew_ids=crew_ids,
            title=title,
            overwrite=overwrite,
            request_options=request_options,
        )
        return _response.data

    async def create_board(
        self,
        *,
        visibility: typing.Optional[str] = None,
        title: typing.Optional[str] = OMIT,
        overwrite: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        visibility : typing.Optional[str]

        title : typing.Optional[str]

        overwrite : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            The board.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.boards.create_board()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_board(
            visibility=visibility, title=title, overwrite=overwrite, request_options=request_options
        )
        return _response.data

    async def save_board(
        self,
        *,
        title: typing.Optional[str] = OMIT,
        overwrite: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        title : typing.Optional[str]

        overwrite : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Saved

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.boards.save_board()


        asyncio.run(main())
        """
        _response = await self._raw_client.save_board(title=title, overwrite=overwrite, request_options=request_options)
        return _response.data



import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.paginated_difficulty_level_response import PaginatedDifficultyLevelResponse
from .raw_client import AsyncRawDifficultylevelClient, RawDifficultylevelClient
from .types.difficulty_level import DifficultyLevel


OMIT = typing.cast(typing.Any, ...)


class DifficultylevelClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDifficultylevelClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDifficultylevelClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDifficultylevelClient
        """
        return self._raw_client

    def get_all_dificultylevels(
        self,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedDifficultyLevelResponse:
        """
        Retrieve all difficultylevels known to the API in a paginated format

        Parameters
        ----------
        page : typing.Optional[int]
            Page number (1-indexed)

        limit : typing.Optional[int]
            Number of items per page (max 100)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedDifficultyLevelResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.difficultylevel.get_all_dificultylevels()
        """
        _response = self._raw_client.get_all_dificultylevels(page=page, limit=limit, request_options=request_options)
        return _response.data

    def create_difficultylevel(
        self,
        *,
        id: typing.Optional[str] = OMIT,
        level: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DifficultyLevel:
        """
        Create a difficultylevel

        Parameters
        ----------
        id : typing.Optional[str]
            ID of a Dificulty Level

        level : typing.Optional[int]
            name of a Dificulty Level

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DifficultyLevel
            Created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.difficultylevel.create_difficultylevel(
            level=1,
        )
        """
        _response = self._raw_client.create_difficultylevel(id=id, level=level, request_options=request_options)
        return _response.data

    def get_single_difficultylevel(
        self, difficulty_level_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DifficultyLevel:
        """
        Get a single difficultylevel definition

        Parameters
        ----------
        difficulty_level_id : str
            UUID of a difficulty level

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DifficultyLevel
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.difficultylevel.get_single_difficultylevel(
            difficulty_level_id="DifficultyLevelID",
        )
        """
        _response = self._raw_client.get_single_difficultylevel(difficulty_level_id, request_options=request_options)
        return _response.data

    def update_difficultylevel(
        self,
        difficulty_level_id: str,
        *,
        id: typing.Optional[str] = OMIT,
        level: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DifficultyLevel:
        """
        Update a difficultylevel

        Parameters
        ----------
        difficulty_level_id : str
            UUID of a difficulty level

        id : typing.Optional[str]
            ID of a Dificulty Level

        level : typing.Optional[int]
            name of a Dificulty Level

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DifficultyLevel
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.difficultylevel.update_difficultylevel(
            difficulty_level_id="DifficultyLevelID",
            level=1,
        )
        """
        _response = self._raw_client.update_difficultylevel(
            difficulty_level_id, id=id, level=level, request_options=request_options
        )
        return _response.data

    def delete_difficultylevel(
        self, difficulty_level_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a difficultylevel

        Parameters
        ----------
        difficulty_level_id : str
            UUID of a difficulty level

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.difficultylevel.delete_difficultylevel(
            difficulty_level_id="DifficultyLevelID",
        )
        """
        _response = self._raw_client.delete_difficultylevel(difficulty_level_id, request_options=request_options)
        return _response.data


class AsyncDifficultylevelClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDifficultylevelClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDifficultylevelClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDifficultylevelClient
        """
        return self._raw_client

    async def get_all_dificultylevels(
        self,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedDifficultyLevelResponse:
        """
        Retrieve all difficultylevels known to the API in a paginated format

        Parameters
        ----------
        page : typing.Optional[int]
            Page number (1-indexed)

        limit : typing.Optional[int]
            Number of items per page (max 100)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedDifficultyLevelResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.difficultylevel.get_all_dificultylevels()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_all_dificultylevels(
            page=page, limit=limit, request_options=request_options
        )
        return _response.data

    async def create_difficultylevel(
        self,
        *,
        id: typing.Optional[str] = OMIT,
        level: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DifficultyLevel:
        """
        Create a difficultylevel

        Parameters
        ----------
        id : typing.Optional[str]
            ID of a Dificulty Level

        level : typing.Optional[int]
            name of a Dificulty Level

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DifficultyLevel
            Created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.difficultylevel.create_difficultylevel(
                level=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_difficultylevel(id=id, level=level, request_options=request_options)
        return _response.data

    async def get_single_difficultylevel(
        self, difficulty_level_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DifficultyLevel:
        """
        Get a single difficultylevel definition

        Parameters
        ----------
        difficulty_level_id : str
            UUID of a difficulty level

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DifficultyLevel
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.difficultylevel.get_single_difficultylevel(
                difficulty_level_id="DifficultyLevelID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_single_difficultylevel(
            difficulty_level_id, request_options=request_options
        )
        return _response.data

    async def update_difficultylevel(
        self,
        difficulty_level_id: str,
        *,
        id: typing.Optional[str] = OMIT,
        level: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DifficultyLevel:
        """
        Update a difficultylevel

        Parameters
        ----------
        difficulty_level_id : str
            UUID of a difficulty level

        id : typing.Optional[str]
            ID of a Dificulty Level

        level : typing.Optional[int]
            name of a Dificulty Level

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DifficultyLevel
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.difficultylevel.update_difficultylevel(
                difficulty_level_id="DifficultyLevelID",
                level=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_difficultylevel(
            difficulty_level_id, id=id, level=level, request_options=request_options
        )
        return _response.data

    async def delete_difficultylevel(
        self, difficulty_level_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a difficultylevel

        Parameters
        ----------
        difficulty_level_id : str
            UUID of a difficulty level

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.difficultylevel.delete_difficultylevel(
                difficulty_level_id="DifficultyLevelID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_difficultylevel(difficulty_level_id, request_options=request_options)
        return _response.data

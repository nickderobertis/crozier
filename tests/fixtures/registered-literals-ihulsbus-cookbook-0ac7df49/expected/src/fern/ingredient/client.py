

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.paginated_ingredient_response import PaginatedIngredientResponse
from .raw_client import AsyncRawIngredientClient, RawIngredientClient
from .types.ingredient import Ingredient


OMIT = typing.cast(typing.Any, ...)


class IngredientClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawIngredientClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawIngredientClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawIngredientClient
        """
        return self._raw_client

    def get_all_ingredient(
        self,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedIngredientResponse:
        """
        Get all ingredients known to the API in a paginated format

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
        PaginatedIngredientResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.ingredient.get_all_ingredient()
        """
        _response = self._raw_client.get_all_ingredient(page=page, limit=limit, request_options=request_options)
        return _response.data

    def create_ingredient(
        self,
        *,
        id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ingredient:
        """
        Create an ingredient

        Parameters
        ----------
        id : typing.Optional[str]
            ID of the ingredient

        name : typing.Optional[str]
            Name of the ingredient

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ingredient
            Created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.ingredient.create_ingredient(
            name="Asparagus",
        )
        """
        _response = self._raw_client.create_ingredient(id=id, name=name, request_options=request_options)
        return _response.data

    def get_ingredient(
        self, ingredient_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ingredient:
        """
        Get a single ingredient

        Parameters
        ----------
        ingredient_id : str
            UUID of an Ingredient

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ingredient
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.ingredient.get_ingredient(
            ingredient_id="IngredientID",
        )
        """
        _response = self._raw_client.get_ingredient(ingredient_id, request_options=request_options)
        return _response.data

    def update_ingredient(
        self,
        ingredient_id: str,
        *,
        id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ingredient:
        """
        Update an ingredient

        Parameters
        ----------
        ingredient_id : str
            UUID of an Ingredient

        id : typing.Optional[str]
            ID of the ingredient

        name : typing.Optional[str]
            Name of the ingredient

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ingredient
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.ingredient.update_ingredient(
            ingredient_id="IngredientID",
            name="Asparagus",
        )
        """
        _response = self._raw_client.update_ingredient(ingredient_id, id=id, name=name, request_options=request_options)
        return _response.data

    def delete_ingredient(self, ingredient_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete an ingredient

        Parameters
        ----------
        ingredient_id : str
            UUID of an Ingredient

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
        client.ingredient.delete_ingredient(
            ingredient_id="IngredientID",
        )
        """
        _response = self._raw_client.delete_ingredient(ingredient_id, request_options=request_options)
        return _response.data


class AsyncIngredientClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawIngredientClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawIngredientClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawIngredientClient
        """
        return self._raw_client

    async def get_all_ingredient(
        self,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedIngredientResponse:
        """
        Get all ingredients known to the API in a paginated format

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
        PaginatedIngredientResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ingredient.get_all_ingredient()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_all_ingredient(page=page, limit=limit, request_options=request_options)
        return _response.data

    async def create_ingredient(
        self,
        *,
        id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ingredient:
        """
        Create an ingredient

        Parameters
        ----------
        id : typing.Optional[str]
            ID of the ingredient

        name : typing.Optional[str]
            Name of the ingredient

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ingredient
            Created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ingredient.create_ingredient(
                name="Asparagus",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_ingredient(id=id, name=name, request_options=request_options)
        return _response.data

    async def get_ingredient(
        self, ingredient_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ingredient:
        """
        Get a single ingredient

        Parameters
        ----------
        ingredient_id : str
            UUID of an Ingredient

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ingredient
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ingredient.get_ingredient(
                ingredient_id="IngredientID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_ingredient(ingredient_id, request_options=request_options)
        return _response.data

    async def update_ingredient(
        self,
        ingredient_id: str,
        *,
        id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ingredient:
        """
        Update an ingredient

        Parameters
        ----------
        ingredient_id : str
            UUID of an Ingredient

        id : typing.Optional[str]
            ID of the ingredient

        name : typing.Optional[str]
            Name of the ingredient

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ingredient
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ingredient.update_ingredient(
                ingredient_id="IngredientID",
                name="Asparagus",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_ingredient(
            ingredient_id, id=id, name=name, request_options=request_options
        )
        return _response.data

    async def delete_ingredient(
        self, ingredient_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete an ingredient

        Parameters
        ----------
        ingredient_id : str
            UUID of an Ingredient

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
            await client.ingredient.delete_ingredient(
                ingredient_id="IngredientID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_ingredient(ingredient_id, request_options=request_options)
        return _response.data

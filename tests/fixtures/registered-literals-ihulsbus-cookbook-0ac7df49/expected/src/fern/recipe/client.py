

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.paginated_recipe_response import PaginatedRecipeResponse
from .raw_client import AsyncRawRecipeClient, RawRecipeClient
from .types.recipe import Recipe


OMIT = typing.cast(typing.Any, ...)


class RecipeClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRecipeClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRecipeClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRecipeClient
        """
        return self._raw_client

    def get_all_recipes(
        self,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedRecipeResponse:
        """
        Retrieves recipes from the API in a paginated format

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
        PaginatedRecipeResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.recipe.get_all_recipes()
        """
        _response = self._raw_client.get_all_recipes(page=page, limit=limit, request_options=request_options)
        return _response.data

    def create_recipe(
        self,
        *,
        name: str,
        description: str,
        serving_count: int,
        id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Recipe:
        """
        Create a recipe

        Parameters
        ----------
        name : str
            Name of a recipe

        description : str
            Short description of the recipe

        serving_count : int
            amount of servings a recipe makes

        id : typing.Optional[str]
            ID of a recipe

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Recipe
            Created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.recipe.create_recipe(
            name="Test",
            description="test",
            serving_count=1,
        )
        """
        _response = self._raw_client.create_recipe(
            name=name, description=description, serving_count=serving_count, id=id, request_options=request_options
        )
        return _response.data

    def get_recipe(self, recipe_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Recipe:
        """
        Get a single recipe based on the provided recipeID

        Parameters
        ----------
        recipe_id : str
            UUID of a recipe

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Recipe
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.recipe.get_recipe(
            recipe_id="RecipeID",
        )
        """
        _response = self._raw_client.get_recipe(recipe_id, request_options=request_options)
        return _response.data

    def update_recipe(
        self,
        recipe_id: str,
        *,
        name: str,
        description: str,
        serving_count: int,
        id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Recipe:
        """
        Update a recipe

        Parameters
        ----------
        recipe_id : str
            UUID of a recipe

        name : str
            Name of a recipe

        description : str
            Short description of the recipe

        serving_count : int
            amount of servings a recipe makes

        id : typing.Optional[str]
            ID of a recipe

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Recipe
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.recipe.update_recipe(
            recipe_id="RecipeID",
            name="Test",
            description="test",
            serving_count=1,
        )
        """
        _response = self._raw_client.update_recipe(
            recipe_id,
            name=name,
            description=description,
            serving_count=serving_count,
            id=id,
            request_options=request_options,
        )
        return _response.data

    def delete_recipe(self, recipe_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a recipe

        Parameters
        ----------
        recipe_id : str
            UUID of a recipe

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
        client.recipe.delete_recipe(
            recipe_id="RecipeID",
        )
        """
        _response = self._raw_client.delete_recipe(recipe_id, request_options=request_options)
        return _response.data


class AsyncRecipeClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRecipeClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRecipeClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRecipeClient
        """
        return self._raw_client

    async def get_all_recipes(
        self,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedRecipeResponse:
        """
        Retrieves recipes from the API in a paginated format

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
        PaginatedRecipeResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.recipe.get_all_recipes()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_all_recipes(page=page, limit=limit, request_options=request_options)
        return _response.data

    async def create_recipe(
        self,
        *,
        name: str,
        description: str,
        serving_count: int,
        id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Recipe:
        """
        Create a recipe

        Parameters
        ----------
        name : str
            Name of a recipe

        description : str
            Short description of the recipe

        serving_count : int
            amount of servings a recipe makes

        id : typing.Optional[str]
            ID of a recipe

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Recipe
            Created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.recipe.create_recipe(
                name="Test",
                description="test",
                serving_count=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_recipe(
            name=name, description=description, serving_count=serving_count, id=id, request_options=request_options
        )
        return _response.data

    async def get_recipe(self, recipe_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Recipe:
        """
        Get a single recipe based on the provided recipeID

        Parameters
        ----------
        recipe_id : str
            UUID of a recipe

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Recipe
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.recipe.get_recipe(
                recipe_id="RecipeID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_recipe(recipe_id, request_options=request_options)
        return _response.data

    async def update_recipe(
        self,
        recipe_id: str,
        *,
        name: str,
        description: str,
        serving_count: int,
        id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Recipe:
        """
        Update a recipe

        Parameters
        ----------
        recipe_id : str
            UUID of a recipe

        name : str
            Name of a recipe

        description : str
            Short description of the recipe

        serving_count : int
            amount of servings a recipe makes

        id : typing.Optional[str]
            ID of a recipe

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Recipe
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.recipe.update_recipe(
                recipe_id="RecipeID",
                name="Test",
                description="test",
                serving_count=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_recipe(
            recipe_id,
            name=name,
            description=description,
            serving_count=serving_count,
            id=id,
            request_options=request_options,
        )
        return _response.data

    async def delete_recipe(self, recipe_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a recipe

        Parameters
        ----------
        recipe_id : str
            UUID of a recipe

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
            await client.recipe.delete_recipe(
                recipe_id="RecipeID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_recipe(recipe_id, request_options=request_options)
        return _response.data

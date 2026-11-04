

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAmountClient, RawAmountClient
from .types.ingredient_amounts import IngredientAmounts


OMIT = typing.cast(typing.Any, ...)


class AmountClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAmountClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAmountClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAmountClient
        """
        return self._raw_client

    def get_recipe_amounts(
        self, recipe_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[IngredientAmounts]:
        """
        Get the quantities of the ingredients belonging to a recipe

        Parameters
        ----------
        recipe_id : str
            UUID of a recipe

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[IngredientAmounts]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.amount.get_recipe_amounts(
            recipe_id="RecipeID",
        )
        """
        _response = self._raw_client.get_recipe_amounts(recipe_id, request_options=request_options)
        return _response.data

    def post_recipe_amounts(
        self,
        recipe_id: str,
        *,
        request: typing.Sequence[IngredientAmounts],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[IngredientAmounts]:
        """
        Set the quantities of the ingredients belonging to a recipe

        Parameters
        ----------
        recipe_id : str
            UUID of a recipe

        request : typing.Sequence[IngredientAmounts]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[IngredientAmounts]
            Created

        Examples
        --------
        from fern.amount import IngredientAmounts

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.amount.post_recipe_amounts(
            recipe_id="RecipeID",
            request=[
                IngredientAmounts(
                    ingredient_id="a796f891-d42f-4182-9ff7-893a41726643",
                    unit_id="b4d99423-9c40-4f80-82fa-5377fe7498b1",
                    quantity=3.0,
                )
            ],
        )
        """
        _response = self._raw_client.post_recipe_amounts(recipe_id, request=request, request_options=request_options)
        return _response.data

    def put_recipe_amounts(
        self,
        recipe_id: str,
        *,
        request: typing.Sequence[IngredientAmounts],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[IngredientAmounts]:
        """
        Update the quantities of the ingredients belonging to a recipe

        Parameters
        ----------
        recipe_id : str
            UUID of a recipe

        request : typing.Sequence[IngredientAmounts]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[IngredientAmounts]
            OK

        Examples
        --------
        from fern.amount import IngredientAmounts

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.amount.put_recipe_amounts(
            recipe_id="RecipeID",
            request=[
                IngredientAmounts(
                    ingredient_id="a796f891-d42f-4182-9ff7-893a41726643",
                    unit_id="b4d99423-9c40-4f80-82fa-5377fe7498b1",
                    quantity=3.0,
                )
            ],
        )
        """
        _response = self._raw_client.put_recipe_amounts(recipe_id, request=request, request_options=request_options)
        return _response.data

    def delete_recipe_amounts(
        self,
        recipe_id: str,
        *,
        request: typing.Sequence[IngredientAmounts],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Delete ingredient quantities belonging to a recipe.
        Each provided ingredient reference will be deleted. If you want to delete all ingredients belonging to a recipe, send all.

        Parameters
        ----------
        recipe_id : str
            UUID of a recipe

        request : typing.Sequence[IngredientAmounts]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            No Content

        Examples
        --------
        from fern.amount import IngredientAmounts

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.amount.delete_recipe_amounts(
            recipe_id="RecipeID",
            request=[IngredientAmounts(), IngredientAmounts()],
        )
        """
        _response = self._raw_client.delete_recipe_amounts(recipe_id, request=request, request_options=request_options)
        return _response.data


class AsyncAmountClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAmountClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAmountClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAmountClient
        """
        return self._raw_client

    async def get_recipe_amounts(
        self, recipe_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[IngredientAmounts]:
        """
        Get the quantities of the ingredients belonging to a recipe

        Parameters
        ----------
        recipe_id : str
            UUID of a recipe

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[IngredientAmounts]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.amount.get_recipe_amounts(
                recipe_id="RecipeID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_recipe_amounts(recipe_id, request_options=request_options)
        return _response.data

    async def post_recipe_amounts(
        self,
        recipe_id: str,
        *,
        request: typing.Sequence[IngredientAmounts],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[IngredientAmounts]:
        """
        Set the quantities of the ingredients belonging to a recipe

        Parameters
        ----------
        recipe_id : str
            UUID of a recipe

        request : typing.Sequence[IngredientAmounts]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[IngredientAmounts]
            Created

        Examples
        --------
        import asyncio

        from fern.amount import IngredientAmounts

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.amount.post_recipe_amounts(
                recipe_id="RecipeID",
                request=[
                    IngredientAmounts(
                        ingredient_id="a796f891-d42f-4182-9ff7-893a41726643",
                        unit_id="b4d99423-9c40-4f80-82fa-5377fe7498b1",
                        quantity=3.0,
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_recipe_amounts(
            recipe_id, request=request, request_options=request_options
        )
        return _response.data

    async def put_recipe_amounts(
        self,
        recipe_id: str,
        *,
        request: typing.Sequence[IngredientAmounts],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[IngredientAmounts]:
        """
        Update the quantities of the ingredients belonging to a recipe

        Parameters
        ----------
        recipe_id : str
            UUID of a recipe

        request : typing.Sequence[IngredientAmounts]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[IngredientAmounts]
            OK

        Examples
        --------
        import asyncio

        from fern.amount import IngredientAmounts

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.amount.put_recipe_amounts(
                recipe_id="RecipeID",
                request=[
                    IngredientAmounts(
                        ingredient_id="a796f891-d42f-4182-9ff7-893a41726643",
                        unit_id="b4d99423-9c40-4f80-82fa-5377fe7498b1",
                        quantity=3.0,
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_recipe_amounts(
            recipe_id, request=request, request_options=request_options
        )
        return _response.data

    async def delete_recipe_amounts(
        self,
        recipe_id: str,
        *,
        request: typing.Sequence[IngredientAmounts],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Delete ingredient quantities belonging to a recipe.
        Each provided ingredient reference will be deleted. If you want to delete all ingredients belonging to a recipe, send all.

        Parameters
        ----------
        recipe_id : str
            UUID of a recipe

        request : typing.Sequence[IngredientAmounts]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            No Content

        Examples
        --------
        import asyncio

        from fern.amount import IngredientAmounts

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.amount.delete_recipe_amounts(
                recipe_id="RecipeID",
                request=[IngredientAmounts(), IngredientAmounts()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_recipe_amounts(
            recipe_id, request=request, request_options=request_options
        )
        return _response.data

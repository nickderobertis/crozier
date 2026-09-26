

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.generation_plan_out import GenerationPlanOut
from ..types.product_profile_in import ProductProfileIn
from .raw_client import AsyncRawGenerationPlanClient, RawGenerationPlanClient
from .types.generation_plan_request_locale import GenerationPlanRequestLocale


OMIT = typing.cast(typing.Any, ...)


class GenerationPlanClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawGenerationPlanClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawGenerationPlanClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawGenerationPlanClient
        """
        return self._raw_client

    def create_generation_plan(
        self,
        *,
        kit_client_id: str,
        product: ProductProfileIn,
        source_image_ref: str,
        explicit_template_refs: typing.Optional[typing.Sequence[str]] = OMIT,
        locale: typing.Optional[GenerationPlanRequestLocale] = OMIT,
        user_prompt: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GenerationPlanOut:
        """
        Create the initial editable output plan for the generation workflow.

        This endpoint intentionally owns the compatibility/default planning
        contract so the frontend can fail loudly when the backend route is broken
        instead of silently manufacturing a local plan.

        Parameters
        ----------
        kit_client_id : str

        product : ProductProfileIn

        source_image_ref : str

        explicit_template_refs : typing.Optional[typing.Sequence[str]]

        locale : typing.Optional[GenerationPlanRequestLocale]

        user_prompt : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GenerationPlanOut
            Successful Response

        Examples
        --------
        from fern import FernApi, ProductProfileIn

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.generation_plan.create_generation_plan(
            kit_client_id="kit_client_id",
            product=ProductProfileIn(),
            source_image_ref="source_image_ref",
        )
        """
        _response = self._raw_client.create_generation_plan(
            kit_client_id=kit_client_id,
            product=product,
            source_image_ref=source_image_ref,
            explicit_template_refs=explicit_template_refs,
            locale=locale,
            user_prompt=user_prompt,
            request_options=request_options,
        )
        return _response.data


class AsyncGenerationPlanClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawGenerationPlanClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawGenerationPlanClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawGenerationPlanClient
        """
        return self._raw_client

    async def create_generation_plan(
        self,
        *,
        kit_client_id: str,
        product: ProductProfileIn,
        source_image_ref: str,
        explicit_template_refs: typing.Optional[typing.Sequence[str]] = OMIT,
        locale: typing.Optional[GenerationPlanRequestLocale] = OMIT,
        user_prompt: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GenerationPlanOut:
        """
        Create the initial editable output plan for the generation workflow.

        This endpoint intentionally owns the compatibility/default planning
        contract so the frontend can fail loudly when the backend route is broken
        instead of silently manufacturing a local plan.

        Parameters
        ----------
        kit_client_id : str

        product : ProductProfileIn

        source_image_ref : str

        explicit_template_refs : typing.Optional[typing.Sequence[str]]

        locale : typing.Optional[GenerationPlanRequestLocale]

        user_prompt : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GenerationPlanOut
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ProductProfileIn

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.generation_plan.create_generation_plan(
                kit_client_id="kit_client_id",
                product=ProductProfileIn(),
                source_image_ref="source_image_ref",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_generation_plan(
            kit_client_id=kit_client_id,
            product=product,
            source_image_ref=source_image_ref,
            explicit_template_refs=explicit_template_refs,
            locale=locale,
            user_prompt=user_prompt,
            request_options=request_options,
        )
        return _response.data

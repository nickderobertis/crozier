

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.delete_kit_image_response import DeleteKitImageResponse
from ..types.generate_response import GenerateResponse
from ..types.kit_list_response import KitListResponse
from ..types.kit_meta_response import KitMetaResponse
from ..types.spec_in import SpecIn
from .raw_client import AsyncRawImagegenClient, RawImagegenClient
from .types.generate_request_locale import GenerateRequestLocale
from .types.list_kits_api_kits_get_request_order import ListKitsApiKitsGetRequestOrder
from .types.list_kits_api_kits_get_request_sort import ListKitsApiKitsGetRequestSort


OMIT = typing.cast(typing.Any, ...)


class ImagegenClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawImagegenClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawImagegenClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawImagegenClient
        """
        return self._raw_client

    def list_kits(
        self,
        *,
        recent: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        status: typing.Optional[str] = None,
        locale: typing.Optional[str] = None,
        min_score: typing.Optional[int] = None,
        category: typing.Optional[str] = None,
        sku: typing.Optional[str] = None,
        sort: typing.Optional[ListKitsApiKitsGetRequestSort] = None,
        order: typing.Optional[ListKitsApiKitsGetRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> KitListResponse:
        """
        Return kits joined with their product catalog row, paginated & filtered.

        ``thumbs`` is the concatenation of up-to-5 hero png_paths (slot 1..5) and
        up-to-9 detail png_paths (M1..M9) — 14 slots total, NULL-padded for any
        missing rows.  Callers render placeholder cells for NULL entries.

        Standalone generated assets are also returned as catalog entries with
        ``source_type='asset'`` so non-kit generations remain visible in Catalog.

        ``recent=true`` preserves the Dashboard contract by returning kit rows
        only. Catalog calls leave ``recent`` false and receive kit plus asset rows.

        ``recent`` is otherwise advisory; sort defaults to ``created_at DESC`` to preserve
        the EPIC-7 Dashboard call shape (``?recent=true&limit=6``).  Catalog
        (EPIC-8) passes ``offset``, ``status``, ``locale``, ``min_score``,
        ``category``, ``sort``, ``order`` for filtered/paginated views.

        Parameters
        ----------
        recent : typing.Optional[bool]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        status : typing.Optional[str]

        locale : typing.Optional[str]

        min_score : typing.Optional[int]

        category : typing.Optional[str]

        sku : typing.Optional[str]

        sort : typing.Optional[ListKitsApiKitsGetRequestSort]

        order : typing.Optional[ListKitsApiKitsGetRequestOrder]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        KitListResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.imagegen.list_kits()
        """
        _response = self._raw_client.list_kits(
            recent=recent,
            limit=limit,
            offset=offset,
            status=status,
            locale=locale,
            min_score=min_score,
            category=category,
            sku=sku,
            sort=sort,
            order=order,
            request_options=request_options,
        )
        return _response.data

    def delete_generated_image(
        self, db_kit_id: int, image_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteKitImageResponse:
        """
        Remove a generated image from a catalog kit slot and delete its PNG.

        Parameters
        ----------
        db_kit_id : int

        image_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteKitImageResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.imagegen.delete_generated_image(
            db_kit_id=1,
            image_id="image_id",
        )
        """
        _response = self._raw_client.delete_generated_image(db_kit_id, image_id, request_options=request_options)
        return _response.data

    def get_kit_meta(
        self, db_kit_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> KitMetaResponse:
        """
        Read result sidecars for *db_kit_id*; 404 if the kit root is unknown.

        Parameters
        ----------
        db_kit_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        KitMetaResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.imagegen.get_kit_meta(
            db_kit_id=1,
        )
        """
        _response = self._raw_client.get_kit_meta(db_kit_id, request_options=request_options)
        return _response.data

    def get_kit_events(self, kit_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Stream per-image status events for *kit_id* as text/event-stream.

        Returns 404 when the kit_id has never been published to the bus
        (callers can use this as a "kit not started" signal).  Each line
        conforms to the SSE wire format::

            data: {"image_id": "H1", "status": "color_locked", "progress": 0,
                   "brand_color_locked": true}

        Parameters
        ----------
        kit_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.imagegen.get_kit_events(
            kit_id="kit_id",
        )
        """
        _response = self._raw_client.get_kit_events(kit_id, request_options=request_options)
        return _response.data

    def post_generate(
        self,
        kit_id: str,
        *,
        brand_color_hex: str,
        locale: GenerateRequestLocale,
        spec: SpecIn,
        retrieved_bestseller_ids: typing.Optional[typing.Sequence[int]] = OMIT,
        style_prompt: typing.Optional[str] = OMIT,
        template_scheme_ref: typing.Optional[str] = OMIT,
        template_slot_overrides: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GenerateResponse:
        """
        Generate the 14-image kit for *kit_id*.

        Parameters
        ----------
        kit_id : str

        brand_color_hex : str

        locale : GenerateRequestLocale

        spec : SpecIn

        retrieved_bestseller_ids : typing.Optional[typing.Sequence[int]]

        style_prompt : typing.Optional[str]

        template_scheme_ref : typing.Optional[str]

        template_slot_overrides : typing.Optional[typing.Dict[str, str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GenerateResponse
            Successful Response

        Examples
        --------
        from fern.imagegen import GenerateRequestLocale

        from fern import (
            DetailSectionIn,
            DetailSectionInId,
            FernApi,
            HeroSectionIn,
            HeroSectionInId,
            SellingPointIn,
            SellingPointInPriority,
            SkuMetaIn,
            SkuMetaInProductType,
            SpecIn,
            SpecInLocale,
            ThreePieceIn,
        )

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.imagegen.post_generate(
            kit_id="kit_id",
            brand_color_hex="brand_color_hex",
            locale=GenerateRequestLocale.ZH,
            spec=SpecIn(
                detail_sections=[
                    DetailSectionIn(
                        id=DetailSectionInId.M1,
                        three_piece=ThreePieceIn(
                            copy="copy",
                            design_note="design_note",
                            visual="visual",
                        ),
                    )
                ],
                hero_sections=[
                    HeroSectionIn(
                        id=HeroSectionInId.H1,
                        three_piece=ThreePieceIn(
                            copy="copy",
                            design_note="design_note",
                            visual="visual",
                        ),
                    )
                ],
                locale=SpecInLocale.ZH,
                selling_points=[
                    SellingPointIn(
                        evidence="evidence",
                        priority=SellingPointInPriority.HIGH,
                        title="title",
                    )
                ],
                sku_meta=SkuMetaIn(
                    brand="brand",
                    category="category",
                    price=1.1,
                    product_type=SkuMetaInProductType.BLUE_HAT,
                ),
            ),
        )
        """
        _response = self._raw_client.post_generate(
            kit_id,
            brand_color_hex=brand_color_hex,
            locale=locale,
            spec=spec,
            retrieved_bestseller_ids=retrieved_bestseller_ids,
            style_prompt=style_prompt,
            template_scheme_ref=template_scheme_ref,
            template_slot_overrides=template_slot_overrides,
            request_options=request_options,
        )
        return _response.data

    def get_generated_image(
        self, kit_id: str, image_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Serve a generated kit image by public kit id and slot id.

        Parameters
        ----------
        kit_id : str

        image_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.imagegen.get_generated_image(
            kit_id="kit_id",
            image_id="image_id",
        )
        """
        _response = self._raw_client.get_generated_image(kit_id, image_id, request_options=request_options)
        return _response.data


class AsyncImagegenClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawImagegenClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawImagegenClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawImagegenClient
        """
        return self._raw_client

    async def list_kits(
        self,
        *,
        recent: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        status: typing.Optional[str] = None,
        locale: typing.Optional[str] = None,
        min_score: typing.Optional[int] = None,
        category: typing.Optional[str] = None,
        sku: typing.Optional[str] = None,
        sort: typing.Optional[ListKitsApiKitsGetRequestSort] = None,
        order: typing.Optional[ListKitsApiKitsGetRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> KitListResponse:
        """
        Return kits joined with their product catalog row, paginated & filtered.

        ``thumbs`` is the concatenation of up-to-5 hero png_paths (slot 1..5) and
        up-to-9 detail png_paths (M1..M9) — 14 slots total, NULL-padded for any
        missing rows.  Callers render placeholder cells for NULL entries.

        Standalone generated assets are also returned as catalog entries with
        ``source_type='asset'`` so non-kit generations remain visible in Catalog.

        ``recent=true`` preserves the Dashboard contract by returning kit rows
        only. Catalog calls leave ``recent`` false and receive kit plus asset rows.

        ``recent`` is otherwise advisory; sort defaults to ``created_at DESC`` to preserve
        the EPIC-7 Dashboard call shape (``?recent=true&limit=6``).  Catalog
        (EPIC-8) passes ``offset``, ``status``, ``locale``, ``min_score``,
        ``category``, ``sort``, ``order`` for filtered/paginated views.

        Parameters
        ----------
        recent : typing.Optional[bool]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        status : typing.Optional[str]

        locale : typing.Optional[str]

        min_score : typing.Optional[int]

        category : typing.Optional[str]

        sku : typing.Optional[str]

        sort : typing.Optional[ListKitsApiKitsGetRequestSort]

        order : typing.Optional[ListKitsApiKitsGetRequestOrder]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        KitListResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.imagegen.list_kits()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_kits(
            recent=recent,
            limit=limit,
            offset=offset,
            status=status,
            locale=locale,
            min_score=min_score,
            category=category,
            sku=sku,
            sort=sort,
            order=order,
            request_options=request_options,
        )
        return _response.data

    async def delete_generated_image(
        self, db_kit_id: int, image_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteKitImageResponse:
        """
        Remove a generated image from a catalog kit slot and delete its PNG.

        Parameters
        ----------
        db_kit_id : int

        image_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteKitImageResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.imagegen.delete_generated_image(
                db_kit_id=1,
                image_id="image_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_generated_image(db_kit_id, image_id, request_options=request_options)
        return _response.data

    async def get_kit_meta(
        self, db_kit_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> KitMetaResponse:
        """
        Read result sidecars for *db_kit_id*; 404 if the kit root is unknown.

        Parameters
        ----------
        db_kit_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        KitMetaResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.imagegen.get_kit_meta(
                db_kit_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_kit_meta(db_kit_id, request_options=request_options)
        return _response.data

    async def get_kit_events(
        self, kit_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Stream per-image status events for *kit_id* as text/event-stream.

        Returns 404 when the kit_id has never been published to the bus
        (callers can use this as a "kit not started" signal).  Each line
        conforms to the SSE wire format::

            data: {"image_id": "H1", "status": "color_locked", "progress": 0,
                   "brand_color_locked": true}

        Parameters
        ----------
        kit_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.imagegen.get_kit_events(
                kit_id="kit_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_kit_events(kit_id, request_options=request_options)
        return _response.data

    async def post_generate(
        self,
        kit_id: str,
        *,
        brand_color_hex: str,
        locale: GenerateRequestLocale,
        spec: SpecIn,
        retrieved_bestseller_ids: typing.Optional[typing.Sequence[int]] = OMIT,
        style_prompt: typing.Optional[str] = OMIT,
        template_scheme_ref: typing.Optional[str] = OMIT,
        template_slot_overrides: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GenerateResponse:
        """
        Generate the 14-image kit for *kit_id*.

        Parameters
        ----------
        kit_id : str

        brand_color_hex : str

        locale : GenerateRequestLocale

        spec : SpecIn

        retrieved_bestseller_ids : typing.Optional[typing.Sequence[int]]

        style_prompt : typing.Optional[str]

        template_scheme_ref : typing.Optional[str]

        template_slot_overrides : typing.Optional[typing.Dict[str, str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GenerateResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern.imagegen import GenerateRequestLocale

        from fern import (
            AsyncFernApi,
            DetailSectionIn,
            DetailSectionInId,
            HeroSectionIn,
            HeroSectionInId,
            SellingPointIn,
            SellingPointInPriority,
            SkuMetaIn,
            SkuMetaInProductType,
            SpecIn,
            SpecInLocale,
            ThreePieceIn,
        )

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.imagegen.post_generate(
                kit_id="kit_id",
                brand_color_hex="brand_color_hex",
                locale=GenerateRequestLocale.ZH,
                spec=SpecIn(
                    detail_sections=[
                        DetailSectionIn(
                            id=DetailSectionInId.M1,
                            three_piece=ThreePieceIn(
                                copy="copy",
                                design_note="design_note",
                                visual="visual",
                            ),
                        )
                    ],
                    hero_sections=[
                        HeroSectionIn(
                            id=HeroSectionInId.H1,
                            three_piece=ThreePieceIn(
                                copy="copy",
                                design_note="design_note",
                                visual="visual",
                            ),
                        )
                    ],
                    locale=SpecInLocale.ZH,
                    selling_points=[
                        SellingPointIn(
                            evidence="evidence",
                            priority=SellingPointInPriority.HIGH,
                            title="title",
                        )
                    ],
                    sku_meta=SkuMetaIn(
                        brand="brand",
                        category="category",
                        price=1.1,
                        product_type=SkuMetaInProductType.BLUE_HAT,
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_generate(
            kit_id,
            brand_color_hex=brand_color_hex,
            locale=locale,
            spec=spec,
            retrieved_bestseller_ids=retrieved_bestseller_ids,
            style_prompt=style_prompt,
            template_scheme_ref=template_scheme_ref,
            template_slot_overrides=template_slot_overrides,
            request_options=request_options,
        )
        return _response.data

    async def get_generated_image(
        self, kit_id: str, image_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Serve a generated kit image by public kit id and slot id.

        Parameters
        ----------
        kit_id : str

        image_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.imagegen.get_generated_image(
                kit_id="kit_id",
                image_id="image_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_generated_image(kit_id, image_id, request_options=request_options)
        return _response.data

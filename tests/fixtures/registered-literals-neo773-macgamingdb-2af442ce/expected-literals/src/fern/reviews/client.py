

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawReviewsClient, RawReviewsClient
from .types.review_create_request_graphics_settings import ReviewCreateRequestGraphicsSettings
from .types.review_create_request_performance import ReviewCreateRequestPerformance
from .types.review_create_request_play_method import ReviewCreateRequestPlayMethod
from .types.review_create_request_translation_layer import ReviewCreateRequestTranslationLayer
from .types.review_create_response import ReviewCreateResponse
from .types.review_delete_review_response import ReviewDeleteReviewResponse
from .types.review_get_upload_url_response import ReviewGetUploadUrlResponse
from .types.review_list_mine_response_item import ReviewListMineResponseItem
from .types.review_update_review_request_performance import ReviewUpdateReviewRequestPerformance
from .types.review_update_review_response import ReviewUpdateReviewResponse


OMIT = typing.cast(typing.Any, ...)


class ReviewsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawReviewsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawReviewsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawReviewsClient
        """
        return self._raw_client

    def review_list_mine(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ReviewListMineResponseItem]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ReviewListMineResponseItem]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.reviews.review_list_mine()
        """
        _response = self._raw_client.review_list_mine(request_options=request_options)
        return _response.data

    def review_get_upload_url(
        self, *, filename: str, content_type: str, game_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ReviewGetUploadUrlResponse:
        """
        Parameters
        ----------
        filename : str

        content_type : str

        game_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReviewGetUploadUrlResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.reviews.review_get_upload_url(
            filename="filename",
            content_type="contentType",
            game_id="gameId",
        )
        """
        _response = self._raw_client.review_get_upload_url(
            filename=filename, content_type=content_type, game_id=game_id, request_options=request_options
        )
        return _response.data

    def review_create(
        self,
        *,
        game_id: str,
        play_method: ReviewCreateRequestPlayMethod,
        performance: ReviewCreateRequestPerformance,
        graphics_settings: ReviewCreateRequestGraphicsSettings,
        mac_config_identifier: str,
        translation_layer: typing.Optional[ReviewCreateRequestTranslationLayer] = OMIT,
        fps: typing.Optional[float] = OMIT,
        resolution: typing.Optional[str] = OMIT,
        notes: typing.Optional[str] = OMIT,
        screenshots: typing.Optional[typing.Sequence[str]] = OMIT,
        software_version: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[ReviewCreateResponse]:
        """
        Parameters
        ----------
        game_id : str

        play_method : ReviewCreateRequestPlayMethod

        performance : ReviewCreateRequestPerformance

        graphics_settings : ReviewCreateRequestGraphicsSettings

        mac_config_identifier : str

        translation_layer : typing.Optional[ReviewCreateRequestTranslationLayer]

        fps : typing.Optional[float]

        resolution : typing.Optional[str]

        notes : typing.Optional[str]

        screenshots : typing.Optional[typing.Sequence[str]]

        software_version : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[ReviewCreateResponse]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.reviews.review_create(
            game_id="gameId",
            play_method="NATIVE",
            performance="EXCELLENT",
            graphics_settings="ULTRA",
            mac_config_identifier="macConfigIdentifier",
        )
        """
        _response = self._raw_client.review_create(
            game_id=game_id,
            play_method=play_method,
            performance=performance,
            graphics_settings=graphics_settings,
            mac_config_identifier=mac_config_identifier,
            translation_layer=translation_layer,
            fps=fps,
            resolution=resolution,
            notes=notes,
            screenshots=screenshots,
            software_version=software_version,
            request_options=request_options,
        )
        return _response.data

    def review_delete_review(
        self, review_id: str, *, confirmation: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> ReviewDeleteReviewResponse:
        """
        Parameters
        ----------
        review_id : str

        confirmation : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReviewDeleteReviewResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.reviews.review_delete_review(
            review_id="reviewId",
            confirmation=True,
        )
        """
        _response = self._raw_client.review_delete_review(
            review_id, confirmation=confirmation, request_options=request_options
        )
        return _response.data

    def review_update_review(
        self,
        review_id: str,
        *,
        notes: str,
        performance: typing.Optional[ReviewUpdateReviewRequestPerformance] = OMIT,
        fps: typing.Optional[float] = OMIT,
        resolution: typing.Optional[str] = OMIT,
        software_version: typing.Optional[str] = OMIT,
        screenshots: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ReviewUpdateReviewResponse:
        """
        Parameters
        ----------
        review_id : str

        notes : str

        performance : typing.Optional[ReviewUpdateReviewRequestPerformance]

        fps : typing.Optional[float]

        resolution : typing.Optional[str]

        software_version : typing.Optional[str]

        screenshots : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReviewUpdateReviewResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.reviews.review_update_review(
            review_id="reviewId",
            notes="notes",
        )
        """
        _response = self._raw_client.review_update_review(
            review_id,
            notes=notes,
            performance=performance,
            fps=fps,
            resolution=resolution,
            software_version=software_version,
            screenshots=screenshots,
            request_options=request_options,
        )
        return _response.data


class AsyncReviewsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawReviewsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawReviewsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawReviewsClient
        """
        return self._raw_client

    async def review_list_mine(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ReviewListMineResponseItem]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ReviewListMineResponseItem]
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.reviews.review_list_mine()


        asyncio.run(main())
        """
        _response = await self._raw_client.review_list_mine(request_options=request_options)
        return _response.data

    async def review_get_upload_url(
        self, *, filename: str, content_type: str, game_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ReviewGetUploadUrlResponse:
        """
        Parameters
        ----------
        filename : str

        content_type : str

        game_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReviewGetUploadUrlResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.reviews.review_get_upload_url(
                filename="filename",
                content_type="contentType",
                game_id="gameId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.review_get_upload_url(
            filename=filename, content_type=content_type, game_id=game_id, request_options=request_options
        )
        return _response.data

    async def review_create(
        self,
        *,
        game_id: str,
        play_method: ReviewCreateRequestPlayMethod,
        performance: ReviewCreateRequestPerformance,
        graphics_settings: ReviewCreateRequestGraphicsSettings,
        mac_config_identifier: str,
        translation_layer: typing.Optional[ReviewCreateRequestTranslationLayer] = OMIT,
        fps: typing.Optional[float] = OMIT,
        resolution: typing.Optional[str] = OMIT,
        notes: typing.Optional[str] = OMIT,
        screenshots: typing.Optional[typing.Sequence[str]] = OMIT,
        software_version: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[ReviewCreateResponse]:
        """
        Parameters
        ----------
        game_id : str

        play_method : ReviewCreateRequestPlayMethod

        performance : ReviewCreateRequestPerformance

        graphics_settings : ReviewCreateRequestGraphicsSettings

        mac_config_identifier : str

        translation_layer : typing.Optional[ReviewCreateRequestTranslationLayer]

        fps : typing.Optional[float]

        resolution : typing.Optional[str]

        notes : typing.Optional[str]

        screenshots : typing.Optional[typing.Sequence[str]]

        software_version : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[ReviewCreateResponse]
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.reviews.review_create(
                game_id="gameId",
                play_method="NATIVE",
                performance="EXCELLENT",
                graphics_settings="ULTRA",
                mac_config_identifier="macConfigIdentifier",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.review_create(
            game_id=game_id,
            play_method=play_method,
            performance=performance,
            graphics_settings=graphics_settings,
            mac_config_identifier=mac_config_identifier,
            translation_layer=translation_layer,
            fps=fps,
            resolution=resolution,
            notes=notes,
            screenshots=screenshots,
            software_version=software_version,
            request_options=request_options,
        )
        return _response.data

    async def review_delete_review(
        self, review_id: str, *, confirmation: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> ReviewDeleteReviewResponse:
        """
        Parameters
        ----------
        review_id : str

        confirmation : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReviewDeleteReviewResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.reviews.review_delete_review(
                review_id="reviewId",
                confirmation=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.review_delete_review(
            review_id, confirmation=confirmation, request_options=request_options
        )
        return _response.data

    async def review_update_review(
        self,
        review_id: str,
        *,
        notes: str,
        performance: typing.Optional[ReviewUpdateReviewRequestPerformance] = OMIT,
        fps: typing.Optional[float] = OMIT,
        resolution: typing.Optional[str] = OMIT,
        software_version: typing.Optional[str] = OMIT,
        screenshots: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ReviewUpdateReviewResponse:
        """
        Parameters
        ----------
        review_id : str

        notes : str

        performance : typing.Optional[ReviewUpdateReviewRequestPerformance]

        fps : typing.Optional[float]

        resolution : typing.Optional[str]

        software_version : typing.Optional[str]

        screenshots : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReviewUpdateReviewResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.reviews.review_update_review(
                review_id="reviewId",
                notes="notes",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.review_update_review(
            review_id,
            notes=notes,
            performance=performance,
            fps=fps,
            resolution=resolution,
            software_version=software_version,
            screenshots=screenshots,
            request_options=request_options,
        )
        return _response.data

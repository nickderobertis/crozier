

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.images_response import ImagesResponse
from .raw_client import AsyncRawImagesClient, RawImagesClient
from .types.create_image_edit_request_model import CreateImageEditRequestModel
from .types.create_image_edit_request_response_format import CreateImageEditRequestResponseFormat
from .types.create_image_edit_request_size import CreateImageEditRequestSize
from .types.create_image_request_model import CreateImageRequestModel
from .types.create_image_request_quality import CreateImageRequestQuality
from .types.create_image_request_response_format import CreateImageRequestResponseFormat
from .types.create_image_request_size import CreateImageRequestSize
from .types.create_image_request_style import CreateImageRequestStyle
from .types.create_image_variation_request_model import CreateImageVariationRequestModel
from .types.create_image_variation_request_response_format import CreateImageVariationRequestResponseFormat
from .types.create_image_variation_request_size import CreateImageVariationRequestSize


OMIT = typing.cast(typing.Any, ...)


class ImagesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawImagesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawImagesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawImagesClient
        """
        return self._raw_client

    def create_image(
        self,
        *,
        prompt: str,
        model: typing.Optional[CreateImageRequestModel] = OMIT,
        n: typing.Optional[int] = OMIT,
        quality: typing.Optional[CreateImageRequestQuality] = OMIT,
        response_format: typing.Optional[CreateImageRequestResponseFormat] = OMIT,
        size: typing.Optional[CreateImageRequestSize] = OMIT,
        style: typing.Optional[CreateImageRequestStyle] = OMIT,
        user: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ImagesResponse:
        """
        Parameters
        ----------
        prompt : str
            A text description of the desired image(s). The maximum length is 1000 characters for `dall-e-2` and 4000 characters for `dall-e-3`.

        model : typing.Optional[CreateImageRequestModel]
            The model to use for image generation.

        n : typing.Optional[int]
            The number of images to generate. Must be between 1 and 10. For `dall-e-3`, only `n=1` is supported.

        quality : typing.Optional[CreateImageRequestQuality]
            The quality of the image that will be generated. `hd` creates images with finer details and greater consistency across the image. This param is only supported for `dall-e-3`.

        response_format : typing.Optional[CreateImageRequestResponseFormat]
            The format in which the generated images are returned. Must be one of `url` or `b64_json`. URLs are only valid for 60 minutes after the image has been generated.

        size : typing.Optional[CreateImageRequestSize]
            The size of the generated images. Must be one of `256x256`, `512x512`, or `1024x1024` for `dall-e-2`. Must be one of `1024x1024`, `1792x1024`, or `1024x1792` for `dall-e-3` models.

        style : typing.Optional[CreateImageRequestStyle]
            The style of the generated images. Must be one of `vivid` or `natural`. Vivid causes the model to lean towards generating hyper-real and dramatic images. Natural causes the model to produce more natural, less hyper-real looking images. This param is only supported for `dall-e-3`.

        user : typing.Optional[str]
            A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse. [Learn more](/docs/guides/safety-best-practices/end-user-ids).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImagesResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.images.create_image(
            prompt="A cute baby sea otter",
        )
        """
        _response = self._raw_client.create_image(
            prompt=prompt,
            model=model,
            n=n,
            quality=quality,
            response_format=response_format,
            size=size,
            style=style,
            user=user,
            request_options=request_options,
        )
        return _response.data

    def create_image_edit(
        self,
        *,
        image: core.File,
        prompt: str,
        mask: typing.Optional[core.File] = OMIT,
        model: typing.Optional[CreateImageEditRequestModel] = OMIT,
        n: typing.Optional[int] = OMIT,
        size: typing.Optional[CreateImageEditRequestSize] = OMIT,
        response_format: typing.Optional[CreateImageEditRequestResponseFormat] = OMIT,
        user: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ImagesResponse:
        """
        Parameters
        ----------
        image : core.File
            See core.File for more documentation

        prompt : str
            A text description of the desired image(s). The maximum length is 1000 characters.

        mask : typing.Optional[core.File]
            See core.File for more documentation

        model : typing.Optional[CreateImageEditRequestModel]
            The model to use for image generation. Only `dall-e-2` is supported at this time.

        n : typing.Optional[int]
            The number of images to generate. Must be between 1 and 10.

        size : typing.Optional[CreateImageEditRequestSize]
            The size of the generated images. Must be one of `256x256`, `512x512`, or `1024x1024`.

        response_format : typing.Optional[CreateImageEditRequestResponseFormat]
            The format in which the generated images are returned. Must be one of `url` or `b64_json`. URLs are only valid for 60 minutes after the image has been generated.

        user : typing.Optional[str]
            A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse. [Learn more](/docs/guides/safety-best-practices/end-user-ids).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImagesResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.images.create_image_edit(
            prompt="prompt",
        )
        """
        _response = self._raw_client.create_image_edit(
            image=image,
            prompt=prompt,
            mask=mask,
            model=model,
            n=n,
            size=size,
            response_format=response_format,
            user=user,
            request_options=request_options,
        )
        return _response.data

    def create_image_variation(
        self,
        *,
        image: core.File,
        model: typing.Optional[CreateImageVariationRequestModel] = OMIT,
        n: typing.Optional[int] = OMIT,
        response_format: typing.Optional[CreateImageVariationRequestResponseFormat] = OMIT,
        size: typing.Optional[CreateImageVariationRequestSize] = OMIT,
        user: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ImagesResponse:
        """
        Parameters
        ----------
        image : core.File
            See core.File for more documentation

        model : typing.Optional[CreateImageVariationRequestModel]
            The model to use for image generation. Only `dall-e-2` is supported at this time.

        n : typing.Optional[int]
            The number of images to generate. Must be between 1 and 10. For `dall-e-3`, only `n=1` is supported.

        response_format : typing.Optional[CreateImageVariationRequestResponseFormat]
            The format in which the generated images are returned. Must be one of `url` or `b64_json`. URLs are only valid for 60 minutes after the image has been generated.

        size : typing.Optional[CreateImageVariationRequestSize]
            The size of the generated images. Must be one of `256x256`, `512x512`, or `1024x1024`.

        user : typing.Optional[str]
            A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse. [Learn more](/docs/guides/safety-best-practices/end-user-ids).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImagesResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.images.create_image_variation()
        """
        _response = self._raw_client.create_image_variation(
            image=image,
            model=model,
            n=n,
            response_format=response_format,
            size=size,
            user=user,
            request_options=request_options,
        )
        return _response.data


class AsyncImagesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawImagesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawImagesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawImagesClient
        """
        return self._raw_client

    async def create_image(
        self,
        *,
        prompt: str,
        model: typing.Optional[CreateImageRequestModel] = OMIT,
        n: typing.Optional[int] = OMIT,
        quality: typing.Optional[CreateImageRequestQuality] = OMIT,
        response_format: typing.Optional[CreateImageRequestResponseFormat] = OMIT,
        size: typing.Optional[CreateImageRequestSize] = OMIT,
        style: typing.Optional[CreateImageRequestStyle] = OMIT,
        user: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ImagesResponse:
        """
        Parameters
        ----------
        prompt : str
            A text description of the desired image(s). The maximum length is 1000 characters for `dall-e-2` and 4000 characters for `dall-e-3`.

        model : typing.Optional[CreateImageRequestModel]
            The model to use for image generation.

        n : typing.Optional[int]
            The number of images to generate. Must be between 1 and 10. For `dall-e-3`, only `n=1` is supported.

        quality : typing.Optional[CreateImageRequestQuality]
            The quality of the image that will be generated. `hd` creates images with finer details and greater consistency across the image. This param is only supported for `dall-e-3`.

        response_format : typing.Optional[CreateImageRequestResponseFormat]
            The format in which the generated images are returned. Must be one of `url` or `b64_json`. URLs are only valid for 60 minutes after the image has been generated.

        size : typing.Optional[CreateImageRequestSize]
            The size of the generated images. Must be one of `256x256`, `512x512`, or `1024x1024` for `dall-e-2`. Must be one of `1024x1024`, `1792x1024`, or `1024x1792` for `dall-e-3` models.

        style : typing.Optional[CreateImageRequestStyle]
            The style of the generated images. Must be one of `vivid` or `natural`. Vivid causes the model to lean towards generating hyper-real and dramatic images. Natural causes the model to produce more natural, less hyper-real looking images. This param is only supported for `dall-e-3`.

        user : typing.Optional[str]
            A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse. [Learn more](/docs/guides/safety-best-practices/end-user-ids).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImagesResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.images.create_image(
                prompt="A cute baby sea otter",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_image(
            prompt=prompt,
            model=model,
            n=n,
            quality=quality,
            response_format=response_format,
            size=size,
            style=style,
            user=user,
            request_options=request_options,
        )
        return _response.data

    async def create_image_edit(
        self,
        *,
        image: core.File,
        prompt: str,
        mask: typing.Optional[core.File] = OMIT,
        model: typing.Optional[CreateImageEditRequestModel] = OMIT,
        n: typing.Optional[int] = OMIT,
        size: typing.Optional[CreateImageEditRequestSize] = OMIT,
        response_format: typing.Optional[CreateImageEditRequestResponseFormat] = OMIT,
        user: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ImagesResponse:
        """
        Parameters
        ----------
        image : core.File
            See core.File for more documentation

        prompt : str
            A text description of the desired image(s). The maximum length is 1000 characters.

        mask : typing.Optional[core.File]
            See core.File for more documentation

        model : typing.Optional[CreateImageEditRequestModel]
            The model to use for image generation. Only `dall-e-2` is supported at this time.

        n : typing.Optional[int]
            The number of images to generate. Must be between 1 and 10.

        size : typing.Optional[CreateImageEditRequestSize]
            The size of the generated images. Must be one of `256x256`, `512x512`, or `1024x1024`.

        response_format : typing.Optional[CreateImageEditRequestResponseFormat]
            The format in which the generated images are returned. Must be one of `url` or `b64_json`. URLs are only valid for 60 minutes after the image has been generated.

        user : typing.Optional[str]
            A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse. [Learn more](/docs/guides/safety-best-practices/end-user-ids).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImagesResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.images.create_image_edit(
                prompt="prompt",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_image_edit(
            image=image,
            prompt=prompt,
            mask=mask,
            model=model,
            n=n,
            size=size,
            response_format=response_format,
            user=user,
            request_options=request_options,
        )
        return _response.data

    async def create_image_variation(
        self,
        *,
        image: core.File,
        model: typing.Optional[CreateImageVariationRequestModel] = OMIT,
        n: typing.Optional[int] = OMIT,
        response_format: typing.Optional[CreateImageVariationRequestResponseFormat] = OMIT,
        size: typing.Optional[CreateImageVariationRequestSize] = OMIT,
        user: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ImagesResponse:
        """
        Parameters
        ----------
        image : core.File
            See core.File for more documentation

        model : typing.Optional[CreateImageVariationRequestModel]
            The model to use for image generation. Only `dall-e-2` is supported at this time.

        n : typing.Optional[int]
            The number of images to generate. Must be between 1 and 10. For `dall-e-3`, only `n=1` is supported.

        response_format : typing.Optional[CreateImageVariationRequestResponseFormat]
            The format in which the generated images are returned. Must be one of `url` or `b64_json`. URLs are only valid for 60 minutes after the image has been generated.

        size : typing.Optional[CreateImageVariationRequestSize]
            The size of the generated images. Must be one of `256x256`, `512x512`, or `1024x1024`.

        user : typing.Optional[str]
            A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse. [Learn more](/docs/guides/safety-best-practices/end-user-ids).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImagesResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.images.create_image_variation()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_image_variation(
            image=image,
            model=model,
            n=n,
            response_format=response_format,
            size=size,
            user=user,
            request_options=request_options,
        )
        return _response.data

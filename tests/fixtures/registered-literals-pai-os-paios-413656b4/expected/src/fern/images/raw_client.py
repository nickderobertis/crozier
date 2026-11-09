

import typing
from json.decoder import JSONDecodeError

from .. import core
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.images_response import ImagesResponse
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
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawImagesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> HttpResponse[ImagesResponse]:
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
        HttpResponse[ImagesResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "images/generations",
            method="POST",
            json={
                "prompt": prompt,
                "model": convert_and_respect_annotation_metadata(
                    object_=model, annotation=typing.Optional[CreateImageRequestModel], direction="write"
                ),
                "n": n,
                "quality": quality,
                "response_format": response_format,
                "size": size,
                "style": style,
                "user": user,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ImagesResponse,
                    parse_obj_as(
                        type_=ImagesResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[ImagesResponse]:
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
        HttpResponse[ImagesResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "images/edits",
            method="POST",
            data={
                "prompt": prompt,
                "model": model,
                "n": n,
                "size": size,
                "response_format": response_format,
                "user": user,
            },
            files={
                "image": image,
                **({"mask": mask} if mask is not None else {}),
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ImagesResponse,
                    parse_obj_as(
                        type_=ImagesResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[ImagesResponse]:
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
        HttpResponse[ImagesResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "images/variations",
            method="POST",
            data={
                "model": model,
                "n": n,
                "response_format": response_format,
                "size": size,
                "user": user,
            },
            files={
                "image": image,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ImagesResponse,
                    parse_obj_as(
                        type_=ImagesResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawImagesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> AsyncHttpResponse[ImagesResponse]:
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
        AsyncHttpResponse[ImagesResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "images/generations",
            method="POST",
            json={
                "prompt": prompt,
                "model": convert_and_respect_annotation_metadata(
                    object_=model, annotation=typing.Optional[CreateImageRequestModel], direction="write"
                ),
                "n": n,
                "quality": quality,
                "response_format": response_format,
                "size": size,
                "style": style,
                "user": user,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ImagesResponse,
                    parse_obj_as(
                        type_=ImagesResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[ImagesResponse]:
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
        AsyncHttpResponse[ImagesResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "images/edits",
            method="POST",
            data={
                "prompt": prompt,
                "model": model,
                "n": n,
                "size": size,
                "response_format": response_format,
                "user": user,
            },
            files={
                "image": image,
                **({"mask": mask} if mask is not None else {}),
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ImagesResponse,
                    parse_obj_as(
                        type_=ImagesResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[ImagesResponse]:
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
        AsyncHttpResponse[ImagesResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "images/variations",
            method="POST",
            data={
                "model": model,
                "n": n,
                "response_format": response_format,
                "size": size,
                "user": user,
            },
            files={
                "image": image,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ImagesResponse,
                    parse_obj_as(
                        type_=ImagesResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)



import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.api_i_paged_response_global_resources_shared_models_global_image import (
    ApiIPagedResponseGlobalResourcesSharedModelsGlobalImage,
)
from ..types.global_resources_shared_models_global_image import GlobalResourcesSharedModelsGlobalImage
from ..types.global_resources_shared_models_global_image_category import GlobalResourcesSharedModelsGlobalImageCategory
from ..types.global_resources_shared_models_global_image_state import GlobalResourcesSharedModelsGlobalImageState
from ..types.system_object import SystemObject
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawGlobalimagesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def getglobalimages(
        self,
        *,
        search: typing.Optional[str] = None,
        category_id: typing.Optional[str] = None,
        publisher: typing.Optional[str] = None,
        include_deleted: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiIPagedResponseGlobalResourcesSharedModelsGlobalImage]:
        """
        No Documentation Found.

        Parameters
        ----------
        search : typing.Optional[str]
            Optional. Searches for matching global images with the matching Category Name, Publisher or Description

        category_id : typing.Optional[str]


        publisher : typing.Optional[str]


        include_deleted : typing.Optional[bool]
            Indicates whether to include GlobalImages marked as removed.

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiIPagedResponseGlobalResourcesSharedModelsGlobalImage]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/GlobalImages",
            method="GET",
            params={
                "search": search,
                "categoryId": category_id,
                "publisher": publisher,
                "includeDeleted": include_deleted,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiIPagedResponseGlobalResourcesSharedModelsGlobalImage,
                    parse_obj_as(
                        type_=ApiIPagedResponseGlobalResourcesSharedModelsGlobalImage,
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

    def postglobalimage(
        self,
        *,
        crc: str,
        description: str,
        height: int,
        name: str,
        state: GlobalResourcesSharedModelsGlobalImageState,
        thumbnail_crc: str,
        width: int,
        override_publisher_or_date: typing.Optional[bool] = None,
        categories: typing.Optional[typing.Sequence[GlobalResourcesSharedModelsGlobalImageCategory]] = OMIT,
        date: typing.Optional[dt.datetime] = OMIT,
        id: typing.Optional[str] = OMIT,
        publisher: typing.Optional[str] = OMIT,
        size: typing.Optional[int] = OMIT,
        thumbnail_size: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        No Documentation Found.

        Parameters
        ----------
        crc : str
            The Hash of the file (SHA256, HEX-encoded).

        description : str
            The description of the file.

        height : int
            The height of the file.

        name : str
            The name of the file when downloaded.

        state : GlobalResourcesSharedModelsGlobalImageState
            Indicates the state of this file. Must be 'Created' when created. Read Only.

        thumbnail_crc : str
            The Hash of the thumbnail file (SHA256, HEX-encoded).

        width : int
            The width of the file.

        override_publisher_or_date : typing.Optional[bool]
            Whether to set the publisher and date to the provided values.

        categories : typing.Optional[typing.Sequence[GlobalResourcesSharedModelsGlobalImageCategory]]
            The category of the file.

        date : typing.Optional[dt.datetime]
            The date of the file.

        id : typing.Optional[str]
            The Id of the GlobalImage Metadata.

        publisher : typing.Optional[str]
            The Publisher of the file.

        size : typing.Optional[int]
            The size of the file in bytes. Null until assigned by server when marked as 'Available'. Read Only

        thumbnail_size : typing.Optional[int]
            The size of the thumbnail file in bytes. Null until assigned by server when marked as 'Available'. Read Only

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/GlobalImages",
            method="POST",
            params={
                "overridePublisherOrDate": override_publisher_or_date,
            },
            json={
                "CRC": crc,
                "Categories": convert_and_respect_annotation_metadata(
                    object_=categories,
                    annotation=typing.Sequence[GlobalResourcesSharedModelsGlobalImageCategory],
                    direction="write",
                ),
                "Date": date,
                "Description": description,
                "Height": height,
                "Id": id,
                "Name": name,
                "Publisher": publisher,
                "Size": size,
                "State": state,
                "ThumbnailCRC": thumbnail_crc,
                "ThumbnailSize": thumbnail_size,
                "Width": width,
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
                    str,
                    parse_obj_as(
                        type_=str,
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

    def getglobalimage(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GlobalResourcesSharedModelsGlobalImage]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The GlobalImage's id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GlobalResourcesSharedModelsGlobalImage]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/GlobalImages/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GlobalResourcesSharedModelsGlobalImage,
                    parse_obj_as(
                        type_=GlobalResourcesSharedModelsGlobalImage,
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

    def putglobalimage(
        self,
        id_: str,
        *,
        crc: str,
        description: str,
        height: int,
        name: str,
        state: GlobalResourcesSharedModelsGlobalImageState,
        thumbnail_crc: str,
        width: int,
        override_publisher_or_date: typing.Optional[bool] = None,
        categories: typing.Optional[typing.Sequence[GlobalResourcesSharedModelsGlobalImageCategory]] = OMIT,
        date: typing.Optional[dt.datetime] = OMIT,
        id: typing.Optional[str] = OMIT,
        publisher: typing.Optional[str] = OMIT,
        size: typing.Optional[int] = OMIT,
        thumbnail_size: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Update the metadata for an image. Size may not be modified by the client.
                        Set status to 'Available' to publish an image. Both the image and thumbnail must be uploaded.
                        Set status to 'Created' to reset an image's contents and re-upload.
                        A file may only be 'Removed' by the DELETE method.

        Parameters
        ----------
        id_ : str
            The GlobalImage's id.

        crc : str
            The Hash of the file (SHA256, HEX-encoded).

        description : str
            The description of the file.

        height : int
            The height of the file.

        name : str
            The name of the file when downloaded.

        state : GlobalResourcesSharedModelsGlobalImageState
            Indicates the state of this file. Must be 'Created' when created. Read Only.

        thumbnail_crc : str
            The Hash of the thumbnail file (SHA256, HEX-encoded).

        width : int
            The width of the file.

        override_publisher_or_date : typing.Optional[bool]
            Whether to set the publisher and date to the provided values.

        categories : typing.Optional[typing.Sequence[GlobalResourcesSharedModelsGlobalImageCategory]]
            The category of the file.

        date : typing.Optional[dt.datetime]
            The date of the file.

        id : typing.Optional[str]
            The Id of the GlobalImage Metadata.

        publisher : typing.Optional[str]
            The Publisher of the file.

        size : typing.Optional[int]
            The size of the file in bytes. Null until assigned by server when marked as 'Available'. Read Only

        thumbnail_size : typing.Optional[int]
            The size of the thumbnail file in bytes. Null until assigned by server when marked as 'Available'. Read Only

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/GlobalImages/{encode_path_param(id_)}",
            method="PUT",
            params={
                "overridePublisherOrDate": override_publisher_or_date,
            },
            json={
                "CRC": crc,
                "Categories": convert_and_respect_annotation_metadata(
                    object_=categories,
                    annotation=typing.Sequence[GlobalResourcesSharedModelsGlobalImageCategory],
                    direction="write",
                ),
                "Date": date,
                "Description": description,
                "Height": height,
                "Id": id,
                "Name": name,
                "Publisher": publisher,
                "Size": size,
                "State": state,
                "ThumbnailCRC": thumbnail_crc,
                "ThumbnailSize": thumbnail_size,
                "Width": width,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def deletefile(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The GlobalImage's id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/GlobalImages/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getglobalimagecontents(
        self,
        id: str,
        *,
        is_full_image: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SystemObject]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The global image metadata id.

        is_full_image : typing.Optional[bool]
            Indicated whether to download the full image or the thumbnail. Defaults to 'true'.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SystemObject]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/GlobalImages/{encode_path_param(id)}/ImageContents",
            method="GET",
            params={
                "isFullImage": is_full_image,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SystemObject,
                    parse_obj_as(
                        type_=SystemObject,
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

    def putglobalimagecontents(
        self,
        id: str,
        *,
        is_full_image: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SystemObject]:
        """
        Both the image and thumbnail must be uploaded.
                        Set isFullImage = 'True' for Full Image, isFullImage = 'False' for Thumbnail

        Parameters
        ----------
        id : str
            The global image metadata id.

        is_full_image : typing.Optional[bool]
            Indicated whether this is the full image or the thumbnail. Defaults to 'true'.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SystemObject]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/GlobalImages/{encode_path_param(id)}/ImageContents",
            method="PUT",
            params={
                "isFullImage": is_full_image,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SystemObject,
                    parse_obj_as(
                        type_=SystemObject,
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


class AsyncRawGlobalimagesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def getglobalimages(
        self,
        *,
        search: typing.Optional[str] = None,
        category_id: typing.Optional[str] = None,
        publisher: typing.Optional[str] = None,
        include_deleted: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiIPagedResponseGlobalResourcesSharedModelsGlobalImage]:
        """
        No Documentation Found.

        Parameters
        ----------
        search : typing.Optional[str]
            Optional. Searches for matching global images with the matching Category Name, Publisher or Description

        category_id : typing.Optional[str]


        publisher : typing.Optional[str]


        include_deleted : typing.Optional[bool]
            Indicates whether to include GlobalImages marked as removed.

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiIPagedResponseGlobalResourcesSharedModelsGlobalImage]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/GlobalImages",
            method="GET",
            params={
                "search": search,
                "categoryId": category_id,
                "publisher": publisher,
                "includeDeleted": include_deleted,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiIPagedResponseGlobalResourcesSharedModelsGlobalImage,
                    parse_obj_as(
                        type_=ApiIPagedResponseGlobalResourcesSharedModelsGlobalImage,
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

    async def postglobalimage(
        self,
        *,
        crc: str,
        description: str,
        height: int,
        name: str,
        state: GlobalResourcesSharedModelsGlobalImageState,
        thumbnail_crc: str,
        width: int,
        override_publisher_or_date: typing.Optional[bool] = None,
        categories: typing.Optional[typing.Sequence[GlobalResourcesSharedModelsGlobalImageCategory]] = OMIT,
        date: typing.Optional[dt.datetime] = OMIT,
        id: typing.Optional[str] = OMIT,
        publisher: typing.Optional[str] = OMIT,
        size: typing.Optional[int] = OMIT,
        thumbnail_size: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        No Documentation Found.

        Parameters
        ----------
        crc : str
            The Hash of the file (SHA256, HEX-encoded).

        description : str
            The description of the file.

        height : int
            The height of the file.

        name : str
            The name of the file when downloaded.

        state : GlobalResourcesSharedModelsGlobalImageState
            Indicates the state of this file. Must be 'Created' when created. Read Only.

        thumbnail_crc : str
            The Hash of the thumbnail file (SHA256, HEX-encoded).

        width : int
            The width of the file.

        override_publisher_or_date : typing.Optional[bool]
            Whether to set the publisher and date to the provided values.

        categories : typing.Optional[typing.Sequence[GlobalResourcesSharedModelsGlobalImageCategory]]
            The category of the file.

        date : typing.Optional[dt.datetime]
            The date of the file.

        id : typing.Optional[str]
            The Id of the GlobalImage Metadata.

        publisher : typing.Optional[str]
            The Publisher of the file.

        size : typing.Optional[int]
            The size of the file in bytes. Null until assigned by server when marked as 'Available'. Read Only

        thumbnail_size : typing.Optional[int]
            The size of the thumbnail file in bytes. Null until assigned by server when marked as 'Available'. Read Only

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/GlobalImages",
            method="POST",
            params={
                "overridePublisherOrDate": override_publisher_or_date,
            },
            json={
                "CRC": crc,
                "Categories": convert_and_respect_annotation_metadata(
                    object_=categories,
                    annotation=typing.Sequence[GlobalResourcesSharedModelsGlobalImageCategory],
                    direction="write",
                ),
                "Date": date,
                "Description": description,
                "Height": height,
                "Id": id,
                "Name": name,
                "Publisher": publisher,
                "Size": size,
                "State": state,
                "ThumbnailCRC": thumbnail_crc,
                "ThumbnailSize": thumbnail_size,
                "Width": width,
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
                    str,
                    parse_obj_as(
                        type_=str,
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

    async def getglobalimage(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GlobalResourcesSharedModelsGlobalImage]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The GlobalImage's id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GlobalResourcesSharedModelsGlobalImage]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/GlobalImages/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GlobalResourcesSharedModelsGlobalImage,
                    parse_obj_as(
                        type_=GlobalResourcesSharedModelsGlobalImage,
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

    async def putglobalimage(
        self,
        id_: str,
        *,
        crc: str,
        description: str,
        height: int,
        name: str,
        state: GlobalResourcesSharedModelsGlobalImageState,
        thumbnail_crc: str,
        width: int,
        override_publisher_or_date: typing.Optional[bool] = None,
        categories: typing.Optional[typing.Sequence[GlobalResourcesSharedModelsGlobalImageCategory]] = OMIT,
        date: typing.Optional[dt.datetime] = OMIT,
        id: typing.Optional[str] = OMIT,
        publisher: typing.Optional[str] = OMIT,
        size: typing.Optional[int] = OMIT,
        thumbnail_size: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Update the metadata for an image. Size may not be modified by the client.
                        Set status to 'Available' to publish an image. Both the image and thumbnail must be uploaded.
                        Set status to 'Created' to reset an image's contents and re-upload.
                        A file may only be 'Removed' by the DELETE method.

        Parameters
        ----------
        id_ : str
            The GlobalImage's id.

        crc : str
            The Hash of the file (SHA256, HEX-encoded).

        description : str
            The description of the file.

        height : int
            The height of the file.

        name : str
            The name of the file when downloaded.

        state : GlobalResourcesSharedModelsGlobalImageState
            Indicates the state of this file. Must be 'Created' when created. Read Only.

        thumbnail_crc : str
            The Hash of the thumbnail file (SHA256, HEX-encoded).

        width : int
            The width of the file.

        override_publisher_or_date : typing.Optional[bool]
            Whether to set the publisher and date to the provided values.

        categories : typing.Optional[typing.Sequence[GlobalResourcesSharedModelsGlobalImageCategory]]
            The category of the file.

        date : typing.Optional[dt.datetime]
            The date of the file.

        id : typing.Optional[str]
            The Id of the GlobalImage Metadata.

        publisher : typing.Optional[str]
            The Publisher of the file.

        size : typing.Optional[int]
            The size of the file in bytes. Null until assigned by server when marked as 'Available'. Read Only

        thumbnail_size : typing.Optional[int]
            The size of the thumbnail file in bytes. Null until assigned by server when marked as 'Available'. Read Only

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/GlobalImages/{encode_path_param(id_)}",
            method="PUT",
            params={
                "overridePublisherOrDate": override_publisher_or_date,
            },
            json={
                "CRC": crc,
                "Categories": convert_and_respect_annotation_metadata(
                    object_=categories,
                    annotation=typing.Sequence[GlobalResourcesSharedModelsGlobalImageCategory],
                    direction="write",
                ),
                "Date": date,
                "Description": description,
                "Height": height,
                "Id": id,
                "Name": name,
                "Publisher": publisher,
                "Size": size,
                "State": state,
                "ThumbnailCRC": thumbnail_crc,
                "ThumbnailSize": thumbnail_size,
                "Width": width,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def deletefile(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The GlobalImage's id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/GlobalImages/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getglobalimagecontents(
        self,
        id: str,
        *,
        is_full_image: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SystemObject]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The global image metadata id.

        is_full_image : typing.Optional[bool]
            Indicated whether to download the full image or the thumbnail. Defaults to 'true'.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SystemObject]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/GlobalImages/{encode_path_param(id)}/ImageContents",
            method="GET",
            params={
                "isFullImage": is_full_image,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SystemObject,
                    parse_obj_as(
                        type_=SystemObject,
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

    async def putglobalimagecontents(
        self,
        id: str,
        *,
        is_full_image: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SystemObject]:
        """
        Both the image and thumbnail must be uploaded.
                        Set isFullImage = 'True' for Full Image, isFullImage = 'False' for Thumbnail

        Parameters
        ----------
        id : str
            The global image metadata id.

        is_full_image : typing.Optional[bool]
            Indicated whether this is the full image or the thumbnail. Defaults to 'true'.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SystemObject]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/GlobalImages/{encode_path_param(id)}/ImageContents",
            method="PUT",
            params={
                "isFullImage": is_full_image,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SystemObject,
                    parse_obj_as(
                        type_=SystemObject,
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

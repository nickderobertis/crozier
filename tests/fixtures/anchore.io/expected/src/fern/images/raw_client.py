

import contextlib
import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.internal_server_error import InternalServerError
from ..types.anchore_image_list import AnchoreImageList
from ..types.content_files_response import ContentFilesResponse
from ..types.content_java_package_response import ContentJavaPackageResponse
from ..types.content_malware_response import ContentMalwareResponse
from ..types.content_package_response import ContentPackageResponse
from ..types.delete_image_response import DeleteImageResponse
from ..types.delete_image_response_list import DeleteImageResponseList
from ..types.image_source import ImageSource
from ..types.metadata_response import MetadataResponse
from ..types.policy_evaluation_list import PolicyEvaluationList
from ..types.vulnerability_response import VulnerabilityResponse
from .types.get_image_vulnerability_types_by_image_id_response_item import (
    GetImageVulnerabilityTypesByImageIdResponseItem,
)
from .types.get_image_vulnerability_types_response_item import GetImageVulnerabilityTypesResponseItem
from .types.list_images_request_analysis_status import ListImagesRequestAnalysisStatus
from .types.list_images_request_image_status import ListImagesRequestImageStatus


OMIT = typing.cast(typing.Any, ...)


class RawImagesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_images(
        self,
        *,
        history: typing.Optional[bool] = None,
        fulltag: typing.Optional[str] = None,
        image_status: typing.Optional[ListImagesRequestImageStatus] = None,
        analysis_status: typing.Optional[ListImagesRequestAnalysisStatus] = None,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AnchoreImageList]:
        """
        List all images visible to the user

        Parameters
        ----------
        history : typing.Optional[bool]
            Include image history in the response

        fulltag : typing.Optional[str]
            Full docker-pull string to filter results by (e.g. docker.io/library/nginx:latest, or myhost.com:5000/testimages:v1.1.1)

        image_status : typing.Optional[ListImagesRequestImageStatus]
            Filter by image_status value on the record. Default if omitted is 'active'.

        analysis_status : typing.Optional[ListImagesRequestAnalysisStatus]
            Filter by analysis_status value on the record.

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AnchoreImageList]
            successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "images",
            method="GET",
            params={
                "history": history,
                "fulltag": fulltag,
                "image_status": image_status,
                "analysis_status": analysis_status,
            },
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AnchoreImageList,
                    parse_obj_as(
                        type_=AnchoreImageList,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def add_image(
        self,
        *,
        force: typing.Optional[bool] = None,
        autosubscribe: typing.Optional[bool] = None,
        anchore_account: typing.Optional[str] = None,
        annotations: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        digest: typing.Optional[str] = OMIT,
        dockerfile: typing.Optional[str] = OMIT,
        image_type: typing.Optional[str] = OMIT,
        source: typing.Optional[ImageSource] = OMIT,
        tag: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AnchoreImageList]:
        """
        Creates a new analysis task that is executed asynchronously

        Parameters
        ----------
        force : typing.Optional[bool]
            Override any existing entry in the system

        autosubscribe : typing.Optional[bool]
            Instruct engine to automatically begin watching the added tag for updates from registry

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        annotations : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            Annotations to be associated with the added image in key/value form

        created_at : typing.Optional[dt.datetime]
            Optional override of the image creation time, only honored when both tag and digest are also supplied  e.g. 2018-10-17T18:14:00Z. Deprecated in favor of the 'source' field

        digest : typing.Optional[str]
            A digest string for an image, maybe a pull string or just a digest. e.g. nginx@sha256:123 or sha256:abc123. If a pull string, it must have same regisry/repo as the tag field. Deprecated in favor of the 'source' field

        dockerfile : typing.Optional[str]
            Base64 encoded content of the dockerfile for the image, if available. Deprecated in favor of the 'source' field.

        image_type : typing.Optional[str]
            Optional. The type of image this is adding, defaults to "docker". This can be ommitted until multiple image types are supported.

        source : typing.Optional[ImageSource]

        tag : typing.Optional[str]
            Full pullable tag reference for image. e.g. docker.io/nginx:latest. Deprecated in favor of the 'source' field

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AnchoreImageList]
            Successfully added image to analysis queue
        """
        _response = self._client_wrapper.httpx_client.request(
            "images",
            method="POST",
            params={
                "force": force,
                "autosubscribe": autosubscribe,
            },
            json={
                "annotations": annotations,
                "created_at": created_at,
                "digest": digest,
                "dockerfile": dockerfile,
                "image_type": image_type,
                "source": convert_and_respect_annotation_metadata(
                    object_=source, annotation=ImageSource, direction="write"
                ),
                "tag": tag,
            },
            headers={
                "content-type": "application/json",
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AnchoreImageList,
                    parse_obj_as(
                        type_=AnchoreImageList,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_images_async(
        self,
        *,
        image_digests: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        force: typing.Optional[bool] = None,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DeleteImageResponseList]:
        """
        Delete analysis for image digests in the list asynchronously

        Parameters
        ----------
        image_digests : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        force : typing.Optional[bool]

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteImageResponseList]
            successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "images",
            method="DELETE",
            params={
                "imageDigests": image_digests,
                "force": force,
            },
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteImageResponseList,
                    parse_obj_as(
                        type_=DeleteImageResponseList,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_image_by_image_id(
        self,
        image_id: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AnchoreImageList]:
        """
        Parameters
        ----------
        image_id : str

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AnchoreImageList]
            Image lookup success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"images/by_id/{jsonable_encoder(image_id)}",
            method="GET",
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AnchoreImageList,
                    parse_obj_as(
                        type_=AnchoreImageList,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_image_by_image_id(
        self,
        image_id: str,
        *,
        force: typing.Optional[bool] = None,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DeleteImageResponse]:
        """
        Parameters
        ----------
        image_id : str

        force : typing.Optional[bool]

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteImageResponse]
            Image deletion success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"images/by_id/{jsonable_encoder(image_id)}",
            method="DELETE",
            params={
                "force": force,
            },
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteImageResponse,
                    parse_obj_as(
                        type_=DeleteImageResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_image_policy_check_by_image_id(
        self,
        image_id: str,
        *,
        tag: str,
        policy_id: typing.Optional[str] = None,
        detail: typing.Optional[bool] = None,
        history: typing.Optional[bool] = None,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PolicyEvaluationList]:
        """
        Get the policy evaluation for the given image

        Parameters
        ----------
        image_id : str

        tag : str

        policy_id : typing.Optional[str]

        detail : typing.Optional[bool]

        history : typing.Optional[bool]

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PolicyEvaluationList]
            Policy evaluation success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"images/by_id/{jsonable_encoder(image_id)}/check",
            method="GET",
            params={
                "policyId": policy_id,
                "tag": tag,
                "detail": detail,
                "history": history,
            },
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PolicyEvaluationList,
                    parse_obj_as(
                        type_=PolicyEvaluationList,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_image_content_by_imageid(
        self,
        image_id: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[str]]:
        """
        Parameters
        ----------
        image_id : str

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[str]]
            Content of specified type from the image
        """
        _response = self._client_wrapper.httpx_client.request(
            f"images/by_id/{jsonable_encoder(image_id)}/content",
            method="GET",
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_image_content_by_type_image_id_files(
        self,
        image_id: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ContentFilesResponse]:
        """
        Parameters
        ----------
        image_id : str

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ContentFilesResponse]
            Content of specified type from the image
        """
        _response = self._client_wrapper.httpx_client.request(
            f"images/by_id/{jsonable_encoder(image_id)}/content/files",
            method="GET",
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContentFilesResponse,
                    parse_obj_as(
                        type_=ContentFilesResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_image_content_by_type_image_id_javapackage(
        self,
        image_id: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ContentJavaPackageResponse]:
        """
        Parameters
        ----------
        image_id : str

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ContentJavaPackageResponse]
            Content of specified type from the image
        """
        _response = self._client_wrapper.httpx_client.request(
            f"images/by_id/{jsonable_encoder(image_id)}/content/java",
            method="GET",
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContentJavaPackageResponse,
                    parse_obj_as(
                        type_=ContentJavaPackageResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_image_content_by_type_image_id(
        self,
        image_id: str,
        ctype: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ContentPackageResponse]:
        """
        Parameters
        ----------
        image_id : str

        ctype : str

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ContentPackageResponse]
            Content of specified type from the image
        """
        _response = self._client_wrapper.httpx_client.request(
            f"images/by_id/{jsonable_encoder(image_id)}/content/{jsonable_encoder(ctype)}",
            method="GET",
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContentPackageResponse,
                    parse_obj_as(
                        type_=ContentPackageResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_image_vulnerability_types_by_image_id(
        self,
        image_id: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[GetImageVulnerabilityTypesByImageIdResponseItem]]:
        """
        Parameters
        ----------
        image_id : str

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[GetImageVulnerabilityTypesByImageIdResponseItem]]
            Vulnerability listing for the image
        """
        _response = self._client_wrapper.httpx_client.request(
            f"images/by_id/{jsonable_encoder(image_id)}/vuln",
            method="GET",
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GetImageVulnerabilityTypesByImageIdResponseItem],
                    parse_obj_as(
                        type_=typing.List[GetImageVulnerabilityTypesByImageIdResponseItem],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_image_vulnerabilities_by_type_image_id(
        self,
        image_id: str,
        vtype: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[VulnerabilityResponse]:
        """
        Parameters
        ----------
        image_id : str

        vtype : str

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[VulnerabilityResponse]
            Vulnerability listing for the image
        """
        _response = self._client_wrapper.httpx_client.request(
            f"images/by_id/{jsonable_encoder(image_id)}/vuln/{jsonable_encoder(vtype)}",
            method="GET",
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VulnerabilityResponse,
                    parse_obj_as(
                        type_=VulnerabilityResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_image(
        self,
        image_digest: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AnchoreImageList]:
        """
        Parameters
        ----------
        image_digest : str

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AnchoreImageList]
            Image lookup success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"images/{jsonable_encoder(image_digest)}",
            method="GET",
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AnchoreImageList,
                    parse_obj_as(
                        type_=AnchoreImageList,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_image(
        self,
        image_digest: str,
        *,
        force: typing.Optional[bool] = None,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DeleteImageResponse]:
        """
        Parameters
        ----------
        image_digest : str

        force : typing.Optional[bool]

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteImageResponse]
            Image deletion success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"images/{jsonable_encoder(image_digest)}",
            method="DELETE",
            params={
                "force": force,
            },
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteImageResponse,
                    parse_obj_as(
                        type_=DeleteImageResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_image_policy_check(
        self,
        image_digest: str,
        *,
        tag: str,
        policy_id: typing.Optional[str] = None,
        detail: typing.Optional[bool] = None,
        history: typing.Optional[bool] = None,
        interactive: typing.Optional[bool] = None,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PolicyEvaluationList]:
        """
        Get the policy evaluation for the given image

        Parameters
        ----------
        image_digest : str

        tag : str

        policy_id : typing.Optional[str]

        detail : typing.Optional[bool]

        history : typing.Optional[bool]

        interactive : typing.Optional[bool]

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PolicyEvaluationList]
            Policy evaluation success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"images/{jsonable_encoder(image_digest)}/check",
            method="GET",
            params={
                "policyId": policy_id,
                "tag": tag,
                "detail": detail,
                "history": history,
                "interactive": interactive,
            },
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PolicyEvaluationList,
                    parse_obj_as(
                        type_=PolicyEvaluationList,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_image_content(
        self,
        image_digest: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[str]]:
        """
        Parameters
        ----------
        image_digest : str

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[str]]
            Content listing for the image
        """
        _response = self._client_wrapper.httpx_client.request(
            f"images/{jsonable_encoder(image_digest)}/content",
            method="GET",
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_image_content_by_type_files(
        self,
        image_digest: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ContentFilesResponse]:
        """
        Parameters
        ----------
        image_digest : str

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ContentFilesResponse]
            Content of specified type from the image
        """
        _response = self._client_wrapper.httpx_client.request(
            f"images/{jsonable_encoder(image_digest)}/content/files",
            method="GET",
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContentFilesResponse,
                    parse_obj_as(
                        type_=ContentFilesResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_image_content_by_type_javapackage(
        self,
        image_digest: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ContentJavaPackageResponse]:
        """
        Parameters
        ----------
        image_digest : str

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ContentJavaPackageResponse]
            Content of specified type from the image
        """
        _response = self._client_wrapper.httpx_client.request(
            f"images/{jsonable_encoder(image_digest)}/content/java",
            method="GET",
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContentJavaPackageResponse,
                    parse_obj_as(
                        type_=ContentJavaPackageResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_image_content_by_type_malware(
        self,
        image_digest: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ContentMalwareResponse]:
        """
        Parameters
        ----------
        image_digest : str

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ContentMalwareResponse]
            Content of specified type from the image
        """
        _response = self._client_wrapper.httpx_client.request(
            f"images/{jsonable_encoder(image_digest)}/content/malware",
            method="GET",
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContentMalwareResponse,
                    parse_obj_as(
                        type_=ContentMalwareResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_image_content_by_type(
        self,
        image_digest: str,
        ctype: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ContentPackageResponse]:
        """
        Parameters
        ----------
        image_digest : str

        ctype : str

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ContentPackageResponse]
            Content of specified type from the image
        """
        _response = self._client_wrapper.httpx_client.request(
            f"images/{jsonable_encoder(image_digest)}/content/{jsonable_encoder(ctype)}",
            method="GET",
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContentPackageResponse,
                    parse_obj_as(
                        type_=ContentPackageResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_image_metadata(
        self,
        image_digest: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[str]]:
        """
        Parameters
        ----------
        image_digest : str

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[str]]
            Metadata listing for the image
        """
        _response = self._client_wrapper.httpx_client.request(
            f"images/{jsonable_encoder(image_digest)}/metadata",
            method="GET",
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_image_metadata_by_type(
        self,
        image_digest: str,
        mtype: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[MetadataResponse]:
        """
        Parameters
        ----------
        image_digest : str

        mtype : str

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MetadataResponse]
            Metadata of specified type from the image
        """
        _response = self._client_wrapper.httpx_client.request(
            f"images/{jsonable_encoder(image_digest)}/metadata/{jsonable_encoder(mtype)}",
            method="GET",
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MetadataResponse,
                    parse_obj_as(
                        type_=MetadataResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    @contextlib.contextmanager
    def get_image_sbom_native(
        self,
        image_digest: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
        """
        Parameters
        ----------
        image_digest : str

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[HttpResponse[typing.Iterator[bytes]]]
            Image lookup success
        """
        with self._client_wrapper.httpx_client.stream(
            f"images/{jsonable_encoder(image_digest)}/sboms/native",
            method="GET",
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        ) as _response:

            def _stream() -> HttpResponse[typing.Iterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return HttpResponse(
                            response=_response, data=(_chunk for _chunk in _response.iter_bytes(chunk_size=_chunk_size))
                        )
                    _response.read()
                    if _response.status_code == 500:
                        raise InternalServerError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Optional[typing.Any],
                                parse_obj_as(
                                    type_=typing.Optional[typing.Any],
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield _stream()

    def get_image_vulnerability_types(
        self,
        image_digest: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[GetImageVulnerabilityTypesResponseItem]]:
        """
        Parameters
        ----------
        image_digest : str

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[GetImageVulnerabilityTypesResponseItem]]
            Vulnerability listing for the image
        """
        _response = self._client_wrapper.httpx_client.request(
            f"images/{jsonable_encoder(image_digest)}/vuln",
            method="GET",
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GetImageVulnerabilityTypesResponseItem],
                    parse_obj_as(
                        type_=typing.List[GetImageVulnerabilityTypesResponseItem],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_image_vulnerabilities_by_type(
        self,
        image_digest: str,
        vtype: str,
        *,
        force_refresh: typing.Optional[bool] = None,
        vendor_only: typing.Optional[bool] = None,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[VulnerabilityResponse]:
        """
        Parameters
        ----------
        image_digest : str

        vtype : str

        force_refresh : typing.Optional[bool]

        vendor_only : typing.Optional[bool]
            Filter results to include only vulnerabilities that are not marked as invalid by upstream OS vendor data. When set to true, it will filter out all vulnerabilities where `will_not_fix` is False. If false all vulnerabilities are returned regardless of `will_not_fix`

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[VulnerabilityResponse]
            Vulnerability listing for the image
        """
        _response = self._client_wrapper.httpx_client.request(
            f"images/{jsonable_encoder(image_digest)}/vuln/{jsonable_encoder(vtype)}",
            method="GET",
            params={
                "force_refresh": force_refresh,
                "vendor_only": vendor_only,
            },
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VulnerabilityResponse,
                    parse_obj_as(
                        type_=VulnerabilityResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawImagesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_images(
        self,
        *,
        history: typing.Optional[bool] = None,
        fulltag: typing.Optional[str] = None,
        image_status: typing.Optional[ListImagesRequestImageStatus] = None,
        analysis_status: typing.Optional[ListImagesRequestAnalysisStatus] = None,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AnchoreImageList]:
        """
        List all images visible to the user

        Parameters
        ----------
        history : typing.Optional[bool]
            Include image history in the response

        fulltag : typing.Optional[str]
            Full docker-pull string to filter results by (e.g. docker.io/library/nginx:latest, or myhost.com:5000/testimages:v1.1.1)

        image_status : typing.Optional[ListImagesRequestImageStatus]
            Filter by image_status value on the record. Default if omitted is 'active'.

        analysis_status : typing.Optional[ListImagesRequestAnalysisStatus]
            Filter by analysis_status value on the record.

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AnchoreImageList]
            successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "images",
            method="GET",
            params={
                "history": history,
                "fulltag": fulltag,
                "image_status": image_status,
                "analysis_status": analysis_status,
            },
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AnchoreImageList,
                    parse_obj_as(
                        type_=AnchoreImageList,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def add_image(
        self,
        *,
        force: typing.Optional[bool] = None,
        autosubscribe: typing.Optional[bool] = None,
        anchore_account: typing.Optional[str] = None,
        annotations: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        digest: typing.Optional[str] = OMIT,
        dockerfile: typing.Optional[str] = OMIT,
        image_type: typing.Optional[str] = OMIT,
        source: typing.Optional[ImageSource] = OMIT,
        tag: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AnchoreImageList]:
        """
        Creates a new analysis task that is executed asynchronously

        Parameters
        ----------
        force : typing.Optional[bool]
            Override any existing entry in the system

        autosubscribe : typing.Optional[bool]
            Instruct engine to automatically begin watching the added tag for updates from registry

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        annotations : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            Annotations to be associated with the added image in key/value form

        created_at : typing.Optional[dt.datetime]
            Optional override of the image creation time, only honored when both tag and digest are also supplied  e.g. 2018-10-17T18:14:00Z. Deprecated in favor of the 'source' field

        digest : typing.Optional[str]
            A digest string for an image, maybe a pull string or just a digest. e.g. nginx@sha256:123 or sha256:abc123. If a pull string, it must have same regisry/repo as the tag field. Deprecated in favor of the 'source' field

        dockerfile : typing.Optional[str]
            Base64 encoded content of the dockerfile for the image, if available. Deprecated in favor of the 'source' field.

        image_type : typing.Optional[str]
            Optional. The type of image this is adding, defaults to "docker". This can be ommitted until multiple image types are supported.

        source : typing.Optional[ImageSource]

        tag : typing.Optional[str]
            Full pullable tag reference for image. e.g. docker.io/nginx:latest. Deprecated in favor of the 'source' field

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AnchoreImageList]
            Successfully added image to analysis queue
        """
        _response = await self._client_wrapper.httpx_client.request(
            "images",
            method="POST",
            params={
                "force": force,
                "autosubscribe": autosubscribe,
            },
            json={
                "annotations": annotations,
                "created_at": created_at,
                "digest": digest,
                "dockerfile": dockerfile,
                "image_type": image_type,
                "source": convert_and_respect_annotation_metadata(
                    object_=source, annotation=ImageSource, direction="write"
                ),
                "tag": tag,
            },
            headers={
                "content-type": "application/json",
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AnchoreImageList,
                    parse_obj_as(
                        type_=AnchoreImageList,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_images_async(
        self,
        *,
        image_digests: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        force: typing.Optional[bool] = None,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DeleteImageResponseList]:
        """
        Delete analysis for image digests in the list asynchronously

        Parameters
        ----------
        image_digests : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        force : typing.Optional[bool]

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteImageResponseList]
            successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "images",
            method="DELETE",
            params={
                "imageDigests": image_digests,
                "force": force,
            },
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteImageResponseList,
                    parse_obj_as(
                        type_=DeleteImageResponseList,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_image_by_image_id(
        self,
        image_id: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AnchoreImageList]:
        """
        Parameters
        ----------
        image_id : str

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AnchoreImageList]
            Image lookup success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"images/by_id/{jsonable_encoder(image_id)}",
            method="GET",
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AnchoreImageList,
                    parse_obj_as(
                        type_=AnchoreImageList,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_image_by_image_id(
        self,
        image_id: str,
        *,
        force: typing.Optional[bool] = None,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DeleteImageResponse]:
        """
        Parameters
        ----------
        image_id : str

        force : typing.Optional[bool]

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteImageResponse]
            Image deletion success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"images/by_id/{jsonable_encoder(image_id)}",
            method="DELETE",
            params={
                "force": force,
            },
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteImageResponse,
                    parse_obj_as(
                        type_=DeleteImageResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_image_policy_check_by_image_id(
        self,
        image_id: str,
        *,
        tag: str,
        policy_id: typing.Optional[str] = None,
        detail: typing.Optional[bool] = None,
        history: typing.Optional[bool] = None,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PolicyEvaluationList]:
        """
        Get the policy evaluation for the given image

        Parameters
        ----------
        image_id : str

        tag : str

        policy_id : typing.Optional[str]

        detail : typing.Optional[bool]

        history : typing.Optional[bool]

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PolicyEvaluationList]
            Policy evaluation success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"images/by_id/{jsonable_encoder(image_id)}/check",
            method="GET",
            params={
                "policyId": policy_id,
                "tag": tag,
                "detail": detail,
                "history": history,
            },
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PolicyEvaluationList,
                    parse_obj_as(
                        type_=PolicyEvaluationList,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_image_content_by_imageid(
        self,
        image_id: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[str]]:
        """
        Parameters
        ----------
        image_id : str

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[str]]
            Content of specified type from the image
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"images/by_id/{jsonable_encoder(image_id)}/content",
            method="GET",
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_image_content_by_type_image_id_files(
        self,
        image_id: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ContentFilesResponse]:
        """
        Parameters
        ----------
        image_id : str

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ContentFilesResponse]
            Content of specified type from the image
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"images/by_id/{jsonable_encoder(image_id)}/content/files",
            method="GET",
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContentFilesResponse,
                    parse_obj_as(
                        type_=ContentFilesResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_image_content_by_type_image_id_javapackage(
        self,
        image_id: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ContentJavaPackageResponse]:
        """
        Parameters
        ----------
        image_id : str

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ContentJavaPackageResponse]
            Content of specified type from the image
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"images/by_id/{jsonable_encoder(image_id)}/content/java",
            method="GET",
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContentJavaPackageResponse,
                    parse_obj_as(
                        type_=ContentJavaPackageResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_image_content_by_type_image_id(
        self,
        image_id: str,
        ctype: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ContentPackageResponse]:
        """
        Parameters
        ----------
        image_id : str

        ctype : str

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ContentPackageResponse]
            Content of specified type from the image
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"images/by_id/{jsonable_encoder(image_id)}/content/{jsonable_encoder(ctype)}",
            method="GET",
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContentPackageResponse,
                    parse_obj_as(
                        type_=ContentPackageResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_image_vulnerability_types_by_image_id(
        self,
        image_id: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[GetImageVulnerabilityTypesByImageIdResponseItem]]:
        """
        Parameters
        ----------
        image_id : str

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[GetImageVulnerabilityTypesByImageIdResponseItem]]
            Vulnerability listing for the image
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"images/by_id/{jsonable_encoder(image_id)}/vuln",
            method="GET",
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GetImageVulnerabilityTypesByImageIdResponseItem],
                    parse_obj_as(
                        type_=typing.List[GetImageVulnerabilityTypesByImageIdResponseItem],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_image_vulnerabilities_by_type_image_id(
        self,
        image_id: str,
        vtype: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[VulnerabilityResponse]:
        """
        Parameters
        ----------
        image_id : str

        vtype : str

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[VulnerabilityResponse]
            Vulnerability listing for the image
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"images/by_id/{jsonable_encoder(image_id)}/vuln/{jsonable_encoder(vtype)}",
            method="GET",
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VulnerabilityResponse,
                    parse_obj_as(
                        type_=VulnerabilityResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_image(
        self,
        image_digest: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AnchoreImageList]:
        """
        Parameters
        ----------
        image_digest : str

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AnchoreImageList]
            Image lookup success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"images/{jsonable_encoder(image_digest)}",
            method="GET",
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AnchoreImageList,
                    parse_obj_as(
                        type_=AnchoreImageList,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_image(
        self,
        image_digest: str,
        *,
        force: typing.Optional[bool] = None,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DeleteImageResponse]:
        """
        Parameters
        ----------
        image_digest : str

        force : typing.Optional[bool]

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteImageResponse]
            Image deletion success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"images/{jsonable_encoder(image_digest)}",
            method="DELETE",
            params={
                "force": force,
            },
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteImageResponse,
                    parse_obj_as(
                        type_=DeleteImageResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_image_policy_check(
        self,
        image_digest: str,
        *,
        tag: str,
        policy_id: typing.Optional[str] = None,
        detail: typing.Optional[bool] = None,
        history: typing.Optional[bool] = None,
        interactive: typing.Optional[bool] = None,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PolicyEvaluationList]:
        """
        Get the policy evaluation for the given image

        Parameters
        ----------
        image_digest : str

        tag : str

        policy_id : typing.Optional[str]

        detail : typing.Optional[bool]

        history : typing.Optional[bool]

        interactive : typing.Optional[bool]

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PolicyEvaluationList]
            Policy evaluation success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"images/{jsonable_encoder(image_digest)}/check",
            method="GET",
            params={
                "policyId": policy_id,
                "tag": tag,
                "detail": detail,
                "history": history,
                "interactive": interactive,
            },
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PolicyEvaluationList,
                    parse_obj_as(
                        type_=PolicyEvaluationList,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_image_content(
        self,
        image_digest: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[str]]:
        """
        Parameters
        ----------
        image_digest : str

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[str]]
            Content listing for the image
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"images/{jsonable_encoder(image_digest)}/content",
            method="GET",
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_image_content_by_type_files(
        self,
        image_digest: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ContentFilesResponse]:
        """
        Parameters
        ----------
        image_digest : str

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ContentFilesResponse]
            Content of specified type from the image
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"images/{jsonable_encoder(image_digest)}/content/files",
            method="GET",
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContentFilesResponse,
                    parse_obj_as(
                        type_=ContentFilesResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_image_content_by_type_javapackage(
        self,
        image_digest: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ContentJavaPackageResponse]:
        """
        Parameters
        ----------
        image_digest : str

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ContentJavaPackageResponse]
            Content of specified type from the image
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"images/{jsonable_encoder(image_digest)}/content/java",
            method="GET",
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContentJavaPackageResponse,
                    parse_obj_as(
                        type_=ContentJavaPackageResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_image_content_by_type_malware(
        self,
        image_digest: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ContentMalwareResponse]:
        """
        Parameters
        ----------
        image_digest : str

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ContentMalwareResponse]
            Content of specified type from the image
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"images/{jsonable_encoder(image_digest)}/content/malware",
            method="GET",
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContentMalwareResponse,
                    parse_obj_as(
                        type_=ContentMalwareResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_image_content_by_type(
        self,
        image_digest: str,
        ctype: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ContentPackageResponse]:
        """
        Parameters
        ----------
        image_digest : str

        ctype : str

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ContentPackageResponse]
            Content of specified type from the image
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"images/{jsonable_encoder(image_digest)}/content/{jsonable_encoder(ctype)}",
            method="GET",
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContentPackageResponse,
                    parse_obj_as(
                        type_=ContentPackageResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_image_metadata(
        self,
        image_digest: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[str]]:
        """
        Parameters
        ----------
        image_digest : str

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[str]]
            Metadata listing for the image
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"images/{jsonable_encoder(image_digest)}/metadata",
            method="GET",
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_image_metadata_by_type(
        self,
        image_digest: str,
        mtype: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[MetadataResponse]:
        """
        Parameters
        ----------
        image_digest : str

        mtype : str

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MetadataResponse]
            Metadata of specified type from the image
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"images/{jsonable_encoder(image_digest)}/metadata/{jsonable_encoder(mtype)}",
            method="GET",
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MetadataResponse,
                    parse_obj_as(
                        type_=MetadataResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    @contextlib.asynccontextmanager
    async def get_image_sbom_native(
        self,
        image_digest: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
        """
        Parameters
        ----------
        image_digest : str

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]
            Image lookup success
        """
        async with self._client_wrapper.httpx_client.stream(
            f"images/{jsonable_encoder(image_digest)}/sboms/native",
            method="GET",
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        ) as _response:

            async def _stream() -> AsyncHttpResponse[typing.AsyncIterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return AsyncHttpResponse(
                            response=_response,
                            data=(_chunk async for _chunk in _response.aiter_bytes(chunk_size=_chunk_size)),
                        )
                    await _response.aread()
                    if _response.status_code == 500:
                        raise InternalServerError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Optional[typing.Any],
                                parse_obj_as(
                                    type_=typing.Optional[typing.Any],
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield await _stream()

    async def get_image_vulnerability_types(
        self,
        image_digest: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[GetImageVulnerabilityTypesResponseItem]]:
        """
        Parameters
        ----------
        image_digest : str

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[GetImageVulnerabilityTypesResponseItem]]
            Vulnerability listing for the image
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"images/{jsonable_encoder(image_digest)}/vuln",
            method="GET",
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GetImageVulnerabilityTypesResponseItem],
                    parse_obj_as(
                        type_=typing.List[GetImageVulnerabilityTypesResponseItem],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_image_vulnerabilities_by_type(
        self,
        image_digest: str,
        vtype: str,
        *,
        force_refresh: typing.Optional[bool] = None,
        vendor_only: typing.Optional[bool] = None,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[VulnerabilityResponse]:
        """
        Parameters
        ----------
        image_digest : str

        vtype : str

        force_refresh : typing.Optional[bool]

        vendor_only : typing.Optional[bool]
            Filter results to include only vulnerabilities that are not marked as invalid by upstream OS vendor data. When set to true, it will filter out all vulnerabilities where `will_not_fix` is False. If false all vulnerabilities are returned regardless of `will_not_fix`

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[VulnerabilityResponse]
            Vulnerability listing for the image
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"images/{jsonable_encoder(image_digest)}/vuln/{jsonable_encoder(vtype)}",
            method="GET",
            params={
                "force_refresh": force_refresh,
                "vendor_only": vendor_only,
            },
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VulnerabilityResponse,
                    parse_obj_as(
                        type_=VulnerabilityResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

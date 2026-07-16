

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
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
from .raw_client import AsyncRawImagesClient, RawImagesClient
from .types.get_image_vulnerability_types_by_image_id_response_item import (
    GetImageVulnerabilityTypesByImageIdResponseItem,
)
from .types.get_image_vulnerability_types_response_item import GetImageVulnerabilityTypesResponseItem
from .types.list_images_request_analysis_status import ListImagesRequestAnalysisStatus
from .types.list_images_request_image_status import ListImagesRequestImageStatus


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

    def list_images(
        self,
        *,
        history: typing.Optional[bool] = None,
        fulltag: typing.Optional[str] = None,
        image_status: typing.Optional[ListImagesRequestImageStatus] = None,
        analysis_status: typing.Optional[ListImagesRequestAnalysisStatus] = None,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AnchoreImageList:
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
        AnchoreImageList
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.images.list_images()
        """
        _response = self._raw_client.list_images(
            history=history,
            fulltag=fulltag,
            image_status=image_status,
            analysis_status=analysis_status,
            anchore_account=anchore_account,
            request_options=request_options,
        )
        return _response.data

    def add_image(
        self,
        *,
        force: typing.Optional[bool] = None,
        autosubscribe: typing.Optional[bool] = None,
        anchore_account: typing.Optional[str] = None,
        annotations: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        digest: typing.Optional[str] = OMIT,
        dockerfile: typing.Optional[str] = OMIT,
        image_type: typing.Optional[str] = OMIT,
        source: typing.Optional[ImageSource] = OMIT,
        tag: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AnchoreImageList:
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

        annotations : typing.Optional[typing.Dict[str, typing.Any]]
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
        AnchoreImageList
            Successfully added image to analysis queue

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.images.add_image()
        """
        _response = self._raw_client.add_image(
            force=force,
            autosubscribe=autosubscribe,
            anchore_account=anchore_account,
            annotations=annotations,
            created_at=created_at,
            digest=digest,
            dockerfile=dockerfile,
            image_type=image_type,
            source=source,
            tag=tag,
            request_options=request_options,
        )
        return _response.data

    def delete_images_async(
        self,
        *,
        image_digests: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        force: typing.Optional[bool] = None,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeleteImageResponseList:
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
        DeleteImageResponseList
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.images.delete_images_async(
            image_digests=["imageDigests"],
        )
        """
        _response = self._raw_client.delete_images_async(
            image_digests=image_digests, force=force, anchore_account=anchore_account, request_options=request_options
        )
        return _response.data

    def get_image_by_image_id(
        self,
        image_id: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AnchoreImageList:
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
        AnchoreImageList
            Image lookup success

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.images.get_image_by_image_id(
            image_id="imageId",
        )
        """
        _response = self._raw_client.get_image_by_image_id(
            image_id, anchore_account=anchore_account, request_options=request_options
        )
        return _response.data

    def delete_image_by_image_id(
        self,
        image_id: str,
        *,
        force: typing.Optional[bool] = None,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeleteImageResponse:
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
        DeleteImageResponse
            Image deletion success

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.images.delete_image_by_image_id(
            image_id="imageId",
        )
        """
        _response = self._raw_client.delete_image_by_image_id(
            image_id, force=force, anchore_account=anchore_account, request_options=request_options
        )
        return _response.data

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
    ) -> PolicyEvaluationList:
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
        PolicyEvaluationList
            Policy evaluation success

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.images.get_image_policy_check_by_image_id(
            image_id="imageId",
            tag="tag",
        )
        """
        _response = self._raw_client.get_image_policy_check_by_image_id(
            image_id,
            tag=tag,
            policy_id=policy_id,
            detail=detail,
            history=history,
            anchore_account=anchore_account,
            request_options=request_options,
        )
        return _response.data

    def list_image_content_by_imageid(
        self,
        image_id: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
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
        typing.List[str]
            Content of specified type from the image

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.images.list_image_content_by_imageid(
            image_id="imageId",
        )
        """
        _response = self._raw_client.list_image_content_by_imageid(
            image_id, anchore_account=anchore_account, request_options=request_options
        )
        return _response.data

    def get_image_content_by_type_image_id_files(
        self,
        image_id: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContentFilesResponse:
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
        ContentFilesResponse
            Content of specified type from the image

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.images.get_image_content_by_type_image_id_files(
            image_id="imageId",
        )
        """
        _response = self._raw_client.get_image_content_by_type_image_id_files(
            image_id, anchore_account=anchore_account, request_options=request_options
        )
        return _response.data

    def get_image_content_by_type_image_id_javapackage(
        self,
        image_id: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContentJavaPackageResponse:
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
        ContentJavaPackageResponse
            Content of specified type from the image

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.images.get_image_content_by_type_image_id_javapackage(
            image_id="imageId",
        )
        """
        _response = self._raw_client.get_image_content_by_type_image_id_javapackage(
            image_id, anchore_account=anchore_account, request_options=request_options
        )
        return _response.data

    def get_image_content_by_type_image_id(
        self,
        image_id: str,
        ctype: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContentPackageResponse:
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
        ContentPackageResponse
            Content of specified type from the image

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.images.get_image_content_by_type_image_id(
            image_id="imageId",
            ctype="ctype",
        )
        """
        _response = self._raw_client.get_image_content_by_type_image_id(
            image_id, ctype, anchore_account=anchore_account, request_options=request_options
        )
        return _response.data

    def get_image_vulnerability_types_by_image_id(
        self,
        image_id: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[GetImageVulnerabilityTypesByImageIdResponseItem]:
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
        typing.List[GetImageVulnerabilityTypesByImageIdResponseItem]
            Vulnerability listing for the image

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.images.get_image_vulnerability_types_by_image_id(
            image_id="imageId",
        )
        """
        _response = self._raw_client.get_image_vulnerability_types_by_image_id(
            image_id, anchore_account=anchore_account, request_options=request_options
        )
        return _response.data

    def get_image_vulnerabilities_by_type_image_id(
        self,
        image_id: str,
        vtype: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VulnerabilityResponse:
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
        VulnerabilityResponse
            Vulnerability listing for the image

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.images.get_image_vulnerabilities_by_type_image_id(
            image_id="imageId",
            vtype="vtype",
        )
        """
        _response = self._raw_client.get_image_vulnerabilities_by_type_image_id(
            image_id, vtype, anchore_account=anchore_account, request_options=request_options
        )
        return _response.data

    def get_image(
        self,
        image_digest: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AnchoreImageList:
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
        AnchoreImageList
            Image lookup success

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.images.get_image(
            image_digest="imageDigest",
        )
        """
        _response = self._raw_client.get_image(
            image_digest, anchore_account=anchore_account, request_options=request_options
        )
        return _response.data

    def delete_image(
        self,
        image_digest: str,
        *,
        force: typing.Optional[bool] = None,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeleteImageResponse:
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
        DeleteImageResponse
            Image deletion success

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.images.delete_image(
            image_digest="imageDigest",
        )
        """
        _response = self._raw_client.delete_image(
            image_digest, force=force, anchore_account=anchore_account, request_options=request_options
        )
        return _response.data

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
    ) -> PolicyEvaluationList:
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
        PolicyEvaluationList
            Policy evaluation success

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.images.get_image_policy_check(
            image_digest="imageDigest",
            tag="tag",
        )
        """
        _response = self._raw_client.get_image_policy_check(
            image_digest,
            tag=tag,
            policy_id=policy_id,
            detail=detail,
            history=history,
            interactive=interactive,
            anchore_account=anchore_account,
            request_options=request_options,
        )
        return _response.data

    def list_image_content(
        self,
        image_digest: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
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
        typing.List[str]
            Content listing for the image

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.images.list_image_content(
            image_digest="imageDigest",
        )
        """
        _response = self._raw_client.list_image_content(
            image_digest, anchore_account=anchore_account, request_options=request_options
        )
        return _response.data

    def get_image_content_by_type_files(
        self,
        image_digest: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContentFilesResponse:
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
        ContentFilesResponse
            Content of specified type from the image

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.images.get_image_content_by_type_files(
            image_digest="imageDigest",
        )
        """
        _response = self._raw_client.get_image_content_by_type_files(
            image_digest, anchore_account=anchore_account, request_options=request_options
        )
        return _response.data

    def get_image_content_by_type_javapackage(
        self,
        image_digest: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContentJavaPackageResponse:
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
        ContentJavaPackageResponse
            Content of specified type from the image

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.images.get_image_content_by_type_javapackage(
            image_digest="imageDigest",
        )
        """
        _response = self._raw_client.get_image_content_by_type_javapackage(
            image_digest, anchore_account=anchore_account, request_options=request_options
        )
        return _response.data

    def get_image_content_by_type_malware(
        self,
        image_digest: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContentMalwareResponse:
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
        ContentMalwareResponse
            Content of specified type from the image

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.images.get_image_content_by_type_malware(
            image_digest="imageDigest",
        )
        """
        _response = self._raw_client.get_image_content_by_type_malware(
            image_digest, anchore_account=anchore_account, request_options=request_options
        )
        return _response.data

    def get_image_content_by_type(
        self,
        image_digest: str,
        ctype: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContentPackageResponse:
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
        ContentPackageResponse
            Content of specified type from the image

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.images.get_image_content_by_type(
            image_digest="imageDigest",
            ctype="ctype",
        )
        """
        _response = self._raw_client.get_image_content_by_type(
            image_digest, ctype, anchore_account=anchore_account, request_options=request_options
        )
        return _response.data

    def list_image_metadata(
        self,
        image_digest: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
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
        typing.List[str]
            Metadata listing for the image

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.images.list_image_metadata(
            image_digest="imageDigest",
        )
        """
        _response = self._raw_client.list_image_metadata(
            image_digest, anchore_account=anchore_account, request_options=request_options
        )
        return _response.data

    def get_image_metadata_by_type(
        self,
        image_digest: str,
        mtype: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MetadataResponse:
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
        MetadataResponse
            Metadata of specified type from the image

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.images.get_image_metadata_by_type(
            image_digest="imageDigest",
            mtype="mtype",
        )
        """
        _response = self._raw_client.get_image_metadata_by_type(
            image_digest, mtype, anchore_account=anchore_account, request_options=request_options
        )
        return _response.data

    def get_image_sbom_native(
        self,
        image_digest: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
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
        typing.Iterator[bytes]
            Image lookup success

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.images.get_image_sbom_native(
            image_digest="imageDigest",
        )
        """
        with self._raw_client.get_image_sbom_native(
            image_digest, anchore_account=anchore_account, request_options=request_options
        ) as r:
            yield from r.data

    def get_image_vulnerability_types(
        self,
        image_digest: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[GetImageVulnerabilityTypesResponseItem]:
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
        typing.List[GetImageVulnerabilityTypesResponseItem]
            Vulnerability listing for the image

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.images.get_image_vulnerability_types(
            image_digest="imageDigest",
        )
        """
        _response = self._raw_client.get_image_vulnerability_types(
            image_digest, anchore_account=anchore_account, request_options=request_options
        )
        return _response.data

    def get_image_vulnerabilities_by_type(
        self,
        image_digest: str,
        vtype: str,
        *,
        force_refresh: typing.Optional[bool] = None,
        vendor_only: typing.Optional[bool] = None,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VulnerabilityResponse:
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
        VulnerabilityResponse
            Vulnerability listing for the image

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.images.get_image_vulnerabilities_by_type(
            image_digest="imageDigest",
            vtype="vtype",
        )
        """
        _response = self._raw_client.get_image_vulnerabilities_by_type(
            image_digest,
            vtype,
            force_refresh=force_refresh,
            vendor_only=vendor_only,
            anchore_account=anchore_account,
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

    async def list_images(
        self,
        *,
        history: typing.Optional[bool] = None,
        fulltag: typing.Optional[str] = None,
        image_status: typing.Optional[ListImagesRequestImageStatus] = None,
        analysis_status: typing.Optional[ListImagesRequestAnalysisStatus] = None,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AnchoreImageList:
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
        AnchoreImageList
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.images.list_images()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_images(
            history=history,
            fulltag=fulltag,
            image_status=image_status,
            analysis_status=analysis_status,
            anchore_account=anchore_account,
            request_options=request_options,
        )
        return _response.data

    async def add_image(
        self,
        *,
        force: typing.Optional[bool] = None,
        autosubscribe: typing.Optional[bool] = None,
        anchore_account: typing.Optional[str] = None,
        annotations: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        digest: typing.Optional[str] = OMIT,
        dockerfile: typing.Optional[str] = OMIT,
        image_type: typing.Optional[str] = OMIT,
        source: typing.Optional[ImageSource] = OMIT,
        tag: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AnchoreImageList:
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

        annotations : typing.Optional[typing.Dict[str, typing.Any]]
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
        AnchoreImageList
            Successfully added image to analysis queue

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.images.add_image()


        asyncio.run(main())
        """
        _response = await self._raw_client.add_image(
            force=force,
            autosubscribe=autosubscribe,
            anchore_account=anchore_account,
            annotations=annotations,
            created_at=created_at,
            digest=digest,
            dockerfile=dockerfile,
            image_type=image_type,
            source=source,
            tag=tag,
            request_options=request_options,
        )
        return _response.data

    async def delete_images_async(
        self,
        *,
        image_digests: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        force: typing.Optional[bool] = None,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeleteImageResponseList:
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
        DeleteImageResponseList
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.images.delete_images_async(
                image_digests=["imageDigests"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_images_async(
            image_digests=image_digests, force=force, anchore_account=anchore_account, request_options=request_options
        )
        return _response.data

    async def get_image_by_image_id(
        self,
        image_id: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AnchoreImageList:
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
        AnchoreImageList
            Image lookup success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.images.get_image_by_image_id(
                image_id="imageId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_image_by_image_id(
            image_id, anchore_account=anchore_account, request_options=request_options
        )
        return _response.data

    async def delete_image_by_image_id(
        self,
        image_id: str,
        *,
        force: typing.Optional[bool] = None,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeleteImageResponse:
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
        DeleteImageResponse
            Image deletion success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.images.delete_image_by_image_id(
                image_id="imageId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_image_by_image_id(
            image_id, force=force, anchore_account=anchore_account, request_options=request_options
        )
        return _response.data

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
    ) -> PolicyEvaluationList:
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
        PolicyEvaluationList
            Policy evaluation success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.images.get_image_policy_check_by_image_id(
                image_id="imageId",
                tag="tag",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_image_policy_check_by_image_id(
            image_id,
            tag=tag,
            policy_id=policy_id,
            detail=detail,
            history=history,
            anchore_account=anchore_account,
            request_options=request_options,
        )
        return _response.data

    async def list_image_content_by_imageid(
        self,
        image_id: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
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
        typing.List[str]
            Content of specified type from the image

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.images.list_image_content_by_imageid(
                image_id="imageId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_image_content_by_imageid(
            image_id, anchore_account=anchore_account, request_options=request_options
        )
        return _response.data

    async def get_image_content_by_type_image_id_files(
        self,
        image_id: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContentFilesResponse:
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
        ContentFilesResponse
            Content of specified type from the image

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.images.get_image_content_by_type_image_id_files(
                image_id="imageId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_image_content_by_type_image_id_files(
            image_id, anchore_account=anchore_account, request_options=request_options
        )
        return _response.data

    async def get_image_content_by_type_image_id_javapackage(
        self,
        image_id: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContentJavaPackageResponse:
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
        ContentJavaPackageResponse
            Content of specified type from the image

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.images.get_image_content_by_type_image_id_javapackage(
                image_id="imageId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_image_content_by_type_image_id_javapackage(
            image_id, anchore_account=anchore_account, request_options=request_options
        )
        return _response.data

    async def get_image_content_by_type_image_id(
        self,
        image_id: str,
        ctype: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContentPackageResponse:
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
        ContentPackageResponse
            Content of specified type from the image

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.images.get_image_content_by_type_image_id(
                image_id="imageId",
                ctype="ctype",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_image_content_by_type_image_id(
            image_id, ctype, anchore_account=anchore_account, request_options=request_options
        )
        return _response.data

    async def get_image_vulnerability_types_by_image_id(
        self,
        image_id: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[GetImageVulnerabilityTypesByImageIdResponseItem]:
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
        typing.List[GetImageVulnerabilityTypesByImageIdResponseItem]
            Vulnerability listing for the image

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.images.get_image_vulnerability_types_by_image_id(
                image_id="imageId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_image_vulnerability_types_by_image_id(
            image_id, anchore_account=anchore_account, request_options=request_options
        )
        return _response.data

    async def get_image_vulnerabilities_by_type_image_id(
        self,
        image_id: str,
        vtype: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VulnerabilityResponse:
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
        VulnerabilityResponse
            Vulnerability listing for the image

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.images.get_image_vulnerabilities_by_type_image_id(
                image_id="imageId",
                vtype="vtype",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_image_vulnerabilities_by_type_image_id(
            image_id, vtype, anchore_account=anchore_account, request_options=request_options
        )
        return _response.data

    async def get_image(
        self,
        image_digest: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AnchoreImageList:
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
        AnchoreImageList
            Image lookup success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.images.get_image(
                image_digest="imageDigest",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_image(
            image_digest, anchore_account=anchore_account, request_options=request_options
        )
        return _response.data

    async def delete_image(
        self,
        image_digest: str,
        *,
        force: typing.Optional[bool] = None,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeleteImageResponse:
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
        DeleteImageResponse
            Image deletion success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.images.delete_image(
                image_digest="imageDigest",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_image(
            image_digest, force=force, anchore_account=anchore_account, request_options=request_options
        )
        return _response.data

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
    ) -> PolicyEvaluationList:
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
        PolicyEvaluationList
            Policy evaluation success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.images.get_image_policy_check(
                image_digest="imageDigest",
                tag="tag",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_image_policy_check(
            image_digest,
            tag=tag,
            policy_id=policy_id,
            detail=detail,
            history=history,
            interactive=interactive,
            anchore_account=anchore_account,
            request_options=request_options,
        )
        return _response.data

    async def list_image_content(
        self,
        image_digest: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
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
        typing.List[str]
            Content listing for the image

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.images.list_image_content(
                image_digest="imageDigest",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_image_content(
            image_digest, anchore_account=anchore_account, request_options=request_options
        )
        return _response.data

    async def get_image_content_by_type_files(
        self,
        image_digest: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContentFilesResponse:
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
        ContentFilesResponse
            Content of specified type from the image

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.images.get_image_content_by_type_files(
                image_digest="imageDigest",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_image_content_by_type_files(
            image_digest, anchore_account=anchore_account, request_options=request_options
        )
        return _response.data

    async def get_image_content_by_type_javapackage(
        self,
        image_digest: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContentJavaPackageResponse:
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
        ContentJavaPackageResponse
            Content of specified type from the image

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.images.get_image_content_by_type_javapackage(
                image_digest="imageDigest",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_image_content_by_type_javapackage(
            image_digest, anchore_account=anchore_account, request_options=request_options
        )
        return _response.data

    async def get_image_content_by_type_malware(
        self,
        image_digest: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContentMalwareResponse:
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
        ContentMalwareResponse
            Content of specified type from the image

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.images.get_image_content_by_type_malware(
                image_digest="imageDigest",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_image_content_by_type_malware(
            image_digest, anchore_account=anchore_account, request_options=request_options
        )
        return _response.data

    async def get_image_content_by_type(
        self,
        image_digest: str,
        ctype: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContentPackageResponse:
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
        ContentPackageResponse
            Content of specified type from the image

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.images.get_image_content_by_type(
                image_digest="imageDigest",
                ctype="ctype",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_image_content_by_type(
            image_digest, ctype, anchore_account=anchore_account, request_options=request_options
        )
        return _response.data

    async def list_image_metadata(
        self,
        image_digest: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
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
        typing.List[str]
            Metadata listing for the image

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.images.list_image_metadata(
                image_digest="imageDigest",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_image_metadata(
            image_digest, anchore_account=anchore_account, request_options=request_options
        )
        return _response.data

    async def get_image_metadata_by_type(
        self,
        image_digest: str,
        mtype: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MetadataResponse:
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
        MetadataResponse
            Metadata of specified type from the image

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.images.get_image_metadata_by_type(
                image_digest="imageDigest",
                mtype="mtype",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_image_metadata_by_type(
            image_digest, mtype, anchore_account=anchore_account, request_options=request_options
        )
        return _response.data

    async def get_image_sbom_native(
        self,
        image_digest: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
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
        typing.AsyncIterator[bytes]
            Image lookup success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.images.get_image_sbom_native(
                image_digest="imageDigest",
            )


        asyncio.run(main())
        """
        async with self._raw_client.get_image_sbom_native(
            image_digest, anchore_account=anchore_account, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def get_image_vulnerability_types(
        self,
        image_digest: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[GetImageVulnerabilityTypesResponseItem]:
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
        typing.List[GetImageVulnerabilityTypesResponseItem]
            Vulnerability listing for the image

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.images.get_image_vulnerability_types(
                image_digest="imageDigest",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_image_vulnerability_types(
            image_digest, anchore_account=anchore_account, request_options=request_options
        )
        return _response.data

    async def get_image_vulnerabilities_by_type(
        self,
        image_digest: str,
        vtype: str,
        *,
        force_refresh: typing.Optional[bool] = None,
        vendor_only: typing.Optional[bool] = None,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VulnerabilityResponse:
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
        VulnerabilityResponse
            Vulnerability listing for the image

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.images.get_image_vulnerabilities_by_type(
                image_digest="imageDigest",
                vtype="vtype",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_image_vulnerabilities_by_type(
            image_digest,
            vtype,
            force_refresh=force_refresh,
            vendor_only=vendor_only,
            anchore_account=anchore_account,
            request_options=request_options,
        )
        return _response.data

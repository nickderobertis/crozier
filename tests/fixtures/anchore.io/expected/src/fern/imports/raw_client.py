

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
from ..types.image_import_content_response import ImageImportContentResponse
from ..types.image_import_operation import ImageImportOperation
from ..types.image_imports import ImageImports
from ..types.import_content_digest_list import ImportContentDigestList
from ..types.import_descriptor import ImportDescriptor
from ..types.import_distribution import ImportDistribution
from ..types.import_package import ImportPackage
from ..types.import_package_relationship import ImportPackageRelationship
from ..types.import_schema import ImportSchema
from ..types.import_source import ImportSource


OMIT = typing.cast(typing.Any, ...)


class RawImportsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_operations(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[ImageImports]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ImageImports]
            success
        """
        _response = self._client_wrapper.httpx_client.request(
            "imports/images",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ImageImports,
                    parse_obj_as(
                        type_=ImageImports,
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

    def create_operation(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ImageImportOperation]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ImageImportOperation]
            success
        """
        _response = self._client_wrapper.httpx_client.request(
            "imports/images",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ImageImportOperation,
                    parse_obj_as(
                        type_=ImageImportOperation,
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

    def get_operation(
        self, operation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ImageImportOperation]:
        """
        Parameters
        ----------
        operation_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ImageImportOperation]
            success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"imports/images/{jsonable_encoder(operation_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ImageImportOperation,
                    parse_obj_as(
                        type_=ImageImportOperation,
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

    def invalidate_operation(
        self, operation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ImageImportOperation]:
        """
        Parameters
        ----------
        operation_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ImageImportOperation]
            success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"imports/images/{jsonable_encoder(operation_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ImageImportOperation,
                    parse_obj_as(
                        type_=ImageImportOperation,
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

    def list_import_dockerfiles(
        self, operation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ImportContentDigestList]:
        """
        Parameters
        ----------
        operation_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ImportContentDigestList]
            success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"imports/images/{jsonable_encoder(operation_id)}/dockerfile",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ImportContentDigestList,
                    parse_obj_as(
                        type_=ImportContentDigestList,
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

    def import_image_dockerfile(
        self, operation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ImageImportContentResponse]:
        """
        Parameters
        ----------
        operation_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ImageImportContentResponse]
            success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"imports/images/{jsonable_encoder(operation_id)}/dockerfile",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ImageImportContentResponse,
                    parse_obj_as(
                        type_=ImageImportContentResponse,
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

    def list_import_image_configs(
        self, operation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ImportContentDigestList]:
        """
        Parameters
        ----------
        operation_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ImportContentDigestList]
            success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"imports/images/{jsonable_encoder(operation_id)}/image_config",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ImportContentDigestList,
                    parse_obj_as(
                        type_=ImportContentDigestList,
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

    def import_image_config(
        self,
        operation_id: str,
        *,
        request: typing.Dict[str, typing.Optional[typing.Any]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ImageImportContentResponse]:
        """
        Parameters
        ----------
        operation_id : str

        request : typing.Dict[str, typing.Optional[typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ImageImportContentResponse]
            success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"imports/images/{jsonable_encoder(operation_id)}/image_config",
            method="POST",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ImageImportContentResponse,
                    parse_obj_as(
                        type_=ImageImportContentResponse,
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

    def list_import_image_manifests(
        self, operation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ImportContentDigestList]:
        """
        Parameters
        ----------
        operation_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ImportContentDigestList]
            success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"imports/images/{jsonable_encoder(operation_id)}/manifest",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ImportContentDigestList,
                    parse_obj_as(
                        type_=ImportContentDigestList,
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

    def import_image_manifest(
        self,
        operation_id: str,
        *,
        request: typing.Dict[str, typing.Optional[typing.Any]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ImageImportContentResponse]:
        """
        Parameters
        ----------
        operation_id : str

        request : typing.Dict[str, typing.Optional[typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ImageImportContentResponse]
            success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"imports/images/{jsonable_encoder(operation_id)}/manifest",
            method="POST",
            json=request,
            headers={
                "content-type": "application/vnd.docker.distribution.manifest.v1+json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ImageImportContentResponse,
                    parse_obj_as(
                        type_=ImageImportContentResponse,
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

    def list_import_packages(
        self, operation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ImportContentDigestList]:
        """
        Parameters
        ----------
        operation_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ImportContentDigestList]
            success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"imports/images/{jsonable_encoder(operation_id)}/packages",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ImportContentDigestList,
                    parse_obj_as(
                        type_=ImportContentDigestList,
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

    def import_image_packages(
        self,
        operation_id: str,
        *,
        artifacts: typing.Sequence[ImportPackage],
        distro: ImportDistribution,
        source: ImportSource,
        artifact_relationships: typing.Optional[typing.Sequence[ImportPackageRelationship]] = OMIT,
        descriptor: typing.Optional[ImportDescriptor] = OMIT,
        schema: typing.Optional[ImportSchema] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ImageImportContentResponse]:
        """
        Parameters
        ----------
        operation_id : str

        artifacts : typing.Sequence[ImportPackage]

        distro : ImportDistribution

        source : ImportSource

        artifact_relationships : typing.Optional[typing.Sequence[ImportPackageRelationship]]

        descriptor : typing.Optional[ImportDescriptor]

        schema : typing.Optional[ImportSchema]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ImageImportContentResponse]
            success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"imports/images/{jsonable_encoder(operation_id)}/packages",
            method="POST",
            json={
                "artifactRelationships": convert_and_respect_annotation_metadata(
                    object_=artifact_relationships,
                    annotation=typing.Sequence[ImportPackageRelationship],
                    direction="write",
                ),
                "artifacts": convert_and_respect_annotation_metadata(
                    object_=artifacts, annotation=typing.Sequence[ImportPackage], direction="write"
                ),
                "descriptor": convert_and_respect_annotation_metadata(
                    object_=descriptor, annotation=ImportDescriptor, direction="write"
                ),
                "distro": convert_and_respect_annotation_metadata(
                    object_=distro, annotation=ImportDistribution, direction="write"
                ),
                "schema": convert_and_respect_annotation_metadata(
                    object_=schema, annotation=ImportSchema, direction="write"
                ),
                "source": convert_and_respect_annotation_metadata(
                    object_=source, annotation=ImportSource, direction="write"
                ),
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
                    ImageImportContentResponse,
                    parse_obj_as(
                        type_=ImageImportContentResponse,
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

    def list_import_parent_manifests(
        self, operation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ImportContentDigestList]:
        """
        Parameters
        ----------
        operation_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ImportContentDigestList]
            success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"imports/images/{jsonable_encoder(operation_id)}/parent_manifest",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ImportContentDigestList,
                    parse_obj_as(
                        type_=ImportContentDigestList,
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

    def import_image_parent_manifest(
        self,
        operation_id: str,
        *,
        request: typing.Dict[str, typing.Optional[typing.Any]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ImageImportContentResponse]:
        """
        Parameters
        ----------
        operation_id : str

        request : typing.Dict[str, typing.Optional[typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ImageImportContentResponse]
            success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"imports/images/{jsonable_encoder(operation_id)}/parent_manifest",
            method="POST",
            json=request,
            headers={
                "content-type": "application/vnd.docker.distribution.manifest.list.v2+json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ImageImportContentResponse,
                    parse_obj_as(
                        type_=ImageImportContentResponse,
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


class AsyncRawImportsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_operations(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ImageImports]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ImageImports]
            success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "imports/images",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ImageImports,
                    parse_obj_as(
                        type_=ImageImports,
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

    async def create_operation(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ImageImportOperation]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ImageImportOperation]
            success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "imports/images",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ImageImportOperation,
                    parse_obj_as(
                        type_=ImageImportOperation,
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

    async def get_operation(
        self, operation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ImageImportOperation]:
        """
        Parameters
        ----------
        operation_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ImageImportOperation]
            success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"imports/images/{jsonable_encoder(operation_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ImageImportOperation,
                    parse_obj_as(
                        type_=ImageImportOperation,
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

    async def invalidate_operation(
        self, operation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ImageImportOperation]:
        """
        Parameters
        ----------
        operation_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ImageImportOperation]
            success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"imports/images/{jsonable_encoder(operation_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ImageImportOperation,
                    parse_obj_as(
                        type_=ImageImportOperation,
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

    async def list_import_dockerfiles(
        self, operation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ImportContentDigestList]:
        """
        Parameters
        ----------
        operation_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ImportContentDigestList]
            success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"imports/images/{jsonable_encoder(operation_id)}/dockerfile",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ImportContentDigestList,
                    parse_obj_as(
                        type_=ImportContentDigestList,
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

    async def import_image_dockerfile(
        self, operation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ImageImportContentResponse]:
        """
        Parameters
        ----------
        operation_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ImageImportContentResponse]
            success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"imports/images/{jsonable_encoder(operation_id)}/dockerfile",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ImageImportContentResponse,
                    parse_obj_as(
                        type_=ImageImportContentResponse,
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

    async def list_import_image_configs(
        self, operation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ImportContentDigestList]:
        """
        Parameters
        ----------
        operation_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ImportContentDigestList]
            success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"imports/images/{jsonable_encoder(operation_id)}/image_config",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ImportContentDigestList,
                    parse_obj_as(
                        type_=ImportContentDigestList,
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

    async def import_image_config(
        self,
        operation_id: str,
        *,
        request: typing.Dict[str, typing.Optional[typing.Any]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ImageImportContentResponse]:
        """
        Parameters
        ----------
        operation_id : str

        request : typing.Dict[str, typing.Optional[typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ImageImportContentResponse]
            success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"imports/images/{jsonable_encoder(operation_id)}/image_config",
            method="POST",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ImageImportContentResponse,
                    parse_obj_as(
                        type_=ImageImportContentResponse,
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

    async def list_import_image_manifests(
        self, operation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ImportContentDigestList]:
        """
        Parameters
        ----------
        operation_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ImportContentDigestList]
            success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"imports/images/{jsonable_encoder(operation_id)}/manifest",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ImportContentDigestList,
                    parse_obj_as(
                        type_=ImportContentDigestList,
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

    async def import_image_manifest(
        self,
        operation_id: str,
        *,
        request: typing.Dict[str, typing.Optional[typing.Any]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ImageImportContentResponse]:
        """
        Parameters
        ----------
        operation_id : str

        request : typing.Dict[str, typing.Optional[typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ImageImportContentResponse]
            success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"imports/images/{jsonable_encoder(operation_id)}/manifest",
            method="POST",
            json=request,
            headers={
                "content-type": "application/vnd.docker.distribution.manifest.v1+json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ImageImportContentResponse,
                    parse_obj_as(
                        type_=ImageImportContentResponse,
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

    async def list_import_packages(
        self, operation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ImportContentDigestList]:
        """
        Parameters
        ----------
        operation_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ImportContentDigestList]
            success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"imports/images/{jsonable_encoder(operation_id)}/packages",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ImportContentDigestList,
                    parse_obj_as(
                        type_=ImportContentDigestList,
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

    async def import_image_packages(
        self,
        operation_id: str,
        *,
        artifacts: typing.Sequence[ImportPackage],
        distro: ImportDistribution,
        source: ImportSource,
        artifact_relationships: typing.Optional[typing.Sequence[ImportPackageRelationship]] = OMIT,
        descriptor: typing.Optional[ImportDescriptor] = OMIT,
        schema: typing.Optional[ImportSchema] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ImageImportContentResponse]:
        """
        Parameters
        ----------
        operation_id : str

        artifacts : typing.Sequence[ImportPackage]

        distro : ImportDistribution

        source : ImportSource

        artifact_relationships : typing.Optional[typing.Sequence[ImportPackageRelationship]]

        descriptor : typing.Optional[ImportDescriptor]

        schema : typing.Optional[ImportSchema]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ImageImportContentResponse]
            success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"imports/images/{jsonable_encoder(operation_id)}/packages",
            method="POST",
            json={
                "artifactRelationships": convert_and_respect_annotation_metadata(
                    object_=artifact_relationships,
                    annotation=typing.Sequence[ImportPackageRelationship],
                    direction="write",
                ),
                "artifacts": convert_and_respect_annotation_metadata(
                    object_=artifacts, annotation=typing.Sequence[ImportPackage], direction="write"
                ),
                "descriptor": convert_and_respect_annotation_metadata(
                    object_=descriptor, annotation=ImportDescriptor, direction="write"
                ),
                "distro": convert_and_respect_annotation_metadata(
                    object_=distro, annotation=ImportDistribution, direction="write"
                ),
                "schema": convert_and_respect_annotation_metadata(
                    object_=schema, annotation=ImportSchema, direction="write"
                ),
                "source": convert_and_respect_annotation_metadata(
                    object_=source, annotation=ImportSource, direction="write"
                ),
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
                    ImageImportContentResponse,
                    parse_obj_as(
                        type_=ImageImportContentResponse,
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

    async def list_import_parent_manifests(
        self, operation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ImportContentDigestList]:
        """
        Parameters
        ----------
        operation_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ImportContentDigestList]
            success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"imports/images/{jsonable_encoder(operation_id)}/parent_manifest",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ImportContentDigestList,
                    parse_obj_as(
                        type_=ImportContentDigestList,
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

    async def import_image_parent_manifest(
        self,
        operation_id: str,
        *,
        request: typing.Dict[str, typing.Optional[typing.Any]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ImageImportContentResponse]:
        """
        Parameters
        ----------
        operation_id : str

        request : typing.Dict[str, typing.Optional[typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ImageImportContentResponse]
            success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"imports/images/{jsonable_encoder(operation_id)}/parent_manifest",
            method="POST",
            json=request,
            headers={
                "content-type": "application/vnd.docker.distribution.manifest.list.v2+json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ImageImportContentResponse,
                    parse_obj_as(
                        type_=ImageImportContentResponse,
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

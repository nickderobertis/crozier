

import contextlib
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.conflict_error import ConflictError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..types.artifact_description import ArtifactDescription
from ..types.artifact_id import ArtifactId
from ..types.artifact_name import ArtifactName
from ..types.artifact_reference import ArtifactReference
from ..types.artifact_state import ArtifactState
from ..types.encoded_artifact_description import EncodedArtifactDescription
from ..types.encoded_artifact_name import EncodedArtifactName
from ..types.error import Error
from ..types.file_content import FileContent
from ..types.group_id import GroupId
from ..types.version import Version
from ..types.version_meta_data import VersionMetaData
from ..types.version_search_results import VersionSearchResults


OMIT = typing.cast(typing.Any, ...)


class RawVersionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_artifact_versions(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[VersionSearchResults]:
        """
        Returns a list of all versions of the artifact.  The result set is paged.

        This operation can fail for the following reasons:

        * No artifact with this `artifactId` exists (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        artifact_id : ArtifactId
            The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.

        offset : typing.Optional[int]
            The number of versions to skip before starting to collect the result set.  Defaults to 0.

        limit : typing.Optional[int]
            The number of versions to return.  Defaults to 20.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[VersionSearchResults]
            List of all artifact versions.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"groups/{jsonable_encoder(group_id)}/artifacts/{jsonable_encoder(artifact_id)}/versions",
            method="GET",
            params={
                "offset": offset,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VersionSearchResults,
                    parse_obj_as(
                        type_=VersionSearchResults,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_artifact_version(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        *,
        request: FileContent,
        registry_version: typing.Optional[Version] = None,
        registry_name: typing.Optional[ArtifactName] = None,
        registry_description: typing.Optional[ArtifactDescription] = None,
        registry_description_encoded: typing.Optional[EncodedArtifactDescription] = None,
        registry_name_encoded: typing.Optional[EncodedArtifactName] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[VersionMetaData]:
        """
        Creates a new version of the artifact by uploading new content.  The configured rules for
        the artifact are applied, and if they all pass, the new content is added as the most recent
        version of the artifact.  If any of the rules fail, an error is returned.

        The body of the request can be the raw content of the new artifact version, or the raw content
        and a set of references pointing to other artifacts, and the type
        of that content should match the artifact's type (for example if the artifact type is `AVRO`
        then the content of the request should be an Apache Avro document).

        This operation can fail for the following reasons:

        * Provided content (request body) was empty (HTTP error `400`)
        * No artifact with this `artifactId` exists (HTTP error `404`)
        * The new content violates one of the rules configured for the artifact (HTTP error `409`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        artifact_id : ArtifactId
            The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.

        request : FileContent

        registry_version : typing.Optional[Version]
            Specifies the version number of this new version of the artifact content.  This would typically
            be a simple integer or a SemVer value.  It must be unique within the artifact.  If this is not
            provided, the server will generate a new, unique version number for this new updated content.

        registry_name : typing.Optional[ArtifactName]
            Specifies the artifact name of this new version of the artifact content. Name must be ASCII-only string. If this is not
            provided, the server will extract the name from the artifact content.

        registry_description : typing.Optional[ArtifactDescription]
            Specifies the artifact description of this new version of the artifact content. Description must be ASCII-only string. If this is not provided, the server will extract the description from the artifact content.

        registry_description_encoded : typing.Optional[EncodedArtifactDescription]
            Specifies the artifact description of this new version of the artifact content. Value of this must be Base64 encoded string. If this is not provided, the server will extract the description from the artifact content.

        registry_name_encoded : typing.Optional[EncodedArtifactName]
            Specifies the artifact name of this new version of the artifact content. Value of this must be Base64 encoded string. If this is not provided, the server will extract the name from the artifact content.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[VersionMetaData]
            The artifact version was successfully created.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"groups/{jsonable_encoder(group_id)}/artifacts/{jsonable_encoder(artifact_id)}/versions",
            method="POST",
            json=request,
            headers={
                "X-Registry-Version": str(registry_version) if registry_version is not None else None,
                "X-Registry-Name": str(registry_name) if registry_name is not None else None,
                "X-Registry-Description": str(registry_description) if registry_description is not None else None,
                "X-Registry-Description-Encoded": str(registry_description_encoded)
                if registry_description_encoded is not None
                else None,
                "X-Registry-Name-Encoded": str(registry_name_encoded) if registry_name_encoded is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VersionMetaData,
                    parse_obj_as(
                        type_=VersionMetaData,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    @contextlib.contextmanager
    def get_artifact_version(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        version: Version,
        *,
        dereference: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
        """
        Retrieves a single version of the artifact content.  Both the `artifactId` and the
        unique `version` number must be provided.  The `Content-Type` of the response depends
        on the artifact type.  In most cases, this is `application/json`, but for some types
        it may be different (for example, `PROTOBUF`).

        This operation can fail for the following reasons:

        * No artifact with this `artifactId` exists (HTTP error `404`)
        * No version with this `version` exists (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        artifact_id : ArtifactId
            The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.

        version : Version
            The unique identifier of a specific version of the artifact content.

        dereference : typing.Optional[bool]
            Allows the user to specify if the content should be dereferenced when being returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[HttpResponse[typing.Iterator[bytes]]]
            The content of one version of one artifact.
        """
        with self._client_wrapper.httpx_client.stream(
            f"groups/{jsonable_encoder(group_id)}/artifacts/{jsonable_encoder(artifact_id)}/versions/{jsonable_encoder(version)}",
            method="GET",
            params={
                "dereference": dereference,
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
                    if _response.status_code == 404:
                        raise NotFoundError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                Error,
                                parse_obj_as(
                                    type_=Error,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 500:
                        raise InternalServerError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                Error,
                                parse_obj_as(
                                    type_=Error,
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

    def get_artifact_version_references(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        version: Version,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[ArtifactReference]]:
        """
        Retrieves a single version of the artifact content.  Both the `artifactId` and the
        unique `version` number must be provided.  The `Content-Type` of the response depends
        on the artifact type.  In most cases, this is `application/json`, but for some types
        it may be different (for example, `PROTOBUF`).

        This operation can fail for the following reasons:

        * No artifact with this `artifactId` exists (HTTP error `404`)
        * No version with this `version` exists (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        artifact_id : ArtifactId
            The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.

        version : Version
            The unique identifier of a specific version of the artifact content.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[ArtifactReference]]
            List of all the artifact references for this artifact.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"groups/{jsonable_encoder(group_id)}/artifacts/{jsonable_encoder(artifact_id)}/versions/{jsonable_encoder(version)}/references",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ArtifactReference],
                    parse_obj_as(
                        type_=typing.List[ArtifactReference],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_artifact_version_state(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        version: Version,
        *,
        state: ArtifactState,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Updates the state of a specific version of an artifact.  For example, you can use
        this operation to disable a specific version.

        This operation can fail for the following reasons:

        * No artifact with this `artifactId` exists (HTTP error `404`)
        * No version with this `version` exists (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        artifact_id : ArtifactId
            The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.

        version : Version
            The unique identifier of a specific version of the artifact content.

        state : ArtifactState

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"groups/{jsonable_encoder(group_id)}/artifacts/{jsonable_encoder(artifact_id)}/versions/{jsonable_encoder(version)}/state",
            method="PUT",
            json={
                "state": state,
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
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawVersionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_artifact_versions(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[VersionSearchResults]:
        """
        Returns a list of all versions of the artifact.  The result set is paged.

        This operation can fail for the following reasons:

        * No artifact with this `artifactId` exists (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        artifact_id : ArtifactId
            The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.

        offset : typing.Optional[int]
            The number of versions to skip before starting to collect the result set.  Defaults to 0.

        limit : typing.Optional[int]
            The number of versions to return.  Defaults to 20.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[VersionSearchResults]
            List of all artifact versions.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"groups/{jsonable_encoder(group_id)}/artifacts/{jsonable_encoder(artifact_id)}/versions",
            method="GET",
            params={
                "offset": offset,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VersionSearchResults,
                    parse_obj_as(
                        type_=VersionSearchResults,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_artifact_version(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        *,
        request: FileContent,
        registry_version: typing.Optional[Version] = None,
        registry_name: typing.Optional[ArtifactName] = None,
        registry_description: typing.Optional[ArtifactDescription] = None,
        registry_description_encoded: typing.Optional[EncodedArtifactDescription] = None,
        registry_name_encoded: typing.Optional[EncodedArtifactName] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[VersionMetaData]:
        """
        Creates a new version of the artifact by uploading new content.  The configured rules for
        the artifact are applied, and if they all pass, the new content is added as the most recent
        version of the artifact.  If any of the rules fail, an error is returned.

        The body of the request can be the raw content of the new artifact version, or the raw content
        and a set of references pointing to other artifacts, and the type
        of that content should match the artifact's type (for example if the artifact type is `AVRO`
        then the content of the request should be an Apache Avro document).

        This operation can fail for the following reasons:

        * Provided content (request body) was empty (HTTP error `400`)
        * No artifact with this `artifactId` exists (HTTP error `404`)
        * The new content violates one of the rules configured for the artifact (HTTP error `409`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        artifact_id : ArtifactId
            The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.

        request : FileContent

        registry_version : typing.Optional[Version]
            Specifies the version number of this new version of the artifact content.  This would typically
            be a simple integer or a SemVer value.  It must be unique within the artifact.  If this is not
            provided, the server will generate a new, unique version number for this new updated content.

        registry_name : typing.Optional[ArtifactName]
            Specifies the artifact name of this new version of the artifact content. Name must be ASCII-only string. If this is not
            provided, the server will extract the name from the artifact content.

        registry_description : typing.Optional[ArtifactDescription]
            Specifies the artifact description of this new version of the artifact content. Description must be ASCII-only string. If this is not provided, the server will extract the description from the artifact content.

        registry_description_encoded : typing.Optional[EncodedArtifactDescription]
            Specifies the artifact description of this new version of the artifact content. Value of this must be Base64 encoded string. If this is not provided, the server will extract the description from the artifact content.

        registry_name_encoded : typing.Optional[EncodedArtifactName]
            Specifies the artifact name of this new version of the artifact content. Value of this must be Base64 encoded string. If this is not provided, the server will extract the name from the artifact content.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[VersionMetaData]
            The artifact version was successfully created.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"groups/{jsonable_encoder(group_id)}/artifacts/{jsonable_encoder(artifact_id)}/versions",
            method="POST",
            json=request,
            headers={
                "X-Registry-Version": str(registry_version) if registry_version is not None else None,
                "X-Registry-Name": str(registry_name) if registry_name is not None else None,
                "X-Registry-Description": str(registry_description) if registry_description is not None else None,
                "X-Registry-Description-Encoded": str(registry_description_encoded)
                if registry_description_encoded is not None
                else None,
                "X-Registry-Name-Encoded": str(registry_name_encoded) if registry_name_encoded is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VersionMetaData,
                    parse_obj_as(
                        type_=VersionMetaData,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    @contextlib.asynccontextmanager
    async def get_artifact_version(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        version: Version,
        *,
        dereference: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
        """
        Retrieves a single version of the artifact content.  Both the `artifactId` and the
        unique `version` number must be provided.  The `Content-Type` of the response depends
        on the artifact type.  In most cases, this is `application/json`, but for some types
        it may be different (for example, `PROTOBUF`).

        This operation can fail for the following reasons:

        * No artifact with this `artifactId` exists (HTTP error `404`)
        * No version with this `version` exists (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        artifact_id : ArtifactId
            The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.

        version : Version
            The unique identifier of a specific version of the artifact content.

        dereference : typing.Optional[bool]
            Allows the user to specify if the content should be dereferenced when being returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]
            The content of one version of one artifact.
        """
        async with self._client_wrapper.httpx_client.stream(
            f"groups/{jsonable_encoder(group_id)}/artifacts/{jsonable_encoder(artifact_id)}/versions/{jsonable_encoder(version)}",
            method="GET",
            params={
                "dereference": dereference,
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
                    if _response.status_code == 404:
                        raise NotFoundError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                Error,
                                parse_obj_as(
                                    type_=Error,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 500:
                        raise InternalServerError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                Error,
                                parse_obj_as(
                                    type_=Error,
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

    async def get_artifact_version_references(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        version: Version,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[ArtifactReference]]:
        """
        Retrieves a single version of the artifact content.  Both the `artifactId` and the
        unique `version` number must be provided.  The `Content-Type` of the response depends
        on the artifact type.  In most cases, this is `application/json`, but for some types
        it may be different (for example, `PROTOBUF`).

        This operation can fail for the following reasons:

        * No artifact with this `artifactId` exists (HTTP error `404`)
        * No version with this `version` exists (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        artifact_id : ArtifactId
            The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.

        version : Version
            The unique identifier of a specific version of the artifact content.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[ArtifactReference]]
            List of all the artifact references for this artifact.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"groups/{jsonable_encoder(group_id)}/artifacts/{jsonable_encoder(artifact_id)}/versions/{jsonable_encoder(version)}/references",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ArtifactReference],
                    parse_obj_as(
                        type_=typing.List[ArtifactReference],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_artifact_version_state(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        version: Version,
        *,
        state: ArtifactState,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Updates the state of a specific version of an artifact.  For example, you can use
        this operation to disable a specific version.

        This operation can fail for the following reasons:

        * No artifact with this `artifactId` exists (HTTP error `404`)
        * No version with this `version` exists (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        artifact_id : ArtifactId
            The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.

        version : Version
            The unique identifier of a specific version of the artifact content.

        state : ArtifactState

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"groups/{jsonable_encoder(group_id)}/artifacts/{jsonable_encoder(artifact_id)}/versions/{jsonable_encoder(version)}/state",
            method="PUT",
            json={
                "state": state,
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
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

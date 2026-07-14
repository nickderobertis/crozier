

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..types.artifact_id import ArtifactId
from ..types.artifact_meta_data import ArtifactMetaData
from ..types.artifact_owner import ArtifactOwner
from ..types.error import Error
from ..types.file_content import FileContent
from ..types.group_id import GroupId
from ..types.properties import Properties
from ..types.version import Version
from ..types.version_meta_data import VersionMetaData


OMIT = typing.cast(typing.Any, ...)


class RawMetadataClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_artifact_meta_data(
        self, group_id: GroupId, artifact_id: ArtifactId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ArtifactMetaData]:
        """
        Gets the metadata for an artifact in the registry.  The returned metadata includes
        both generated (read-only) and editable metadata (such as name and description).

        This operation can fail for the following reasons:

        * No artifact with this `artifactId` exists (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        artifact_id : ArtifactId
            The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ArtifactMetaData]
            The artifact's metadata.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"groups/{jsonable_encoder(group_id)}/artifacts/{jsonable_encoder(artifact_id)}/meta",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ArtifactMetaData,
                    parse_obj_as(
                        type_=ArtifactMetaData,
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

    def get_artifact_version_meta_data_by_content(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        *,
        request: FileContent,
        canonical: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[VersionMetaData]:
        """
        Gets the metadata for an artifact that matches the raw content.  Searches the registry
        for a version of the given artifact matching the content provided in the body of the
        POST.

        This operation can fail for the following reasons:

        * Provided content (request body) was empty (HTTP error `400`)
        * No artifact with the `artifactId` exists (HTTP error `404`)
        * No artifact version matching the provided content exists (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        artifact_id : ArtifactId
            The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.

        request : FileContent

        canonical : typing.Optional[bool]
            Parameter that can be set to `true` to indicate that the server should "canonicalize" the content when searching for a matching version.  Canonicalization is unique to each artifact type, but typically involves removing any extra whitespace and formatting the content in a consistent manner.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[VersionMetaData]
            The metadata of the artifact version matching the provided content.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"groups/{jsonable_encoder(group_id)}/artifacts/{jsonable_encoder(artifact_id)}/meta",
            method="POST",
            params={
                "canonical": canonical,
            },
            json=request,
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

    def update_artifact_meta_data(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        *,
        description: typing.Optional[str] = OMIT,
        labels: typing.Optional[typing.Sequence[str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        properties: typing.Optional[Properties] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Updates the editable parts of the artifact's metadata.  Not all metadata fields can
        be updated.  For example, `createdOn` and `createdBy` are both read-only properties.

        This operation can fail for the following reasons:

        * No artifact with the `artifactId` exists (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        artifact_id : ArtifactId
            The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.

        description : typing.Optional[str]

        labels : typing.Optional[typing.Sequence[str]]


        name : typing.Optional[str]

        properties : typing.Optional[Properties]


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"groups/{jsonable_encoder(group_id)}/artifacts/{jsonable_encoder(artifact_id)}/meta",
            method="PUT",
            json={
                "description": description,
                "labels": labels,
                "name": name,
                "properties": properties,
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

    def get_artifact_owner(
        self, group_id: GroupId, artifact_id: ArtifactId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ArtifactOwner]:
        """
        Gets the owner of an artifact in the registry.

        This operation can fail for the following reasons:

        * No artifact with this `artifactId` exists (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        artifact_id : ArtifactId
            The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ArtifactOwner]
            The artifact's owner.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"groups/{jsonable_encoder(group_id)}/artifacts/{jsonable_encoder(artifact_id)}/owner",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ArtifactOwner,
                    parse_obj_as(
                        type_=ArtifactOwner,
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

    def update_artifact_owner(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        *,
        owner: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Changes the ownership of an artifact.

        This operation can fail for the following reasons:

        * No artifact with this `artifactId` exists (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        artifact_id : ArtifactId
            The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.

        owner : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"groups/{jsonable_encoder(group_id)}/artifacts/{jsonable_encoder(artifact_id)}/owner",
            method="PUT",
            json={
                "owner": owner,
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

    def get_artifact_version_meta_data(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        version: Version,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[VersionMetaData]:
        """
        Retrieves the metadata for a single version of the artifact.  The version metadata is
        a subset of the artifact metadata and only includes the metadata that is specific to
        the version (for example, this doesn't include `modifiedOn`).

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
        HttpResponse[VersionMetaData]
            The artifact version's metadata.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"groups/{jsonable_encoder(group_id)}/artifacts/{jsonable_encoder(artifact_id)}/versions/{jsonable_encoder(version)}/meta",
            method="GET",
            request_options=request_options,
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

    def update_artifact_version_meta_data(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        version: Version,
        *,
        description: typing.Optional[str] = OMIT,
        labels: typing.Optional[typing.Sequence[str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        properties: typing.Optional[Properties] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Updates the user-editable portion of the artifact version's metadata.  Only some of
        the metadata fields are editable by the user.  For example, `description` is editable,
        but `createdOn` is not.

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

        description : typing.Optional[str]

        labels : typing.Optional[typing.Sequence[str]]


        name : typing.Optional[str]

        properties : typing.Optional[Properties]


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"groups/{jsonable_encoder(group_id)}/artifacts/{jsonable_encoder(artifact_id)}/versions/{jsonable_encoder(version)}/meta",
            method="PUT",
            json={
                "description": description,
                "labels": labels,
                "name": name,
                "properties": properties,
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

    def delete_artifact_version_meta_data(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        version: Version,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Deletes the user-editable metadata properties of the artifact version.  Any properties
        that are not user-editable are preserved.

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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"groups/{jsonable_encoder(group_id)}/artifacts/{jsonable_encoder(artifact_id)}/versions/{jsonable_encoder(version)}/meta",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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


class AsyncRawMetadataClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_artifact_meta_data(
        self, group_id: GroupId, artifact_id: ArtifactId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ArtifactMetaData]:
        """
        Gets the metadata for an artifact in the registry.  The returned metadata includes
        both generated (read-only) and editable metadata (such as name and description).

        This operation can fail for the following reasons:

        * No artifact with this `artifactId` exists (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        artifact_id : ArtifactId
            The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ArtifactMetaData]
            The artifact's metadata.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"groups/{jsonable_encoder(group_id)}/artifacts/{jsonable_encoder(artifact_id)}/meta",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ArtifactMetaData,
                    parse_obj_as(
                        type_=ArtifactMetaData,
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

    async def get_artifact_version_meta_data_by_content(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        *,
        request: FileContent,
        canonical: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[VersionMetaData]:
        """
        Gets the metadata for an artifact that matches the raw content.  Searches the registry
        for a version of the given artifact matching the content provided in the body of the
        POST.

        This operation can fail for the following reasons:

        * Provided content (request body) was empty (HTTP error `400`)
        * No artifact with the `artifactId` exists (HTTP error `404`)
        * No artifact version matching the provided content exists (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        artifact_id : ArtifactId
            The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.

        request : FileContent

        canonical : typing.Optional[bool]
            Parameter that can be set to `true` to indicate that the server should "canonicalize" the content when searching for a matching version.  Canonicalization is unique to each artifact type, but typically involves removing any extra whitespace and formatting the content in a consistent manner.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[VersionMetaData]
            The metadata of the artifact version matching the provided content.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"groups/{jsonable_encoder(group_id)}/artifacts/{jsonable_encoder(artifact_id)}/meta",
            method="POST",
            params={
                "canonical": canonical,
            },
            json=request,
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

    async def update_artifact_meta_data(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        *,
        description: typing.Optional[str] = OMIT,
        labels: typing.Optional[typing.Sequence[str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        properties: typing.Optional[Properties] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Updates the editable parts of the artifact's metadata.  Not all metadata fields can
        be updated.  For example, `createdOn` and `createdBy` are both read-only properties.

        This operation can fail for the following reasons:

        * No artifact with the `artifactId` exists (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        artifact_id : ArtifactId
            The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.

        description : typing.Optional[str]

        labels : typing.Optional[typing.Sequence[str]]


        name : typing.Optional[str]

        properties : typing.Optional[Properties]


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"groups/{jsonable_encoder(group_id)}/artifacts/{jsonable_encoder(artifact_id)}/meta",
            method="PUT",
            json={
                "description": description,
                "labels": labels,
                "name": name,
                "properties": properties,
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

    async def get_artifact_owner(
        self, group_id: GroupId, artifact_id: ArtifactId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ArtifactOwner]:
        """
        Gets the owner of an artifact in the registry.

        This operation can fail for the following reasons:

        * No artifact with this `artifactId` exists (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        artifact_id : ArtifactId
            The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ArtifactOwner]
            The artifact's owner.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"groups/{jsonable_encoder(group_id)}/artifacts/{jsonable_encoder(artifact_id)}/owner",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ArtifactOwner,
                    parse_obj_as(
                        type_=ArtifactOwner,
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

    async def update_artifact_owner(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        *,
        owner: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Changes the ownership of an artifact.

        This operation can fail for the following reasons:

        * No artifact with this `artifactId` exists (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        artifact_id : ArtifactId
            The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.

        owner : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"groups/{jsonable_encoder(group_id)}/artifacts/{jsonable_encoder(artifact_id)}/owner",
            method="PUT",
            json={
                "owner": owner,
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

    async def get_artifact_version_meta_data(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        version: Version,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[VersionMetaData]:
        """
        Retrieves the metadata for a single version of the artifact.  The version metadata is
        a subset of the artifact metadata and only includes the metadata that is specific to
        the version (for example, this doesn't include `modifiedOn`).

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
        AsyncHttpResponse[VersionMetaData]
            The artifact version's metadata.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"groups/{jsonable_encoder(group_id)}/artifacts/{jsonable_encoder(artifact_id)}/versions/{jsonable_encoder(version)}/meta",
            method="GET",
            request_options=request_options,
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

    async def update_artifact_version_meta_data(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        version: Version,
        *,
        description: typing.Optional[str] = OMIT,
        labels: typing.Optional[typing.Sequence[str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        properties: typing.Optional[Properties] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Updates the user-editable portion of the artifact version's metadata.  Only some of
        the metadata fields are editable by the user.  For example, `description` is editable,
        but `createdOn` is not.

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

        description : typing.Optional[str]

        labels : typing.Optional[typing.Sequence[str]]


        name : typing.Optional[str]

        properties : typing.Optional[Properties]


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"groups/{jsonable_encoder(group_id)}/artifacts/{jsonable_encoder(artifact_id)}/versions/{jsonable_encoder(version)}/meta",
            method="PUT",
            json={
                "description": description,
                "labels": labels,
                "name": name,
                "properties": properties,
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

    async def delete_artifact_version_meta_data(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        version: Version,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Deletes the user-editable metadata properties of the artifact version.  Any properties
        that are not user-editable are preserved.

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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"groups/{jsonable_encoder(group_id)}/artifacts/{jsonable_encoder(artifact_id)}/versions/{jsonable_encoder(version)}/meta",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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

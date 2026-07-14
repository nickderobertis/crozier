

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.internal_server_error import InternalServerError
from ..types.artifact_search_results import ArtifactSearchResults
from ..types.artifact_type import ArtifactType
from ..types.error import Error
from ..types.file_content import FileContent
from ..types.sort_by import SortBy
from ..types.sort_order import SortOrder
from .types.search_artifacts_by_content_request_order import SearchArtifactsByContentRequestOrder
from .types.search_artifacts_by_content_request_orderby import SearchArtifactsByContentRequestOrderby


OMIT = typing.cast(typing.Any, ...)


class RawSearchClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def artifacts(
        self,
        *,
        name: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[SortOrder] = None,
        orderby: typing.Optional[SortBy] = None,
        labels: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        properties: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        description: typing.Optional[str] = None,
        group: typing.Optional[str] = None,
        global_id: typing.Optional[int] = None,
        content_id: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ArtifactSearchResults]:
        """
        Returns a paginated list of all artifacts that match the provided filter criteria.

        Parameters
        ----------
        name : typing.Optional[str]
            Filter by artifact name.

        offset : typing.Optional[int]
            The number of artifacts to skip before starting to collect the result set.  Defaults to 0.

        limit : typing.Optional[int]
            The number of artifacts to return.  Defaults to 20.

        order : typing.Optional[SortOrder]
            Sort order, ascending (`asc`) or descending (`desc`).

        orderby : typing.Optional[SortBy]
            The field to sort by.  Can be one of:

            * `name`
            * `createdOn`

        labels : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Filter by label.  Include one or more label to only return artifacts containing all of the
            specified labels.

        properties : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Filter by one or more name/value property.  Separate each name/value pair using a colon.  For
            example `properties=foo:bar` will return only artifacts with a custom property named `foo`
            and value `bar`.

        description : typing.Optional[str]
            Filter by description.

        group : typing.Optional[str]
            Filter by artifact group.

        global_id : typing.Optional[int]
            Filter by globalId.

        content_id : typing.Optional[int]
            Filter by contentId.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ArtifactSearchResults]
            On a successful response, returns a result set of artifacts - one for each artifact
            in the registry that matches the criteria.
        """
        _response = self._client_wrapper.httpx_client.request(
            "search/artifacts",
            method="GET",
            params={
                "name": name,
                "offset": offset,
                "limit": limit,
                "order": order,
                "orderby": orderby,
                "labels": labels,
                "properties": properties,
                "description": description,
                "group": group,
                "globalId": global_id,
                "contentId": content_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ArtifactSearchResults,
                    parse_obj_as(
                        type_=ArtifactSearchResults,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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

    def artifacts_by_content(
        self,
        *,
        request: FileContent,
        canonical: typing.Optional[bool] = None,
        artifact_type: typing.Optional[ArtifactType] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[SearchArtifactsByContentRequestOrder] = None,
        orderby: typing.Optional[SearchArtifactsByContentRequestOrderby] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ArtifactSearchResults]:
        """
        Returns a paginated list of all artifacts with at least one version that matches the
        posted content.

        Parameters
        ----------
        request : FileContent

        canonical : typing.Optional[bool]
            Parameter that can be set to `true` to indicate that the server should "canonicalize" the content when searching for matching artifacts.  Canonicalization is unique to each artifact type, but typically involves removing any extra whitespace and formatting the content in a consistent manner.  Must be used along with the `artifactType` query parameter.

        artifact_type : typing.Optional[ArtifactType]
            Indicates the type of artifact represented by the content being used for the search.  This is only needed when using the `canonical` query parameter, so that the server knows how to canonicalize the content prior to searching for matching artifacts.

        offset : typing.Optional[int]
            The number of artifacts to skip before starting to collect the result set.  Defaults to 0.

        limit : typing.Optional[int]
            The number of artifacts to return.  Defaults to 20.

        order : typing.Optional[SearchArtifactsByContentRequestOrder]
            Sort order, ascending (`asc`) or descending (`desc`).

        orderby : typing.Optional[SearchArtifactsByContentRequestOrderby]
            The field to sort by.  Can be one of:

            * `name`
            * `createdOn`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ArtifactSearchResults]
            On a successful response, returns a result set of artifacts - one for each artifact
            in the registry that matches the criteria.
        """
        _response = self._client_wrapper.httpx_client.request(
            "search/artifacts",
            method="POST",
            params={
                "canonical": canonical,
                "artifactType": artifact_type,
                "offset": offset,
                "limit": limit,
                "order": order,
                "orderby": orderby,
            },
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ArtifactSearchResults,
                    parse_obj_as(
                        type_=ArtifactSearchResults,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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


class AsyncRawSearchClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def artifacts(
        self,
        *,
        name: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[SortOrder] = None,
        orderby: typing.Optional[SortBy] = None,
        labels: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        properties: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        description: typing.Optional[str] = None,
        group: typing.Optional[str] = None,
        global_id: typing.Optional[int] = None,
        content_id: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ArtifactSearchResults]:
        """
        Returns a paginated list of all artifacts that match the provided filter criteria.

        Parameters
        ----------
        name : typing.Optional[str]
            Filter by artifact name.

        offset : typing.Optional[int]
            The number of artifacts to skip before starting to collect the result set.  Defaults to 0.

        limit : typing.Optional[int]
            The number of artifacts to return.  Defaults to 20.

        order : typing.Optional[SortOrder]
            Sort order, ascending (`asc`) or descending (`desc`).

        orderby : typing.Optional[SortBy]
            The field to sort by.  Can be one of:

            * `name`
            * `createdOn`

        labels : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Filter by label.  Include one or more label to only return artifacts containing all of the
            specified labels.

        properties : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Filter by one or more name/value property.  Separate each name/value pair using a colon.  For
            example `properties=foo:bar` will return only artifacts with a custom property named `foo`
            and value `bar`.

        description : typing.Optional[str]
            Filter by description.

        group : typing.Optional[str]
            Filter by artifact group.

        global_id : typing.Optional[int]
            Filter by globalId.

        content_id : typing.Optional[int]
            Filter by contentId.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ArtifactSearchResults]
            On a successful response, returns a result set of artifacts - one for each artifact
            in the registry that matches the criteria.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "search/artifacts",
            method="GET",
            params={
                "name": name,
                "offset": offset,
                "limit": limit,
                "order": order,
                "orderby": orderby,
                "labels": labels,
                "properties": properties,
                "description": description,
                "group": group,
                "globalId": global_id,
                "contentId": content_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ArtifactSearchResults,
                    parse_obj_as(
                        type_=ArtifactSearchResults,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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

    async def artifacts_by_content(
        self,
        *,
        request: FileContent,
        canonical: typing.Optional[bool] = None,
        artifact_type: typing.Optional[ArtifactType] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[SearchArtifactsByContentRequestOrder] = None,
        orderby: typing.Optional[SearchArtifactsByContentRequestOrderby] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ArtifactSearchResults]:
        """
        Returns a paginated list of all artifacts with at least one version that matches the
        posted content.

        Parameters
        ----------
        request : FileContent

        canonical : typing.Optional[bool]
            Parameter that can be set to `true` to indicate that the server should "canonicalize" the content when searching for matching artifacts.  Canonicalization is unique to each artifact type, but typically involves removing any extra whitespace and formatting the content in a consistent manner.  Must be used along with the `artifactType` query parameter.

        artifact_type : typing.Optional[ArtifactType]
            Indicates the type of artifact represented by the content being used for the search.  This is only needed when using the `canonical` query parameter, so that the server knows how to canonicalize the content prior to searching for matching artifacts.

        offset : typing.Optional[int]
            The number of artifacts to skip before starting to collect the result set.  Defaults to 0.

        limit : typing.Optional[int]
            The number of artifacts to return.  Defaults to 20.

        order : typing.Optional[SearchArtifactsByContentRequestOrder]
            Sort order, ascending (`asc`) or descending (`desc`).

        orderby : typing.Optional[SearchArtifactsByContentRequestOrderby]
            The field to sort by.  Can be one of:

            * `name`
            * `createdOn`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ArtifactSearchResults]
            On a successful response, returns a result set of artifacts - one for each artifact
            in the registry that matches the criteria.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "search/artifacts",
            method="POST",
            params={
                "canonical": canonical,
                "artifactType": artifact_type,
                "offset": offset,
                "limit": limit,
                "order": order,
                "orderby": orderby,
            },
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ArtifactSearchResults,
                    parse_obj_as(
                        type_=ArtifactSearchResults,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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

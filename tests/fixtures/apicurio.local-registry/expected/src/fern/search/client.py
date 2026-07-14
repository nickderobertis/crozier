

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.artifact_search_results import ArtifactSearchResults
from ..types.artifact_type import ArtifactType
from ..types.file_content import FileContent
from ..types.sort_by import SortBy
from ..types.sort_order import SortOrder
from .raw_client import AsyncRawSearchClient, RawSearchClient
from .types.search_artifacts_by_content_request_order import SearchArtifactsByContentRequestOrder
from .types.search_artifacts_by_content_request_orderby import SearchArtifactsByContentRequestOrderby


OMIT = typing.cast(typing.Any, ...)


class SearchClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSearchClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSearchClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSearchClient
        """
        return self._raw_client

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
    ) -> ArtifactSearchResults:
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
        ArtifactSearchResults
            On a successful response, returns a result set of artifacts - one for each artifact
            in the registry that matches the criteria.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.search.artifacts()
        """
        _response = self._raw_client.artifacts(
            name=name,
            offset=offset,
            limit=limit,
            order=order,
            orderby=orderby,
            labels=labels,
            properties=properties,
            description=description,
            group=group,
            global_id=global_id,
            content_id=content_id,
            request_options=request_options,
        )
        return _response.data

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
    ) -> ArtifactSearchResults:
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
        ArtifactSearchResults
            On a successful response, returns a result set of artifacts - one for each artifact
            in the registry that matches the criteria.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.search.artifacts_by_content(
            artifact_type="AVRO",
            request="string",
        )
        """
        _response = self._raw_client.artifacts_by_content(
            request=request,
            canonical=canonical,
            artifact_type=artifact_type,
            offset=offset,
            limit=limit,
            order=order,
            orderby=orderby,
            request_options=request_options,
        )
        return _response.data


class AsyncSearchClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSearchClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSearchClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSearchClient
        """
        return self._raw_client

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
    ) -> ArtifactSearchResults:
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
        ArtifactSearchResults
            On a successful response, returns a result set of artifacts - one for each artifact
            in the registry that matches the criteria.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.search.artifacts()


        asyncio.run(main())
        """
        _response = await self._raw_client.artifacts(
            name=name,
            offset=offset,
            limit=limit,
            order=order,
            orderby=orderby,
            labels=labels,
            properties=properties,
            description=description,
            group=group,
            global_id=global_id,
            content_id=content_id,
            request_options=request_options,
        )
        return _response.data

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
    ) -> ArtifactSearchResults:
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
        ArtifactSearchResults
            On a successful response, returns a result set of artifacts - one for each artifact
            in the registry that matches the criteria.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.search.artifacts_by_content(
                artifact_type="AVRO",
                request="string",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.artifacts_by_content(
            request=request,
            canonical=canonical,
            artifact_type=artifact_type,
            offset=offset,
            limit=limit,
            order=order,
            orderby=orderby,
            request_options=request_options,
        )
        return _response.data

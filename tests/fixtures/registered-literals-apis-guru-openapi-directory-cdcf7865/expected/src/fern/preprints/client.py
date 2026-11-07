

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawPreprintsClient, RawPreprintsClient
from .types.preprints_bibliographic_contributors_list_response_item import (
    PreprintsBibliographicContributorsListResponseItem,
)
from .types.preprints_citation_list_response import PreprintsCitationListResponse
from .types.preprints_citation_read_response import PreprintsCitationReadResponse
from .types.preprints_contributors_create_request_attributes import PreprintsContributorsCreateRequestAttributes
from .types.preprints_contributors_list_response_item import PreprintsContributorsListResponseItem
from .types.preprints_create_request_attributes import PreprintsCreateRequestAttributes
from .types.preprints_create_request_relationships import PreprintsCreateRequestRelationships
from .types.preprints_list_response_item import PreprintsListResponseItem
from .types.preprints_read_response import PreprintsReadResponse


OMIT = typing.cast(typing.Any, ...)


class PreprintsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPreprintsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPreprintsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPreprintsClient
        """
        return self._raw_client

    def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[PreprintsListResponseItem]:
        """

        A paginated list of preprints from all preprint providers. The returned preprints are sorted by their creation date, with the most recent preprints appearing first.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of 10 preprints. Each resource in the array is a separate preprint object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        This request should never return an error.
        #### Filtering
        You can optionally request that the response only include preprints that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/preprints/?filter[provider]=socarxiv.

        Preprints may be filtered by their `id`, `is_published`, `date_created`, `date_modified`, and `provider`.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PreprintsListResponseItem]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.preprints.list()
        """
        _response = self._raw_client.list(request_options=request_options)
        return _response.data

    def create(
        self,
        *,
        relationships: PreprintsCreateRequestRelationships,
        type: str,
        attributes: typing.Optional[PreprintsCreateRequestAttributes] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Creates a new preprint.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the created preprint, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes]() to understand why this request may have failed.

        Parameters
        ----------
        relationships : PreprintsCreateRequestRelationships
            URLs to other entities or entity collections that have a relationship to the preprint entity.

        type : str
            The type identifier of the preprint entity (`preprints`).

        attributes : typing.Optional[PreprintsCreateRequestAttributes]
            The properties of the preprint entity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.preprints import PreprintsCreateRequestRelationships

        from fern import FernApi

        client = FernApi()
        client.preprints.create(
            relationships=PreprintsCreateRequestRelationships(
                node="node",
                primary_file="primary_file",
                provider="provider",
            ),
            type="type",
        )
        """
        _response = self._raw_client.create(
            relationships=relationships, type=type, attributes=attributes, request_options=request_options
        )
        return _response.data

    def read(
        self, preprint_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PreprintsReadResponse:
        """
        Retrieves the details of a preprint.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested preprint, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        preprint_id : str
            The unique identifier of the preprint.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PreprintsReadResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.preprints.read(
            preprint_id="preprint_id",
        )
        """
        _response = self._raw_client.read(preprint_id, request_options=request_options)
        return _response.data

    def partial_update(
        self,
        preprint_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates the specified preprint by setting the values of the parameters passed. Any parameters not provided will be left unchanged.
        #### Returns
        Returns a JSON object with a `data` key containing the new representation of the updated preprint, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes]() to understand why this request may have failed.

        Parameters
        ----------
        preprint_id : str
            The unique identifier of the preprint.

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.preprints.partial_update(
            preprint_id="preprint_id",
            request={
                "data": {
                    "attributes": {"doi": "{doi}"},
                    "id": "{preprint_id}",
                    "relationships": {
                        "primary_file": {
                            "data": {"id": "{file_id}", "type": "primary_files"}
                        }
                    },
                }
            },
        )
        """
        _response = self._raw_client.partial_update(preprint_id, request=request, request_options=request_options)
        return _response.data

    def bibliographic_contributors_list(
        self, preprint_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[PreprintsBibliographicContributorsListResponseItem]:
        """
        A paginated list of the Preprint's Bibliographic Contributors, sorted by their index.
        Contributors are users who can make changes to the Preprint. Contributors with WRITE permissions may edit preprint details, and ADMIN Contributors may add or remove other Contributors.

        Contributors are categorized as either "bibliographic" or "non-bibliographic". From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed on the project overview page on the OSF, while non-bibliographic contributors are not.

        Note that if an anonymous view_only key is being used to view the list of contributors, the user relationship will not be exposed and the contributor ID will be an empty string.

        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of 10 contributors. Each resource in the array contains the full representation of the contributor, meaning additional requests to a contributor's detail view are not necessary. Additionally, the full representation of the user this contributor represents is automatically embedded within the `data` key of the response.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
        #### Filtering
        You can optionally request that the response only include contributors that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/preprints/y9jdt/contributors/?filter[bibliographic]=true.

        Contributors may be filtered by their `bibliographic` and `permission` attributes.

        Parameters
        ----------
        preprint_id : str
            The unique identifier of the preprint.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PreprintsBibliographicContributorsListResponseItem]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.preprints.bibliographic_contributors_list(
            preprint_id="preprint_id",
        )
        """
        _response = self._raw_client.bibliographic_contributors_list(preprint_id, request_options=request_options)
        return _response.data

    def citation_list(
        self, preprint_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PreprintsCitationListResponse:
        """
        The citation details for a preprint, in CSL format.
        #### Returns
        Returns a JSON object with a `data` key that contains the representation of the details necessary for the preprint citation.

        Parameters
        ----------
        preprint_id : str
            The unique identifier of the preprint whose citation you wish to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PreprintsCitationListResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.preprints.citation_list(
            preprint_id="preprint_id",
        )
        """
        _response = self._raw_client.citation_list(preprint_id, request_options=request_options)
        return _response.data

    def citation_read(
        self, preprint_id: str, style_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PreprintsCitationReadResponse:
        """
        The citation for a preprint in a specific style.
        #### Returns
        Returns a JSON object with a `data` key that contains the representation of the preprint citation, in the requested style.

        Parameters
        ----------
        preprint_id : str
            The unique identifier of the preprint.

        style_id : str
            The unique identifier of the citation style.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PreprintsCitationReadResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.preprints.citation_read(
            preprint_id="preprint_id",
            style_id="style_id",
        )
        """
        _response = self._raw_client.citation_read(preprint_id, style_id, request_options=request_options)
        return _response.data

    def contributors_list(
        self, preprint_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[PreprintsContributorsListResponseItem]:
        """
        A paginated list of the Preprint's Contributors, sorted by their index.

        Contributors are users who can make changes to the Preprint. Contributors with WRITE permissions may edit preprint details, and ADMIN Contributors may add or remove other Contributors.

        Contributors are categorized as either "bibliographic" or "non-bibliographic". From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed on the project overview page on the OSF, while non-bibliographic contributors are not.

        Note that if an anonymous view_only key is being used to view the list of Contributors, the user relationship will not be exposed and the Contributor ID will be an empty string.

        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of 10 contributors. Each resource in the array contains the full representation of the contributor, meaning additional requests to a contributor's detail view are not necessary. Additionally, the full representation of the user this contributor represents is automatically embedded within the `data` key of the response.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
        #### Filtering
        You can optionally request that the response only include contributors that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/preprints/y9jdt/contributors/?filter[bibliographic]=true.

        Contributors may be filtered by their `bibliographic` and `permission` attributes.

        Parameters
        ----------
        preprint_id : str
            The unique identifier of the preprint.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PreprintsContributorsListResponseItem]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.preprints.contributors_list(
            preprint_id="preprint_id",
        )
        """
        _response = self._raw_client.contributors_list(preprint_id, request_options=request_options)
        return _response.data

    def contributors_create(
        self,
        preprint_id: str,
        *,
        attributes: typing.Optional[PreprintsContributorsCreateRequestAttributes] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Adds a contributor to a Preprint, effectively creating a relationship between the Preprint and a user.

        Contributors are users who can make changes to the Preprint. Contributors with WRITE permissions may edit preprint details, and ADMIN Contributors may add or remove other Contributors.

        Contributors are categorized as either "bibliographic" or "non-bibliographic" contributors. From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed on the project overview page on the OSF, while non-bibliographic contributors are not.
        #### Permissions
        Only project administrators can add contributors to a Preprint.
        #### Required
        A relationship object with a `data` key, containing the `users` type and valid user ID is required.

        All attributes describing the relationship between the Preprint and the user are optional.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the new contributor, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        preprint_id : str
            The unique identifier of the Preprint.

        attributes : typing.Optional[PreprintsContributorsCreateRequestAttributes]
            The properties of the contributor entity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.preprints.contributors_create(
            preprint_id="preprint_id",
        )
        """
        _response = self._raw_client.contributors_create(
            preprint_id, attributes=attributes, request_options=request_options
        )
        return _response.data

    def contributor_read(
        self, preprint_id: str, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Retrieves the details of a contributor on this Preprint.
        Contributors are categorized as either "bibliographic" or "non-bibliographic". From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed on the project overview page on the OSF, while non-bibliographic contributors are not.

        Note that if an anonymous view_only key is being used to view the list of contributors, the user relationship will not be exposed and the contributor ID will be an empty string.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested contributor, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        preprint_id : str
            The unique identifier of the Preprint.

        user_id : str
            The unique identifier of the user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.preprints.contributor_read(
            preprint_id="preprint_id",
            user_id="user_id",
        )
        """
        _response = self._raw_client.contributor_read(preprint_id, user_id, request_options=request_options)
        return _response.data


class AsyncPreprintsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPreprintsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPreprintsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPreprintsClient
        """
        return self._raw_client

    async def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[PreprintsListResponseItem]:
        """

        A paginated list of preprints from all preprint providers. The returned preprints are sorted by their creation date, with the most recent preprints appearing first.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of 10 preprints. Each resource in the array is a separate preprint object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        This request should never return an error.
        #### Filtering
        You can optionally request that the response only include preprints that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/preprints/?filter[provider]=socarxiv.

        Preprints may be filtered by their `id`, `is_published`, `date_created`, `date_modified`, and `provider`.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PreprintsListResponseItem]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.preprints.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(request_options=request_options)
        return _response.data

    async def create(
        self,
        *,
        relationships: PreprintsCreateRequestRelationships,
        type: str,
        attributes: typing.Optional[PreprintsCreateRequestAttributes] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Creates a new preprint.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the created preprint, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes]() to understand why this request may have failed.

        Parameters
        ----------
        relationships : PreprintsCreateRequestRelationships
            URLs to other entities or entity collections that have a relationship to the preprint entity.

        type : str
            The type identifier of the preprint entity (`preprints`).

        attributes : typing.Optional[PreprintsCreateRequestAttributes]
            The properties of the preprint entity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.preprints import PreprintsCreateRequestRelationships

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.preprints.create(
                relationships=PreprintsCreateRequestRelationships(
                    node="node",
                    primary_file="primary_file",
                    provider="provider",
                ),
                type="type",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(
            relationships=relationships, type=type, attributes=attributes, request_options=request_options
        )
        return _response.data

    async def read(
        self, preprint_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PreprintsReadResponse:
        """
        Retrieves the details of a preprint.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested preprint, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        preprint_id : str
            The unique identifier of the preprint.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PreprintsReadResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.preprints.read(
                preprint_id="preprint_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read(preprint_id, request_options=request_options)
        return _response.data

    async def partial_update(
        self,
        preprint_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates the specified preprint by setting the values of the parameters passed. Any parameters not provided will be left unchanged.
        #### Returns
        Returns a JSON object with a `data` key containing the new representation of the updated preprint, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes]() to understand why this request may have failed.

        Parameters
        ----------
        preprint_id : str
            The unique identifier of the preprint.

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.preprints.partial_update(
                preprint_id="preprint_id",
                request={
                    "data": {
                        "attributes": {"doi": "{doi}"},
                        "id": "{preprint_id}",
                        "relationships": {
                            "primary_file": {
                                "data": {"id": "{file_id}", "type": "primary_files"}
                            }
                        },
                    }
                },
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.partial_update(preprint_id, request=request, request_options=request_options)
        return _response.data

    async def bibliographic_contributors_list(
        self, preprint_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[PreprintsBibliographicContributorsListResponseItem]:
        """
        A paginated list of the Preprint's Bibliographic Contributors, sorted by their index.
        Contributors are users who can make changes to the Preprint. Contributors with WRITE permissions may edit preprint details, and ADMIN Contributors may add or remove other Contributors.

        Contributors are categorized as either "bibliographic" or "non-bibliographic". From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed on the project overview page on the OSF, while non-bibliographic contributors are not.

        Note that if an anonymous view_only key is being used to view the list of contributors, the user relationship will not be exposed and the contributor ID will be an empty string.

        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of 10 contributors. Each resource in the array contains the full representation of the contributor, meaning additional requests to a contributor's detail view are not necessary. Additionally, the full representation of the user this contributor represents is automatically embedded within the `data` key of the response.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
        #### Filtering
        You can optionally request that the response only include contributors that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/preprints/y9jdt/contributors/?filter[bibliographic]=true.

        Contributors may be filtered by their `bibliographic` and `permission` attributes.

        Parameters
        ----------
        preprint_id : str
            The unique identifier of the preprint.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PreprintsBibliographicContributorsListResponseItem]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.preprints.bibliographic_contributors_list(
                preprint_id="preprint_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.bibliographic_contributors_list(preprint_id, request_options=request_options)
        return _response.data

    async def citation_list(
        self, preprint_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PreprintsCitationListResponse:
        """
        The citation details for a preprint, in CSL format.
        #### Returns
        Returns a JSON object with a `data` key that contains the representation of the details necessary for the preprint citation.

        Parameters
        ----------
        preprint_id : str
            The unique identifier of the preprint whose citation you wish to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PreprintsCitationListResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.preprints.citation_list(
                preprint_id="preprint_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.citation_list(preprint_id, request_options=request_options)
        return _response.data

    async def citation_read(
        self, preprint_id: str, style_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PreprintsCitationReadResponse:
        """
        The citation for a preprint in a specific style.
        #### Returns
        Returns a JSON object with a `data` key that contains the representation of the preprint citation, in the requested style.

        Parameters
        ----------
        preprint_id : str
            The unique identifier of the preprint.

        style_id : str
            The unique identifier of the citation style.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PreprintsCitationReadResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.preprints.citation_read(
                preprint_id="preprint_id",
                style_id="style_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.citation_read(preprint_id, style_id, request_options=request_options)
        return _response.data

    async def contributors_list(
        self, preprint_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[PreprintsContributorsListResponseItem]:
        """
        A paginated list of the Preprint's Contributors, sorted by their index.

        Contributors are users who can make changes to the Preprint. Contributors with WRITE permissions may edit preprint details, and ADMIN Contributors may add or remove other Contributors.

        Contributors are categorized as either "bibliographic" or "non-bibliographic". From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed on the project overview page on the OSF, while non-bibliographic contributors are not.

        Note that if an anonymous view_only key is being used to view the list of Contributors, the user relationship will not be exposed and the Contributor ID will be an empty string.

        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of 10 contributors. Each resource in the array contains the full representation of the contributor, meaning additional requests to a contributor's detail view are not necessary. Additionally, the full representation of the user this contributor represents is automatically embedded within the `data` key of the response.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
        #### Filtering
        You can optionally request that the response only include contributors that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/preprints/y9jdt/contributors/?filter[bibliographic]=true.

        Contributors may be filtered by their `bibliographic` and `permission` attributes.

        Parameters
        ----------
        preprint_id : str
            The unique identifier of the preprint.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PreprintsContributorsListResponseItem]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.preprints.contributors_list(
                preprint_id="preprint_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contributors_list(preprint_id, request_options=request_options)
        return _response.data

    async def contributors_create(
        self,
        preprint_id: str,
        *,
        attributes: typing.Optional[PreprintsContributorsCreateRequestAttributes] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Adds a contributor to a Preprint, effectively creating a relationship between the Preprint and a user.

        Contributors are users who can make changes to the Preprint. Contributors with WRITE permissions may edit preprint details, and ADMIN Contributors may add or remove other Contributors.

        Contributors are categorized as either "bibliographic" or "non-bibliographic" contributors. From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed on the project overview page on the OSF, while non-bibliographic contributors are not.
        #### Permissions
        Only project administrators can add contributors to a Preprint.
        #### Required
        A relationship object with a `data` key, containing the `users` type and valid user ID is required.

        All attributes describing the relationship between the Preprint and the user are optional.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the new contributor, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        preprint_id : str
            The unique identifier of the Preprint.

        attributes : typing.Optional[PreprintsContributorsCreateRequestAttributes]
            The properties of the contributor entity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.preprints.contributors_create(
                preprint_id="preprint_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contributors_create(
            preprint_id, attributes=attributes, request_options=request_options
        )
        return _response.data

    async def contributor_read(
        self, preprint_id: str, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Retrieves the details of a contributor on this Preprint.
        Contributors are categorized as either "bibliographic" or "non-bibliographic". From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed on the project overview page on the OSF, while non-bibliographic contributors are not.

        Note that if an anonymous view_only key is being used to view the list of contributors, the user relationship will not be exposed and the contributor ID will be an empty string.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested contributor, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        preprint_id : str
            The unique identifier of the Preprint.

        user_id : str
            The unique identifier of the user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.preprints.contributor_read(
                preprint_id="preprint_id",
                user_id="user_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contributor_read(preprint_id, user_id, request_options=request_options)
        return _response.data

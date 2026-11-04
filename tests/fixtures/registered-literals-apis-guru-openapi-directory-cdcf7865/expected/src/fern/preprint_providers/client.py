

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawPreprintProvidersClient, RawPreprintProvidersClient
from .types.preprint_provider_detail_response import PreprintProviderDetailResponse
from .types.preprint_provider_licenses_list_response import PreprintProviderLicensesListResponse
from .types.preprint_provider_list_response import PreprintProviderListResponse
from .types.preprint_provider_taxonomies_list_response import PreprintProviderTaxonomiesListResponse
from .types.preprint_providers_preprints_list_response_item import PreprintProvidersPreprintsListResponseItem


class PreprintProvidersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPreprintProvidersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPreprintProvidersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPreprintProvidersClient
        """
        return self._raw_client

    def preprint_provider_list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PreprintProviderListResponse:
        """

        A paginated list of all preprint providers. The returned preprint providers are sorted by their creation date, with the most recent preprints appearing first.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of 10 preprint providers. Each resource in the array is a separate preprint provider object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        This request should never return an error.
        #### Filtering
        You can optionally request that the response only include preprint providers that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/preprint_providers/?filter[id]=osf.

        Preprint Providers may be filtered by their `id`, `name`,  and `description`

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PreprintProviderListResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.preprint_providers.preprint_provider_list()
        """
        _response = self._raw_client.preprint_provider_list(request_options=request_options)
        return _response.data

    def preprint_provider_detail(
        self, preprint_provider_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PreprintProviderDetailResponse:
        """
        Retrieves the details of a preprint provider.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested preprint provider, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        #### Acceptable Subjects Structure
        Each preprint provider specifies acceptable subjects.
        `subjects_acceptable` is an array found in `attributes`.
        Subjects consist of general parent subjects (e.g., Engineering), more specific child subjects (e.g., Aerospace Engineering), and even more specific grandchild subjects (e.g., Aerodynamics and Fluid Mechanics). Subjects can only be nested 3 deep.


            "subjects_acceptable": [
                [
                    [
                        # Parent Subject:
                        # Architecture
                        "584240d954be81056ceca9e5",

                        # Child Subject:
                        # Architectural Engineering
                        "584240da54be81056cecac87"
                    ],
                    # Include all Architectural Engineering's children:
                    true
                ],
                [
                    [
                        # Parent Subject:
                        # Engineering
                        "584240da54be81056cecaca9",

                        # Child Subject:
                        # Aerospace Engineering
                        "584240db54be81056cecacd6",

                        # Grandchild Subject:
                        # Aerodynamics and Fluid Mechanics
                        "584240da54be81056cecaa74"
                    ],
                    # All nestings 3 deep must be false
                    false
                ]
            ]

        The above structure would allow Architecture, Architectural Engineering, all of Architectural Engineering's children, Engineering, Aerospace Engineering, and Aerodynamics and Fluid Mechanics.

        Parameters
        ----------
        preprint_provider_id : str
            The unique identifier of the preprint provider.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PreprintProviderDetailResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.preprint_providers.preprint_provider_detail(
            preprint_provider_id="preprint_provider_id",
        )
        """
        _response = self._raw_client.preprint_provider_detail(preprint_provider_id, request_options=request_options)
        return _response.data

    def preprint_provider_licenses_list(
        self, preprint_provider_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PreprintProviderLicensesListResponse:
        """

        A paginated list of the licenses allowed by a preprint provider.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of 10 preprint providers. Each resource in the array is a separate preprint provider object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        preprint_provider_id : str
            The unique identifier of the preprint provider.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PreprintProviderLicensesListResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.preprint_providers.preprint_provider_licenses_list(
            preprint_provider_id="preprint_provider_id",
        )
        """
        _response = self._raw_client.preprint_provider_licenses_list(
            preprint_provider_id, request_options=request_options
        )
        return _response.data

    def preprints_list(
        self, preprint_provider_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[PreprintProvidersPreprintsListResponseItem]:
        """

        A paginated list of preprints from the specified preprint provider. The returned preprints are sorted by their creation date, with the most recent preprints appearing first.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of 10 preprints. Each resource in the array is a separate preprint object.

        The `links` key contains a dictionary with keys that can be used for [pagination](#tag/Pagination).

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        #### Filtering
        You can optionally request that the response only include preprints that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/preprint_providers/osf/preprints/?filter[is_published]=true.

        Preprints may be filtered by their `id`, `is_published`, `date_created`, `date_modified`, and `provider`.

        Parameters
        ----------
        preprint_provider_id : str
            The unique identifier of the preprint provider.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PreprintProvidersPreprintsListResponseItem]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.preprint_providers.preprints_list(
            preprint_provider_id="preprint_provider_id",
        )
        """
        _response = self._raw_client.preprints_list(preprint_provider_id, request_options=request_options)
        return _response.data

    def preprint_provider_taxonomies_list(
        self, preprint_provider_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PreprintProviderTaxonomiesListResponse:
        """

        A paginated list of the taxonomies for a preprint provider. The returned preprint providers taxonomies are sorted by their creation date, with the most recent preprints appearing first.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of 10 preprint providers. Each resource in the array is a separate preprint provider object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        preprint_provider_id : str
            The unique identifier of the preprint provider.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PreprintProviderTaxonomiesListResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.preprint_providers.preprint_provider_taxonomies_list(
            preprint_provider_id="preprint_provider_id",
        )
        """
        _response = self._raw_client.preprint_provider_taxonomies_list(
            preprint_provider_id, request_options=request_options
        )
        return _response.data


class AsyncPreprintProvidersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPreprintProvidersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPreprintProvidersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPreprintProvidersClient
        """
        return self._raw_client

    async def preprint_provider_list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PreprintProviderListResponse:
        """

        A paginated list of all preprint providers. The returned preprint providers are sorted by their creation date, with the most recent preprints appearing first.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of 10 preprint providers. Each resource in the array is a separate preprint provider object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        This request should never return an error.
        #### Filtering
        You can optionally request that the response only include preprint providers that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/preprint_providers/?filter[id]=osf.

        Preprint Providers may be filtered by their `id`, `name`,  and `description`

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PreprintProviderListResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.preprint_providers.preprint_provider_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.preprint_provider_list(request_options=request_options)
        return _response.data

    async def preprint_provider_detail(
        self, preprint_provider_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PreprintProviderDetailResponse:
        """
        Retrieves the details of a preprint provider.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested preprint provider, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        #### Acceptable Subjects Structure
        Each preprint provider specifies acceptable subjects.
        `subjects_acceptable` is an array found in `attributes`.
        Subjects consist of general parent subjects (e.g., Engineering), more specific child subjects (e.g., Aerospace Engineering), and even more specific grandchild subjects (e.g., Aerodynamics and Fluid Mechanics). Subjects can only be nested 3 deep.


            "subjects_acceptable": [
                [
                    [
                        # Parent Subject:
                        # Architecture
                        "584240d954be81056ceca9e5",

                        # Child Subject:
                        # Architectural Engineering
                        "584240da54be81056cecac87"
                    ],
                    # Include all Architectural Engineering's children:
                    true
                ],
                [
                    [
                        # Parent Subject:
                        # Engineering
                        "584240da54be81056cecaca9",

                        # Child Subject:
                        # Aerospace Engineering
                        "584240db54be81056cecacd6",

                        # Grandchild Subject:
                        # Aerodynamics and Fluid Mechanics
                        "584240da54be81056cecaa74"
                    ],
                    # All nestings 3 deep must be false
                    false
                ]
            ]

        The above structure would allow Architecture, Architectural Engineering, all of Architectural Engineering's children, Engineering, Aerospace Engineering, and Aerodynamics and Fluid Mechanics.

        Parameters
        ----------
        preprint_provider_id : str
            The unique identifier of the preprint provider.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PreprintProviderDetailResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.preprint_providers.preprint_provider_detail(
                preprint_provider_id="preprint_provider_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.preprint_provider_detail(
            preprint_provider_id, request_options=request_options
        )
        return _response.data

    async def preprint_provider_licenses_list(
        self, preprint_provider_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PreprintProviderLicensesListResponse:
        """

        A paginated list of the licenses allowed by a preprint provider.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of 10 preprint providers. Each resource in the array is a separate preprint provider object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        preprint_provider_id : str
            The unique identifier of the preprint provider.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PreprintProviderLicensesListResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.preprint_providers.preprint_provider_licenses_list(
                preprint_provider_id="preprint_provider_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.preprint_provider_licenses_list(
            preprint_provider_id, request_options=request_options
        )
        return _response.data

    async def preprints_list(
        self, preprint_provider_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[PreprintProvidersPreprintsListResponseItem]:
        """

        A paginated list of preprints from the specified preprint provider. The returned preprints are sorted by their creation date, with the most recent preprints appearing first.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of 10 preprints. Each resource in the array is a separate preprint object.

        The `links` key contains a dictionary with keys that can be used for [pagination](#tag/Pagination).

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        #### Filtering
        You can optionally request that the response only include preprints that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/preprint_providers/osf/preprints/?filter[is_published]=true.

        Preprints may be filtered by their `id`, `is_published`, `date_created`, `date_modified`, and `provider`.

        Parameters
        ----------
        preprint_provider_id : str
            The unique identifier of the preprint provider.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PreprintProvidersPreprintsListResponseItem]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.preprint_providers.preprints_list(
                preprint_provider_id="preprint_provider_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.preprints_list(preprint_provider_id, request_options=request_options)
        return _response.data

    async def preprint_provider_taxonomies_list(
        self, preprint_provider_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PreprintProviderTaxonomiesListResponse:
        """

        A paginated list of the taxonomies for a preprint provider. The returned preprint providers taxonomies are sorted by their creation date, with the most recent preprints appearing first.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of 10 preprint providers. Each resource in the array is a separate preprint provider object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        preprint_provider_id : str
            The unique identifier of the preprint provider.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PreprintProviderTaxonomiesListResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.preprint_providers.preprint_provider_taxonomies_list(
                preprint_provider_id="preprint_provider_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.preprint_provider_taxonomies_list(
            preprint_provider_id, request_options=request_options
        )
        return _response.data



import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawInstitutionsClient, RawInstitutionsClient
from .types.institutions_detail_response_item import InstitutionsDetailResponseItem
from .types.institutions_list_response_item import InstitutionsListResponseItem
from .types.institutions_node_list_response_item import InstitutionsNodeListResponseItem
from .types.institutions_users_list_response_item import InstitutionsUsersListResponseItem


class InstitutionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawInstitutionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawInstitutionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawInstitutionsClient
        """
        return self._raw_client

    def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[InstitutionsListResponseItem]:
        """

        A paginated list of all verified institutions.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of 10 institutions. Each resource in the array is a separate institution object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        This request should never return an error.
        #### Filtering
        You can optionally request that the response only include institutions that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/institutions/?filter[id]=cos.

        Institutions may be filtered by their `id`, `name`, and `auth_url`

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[InstitutionsListResponseItem]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.institutions.list()
        """
        _response = self._raw_client.list(request_options=request_options)
        return _response.data

    def detail(
        self, institution_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[InstitutionsDetailResponseItem]:
        """
        Retrieves the details of an institution
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested institution, if the request was successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        institution_id : str
            The unique identifier of the institution you wish to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[InstitutionsDetailResponseItem]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.institutions.detail(
            institution_id="institution_id",
        )
        """
        _response = self._raw_client.detail(institution_id, request_options=request_options)
        return _response.data

    def node_list(
        self, institution_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[InstitutionsNodeListResponseItem]:
        """
        A paginated list of all nodes affiliated with an institution.
        #### Versioning
        As of version `2.2`, affiliated components (in addition to affiliated top-level projects) are returned from this endpoint.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of 10 nodes. Each resource in the array is a separate nodes object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
        #### Filtering
        You can optionally request that the response only include nodes that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/institutions/cos/nodes?filter[title]=science.

        Nodes may be filtered by their `id`, `title`, `description`, `public`, `tags`, `category`, `date_created`, `date_modified`, `root`, `parent`, `contributors`, and `preprint`

        Parameters
        ----------
        institution_id : str
            The unique identifier of the institution you wish to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[InstitutionsNodeListResponseItem]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.institutions.node_list(
            institution_id="institution_id",
        )
        """
        _response = self._raw_client.node_list(institution_id, request_options=request_options)
        return _response.data

    def registration_list(
        self, institution_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        A paginated list of all registrations affiliated with an institution.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of 10 registrations. Each resource in the array is a separate users object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
        #### Filtering
        You can optionally request that the response only include registrations that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/institutions/cos/registrations?filter[title]=science.

        Registrations may be filtered by their  `id`, `title`, `description`, `public`, `tags`, `category`, `date_created`, `date_modified`, `root`, `parent`, `contributors`, and `preprint`

        Parameters
        ----------
        institution_id : str
            The unique identifier of the institution you wish to retrieve.

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
        client.institutions.registration_list(
            institution_id="institution_id",
        )
        """
        _response = self._raw_client.registration_list(institution_id, request_options=request_options)
        return _response.data

    def users_list(
        self, institution_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[InstitutionsUsersListResponseItem]:
        """
        A paginated list of all users affiliated with an institution.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of 10 users. Each resource in the array is a separate users object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
        #### Filtering
        You can optionally request that the response only include users that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/institutions/cos/users?filter[family_name]=Nosek.

        Users may be filtered by their `id`, `full_name`, `given_name`, `middle_names`, and `family_name`

        Parameters
        ----------
        institution_id : str
            The unique identifier of the institution you wish to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[InstitutionsUsersListResponseItem]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.institutions.users_list(
            institution_id="institution_id",
        )
        """
        _response = self._raw_client.users_list(institution_id, request_options=request_options)
        return _response.data


class AsyncInstitutionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawInstitutionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawInstitutionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawInstitutionsClient
        """
        return self._raw_client

    async def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[InstitutionsListResponseItem]:
        """

        A paginated list of all verified institutions.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of 10 institutions. Each resource in the array is a separate institution object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        This request should never return an error.
        #### Filtering
        You can optionally request that the response only include institutions that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/institutions/?filter[id]=cos.

        Institutions may be filtered by their `id`, `name`, and `auth_url`

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[InstitutionsListResponseItem]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.institutions.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(request_options=request_options)
        return _response.data

    async def detail(
        self, institution_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[InstitutionsDetailResponseItem]:
        """
        Retrieves the details of an institution
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested institution, if the request was successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        institution_id : str
            The unique identifier of the institution you wish to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[InstitutionsDetailResponseItem]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.institutions.detail(
                institution_id="institution_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.detail(institution_id, request_options=request_options)
        return _response.data

    async def node_list(
        self, institution_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[InstitutionsNodeListResponseItem]:
        """
        A paginated list of all nodes affiliated with an institution.
        #### Versioning
        As of version `2.2`, affiliated components (in addition to affiliated top-level projects) are returned from this endpoint.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of 10 nodes. Each resource in the array is a separate nodes object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
        #### Filtering
        You can optionally request that the response only include nodes that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/institutions/cos/nodes?filter[title]=science.

        Nodes may be filtered by their `id`, `title`, `description`, `public`, `tags`, `category`, `date_created`, `date_modified`, `root`, `parent`, `contributors`, and `preprint`

        Parameters
        ----------
        institution_id : str
            The unique identifier of the institution you wish to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[InstitutionsNodeListResponseItem]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.institutions.node_list(
                institution_id="institution_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.node_list(institution_id, request_options=request_options)
        return _response.data

    async def registration_list(
        self, institution_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        A paginated list of all registrations affiliated with an institution.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of 10 registrations. Each resource in the array is a separate users object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
        #### Filtering
        You can optionally request that the response only include registrations that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/institutions/cos/registrations?filter[title]=science.

        Registrations may be filtered by their  `id`, `title`, `description`, `public`, `tags`, `category`, `date_created`, `date_modified`, `root`, `parent`, `contributors`, and `preprint`

        Parameters
        ----------
        institution_id : str
            The unique identifier of the institution you wish to retrieve.

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
            await client.institutions.registration_list(
                institution_id="institution_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.registration_list(institution_id, request_options=request_options)
        return _response.data

    async def users_list(
        self, institution_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[InstitutionsUsersListResponseItem]:
        """
        A paginated list of all users affiliated with an institution.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of 10 users. Each resource in the array is a separate users object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
        #### Filtering
        You can optionally request that the response only include users that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/institutions/cos/users?filter[family_name]=Nosek.

        Users may be filtered by their `id`, `full_name`, `given_name`, `middle_names`, and `family_name`

        Parameters
        ----------
        institution_id : str
            The unique identifier of the institution you wish to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[InstitutionsUsersListResponseItem]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.institutions.users_list(
                institution_id="institution_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.users_list(institution_id, request_options=request_options)
        return _response.data

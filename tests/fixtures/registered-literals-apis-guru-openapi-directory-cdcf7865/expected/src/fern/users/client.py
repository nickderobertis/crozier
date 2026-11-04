

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawUsersClient, RawUsersClient
from .types.users_addon_accounts_list_response_item import UsersAddonAccountsListResponseItem
from .types.users_addon_accounts_read_response import UsersAddonAccountsReadResponse
from .types.users_addons_list_response_item import UsersAddonsListResponseItem
from .types.users_addons_read_response import UsersAddonsReadResponse
from .types.users_institutions_list_response_item import UsersInstitutionsListResponseItem
from .types.users_list_response_item import UsersListResponseItem
from .types.users_nodes_list_response_item import UsersNodesListResponseItem
from .types.users_partial_update_request_attributes import UsersPartialUpdateRequestAttributes
from .types.users_preprints_list_response_item import UsersPreprintsListResponseItem
from .types.users_read_response import UsersReadResponse


OMIT = typing.cast(typing.Any, ...)


class UsersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUsersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUsersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUsersClient
        """
        return self._raw_client

    def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[UsersListResponseItem]:
        """

        A paginated list of all users registered on the OSF. The returned users are sorted by their `date_registered`, with the most recently registered users appearing first.

        The subroute `/users/me/` is a special endpoint that always points to the currently logged-in user.
        #### Versioning
        As of version `2.3`, merged users will not be returned from this endpoint.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of 10 users. Each resource in the array is a separate users object and contains the full representation of the user, meaning additional requests to a user's detail view are not necessary.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        This request should never return an error.
        #### Filtering
        You can optionally request that the response only include nodes that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/users/?filter[family_name]=Nosek.

        Users may be filtered by their `id`, `full_name`, `given_name`, `middle_name`, or `family_name`.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[UsersListResponseItem]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.list()
        """
        _response = self._raw_client.list(request_options=request_options)
        return _response.data

    def read(self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> UsersReadResponse:
        """
        Retrieves the details of a given users.

        The returned information includes the user's bibliographic information and the date the user was registered.

        Additionally, relationships to the list of institutions with which the user is affiliated, and to the list of nodes which the user contributes to (that the requesting user has permission to see) are returned.

        If `me` is given as the `user_id` in the request path, the record of the currently logged-in user will be returned.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested user, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        user_id : str
            The unique identifier of the user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UsersReadResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.read(
            user_id="user_id",
        )
        """
        _response = self._raw_client.read(user_id, request_options=request_options)
        return _response.data

    def partial_update(
        self,
        user_id: str,
        *,
        attributes: UsersPartialUpdateRequestAttributes,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates a user by setting the values of the attributes specified in the request body. Any unspecified attributes will be left unchanged.

        Users can be updated with either a **PUT** or **PATCH** request. The `full_name` field is mandatory in a **PUT** request, and optional in a **PATCH**.

        **Note**: if you make a PUT/PATCH request to the `/users/me/` endpoint, you must still provide your full user ID in the ID field of the request. We do not support using the `me` alias in request bodies at this time.
        #### Returns
        Returns a JSON object with a `data` key containing the new representation of the updated node, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        user_id : str
            The unique identifier of the user.

        attributes : UsersPartialUpdateRequestAttributes
            The properties of the user entity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.users import UsersPartialUpdateRequestAttributes

        from fern import FernApi

        client = FernApi()
        client.users.partial_update(
            user_id="user_id",
            attributes=UsersPartialUpdateRequestAttributes(
                full_name="full_name",
            ),
        )
        """
        _response = self._raw_client.partial_update(user_id, attributes=attributes, request_options=request_options)
        return _response.data

    def addons_list(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[UsersAddonsListResponseItem]:
        """

        A paginated list of authorized user addons

        #### Permissions

        User addons are visible only to the user that authorized the addon.

        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of up to 10 addons. Each resource in the array is a separate addon object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Attempting to request the accounts for an addon that is not enabled will result in a **404 Not Found** response.

        Parameters
        ----------
        user_id : str
            The unique identifier of the user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[UsersAddonsListResponseItem]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.addons_list(
            user_id="user_id",
        )
        """
        _response = self._raw_client.addons_list(user_id, request_options=request_options)
        return _response.data

    def addons_read(
        self, user_id: str, provider: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UsersAddonsReadResponse:
        """
        Retrieves the details of an authorized user addon

        #### Permissions

        User addons are visible only to the user that authorized the addon.

        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested user addon, if the request was successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Attempting to request the accounts for an addon that is not enabled will result in a **404 Not Found** response.

        Parameters
        ----------
        user_id : str
            The unique identifier of the user.

        provider : str
            The unique identifier of the addon provider.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UsersAddonsReadResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.addons_read(
            user_id="user_id",
            provider="provider",
        )
        """
        _response = self._raw_client.addons_read(user_id, provider, request_options=request_options)
        return _response.data

    def addon_accounts_list(
        self, user_id: str, provider: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[UsersAddonAccountsListResponseItem]:
        """

        A paginated list of addon accounts authorized by this user.

        #### Permissions

        Addon accounts are visible only to the user that authorized the account.

        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of at most 10 addon account objects. Each resource in the array is a separate  addon account object and contains the full representation of the addon account.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        Parameters
        ----------
        user_id : str
            The unique identifier of the user.

        provider : str
            The unique identifier of the addon provider.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[UsersAddonAccountsListResponseItem]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.addon_accounts_list(
            user_id="user_id",
            provider="provider",
        )
        """
        _response = self._raw_client.addon_accounts_list(user_id, provider, request_options=request_options)
        return _response.data

    def addon_accounts_read(
        self, user_id: str, provider: str, account_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UsersAddonAccountsReadResponse:
        """
        Retrieves the details of an addon account

        #### Permissions

        Addon accounts are visible only to the user that authorized the account.

        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested addon account, if the request was successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        user_id : str
            The unique identifier of the user.

        provider : str
            The unique identifier of the addon provider.

        account_id : str
            The unique identifier of the addon account.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UsersAddonAccountsReadResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.addon_accounts_read(
            user_id="user_id",
            provider="provider",
            account_id="account_id",
        )
        """
        _response = self._raw_client.addon_accounts_read(user_id, provider, account_id, request_options=request_options)
        return _response.data

    def institutions_list(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[UsersInstitutionsListResponseItem]:
        """
        A paginated list of institutions that the user is affiliated with.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of 10 institutions. Each resource in the array is a complete institution object and contains the full representation of the institution, meaning additional requests to a institution's detail view are not necessary.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        Parameters
        ----------
        user_id : str
            The unique identifier of the user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[UsersInstitutionsListResponseItem]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.institutions_list(
            user_id="user_id",
        )
        """
        _response = self._raw_client.institutions_list(user_id, request_options=request_options)
        return _response.data

    def nodes_list(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[UsersNodesListResponseItem]:
        """
        A paginated list of nodes that the user is a contributor to. The returned nodes are sorted by their `date_modified`, with the most recently updated nodes appearing first.

        If the user ID in the path is the same as the logged-in user, all nodes will be returned. Otherwise, only the user's public nodes will be returned.

        User registrations are not available at this endpoint.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of 10 nodes. Each resource in the array is a separate node object and contains the full representation of the node, meaning additional requests to a node's detail view are not necessary.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
        #### Filtering
        You can optionally request that the response only include nodes that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/users/cdi38/nodes/?filter[title]=open.

        Nodes may be filtered by their `id`, `title`, `category`, `description`, `public`, `tags`, `date_created`, `date_modified`, `root`, `parent`, `preprint`, and `contributors`.

        Parameters
        ----------
        user_id : str
            The unique identifier of the user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[UsersNodesListResponseItem]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.nodes_list(
            user_id="user_id",
        )
        """
        _response = self._raw_client.nodes_list(user_id, request_options=request_options)
        return _response.data

    def preprints_list(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[UsersPreprintsListResponseItem]:
        """
        A paginated list of preprints that the user contributes to. The returned preprints are sorted by their creation date, with the most recent preprints appearing first.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of 10 preprints. Each resource in the array is a complete preprint object and contains the full representation of the preprint, meaning additional requests to a preprint's detail view are not necessary.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
        #### Filtering
        You can optionally request that the response only include preprints that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/users/cdi38/preprints/?filter[provider]=psyarxiv.

        Preprints may be filtered by their `id`, `is_published`, `date_created`, `date_modified`, and `provider`.

        Parameters
        ----------
        user_id : str
            The unique identifier of the user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[UsersPreprintsListResponseItem]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.preprints_list(
            user_id="user_id",
        )
        """
        _response = self._raw_client.preprints_list(user_id, request_options=request_options)
        return _response.data

    def registrations_list(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        A paginated list of registrations that the user is a contributor to. The returned registrations are sorted by their `date_modified`, with the most recently updated registrations appearing first.

        If the user ID in the path is the same as the logged-in user, all registrations will be returned. Otherwise, only the user's public registrations will be returned.

        User nodes are not available at this endpoint.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of 10 registrations. Each resource in the array is a separate registration object and contains the full representation of the registration, meaning additional requests to a registration's detail view are not necessary.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
        #### Filtering
        You can optionally request that the response only include registrations that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/users/cdi38/registrations/?filter[title]=replication.

        Registrations may be filtered by their `id`, `title`, `category`, `description`, `public`, `tags`, `date_created`, `date_modified`, `root`, `parent`, and `contributors`.

        Parameters
        ----------
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
        client.users.registrations_list(
            user_id="user_id",
        )
        """
        _response = self._raw_client.registrations_list(user_id, request_options=request_options)
        return _response.data


class AsyncUsersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUsersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUsersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUsersClient
        """
        return self._raw_client

    async def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[UsersListResponseItem]:
        """

        A paginated list of all users registered on the OSF. The returned users are sorted by their `date_registered`, with the most recently registered users appearing first.

        The subroute `/users/me/` is a special endpoint that always points to the currently logged-in user.
        #### Versioning
        As of version `2.3`, merged users will not be returned from this endpoint.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of 10 users. Each resource in the array is a separate users object and contains the full representation of the user, meaning additional requests to a user's detail view are not necessary.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        This request should never return an error.
        #### Filtering
        You can optionally request that the response only include nodes that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/users/?filter[family_name]=Nosek.

        Users may be filtered by their `id`, `full_name`, `given_name`, `middle_name`, or `family_name`.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[UsersListResponseItem]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(request_options=request_options)
        return _response.data

    async def read(self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> UsersReadResponse:
        """
        Retrieves the details of a given users.

        The returned information includes the user's bibliographic information and the date the user was registered.

        Additionally, relationships to the list of institutions with which the user is affiliated, and to the list of nodes which the user contributes to (that the requesting user has permission to see) are returned.

        If `me` is given as the `user_id` in the request path, the record of the currently logged-in user will be returned.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested user, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        user_id : str
            The unique identifier of the user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UsersReadResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.read(
                user_id="user_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read(user_id, request_options=request_options)
        return _response.data

    async def partial_update(
        self,
        user_id: str,
        *,
        attributes: UsersPartialUpdateRequestAttributes,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates a user by setting the values of the attributes specified in the request body. Any unspecified attributes will be left unchanged.

        Users can be updated with either a **PUT** or **PATCH** request. The `full_name` field is mandatory in a **PUT** request, and optional in a **PATCH**.

        **Note**: if you make a PUT/PATCH request to the `/users/me/` endpoint, you must still provide your full user ID in the ID field of the request. We do not support using the `me` alias in request bodies at this time.
        #### Returns
        Returns a JSON object with a `data` key containing the new representation of the updated node, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        user_id : str
            The unique identifier of the user.

        attributes : UsersPartialUpdateRequestAttributes
            The properties of the user entity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.users import UsersPartialUpdateRequestAttributes

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.partial_update(
                user_id="user_id",
                attributes=UsersPartialUpdateRequestAttributes(
                    full_name="full_name",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.partial_update(
            user_id, attributes=attributes, request_options=request_options
        )
        return _response.data

    async def addons_list(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[UsersAddonsListResponseItem]:
        """

        A paginated list of authorized user addons

        #### Permissions

        User addons are visible only to the user that authorized the addon.

        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of up to 10 addons. Each resource in the array is a separate addon object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Attempting to request the accounts for an addon that is not enabled will result in a **404 Not Found** response.

        Parameters
        ----------
        user_id : str
            The unique identifier of the user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[UsersAddonsListResponseItem]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.addons_list(
                user_id="user_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.addons_list(user_id, request_options=request_options)
        return _response.data

    async def addons_read(
        self, user_id: str, provider: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UsersAddonsReadResponse:
        """
        Retrieves the details of an authorized user addon

        #### Permissions

        User addons are visible only to the user that authorized the addon.

        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested user addon, if the request was successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Attempting to request the accounts for an addon that is not enabled will result in a **404 Not Found** response.

        Parameters
        ----------
        user_id : str
            The unique identifier of the user.

        provider : str
            The unique identifier of the addon provider.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UsersAddonsReadResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.addons_read(
                user_id="user_id",
                provider="provider",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.addons_read(user_id, provider, request_options=request_options)
        return _response.data

    async def addon_accounts_list(
        self, user_id: str, provider: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[UsersAddonAccountsListResponseItem]:
        """

        A paginated list of addon accounts authorized by this user.

        #### Permissions

        Addon accounts are visible only to the user that authorized the account.

        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of at most 10 addon account objects. Each resource in the array is a separate  addon account object and contains the full representation of the addon account.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        Parameters
        ----------
        user_id : str
            The unique identifier of the user.

        provider : str
            The unique identifier of the addon provider.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[UsersAddonAccountsListResponseItem]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.addon_accounts_list(
                user_id="user_id",
                provider="provider",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.addon_accounts_list(user_id, provider, request_options=request_options)
        return _response.data

    async def addon_accounts_read(
        self, user_id: str, provider: str, account_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UsersAddonAccountsReadResponse:
        """
        Retrieves the details of an addon account

        #### Permissions

        Addon accounts are visible only to the user that authorized the account.

        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested addon account, if the request was successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        user_id : str
            The unique identifier of the user.

        provider : str
            The unique identifier of the addon provider.

        account_id : str
            The unique identifier of the addon account.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UsersAddonAccountsReadResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.addon_accounts_read(
                user_id="user_id",
                provider="provider",
                account_id="account_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.addon_accounts_read(
            user_id, provider, account_id, request_options=request_options
        )
        return _response.data

    async def institutions_list(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[UsersInstitutionsListResponseItem]:
        """
        A paginated list of institutions that the user is affiliated with.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of 10 institutions. Each resource in the array is a complete institution object and contains the full representation of the institution, meaning additional requests to a institution's detail view are not necessary.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        Parameters
        ----------
        user_id : str
            The unique identifier of the user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[UsersInstitutionsListResponseItem]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.institutions_list(
                user_id="user_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.institutions_list(user_id, request_options=request_options)
        return _response.data

    async def nodes_list(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[UsersNodesListResponseItem]:
        """
        A paginated list of nodes that the user is a contributor to. The returned nodes are sorted by their `date_modified`, with the most recently updated nodes appearing first.

        If the user ID in the path is the same as the logged-in user, all nodes will be returned. Otherwise, only the user's public nodes will be returned.

        User registrations are not available at this endpoint.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of 10 nodes. Each resource in the array is a separate node object and contains the full representation of the node, meaning additional requests to a node's detail view are not necessary.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
        #### Filtering
        You can optionally request that the response only include nodes that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/users/cdi38/nodes/?filter[title]=open.

        Nodes may be filtered by their `id`, `title`, `category`, `description`, `public`, `tags`, `date_created`, `date_modified`, `root`, `parent`, `preprint`, and `contributors`.

        Parameters
        ----------
        user_id : str
            The unique identifier of the user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[UsersNodesListResponseItem]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.nodes_list(
                user_id="user_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.nodes_list(user_id, request_options=request_options)
        return _response.data

    async def preprints_list(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[UsersPreprintsListResponseItem]:
        """
        A paginated list of preprints that the user contributes to. The returned preprints are sorted by their creation date, with the most recent preprints appearing first.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of 10 preprints. Each resource in the array is a complete preprint object and contains the full representation of the preprint, meaning additional requests to a preprint's detail view are not necessary.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
        #### Filtering
        You can optionally request that the response only include preprints that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/users/cdi38/preprints/?filter[provider]=psyarxiv.

        Preprints may be filtered by their `id`, `is_published`, `date_created`, `date_modified`, and `provider`.

        Parameters
        ----------
        user_id : str
            The unique identifier of the user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[UsersPreprintsListResponseItem]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.preprints_list(
                user_id="user_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.preprints_list(user_id, request_options=request_options)
        return _response.data

    async def registrations_list(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        A paginated list of registrations that the user is a contributor to. The returned registrations are sorted by their `date_modified`, with the most recently updated registrations appearing first.

        If the user ID in the path is the same as the logged-in user, all registrations will be returned. Otherwise, only the user's public registrations will be returned.

        User nodes are not available at this endpoint.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of 10 registrations. Each resource in the array is a separate registration object and contains the full representation of the registration, meaning additional requests to a registration's detail view are not necessary.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
        #### Filtering
        You can optionally request that the response only include registrations that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/users/cdi38/registrations/?filter[title]=replication.

        Registrations may be filtered by their `id`, `title`, `category`, `description`, `public`, `tags`, `date_created`, `date_modified`, `root`, `parent`, and `contributors`.

        Parameters
        ----------
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
            await client.users.registrations_list(
                user_id="user_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.registrations_list(user_id, request_options=request_options)
        return _response.data

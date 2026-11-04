

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
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
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawUsersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[UsersListResponseItem]]:
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
        HttpResponse[typing.List[UsersListResponseItem]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "users/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[UsersListResponseItem],
                    parse_obj_as(
                        type_=typing.List[UsersListResponseItem],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def read(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UsersReadResponse]:
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
        HttpResponse[UsersReadResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"users/{encode_path_param(user_id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UsersReadResponse,
                    parse_obj_as(
                        type_=UsersReadResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def partial_update(
        self,
        user_id: str,
        *,
        attributes: UsersPartialUpdateRequestAttributes,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"users/{encode_path_param(user_id)}/",
            method="PATCH",
            json={
                "attributes": convert_and_respect_annotation_metadata(
                    object_=attributes, annotation=UsersPartialUpdateRequestAttributes, direction="write"
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
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def addons_list(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[UsersAddonsListResponseItem]]:
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
        HttpResponse[typing.List[UsersAddonsListResponseItem]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"users/{encode_path_param(user_id)}/addons/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[UsersAddonsListResponseItem],
                    parse_obj_as(
                        type_=typing.List[UsersAddonsListResponseItem],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def addons_read(
        self, user_id: str, provider: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UsersAddonsReadResponse]:
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
        HttpResponse[UsersAddonsReadResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"users/{encode_path_param(user_id)}/addons/{encode_path_param(provider)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UsersAddonsReadResponse,
                    parse_obj_as(
                        type_=UsersAddonsReadResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def addon_accounts_list(
        self, user_id: str, provider: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[UsersAddonAccountsListResponseItem]]:
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
        HttpResponse[typing.List[UsersAddonAccountsListResponseItem]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"users/{encode_path_param(user_id)}/addons/{encode_path_param(provider)}/accounts/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[UsersAddonAccountsListResponseItem],
                    parse_obj_as(
                        type_=typing.List[UsersAddonAccountsListResponseItem],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def addon_accounts_read(
        self, user_id: str, provider: str, account_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UsersAddonAccountsReadResponse]:
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
        HttpResponse[UsersAddonAccountsReadResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"users/{encode_path_param(user_id)}/addons/{encode_path_param(provider)}/accounts/{encode_path_param(account_id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UsersAddonAccountsReadResponse,
                    parse_obj_as(
                        type_=UsersAddonAccountsReadResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def institutions_list(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[UsersInstitutionsListResponseItem]]:
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
        HttpResponse[typing.List[UsersInstitutionsListResponseItem]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"users/{encode_path_param(user_id)}/institutions/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[UsersInstitutionsListResponseItem],
                    parse_obj_as(
                        type_=typing.List[UsersInstitutionsListResponseItem],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def nodes_list(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[UsersNodesListResponseItem]]:
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
        HttpResponse[typing.List[UsersNodesListResponseItem]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"users/{encode_path_param(user_id)}/nodes/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[UsersNodesListResponseItem],
                    parse_obj_as(
                        type_=typing.List[UsersNodesListResponseItem],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def preprints_list(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[UsersPreprintsListResponseItem]]:
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
        HttpResponse[typing.List[UsersPreprintsListResponseItem]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"users/{encode_path_param(user_id)}/preprints/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[UsersPreprintsListResponseItem],
                    parse_obj_as(
                        type_=typing.List[UsersPreprintsListResponseItem],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def registrations_list(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Any]:
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
        HttpResponse[typing.Any]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"users/{encode_path_param(user_id)}/registrations/",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawUsersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[UsersListResponseItem]]:
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
        AsyncHttpResponse[typing.List[UsersListResponseItem]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "users/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[UsersListResponseItem],
                    parse_obj_as(
                        type_=typing.List[UsersListResponseItem],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def read(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UsersReadResponse]:
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
        AsyncHttpResponse[UsersReadResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"users/{encode_path_param(user_id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UsersReadResponse,
                    parse_obj_as(
                        type_=UsersReadResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def partial_update(
        self,
        user_id: str,
        *,
        attributes: UsersPartialUpdateRequestAttributes,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"users/{encode_path_param(user_id)}/",
            method="PATCH",
            json={
                "attributes": convert_and_respect_annotation_metadata(
                    object_=attributes, annotation=UsersPartialUpdateRequestAttributes, direction="write"
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
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def addons_list(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[UsersAddonsListResponseItem]]:
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
        AsyncHttpResponse[typing.List[UsersAddonsListResponseItem]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"users/{encode_path_param(user_id)}/addons/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[UsersAddonsListResponseItem],
                    parse_obj_as(
                        type_=typing.List[UsersAddonsListResponseItem],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def addons_read(
        self, user_id: str, provider: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UsersAddonsReadResponse]:
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
        AsyncHttpResponse[UsersAddonsReadResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"users/{encode_path_param(user_id)}/addons/{encode_path_param(provider)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UsersAddonsReadResponse,
                    parse_obj_as(
                        type_=UsersAddonsReadResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def addon_accounts_list(
        self, user_id: str, provider: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[UsersAddonAccountsListResponseItem]]:
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
        AsyncHttpResponse[typing.List[UsersAddonAccountsListResponseItem]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"users/{encode_path_param(user_id)}/addons/{encode_path_param(provider)}/accounts/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[UsersAddonAccountsListResponseItem],
                    parse_obj_as(
                        type_=typing.List[UsersAddonAccountsListResponseItem],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def addon_accounts_read(
        self, user_id: str, provider: str, account_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UsersAddonAccountsReadResponse]:
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
        AsyncHttpResponse[UsersAddonAccountsReadResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"users/{encode_path_param(user_id)}/addons/{encode_path_param(provider)}/accounts/{encode_path_param(account_id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UsersAddonAccountsReadResponse,
                    parse_obj_as(
                        type_=UsersAddonAccountsReadResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def institutions_list(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[UsersInstitutionsListResponseItem]]:
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
        AsyncHttpResponse[typing.List[UsersInstitutionsListResponseItem]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"users/{encode_path_param(user_id)}/institutions/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[UsersInstitutionsListResponseItem],
                    parse_obj_as(
                        type_=typing.List[UsersInstitutionsListResponseItem],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def nodes_list(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[UsersNodesListResponseItem]]:
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
        AsyncHttpResponse[typing.List[UsersNodesListResponseItem]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"users/{encode_path_param(user_id)}/nodes/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[UsersNodesListResponseItem],
                    parse_obj_as(
                        type_=typing.List[UsersNodesListResponseItem],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def preprints_list(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[UsersPreprintsListResponseItem]]:
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
        AsyncHttpResponse[typing.List[UsersPreprintsListResponseItem]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"users/{encode_path_param(user_id)}/preprints/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[UsersPreprintsListResponseItem],
                    parse_obj_as(
                        type_=typing.List[UsersPreprintsListResponseItem],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def registrations_list(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
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
        AsyncHttpResponse[typing.Any]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"users/{encode_path_param(user_id)}/registrations/",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)



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
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.client import Client
from ..types.create_client_endpoint_output import CreateClientEndpointOutput
from ..types.get_clients_request_client_id import GetClientsRequestClientId
from ..types.get_clients_request_created_at import GetClientsRequestCreatedAt
from ..types.get_clients_request_display_name import GetClientsRequestDisplayName
from ..types.json_web_key_set import JsonWebKeySet
from ..types.query_clients_endpoint_paged_result_of_output import QueryClientsEndpointPagedResultOfOutput
from ..types.validation_problem_details import ValidationProblemDetails
from .types.get_clients_request_logic import GetClientsRequestLogic
from .types.get_clients_request_sort_item import GetClientsRequestSortItem
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawClientClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def creates_a_new_client_for_the_current_customer(
        self,
        *,
        display_name: typing.Optional[str] = OMIT,
        organization_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateClientEndpointOutput]:
        """
        Parameters
        ----------
        display_name : typing.Optional[str]
            An optional display name for the client.

        organization_id : typing.Optional[str]
            The organization to authorize the client for. Defaults to the caller's active organization.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateClientEndpointOutput]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "client",
            method="POST",
            json={
                "displayName": display_name,
                "organizationId": organization_id,
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
                    CreateClientEndpointOutput,
                    parse_obj_as(
                        type_=CreateClientEndpointOutput,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationProblemDetails,
                        parse_obj_as(
                            type_=ValidationProblemDetails,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def identity_get_client(
        self, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Client]:
        """
        Parameters
        ----------
        client_id : str
            The id of the client to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Client]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"client/{encode_path_param(client_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Client,
                    parse_obj_as(
                        type_=Client,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationProblemDetails,
                        parse_obj_as(
                            type_=ValidationProblemDetails,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def deletes_a_client(
        self, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        client_id : str
            The id of the client to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"client/{encode_path_param(client_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationProblemDetails,
                        parse_obj_as(
                            type_=ValidationProblemDetails,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def queries_clients_for_the_current_customer(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sort: typing.Optional[
            typing.Union[GetClientsRequestSortItem, typing.Sequence[GetClientsRequestSortItem]]
        ] = None,
        client_id: typing.Optional[GetClientsRequestClientId] = None,
        display_name: typing.Optional[GetClientsRequestDisplayName] = None,
        created_at: typing.Optional[GetClientsRequestCreatedAt] = None,
        logic: typing.Optional[GetClientsRequestLogic] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[QueryClientsEndpointPagedResultOfOutput]:
        """
        Clients are service credentials that allow automated processes to authenticate against the API.

        Parameters
        ----------
        page : typing.Optional[int]
            The 1-based page index.

        page_size : typing.Optional[int]
            The number of items per page.

        sort : typing.Optional[typing.Union[GetClientsRequestSortItem, typing.Sequence[GetClientsRequestSortItem]]]
            Sort fields. Prefix with - for descending order (e.g. -created_at).

        client_id : typing.Optional[GetClientsRequestClientId]
            Filter by client_id.

        display_name : typing.Optional[GetClientsRequestDisplayName]
            Filter by display_name.

        created_at : typing.Optional[GetClientsRequestCreatedAt]
            Filter by created_at.

        logic : typing.Optional[GetClientsRequestLogic]
            How to combine the field filters: "and" (default) requires every filter to match, "or" requires any of them to match.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[QueryClientsEndpointPagedResultOfOutput]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "clients",
            method="GET",
            params={
                "page": page,
                "page_size": page_size,
                "sort": sort,
                "client_id": convert_and_respect_annotation_metadata(
                    object_=client_id, annotation=GetClientsRequestClientId, direction="write"
                ),
                "display_name": convert_and_respect_annotation_metadata(
                    object_=display_name, annotation=GetClientsRequestDisplayName, direction="write"
                ),
                "created_at": convert_and_respect_annotation_metadata(
                    object_=created_at, annotation=GetClientsRequestCreatedAt, direction="write"
                ),
                "logic": logic,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    QueryClientsEndpointPagedResultOfOutput,
                    parse_obj_as(
                        type_=QueryClientsEndpointPagedResultOfOutput,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationProblemDetails,
                        parse_obj_as(
                            type_=ValidationProblemDetails,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def registers_a_new_client_using_the_open_id_connect_dynamic_client_registration_protocol(
        self,
        *,
        redirect_uris: typing.Optional[typing.Sequence[str]] = OMIT,
        grant_types: typing.Optional[typing.Sequence[str]] = OMIT,
        response_types: typing.Optional[typing.Sequence[str]] = OMIT,
        client_id: typing.Optional[str] = OMIT,
        client_name: typing.Optional[str] = OMIT,
        client_uri: typing.Optional[str] = OMIT,
        logo_uri: typing.Optional[str] = OMIT,
        scope: typing.Optional[str] = OMIT,
        contacts: typing.Optional[typing.Sequence[str]] = OMIT,
        tos_uri: typing.Optional[str] = OMIT,
        policy_uri: typing.Optional[str] = OMIT,
        jwks_uri: typing.Optional[str] = OMIT,
        jwks: typing.Optional[JsonWebKeySet] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Follows RFC 7591.

        Parameters
        ----------
        redirect_uris : typing.Optional[typing.Sequence[str]]

        grant_types : typing.Optional[typing.Sequence[str]]

        response_types : typing.Optional[typing.Sequence[str]]

        client_id : typing.Optional[str]

        client_name : typing.Optional[str]

        client_uri : typing.Optional[str]

        logo_uri : typing.Optional[str]

        scope : typing.Optional[str]
            String containing a space-separated list of scope values
             that the client can use when requesting access tokens.

        contacts : typing.Optional[typing.Sequence[str]]
            Array of strings representing ways to contact people responsible for this client,
             typically email addresses.

        tos_uri : typing.Optional[str]

        policy_uri : typing.Optional[str]

        jwks_uri : typing.Optional[str]

        jwks : typing.Optional[JsonWebKeySet]
            Client's JSON Web Key Set [RFC7517] document value, which contains the client's public keys.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "client/register",
            method="POST",
            json={
                "redirect_uris": redirect_uris,
                "grant_types": grant_types,
                "response_types": response_types,
                "client_id": client_id,
                "client_name": client_name,
                "client_uri": client_uri,
                "logo_uri": logo_uri,
                "scope": scope,
                "contacts": contacts,
                "tos_uri": tos_uri,
                "policy_uri": policy_uri,
                "jwks_uri": jwks_uri,
                "jwks": convert_and_respect_annotation_metadata(
                    object_=jwks, annotation=JsonWebKeySet, direction="write"
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


class AsyncRawClientClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def creates_a_new_client_for_the_current_customer(
        self,
        *,
        display_name: typing.Optional[str] = OMIT,
        organization_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateClientEndpointOutput]:
        """
        Parameters
        ----------
        display_name : typing.Optional[str]
            An optional display name for the client.

        organization_id : typing.Optional[str]
            The organization to authorize the client for. Defaults to the caller's active organization.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateClientEndpointOutput]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "client",
            method="POST",
            json={
                "displayName": display_name,
                "organizationId": organization_id,
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
                    CreateClientEndpointOutput,
                    parse_obj_as(
                        type_=CreateClientEndpointOutput,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationProblemDetails,
                        parse_obj_as(
                            type_=ValidationProblemDetails,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def identity_get_client(
        self, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Client]:
        """
        Parameters
        ----------
        client_id : str
            The id of the client to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Client]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"client/{encode_path_param(client_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Client,
                    parse_obj_as(
                        type_=Client,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationProblemDetails,
                        parse_obj_as(
                            type_=ValidationProblemDetails,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def deletes_a_client(
        self, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        client_id : str
            The id of the client to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"client/{encode_path_param(client_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationProblemDetails,
                        parse_obj_as(
                            type_=ValidationProblemDetails,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def queries_clients_for_the_current_customer(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sort: typing.Optional[
            typing.Union[GetClientsRequestSortItem, typing.Sequence[GetClientsRequestSortItem]]
        ] = None,
        client_id: typing.Optional[GetClientsRequestClientId] = None,
        display_name: typing.Optional[GetClientsRequestDisplayName] = None,
        created_at: typing.Optional[GetClientsRequestCreatedAt] = None,
        logic: typing.Optional[GetClientsRequestLogic] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[QueryClientsEndpointPagedResultOfOutput]:
        """
        Clients are service credentials that allow automated processes to authenticate against the API.

        Parameters
        ----------
        page : typing.Optional[int]
            The 1-based page index.

        page_size : typing.Optional[int]
            The number of items per page.

        sort : typing.Optional[typing.Union[GetClientsRequestSortItem, typing.Sequence[GetClientsRequestSortItem]]]
            Sort fields. Prefix with - for descending order (e.g. -created_at).

        client_id : typing.Optional[GetClientsRequestClientId]
            Filter by client_id.

        display_name : typing.Optional[GetClientsRequestDisplayName]
            Filter by display_name.

        created_at : typing.Optional[GetClientsRequestCreatedAt]
            Filter by created_at.

        logic : typing.Optional[GetClientsRequestLogic]
            How to combine the field filters: "and" (default) requires every filter to match, "or" requires any of them to match.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[QueryClientsEndpointPagedResultOfOutput]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "clients",
            method="GET",
            params={
                "page": page,
                "page_size": page_size,
                "sort": sort,
                "client_id": convert_and_respect_annotation_metadata(
                    object_=client_id, annotation=GetClientsRequestClientId, direction="write"
                ),
                "display_name": convert_and_respect_annotation_metadata(
                    object_=display_name, annotation=GetClientsRequestDisplayName, direction="write"
                ),
                "created_at": convert_and_respect_annotation_metadata(
                    object_=created_at, annotation=GetClientsRequestCreatedAt, direction="write"
                ),
                "logic": logic,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    QueryClientsEndpointPagedResultOfOutput,
                    parse_obj_as(
                        type_=QueryClientsEndpointPagedResultOfOutput,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationProblemDetails,
                        parse_obj_as(
                            type_=ValidationProblemDetails,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def registers_a_new_client_using_the_open_id_connect_dynamic_client_registration_protocol(
        self,
        *,
        redirect_uris: typing.Optional[typing.Sequence[str]] = OMIT,
        grant_types: typing.Optional[typing.Sequence[str]] = OMIT,
        response_types: typing.Optional[typing.Sequence[str]] = OMIT,
        client_id: typing.Optional[str] = OMIT,
        client_name: typing.Optional[str] = OMIT,
        client_uri: typing.Optional[str] = OMIT,
        logo_uri: typing.Optional[str] = OMIT,
        scope: typing.Optional[str] = OMIT,
        contacts: typing.Optional[typing.Sequence[str]] = OMIT,
        tos_uri: typing.Optional[str] = OMIT,
        policy_uri: typing.Optional[str] = OMIT,
        jwks_uri: typing.Optional[str] = OMIT,
        jwks: typing.Optional[JsonWebKeySet] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Follows RFC 7591.

        Parameters
        ----------
        redirect_uris : typing.Optional[typing.Sequence[str]]

        grant_types : typing.Optional[typing.Sequence[str]]

        response_types : typing.Optional[typing.Sequence[str]]

        client_id : typing.Optional[str]

        client_name : typing.Optional[str]

        client_uri : typing.Optional[str]

        logo_uri : typing.Optional[str]

        scope : typing.Optional[str]
            String containing a space-separated list of scope values
             that the client can use when requesting access tokens.

        contacts : typing.Optional[typing.Sequence[str]]
            Array of strings representing ways to contact people responsible for this client,
             typically email addresses.

        tos_uri : typing.Optional[str]

        policy_uri : typing.Optional[str]

        jwks_uri : typing.Optional[str]

        jwks : typing.Optional[JsonWebKeySet]
            Client's JSON Web Key Set [RFC7517] document value, which contains the client's public keys.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "client/register",
            method="POST",
            json={
                "redirect_uris": redirect_uris,
                "grant_types": grant_types,
                "response_types": response_types,
                "client_id": client_id,
                "client_name": client_name,
                "client_uri": client_uri,
                "logo_uri": logo_uri,
                "scope": scope,
                "contacts": contacts,
                "tos_uri": tos_uri,
                "policy_uri": policy_uri,
                "jwks_uri": jwks_uri,
                "jwks": convert_and_respect_annotation_metadata(
                    object_=jwks, annotation=JsonWebKeySet, direction="write"
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

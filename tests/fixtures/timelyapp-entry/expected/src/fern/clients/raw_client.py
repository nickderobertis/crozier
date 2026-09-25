

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
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_found_error import NotFoundError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.v1company import V1Company
from .types.get11account_id_clients_request_show import Get11AccountIdClientsRequestShow
from .types.v1companies_create_client import V1CompaniesCreateClient
from .types.v1companies_update_client import V1CompaniesUpdateClient
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawClientsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_all_clients_of_an_account(
        self,
        account_id: int,
        *,
        limit: typing.Optional[int] = None,
        order: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        show: typing.Optional[Get11AccountIdClientsRequestShow] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[V1Company]]:
        """
        NOTE: By default, client list will return first 10000 clients in alphabetical order. You can also use optional parameters like “limit”, “offset”, “show” and “order” to change the results.

        Parameters
        ----------
        account_id : int
            Account ID for the clients you want to retrieve

        limit : typing.Optional[int]
            Retrieve number of clients

        order : typing.Optional[str]
            "asc (default)" and "desc"

        offset : typing.Optional[int]
            Retrieve clients from offset

        show : typing.Optional[Get11AccountIdClientsRequestShow]
            Specifies which records to retrieve. Example: "show=all" or "show=active" or "show=archived"

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[V1Company]]
            Client details
        """
        _response = self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/clients",
            method="GET",
            params={
                "limit": limit,
                "order": order,
                "offset": offset,
                "show": show,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[V1Company],
                    parse_obj_as(
                        type_=typing.List[V1Company],
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

    def create_client(
        self,
        account_id: int,
        *,
        client: V1CompaniesCreateClient,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V1Company]:
        """
        This API lets you create a client for an account.

        Parameters
        ----------
        account_id : int
            Account ID for the client you want to create

        client : V1CompaniesCreateClient

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[V1Company]
            Client
        """
        _response = self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/clients",
            method="POST",
            json={
                "client": convert_and_respect_annotation_metadata(
                    object_=client, annotation=V1CompaniesCreateClient, direction="write"
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
                _data = typing.cast(
                    V1Company,
                    parse_obj_as(
                        type_=V1Company,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    def client_details(
        self,
        account_id: int,
        id: int,
        *,
        project_counts: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V1Company]:
        """
        Client details and project counts

        Parameters
        ----------
        account_id : int
            Account ID for the client you want to retrieve

        id : int
            Client ID to retrieve

        project_counts : typing.Optional[str]
            Specify to retrieve project counts. Example values: "true" or "false"

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[V1Company]
            Client details
        """
        _response = self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/clients/{encode_path_param(id)}",
            method="GET",
            params={
                "project_counts": project_counts,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V1Company,
                    parse_obj_as(
                        type_=V1Company,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
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

    def client_update(
        self,
        account_id: int,
        id: int,
        *,
        client: V1CompaniesUpdateClient,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V1Company]:
        """
        Update client details just by using a client ID.

        Parameters
        ----------
        account_id : int
            Account ID for the client you want to update

        id : int
            Client ID to update

        client : V1CompaniesUpdateClient

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[V1Company]
            Client details
        """
        _response = self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/clients/{encode_path_param(id)}",
            method="PUT",
            json={
                "client": convert_and_respect_annotation_metadata(
                    object_=client, annotation=V1CompaniesUpdateClient, direction="write"
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
                _data = typing.cast(
                    V1Company,
                    parse_obj_as(
                        type_=V1Company,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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


class AsyncRawClientsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_all_clients_of_an_account(
        self,
        account_id: int,
        *,
        limit: typing.Optional[int] = None,
        order: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        show: typing.Optional[Get11AccountIdClientsRequestShow] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[V1Company]]:
        """
        NOTE: By default, client list will return first 10000 clients in alphabetical order. You can also use optional parameters like “limit”, “offset”, “show” and “order” to change the results.

        Parameters
        ----------
        account_id : int
            Account ID for the clients you want to retrieve

        limit : typing.Optional[int]
            Retrieve number of clients

        order : typing.Optional[str]
            "asc (default)" and "desc"

        offset : typing.Optional[int]
            Retrieve clients from offset

        show : typing.Optional[Get11AccountIdClientsRequestShow]
            Specifies which records to retrieve. Example: "show=all" or "show=active" or "show=archived"

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[V1Company]]
            Client details
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/clients",
            method="GET",
            params={
                "limit": limit,
                "order": order,
                "offset": offset,
                "show": show,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[V1Company],
                    parse_obj_as(
                        type_=typing.List[V1Company],
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

    async def create_client(
        self,
        account_id: int,
        *,
        client: V1CompaniesCreateClient,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V1Company]:
        """
        This API lets you create a client for an account.

        Parameters
        ----------
        account_id : int
            Account ID for the client you want to create

        client : V1CompaniesCreateClient

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[V1Company]
            Client
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/clients",
            method="POST",
            json={
                "client": convert_and_respect_annotation_metadata(
                    object_=client, annotation=V1CompaniesCreateClient, direction="write"
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
                _data = typing.cast(
                    V1Company,
                    parse_obj_as(
                        type_=V1Company,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    async def client_details(
        self,
        account_id: int,
        id: int,
        *,
        project_counts: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V1Company]:
        """
        Client details and project counts

        Parameters
        ----------
        account_id : int
            Account ID for the client you want to retrieve

        id : int
            Client ID to retrieve

        project_counts : typing.Optional[str]
            Specify to retrieve project counts. Example values: "true" or "false"

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[V1Company]
            Client details
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/clients/{encode_path_param(id)}",
            method="GET",
            params={
                "project_counts": project_counts,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V1Company,
                    parse_obj_as(
                        type_=V1Company,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
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

    async def client_update(
        self,
        account_id: int,
        id: int,
        *,
        client: V1CompaniesUpdateClient,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V1Company]:
        """
        Update client details just by using a client ID.

        Parameters
        ----------
        account_id : int
            Account ID for the client you want to update

        id : int
            Client ID to update

        client : V1CompaniesUpdateClient

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[V1Company]
            Client details
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/clients/{encode_path_param(id)}",
            method="PUT",
            json={
                "client": convert_and_respect_annotation_metadata(
                    object_=client, annotation=V1CompaniesUpdateClient, direction="write"
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
                _data = typing.cast(
                    V1Company,
                    parse_obj_as(
                        type_=V1Company,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

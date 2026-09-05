

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.content import Content
from ..types.delete_address import DeleteAddress
from ..types.export_address import ExportAddress
from ..types.import_address import ImportAddress
from ..types.list_addresses import ListAddresses
from ..types.new_address import NewAddress
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawAddressRequestsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def delete_address(
        self,
        *,
        authorization: str,
        ethereumaddress: str,
        password: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DeleteAddress]:
        """
        Deletes an existing ethereum address. Be careful when using this function.

        Parameters
        ----------
        authorization : str
            API Key

        ethereumaddress : str

        password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteAddress]

        """
        _response = self._client_wrapper.httpx_client.request(
            "deleteAddress",
            method="POST",
            json={
                "ethereumaddress": ethereumaddress,
                "password": password,
            },
            headers={
                "content-type": "application/json",
                "Authorization": str(authorization) if authorization is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteAddress,
                    parse_obj_as(
                        type_=DeleteAddress,
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

    def export_address(
        self,
        *,
        authorization: str,
        ethaddress: str,
        password: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ExportAddress]:
        """
        Returns all ethereum addresses created with an account.

        Parameters
        ----------
        authorization : str
            API Key

        ethaddress : str

        password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ExportAddress]

        """
        _response = self._client_wrapper.httpx_client.request(
            "exportAddress",
            method="POST",
            json={
                "ethaddress": ethaddress,
                "password": password,
            },
            headers={
                "content-type": "application/json",
                "Authorization": str(authorization) if authorization is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ExportAddress,
                    parse_obj_as(
                        type_=ExportAddress,
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

    def import_address(
        self,
        *,
        authorization: str,
        content: Content,
        filename: str,
        password: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ImportAddress]:
        """
        Returns all ethereum addresses created with an account.

        Parameters
        ----------
        authorization : str
            API Key

        content : Content

        filename : str

        password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ImportAddress]

        """
        _response = self._client_wrapper.httpx_client.request(
            "importAddress",
            method="POST",
            json={
                "content": convert_and_respect_annotation_metadata(
                    object_=content, annotation=Content, direction="write"
                ),
                "filename": filename,
                "password": password,
            },
            headers={
                "content-type": "application/json",
                "Authorization": str(authorization) if authorization is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ImportAddress,
                    parse_obj_as(
                        type_=ImportAddress,
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

    def list_addresses(
        self, *, authorization: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ListAddresses]:
        """
        Returns all ethereum addresses created with an account.

        Parameters
        ----------
        authorization : str
            API Key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListAddresses]

        """
        _response = self._client_wrapper.httpx_client.request(
            "listAddresses",
            method="POST",
            headers={
                "Authorization": str(authorization) if authorization is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListAddresses,
                    parse_obj_as(
                        type_=ListAddresses,
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

    def new_address(
        self, *, authorization: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[NewAddress]:
        """
        Generates a new ethereum addresses you can use to send or receive funds. Do not lose the password! We can't restore access to an address if you lose it.

        Parameters
        ----------
        authorization : str
            API Key

        password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[NewAddress]

        """
        _response = self._client_wrapper.httpx_client.request(
            "newAddress",
            method="POST",
            json={
                "password": password,
            },
            headers={
                "content-type": "application/json",
                "Authorization": str(authorization) if authorization is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NewAddress,
                    parse_obj_as(
                        type_=NewAddress,
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


class AsyncRawAddressRequestsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def delete_address(
        self,
        *,
        authorization: str,
        ethereumaddress: str,
        password: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DeleteAddress]:
        """
        Deletes an existing ethereum address. Be careful when using this function.

        Parameters
        ----------
        authorization : str
            API Key

        ethereumaddress : str

        password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteAddress]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "deleteAddress",
            method="POST",
            json={
                "ethereumaddress": ethereumaddress,
                "password": password,
            },
            headers={
                "content-type": "application/json",
                "Authorization": str(authorization) if authorization is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteAddress,
                    parse_obj_as(
                        type_=DeleteAddress,
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

    async def export_address(
        self,
        *,
        authorization: str,
        ethaddress: str,
        password: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ExportAddress]:
        """
        Returns all ethereum addresses created with an account.

        Parameters
        ----------
        authorization : str
            API Key

        ethaddress : str

        password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ExportAddress]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "exportAddress",
            method="POST",
            json={
                "ethaddress": ethaddress,
                "password": password,
            },
            headers={
                "content-type": "application/json",
                "Authorization": str(authorization) if authorization is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ExportAddress,
                    parse_obj_as(
                        type_=ExportAddress,
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

    async def import_address(
        self,
        *,
        authorization: str,
        content: Content,
        filename: str,
        password: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ImportAddress]:
        """
        Returns all ethereum addresses created with an account.

        Parameters
        ----------
        authorization : str
            API Key

        content : Content

        filename : str

        password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ImportAddress]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "importAddress",
            method="POST",
            json={
                "content": convert_and_respect_annotation_metadata(
                    object_=content, annotation=Content, direction="write"
                ),
                "filename": filename,
                "password": password,
            },
            headers={
                "content-type": "application/json",
                "Authorization": str(authorization) if authorization is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ImportAddress,
                    parse_obj_as(
                        type_=ImportAddress,
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

    async def list_addresses(
        self, *, authorization: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ListAddresses]:
        """
        Returns all ethereum addresses created with an account.

        Parameters
        ----------
        authorization : str
            API Key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListAddresses]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "listAddresses",
            method="POST",
            headers={
                "Authorization": str(authorization) if authorization is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListAddresses,
                    parse_obj_as(
                        type_=ListAddresses,
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

    async def new_address(
        self, *, authorization: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[NewAddress]:
        """
        Generates a new ethereum addresses you can use to send or receive funds. Do not lose the password! We can't restore access to an address if you lose it.

        Parameters
        ----------
        authorization : str
            API Key

        password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[NewAddress]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "newAddress",
            method="POST",
            json={
                "password": password,
            },
            headers={
                "content-type": "application/json",
                "Authorization": str(authorization) if authorization is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NewAddress,
                    parse_obj_as(
                        type_=NewAddress,
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

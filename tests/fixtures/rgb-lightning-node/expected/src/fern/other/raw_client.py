

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.check_indexer_url_response import CheckIndexerUrlResponse
from ..types.empty_response import EmptyResponse
from ..types.init_response import InitResponse
from ..types.ldk_chain_sync import LdkChainSync
from ..types.network_info_response import NetworkInfoResponse
from ..types.node_info_response import NodeInfoResponse
from ..types.sign_message_response import SignMessageResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawOtherClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def backup_the_node(
        self, *, backup_path: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EmptyResponse]:
        """
        Create a backup of the node's data

        Parameters
        ----------
        backup_path : str

        password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EmptyResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "backup",
            method="POST",
            json={
                "backup_path": backup_path,
                "password": password,
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
                    EmptyResponse,
                    parse_obj_as(
                        type_=EmptyResponse,
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

    def change_the_password(
        self, *, old_password: str, new_password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EmptyResponse]:
        """
        Change the node's password

        Parameters
        ----------
        old_password : str

        new_password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EmptyResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "changepassword",
            method="POST",
            json={
                "old_password": old_password,
                "new_password": new_password,
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
                    EmptyResponse,
                    parse_obj_as(
                        type_=EmptyResponse,
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

    def check_an_indexer_url(
        self, *, indexer_url: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CheckIndexerUrlResponse]:
        """
        Check the given indexer URL is valid

        Parameters
        ----------
        indexer_url : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CheckIndexerUrlResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "checkindexerurl",
            method="POST",
            json={
                "indexer_url": indexer_url,
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
                    CheckIndexerUrlResponse,
                    parse_obj_as(
                        type_=CheckIndexerUrlResponse,
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

    def check_a_proxy_endpoint(
        self, *, proxy_endpoint: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EmptyResponse]:
        """
        Check the given proxy endpoint is valid

        Parameters
        ----------
        proxy_endpoint : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EmptyResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "checkproxyendpoint",
            method="POST",
            json={
                "proxy_endpoint": proxy_endpoint,
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
                    EmptyResponse,
                    parse_obj_as(
                        type_=EmptyResponse,
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

    def init_the_node(
        self,
        *,
        password: str,
        mnemonic: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[InitResponse]:
        """
        Initialize a new node, optionally providing a mnemonic. If no mnemonic is provided a new one is generated. Note that a mnemonic alone is not sufficient to recover RGB state, which also requires client-side data.

        Parameters
        ----------
        password : str

        mnemonic : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[InitResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "init",
            method="POST",
            json={
                "password": password,
                "mnemonic": mnemonic,
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
                    InitResponse,
                    parse_obj_as(
                        type_=InitResponse,
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

    def lock_the_node(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[EmptyResponse]:
        """
        Lock an unlocked node

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EmptyResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "lock",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EmptyResponse,
                    parse_obj_as(
                        type_=EmptyResponse,
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

    def get_network_info(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[NetworkInfoResponse]:
        """
        Get info on the Bitcoin network where the LN is running

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[NetworkInfoResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "networkinfo",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NetworkInfoResponse,
                    parse_obj_as(
                        type_=NetworkInfoResponse,
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

    def get_node_info(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[NodeInfoResponse]:
        """
        Get the LN node's info

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[NodeInfoResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "nodeinfo",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NodeInfoResponse,
                    parse_obj_as(
                        type_=NodeInfoResponse,
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

    def restore_the_node(
        self, *, backup_path: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EmptyResponse]:
        """
        Restore a node from a backup file

        Parameters
        ----------
        backup_path : str

        password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EmptyResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "restore",
            method="POST",
            json={
                "backup_path": backup_path,
                "password": password,
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
                    EmptyResponse,
                    parse_obj_as(
                        type_=EmptyResponse,
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

    def revoke_a_token(
        self, *, token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EmptyResponse]:
        """
        Revoke an authentication token

        Parameters
        ----------
        token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EmptyResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "revoketoken",
            method="POST",
            json={
                "token": token,
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
                    EmptyResponse,
                    parse_obj_as(
                        type_=EmptyResponse,
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

    def send_an_onion_message(
        self,
        *,
        node_ids: typing.Sequence[str],
        tlv_type: int,
        data: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EmptyResponse]:
        """
        Send an onion message via the LN

        Parameters
        ----------
        node_ids : typing.Sequence[str]

        tlv_type : int

        data : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EmptyResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "sendonionmessage",
            method="POST",
            json={
                "node_ids": node_ids,
                "tlv_type": tlv_type,
                "data": data,
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
                    EmptyResponse,
                    parse_obj_as(
                        type_=EmptyResponse,
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

    def shutdown_the_node(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EmptyResponse]:
        """
        Gracefully shutdown the node

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EmptyResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "shutdown",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EmptyResponse,
                    parse_obj_as(
                        type_=EmptyResponse,
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

    def sign_a_message(
        self, *, message: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SignMessageResponse]:
        """
        Sign the provided message

        Parameters
        ----------
        message : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SignMessageResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "signmessage",
            method="POST",
            json={
                "message": message,
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
                    SignMessageResponse,
                    parse_obj_as(
                        type_=SignMessageResponse,
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

    def unlock_the_node(
        self,
        *,
        password: str,
        ldk_chain_sync: LdkChainSync,
        indexer_url: str,
        announce_addresses: typing.Sequence[str],
        announce_alias: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EmptyResponse]:
        """
        Unlock a locked node

        Parameters
        ----------
        password : str

        ldk_chain_sync : LdkChainSync

        indexer_url : str

        announce_addresses : typing.Sequence[str]

        announce_alias : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EmptyResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "unlock",
            method="POST",
            json={
                "password": password,
                "ldk_chain_sync": convert_and_respect_annotation_metadata(
                    object_=ldk_chain_sync, annotation=LdkChainSync, direction="write"
                ),
                "indexer_url": indexer_url,
                "announce_addresses": announce_addresses,
                "announce_alias": announce_alias,
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
                    EmptyResponse,
                    parse_obj_as(
                        type_=EmptyResponse,
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


class AsyncRawOtherClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def backup_the_node(
        self, *, backup_path: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EmptyResponse]:
        """
        Create a backup of the node's data

        Parameters
        ----------
        backup_path : str

        password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EmptyResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "backup",
            method="POST",
            json={
                "backup_path": backup_path,
                "password": password,
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
                    EmptyResponse,
                    parse_obj_as(
                        type_=EmptyResponse,
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

    async def change_the_password(
        self, *, old_password: str, new_password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EmptyResponse]:
        """
        Change the node's password

        Parameters
        ----------
        old_password : str

        new_password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EmptyResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "changepassword",
            method="POST",
            json={
                "old_password": old_password,
                "new_password": new_password,
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
                    EmptyResponse,
                    parse_obj_as(
                        type_=EmptyResponse,
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

    async def check_an_indexer_url(
        self, *, indexer_url: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CheckIndexerUrlResponse]:
        """
        Check the given indexer URL is valid

        Parameters
        ----------
        indexer_url : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CheckIndexerUrlResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "checkindexerurl",
            method="POST",
            json={
                "indexer_url": indexer_url,
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
                    CheckIndexerUrlResponse,
                    parse_obj_as(
                        type_=CheckIndexerUrlResponse,
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

    async def check_a_proxy_endpoint(
        self, *, proxy_endpoint: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EmptyResponse]:
        """
        Check the given proxy endpoint is valid

        Parameters
        ----------
        proxy_endpoint : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EmptyResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "checkproxyendpoint",
            method="POST",
            json={
                "proxy_endpoint": proxy_endpoint,
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
                    EmptyResponse,
                    parse_obj_as(
                        type_=EmptyResponse,
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

    async def init_the_node(
        self,
        *,
        password: str,
        mnemonic: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[InitResponse]:
        """
        Initialize a new node, optionally providing a mnemonic. If no mnemonic is provided a new one is generated. Note that a mnemonic alone is not sufficient to recover RGB state, which also requires client-side data.

        Parameters
        ----------
        password : str

        mnemonic : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[InitResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "init",
            method="POST",
            json={
                "password": password,
                "mnemonic": mnemonic,
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
                    InitResponse,
                    parse_obj_as(
                        type_=InitResponse,
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

    async def lock_the_node(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EmptyResponse]:
        """
        Lock an unlocked node

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EmptyResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "lock",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EmptyResponse,
                    parse_obj_as(
                        type_=EmptyResponse,
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

    async def get_network_info(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[NetworkInfoResponse]:
        """
        Get info on the Bitcoin network where the LN is running

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[NetworkInfoResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "networkinfo",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NetworkInfoResponse,
                    parse_obj_as(
                        type_=NetworkInfoResponse,
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

    async def get_node_info(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[NodeInfoResponse]:
        """
        Get the LN node's info

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[NodeInfoResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "nodeinfo",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NodeInfoResponse,
                    parse_obj_as(
                        type_=NodeInfoResponse,
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

    async def restore_the_node(
        self, *, backup_path: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EmptyResponse]:
        """
        Restore a node from a backup file

        Parameters
        ----------
        backup_path : str

        password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EmptyResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "restore",
            method="POST",
            json={
                "backup_path": backup_path,
                "password": password,
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
                    EmptyResponse,
                    parse_obj_as(
                        type_=EmptyResponse,
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

    async def revoke_a_token(
        self, *, token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EmptyResponse]:
        """
        Revoke an authentication token

        Parameters
        ----------
        token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EmptyResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "revoketoken",
            method="POST",
            json={
                "token": token,
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
                    EmptyResponse,
                    parse_obj_as(
                        type_=EmptyResponse,
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

    async def send_an_onion_message(
        self,
        *,
        node_ids: typing.Sequence[str],
        tlv_type: int,
        data: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EmptyResponse]:
        """
        Send an onion message via the LN

        Parameters
        ----------
        node_ids : typing.Sequence[str]

        tlv_type : int

        data : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EmptyResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "sendonionmessage",
            method="POST",
            json={
                "node_ids": node_ids,
                "tlv_type": tlv_type,
                "data": data,
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
                    EmptyResponse,
                    parse_obj_as(
                        type_=EmptyResponse,
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

    async def shutdown_the_node(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EmptyResponse]:
        """
        Gracefully shutdown the node

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EmptyResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "shutdown",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EmptyResponse,
                    parse_obj_as(
                        type_=EmptyResponse,
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

    async def sign_a_message(
        self, *, message: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SignMessageResponse]:
        """
        Sign the provided message

        Parameters
        ----------
        message : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SignMessageResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "signmessage",
            method="POST",
            json={
                "message": message,
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
                    SignMessageResponse,
                    parse_obj_as(
                        type_=SignMessageResponse,
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

    async def unlock_the_node(
        self,
        *,
        password: str,
        ldk_chain_sync: LdkChainSync,
        indexer_url: str,
        announce_addresses: typing.Sequence[str],
        announce_alias: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EmptyResponse]:
        """
        Unlock a locked node

        Parameters
        ----------
        password : str

        ldk_chain_sync : LdkChainSync

        indexer_url : str

        announce_addresses : typing.Sequence[str]

        announce_alias : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EmptyResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "unlock",
            method="POST",
            json={
                "password": password,
                "ldk_chain_sync": convert_and_respect_annotation_metadata(
                    object_=ldk_chain_sync, annotation=LdkChainSync, direction="write"
                ),
                "indexer_url": indexer_url,
                "announce_addresses": announce_addresses,
                "announce_alias": announce_alias,
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
                    EmptyResponse,
                    parse_obj_as(
                        type_=EmptyResponse,
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

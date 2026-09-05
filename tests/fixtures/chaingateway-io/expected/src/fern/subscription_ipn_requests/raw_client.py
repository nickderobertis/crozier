

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.list_failed_ip_ns import ListFailedIpNs
from ..types.list_subscribed_addresses import ListSubscribedAddresses
from ..types.resend_failed_ipn import ResendFailedIpn
from ..types.subscribe_address import SubscribeAddress
from ..types.unsubscribe_address import UnsubscribeAddress
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawSubscriptionIpnRequestsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_failed_ip_ns(
        self, *, authorization: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ListFailedIpNs]:
        """
        Returns all subscriptions/IPNs created with an account.

        Parameters
        ----------
        authorization : str
            API Key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListFailedIpNs]

        """
        _response = self._client_wrapper.httpx_client.request(
            "listFailedIPNs",
            method="POST",
            headers={
                "Authorization": str(authorization) if authorization is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListFailedIpNs,
                    parse_obj_as(
                        type_=ListFailedIpNs,
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

    def list_subscribed_addresses(
        self, *, authorization: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ListSubscribedAddresses]:
        """
        Returns all subscriptions/IPNs created with an account.

        Parameters
        ----------
        authorization : str
            API Key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListSubscribedAddresses]

        """
        _response = self._client_wrapper.httpx_client.request(
            "listSubscribedAddresses",
            method="POST",
            headers={
                "Authorization": str(authorization) if authorization is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListSubscribedAddresses,
                    parse_obj_as(
                        type_=ListSubscribedAddresses,
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

    def resend_failed_ipn(
        self, *, authorization: str, id: int, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ResendFailedIpn]:
        """
        Returns all subscriptions/IPNs created with an account.

        Parameters
        ----------
        authorization : str
            API Key

        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ResendFailedIpn]

        """
        _response = self._client_wrapper.httpx_client.request(
            "resendFailedIPN",
            method="POST",
            json={
                "id": id,
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
                    ResendFailedIpn,
                    parse_obj_as(
                        type_=ResendFailedIpn,
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

    def subscribe_address(
        self,
        *,
        authorization: str,
        contractaddress: str,
        ethereumaddress: str,
        url: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SubscribeAddress]:
        """
        Creates a new subscription/IPN for the given address (and contractaddress). You will receive a notification to the given url every time a deposit is received. Unsubscribe the address before sending tokens/ETH from it or you won't get reliable notifications anymore.

        Parameters
        ----------
        authorization : str
            API Key

        contractaddress : str

        ethereumaddress : str

        url : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SubscribeAddress]

        """
        _response = self._client_wrapper.httpx_client.request(
            "subscribeAddress",
            method="POST",
            json={
                "contractaddress": contractaddress,
                "ethereumaddress": ethereumaddress,
                "url": url,
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
                    SubscribeAddress,
                    parse_obj_as(
                        type_=SubscribeAddress,
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

    def unsubscribe_address(
        self,
        *,
        authorization: str,
        contractaddress: str,
        ethereumaddress: str,
        url: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UnsubscribeAddress]:
        """
        Deletes an existing subscription/IPN for the given address (and contractaddress).

        Parameters
        ----------
        authorization : str
            API Key

        contractaddress : str

        ethereumaddress : str

        url : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UnsubscribeAddress]

        """
        _response = self._client_wrapper.httpx_client.request(
            "unsubscribeAddress",
            method="POST",
            json={
                "contractaddress": contractaddress,
                "ethereumaddress": ethereumaddress,
                "url": url,
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
                    UnsubscribeAddress,
                    parse_obj_as(
                        type_=UnsubscribeAddress,
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


class AsyncRawSubscriptionIpnRequestsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_failed_ip_ns(
        self, *, authorization: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ListFailedIpNs]:
        """
        Returns all subscriptions/IPNs created with an account.

        Parameters
        ----------
        authorization : str
            API Key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListFailedIpNs]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "listFailedIPNs",
            method="POST",
            headers={
                "Authorization": str(authorization) if authorization is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListFailedIpNs,
                    parse_obj_as(
                        type_=ListFailedIpNs,
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

    async def list_subscribed_addresses(
        self, *, authorization: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ListSubscribedAddresses]:
        """
        Returns all subscriptions/IPNs created with an account.

        Parameters
        ----------
        authorization : str
            API Key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListSubscribedAddresses]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "listSubscribedAddresses",
            method="POST",
            headers={
                "Authorization": str(authorization) if authorization is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListSubscribedAddresses,
                    parse_obj_as(
                        type_=ListSubscribedAddresses,
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

    async def resend_failed_ipn(
        self, *, authorization: str, id: int, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ResendFailedIpn]:
        """
        Returns all subscriptions/IPNs created with an account.

        Parameters
        ----------
        authorization : str
            API Key

        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ResendFailedIpn]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "resendFailedIPN",
            method="POST",
            json={
                "id": id,
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
                    ResendFailedIpn,
                    parse_obj_as(
                        type_=ResendFailedIpn,
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

    async def subscribe_address(
        self,
        *,
        authorization: str,
        contractaddress: str,
        ethereumaddress: str,
        url: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SubscribeAddress]:
        """
        Creates a new subscription/IPN for the given address (and contractaddress). You will receive a notification to the given url every time a deposit is received. Unsubscribe the address before sending tokens/ETH from it or you won't get reliable notifications anymore.

        Parameters
        ----------
        authorization : str
            API Key

        contractaddress : str

        ethereumaddress : str

        url : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SubscribeAddress]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "subscribeAddress",
            method="POST",
            json={
                "contractaddress": contractaddress,
                "ethereumaddress": ethereumaddress,
                "url": url,
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
                    SubscribeAddress,
                    parse_obj_as(
                        type_=SubscribeAddress,
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

    async def unsubscribe_address(
        self,
        *,
        authorization: str,
        contractaddress: str,
        ethereumaddress: str,
        url: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UnsubscribeAddress]:
        """
        Deletes an existing subscription/IPN for the given address (and contractaddress).

        Parameters
        ----------
        authorization : str
            API Key

        contractaddress : str

        ethereumaddress : str

        url : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UnsubscribeAddress]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "unsubscribeAddress",
            method="POST",
            json={
                "contractaddress": contractaddress,
                "ethereumaddress": ethereumaddress,
                "url": url,
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
                    UnsubscribeAddress,
                    parse_obj_as(
                        type_=UnsubscribeAddress,
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



import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.internal_server_error import InternalServerError
from ..types.subscription_list import SubscriptionList
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawSubscriptionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_subscriptions(
        self,
        *,
        subscription_key: typing.Optional[str] = None,
        subscription_type: typing.Optional[str] = None,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SubscriptionList]:
        """
        Parameters
        ----------
        subscription_key : typing.Optional[str]
            filter only subscriptions matching key

        subscription_type : typing.Optional[str]
            filter only subscriptions matching type

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SubscriptionList]
            Subscription listing
        """
        _response = self._client_wrapper.httpx_client.request(
            "subscriptions",
            method="GET",
            params={
                "subscription_key": subscription_key,
                "subscription_type": subscription_type,
            },
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SubscriptionList,
                    parse_obj_as(
                        type_=SubscriptionList,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
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

    def add_subscription(
        self,
        *,
        anchore_account: typing.Optional[str] = None,
        subscription_key: typing.Optional[str] = OMIT,
        subscription_type: typing.Optional[str] = OMIT,
        subscription_value: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SubscriptionList]:
        """
        Create a new subscription to watch a tag and get notifications of changes

        Parameters
        ----------
        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        subscription_key : typing.Optional[str]

        subscription_type : typing.Optional[str]

        subscription_value : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SubscriptionList]
            Subscription add success
        """
        _response = self._client_wrapper.httpx_client.request(
            "subscriptions",
            method="POST",
            json={
                "subscription_key": subscription_key,
                "subscription_type": subscription_type,
                "subscription_value": subscription_value,
            },
            headers={
                "content-type": "application/json",
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SubscriptionList,
                    parse_obj_as(
                        type_=SubscriptionList,
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

    def get_subscription(
        self,
        subscription_id: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SubscriptionList]:
        """
        Parameters
        ----------
        subscription_id : str

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SubscriptionList]
            Filtered subscription list by type
        """
        _response = self._client_wrapper.httpx_client.request(
            f"subscriptions/{encode_path_param(subscription_id)}",
            method="GET",
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SubscriptionList,
                    parse_obj_as(
                        type_=SubscriptionList,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
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

    def update_subscription(
        self,
        subscription_id: str,
        *,
        anchore_account: typing.Optional[str] = None,
        active: typing.Optional[bool] = OMIT,
        subscription_value: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SubscriptionList]:
        """
        Parameters
        ----------
        subscription_id : str

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        active : typing.Optional[bool]
            Toggle the subscription processing on or off

        subscription_value : typing.Optional[str]
            The new subscription value, e.g. the new tag to be subscribed to

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SubscriptionList]
            Subscription add success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"subscriptions/{encode_path_param(subscription_id)}",
            method="PUT",
            json={
                "active": active,
                "subscription_value": subscription_value,
            },
            headers={
                "content-type": "application/json",
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SubscriptionList,
                    parse_obj_as(
                        type_=SubscriptionList,
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

    def delete_subscription(
        self,
        subscription_id: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"subscriptions/{encode_path_param(subscription_id)}",
            method="DELETE",
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 500:
                raise InternalServerError(
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


class AsyncRawSubscriptionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_subscriptions(
        self,
        *,
        subscription_key: typing.Optional[str] = None,
        subscription_type: typing.Optional[str] = None,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SubscriptionList]:
        """
        Parameters
        ----------
        subscription_key : typing.Optional[str]
            filter only subscriptions matching key

        subscription_type : typing.Optional[str]
            filter only subscriptions matching type

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SubscriptionList]
            Subscription listing
        """
        _response = await self._client_wrapper.httpx_client.request(
            "subscriptions",
            method="GET",
            params={
                "subscription_key": subscription_key,
                "subscription_type": subscription_type,
            },
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SubscriptionList,
                    parse_obj_as(
                        type_=SubscriptionList,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def add_subscription(
        self,
        *,
        anchore_account: typing.Optional[str] = None,
        subscription_key: typing.Optional[str] = OMIT,
        subscription_type: typing.Optional[str] = OMIT,
        subscription_value: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SubscriptionList]:
        """
        Create a new subscription to watch a tag and get notifications of changes

        Parameters
        ----------
        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        subscription_key : typing.Optional[str]

        subscription_type : typing.Optional[str]

        subscription_value : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SubscriptionList]
            Subscription add success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "subscriptions",
            method="POST",
            json={
                "subscription_key": subscription_key,
                "subscription_type": subscription_type,
                "subscription_value": subscription_value,
            },
            headers={
                "content-type": "application/json",
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SubscriptionList,
                    parse_obj_as(
                        type_=SubscriptionList,
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

    async def get_subscription(
        self,
        subscription_id: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SubscriptionList]:
        """
        Parameters
        ----------
        subscription_id : str

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SubscriptionList]
            Filtered subscription list by type
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"subscriptions/{encode_path_param(subscription_id)}",
            method="GET",
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SubscriptionList,
                    parse_obj_as(
                        type_=SubscriptionList,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def update_subscription(
        self,
        subscription_id: str,
        *,
        anchore_account: typing.Optional[str] = None,
        active: typing.Optional[bool] = OMIT,
        subscription_value: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SubscriptionList]:
        """
        Parameters
        ----------
        subscription_id : str

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        active : typing.Optional[bool]
            Toggle the subscription processing on or off

        subscription_value : typing.Optional[str]
            The new subscription value, e.g. the new tag to be subscribed to

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SubscriptionList]
            Subscription add success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"subscriptions/{encode_path_param(subscription_id)}",
            method="PUT",
            json={
                "active": active,
                "subscription_value": subscription_value,
            },
            headers={
                "content-type": "application/json",
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SubscriptionList,
                    parse_obj_as(
                        type_=SubscriptionList,
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

    async def delete_subscription(
        self,
        subscription_id: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"subscriptions/{encode_path_param(subscription_id)}",
            method="DELETE",
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 500:
                raise InternalServerError(
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

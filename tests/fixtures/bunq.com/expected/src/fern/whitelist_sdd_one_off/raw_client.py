

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..types.amount import Amount
from ..types.whitelist_sdd_one_off_create import WhitelistSddOneOffCreate
from ..types.whitelist_sdd_one_off_delete import WhitelistSddOneOffDelete
from ..types.whitelist_sdd_one_off_listing import WhitelistSddOneOffListing
from ..types.whitelist_sdd_one_off_read import WhitelistSddOneOffRead
from ..types.whitelist_sdd_one_off_update import WhitelistSddOneOffUpdate


OMIT = typing.cast(typing.Any, ...)


class RawWhitelistSddOneOffClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_all_whitelist_sdd_one_off_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[WhitelistSddOneOffListing]]:
        """
        Get a listing of all one off SDD whitelist entries for a target monetary account.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[WhitelistSddOneOffListing]]
            Whitelist an one off SDD so that when another one off SDD from the creditor comes in, it is automatically accepted.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/whitelist-sdd-one-off",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[WhitelistSddOneOffListing],
                    parse_obj_as(
                        type_=typing.List[WhitelistSddOneOffListing],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_whitelist_sdd_one_off_for_user(
        self,
        user_id: int,
        *,
        monetary_account_paying_id: int,
        request_id: int,
        maximum_amount_per_month: typing.Optional[Amount] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WhitelistSddOneOffCreate]:
        """
        Create a new one off SDD whitelist entry.

        Parameters
        ----------
        user_id : int


        monetary_account_paying_id : int
            ID of the monetary account of which you want to pay from.

        request_id : int
            ID of the request for which you want to whitelist the originating SDD.

        maximum_amount_per_month : typing.Optional[Amount]
            The maximum amount of money that is allowed to be deducted based on the whitelist.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WhitelistSddOneOffCreate]
            Whitelist an one off SDD so that when another one off SDD from the creditor comes in, it is automatically accepted.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/whitelist-sdd-one-off",
            method="POST",
            json={
                "maximum_amount_per_month": convert_and_respect_annotation_metadata(
                    object_=maximum_amount_per_month, annotation=Amount, direction="write"
                ),
                "monetary_account_paying_id": monetary_account_paying_id,
                "request_id": request_id,
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
                    WhitelistSddOneOffCreate,
                    parse_obj_as(
                        type_=WhitelistSddOneOffCreate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def read_whitelist_sdd_one_off_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[WhitelistSddOneOffRead]:
        """
        Get a specific one off SDD whitelist entry.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WhitelistSddOneOffRead]
            Whitelist an one off SDD so that when another one off SDD from the creditor comes in, it is automatically accepted.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/whitelist-sdd-one-off/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WhitelistSddOneOffRead,
                    parse_obj_as(
                        type_=WhitelistSddOneOffRead,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_whitelist_sdd_one_off_for_user(
        self,
        user_id: int,
        item_id: int,
        *,
        monetary_account_paying_id: int,
        request_id: int,
        maximum_amount_per_month: typing.Optional[Amount] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WhitelistSddOneOffUpdate]:
        """
        Whitelist an one off SDD so that when another one off SDD from the creditor comes in, it is automatically accepted.

        Parameters
        ----------
        user_id : int


        item_id : int


        monetary_account_paying_id : int
            ID of the monetary account of which you want to pay from.

        request_id : int
            ID of the request for which you want to whitelist the originating SDD.

        maximum_amount_per_month : typing.Optional[Amount]
            The maximum amount of money that is allowed to be deducted based on the whitelist.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WhitelistSddOneOffUpdate]
            Whitelist an one off SDD so that when another one off SDD from the creditor comes in, it is automatically accepted.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/whitelist-sdd-one-off/{jsonable_encoder(item_id)}",
            method="PUT",
            json={
                "maximum_amount_per_month": convert_and_respect_annotation_metadata(
                    object_=maximum_amount_per_month, annotation=Amount, direction="write"
                ),
                "monetary_account_paying_id": monetary_account_paying_id,
                "request_id": request_id,
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
                    WhitelistSddOneOffUpdate,
                    parse_obj_as(
                        type_=WhitelistSddOneOffUpdate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_whitelist_sdd_one_off_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[WhitelistSddOneOffDelete]:
        """
        Whitelist an one off SDD so that when another one off SDD from the creditor comes in, it is automatically accepted.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WhitelistSddOneOffDelete]
            Whitelist an one off SDD so that when another one off SDD from the creditor comes in, it is automatically accepted.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/whitelist-sdd-one-off/{jsonable_encoder(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WhitelistSddOneOffDelete,
                    parse_obj_as(
                        type_=WhitelistSddOneOffDelete,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawWhitelistSddOneOffClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_all_whitelist_sdd_one_off_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[WhitelistSddOneOffListing]]:
        """
        Get a listing of all one off SDD whitelist entries for a target monetary account.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[WhitelistSddOneOffListing]]
            Whitelist an one off SDD so that when another one off SDD from the creditor comes in, it is automatically accepted.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/whitelist-sdd-one-off",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[WhitelistSddOneOffListing],
                    parse_obj_as(
                        type_=typing.List[WhitelistSddOneOffListing],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_whitelist_sdd_one_off_for_user(
        self,
        user_id: int,
        *,
        monetary_account_paying_id: int,
        request_id: int,
        maximum_amount_per_month: typing.Optional[Amount] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WhitelistSddOneOffCreate]:
        """
        Create a new one off SDD whitelist entry.

        Parameters
        ----------
        user_id : int


        monetary_account_paying_id : int
            ID of the monetary account of which you want to pay from.

        request_id : int
            ID of the request for which you want to whitelist the originating SDD.

        maximum_amount_per_month : typing.Optional[Amount]
            The maximum amount of money that is allowed to be deducted based on the whitelist.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WhitelistSddOneOffCreate]
            Whitelist an one off SDD so that when another one off SDD from the creditor comes in, it is automatically accepted.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/whitelist-sdd-one-off",
            method="POST",
            json={
                "maximum_amount_per_month": convert_and_respect_annotation_metadata(
                    object_=maximum_amount_per_month, annotation=Amount, direction="write"
                ),
                "monetary_account_paying_id": monetary_account_paying_id,
                "request_id": request_id,
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
                    WhitelistSddOneOffCreate,
                    parse_obj_as(
                        type_=WhitelistSddOneOffCreate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def read_whitelist_sdd_one_off_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[WhitelistSddOneOffRead]:
        """
        Get a specific one off SDD whitelist entry.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WhitelistSddOneOffRead]
            Whitelist an one off SDD so that when another one off SDD from the creditor comes in, it is automatically accepted.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/whitelist-sdd-one-off/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WhitelistSddOneOffRead,
                    parse_obj_as(
                        type_=WhitelistSddOneOffRead,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_whitelist_sdd_one_off_for_user(
        self,
        user_id: int,
        item_id: int,
        *,
        monetary_account_paying_id: int,
        request_id: int,
        maximum_amount_per_month: typing.Optional[Amount] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WhitelistSddOneOffUpdate]:
        """
        Whitelist an one off SDD so that when another one off SDD from the creditor comes in, it is automatically accepted.

        Parameters
        ----------
        user_id : int


        item_id : int


        monetary_account_paying_id : int
            ID of the monetary account of which you want to pay from.

        request_id : int
            ID of the request for which you want to whitelist the originating SDD.

        maximum_amount_per_month : typing.Optional[Amount]
            The maximum amount of money that is allowed to be deducted based on the whitelist.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WhitelistSddOneOffUpdate]
            Whitelist an one off SDD so that when another one off SDD from the creditor comes in, it is automatically accepted.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/whitelist-sdd-one-off/{jsonable_encoder(item_id)}",
            method="PUT",
            json={
                "maximum_amount_per_month": convert_and_respect_annotation_metadata(
                    object_=maximum_amount_per_month, annotation=Amount, direction="write"
                ),
                "monetary_account_paying_id": monetary_account_paying_id,
                "request_id": request_id,
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
                    WhitelistSddOneOffUpdate,
                    parse_obj_as(
                        type_=WhitelistSddOneOffUpdate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_whitelist_sdd_one_off_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[WhitelistSddOneOffDelete]:
        """
        Whitelist an one off SDD so that when another one off SDD from the creditor comes in, it is automatically accepted.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WhitelistSddOneOffDelete]
            Whitelist an one off SDD so that when another one off SDD from the creditor comes in, it is automatically accepted.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/whitelist-sdd-one-off/{jsonable_encoder(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WhitelistSddOneOffDelete,
                    parse_obj_as(
                        type_=WhitelistSddOneOffDelete,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

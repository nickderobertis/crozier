

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
from ..types.amount import Amount
from ..types.whitelist_sdd_recurring_create import WhitelistSddRecurringCreate
from ..types.whitelist_sdd_recurring_delete import WhitelistSddRecurringDelete
from ..types.whitelist_sdd_recurring_listing import WhitelistSddRecurringListing
from ..types.whitelist_sdd_recurring_read import WhitelistSddRecurringRead
from ..types.whitelist_sdd_recurring_update import WhitelistSddRecurringUpdate
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawWhitelistSddRecurringClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_all_whitelist_sdd_recurring_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[WhitelistSddRecurringListing]]:
        """
        Get a listing of all recurring SDD whitelist entries for a target monetary account.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[WhitelistSddRecurringListing]]
            Whitelist a recurring SDD so that when another recurrence comes in, it is automatically accepted.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/whitelist-sdd-recurring",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[WhitelistSddRecurringListing],
                    parse_obj_as(
                        type_=typing.List[WhitelistSddRecurringListing],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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

    def create_whitelist_sdd_recurring_for_user(
        self,
        user_id: int,
        *,
        monetary_account_paying_id: int,
        request_id: int,
        maximum_amount_per_month: typing.Optional[Amount] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WhitelistSddRecurringCreate]:
        """
        Create a new recurring SDD whitelist entry.

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
        HttpResponse[WhitelistSddRecurringCreate]
            Whitelist a recurring SDD so that when another recurrence comes in, it is automatically accepted.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/whitelist-sdd-recurring",
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
                    WhitelistSddRecurringCreate,
                    parse_obj_as(
                        type_=WhitelistSddRecurringCreate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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

    def read_whitelist_sdd_recurring_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[WhitelistSddRecurringRead]:
        """
        Get a specific recurring SDD whitelist entry.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WhitelistSddRecurringRead]
            Whitelist a recurring SDD so that when another recurrence comes in, it is automatically accepted.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/whitelist-sdd-recurring/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WhitelistSddRecurringRead,
                    parse_obj_as(
                        type_=WhitelistSddRecurringRead,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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

    def update_whitelist_sdd_recurring_for_user(
        self,
        user_id: int,
        item_id: int,
        *,
        monetary_account_paying_id: int,
        request_id: int,
        maximum_amount_per_month: typing.Optional[Amount] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WhitelistSddRecurringUpdate]:
        """
        Whitelist a recurring SDD so that when another recurrence comes in, it is automatically accepted.

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
        HttpResponse[WhitelistSddRecurringUpdate]
            Whitelist a recurring SDD so that when another recurrence comes in, it is automatically accepted.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/whitelist-sdd-recurring/{encode_path_param(item_id)}",
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
                    WhitelistSddRecurringUpdate,
                    parse_obj_as(
                        type_=WhitelistSddRecurringUpdate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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

    def delete_whitelist_sdd_recurring_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[WhitelistSddRecurringDelete]:
        """
        Whitelist a recurring SDD so that when another recurrence comes in, it is automatically accepted.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WhitelistSddRecurringDelete]
            Whitelist a recurring SDD so that when another recurrence comes in, it is automatically accepted.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/whitelist-sdd-recurring/{encode_path_param(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WhitelistSddRecurringDelete,
                    parse_obj_as(
                        type_=WhitelistSddRecurringDelete,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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


class AsyncRawWhitelistSddRecurringClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_all_whitelist_sdd_recurring_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[WhitelistSddRecurringListing]]:
        """
        Get a listing of all recurring SDD whitelist entries for a target monetary account.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[WhitelistSddRecurringListing]]
            Whitelist a recurring SDD so that when another recurrence comes in, it is automatically accepted.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/whitelist-sdd-recurring",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[WhitelistSddRecurringListing],
                    parse_obj_as(
                        type_=typing.List[WhitelistSddRecurringListing],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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

    async def create_whitelist_sdd_recurring_for_user(
        self,
        user_id: int,
        *,
        monetary_account_paying_id: int,
        request_id: int,
        maximum_amount_per_month: typing.Optional[Amount] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WhitelistSddRecurringCreate]:
        """
        Create a new recurring SDD whitelist entry.

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
        AsyncHttpResponse[WhitelistSddRecurringCreate]
            Whitelist a recurring SDD so that when another recurrence comes in, it is automatically accepted.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/whitelist-sdd-recurring",
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
                    WhitelistSddRecurringCreate,
                    parse_obj_as(
                        type_=WhitelistSddRecurringCreate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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

    async def read_whitelist_sdd_recurring_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[WhitelistSddRecurringRead]:
        """
        Get a specific recurring SDD whitelist entry.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WhitelistSddRecurringRead]
            Whitelist a recurring SDD so that when another recurrence comes in, it is automatically accepted.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/whitelist-sdd-recurring/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WhitelistSddRecurringRead,
                    parse_obj_as(
                        type_=WhitelistSddRecurringRead,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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

    async def update_whitelist_sdd_recurring_for_user(
        self,
        user_id: int,
        item_id: int,
        *,
        monetary_account_paying_id: int,
        request_id: int,
        maximum_amount_per_month: typing.Optional[Amount] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WhitelistSddRecurringUpdate]:
        """
        Whitelist a recurring SDD so that when another recurrence comes in, it is automatically accepted.

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
        AsyncHttpResponse[WhitelistSddRecurringUpdate]
            Whitelist a recurring SDD so that when another recurrence comes in, it is automatically accepted.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/whitelist-sdd-recurring/{encode_path_param(item_id)}",
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
                    WhitelistSddRecurringUpdate,
                    parse_obj_as(
                        type_=WhitelistSddRecurringUpdate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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

    async def delete_whitelist_sdd_recurring_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[WhitelistSddRecurringDelete]:
        """
        Whitelist a recurring SDD so that when another recurrence comes in, it is automatically accepted.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WhitelistSddRecurringDelete]
            Whitelist a recurring SDD so that when another recurrence comes in, it is automatically accepted.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/whitelist-sdd-recurring/{encode_path_param(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WhitelistSddRecurringDelete,
                    parse_obj_as(
                        type_=WhitelistSddRecurringDelete,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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

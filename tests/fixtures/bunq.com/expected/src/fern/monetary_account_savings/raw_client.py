

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
from ..types.co_owner import CoOwner
from ..types.monetary_account_savings_create import MonetaryAccountSavingsCreate
from ..types.monetary_account_savings_listing import MonetaryAccountSavingsListing
from ..types.monetary_account_savings_read import MonetaryAccountSavingsRead
from ..types.monetary_account_savings_update import MonetaryAccountSavingsUpdate
from ..types.monetary_account_setting import MonetaryAccountSetting


OMIT = typing.cast(typing.Any, ...)


class RawMonetaryAccountSavingsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_all_monetary_account_savings_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[MonetaryAccountSavingsListing]]:
        """
        Gets a listing of all MonetaryAccountSavingss of a given user.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[MonetaryAccountSavingsListing]]
            With MonetaryAccountSavings you can create a new savings account.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account-savings",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[MonetaryAccountSavingsListing],
                    parse_obj_as(
                        type_=typing.List[MonetaryAccountSavingsListing],
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

    def create_monetary_account_savings_for_user(
        self,
        user_id: int,
        *,
        currency: str,
        all_co_owner: typing.Optional[typing.Sequence[CoOwner]] = OMIT,
        avatar_uuid: typing.Optional[str] = OMIT,
        daily_limit: typing.Optional[Amount] = OMIT,
        description: typing.Optional[str] = OMIT,
        reason: typing.Optional[str] = OMIT,
        reason_description: typing.Optional[str] = OMIT,
        savings_goal: typing.Optional[Amount] = OMIT,
        setting: typing.Optional[MonetaryAccountSetting] = OMIT,
        status: typing.Optional[str] = OMIT,
        sub_status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[MonetaryAccountSavingsCreate]:
        """
        Create new MonetaryAccountSavings.

        Parameters
        ----------
        user_id : int


        currency : str
            The currency of the MonetaryAccountSavings as an ISO 4217 formatted currency code.

        all_co_owner : typing.Optional[typing.Sequence[CoOwner]]
            The users the account will be joint with.

        avatar_uuid : typing.Optional[str]
            The UUID of the Avatar of the MonetaryAccountSavings.

        daily_limit : typing.Optional[Amount]
            The daily spending limit Amount of the MonetaryAccountSavings. Defaults to 1000 EUR. Currency must match the MonetaryAccountSavings's currency. Limited to 10000 EUR.

        description : typing.Optional[str]
            The description of the MonetaryAccountSavings. Defaults to 'bunq account'.

        reason : typing.Optional[str]
            The reason for voluntarily cancelling (closing) the MonetaryAccountSavings, can only be OTHER. Should only be specified if updating the status to CANCELLED.

        reason_description : typing.Optional[str]
            The optional free-form reason for voluntarily cancelling (closing) the MonetaryAccountSavings. Can be any user provided message. Should only be specified if updating the status to CANCELLED.

        savings_goal : typing.Optional[Amount]
            The Savings Goal set for this MonetaryAccountSavings.

        setting : typing.Optional[MonetaryAccountSetting]
            The settings of the MonetaryAccountSavings.

        status : typing.Optional[str]
            The status of the MonetaryAccountSavings. Ignored in POST requests (always set to ACTIVE) can be CANCELLED or PENDING_REOPEN in PUT requests to cancel (close) or reopen the MonetaryAccountSavings. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).

        sub_status : typing.Optional[str]
            The sub-status of the MonetaryAccountSavings providing extra information regarding the status. Should be ignored for POST requests. In case of PUT requests with status CANCELLED it can only be REDEMPTION_VOLUNTARY, while with status PENDING_REOPEN it can only be NONE. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MonetaryAccountSavingsCreate]
            With MonetaryAccountSavings you can create a new savings account.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account-savings",
            method="POST",
            json={
                "all_co_owner": convert_and_respect_annotation_metadata(
                    object_=all_co_owner, annotation=typing.Sequence[CoOwner], direction="write"
                ),
                "avatar_uuid": avatar_uuid,
                "currency": currency,
                "daily_limit": convert_and_respect_annotation_metadata(
                    object_=daily_limit, annotation=Amount, direction="write"
                ),
                "description": description,
                "reason": reason,
                "reason_description": reason_description,
                "savings_goal": convert_and_respect_annotation_metadata(
                    object_=savings_goal, annotation=Amount, direction="write"
                ),
                "setting": convert_and_respect_annotation_metadata(
                    object_=setting, annotation=MonetaryAccountSetting, direction="write"
                ),
                "status": status,
                "sub_status": sub_status,
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
                    MonetaryAccountSavingsCreate,
                    parse_obj_as(
                        type_=MonetaryAccountSavingsCreate,
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

    def read_monetary_account_savings_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MonetaryAccountSavingsRead]:
        """
        Get a specific MonetaryAccountSavings.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MonetaryAccountSavingsRead]
            With MonetaryAccountSavings you can create a new savings account.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account-savings/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MonetaryAccountSavingsRead,
                    parse_obj_as(
                        type_=MonetaryAccountSavingsRead,
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

    def update_monetary_account_savings_for_user(
        self,
        user_id: int,
        item_id: int,
        *,
        currency: str,
        all_co_owner: typing.Optional[typing.Sequence[CoOwner]] = OMIT,
        avatar_uuid: typing.Optional[str] = OMIT,
        daily_limit: typing.Optional[Amount] = OMIT,
        description: typing.Optional[str] = OMIT,
        reason: typing.Optional[str] = OMIT,
        reason_description: typing.Optional[str] = OMIT,
        savings_goal: typing.Optional[Amount] = OMIT,
        setting: typing.Optional[MonetaryAccountSetting] = OMIT,
        status: typing.Optional[str] = OMIT,
        sub_status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[MonetaryAccountSavingsUpdate]:
        """
        Update a specific existing MonetaryAccountSavings.

        Parameters
        ----------
        user_id : int


        item_id : int


        currency : str
            The currency of the MonetaryAccountSavings as an ISO 4217 formatted currency code.

        all_co_owner : typing.Optional[typing.Sequence[CoOwner]]
            The users the account will be joint with.

        avatar_uuid : typing.Optional[str]
            The UUID of the Avatar of the MonetaryAccountSavings.

        daily_limit : typing.Optional[Amount]
            The daily spending limit Amount of the MonetaryAccountSavings. Defaults to 1000 EUR. Currency must match the MonetaryAccountSavings's currency. Limited to 10000 EUR.

        description : typing.Optional[str]
            The description of the MonetaryAccountSavings. Defaults to 'bunq account'.

        reason : typing.Optional[str]
            The reason for voluntarily cancelling (closing) the MonetaryAccountSavings, can only be OTHER. Should only be specified if updating the status to CANCELLED.

        reason_description : typing.Optional[str]
            The optional free-form reason for voluntarily cancelling (closing) the MonetaryAccountSavings. Can be any user provided message. Should only be specified if updating the status to CANCELLED.

        savings_goal : typing.Optional[Amount]
            The Savings Goal set for this MonetaryAccountSavings.

        setting : typing.Optional[MonetaryAccountSetting]
            The settings of the MonetaryAccountSavings.

        status : typing.Optional[str]
            The status of the MonetaryAccountSavings. Ignored in POST requests (always set to ACTIVE) can be CANCELLED or PENDING_REOPEN in PUT requests to cancel (close) or reopen the MonetaryAccountSavings. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).

        sub_status : typing.Optional[str]
            The sub-status of the MonetaryAccountSavings providing extra information regarding the status. Should be ignored for POST requests. In case of PUT requests with status CANCELLED it can only be REDEMPTION_VOLUNTARY, while with status PENDING_REOPEN it can only be NONE. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MonetaryAccountSavingsUpdate]
            With MonetaryAccountSavings you can create a new savings account.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account-savings/{jsonable_encoder(item_id)}",
            method="PUT",
            json={
                "all_co_owner": convert_and_respect_annotation_metadata(
                    object_=all_co_owner, annotation=typing.Sequence[CoOwner], direction="write"
                ),
                "avatar_uuid": avatar_uuid,
                "currency": currency,
                "daily_limit": convert_and_respect_annotation_metadata(
                    object_=daily_limit, annotation=Amount, direction="write"
                ),
                "description": description,
                "reason": reason,
                "reason_description": reason_description,
                "savings_goal": convert_and_respect_annotation_metadata(
                    object_=savings_goal, annotation=Amount, direction="write"
                ),
                "setting": convert_and_respect_annotation_metadata(
                    object_=setting, annotation=MonetaryAccountSetting, direction="write"
                ),
                "status": status,
                "sub_status": sub_status,
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
                    MonetaryAccountSavingsUpdate,
                    parse_obj_as(
                        type_=MonetaryAccountSavingsUpdate,
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


class AsyncRawMonetaryAccountSavingsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_all_monetary_account_savings_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[MonetaryAccountSavingsListing]]:
        """
        Gets a listing of all MonetaryAccountSavingss of a given user.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[MonetaryAccountSavingsListing]]
            With MonetaryAccountSavings you can create a new savings account.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account-savings",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[MonetaryAccountSavingsListing],
                    parse_obj_as(
                        type_=typing.List[MonetaryAccountSavingsListing],
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

    async def create_monetary_account_savings_for_user(
        self,
        user_id: int,
        *,
        currency: str,
        all_co_owner: typing.Optional[typing.Sequence[CoOwner]] = OMIT,
        avatar_uuid: typing.Optional[str] = OMIT,
        daily_limit: typing.Optional[Amount] = OMIT,
        description: typing.Optional[str] = OMIT,
        reason: typing.Optional[str] = OMIT,
        reason_description: typing.Optional[str] = OMIT,
        savings_goal: typing.Optional[Amount] = OMIT,
        setting: typing.Optional[MonetaryAccountSetting] = OMIT,
        status: typing.Optional[str] = OMIT,
        sub_status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[MonetaryAccountSavingsCreate]:
        """
        Create new MonetaryAccountSavings.

        Parameters
        ----------
        user_id : int


        currency : str
            The currency of the MonetaryAccountSavings as an ISO 4217 formatted currency code.

        all_co_owner : typing.Optional[typing.Sequence[CoOwner]]
            The users the account will be joint with.

        avatar_uuid : typing.Optional[str]
            The UUID of the Avatar of the MonetaryAccountSavings.

        daily_limit : typing.Optional[Amount]
            The daily spending limit Amount of the MonetaryAccountSavings. Defaults to 1000 EUR. Currency must match the MonetaryAccountSavings's currency. Limited to 10000 EUR.

        description : typing.Optional[str]
            The description of the MonetaryAccountSavings. Defaults to 'bunq account'.

        reason : typing.Optional[str]
            The reason for voluntarily cancelling (closing) the MonetaryAccountSavings, can only be OTHER. Should only be specified if updating the status to CANCELLED.

        reason_description : typing.Optional[str]
            The optional free-form reason for voluntarily cancelling (closing) the MonetaryAccountSavings. Can be any user provided message. Should only be specified if updating the status to CANCELLED.

        savings_goal : typing.Optional[Amount]
            The Savings Goal set for this MonetaryAccountSavings.

        setting : typing.Optional[MonetaryAccountSetting]
            The settings of the MonetaryAccountSavings.

        status : typing.Optional[str]
            The status of the MonetaryAccountSavings. Ignored in POST requests (always set to ACTIVE) can be CANCELLED or PENDING_REOPEN in PUT requests to cancel (close) or reopen the MonetaryAccountSavings. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).

        sub_status : typing.Optional[str]
            The sub-status of the MonetaryAccountSavings providing extra information regarding the status. Should be ignored for POST requests. In case of PUT requests with status CANCELLED it can only be REDEMPTION_VOLUNTARY, while with status PENDING_REOPEN it can only be NONE. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MonetaryAccountSavingsCreate]
            With MonetaryAccountSavings you can create a new savings account.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account-savings",
            method="POST",
            json={
                "all_co_owner": convert_and_respect_annotation_metadata(
                    object_=all_co_owner, annotation=typing.Sequence[CoOwner], direction="write"
                ),
                "avatar_uuid": avatar_uuid,
                "currency": currency,
                "daily_limit": convert_and_respect_annotation_metadata(
                    object_=daily_limit, annotation=Amount, direction="write"
                ),
                "description": description,
                "reason": reason,
                "reason_description": reason_description,
                "savings_goal": convert_and_respect_annotation_metadata(
                    object_=savings_goal, annotation=Amount, direction="write"
                ),
                "setting": convert_and_respect_annotation_metadata(
                    object_=setting, annotation=MonetaryAccountSetting, direction="write"
                ),
                "status": status,
                "sub_status": sub_status,
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
                    MonetaryAccountSavingsCreate,
                    parse_obj_as(
                        type_=MonetaryAccountSavingsCreate,
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

    async def read_monetary_account_savings_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MonetaryAccountSavingsRead]:
        """
        Get a specific MonetaryAccountSavings.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MonetaryAccountSavingsRead]
            With MonetaryAccountSavings you can create a new savings account.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account-savings/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MonetaryAccountSavingsRead,
                    parse_obj_as(
                        type_=MonetaryAccountSavingsRead,
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

    async def update_monetary_account_savings_for_user(
        self,
        user_id: int,
        item_id: int,
        *,
        currency: str,
        all_co_owner: typing.Optional[typing.Sequence[CoOwner]] = OMIT,
        avatar_uuid: typing.Optional[str] = OMIT,
        daily_limit: typing.Optional[Amount] = OMIT,
        description: typing.Optional[str] = OMIT,
        reason: typing.Optional[str] = OMIT,
        reason_description: typing.Optional[str] = OMIT,
        savings_goal: typing.Optional[Amount] = OMIT,
        setting: typing.Optional[MonetaryAccountSetting] = OMIT,
        status: typing.Optional[str] = OMIT,
        sub_status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[MonetaryAccountSavingsUpdate]:
        """
        Update a specific existing MonetaryAccountSavings.

        Parameters
        ----------
        user_id : int


        item_id : int


        currency : str
            The currency of the MonetaryAccountSavings as an ISO 4217 formatted currency code.

        all_co_owner : typing.Optional[typing.Sequence[CoOwner]]
            The users the account will be joint with.

        avatar_uuid : typing.Optional[str]
            The UUID of the Avatar of the MonetaryAccountSavings.

        daily_limit : typing.Optional[Amount]
            The daily spending limit Amount of the MonetaryAccountSavings. Defaults to 1000 EUR. Currency must match the MonetaryAccountSavings's currency. Limited to 10000 EUR.

        description : typing.Optional[str]
            The description of the MonetaryAccountSavings. Defaults to 'bunq account'.

        reason : typing.Optional[str]
            The reason for voluntarily cancelling (closing) the MonetaryAccountSavings, can only be OTHER. Should only be specified if updating the status to CANCELLED.

        reason_description : typing.Optional[str]
            The optional free-form reason for voluntarily cancelling (closing) the MonetaryAccountSavings. Can be any user provided message. Should only be specified if updating the status to CANCELLED.

        savings_goal : typing.Optional[Amount]
            The Savings Goal set for this MonetaryAccountSavings.

        setting : typing.Optional[MonetaryAccountSetting]
            The settings of the MonetaryAccountSavings.

        status : typing.Optional[str]
            The status of the MonetaryAccountSavings. Ignored in POST requests (always set to ACTIVE) can be CANCELLED or PENDING_REOPEN in PUT requests to cancel (close) or reopen the MonetaryAccountSavings. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).

        sub_status : typing.Optional[str]
            The sub-status of the MonetaryAccountSavings providing extra information regarding the status. Should be ignored for POST requests. In case of PUT requests with status CANCELLED it can only be REDEMPTION_VOLUNTARY, while with status PENDING_REOPEN it can only be NONE. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MonetaryAccountSavingsUpdate]
            With MonetaryAccountSavings you can create a new savings account.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account-savings/{jsonable_encoder(item_id)}",
            method="PUT",
            json={
                "all_co_owner": convert_and_respect_annotation_metadata(
                    object_=all_co_owner, annotation=typing.Sequence[CoOwner], direction="write"
                ),
                "avatar_uuid": avatar_uuid,
                "currency": currency,
                "daily_limit": convert_and_respect_annotation_metadata(
                    object_=daily_limit, annotation=Amount, direction="write"
                ),
                "description": description,
                "reason": reason,
                "reason_description": reason_description,
                "savings_goal": convert_and_respect_annotation_metadata(
                    object_=savings_goal, annotation=Amount, direction="write"
                ),
                "setting": convert_and_respect_annotation_metadata(
                    object_=setting, annotation=MonetaryAccountSetting, direction="write"
                ),
                "status": status,
                "sub_status": sub_status,
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
                    MonetaryAccountSavingsUpdate,
                    parse_obj_as(
                        type_=MonetaryAccountSavingsUpdate,
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

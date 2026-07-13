

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
from ..types.monetary_account_joint_create import MonetaryAccountJointCreate
from ..types.monetary_account_joint_listing import MonetaryAccountJointListing
from ..types.monetary_account_joint_read import MonetaryAccountJointRead
from ..types.monetary_account_joint_update import MonetaryAccountJointUpdate
from ..types.monetary_account_setting import MonetaryAccountSetting
from ..types.pointer import Pointer


OMIT = typing.cast(typing.Any, ...)


class RawMonetaryAccountJointClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_all_monetary_account_joint_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[MonetaryAccountJointListing]]:
        """
        The endpoint for joint monetary accounts.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[MonetaryAccountJointListing]]
            The endpoint for joint monetary accounts.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account-joint",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[MonetaryAccountJointListing],
                    parse_obj_as(
                        type_=typing.List[MonetaryAccountJointListing],
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

    def create_monetary_account_joint_for_user(
        self,
        user_id: int,
        *,
        all_co_owner: typing.Sequence[CoOwner],
        currency: str,
        alias: typing.Optional[typing.Sequence[Pointer]] = OMIT,
        avatar_uuid: typing.Optional[str] = OMIT,
        daily_limit: typing.Optional[Amount] = OMIT,
        description: typing.Optional[str] = OMIT,
        overdraft_limit: typing.Optional[Amount] = OMIT,
        reason: typing.Optional[str] = OMIT,
        reason_description: typing.Optional[str] = OMIT,
        setting: typing.Optional[MonetaryAccountSetting] = OMIT,
        status: typing.Optional[str] = OMIT,
        sub_status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[MonetaryAccountJointCreate]:
        """
        The endpoint for joint monetary accounts.

        Parameters
        ----------
        user_id : int


        all_co_owner : typing.Sequence[CoOwner]
            The users the account will be joint with.

        currency : str
            The currency of the MonetaryAccountJoint as an ISO 4217 formatted currency code.

        alias : typing.Optional[typing.Sequence[Pointer]]
            The Aliases to add to MonetaryAccountJoint. Must all be confirmed first. Can mostly be ignored.

        avatar_uuid : typing.Optional[str]
            The UUID of the Avatar of the MonetaryAccountJoint.

        daily_limit : typing.Optional[Amount]
            The daily spending limit Amount of the MonetaryAccountJoint. Defaults to 1000 EUR. Currency must match the MonetaryAccountJoint's currency. Limited to 10000 EUR.

        description : typing.Optional[str]
            The description of the MonetaryAccountJoint. Defaults to 'bunq account'.

        overdraft_limit : typing.Optional[Amount]
            The maximum Amount the MonetaryAccountJoint can be 'in the red'. Must be 0 EUR or omitted.

        reason : typing.Optional[str]
            The reason for voluntarily cancelling (closing) the MonetaryAccountJoint, can only be OTHER. Should only be specified if updating the status to CANCELLED.

        reason_description : typing.Optional[str]
            The optional free-form reason for voluntarily cancelling (closing) the MonetaryAccountJoint. Can be any user provided message. Should only be specified if updating the status to CANCELLED.

        setting : typing.Optional[MonetaryAccountSetting]
            The settings of the MonetaryAccountJoint.

        status : typing.Optional[str]
            The status of the MonetaryAccountJoint. Ignored in POST requests (always set to ACTIVE) can be CANCELLED or PENDING_REOPEN in PUT requests to cancel (close) or reopen the MonetaryAccountJoint. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).

        sub_status : typing.Optional[str]
            The sub-status of the MonetaryAccountJoint providing extra information regarding the status. Should be ignored for POST requests. In case of PUT requests with status CANCELLED it can only be REDEMPTION_VOLUNTARY, while with status PENDING_REOPEN it can only be NONE. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MonetaryAccountJointCreate]
            The endpoint for joint monetary accounts.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account-joint",
            method="POST",
            json={
                "alias": convert_and_respect_annotation_metadata(
                    object_=alias, annotation=typing.Sequence[Pointer], direction="write"
                ),
                "all_co_owner": convert_and_respect_annotation_metadata(
                    object_=all_co_owner, annotation=typing.Sequence[CoOwner], direction="write"
                ),
                "avatar_uuid": avatar_uuid,
                "currency": currency,
                "daily_limit": convert_and_respect_annotation_metadata(
                    object_=daily_limit, annotation=Amount, direction="write"
                ),
                "description": description,
                "overdraft_limit": convert_and_respect_annotation_metadata(
                    object_=overdraft_limit, annotation=Amount, direction="write"
                ),
                "reason": reason,
                "reason_description": reason_description,
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
                    MonetaryAccountJointCreate,
                    parse_obj_as(
                        type_=MonetaryAccountJointCreate,
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

    def read_monetary_account_joint_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MonetaryAccountJointRead]:
        """
        The endpoint for joint monetary accounts.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MonetaryAccountJointRead]
            The endpoint for joint monetary accounts.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account-joint/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MonetaryAccountJointRead,
                    parse_obj_as(
                        type_=MonetaryAccountJointRead,
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

    def update_monetary_account_joint_for_user(
        self,
        user_id: int,
        item_id: int,
        *,
        all_co_owner: typing.Sequence[CoOwner],
        currency: str,
        alias: typing.Optional[typing.Sequence[Pointer]] = OMIT,
        avatar_uuid: typing.Optional[str] = OMIT,
        daily_limit: typing.Optional[Amount] = OMIT,
        description: typing.Optional[str] = OMIT,
        overdraft_limit: typing.Optional[Amount] = OMIT,
        reason: typing.Optional[str] = OMIT,
        reason_description: typing.Optional[str] = OMIT,
        setting: typing.Optional[MonetaryAccountSetting] = OMIT,
        status: typing.Optional[str] = OMIT,
        sub_status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[MonetaryAccountJointUpdate]:
        """
        The endpoint for joint monetary accounts.

        Parameters
        ----------
        user_id : int


        item_id : int


        all_co_owner : typing.Sequence[CoOwner]
            The users the account will be joint with.

        currency : str
            The currency of the MonetaryAccountJoint as an ISO 4217 formatted currency code.

        alias : typing.Optional[typing.Sequence[Pointer]]
            The Aliases to add to MonetaryAccountJoint. Must all be confirmed first. Can mostly be ignored.

        avatar_uuid : typing.Optional[str]
            The UUID of the Avatar of the MonetaryAccountJoint.

        daily_limit : typing.Optional[Amount]
            The daily spending limit Amount of the MonetaryAccountJoint. Defaults to 1000 EUR. Currency must match the MonetaryAccountJoint's currency. Limited to 10000 EUR.

        description : typing.Optional[str]
            The description of the MonetaryAccountJoint. Defaults to 'bunq account'.

        overdraft_limit : typing.Optional[Amount]
            The maximum Amount the MonetaryAccountJoint can be 'in the red'. Must be 0 EUR or omitted.

        reason : typing.Optional[str]
            The reason for voluntarily cancelling (closing) the MonetaryAccountJoint, can only be OTHER. Should only be specified if updating the status to CANCELLED.

        reason_description : typing.Optional[str]
            The optional free-form reason for voluntarily cancelling (closing) the MonetaryAccountJoint. Can be any user provided message. Should only be specified if updating the status to CANCELLED.

        setting : typing.Optional[MonetaryAccountSetting]
            The settings of the MonetaryAccountJoint.

        status : typing.Optional[str]
            The status of the MonetaryAccountJoint. Ignored in POST requests (always set to ACTIVE) can be CANCELLED or PENDING_REOPEN in PUT requests to cancel (close) or reopen the MonetaryAccountJoint. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).

        sub_status : typing.Optional[str]
            The sub-status of the MonetaryAccountJoint providing extra information regarding the status. Should be ignored for POST requests. In case of PUT requests with status CANCELLED it can only be REDEMPTION_VOLUNTARY, while with status PENDING_REOPEN it can only be NONE. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MonetaryAccountJointUpdate]
            The endpoint for joint monetary accounts.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account-joint/{jsonable_encoder(item_id)}",
            method="PUT",
            json={
                "alias": convert_and_respect_annotation_metadata(
                    object_=alias, annotation=typing.Sequence[Pointer], direction="write"
                ),
                "all_co_owner": convert_and_respect_annotation_metadata(
                    object_=all_co_owner, annotation=typing.Sequence[CoOwner], direction="write"
                ),
                "avatar_uuid": avatar_uuid,
                "currency": currency,
                "daily_limit": convert_and_respect_annotation_metadata(
                    object_=daily_limit, annotation=Amount, direction="write"
                ),
                "description": description,
                "overdraft_limit": convert_and_respect_annotation_metadata(
                    object_=overdraft_limit, annotation=Amount, direction="write"
                ),
                "reason": reason,
                "reason_description": reason_description,
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
                    MonetaryAccountJointUpdate,
                    parse_obj_as(
                        type_=MonetaryAccountJointUpdate,
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


class AsyncRawMonetaryAccountJointClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_all_monetary_account_joint_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[MonetaryAccountJointListing]]:
        """
        The endpoint for joint monetary accounts.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[MonetaryAccountJointListing]]
            The endpoint for joint monetary accounts.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account-joint",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[MonetaryAccountJointListing],
                    parse_obj_as(
                        type_=typing.List[MonetaryAccountJointListing],
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

    async def create_monetary_account_joint_for_user(
        self,
        user_id: int,
        *,
        all_co_owner: typing.Sequence[CoOwner],
        currency: str,
        alias: typing.Optional[typing.Sequence[Pointer]] = OMIT,
        avatar_uuid: typing.Optional[str] = OMIT,
        daily_limit: typing.Optional[Amount] = OMIT,
        description: typing.Optional[str] = OMIT,
        overdraft_limit: typing.Optional[Amount] = OMIT,
        reason: typing.Optional[str] = OMIT,
        reason_description: typing.Optional[str] = OMIT,
        setting: typing.Optional[MonetaryAccountSetting] = OMIT,
        status: typing.Optional[str] = OMIT,
        sub_status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[MonetaryAccountJointCreate]:
        """
        The endpoint for joint monetary accounts.

        Parameters
        ----------
        user_id : int


        all_co_owner : typing.Sequence[CoOwner]
            The users the account will be joint with.

        currency : str
            The currency of the MonetaryAccountJoint as an ISO 4217 formatted currency code.

        alias : typing.Optional[typing.Sequence[Pointer]]
            The Aliases to add to MonetaryAccountJoint. Must all be confirmed first. Can mostly be ignored.

        avatar_uuid : typing.Optional[str]
            The UUID of the Avatar of the MonetaryAccountJoint.

        daily_limit : typing.Optional[Amount]
            The daily spending limit Amount of the MonetaryAccountJoint. Defaults to 1000 EUR. Currency must match the MonetaryAccountJoint's currency. Limited to 10000 EUR.

        description : typing.Optional[str]
            The description of the MonetaryAccountJoint. Defaults to 'bunq account'.

        overdraft_limit : typing.Optional[Amount]
            The maximum Amount the MonetaryAccountJoint can be 'in the red'. Must be 0 EUR or omitted.

        reason : typing.Optional[str]
            The reason for voluntarily cancelling (closing) the MonetaryAccountJoint, can only be OTHER. Should only be specified if updating the status to CANCELLED.

        reason_description : typing.Optional[str]
            The optional free-form reason for voluntarily cancelling (closing) the MonetaryAccountJoint. Can be any user provided message. Should only be specified if updating the status to CANCELLED.

        setting : typing.Optional[MonetaryAccountSetting]
            The settings of the MonetaryAccountJoint.

        status : typing.Optional[str]
            The status of the MonetaryAccountJoint. Ignored in POST requests (always set to ACTIVE) can be CANCELLED or PENDING_REOPEN in PUT requests to cancel (close) or reopen the MonetaryAccountJoint. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).

        sub_status : typing.Optional[str]
            The sub-status of the MonetaryAccountJoint providing extra information regarding the status. Should be ignored for POST requests. In case of PUT requests with status CANCELLED it can only be REDEMPTION_VOLUNTARY, while with status PENDING_REOPEN it can only be NONE. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MonetaryAccountJointCreate]
            The endpoint for joint monetary accounts.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account-joint",
            method="POST",
            json={
                "alias": convert_and_respect_annotation_metadata(
                    object_=alias, annotation=typing.Sequence[Pointer], direction="write"
                ),
                "all_co_owner": convert_and_respect_annotation_metadata(
                    object_=all_co_owner, annotation=typing.Sequence[CoOwner], direction="write"
                ),
                "avatar_uuid": avatar_uuid,
                "currency": currency,
                "daily_limit": convert_and_respect_annotation_metadata(
                    object_=daily_limit, annotation=Amount, direction="write"
                ),
                "description": description,
                "overdraft_limit": convert_and_respect_annotation_metadata(
                    object_=overdraft_limit, annotation=Amount, direction="write"
                ),
                "reason": reason,
                "reason_description": reason_description,
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
                    MonetaryAccountJointCreate,
                    parse_obj_as(
                        type_=MonetaryAccountJointCreate,
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

    async def read_monetary_account_joint_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MonetaryAccountJointRead]:
        """
        The endpoint for joint monetary accounts.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MonetaryAccountJointRead]
            The endpoint for joint monetary accounts.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account-joint/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MonetaryAccountJointRead,
                    parse_obj_as(
                        type_=MonetaryAccountJointRead,
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

    async def update_monetary_account_joint_for_user(
        self,
        user_id: int,
        item_id: int,
        *,
        all_co_owner: typing.Sequence[CoOwner],
        currency: str,
        alias: typing.Optional[typing.Sequence[Pointer]] = OMIT,
        avatar_uuid: typing.Optional[str] = OMIT,
        daily_limit: typing.Optional[Amount] = OMIT,
        description: typing.Optional[str] = OMIT,
        overdraft_limit: typing.Optional[Amount] = OMIT,
        reason: typing.Optional[str] = OMIT,
        reason_description: typing.Optional[str] = OMIT,
        setting: typing.Optional[MonetaryAccountSetting] = OMIT,
        status: typing.Optional[str] = OMIT,
        sub_status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[MonetaryAccountJointUpdate]:
        """
        The endpoint for joint monetary accounts.

        Parameters
        ----------
        user_id : int


        item_id : int


        all_co_owner : typing.Sequence[CoOwner]
            The users the account will be joint with.

        currency : str
            The currency of the MonetaryAccountJoint as an ISO 4217 formatted currency code.

        alias : typing.Optional[typing.Sequence[Pointer]]
            The Aliases to add to MonetaryAccountJoint. Must all be confirmed first. Can mostly be ignored.

        avatar_uuid : typing.Optional[str]
            The UUID of the Avatar of the MonetaryAccountJoint.

        daily_limit : typing.Optional[Amount]
            The daily spending limit Amount of the MonetaryAccountJoint. Defaults to 1000 EUR. Currency must match the MonetaryAccountJoint's currency. Limited to 10000 EUR.

        description : typing.Optional[str]
            The description of the MonetaryAccountJoint. Defaults to 'bunq account'.

        overdraft_limit : typing.Optional[Amount]
            The maximum Amount the MonetaryAccountJoint can be 'in the red'. Must be 0 EUR or omitted.

        reason : typing.Optional[str]
            The reason for voluntarily cancelling (closing) the MonetaryAccountJoint, can only be OTHER. Should only be specified if updating the status to CANCELLED.

        reason_description : typing.Optional[str]
            The optional free-form reason for voluntarily cancelling (closing) the MonetaryAccountJoint. Can be any user provided message. Should only be specified if updating the status to CANCELLED.

        setting : typing.Optional[MonetaryAccountSetting]
            The settings of the MonetaryAccountJoint.

        status : typing.Optional[str]
            The status of the MonetaryAccountJoint. Ignored in POST requests (always set to ACTIVE) can be CANCELLED or PENDING_REOPEN in PUT requests to cancel (close) or reopen the MonetaryAccountJoint. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).

        sub_status : typing.Optional[str]
            The sub-status of the MonetaryAccountJoint providing extra information regarding the status. Should be ignored for POST requests. In case of PUT requests with status CANCELLED it can only be REDEMPTION_VOLUNTARY, while with status PENDING_REOPEN it can only be NONE. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MonetaryAccountJointUpdate]
            The endpoint for joint monetary accounts.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account-joint/{jsonable_encoder(item_id)}",
            method="PUT",
            json={
                "alias": convert_and_respect_annotation_metadata(
                    object_=alias, annotation=typing.Sequence[Pointer], direction="write"
                ),
                "all_co_owner": convert_and_respect_annotation_metadata(
                    object_=all_co_owner, annotation=typing.Sequence[CoOwner], direction="write"
                ),
                "avatar_uuid": avatar_uuid,
                "currency": currency,
                "daily_limit": convert_and_respect_annotation_metadata(
                    object_=daily_limit, annotation=Amount, direction="write"
                ),
                "description": description,
                "overdraft_limit": convert_and_respect_annotation_metadata(
                    object_=overdraft_limit, annotation=Amount, direction="write"
                ),
                "reason": reason,
                "reason_description": reason_description,
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
                    MonetaryAccountJointUpdate,
                    parse_obj_as(
                        type_=MonetaryAccountJointUpdate,
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



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
from ..types.monetary_account_bank_create import MonetaryAccountBankCreate
from ..types.monetary_account_bank_listing import MonetaryAccountBankListing
from ..types.monetary_account_bank_read import MonetaryAccountBankRead
from ..types.monetary_account_bank_update import MonetaryAccountBankUpdate
from ..types.monetary_account_setting import MonetaryAccountSetting
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawMonetaryAccountBankClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_all_monetary_account_bank_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[MonetaryAccountBankListing]]:
        """
        Gets a listing of all MonetaryAccountBanks of a given user.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[MonetaryAccountBankListing]]
            With MonetaryAccountBank you can create a new bank account, retrieve information regarding your existing MonetaryAccountBanks and update specific fields of an existing MonetaryAccountBank. Examples of fields that can be updated are the description, the daily limit and the avatar of the account.<br/><br/>Notification filters can be set on a monetary account level to receive callbacks. For more information check the <a href="/api/1/page/callbacks">dedicated callbacks page</a>.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account-bank",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[MonetaryAccountBankListing],
                    parse_obj_as(
                        type_=typing.List[MonetaryAccountBankListing],
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

    def create_monetary_account_bank_for_user(
        self,
        user_id: int,
        *,
        currency: str,
        avatar_uuid: typing.Optional[str] = OMIT,
        country_iban: typing.Optional[str] = OMIT,
        daily_limit: typing.Optional[Amount] = OMIT,
        description: typing.Optional[str] = OMIT,
        display_name: typing.Optional[str] = OMIT,
        reason: typing.Optional[str] = OMIT,
        reason_description: typing.Optional[str] = OMIT,
        setting: typing.Optional[MonetaryAccountSetting] = OMIT,
        status: typing.Optional[str] = OMIT,
        sub_status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[MonetaryAccountBankCreate]:
        """
        Create new MonetaryAccountBank.

        Parameters
        ----------
        user_id : int


        currency : str
            The currency of the MonetaryAccountBank as an ISO 4217 formatted currency code.

        avatar_uuid : typing.Optional[str]
            The UUID of the Avatar of the MonetaryAccountBank.

        country_iban : typing.Optional[str]
            The country of the monetary account IBAN.

        daily_limit : typing.Optional[Amount]
            The daily spending limit Amount of the MonetaryAccountBank. Defaults to 1000 EUR. Currency must match the MonetaryAccountBank's currency. Limited to 10000 EUR.

        description : typing.Optional[str]
            The description of the MonetaryAccountBank. Defaults to 'bunq account'.

        display_name : typing.Optional[str]
            The legal name of the user / company using this monetary account.

        reason : typing.Optional[str]
            The reason for voluntarily cancelling (closing) the MonetaryAccountBank, can only be OTHER. Should only be specified if updating the status to CANCELLED.

        reason_description : typing.Optional[str]
            The optional free-form reason for voluntarily cancelling (closing) the MonetaryAccountBank. Can be any user provided message. Should only be specified if updating the status to CANCELLED.

        setting : typing.Optional[MonetaryAccountSetting]
            The settings of the MonetaryAccountBank.

        status : typing.Optional[str]
            The status of the MonetaryAccountBank. Ignored in POST requests (always set to ACTIVE) can be CANCELLED or PENDING_REOPEN in PUT requests to cancel (close) or reopen the MonetaryAccountBank. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).

        sub_status : typing.Optional[str]
            The sub-status of the MonetaryAccountBank providing extra information regarding the status. Should be ignored for POST requests. In case of PUT requests with status CANCELLED it can only be REDEMPTION_VOLUNTARY, while with status PENDING_REOPEN it can only be NONE. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MonetaryAccountBankCreate]
            With MonetaryAccountBank you can create a new bank account, retrieve information regarding your existing MonetaryAccountBanks and update specific fields of an existing MonetaryAccountBank. Examples of fields that can be updated are the description, the daily limit and the avatar of the account.<br/><br/>Notification filters can be set on a monetary account level to receive callbacks. For more information check the <a href="/api/1/page/callbacks">dedicated callbacks page</a>.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account-bank",
            method="POST",
            json={
                "avatar_uuid": avatar_uuid,
                "country_iban": country_iban,
                "currency": currency,
                "daily_limit": convert_and_respect_annotation_metadata(
                    object_=daily_limit, annotation=Amount, direction="write"
                ),
                "description": description,
                "display_name": display_name,
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
                    MonetaryAccountBankCreate,
                    parse_obj_as(
                        type_=MonetaryAccountBankCreate,
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

    def read_monetary_account_bank_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MonetaryAccountBankRead]:
        """
        Get a specific MonetaryAccountBank.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MonetaryAccountBankRead]
            With MonetaryAccountBank you can create a new bank account, retrieve information regarding your existing MonetaryAccountBanks and update specific fields of an existing MonetaryAccountBank. Examples of fields that can be updated are the description, the daily limit and the avatar of the account.<br/><br/>Notification filters can be set on a monetary account level to receive callbacks. For more information check the <a href="/api/1/page/callbacks">dedicated callbacks page</a>.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account-bank/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MonetaryAccountBankRead,
                    parse_obj_as(
                        type_=MonetaryAccountBankRead,
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

    def update_monetary_account_bank_for_user(
        self,
        user_id: int,
        item_id: int,
        *,
        currency: str,
        avatar_uuid: typing.Optional[str] = OMIT,
        country_iban: typing.Optional[str] = OMIT,
        daily_limit: typing.Optional[Amount] = OMIT,
        description: typing.Optional[str] = OMIT,
        display_name: typing.Optional[str] = OMIT,
        reason: typing.Optional[str] = OMIT,
        reason_description: typing.Optional[str] = OMIT,
        setting: typing.Optional[MonetaryAccountSetting] = OMIT,
        status: typing.Optional[str] = OMIT,
        sub_status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[MonetaryAccountBankUpdate]:
        """
        Update a specific existing MonetaryAccountBank.

        Parameters
        ----------
        user_id : int


        item_id : int


        currency : str
            The currency of the MonetaryAccountBank as an ISO 4217 formatted currency code.

        avatar_uuid : typing.Optional[str]
            The UUID of the Avatar of the MonetaryAccountBank.

        country_iban : typing.Optional[str]
            The country of the monetary account IBAN.

        daily_limit : typing.Optional[Amount]
            The daily spending limit Amount of the MonetaryAccountBank. Defaults to 1000 EUR. Currency must match the MonetaryAccountBank's currency. Limited to 10000 EUR.

        description : typing.Optional[str]
            The description of the MonetaryAccountBank. Defaults to 'bunq account'.

        display_name : typing.Optional[str]
            The legal name of the user / company using this monetary account.

        reason : typing.Optional[str]
            The reason for voluntarily cancelling (closing) the MonetaryAccountBank, can only be OTHER. Should only be specified if updating the status to CANCELLED.

        reason_description : typing.Optional[str]
            The optional free-form reason for voluntarily cancelling (closing) the MonetaryAccountBank. Can be any user provided message. Should only be specified if updating the status to CANCELLED.

        setting : typing.Optional[MonetaryAccountSetting]
            The settings of the MonetaryAccountBank.

        status : typing.Optional[str]
            The status of the MonetaryAccountBank. Ignored in POST requests (always set to ACTIVE) can be CANCELLED or PENDING_REOPEN in PUT requests to cancel (close) or reopen the MonetaryAccountBank. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).

        sub_status : typing.Optional[str]
            The sub-status of the MonetaryAccountBank providing extra information regarding the status. Should be ignored for POST requests. In case of PUT requests with status CANCELLED it can only be REDEMPTION_VOLUNTARY, while with status PENDING_REOPEN it can only be NONE. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MonetaryAccountBankUpdate]
            With MonetaryAccountBank you can create a new bank account, retrieve information regarding your existing MonetaryAccountBanks and update specific fields of an existing MonetaryAccountBank. Examples of fields that can be updated are the description, the daily limit and the avatar of the account.<br/><br/>Notification filters can be set on a monetary account level to receive callbacks. For more information check the <a href="/api/1/page/callbacks">dedicated callbacks page</a>.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account-bank/{encode_path_param(item_id)}",
            method="PUT",
            json={
                "avatar_uuid": avatar_uuid,
                "country_iban": country_iban,
                "currency": currency,
                "daily_limit": convert_and_respect_annotation_metadata(
                    object_=daily_limit, annotation=Amount, direction="write"
                ),
                "description": description,
                "display_name": display_name,
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
                    MonetaryAccountBankUpdate,
                    parse_obj_as(
                        type_=MonetaryAccountBankUpdate,
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


class AsyncRawMonetaryAccountBankClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_all_monetary_account_bank_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[MonetaryAccountBankListing]]:
        """
        Gets a listing of all MonetaryAccountBanks of a given user.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[MonetaryAccountBankListing]]
            With MonetaryAccountBank you can create a new bank account, retrieve information regarding your existing MonetaryAccountBanks and update specific fields of an existing MonetaryAccountBank. Examples of fields that can be updated are the description, the daily limit and the avatar of the account.<br/><br/>Notification filters can be set on a monetary account level to receive callbacks. For more information check the <a href="/api/1/page/callbacks">dedicated callbacks page</a>.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account-bank",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[MonetaryAccountBankListing],
                    parse_obj_as(
                        type_=typing.List[MonetaryAccountBankListing],
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

    async def create_monetary_account_bank_for_user(
        self,
        user_id: int,
        *,
        currency: str,
        avatar_uuid: typing.Optional[str] = OMIT,
        country_iban: typing.Optional[str] = OMIT,
        daily_limit: typing.Optional[Amount] = OMIT,
        description: typing.Optional[str] = OMIT,
        display_name: typing.Optional[str] = OMIT,
        reason: typing.Optional[str] = OMIT,
        reason_description: typing.Optional[str] = OMIT,
        setting: typing.Optional[MonetaryAccountSetting] = OMIT,
        status: typing.Optional[str] = OMIT,
        sub_status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[MonetaryAccountBankCreate]:
        """
        Create new MonetaryAccountBank.

        Parameters
        ----------
        user_id : int


        currency : str
            The currency of the MonetaryAccountBank as an ISO 4217 formatted currency code.

        avatar_uuid : typing.Optional[str]
            The UUID of the Avatar of the MonetaryAccountBank.

        country_iban : typing.Optional[str]
            The country of the monetary account IBAN.

        daily_limit : typing.Optional[Amount]
            The daily spending limit Amount of the MonetaryAccountBank. Defaults to 1000 EUR. Currency must match the MonetaryAccountBank's currency. Limited to 10000 EUR.

        description : typing.Optional[str]
            The description of the MonetaryAccountBank. Defaults to 'bunq account'.

        display_name : typing.Optional[str]
            The legal name of the user / company using this monetary account.

        reason : typing.Optional[str]
            The reason for voluntarily cancelling (closing) the MonetaryAccountBank, can only be OTHER. Should only be specified if updating the status to CANCELLED.

        reason_description : typing.Optional[str]
            The optional free-form reason for voluntarily cancelling (closing) the MonetaryAccountBank. Can be any user provided message. Should only be specified if updating the status to CANCELLED.

        setting : typing.Optional[MonetaryAccountSetting]
            The settings of the MonetaryAccountBank.

        status : typing.Optional[str]
            The status of the MonetaryAccountBank. Ignored in POST requests (always set to ACTIVE) can be CANCELLED or PENDING_REOPEN in PUT requests to cancel (close) or reopen the MonetaryAccountBank. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).

        sub_status : typing.Optional[str]
            The sub-status of the MonetaryAccountBank providing extra information regarding the status. Should be ignored for POST requests. In case of PUT requests with status CANCELLED it can only be REDEMPTION_VOLUNTARY, while with status PENDING_REOPEN it can only be NONE. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MonetaryAccountBankCreate]
            With MonetaryAccountBank you can create a new bank account, retrieve information regarding your existing MonetaryAccountBanks and update specific fields of an existing MonetaryAccountBank. Examples of fields that can be updated are the description, the daily limit and the avatar of the account.<br/><br/>Notification filters can be set on a monetary account level to receive callbacks. For more information check the <a href="/api/1/page/callbacks">dedicated callbacks page</a>.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account-bank",
            method="POST",
            json={
                "avatar_uuid": avatar_uuid,
                "country_iban": country_iban,
                "currency": currency,
                "daily_limit": convert_and_respect_annotation_metadata(
                    object_=daily_limit, annotation=Amount, direction="write"
                ),
                "description": description,
                "display_name": display_name,
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
                    MonetaryAccountBankCreate,
                    parse_obj_as(
                        type_=MonetaryAccountBankCreate,
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

    async def read_monetary_account_bank_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MonetaryAccountBankRead]:
        """
        Get a specific MonetaryAccountBank.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MonetaryAccountBankRead]
            With MonetaryAccountBank you can create a new bank account, retrieve information regarding your existing MonetaryAccountBanks and update specific fields of an existing MonetaryAccountBank. Examples of fields that can be updated are the description, the daily limit and the avatar of the account.<br/><br/>Notification filters can be set on a monetary account level to receive callbacks. For more information check the <a href="/api/1/page/callbacks">dedicated callbacks page</a>.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account-bank/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MonetaryAccountBankRead,
                    parse_obj_as(
                        type_=MonetaryAccountBankRead,
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

    async def update_monetary_account_bank_for_user(
        self,
        user_id: int,
        item_id: int,
        *,
        currency: str,
        avatar_uuid: typing.Optional[str] = OMIT,
        country_iban: typing.Optional[str] = OMIT,
        daily_limit: typing.Optional[Amount] = OMIT,
        description: typing.Optional[str] = OMIT,
        display_name: typing.Optional[str] = OMIT,
        reason: typing.Optional[str] = OMIT,
        reason_description: typing.Optional[str] = OMIT,
        setting: typing.Optional[MonetaryAccountSetting] = OMIT,
        status: typing.Optional[str] = OMIT,
        sub_status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[MonetaryAccountBankUpdate]:
        """
        Update a specific existing MonetaryAccountBank.

        Parameters
        ----------
        user_id : int


        item_id : int


        currency : str
            The currency of the MonetaryAccountBank as an ISO 4217 formatted currency code.

        avatar_uuid : typing.Optional[str]
            The UUID of the Avatar of the MonetaryAccountBank.

        country_iban : typing.Optional[str]
            The country of the monetary account IBAN.

        daily_limit : typing.Optional[Amount]
            The daily spending limit Amount of the MonetaryAccountBank. Defaults to 1000 EUR. Currency must match the MonetaryAccountBank's currency. Limited to 10000 EUR.

        description : typing.Optional[str]
            The description of the MonetaryAccountBank. Defaults to 'bunq account'.

        display_name : typing.Optional[str]
            The legal name of the user / company using this monetary account.

        reason : typing.Optional[str]
            The reason for voluntarily cancelling (closing) the MonetaryAccountBank, can only be OTHER. Should only be specified if updating the status to CANCELLED.

        reason_description : typing.Optional[str]
            The optional free-form reason for voluntarily cancelling (closing) the MonetaryAccountBank. Can be any user provided message. Should only be specified if updating the status to CANCELLED.

        setting : typing.Optional[MonetaryAccountSetting]
            The settings of the MonetaryAccountBank.

        status : typing.Optional[str]
            The status of the MonetaryAccountBank. Ignored in POST requests (always set to ACTIVE) can be CANCELLED or PENDING_REOPEN in PUT requests to cancel (close) or reopen the MonetaryAccountBank. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).

        sub_status : typing.Optional[str]
            The sub-status of the MonetaryAccountBank providing extra information regarding the status. Should be ignored for POST requests. In case of PUT requests with status CANCELLED it can only be REDEMPTION_VOLUNTARY, while with status PENDING_REOPEN it can only be NONE. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MonetaryAccountBankUpdate]
            With MonetaryAccountBank you can create a new bank account, retrieve information regarding your existing MonetaryAccountBanks and update specific fields of an existing MonetaryAccountBank. Examples of fields that can be updated are the description, the daily limit and the avatar of the account.<br/><br/>Notification filters can be set on a monetary account level to receive callbacks. For more information check the <a href="/api/1/page/callbacks">dedicated callbacks page</a>.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account-bank/{encode_path_param(item_id)}",
            method="PUT",
            json={
                "avatar_uuid": avatar_uuid,
                "country_iban": country_iban,
                "currency": currency,
                "daily_limit": convert_and_respect_annotation_metadata(
                    object_=daily_limit, annotation=Amount, direction="write"
                ),
                "description": description,
                "display_name": display_name,
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
                    MonetaryAccountBankUpdate,
                    parse_obj_as(
                        type_=MonetaryAccountBankUpdate,
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

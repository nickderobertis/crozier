

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
from ..types.label_monetary_account import LabelMonetaryAccount
from ..types.label_user import LabelUser
from ..types.relation_user import RelationUser
from ..types.share_detail import ShareDetail
from ..types.share_invite_monetary_account_response_listing import ShareInviteMonetaryAccountResponseListing
from ..types.share_invite_monetary_account_response_read import ShareInviteMonetaryAccountResponseRead
from ..types.share_invite_monetary_account_response_update import ShareInviteMonetaryAccountResponseUpdate
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawShareInviteMonetaryAccountResponseClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_all_share_invite_monetary_account_response_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[ShareInviteMonetaryAccountResponseListing]]:
        """
        Return all the shares a user was invited to.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[ShareInviteMonetaryAccountResponseListing]]
            Used to view or respond to shares a user was invited to. See 'share-invite-bank-inquiry' for more information about the inquiring endpoint.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/share-invite-monetary-account-response",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ShareInviteMonetaryAccountResponseListing],
                    parse_obj_as(
                        type_=typing.List[ShareInviteMonetaryAccountResponseListing],
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

    def read_share_invite_monetary_account_response_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ShareInviteMonetaryAccountResponseRead]:
        """
        Return the details of a specific share a user was invited to.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ShareInviteMonetaryAccountResponseRead]
            Used to view or respond to shares a user was invited to. See 'share-invite-bank-inquiry' for more information about the inquiring endpoint.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/share-invite-monetary-account-response/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ShareInviteMonetaryAccountResponseRead,
                    parse_obj_as(
                        type_=ShareInviteMonetaryAccountResponseRead,
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

    def update_share_invite_monetary_account_response_for_user(
        self,
        user_id: int,
        item_id: int,
        *,
        access_type: typing.Optional[str] = OMIT,
        card_id: typing.Optional[int] = OMIT,
        counter_alias: typing.Optional[LabelMonetaryAccount] = OMIT,
        created: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        draft_share_invite_bank_id: typing.Optional[int] = OMIT,
        end_date: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        monetary_account_id: typing.Optional[int] = OMIT,
        relation_user: typing.Optional[RelationUser] = OMIT,
        share_detail: typing.Optional[ShareDetail] = OMIT,
        share_type: typing.Optional[str] = OMIT,
        start_date: typing.Optional[str] = OMIT,
        status: typing.Optional[str] = OMIT,
        updated: typing.Optional[str] = OMIT,
        user_alias_cancelled: typing.Optional[LabelUser] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ShareInviteMonetaryAccountResponseUpdate]:
        """
        Accept or reject a share a user was invited to.

        Parameters
        ----------
        user_id : int


        item_id : int


        access_type : typing.Optional[str]
            Type of access that is wanted, one of VIEW_BALANCE, VIEW_TRANSACTION, DRAFT_PAYMENT or FULL_TRANSIENT

        card_id : typing.Optional[int]
            The card to link to the shared monetary account. Used only if share_detail is ShareDetailCardPayment.

        counter_alias : typing.Optional[LabelMonetaryAccount]
            The monetary account and user who created the share.

        created : typing.Optional[str]
            The timestamp of the ShareInviteBankResponse creation.

        description : typing.Optional[str]
            The description of this share. It is basically the monetary account description.

        draft_share_invite_bank_id : typing.Optional[int]
            The id of the draft share invite bank.

        end_date : typing.Optional[str]
            The expiration date of this share.

        id : typing.Optional[int]
            The id of the ShareInviteBankResponse.

        monetary_account_id : typing.Optional[int]
            The id of the monetary account the ACCEPTED share applies to. null otherwise.

        relation_user : typing.Optional[RelationUser]
            All of the relation users towards this MA.

        share_detail : typing.Optional[ShareDetail]
            The share details.

        share_type : typing.Optional[str]
            The share type, either STANDARD or MUTUAL.

        start_date : typing.Optional[str]
            The start date of this share.

        status : typing.Optional[str]
            The status of the share. Can be ACTIVE, REVOKED, REJECTED.

        updated : typing.Optional[str]
            The timestamp of the ShareInviteBankResponse last update.

        user_alias_cancelled : typing.Optional[LabelUser]
            The user who cancelled the share if it has been revoked or rejected.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ShareInviteMonetaryAccountResponseUpdate]
            Used to view or respond to shares a user was invited to. See 'share-invite-bank-inquiry' for more information about the inquiring endpoint.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/share-invite-monetary-account-response/{encode_path_param(item_id)}",
            method="PUT",
            json={
                "access_type": access_type,
                "card_id": card_id,
                "counter_alias": convert_and_respect_annotation_metadata(
                    object_=counter_alias, annotation=LabelMonetaryAccount, direction="write"
                ),
                "created": created,
                "description": description,
                "draft_share_invite_bank_id": draft_share_invite_bank_id,
                "end_date": end_date,
                "id": id,
                "monetary_account_id": monetary_account_id,
                "relation_user": convert_and_respect_annotation_metadata(
                    object_=relation_user, annotation=RelationUser, direction="write"
                ),
                "share_detail": convert_and_respect_annotation_metadata(
                    object_=share_detail, annotation=ShareDetail, direction="write"
                ),
                "share_type": share_type,
                "start_date": start_date,
                "status": status,
                "updated": updated,
                "user_alias_cancelled": convert_and_respect_annotation_metadata(
                    object_=user_alias_cancelled, annotation=LabelUser, direction="write"
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
                    ShareInviteMonetaryAccountResponseUpdate,
                    parse_obj_as(
                        type_=ShareInviteMonetaryAccountResponseUpdate,
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


class AsyncRawShareInviteMonetaryAccountResponseClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_all_share_invite_monetary_account_response_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[ShareInviteMonetaryAccountResponseListing]]:
        """
        Return all the shares a user was invited to.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[ShareInviteMonetaryAccountResponseListing]]
            Used to view or respond to shares a user was invited to. See 'share-invite-bank-inquiry' for more information about the inquiring endpoint.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/share-invite-monetary-account-response",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ShareInviteMonetaryAccountResponseListing],
                    parse_obj_as(
                        type_=typing.List[ShareInviteMonetaryAccountResponseListing],
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

    async def read_share_invite_monetary_account_response_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ShareInviteMonetaryAccountResponseRead]:
        """
        Return the details of a specific share a user was invited to.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ShareInviteMonetaryAccountResponseRead]
            Used to view or respond to shares a user was invited to. See 'share-invite-bank-inquiry' for more information about the inquiring endpoint.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/share-invite-monetary-account-response/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ShareInviteMonetaryAccountResponseRead,
                    parse_obj_as(
                        type_=ShareInviteMonetaryAccountResponseRead,
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

    async def update_share_invite_monetary_account_response_for_user(
        self,
        user_id: int,
        item_id: int,
        *,
        access_type: typing.Optional[str] = OMIT,
        card_id: typing.Optional[int] = OMIT,
        counter_alias: typing.Optional[LabelMonetaryAccount] = OMIT,
        created: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        draft_share_invite_bank_id: typing.Optional[int] = OMIT,
        end_date: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        monetary_account_id: typing.Optional[int] = OMIT,
        relation_user: typing.Optional[RelationUser] = OMIT,
        share_detail: typing.Optional[ShareDetail] = OMIT,
        share_type: typing.Optional[str] = OMIT,
        start_date: typing.Optional[str] = OMIT,
        status: typing.Optional[str] = OMIT,
        updated: typing.Optional[str] = OMIT,
        user_alias_cancelled: typing.Optional[LabelUser] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ShareInviteMonetaryAccountResponseUpdate]:
        """
        Accept or reject a share a user was invited to.

        Parameters
        ----------
        user_id : int


        item_id : int


        access_type : typing.Optional[str]
            Type of access that is wanted, one of VIEW_BALANCE, VIEW_TRANSACTION, DRAFT_PAYMENT or FULL_TRANSIENT

        card_id : typing.Optional[int]
            The card to link to the shared monetary account. Used only if share_detail is ShareDetailCardPayment.

        counter_alias : typing.Optional[LabelMonetaryAccount]
            The monetary account and user who created the share.

        created : typing.Optional[str]
            The timestamp of the ShareInviteBankResponse creation.

        description : typing.Optional[str]
            The description of this share. It is basically the monetary account description.

        draft_share_invite_bank_id : typing.Optional[int]
            The id of the draft share invite bank.

        end_date : typing.Optional[str]
            The expiration date of this share.

        id : typing.Optional[int]
            The id of the ShareInviteBankResponse.

        monetary_account_id : typing.Optional[int]
            The id of the monetary account the ACCEPTED share applies to. null otherwise.

        relation_user : typing.Optional[RelationUser]
            All of the relation users towards this MA.

        share_detail : typing.Optional[ShareDetail]
            The share details.

        share_type : typing.Optional[str]
            The share type, either STANDARD or MUTUAL.

        start_date : typing.Optional[str]
            The start date of this share.

        status : typing.Optional[str]
            The status of the share. Can be ACTIVE, REVOKED, REJECTED.

        updated : typing.Optional[str]
            The timestamp of the ShareInviteBankResponse last update.

        user_alias_cancelled : typing.Optional[LabelUser]
            The user who cancelled the share if it has been revoked or rejected.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ShareInviteMonetaryAccountResponseUpdate]
            Used to view or respond to shares a user was invited to. See 'share-invite-bank-inquiry' for more information about the inquiring endpoint.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/share-invite-monetary-account-response/{encode_path_param(item_id)}",
            method="PUT",
            json={
                "access_type": access_type,
                "card_id": card_id,
                "counter_alias": convert_and_respect_annotation_metadata(
                    object_=counter_alias, annotation=LabelMonetaryAccount, direction="write"
                ),
                "created": created,
                "description": description,
                "draft_share_invite_bank_id": draft_share_invite_bank_id,
                "end_date": end_date,
                "id": id,
                "monetary_account_id": monetary_account_id,
                "relation_user": convert_and_respect_annotation_metadata(
                    object_=relation_user, annotation=RelationUser, direction="write"
                ),
                "share_detail": convert_and_respect_annotation_metadata(
                    object_=share_detail, annotation=ShareDetail, direction="write"
                ),
                "share_type": share_type,
                "start_date": start_date,
                "status": status,
                "updated": updated,
                "user_alias_cancelled": convert_and_respect_annotation_metadata(
                    object_=user_alias_cancelled, annotation=LabelUser, direction="write"
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
                    ShareInviteMonetaryAccountResponseUpdate,
                    parse_obj_as(
                        type_=ShareInviteMonetaryAccountResponseUpdate,
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

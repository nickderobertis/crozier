

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
from ..types.share_detail import ShareDetail
from ..types.share_invite_monetary_account_inquiry_create import ShareInviteMonetaryAccountInquiryCreate
from ..types.share_invite_monetary_account_inquiry_listing import ShareInviteMonetaryAccountInquiryListing
from ..types.share_invite_monetary_account_inquiry_read import ShareInviteMonetaryAccountInquiryRead
from ..types.share_invite_monetary_account_inquiry_update import ShareInviteMonetaryAccountInquiryUpdate
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawShareInviteMonetaryAccountInquiryClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_all_share_invite_monetary_account_inquiry_for_user_monetary_account(
        self, user_id: int, monetary_account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[ShareInviteMonetaryAccountInquiryListing]]:
        """
        [DEPRECATED - use /share-invite-monetary-account-response] Get a list with all the share inquiries for a monetary account, only if the requesting user has permission to change the details of the various ones.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[ShareInviteMonetaryAccountInquiryListing]]
            [DEPRECATED - use /share-invite-monetary-account-response] Used to share a monetary account with another bunq user, as in the 'Connect' feature in the bunq app. Allow the creation of share inquiries that, in the same way as request inquiries, can be revoked by the user creating them or accepted/rejected by the other party.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/share-invite-monetary-account-inquiry",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ShareInviteMonetaryAccountInquiryListing],
                    parse_obj_as(
                        type_=typing.List[ShareInviteMonetaryAccountInquiryListing],
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

    def create_share_invite_monetary_account_inquiry_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id_: int,
        *,
        access_type: typing.Optional[str] = OMIT,
        alias: typing.Optional[LabelMonetaryAccount] = OMIT,
        counter_user_alias: typing.Optional[LabelUser] = OMIT,
        draft_share_invite_bank_id: typing.Optional[int] = OMIT,
        end_date: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        monetary_account_id: typing.Optional[int] = OMIT,
        relationship: typing.Optional[str] = OMIT,
        share_detail: typing.Optional[ShareDetail] = OMIT,
        share_type: typing.Optional[str] = OMIT,
        start_date: typing.Optional[str] = OMIT,
        status: typing.Optional[str] = OMIT,
        user_alias_created: typing.Optional[LabelUser] = OMIT,
        user_alias_revoked: typing.Optional[LabelUser] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ShareInviteMonetaryAccountInquiryCreate]:
        """
        [DEPRECATED - use /share-invite-monetary-account-response] Create a new share inquiry for a monetary account, specifying the permission the other bunq user will have on it.

        Parameters
        ----------
        user_id : int


        monetary_account_id_ : int


        access_type : typing.Optional[str]
            Type of access that is in place.

        alias : typing.Optional[LabelMonetaryAccount]
            The label of the monetary account that's being shared.

        counter_user_alias : typing.Optional[LabelUser]
            The label of the user to share with.

        draft_share_invite_bank_id : typing.Optional[int]
            DEPRECATED: USE `access_type` INSTEAD | The id of the draft share invite bank.

        end_date : typing.Optional[str]
            DEPRECATED: USE `access_type` INSTEAD | The expiration date of this share.

        id : typing.Optional[int]
            The id of the newly created share invite.

        monetary_account_id : typing.Optional[int]
            The id of the monetary account the share applies to.

        relationship : typing.Optional[str]
            The relationship: COMPANY_DIRECTOR, COMPANY_EMPLOYEE, etc

        share_detail : typing.Optional[ShareDetail]
            DEPRECATED: USE `access_type` INSTEAD | The share details. Only one of these objects may be passed.

        share_type : typing.Optional[str]
            DEPRECATED: USE `access_type` INSTEAD | The share type, either STANDARD or MUTUAL.

        start_date : typing.Optional[str]
            DEPRECATED: USE `access_type` INSTEAD | The start date of this share.

        status : typing.Optional[str]
            The status of the share. Can be ACTIVE, REVOKED, REJECTED.

        user_alias_created : typing.Optional[LabelUser]
            The user who created the share.

        user_alias_revoked : typing.Optional[LabelUser]
            The user who revoked the share.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ShareInviteMonetaryAccountInquiryCreate]
            [DEPRECATED - use /share-invite-monetary-account-response] Used to share a monetary account with another bunq user, as in the 'Connect' feature in the bunq app. Allow the creation of share inquiries that, in the same way as request inquiries, can be revoked by the user creating them or accepted/rejected by the other party.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id_)}/share-invite-monetary-account-inquiry",
            method="POST",
            json={
                "access_type": access_type,
                "alias": convert_and_respect_annotation_metadata(
                    object_=alias, annotation=LabelMonetaryAccount, direction="write"
                ),
                "counter_user_alias": convert_and_respect_annotation_metadata(
                    object_=counter_user_alias, annotation=LabelUser, direction="write"
                ),
                "draft_share_invite_bank_id": draft_share_invite_bank_id,
                "end_date": end_date,
                "id": id,
                "monetary_account_id": monetary_account_id,
                "relationship": relationship,
                "share_detail": convert_and_respect_annotation_metadata(
                    object_=share_detail, annotation=ShareDetail, direction="write"
                ),
                "share_type": share_type,
                "start_date": start_date,
                "status": status,
                "user_alias_created": convert_and_respect_annotation_metadata(
                    object_=user_alias_created, annotation=LabelUser, direction="write"
                ),
                "user_alias_revoked": convert_and_respect_annotation_metadata(
                    object_=user_alias_revoked, annotation=LabelUser, direction="write"
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
                    ShareInviteMonetaryAccountInquiryCreate,
                    parse_obj_as(
                        type_=ShareInviteMonetaryAccountInquiryCreate,
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

    def read_share_invite_monetary_account_inquiry_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ShareInviteMonetaryAccountInquiryRead]:
        """
        [DEPRECATED - use /share-invite-monetary-account-response] Get the details of a specific share inquiry.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ShareInviteMonetaryAccountInquiryRead]
            [DEPRECATED - use /share-invite-monetary-account-response] Used to share a monetary account with another bunq user, as in the 'Connect' feature in the bunq app. Allow the creation of share inquiries that, in the same way as request inquiries, can be revoked by the user creating them or accepted/rejected by the other party.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/share-invite-monetary-account-inquiry/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ShareInviteMonetaryAccountInquiryRead,
                    parse_obj_as(
                        type_=ShareInviteMonetaryAccountInquiryRead,
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

    def update_share_invite_monetary_account_inquiry_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id_: int,
        item_id: int,
        *,
        access_type: typing.Optional[str] = OMIT,
        alias: typing.Optional[LabelMonetaryAccount] = OMIT,
        counter_user_alias: typing.Optional[LabelUser] = OMIT,
        draft_share_invite_bank_id: typing.Optional[int] = OMIT,
        end_date: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        monetary_account_id: typing.Optional[int] = OMIT,
        relationship: typing.Optional[str] = OMIT,
        share_detail: typing.Optional[ShareDetail] = OMIT,
        share_type: typing.Optional[str] = OMIT,
        start_date: typing.Optional[str] = OMIT,
        status: typing.Optional[str] = OMIT,
        user_alias_created: typing.Optional[LabelUser] = OMIT,
        user_alias_revoked: typing.Optional[LabelUser] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ShareInviteMonetaryAccountInquiryUpdate]:
        """
        [DEPRECATED - use /share-invite-monetary-account-response] Update the details of a share. This includes updating status (revoking or cancelling it), granted permission and validity period of this share.

        Parameters
        ----------
        user_id : int


        monetary_account_id_ : int


        item_id : int


        access_type : typing.Optional[str]
            Type of access that is in place.

        alias : typing.Optional[LabelMonetaryAccount]
            The label of the monetary account that's being shared.

        counter_user_alias : typing.Optional[LabelUser]
            The label of the user to share with.

        draft_share_invite_bank_id : typing.Optional[int]
            DEPRECATED: USE `access_type` INSTEAD | The id of the draft share invite bank.

        end_date : typing.Optional[str]
            DEPRECATED: USE `access_type` INSTEAD | The expiration date of this share.

        id : typing.Optional[int]
            The id of the newly created share invite.

        monetary_account_id : typing.Optional[int]
            The id of the monetary account the share applies to.

        relationship : typing.Optional[str]
            The relationship: COMPANY_DIRECTOR, COMPANY_EMPLOYEE, etc

        share_detail : typing.Optional[ShareDetail]
            DEPRECATED: USE `access_type` INSTEAD | The share details. Only one of these objects may be passed.

        share_type : typing.Optional[str]
            DEPRECATED: USE `access_type` INSTEAD | The share type, either STANDARD or MUTUAL.

        start_date : typing.Optional[str]
            DEPRECATED: USE `access_type` INSTEAD | The start date of this share.

        status : typing.Optional[str]
            The status of the share. Can be ACTIVE, REVOKED, REJECTED.

        user_alias_created : typing.Optional[LabelUser]
            The user who created the share.

        user_alias_revoked : typing.Optional[LabelUser]
            The user who revoked the share.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ShareInviteMonetaryAccountInquiryUpdate]
            [DEPRECATED - use /share-invite-monetary-account-response] Used to share a monetary account with another bunq user, as in the 'Connect' feature in the bunq app. Allow the creation of share inquiries that, in the same way as request inquiries, can be revoked by the user creating them or accepted/rejected by the other party.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id_)}/share-invite-monetary-account-inquiry/{encode_path_param(item_id)}",
            method="PUT",
            json={
                "access_type": access_type,
                "alias": convert_and_respect_annotation_metadata(
                    object_=alias, annotation=LabelMonetaryAccount, direction="write"
                ),
                "counter_user_alias": convert_and_respect_annotation_metadata(
                    object_=counter_user_alias, annotation=LabelUser, direction="write"
                ),
                "draft_share_invite_bank_id": draft_share_invite_bank_id,
                "end_date": end_date,
                "id": id,
                "monetary_account_id": monetary_account_id,
                "relationship": relationship,
                "share_detail": convert_and_respect_annotation_metadata(
                    object_=share_detail, annotation=ShareDetail, direction="write"
                ),
                "share_type": share_type,
                "start_date": start_date,
                "status": status,
                "user_alias_created": convert_and_respect_annotation_metadata(
                    object_=user_alias_created, annotation=LabelUser, direction="write"
                ),
                "user_alias_revoked": convert_and_respect_annotation_metadata(
                    object_=user_alias_revoked, annotation=LabelUser, direction="write"
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
                    ShareInviteMonetaryAccountInquiryUpdate,
                    parse_obj_as(
                        type_=ShareInviteMonetaryAccountInquiryUpdate,
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


class AsyncRawShareInviteMonetaryAccountInquiryClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_all_share_invite_monetary_account_inquiry_for_user_monetary_account(
        self, user_id: int, monetary_account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[ShareInviteMonetaryAccountInquiryListing]]:
        """
        [DEPRECATED - use /share-invite-monetary-account-response] Get a list with all the share inquiries for a monetary account, only if the requesting user has permission to change the details of the various ones.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[ShareInviteMonetaryAccountInquiryListing]]
            [DEPRECATED - use /share-invite-monetary-account-response] Used to share a monetary account with another bunq user, as in the 'Connect' feature in the bunq app. Allow the creation of share inquiries that, in the same way as request inquiries, can be revoked by the user creating them or accepted/rejected by the other party.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/share-invite-monetary-account-inquiry",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ShareInviteMonetaryAccountInquiryListing],
                    parse_obj_as(
                        type_=typing.List[ShareInviteMonetaryAccountInquiryListing],
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

    async def create_share_invite_monetary_account_inquiry_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id_: int,
        *,
        access_type: typing.Optional[str] = OMIT,
        alias: typing.Optional[LabelMonetaryAccount] = OMIT,
        counter_user_alias: typing.Optional[LabelUser] = OMIT,
        draft_share_invite_bank_id: typing.Optional[int] = OMIT,
        end_date: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        monetary_account_id: typing.Optional[int] = OMIT,
        relationship: typing.Optional[str] = OMIT,
        share_detail: typing.Optional[ShareDetail] = OMIT,
        share_type: typing.Optional[str] = OMIT,
        start_date: typing.Optional[str] = OMIT,
        status: typing.Optional[str] = OMIT,
        user_alias_created: typing.Optional[LabelUser] = OMIT,
        user_alias_revoked: typing.Optional[LabelUser] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ShareInviteMonetaryAccountInquiryCreate]:
        """
        [DEPRECATED - use /share-invite-monetary-account-response] Create a new share inquiry for a monetary account, specifying the permission the other bunq user will have on it.

        Parameters
        ----------
        user_id : int


        monetary_account_id_ : int


        access_type : typing.Optional[str]
            Type of access that is in place.

        alias : typing.Optional[LabelMonetaryAccount]
            The label of the monetary account that's being shared.

        counter_user_alias : typing.Optional[LabelUser]
            The label of the user to share with.

        draft_share_invite_bank_id : typing.Optional[int]
            DEPRECATED: USE `access_type` INSTEAD | The id of the draft share invite bank.

        end_date : typing.Optional[str]
            DEPRECATED: USE `access_type` INSTEAD | The expiration date of this share.

        id : typing.Optional[int]
            The id of the newly created share invite.

        monetary_account_id : typing.Optional[int]
            The id of the monetary account the share applies to.

        relationship : typing.Optional[str]
            The relationship: COMPANY_DIRECTOR, COMPANY_EMPLOYEE, etc

        share_detail : typing.Optional[ShareDetail]
            DEPRECATED: USE `access_type` INSTEAD | The share details. Only one of these objects may be passed.

        share_type : typing.Optional[str]
            DEPRECATED: USE `access_type` INSTEAD | The share type, either STANDARD or MUTUAL.

        start_date : typing.Optional[str]
            DEPRECATED: USE `access_type` INSTEAD | The start date of this share.

        status : typing.Optional[str]
            The status of the share. Can be ACTIVE, REVOKED, REJECTED.

        user_alias_created : typing.Optional[LabelUser]
            The user who created the share.

        user_alias_revoked : typing.Optional[LabelUser]
            The user who revoked the share.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ShareInviteMonetaryAccountInquiryCreate]
            [DEPRECATED - use /share-invite-monetary-account-response] Used to share a monetary account with another bunq user, as in the 'Connect' feature in the bunq app. Allow the creation of share inquiries that, in the same way as request inquiries, can be revoked by the user creating them or accepted/rejected by the other party.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id_)}/share-invite-monetary-account-inquiry",
            method="POST",
            json={
                "access_type": access_type,
                "alias": convert_and_respect_annotation_metadata(
                    object_=alias, annotation=LabelMonetaryAccount, direction="write"
                ),
                "counter_user_alias": convert_and_respect_annotation_metadata(
                    object_=counter_user_alias, annotation=LabelUser, direction="write"
                ),
                "draft_share_invite_bank_id": draft_share_invite_bank_id,
                "end_date": end_date,
                "id": id,
                "monetary_account_id": monetary_account_id,
                "relationship": relationship,
                "share_detail": convert_and_respect_annotation_metadata(
                    object_=share_detail, annotation=ShareDetail, direction="write"
                ),
                "share_type": share_type,
                "start_date": start_date,
                "status": status,
                "user_alias_created": convert_and_respect_annotation_metadata(
                    object_=user_alias_created, annotation=LabelUser, direction="write"
                ),
                "user_alias_revoked": convert_and_respect_annotation_metadata(
                    object_=user_alias_revoked, annotation=LabelUser, direction="write"
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
                    ShareInviteMonetaryAccountInquiryCreate,
                    parse_obj_as(
                        type_=ShareInviteMonetaryAccountInquiryCreate,
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

    async def read_share_invite_monetary_account_inquiry_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ShareInviteMonetaryAccountInquiryRead]:
        """
        [DEPRECATED - use /share-invite-monetary-account-response] Get the details of a specific share inquiry.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ShareInviteMonetaryAccountInquiryRead]
            [DEPRECATED - use /share-invite-monetary-account-response] Used to share a monetary account with another bunq user, as in the 'Connect' feature in the bunq app. Allow the creation of share inquiries that, in the same way as request inquiries, can be revoked by the user creating them or accepted/rejected by the other party.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/share-invite-monetary-account-inquiry/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ShareInviteMonetaryAccountInquiryRead,
                    parse_obj_as(
                        type_=ShareInviteMonetaryAccountInquiryRead,
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

    async def update_share_invite_monetary_account_inquiry_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id_: int,
        item_id: int,
        *,
        access_type: typing.Optional[str] = OMIT,
        alias: typing.Optional[LabelMonetaryAccount] = OMIT,
        counter_user_alias: typing.Optional[LabelUser] = OMIT,
        draft_share_invite_bank_id: typing.Optional[int] = OMIT,
        end_date: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        monetary_account_id: typing.Optional[int] = OMIT,
        relationship: typing.Optional[str] = OMIT,
        share_detail: typing.Optional[ShareDetail] = OMIT,
        share_type: typing.Optional[str] = OMIT,
        start_date: typing.Optional[str] = OMIT,
        status: typing.Optional[str] = OMIT,
        user_alias_created: typing.Optional[LabelUser] = OMIT,
        user_alias_revoked: typing.Optional[LabelUser] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ShareInviteMonetaryAccountInquiryUpdate]:
        """
        [DEPRECATED - use /share-invite-monetary-account-response] Update the details of a share. This includes updating status (revoking or cancelling it), granted permission and validity period of this share.

        Parameters
        ----------
        user_id : int


        monetary_account_id_ : int


        item_id : int


        access_type : typing.Optional[str]
            Type of access that is in place.

        alias : typing.Optional[LabelMonetaryAccount]
            The label of the monetary account that's being shared.

        counter_user_alias : typing.Optional[LabelUser]
            The label of the user to share with.

        draft_share_invite_bank_id : typing.Optional[int]
            DEPRECATED: USE `access_type` INSTEAD | The id of the draft share invite bank.

        end_date : typing.Optional[str]
            DEPRECATED: USE `access_type` INSTEAD | The expiration date of this share.

        id : typing.Optional[int]
            The id of the newly created share invite.

        monetary_account_id : typing.Optional[int]
            The id of the monetary account the share applies to.

        relationship : typing.Optional[str]
            The relationship: COMPANY_DIRECTOR, COMPANY_EMPLOYEE, etc

        share_detail : typing.Optional[ShareDetail]
            DEPRECATED: USE `access_type` INSTEAD | The share details. Only one of these objects may be passed.

        share_type : typing.Optional[str]
            DEPRECATED: USE `access_type` INSTEAD | The share type, either STANDARD or MUTUAL.

        start_date : typing.Optional[str]
            DEPRECATED: USE `access_type` INSTEAD | The start date of this share.

        status : typing.Optional[str]
            The status of the share. Can be ACTIVE, REVOKED, REJECTED.

        user_alias_created : typing.Optional[LabelUser]
            The user who created the share.

        user_alias_revoked : typing.Optional[LabelUser]
            The user who revoked the share.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ShareInviteMonetaryAccountInquiryUpdate]
            [DEPRECATED - use /share-invite-monetary-account-response] Used to share a monetary account with another bunq user, as in the 'Connect' feature in the bunq app. Allow the creation of share inquiries that, in the same way as request inquiries, can be revoked by the user creating them or accepted/rejected by the other party.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id_)}/share-invite-monetary-account-inquiry/{encode_path_param(item_id)}",
            method="PUT",
            json={
                "access_type": access_type,
                "alias": convert_and_respect_annotation_metadata(
                    object_=alias, annotation=LabelMonetaryAccount, direction="write"
                ),
                "counter_user_alias": convert_and_respect_annotation_metadata(
                    object_=counter_user_alias, annotation=LabelUser, direction="write"
                ),
                "draft_share_invite_bank_id": draft_share_invite_bank_id,
                "end_date": end_date,
                "id": id,
                "monetary_account_id": monetary_account_id,
                "relationship": relationship,
                "share_detail": convert_and_respect_annotation_metadata(
                    object_=share_detail, annotation=ShareDetail, direction="write"
                ),
                "share_type": share_type,
                "start_date": start_date,
                "status": status,
                "user_alias_created": convert_and_respect_annotation_metadata(
                    object_=user_alias_created, annotation=LabelUser, direction="write"
                ),
                "user_alias_revoked": convert_and_respect_annotation_metadata(
                    object_=user_alias_revoked, annotation=LabelUser, direction="write"
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
                    ShareInviteMonetaryAccountInquiryUpdate,
                    parse_obj_as(
                        type_=ShareInviteMonetaryAccountInquiryUpdate,
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

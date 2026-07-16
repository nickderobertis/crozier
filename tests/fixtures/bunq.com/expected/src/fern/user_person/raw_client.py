

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
from ..types.address import Address
from ..types.amount import Amount
from ..types.avatar import Avatar
from ..types.notification_filter import NotificationFilter
from ..types.pointer import Pointer
from ..types.relation_user import RelationUser
from ..types.tax_resident import TaxResident
from ..types.user_person_read import UserPersonRead
from ..types.user_person_update import UserPersonUpdate
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawUserPersonClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def read_user_person(
        self, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UserPersonRead]:
        """
        Get a specific person.

        Parameters
        ----------
        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UserPersonRead]
            With UserPerson you can retrieve information regarding the authenticated UserPerson and update specific fields.<br/><br/>Notification filters can be set on a UserPerson level to receive callbacks. For more information check the <a href="/api/1/page/callbacks">dedicated callbacks page</a>.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user-person/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserPersonRead,
                    parse_obj_as(
                        type_=UserPersonRead,
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

    def update_user_person(
        self,
        item_id: int,
        *,
        address_main: typing.Optional[Address] = OMIT,
        address_postal: typing.Optional[Address] = OMIT,
        alias: typing.Optional[typing.Sequence[Pointer]] = OMIT,
        avatar: typing.Optional[Avatar] = OMIT,
        avatar_uuid: typing.Optional[str] = OMIT,
        country_of_birth: typing.Optional[str] = OMIT,
        created: typing.Optional[str] = OMIT,
        daily_limit_without_confirmation_login: typing.Optional[Amount] = OMIT,
        date_of_birth: typing.Optional[str] = OMIT,
        display_name: typing.Optional[str] = OMIT,
        document_back_attachment_id: typing.Optional[int] = OMIT,
        document_country_of_issuance: typing.Optional[str] = OMIT,
        document_front_attachment_id: typing.Optional[int] = OMIT,
        document_number: typing.Optional[str] = OMIT,
        document_type: typing.Optional[str] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        gender: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        language: typing.Optional[str] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        legal_guardian_alias: typing.Optional[Pointer] = OMIT,
        legal_name: typing.Optional[str] = OMIT,
        middle_name: typing.Optional[str] = OMIT,
        nationality: typing.Optional[str] = OMIT,
        notification_filters: typing.Optional[typing.Sequence[NotificationFilter]] = OMIT,
        place_of_birth: typing.Optional[str] = OMIT,
        public_nick_name: typing.Optional[str] = OMIT,
        public_uuid: typing.Optional[str] = OMIT,
        region: typing.Optional[str] = OMIT,
        relations: typing.Optional[typing.Sequence[RelationUser]] = OMIT,
        session_timeout: typing.Optional[int] = OMIT,
        signup_track_type: typing.Optional[str] = OMIT,
        status: typing.Optional[str] = OMIT,
        sub_status: typing.Optional[str] = OMIT,
        subscription_type: typing.Optional[str] = OMIT,
        tax_resident: typing.Optional[typing.Sequence[TaxResident]] = OMIT,
        updated: typing.Optional[str] = OMIT,
        version_terms_of_service: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UserPersonUpdate]:
        """
        Modify a specific person object's data.

        Parameters
        ----------
        item_id : int


        address_main : typing.Optional[Address]
            The person's main address.

        address_postal : typing.Optional[Address]
            The person's postal address.

        alias : typing.Optional[typing.Sequence[Pointer]]
            The aliases of the user.

        avatar : typing.Optional[Avatar]
            The user's avatar.

        avatar_uuid : typing.Optional[str]
            The public UUID of the user's avatar.

        country_of_birth : typing.Optional[str]
            The person's country of birth. Formatted as a SO 3166-1 alpha-2 country code.

        created : typing.Optional[str]
            The timestamp of the person object's creation.

        daily_limit_without_confirmation_login : typing.Optional[Amount]
            The amount the user can pay in the session without asking for credentials.

        date_of_birth : typing.Optional[str]
            The person's date of birth. Accepts ISO8601 date formats.

        display_name : typing.Optional[str]
            The display name for the person.

        document_back_attachment_id : typing.Optional[int]
            The reference to the uploaded picture/scan of the back side of the identification document.

        document_country_of_issuance : typing.Optional[str]
            The country which issued the identification document the person registered with.

        document_front_attachment_id : typing.Optional[int]
            The reference to the uploaded picture/scan of the front side of the identification document.

        document_number : typing.Optional[str]
            The identification document number the person registered with.

        document_type : typing.Optional[str]
            The type of identification document the person registered with.

        first_name : typing.Optional[str]
            The person's first name.

        gender : typing.Optional[str]
            The person's gender. Can be MALE, FEMALE or UNKNOWN.

        id : typing.Optional[int]
            The id of the modified person object.

        language : typing.Optional[str]
            The person's preferred language. Formatted as a ISO 639-1 language code plus a ISO 3166-1 alpha-2 country code, seperated by an underscore.

        last_name : typing.Optional[str]
            The person's last name.

        legal_guardian_alias : typing.Optional[Pointer]
            The legal guardian of the user. Required for minors.

        legal_name : typing.Optional[str]
            The person's legal name.

        middle_name : typing.Optional[str]
            The person's middle name.

        nationality : typing.Optional[str]
            The person's nationality. Formatted as a SO 3166-1 alpha-2 country code.

        notification_filters : typing.Optional[typing.Sequence[NotificationFilter]]
            The types of notifications that will result in a push notification or URL callback for this UserPerson.

        place_of_birth : typing.Optional[str]
            The person's place of birth.

        public_nick_name : typing.Optional[str]
            The public nick name for the person.

        public_uuid : typing.Optional[str]
            The person's public UUID.

        region : typing.Optional[str]
            The person's preferred region. Formatted as a ISO 639-1 language code plus a ISO 3166-1 alpha-2 country code, seperated by an underscore.

        relations : typing.Optional[typing.Sequence[RelationUser]]
            The relations for this user.

        session_timeout : typing.Optional[int]
            The setting for the session timeout of the user in seconds.

        signup_track_type : typing.Optional[str]
            The type of signup track the user is following.

        status : typing.Optional[str]
            The user status. The user status. Can be: ACTIVE, BLOCKED, SIGNUP, RECOVERY, DENIED or ABORTED.

        sub_status : typing.Optional[str]
            The user sub-status. Can be: NONE, FACE_RESET, APPROVAL, APPROVAL_DIRECTOR, APPROVAL_PARENT, APPROVAL_SUPPORT, COUNTER_IBAN, IDEAL or SUBMIT.

        subscription_type : typing.Optional[str]
            The subscription type the user should start on.

        tax_resident : typing.Optional[typing.Sequence[TaxResident]]
            The user's tax residence numbers for different countries.

        updated : typing.Optional[str]
            The timestamp of the person object's last update.

        version_terms_of_service : typing.Optional[str]
            The version of the terms of service accepted by the user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UserPersonUpdate]
            With UserPerson you can retrieve information regarding the authenticated UserPerson and update specific fields.<br/><br/>Notification filters can be set on a UserPerson level to receive callbacks. For more information check the <a href="/api/1/page/callbacks">dedicated callbacks page</a>.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user-person/{encode_path_param(item_id)}",
            method="PUT",
            json={
                "address_main": convert_and_respect_annotation_metadata(
                    object_=address_main, annotation=Address, direction="write"
                ),
                "address_postal": convert_and_respect_annotation_metadata(
                    object_=address_postal, annotation=Address, direction="write"
                ),
                "alias": convert_and_respect_annotation_metadata(
                    object_=alias, annotation=typing.Sequence[Pointer], direction="write"
                ),
                "avatar": convert_and_respect_annotation_metadata(object_=avatar, annotation=Avatar, direction="write"),
                "avatar_uuid": avatar_uuid,
                "country_of_birth": country_of_birth,
                "created": created,
                "daily_limit_without_confirmation_login": convert_and_respect_annotation_metadata(
                    object_=daily_limit_without_confirmation_login, annotation=Amount, direction="write"
                ),
                "date_of_birth": date_of_birth,
                "display_name": display_name,
                "document_back_attachment_id": document_back_attachment_id,
                "document_country_of_issuance": document_country_of_issuance,
                "document_front_attachment_id": document_front_attachment_id,
                "document_number": document_number,
                "document_type": document_type,
                "first_name": first_name,
                "gender": gender,
                "id": id,
                "language": language,
                "last_name": last_name,
                "legal_guardian_alias": convert_and_respect_annotation_metadata(
                    object_=legal_guardian_alias, annotation=Pointer, direction="write"
                ),
                "legal_name": legal_name,
                "middle_name": middle_name,
                "nationality": nationality,
                "notification_filters": convert_and_respect_annotation_metadata(
                    object_=notification_filters, annotation=typing.Sequence[NotificationFilter], direction="write"
                ),
                "place_of_birth": place_of_birth,
                "public_nick_name": public_nick_name,
                "public_uuid": public_uuid,
                "region": region,
                "relations": convert_and_respect_annotation_metadata(
                    object_=relations, annotation=typing.Sequence[RelationUser], direction="write"
                ),
                "session_timeout": session_timeout,
                "signup_track_type": signup_track_type,
                "status": status,
                "sub_status": sub_status,
                "subscription_type": subscription_type,
                "tax_resident": convert_and_respect_annotation_metadata(
                    object_=tax_resident, annotation=typing.Sequence[TaxResident], direction="write"
                ),
                "updated": updated,
                "version_terms_of_service": version_terms_of_service,
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
                    UserPersonUpdate,
                    parse_obj_as(
                        type_=UserPersonUpdate,
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


class AsyncRawUserPersonClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def read_user_person(
        self, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UserPersonRead]:
        """
        Get a specific person.

        Parameters
        ----------
        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UserPersonRead]
            With UserPerson you can retrieve information regarding the authenticated UserPerson and update specific fields.<br/><br/>Notification filters can be set on a UserPerson level to receive callbacks. For more information check the <a href="/api/1/page/callbacks">dedicated callbacks page</a>.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user-person/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserPersonRead,
                    parse_obj_as(
                        type_=UserPersonRead,
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

    async def update_user_person(
        self,
        item_id: int,
        *,
        address_main: typing.Optional[Address] = OMIT,
        address_postal: typing.Optional[Address] = OMIT,
        alias: typing.Optional[typing.Sequence[Pointer]] = OMIT,
        avatar: typing.Optional[Avatar] = OMIT,
        avatar_uuid: typing.Optional[str] = OMIT,
        country_of_birth: typing.Optional[str] = OMIT,
        created: typing.Optional[str] = OMIT,
        daily_limit_without_confirmation_login: typing.Optional[Amount] = OMIT,
        date_of_birth: typing.Optional[str] = OMIT,
        display_name: typing.Optional[str] = OMIT,
        document_back_attachment_id: typing.Optional[int] = OMIT,
        document_country_of_issuance: typing.Optional[str] = OMIT,
        document_front_attachment_id: typing.Optional[int] = OMIT,
        document_number: typing.Optional[str] = OMIT,
        document_type: typing.Optional[str] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        gender: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        language: typing.Optional[str] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        legal_guardian_alias: typing.Optional[Pointer] = OMIT,
        legal_name: typing.Optional[str] = OMIT,
        middle_name: typing.Optional[str] = OMIT,
        nationality: typing.Optional[str] = OMIT,
        notification_filters: typing.Optional[typing.Sequence[NotificationFilter]] = OMIT,
        place_of_birth: typing.Optional[str] = OMIT,
        public_nick_name: typing.Optional[str] = OMIT,
        public_uuid: typing.Optional[str] = OMIT,
        region: typing.Optional[str] = OMIT,
        relations: typing.Optional[typing.Sequence[RelationUser]] = OMIT,
        session_timeout: typing.Optional[int] = OMIT,
        signup_track_type: typing.Optional[str] = OMIT,
        status: typing.Optional[str] = OMIT,
        sub_status: typing.Optional[str] = OMIT,
        subscription_type: typing.Optional[str] = OMIT,
        tax_resident: typing.Optional[typing.Sequence[TaxResident]] = OMIT,
        updated: typing.Optional[str] = OMIT,
        version_terms_of_service: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UserPersonUpdate]:
        """
        Modify a specific person object's data.

        Parameters
        ----------
        item_id : int


        address_main : typing.Optional[Address]
            The person's main address.

        address_postal : typing.Optional[Address]
            The person's postal address.

        alias : typing.Optional[typing.Sequence[Pointer]]
            The aliases of the user.

        avatar : typing.Optional[Avatar]
            The user's avatar.

        avatar_uuid : typing.Optional[str]
            The public UUID of the user's avatar.

        country_of_birth : typing.Optional[str]
            The person's country of birth. Formatted as a SO 3166-1 alpha-2 country code.

        created : typing.Optional[str]
            The timestamp of the person object's creation.

        daily_limit_without_confirmation_login : typing.Optional[Amount]
            The amount the user can pay in the session without asking for credentials.

        date_of_birth : typing.Optional[str]
            The person's date of birth. Accepts ISO8601 date formats.

        display_name : typing.Optional[str]
            The display name for the person.

        document_back_attachment_id : typing.Optional[int]
            The reference to the uploaded picture/scan of the back side of the identification document.

        document_country_of_issuance : typing.Optional[str]
            The country which issued the identification document the person registered with.

        document_front_attachment_id : typing.Optional[int]
            The reference to the uploaded picture/scan of the front side of the identification document.

        document_number : typing.Optional[str]
            The identification document number the person registered with.

        document_type : typing.Optional[str]
            The type of identification document the person registered with.

        first_name : typing.Optional[str]
            The person's first name.

        gender : typing.Optional[str]
            The person's gender. Can be MALE, FEMALE or UNKNOWN.

        id : typing.Optional[int]
            The id of the modified person object.

        language : typing.Optional[str]
            The person's preferred language. Formatted as a ISO 639-1 language code plus a ISO 3166-1 alpha-2 country code, seperated by an underscore.

        last_name : typing.Optional[str]
            The person's last name.

        legal_guardian_alias : typing.Optional[Pointer]
            The legal guardian of the user. Required for minors.

        legal_name : typing.Optional[str]
            The person's legal name.

        middle_name : typing.Optional[str]
            The person's middle name.

        nationality : typing.Optional[str]
            The person's nationality. Formatted as a SO 3166-1 alpha-2 country code.

        notification_filters : typing.Optional[typing.Sequence[NotificationFilter]]
            The types of notifications that will result in a push notification or URL callback for this UserPerson.

        place_of_birth : typing.Optional[str]
            The person's place of birth.

        public_nick_name : typing.Optional[str]
            The public nick name for the person.

        public_uuid : typing.Optional[str]
            The person's public UUID.

        region : typing.Optional[str]
            The person's preferred region. Formatted as a ISO 639-1 language code plus a ISO 3166-1 alpha-2 country code, seperated by an underscore.

        relations : typing.Optional[typing.Sequence[RelationUser]]
            The relations for this user.

        session_timeout : typing.Optional[int]
            The setting for the session timeout of the user in seconds.

        signup_track_type : typing.Optional[str]
            The type of signup track the user is following.

        status : typing.Optional[str]
            The user status. The user status. Can be: ACTIVE, BLOCKED, SIGNUP, RECOVERY, DENIED or ABORTED.

        sub_status : typing.Optional[str]
            The user sub-status. Can be: NONE, FACE_RESET, APPROVAL, APPROVAL_DIRECTOR, APPROVAL_PARENT, APPROVAL_SUPPORT, COUNTER_IBAN, IDEAL or SUBMIT.

        subscription_type : typing.Optional[str]
            The subscription type the user should start on.

        tax_resident : typing.Optional[typing.Sequence[TaxResident]]
            The user's tax residence numbers for different countries.

        updated : typing.Optional[str]
            The timestamp of the person object's last update.

        version_terms_of_service : typing.Optional[str]
            The version of the terms of service accepted by the user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UserPersonUpdate]
            With UserPerson you can retrieve information regarding the authenticated UserPerson and update specific fields.<br/><br/>Notification filters can be set on a UserPerson level to receive callbacks. For more information check the <a href="/api/1/page/callbacks">dedicated callbacks page</a>.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user-person/{encode_path_param(item_id)}",
            method="PUT",
            json={
                "address_main": convert_and_respect_annotation_metadata(
                    object_=address_main, annotation=Address, direction="write"
                ),
                "address_postal": convert_and_respect_annotation_metadata(
                    object_=address_postal, annotation=Address, direction="write"
                ),
                "alias": convert_and_respect_annotation_metadata(
                    object_=alias, annotation=typing.Sequence[Pointer], direction="write"
                ),
                "avatar": convert_and_respect_annotation_metadata(object_=avatar, annotation=Avatar, direction="write"),
                "avatar_uuid": avatar_uuid,
                "country_of_birth": country_of_birth,
                "created": created,
                "daily_limit_without_confirmation_login": convert_and_respect_annotation_metadata(
                    object_=daily_limit_without_confirmation_login, annotation=Amount, direction="write"
                ),
                "date_of_birth": date_of_birth,
                "display_name": display_name,
                "document_back_attachment_id": document_back_attachment_id,
                "document_country_of_issuance": document_country_of_issuance,
                "document_front_attachment_id": document_front_attachment_id,
                "document_number": document_number,
                "document_type": document_type,
                "first_name": first_name,
                "gender": gender,
                "id": id,
                "language": language,
                "last_name": last_name,
                "legal_guardian_alias": convert_and_respect_annotation_metadata(
                    object_=legal_guardian_alias, annotation=Pointer, direction="write"
                ),
                "legal_name": legal_name,
                "middle_name": middle_name,
                "nationality": nationality,
                "notification_filters": convert_and_respect_annotation_metadata(
                    object_=notification_filters, annotation=typing.Sequence[NotificationFilter], direction="write"
                ),
                "place_of_birth": place_of_birth,
                "public_nick_name": public_nick_name,
                "public_uuid": public_uuid,
                "region": region,
                "relations": convert_and_respect_annotation_metadata(
                    object_=relations, annotation=typing.Sequence[RelationUser], direction="write"
                ),
                "session_timeout": session_timeout,
                "signup_track_type": signup_track_type,
                "status": status,
                "sub_status": sub_status,
                "subscription_type": subscription_type,
                "tax_resident": convert_and_respect_annotation_metadata(
                    object_=tax_resident, annotation=typing.Sequence[TaxResident], direction="write"
                ),
                "updated": updated,
                "version_terms_of_service": version_terms_of_service,
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
                    UserPersonUpdate,
                    parse_obj_as(
                        type_=UserPersonUpdate,
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

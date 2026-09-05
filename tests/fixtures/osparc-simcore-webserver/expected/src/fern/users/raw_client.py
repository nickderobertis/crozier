

import datetime as dt
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
from ..errors.conflict_error import ConflictError
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_found_error import NotFoundError
from ..errors.service_unavailable_error import ServiceUnavailableError
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.address_line_safe_str import AddressLineSafeStr
from ..types.country_name_str import CountryNameStr
from ..types.display_safe_str import DisplaySafeStr
from ..types.envelope_list_my_permission_get import EnvelopeListMyPermissionGet
from ..types.envelope_list_my_token_get import EnvelopeListMyTokenGet
from ..types.envelope_list_user_account_get import EnvelopeListUserAccountGet
from ..types.envelope_list_user_account_product_option_get import EnvelopeListUserAccountProductOptionGet
from ..types.envelope_list_user_get import EnvelopeListUserGet
from ..types.envelope_list_user_notification import EnvelopeListUserNotification
from ..types.envelope_my_function_permissions_get import EnvelopeMyFunctionPermissionsGet
from ..types.envelope_my_profile_rest_get import EnvelopeMyProfileRestGet
from ..types.envelope_my_token_get import EnvelopeMyTokenGet
from ..types.envelope_user_account_get import EnvelopeUserAccountGet
from ..types.envelope_user_account_preview_approval_get import EnvelopeUserAccountPreviewApprovalGet
from ..types.envelope_user_account_preview_rejection_get import EnvelopeUserAccountPreviewRejectionGet
from ..types.first_name_str import FirstNameStr
from ..types.glob_pattern_safe_str import GlobPatternSafeStr
from ..types.group_id_int import GroupIdInt
from ..types.invitation_details import InvitationDetails
from ..types.last_name_str import LastNameStr
from ..types.lower_case_email_str import LowerCaseEmailStr
from ..types.message_content import MessageContent
from ..types.my_profile_address_rest_patch import MyProfileAddressRestPatch
from ..types.my_profile_privacy_patch import MyProfilePrivacyPatch
from ..types.notification_category import NotificationCategory
from ..types.page_user_account_get import PageUserAccountGet
from ..types.phone_number_str import PhoneNumberStr
from ..types.postal_code_safe_str import PostalCodeSafeStr
from ..types.search_pattern_safe_str import SearchPatternSafeStr
from ..types.supported_locale import SupportedLocale
from ..types.user_id_int import UserIdInt
from ..types.user_name_safe_id import UserNameSafeId
from .types.list_users_accounts_request_review_status import ListUsersAccountsRequestReviewStatus
from .types.user_notification_create_product import UserNotificationCreateProduct
from .types.user_notification_create_resource_id import UserNotificationCreateResourceId
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawUsersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_my_profile(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeMyProfileRestGet]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeMyProfileRestGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/me",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeMyProfileRestGet,
                    parse_obj_as(
                        type_=EnvelopeMyProfileRestGet,
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

    def update_my_profile(
        self,
        *,
        first_name: typing.Optional[FirstNameStr] = OMIT,
        last_name: typing.Optional[LastNameStr] = OMIT,
        user_name: typing.Optional[UserNameSafeId] = OMIT,
        language: typing.Optional[SupportedLocale] = OMIT,
        privacy: typing.Optional[MyProfilePrivacyPatch] = OMIT,
        contact: typing.Optional[MyProfileAddressRestPatch] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        first_name : typing.Optional[FirstNameStr]

        last_name : typing.Optional[LastNameStr]

        user_name : typing.Optional[UserNameSafeId]

        language : typing.Optional[SupportedLocale]
            Persisted UI/communications language. The user owns and can edit it directly.

        privacy : typing.Optional[MyProfilePrivacyPatch]

        contact : typing.Optional[MyProfileAddressRestPatch]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/me",
            method="PATCH",
            json={
                "first_name": first_name,
                "last_name": last_name,
                "userName": user_name,
                "language": language,
                "privacy": convert_and_respect_annotation_metadata(
                    object_=privacy, annotation=typing.Optional[MyProfilePrivacyPatch], direction="write"
                ),
                "contact": convert_and_respect_annotation_metadata(
                    object_=contact, annotation=typing.Optional[MyProfileAddressRestPatch], direction="write"
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
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def my_phone_register(
        self, *, phone: PhoneNumberStr, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Any]:
        """
        Starts the phone registration process

        Parameters
        ----------
        phone : PhoneNumberStr
            Phone number to register

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Phone registration initiated
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/me/phone:register",
            method="POST",
            json={
                "phone": phone,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    def my_phone_resend(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[typing.Any]:
        """
        Resends the phone registration code

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Phone code resent
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/me/phone:resend",
            method="POST",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
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

    def my_phone_confirm(
        self, *, code: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Confirms the phone registration

        Parameters
        ----------
        code : str
            Alphanumeric confirmation code

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/me/phone:confirm",
            method="POST",
            json={
                "code": code,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    def set_frontend_preference(
        self, preference_id: str, *, value: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        preference_id : str

        value : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/me/preferences/{encode_path_param(preference_id)}",
            method="PATCH",
            json={
                "value": value,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_tokens(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeListMyTokenGet]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeListMyTokenGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/me/tokens",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeListMyTokenGet,
                    parse_obj_as(
                        type_=EnvelopeListMyTokenGet,
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

    def create_token(
        self,
        *,
        service: str,
        token_key: str,
        token_secret: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvelopeMyTokenGet]:
        """
        Parameters
        ----------
        service : str
            uniquely identifies the service where this token is used

        token_key : str

        token_secret : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeMyTokenGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/me/tokens",
            method="POST",
            json={
                "service": service,
                "token_key": token_key,
                "token_secret": token_secret,
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
                    EnvelopeMyTokenGet,
                    parse_obj_as(
                        type_=EnvelopeMyTokenGet,
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

    def get_token(
        self, service: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeMyTokenGet]:
        """
        Parameters
        ----------
        service : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeMyTokenGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/me/tokens/{encode_path_param(service)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeMyTokenGet,
                    parse_obj_as(
                        type_=EnvelopeMyTokenGet,
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

    def delete_token(
        self, service: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        service : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/me/tokens/{encode_path_param(service)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_user_notifications(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeListUserNotification]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeListUserNotification]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/me/notifications",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeListUserNotification,
                    parse_obj_as(
                        type_=EnvelopeListUserNotification,
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

    def create_user_notification(
        self,
        *,
        user_id: UserIdInt,
        category: NotificationCategory,
        actionable_path: str,
        title: str,
        text: str,
        date: dt.datetime,
        product: typing.Optional[UserNotificationCreateProduct] = OMIT,
        resource_id: typing.Optional[UserNotificationCreateResourceId] = OMIT,
        user_from_id: typing.Optional[UserIdInt] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        user_id : UserIdInt

        category : NotificationCategory

        actionable_path : str

        title : str

        text : str

        date : dt.datetime

        product : typing.Optional[UserNotificationCreateProduct]

        resource_id : typing.Optional[UserNotificationCreateResourceId]

        user_from_id : typing.Optional[UserIdInt]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/me/notifications",
            method="POST",
            json={
                "user_id": user_id,
                "category": category,
                "actionable_path": actionable_path,
                "title": title,
                "text": text,
                "date": date,
                "product": convert_and_respect_annotation_metadata(
                    object_=product, annotation=UserNotificationCreateProduct, direction="write"
                ),
                "resource_id": convert_and_respect_annotation_metadata(
                    object_=resource_id, annotation=UserNotificationCreateResourceId, direction="write"
                ),
                "user_from_id": user_from_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def mark_notification_as_read(
        self, notification_id: str, *, read: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        notification_id : str

        read : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/me/notifications/{encode_path_param(notification_id)}",
            method="PATCH",
            json={
                "read": read,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_user_permissions(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeListMyPermissionGet]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeListMyPermissionGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/me/permissions",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeListMyPermissionGet,
                    parse_obj_as(
                        type_=EnvelopeListMyPermissionGet,
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

    def list_user_functions_permissions(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeMyFunctionPermissionsGet]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeMyFunctionPermissionsGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/me/function-permissions",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeMyFunctionPermissionsGet,
                    parse_obj_as(
                        type_=EnvelopeMyFunctionPermissionsGet,
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

    def search_users(
        self,
        *,
        match: SearchPatternSafeStr,
        limit: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvelopeListUserGet]:
        """
        Search among users who are publicly visible to the caller (i.e., me) based on their privacy settings.

        Parameters
        ----------
        match : SearchPatternSafeStr
            Search string to match with usernames and public profiles (e.g. emails, first/last name)

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeListUserGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/users:search",
            method="POST",
            json={
                "match": match,
                "limit": limit,
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
                    EnvelopeListUserGet,
                    parse_obj_as(
                        type_=EnvelopeListUserGet,
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

    def list_users_accounts(
        self,
        *,
        order_by: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        review_status: typing.Optional[ListUsersAccountsRequestReviewStatus] = None,
        registered: typing.Optional[bool] = None,
        product_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PageUserAccountGet]:
        """
        Parameters
        ----------
        order_by : typing.Optional[str]
            Comma-separated list of field names for sorting. Prefix with '-' for descending, '+' or no prefix for ascending.

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        review_status : typing.Optional[ListUsersAccountsRequestReviewStatus]

        registered : typing.Optional[bool]

        product_name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PageUserAccountGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/admin/user-accounts",
            method="GET",
            params={
                "order_by": order_by,
                "limit": limit,
                "offset": offset,
                "review_status": review_status,
                "registered": registered,
                "product_name": product_name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageUserAccountGet,
                    parse_obj_as(
                        type_=PageUserAccountGet,
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
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

    def approve_user_account(
        self,
        *,
        email: str,
        bcc_emails: typing.Optional[typing.Sequence[str]] = OMIT,
        invitation_url: typing.Optional[str] = OMIT,
        message_content: typing.Optional[MessageContent] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        email : str

        bcc_emails : typing.Optional[typing.Sequence[str]]

        invitation_url : typing.Optional[str]

        message_content : typing.Optional[MessageContent]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/admin/user-accounts:approve",
            method="POST",
            json={
                "email": email,
                "bccEmails": bcc_emails,
                "invitationUrl": invitation_url,
                "messageContent": convert_and_respect_annotation_metadata(
                    object_=message_content, annotation=typing.Optional[MessageContent], direction="write"
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
                return HttpResponse(response=_response, data=None)
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
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

    def preview_approval_user_account(
        self, *, email: str, invitation: InvitationDetails, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeUserAccountPreviewApprovalGet]:
        """
        Parameters
        ----------
        email : str

        invitation : InvitationDetails

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeUserAccountPreviewApprovalGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/admin/user-accounts:preview-approval",
            method="POST",
            json={
                "email": email,
                "invitation": convert_and_respect_annotation_metadata(
                    object_=invitation, annotation=InvitationDetails, direction="write"
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
                    EnvelopeUserAccountPreviewApprovalGet,
                    parse_obj_as(
                        type_=EnvelopeUserAccountPreviewApprovalGet,
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
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

    def reject_user_account(
        self,
        *,
        email: str,
        bcc_emails: typing.Optional[typing.Sequence[str]] = OMIT,
        message_content: typing.Optional[MessageContent] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        email : str

        bcc_emails : typing.Optional[typing.Sequence[str]]

        message_content : typing.Optional[MessageContent]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/admin/user-accounts:reject",
            method="POST",
            json={
                "email": email,
                "bccEmails": bcc_emails,
                "messageContent": convert_and_respect_annotation_metadata(
                    object_=message_content, annotation=typing.Optional[MessageContent], direction="write"
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
                return HttpResponse(response=_response, data=None)
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
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

    def preview_rejection_user_account(
        self, *, email: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeUserAccountPreviewRejectionGet]:
        """
        Parameters
        ----------
        email : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeUserAccountPreviewRejectionGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/admin/user-accounts:preview-rejection",
            method="POST",
            json={
                "email": email,
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
                    EnvelopeUserAccountPreviewRejectionGet,
                    parse_obj_as(
                        type_=EnvelopeUserAccountPreviewRejectionGet,
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
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

    def search_user_accounts(
        self,
        *,
        email: typing.Optional[GlobPatternSafeStr] = None,
        primary_group_id: typing.Optional[GroupIdInt] = None,
        user_name: typing.Optional[GlobPatternSafeStr] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvelopeListUserAccountGet]:
        """
        Parameters
        ----------
        email : typing.Optional[GlobPatternSafeStr]

        primary_group_id : typing.Optional[GroupIdInt]

        user_name : typing.Optional[GlobPatternSafeStr]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeListUserAccountGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/admin/user-accounts:search",
            method="GET",
            params={
                "email": email,
                "primary_group_id": primary_group_id,
                "user_name": user_name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeListUserAccountGet,
                    parse_obj_as(
                        type_=EnvelopeListUserAccountGet,
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
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

    def move_user_account(
        self,
        *,
        pre_registration_id: int,
        new_product_name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        pre_registration_id : int

        new_product_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/admin/user-accounts:move",
            method="POST",
            json={
                "preRegistrationId": pre_registration_id,
                "newProductName": new_product_name,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
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

    def list_products_for_user_accounts(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeListUserAccountProductOptionGet]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeListUserAccountProductOptionGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/admin/products",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeListUserAccountProductOptionGet,
                    parse_obj_as(
                        type_=EnvelopeListUserAccountProductOptionGet,
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
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

    def pre_register_user_account(
        self,
        *,
        first_name: FirstNameStr,
        last_name: LastNameStr,
        email: LowerCaseEmailStr,
        address: AddressLineSafeStr,
        city: DisplaySafeStr,
        postal_code: PostalCodeSafeStr,
        country: CountryNameStr,
        institution: typing.Optional[DisplaySafeStr] = OMIT,
        phone: typing.Optional[PhoneNumberStr] = OMIT,
        state: typing.Optional[DisplaySafeStr] = OMIT,
        extras: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvelopeUserAccountGet]:
        """
        Parameters
        ----------
        first_name : FirstNameStr

        last_name : LastNameStr

        email : LowerCaseEmailStr

        address : AddressLineSafeStr

        city : DisplaySafeStr

        postal_code : PostalCodeSafeStr

        country : CountryNameStr

        institution : typing.Optional[DisplaySafeStr]
            company, university, ...

        phone : typing.Optional[PhoneNumberStr]

        state : typing.Optional[DisplaySafeStr]

        extras : typing.Optional[typing.Dict[str, typing.Any]]
            Keeps extra information provided in the request form.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeUserAccountGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/admin/user-accounts:pre-register",
            method="POST",
            json={
                "firstName": first_name,
                "lastName": last_name,
                "email": email,
                "institution": institution,
                "phone": phone,
                "address": address,
                "city": city,
                "state": state,
                "postalCode": postal_code,
                "country": country,
                "extras": extras,
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
                    EnvelopeUserAccountGet,
                    parse_obj_as(
                        type_=EnvelopeUserAccountGet,
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
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


class AsyncRawUsersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_my_profile(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeMyProfileRestGet]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeMyProfileRestGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/me",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeMyProfileRestGet,
                    parse_obj_as(
                        type_=EnvelopeMyProfileRestGet,
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

    async def update_my_profile(
        self,
        *,
        first_name: typing.Optional[FirstNameStr] = OMIT,
        last_name: typing.Optional[LastNameStr] = OMIT,
        user_name: typing.Optional[UserNameSafeId] = OMIT,
        language: typing.Optional[SupportedLocale] = OMIT,
        privacy: typing.Optional[MyProfilePrivacyPatch] = OMIT,
        contact: typing.Optional[MyProfileAddressRestPatch] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        first_name : typing.Optional[FirstNameStr]

        last_name : typing.Optional[LastNameStr]

        user_name : typing.Optional[UserNameSafeId]

        language : typing.Optional[SupportedLocale]
            Persisted UI/communications language. The user owns and can edit it directly.

        privacy : typing.Optional[MyProfilePrivacyPatch]

        contact : typing.Optional[MyProfileAddressRestPatch]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/me",
            method="PATCH",
            json={
                "first_name": first_name,
                "last_name": last_name,
                "userName": user_name,
                "language": language,
                "privacy": convert_and_respect_annotation_metadata(
                    object_=privacy, annotation=typing.Optional[MyProfilePrivacyPatch], direction="write"
                ),
                "contact": convert_and_respect_annotation_metadata(
                    object_=contact, annotation=typing.Optional[MyProfileAddressRestPatch], direction="write"
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
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def my_phone_register(
        self, *, phone: PhoneNumberStr, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Starts the phone registration process

        Parameters
        ----------
        phone : PhoneNumberStr
            Phone number to register

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Phone registration initiated
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/me/phone:register",
            method="POST",
            json={
                "phone": phone,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    async def my_phone_resend(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Resends the phone registration code

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Phone code resent
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/me/phone:resend",
            method="POST",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
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

    async def my_phone_confirm(
        self, *, code: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Confirms the phone registration

        Parameters
        ----------
        code : str
            Alphanumeric confirmation code

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/me/phone:confirm",
            method="POST",
            json={
                "code": code,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    async def set_frontend_preference(
        self, preference_id: str, *, value: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        preference_id : str

        value : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/me/preferences/{encode_path_param(preference_id)}",
            method="PATCH",
            json={
                "value": value,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_tokens(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeListMyTokenGet]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeListMyTokenGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/me/tokens",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeListMyTokenGet,
                    parse_obj_as(
                        type_=EnvelopeListMyTokenGet,
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

    async def create_token(
        self,
        *,
        service: str,
        token_key: str,
        token_secret: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvelopeMyTokenGet]:
        """
        Parameters
        ----------
        service : str
            uniquely identifies the service where this token is used

        token_key : str

        token_secret : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeMyTokenGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/me/tokens",
            method="POST",
            json={
                "service": service,
                "token_key": token_key,
                "token_secret": token_secret,
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
                    EnvelopeMyTokenGet,
                    parse_obj_as(
                        type_=EnvelopeMyTokenGet,
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

    async def get_token(
        self, service: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeMyTokenGet]:
        """
        Parameters
        ----------
        service : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeMyTokenGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/me/tokens/{encode_path_param(service)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeMyTokenGet,
                    parse_obj_as(
                        type_=EnvelopeMyTokenGet,
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

    async def delete_token(
        self, service: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        service : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/me/tokens/{encode_path_param(service)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_user_notifications(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeListUserNotification]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeListUserNotification]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/me/notifications",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeListUserNotification,
                    parse_obj_as(
                        type_=EnvelopeListUserNotification,
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

    async def create_user_notification(
        self,
        *,
        user_id: UserIdInt,
        category: NotificationCategory,
        actionable_path: str,
        title: str,
        text: str,
        date: dt.datetime,
        product: typing.Optional[UserNotificationCreateProduct] = OMIT,
        resource_id: typing.Optional[UserNotificationCreateResourceId] = OMIT,
        user_from_id: typing.Optional[UserIdInt] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        user_id : UserIdInt

        category : NotificationCategory

        actionable_path : str

        title : str

        text : str

        date : dt.datetime

        product : typing.Optional[UserNotificationCreateProduct]

        resource_id : typing.Optional[UserNotificationCreateResourceId]

        user_from_id : typing.Optional[UserIdInt]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/me/notifications",
            method="POST",
            json={
                "user_id": user_id,
                "category": category,
                "actionable_path": actionable_path,
                "title": title,
                "text": text,
                "date": date,
                "product": convert_and_respect_annotation_metadata(
                    object_=product, annotation=UserNotificationCreateProduct, direction="write"
                ),
                "resource_id": convert_and_respect_annotation_metadata(
                    object_=resource_id, annotation=UserNotificationCreateResourceId, direction="write"
                ),
                "user_from_id": user_from_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def mark_notification_as_read(
        self, notification_id: str, *, read: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        notification_id : str

        read : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/me/notifications/{encode_path_param(notification_id)}",
            method="PATCH",
            json={
                "read": read,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_user_permissions(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeListMyPermissionGet]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeListMyPermissionGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/me/permissions",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeListMyPermissionGet,
                    parse_obj_as(
                        type_=EnvelopeListMyPermissionGet,
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

    async def list_user_functions_permissions(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeMyFunctionPermissionsGet]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeMyFunctionPermissionsGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/me/function-permissions",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeMyFunctionPermissionsGet,
                    parse_obj_as(
                        type_=EnvelopeMyFunctionPermissionsGet,
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

    async def search_users(
        self,
        *,
        match: SearchPatternSafeStr,
        limit: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvelopeListUserGet]:
        """
        Search among users who are publicly visible to the caller (i.e., me) based on their privacy settings.

        Parameters
        ----------
        match : SearchPatternSafeStr
            Search string to match with usernames and public profiles (e.g. emails, first/last name)

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeListUserGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/users:search",
            method="POST",
            json={
                "match": match,
                "limit": limit,
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
                    EnvelopeListUserGet,
                    parse_obj_as(
                        type_=EnvelopeListUserGet,
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

    async def list_users_accounts(
        self,
        *,
        order_by: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        review_status: typing.Optional[ListUsersAccountsRequestReviewStatus] = None,
        registered: typing.Optional[bool] = None,
        product_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PageUserAccountGet]:
        """
        Parameters
        ----------
        order_by : typing.Optional[str]
            Comma-separated list of field names for sorting. Prefix with '-' for descending, '+' or no prefix for ascending.

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        review_status : typing.Optional[ListUsersAccountsRequestReviewStatus]

        registered : typing.Optional[bool]

        product_name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PageUserAccountGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/admin/user-accounts",
            method="GET",
            params={
                "order_by": order_by,
                "limit": limit,
                "offset": offset,
                "review_status": review_status,
                "registered": registered,
                "product_name": product_name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageUserAccountGet,
                    parse_obj_as(
                        type_=PageUserAccountGet,
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
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

    async def approve_user_account(
        self,
        *,
        email: str,
        bcc_emails: typing.Optional[typing.Sequence[str]] = OMIT,
        invitation_url: typing.Optional[str] = OMIT,
        message_content: typing.Optional[MessageContent] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        email : str

        bcc_emails : typing.Optional[typing.Sequence[str]]

        invitation_url : typing.Optional[str]

        message_content : typing.Optional[MessageContent]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/admin/user-accounts:approve",
            method="POST",
            json={
                "email": email,
                "bccEmails": bcc_emails,
                "invitationUrl": invitation_url,
                "messageContent": convert_and_respect_annotation_metadata(
                    object_=message_content, annotation=typing.Optional[MessageContent], direction="write"
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
                return AsyncHttpResponse(response=_response, data=None)
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
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

    async def preview_approval_user_account(
        self, *, email: str, invitation: InvitationDetails, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeUserAccountPreviewApprovalGet]:
        """
        Parameters
        ----------
        email : str

        invitation : InvitationDetails

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeUserAccountPreviewApprovalGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/admin/user-accounts:preview-approval",
            method="POST",
            json={
                "email": email,
                "invitation": convert_and_respect_annotation_metadata(
                    object_=invitation, annotation=InvitationDetails, direction="write"
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
                    EnvelopeUserAccountPreviewApprovalGet,
                    parse_obj_as(
                        type_=EnvelopeUserAccountPreviewApprovalGet,
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
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

    async def reject_user_account(
        self,
        *,
        email: str,
        bcc_emails: typing.Optional[typing.Sequence[str]] = OMIT,
        message_content: typing.Optional[MessageContent] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        email : str

        bcc_emails : typing.Optional[typing.Sequence[str]]

        message_content : typing.Optional[MessageContent]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/admin/user-accounts:reject",
            method="POST",
            json={
                "email": email,
                "bccEmails": bcc_emails,
                "messageContent": convert_and_respect_annotation_metadata(
                    object_=message_content, annotation=typing.Optional[MessageContent], direction="write"
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
                return AsyncHttpResponse(response=_response, data=None)
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
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

    async def preview_rejection_user_account(
        self, *, email: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeUserAccountPreviewRejectionGet]:
        """
        Parameters
        ----------
        email : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeUserAccountPreviewRejectionGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/admin/user-accounts:preview-rejection",
            method="POST",
            json={
                "email": email,
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
                    EnvelopeUserAccountPreviewRejectionGet,
                    parse_obj_as(
                        type_=EnvelopeUserAccountPreviewRejectionGet,
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
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

    async def search_user_accounts(
        self,
        *,
        email: typing.Optional[GlobPatternSafeStr] = None,
        primary_group_id: typing.Optional[GroupIdInt] = None,
        user_name: typing.Optional[GlobPatternSafeStr] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvelopeListUserAccountGet]:
        """
        Parameters
        ----------
        email : typing.Optional[GlobPatternSafeStr]

        primary_group_id : typing.Optional[GroupIdInt]

        user_name : typing.Optional[GlobPatternSafeStr]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeListUserAccountGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/admin/user-accounts:search",
            method="GET",
            params={
                "email": email,
                "primary_group_id": primary_group_id,
                "user_name": user_name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeListUserAccountGet,
                    parse_obj_as(
                        type_=EnvelopeListUserAccountGet,
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
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

    async def move_user_account(
        self,
        *,
        pre_registration_id: int,
        new_product_name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        pre_registration_id : int

        new_product_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/admin/user-accounts:move",
            method="POST",
            json={
                "preRegistrationId": pre_registration_id,
                "newProductName": new_product_name,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
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

    async def list_products_for_user_accounts(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeListUserAccountProductOptionGet]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeListUserAccountProductOptionGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/admin/products",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeListUserAccountProductOptionGet,
                    parse_obj_as(
                        type_=EnvelopeListUserAccountProductOptionGet,
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
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

    async def pre_register_user_account(
        self,
        *,
        first_name: FirstNameStr,
        last_name: LastNameStr,
        email: LowerCaseEmailStr,
        address: AddressLineSafeStr,
        city: DisplaySafeStr,
        postal_code: PostalCodeSafeStr,
        country: CountryNameStr,
        institution: typing.Optional[DisplaySafeStr] = OMIT,
        phone: typing.Optional[PhoneNumberStr] = OMIT,
        state: typing.Optional[DisplaySafeStr] = OMIT,
        extras: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvelopeUserAccountGet]:
        """
        Parameters
        ----------
        first_name : FirstNameStr

        last_name : LastNameStr

        email : LowerCaseEmailStr

        address : AddressLineSafeStr

        city : DisplaySafeStr

        postal_code : PostalCodeSafeStr

        country : CountryNameStr

        institution : typing.Optional[DisplaySafeStr]
            company, university, ...

        phone : typing.Optional[PhoneNumberStr]

        state : typing.Optional[DisplaySafeStr]

        extras : typing.Optional[typing.Dict[str, typing.Any]]
            Keeps extra information provided in the request form.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeUserAccountGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/admin/user-accounts:pre-register",
            method="POST",
            json={
                "firstName": first_name,
                "lastName": last_name,
                "email": email,
                "institution": institution,
                "phone": phone,
                "address": address,
                "city": city,
                "state": state,
                "postalCode": postal_code,
                "country": country,
                "extras": extras,
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
                    EnvelopeUserAccountGet,
                    parse_obj_as(
                        type_=EnvelopeUserAccountGet,
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
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

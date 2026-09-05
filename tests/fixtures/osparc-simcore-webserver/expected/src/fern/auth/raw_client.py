

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.conflict_error import ConflictError
from ..errors.not_found_error import NotFoundError
from ..errors.service_unavailable_error import ServiceUnavailableError
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.envelope_api_key_create_response import EnvelopeApiKeyCreateResponse
from ..types.envelope_api_key_get import EnvelopeApiKeyGet
from ..types.envelope_invitation_info import EnvelopeInvitationInfo
from ..types.envelope_list_api_key_get import EnvelopeListApiKeyGet
from ..types.envelope_log import EnvelopeLog
from ..types.envelope_login_next_page import EnvelopeLoginNextPage
from ..types.envelope_register_phone_next_page import EnvelopeRegisterPhoneNextPage
from ..types.lower_case_email_str import LowerCaseEmailStr
from ..types.phone_number_str import PhoneNumberStr
from .types.resend2fa_body_via import Resend2FaBodyVia
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawAuthClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def request_product_account(
        self,
        *,
        form: typing.Dict[str, typing.Any],
        captcha: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        form : typing.Dict[str, typing.Any]

        captcha : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/auth/request-account",
            method="POST",
            json={
                "form": form,
                "captcha": captcha,
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

    def check_registration_invitation(
        self, *, invitation: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeInvitationInfo]:
        """
        Check invitation and returns associated email or None

        Parameters
        ----------
        invitation : str
            Invitation code

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeInvitationInfo]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/auth/register/invitations:check",
            method="POST",
            json={
                "invitation": invitation,
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
                    EnvelopeInvitationInfo,
                    parse_obj_as(
                        type_=EnvelopeInvitationInfo,
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

    def register(
        self,
        *,
        email: LowerCaseEmailStr,
        password: str,
        confirm: typing.Optional[str] = OMIT,
        invitation: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvelopeLog]:
        """
        User registration

        Parameters
        ----------
        email : LowerCaseEmailStr

        password : str

        confirm : typing.Optional[str]
            Password confirmation

        invitation : typing.Optional[str]
            Invitation code

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeLog]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/auth/register",
            method="POST",
            json={
                "email": email,
                "password": password,
                "confirm": confirm,
                "invitation": invitation,
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
                    EnvelopeLog,
                    parse_obj_as(
                        type_=EnvelopeLog,
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

    def unregister_account(
        self, *, email: LowerCaseEmailStr, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeLog]:
        """
        Parameters
        ----------
        email : LowerCaseEmailStr

        password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeLog]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/auth/unregister",
            method="POST",
            json={
                "email": email,
                "password": password,
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
                    EnvelopeLog,
                    parse_obj_as(
                        type_=EnvelopeLog,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def register_phone(
        self,
        *,
        email: LowerCaseEmailStr,
        phone: PhoneNumberStr,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvelopeRegisterPhoneNextPage]:
        """
        user tries to verify phone number for 2 Factor Authentication when registering

        Parameters
        ----------
        email : LowerCaseEmailStr

        phone : PhoneNumberStr
            Phone number E.164, needed on the deployments with 2FA

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeRegisterPhoneNextPage]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/auth/verify-phone-number",
            method="POST",
            json={
                "email": email,
                "phone": phone,
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
                    EnvelopeRegisterPhoneNextPage,
                    parse_obj_as(
                        type_=EnvelopeRegisterPhoneNextPage,
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

    def phone_confirmation(
        self,
        *,
        email: LowerCaseEmailStr,
        phone: str,
        code: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvelopeLog]:
        """
        user enters 2 Factor Authentication code when registering

        Parameters
        ----------
        email : LowerCaseEmailStr

        phone : str
            Phone number E.164, needed on the deployments with 2FA

        code : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeLog]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/auth/validate-code-register",
            method="POST",
            json={
                "email": email,
                "phone": phone,
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
                _data = typing.cast(
                    EnvelopeLog,
                    parse_obj_as(
                        type_=EnvelopeLog,
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

    def login(
        self, *, email: LowerCaseEmailStr, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeLoginNextPage]:
        """
        user logs in

        Parameters
        ----------
        email : LowerCaseEmailStr

        password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeLoginNextPage]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/auth/login",
            method="POST",
            json={
                "email": email,
                "password": password,
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
                    EnvelopeLoginNextPage,
                    parse_obj_as(
                        type_=EnvelopeLoginNextPage,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def login2fa(
        self, *, email: LowerCaseEmailStr, code: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeLog]:
        """
        user enters 2 Factor Authentication code when login in

        Parameters
        ----------
        email : LowerCaseEmailStr

        code : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeLog]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/auth/validate-code-login",
            method="POST",
            json={
                "email": email,
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
                _data = typing.cast(
                    EnvelopeLog,
                    parse_obj_as(
                        type_=EnvelopeLog,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def resend2fa_code(
        self,
        *,
        email: LowerCaseEmailStr,
        via: typing.Optional[Resend2FaBodyVia] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvelopeLog]:
        """
        Resends 2FA either via email or sms

        Parameters
        ----------
        email : LowerCaseEmailStr
            User email (identifier)

        via : typing.Optional[Resend2FaBodyVia]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeLog]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/auth/two_factor:resend",
            method="POST",
            json={
                "email": email,
                "via": via,
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
                    EnvelopeLog,
                    parse_obj_as(
                        type_=EnvelopeLog,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def logout(
        self, *, client_session_id: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeLog]:
        """
        user logout

        Parameters
        ----------
        client_session_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeLog]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/auth/logout",
            method="POST",
            json={
                "client_session_id": client_session_id,
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
                    EnvelopeLog,
                    parse_obj_as(
                        type_=EnvelopeLog,
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

    def check_auth(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """
        checks whether user request is authenticated

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/auth:check",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def initiate_reset_password(
        self, *, email: LowerCaseEmailStr, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeLog]:
        """
        Parameters
        ----------
        email : LowerCaseEmailStr

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeLog]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/auth/reset-password",
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
                    EnvelopeLog,
                    parse_obj_as(
                        type_=EnvelopeLog,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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

    def complete_reset_password(
        self, code: str, *, password: str, confirm: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeLog]:
        """
        Parameters
        ----------
        code : str

        password : str

        confirm : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeLog]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/auth/reset-password/{encode_path_param(code)}",
            method="POST",
            json={
                "password": password,
                "confirm": confirm,
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
                    EnvelopeLog,
                    parse_obj_as(
                        type_=EnvelopeLog,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def change_password(
        self, *, current: str, new: str, confirm: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeLog]:
        """
        logged in user changes password

        Parameters
        ----------
        current : str

        new : str

        confirm : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeLog]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/auth/change-password",
            method="POST",
            json={
                "current": current,
                "new": new,
                "confirm": confirm,
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
                    EnvelopeLog,
                    parse_obj_as(
                        type_=EnvelopeLog,
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

    def confirmation(
        self, code: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeLog]:
        """
        email link sent to user to confirm an action

        Parameters
        ----------
        code : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeLog]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/auth/confirmation/{encode_path_param(code)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeLog,
                    parse_obj_as(
                        type_=EnvelopeLog,
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

    def create_captcha(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/auth/captcha",
            method="GET",
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_api_keys(
        self,
        *,
        include_autogenerated: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvelopeListApiKeyGet]:
        """
        lists API keys by this user

        Parameters
        ----------
        include_autogenerated : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeListApiKeyGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/auth/api-keys",
            method="GET",
            params={
                "includeAutogenerated": include_autogenerated,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeListApiKeyGet,
                    parse_obj_as(
                        type_=EnvelopeListApiKeyGet,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_api_key(
        self,
        *,
        display_name: str,
        expiration: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvelopeApiKeyCreateResponse]:
        """
        creates API keys to access public API

        Parameters
        ----------
        display_name : str

        expiration : typing.Optional[str]
            Time delta from creation time to expiration. If None, then it does not expire.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeApiKeyCreateResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/auth/api-keys",
            method="POST",
            json={
                "displayName": display_name,
                "expiration": expiration,
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
                    EnvelopeApiKeyCreateResponse,
                    parse_obj_as(
                        type_=EnvelopeApiKeyCreateResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_api_key(
        self, api_key_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeApiKeyGet]:
        """
        returns the API Key with the given ID

        Parameters
        ----------
        api_key_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeApiKeyGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/auth/api-keys/{encode_path_param(api_key_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeApiKeyGet,
                    parse_obj_as(
                        type_=EnvelopeApiKeyGet,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_api_key(
        self, api_key_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        deletes the API key with the given ID

        Parameters
        ----------
        api_key_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/auth/api-keys/{encode_path_param(api_key_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawAuthClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def request_product_account(
        self,
        *,
        form: typing.Dict[str, typing.Any],
        captcha: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        form : typing.Dict[str, typing.Any]

        captcha : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/auth/request-account",
            method="POST",
            json={
                "form": form,
                "captcha": captcha,
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

    async def check_registration_invitation(
        self, *, invitation: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeInvitationInfo]:
        """
        Check invitation and returns associated email or None

        Parameters
        ----------
        invitation : str
            Invitation code

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeInvitationInfo]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/auth/register/invitations:check",
            method="POST",
            json={
                "invitation": invitation,
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
                    EnvelopeInvitationInfo,
                    parse_obj_as(
                        type_=EnvelopeInvitationInfo,
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

    async def register(
        self,
        *,
        email: LowerCaseEmailStr,
        password: str,
        confirm: typing.Optional[str] = OMIT,
        invitation: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvelopeLog]:
        """
        User registration

        Parameters
        ----------
        email : LowerCaseEmailStr

        password : str

        confirm : typing.Optional[str]
            Password confirmation

        invitation : typing.Optional[str]
            Invitation code

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeLog]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/auth/register",
            method="POST",
            json={
                "email": email,
                "password": password,
                "confirm": confirm,
                "invitation": invitation,
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
                    EnvelopeLog,
                    parse_obj_as(
                        type_=EnvelopeLog,
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

    async def unregister_account(
        self, *, email: LowerCaseEmailStr, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeLog]:
        """
        Parameters
        ----------
        email : LowerCaseEmailStr

        password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeLog]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/auth/unregister",
            method="POST",
            json={
                "email": email,
                "password": password,
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
                    EnvelopeLog,
                    parse_obj_as(
                        type_=EnvelopeLog,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def register_phone(
        self,
        *,
        email: LowerCaseEmailStr,
        phone: PhoneNumberStr,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvelopeRegisterPhoneNextPage]:
        """
        user tries to verify phone number for 2 Factor Authentication when registering

        Parameters
        ----------
        email : LowerCaseEmailStr

        phone : PhoneNumberStr
            Phone number E.164, needed on the deployments with 2FA

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeRegisterPhoneNextPage]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/auth/verify-phone-number",
            method="POST",
            json={
                "email": email,
                "phone": phone,
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
                    EnvelopeRegisterPhoneNextPage,
                    parse_obj_as(
                        type_=EnvelopeRegisterPhoneNextPage,
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

    async def phone_confirmation(
        self,
        *,
        email: LowerCaseEmailStr,
        phone: str,
        code: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvelopeLog]:
        """
        user enters 2 Factor Authentication code when registering

        Parameters
        ----------
        email : LowerCaseEmailStr

        phone : str
            Phone number E.164, needed on the deployments with 2FA

        code : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeLog]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/auth/validate-code-register",
            method="POST",
            json={
                "email": email,
                "phone": phone,
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
                _data = typing.cast(
                    EnvelopeLog,
                    parse_obj_as(
                        type_=EnvelopeLog,
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

    async def login(
        self, *, email: LowerCaseEmailStr, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeLoginNextPage]:
        """
        user logs in

        Parameters
        ----------
        email : LowerCaseEmailStr

        password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeLoginNextPage]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/auth/login",
            method="POST",
            json={
                "email": email,
                "password": password,
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
                    EnvelopeLoginNextPage,
                    parse_obj_as(
                        type_=EnvelopeLoginNextPage,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def login2fa(
        self, *, email: LowerCaseEmailStr, code: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeLog]:
        """
        user enters 2 Factor Authentication code when login in

        Parameters
        ----------
        email : LowerCaseEmailStr

        code : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeLog]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/auth/validate-code-login",
            method="POST",
            json={
                "email": email,
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
                _data = typing.cast(
                    EnvelopeLog,
                    parse_obj_as(
                        type_=EnvelopeLog,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def resend2fa_code(
        self,
        *,
        email: LowerCaseEmailStr,
        via: typing.Optional[Resend2FaBodyVia] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvelopeLog]:
        """
        Resends 2FA either via email or sms

        Parameters
        ----------
        email : LowerCaseEmailStr
            User email (identifier)

        via : typing.Optional[Resend2FaBodyVia]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeLog]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/auth/two_factor:resend",
            method="POST",
            json={
                "email": email,
                "via": via,
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
                    EnvelopeLog,
                    parse_obj_as(
                        type_=EnvelopeLog,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def logout(
        self, *, client_session_id: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeLog]:
        """
        user logout

        Parameters
        ----------
        client_session_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeLog]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/auth/logout",
            method="POST",
            json={
                "client_session_id": client_session_id,
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
                    EnvelopeLog,
                    parse_obj_as(
                        type_=EnvelopeLog,
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

    async def check_auth(self, *, request_options: typing.Optional[RequestOptions] = None) -> AsyncHttpResponse[None]:
        """
        checks whether user request is authenticated

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/auth:check",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def initiate_reset_password(
        self, *, email: LowerCaseEmailStr, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeLog]:
        """
        Parameters
        ----------
        email : LowerCaseEmailStr

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeLog]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/auth/reset-password",
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
                    EnvelopeLog,
                    parse_obj_as(
                        type_=EnvelopeLog,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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

    async def complete_reset_password(
        self, code: str, *, password: str, confirm: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeLog]:
        """
        Parameters
        ----------
        code : str

        password : str

        confirm : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeLog]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/auth/reset-password/{encode_path_param(code)}",
            method="POST",
            json={
                "password": password,
                "confirm": confirm,
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
                    EnvelopeLog,
                    parse_obj_as(
                        type_=EnvelopeLog,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def change_password(
        self, *, current: str, new: str, confirm: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeLog]:
        """
        logged in user changes password

        Parameters
        ----------
        current : str

        new : str

        confirm : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeLog]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/auth/change-password",
            method="POST",
            json={
                "current": current,
                "new": new,
                "confirm": confirm,
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
                    EnvelopeLog,
                    parse_obj_as(
                        type_=EnvelopeLog,
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

    async def confirmation(
        self, code: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeLog]:
        """
        email link sent to user to confirm an action

        Parameters
        ----------
        code : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeLog]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/auth/confirmation/{encode_path_param(code)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeLog,
                    parse_obj_as(
                        type_=EnvelopeLog,
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

    async def create_captcha(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/auth/captcha",
            method="GET",
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_api_keys(
        self,
        *,
        include_autogenerated: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvelopeListApiKeyGet]:
        """
        lists API keys by this user

        Parameters
        ----------
        include_autogenerated : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeListApiKeyGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/auth/api-keys",
            method="GET",
            params={
                "includeAutogenerated": include_autogenerated,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeListApiKeyGet,
                    parse_obj_as(
                        type_=EnvelopeListApiKeyGet,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_api_key(
        self,
        *,
        display_name: str,
        expiration: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvelopeApiKeyCreateResponse]:
        """
        creates API keys to access public API

        Parameters
        ----------
        display_name : str

        expiration : typing.Optional[str]
            Time delta from creation time to expiration. If None, then it does not expire.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeApiKeyCreateResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/auth/api-keys",
            method="POST",
            json={
                "displayName": display_name,
                "expiration": expiration,
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
                    EnvelopeApiKeyCreateResponse,
                    parse_obj_as(
                        type_=EnvelopeApiKeyCreateResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_api_key(
        self, api_key_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeApiKeyGet]:
        """
        returns the API Key with the given ID

        Parameters
        ----------
        api_key_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeApiKeyGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/auth/api-keys/{encode_path_param(api_key_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeApiKeyGet,
                    parse_obj_as(
                        type_=EnvelopeApiKeyGet,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_api_key(
        self, api_key_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        deletes the API key with the given ID

        Parameters
        ----------
        api_key_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/auth/api-keys/{encode_path_param(api_key_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

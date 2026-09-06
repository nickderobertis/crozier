

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
from ..types.api_i_paged_response_global_resources_shared_models_translation_request import (
    ApiIPagedResponseGlobalResourcesSharedModelsTranslationRequest,
)
from ..types.global_resources_shared_models_translation_request import GlobalResourcesSharedModelsTranslationRequest
from ..types.global_resources_shared_models_translation_request_state import (
    GlobalResourcesSharedModelsTranslationRequestState,
)
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawTranslationrequestsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def gettranslationrequests(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiIPagedResponseGlobalResourcesSharedModelsTranslationRequest]:
        """
        No Documentation Found.

        Parameters
        ----------
        limit : typing.Optional[int]


        offset : typing.Optional[int]


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiIPagedResponseGlobalResourcesSharedModelsTranslationRequest]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/TranslationRequests",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiIPagedResponseGlobalResourcesSharedModelsTranslationRequest,
                    parse_obj_as(
                        type_=ApiIPagedResponseGlobalResourcesSharedModelsTranslationRequest,
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

    def createtranslationrequest(
        self,
        *,
        cc_email_addresses: typing.Sequence[str],
        charge_to_account: str,
        deadline: dt.datetime,
        locale_ids: typing.Sequence[int],
        notes: str,
        state: GlobalResourcesSharedModelsTranslationRequestState,
        approval_user_id: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        questions_user_id: typing.Optional[int] = OMIT,
        submitted_by: typing.Optional[int] = OMIT,
        translator_email: typing.Optional[str] = OMIT,
        translator_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[int]:
        """
        No Documentation Found.

        Parameters
        ----------
        cc_email_addresses : typing.Sequence[str]
            Additional email addresses to CC on emails pertaining to the request

        charge_to_account : str
            The account to charge for the request

        deadline : dt.datetime
            The date by which the translations in the request are needed. Defaults to 30 days from the current date

        locale_ids : typing.Sequence[int]
            Locale IDs to which these strings are requested to be translated

        notes : str
            Additional notes or comments about the request

        state : GlobalResourcesSharedModelsTranslationRequestState
            The state of the request

        approval_user_id : typing.Optional[int]
            The ID of the user from which approval for the request is required

        id : typing.Optional[int]
            The ID of the request

        questions_user_id : typing.Optional[int]
            The ID of the user to which to address questions regarding the request

        submitted_by : typing.Optional[int]
            The ID of the User that submitted the request

        translator_email : typing.Optional[str]
            The email address for the translator

        translator_name : typing.Optional[str]
            The name of the translator

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[int]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/TranslationRequests",
            method="POST",
            json={
                "ApprovalUserId": approval_user_id,
                "CCEmailAddresses": cc_email_addresses,
                "ChargeToAccount": charge_to_account,
                "Deadline": deadline,
                "Id": id,
                "LocaleIds": locale_ids,
                "Notes": notes,
                "QuestionsUserId": questions_user_id,
                "State": state,
                "SubmittedBy": submitted_by,
                "TranslatorEmail": translator_email,
                "TranslatorName": translator_name,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    int,
                    parse_obj_as(
                        type_=int,
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

    def gettranslationrequest(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GlobalResourcesSharedModelsTranslationRequest]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GlobalResourcesSharedModelsTranslationRequest]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/TranslationRequests/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GlobalResourcesSharedModelsTranslationRequest,
                    parse_obj_as(
                        type_=GlobalResourcesSharedModelsTranslationRequest,
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

    def updatetranslationrequest(
        self,
        id_: int,
        *,
        cc_email_addresses: typing.Sequence[str],
        charge_to_account: str,
        deadline: dt.datetime,
        locale_ids: typing.Sequence[int],
        notes: str,
        state: GlobalResourcesSharedModelsTranslationRequestState,
        do_resend_request: typing.Optional[bool] = None,
        approval_user_id: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        questions_user_id: typing.Optional[int] = OMIT,
        submitted_by: typing.Optional[int] = OMIT,
        translator_email: typing.Optional[str] = OMIT,
        translator_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id_ : int


        cc_email_addresses : typing.Sequence[str]
            Additional email addresses to CC on emails pertaining to the request

        charge_to_account : str
            The account to charge for the request

        deadline : dt.datetime
            The date by which the translations in the request are needed. Defaults to 30 days from the current date

        locale_ids : typing.Sequence[int]
            Locale IDs to which these strings are requested to be translated

        notes : str
            Additional notes or comments about the request

        state : GlobalResourcesSharedModelsTranslationRequestState
            The state of the request

        do_resend_request : typing.Optional[bool]


        approval_user_id : typing.Optional[int]
            The ID of the user from which approval for the request is required

        id : typing.Optional[int]
            The ID of the request

        questions_user_id : typing.Optional[int]
            The ID of the user to which to address questions regarding the request

        submitted_by : typing.Optional[int]
            The ID of the User that submitted the request

        translator_email : typing.Optional[str]
            The email address for the translator

        translator_name : typing.Optional[str]
            The name of the translator

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/TranslationRequests/{encode_path_param(id_)}",
            method="PUT",
            params={
                "doResendRequest": do_resend_request,
            },
            json={
                "ApprovalUserId": approval_user_id,
                "CCEmailAddresses": cc_email_addresses,
                "ChargeToAccount": charge_to_account,
                "Deadline": deadline,
                "Id": id,
                "LocaleIds": locale_ids,
                "Notes": notes,
                "QuestionsUserId": questions_user_id,
                "State": state,
                "SubmittedBy": submitted_by,
                "TranslatorEmail": translator_email,
                "TranslatorName": translator_name,
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

    def updatetranslationrequeststrings(
        self, id: int, *, request: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int

        request : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/TranslationRequests/{encode_path_param(id)}/Strings",
            method="PUT",
            json=request,
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


class AsyncRawTranslationrequestsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def gettranslationrequests(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiIPagedResponseGlobalResourcesSharedModelsTranslationRequest]:
        """
        No Documentation Found.

        Parameters
        ----------
        limit : typing.Optional[int]


        offset : typing.Optional[int]


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiIPagedResponseGlobalResourcesSharedModelsTranslationRequest]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/TranslationRequests",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiIPagedResponseGlobalResourcesSharedModelsTranslationRequest,
                    parse_obj_as(
                        type_=ApiIPagedResponseGlobalResourcesSharedModelsTranslationRequest,
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

    async def createtranslationrequest(
        self,
        *,
        cc_email_addresses: typing.Sequence[str],
        charge_to_account: str,
        deadline: dt.datetime,
        locale_ids: typing.Sequence[int],
        notes: str,
        state: GlobalResourcesSharedModelsTranslationRequestState,
        approval_user_id: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        questions_user_id: typing.Optional[int] = OMIT,
        submitted_by: typing.Optional[int] = OMIT,
        translator_email: typing.Optional[str] = OMIT,
        translator_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[int]:
        """
        No Documentation Found.

        Parameters
        ----------
        cc_email_addresses : typing.Sequence[str]
            Additional email addresses to CC on emails pertaining to the request

        charge_to_account : str
            The account to charge for the request

        deadline : dt.datetime
            The date by which the translations in the request are needed. Defaults to 30 days from the current date

        locale_ids : typing.Sequence[int]
            Locale IDs to which these strings are requested to be translated

        notes : str
            Additional notes or comments about the request

        state : GlobalResourcesSharedModelsTranslationRequestState
            The state of the request

        approval_user_id : typing.Optional[int]
            The ID of the user from which approval for the request is required

        id : typing.Optional[int]
            The ID of the request

        questions_user_id : typing.Optional[int]
            The ID of the user to which to address questions regarding the request

        submitted_by : typing.Optional[int]
            The ID of the User that submitted the request

        translator_email : typing.Optional[str]
            The email address for the translator

        translator_name : typing.Optional[str]
            The name of the translator

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[int]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/TranslationRequests",
            method="POST",
            json={
                "ApprovalUserId": approval_user_id,
                "CCEmailAddresses": cc_email_addresses,
                "ChargeToAccount": charge_to_account,
                "Deadline": deadline,
                "Id": id,
                "LocaleIds": locale_ids,
                "Notes": notes,
                "QuestionsUserId": questions_user_id,
                "State": state,
                "SubmittedBy": submitted_by,
                "TranslatorEmail": translator_email,
                "TranslatorName": translator_name,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    int,
                    parse_obj_as(
                        type_=int,
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

    async def gettranslationrequest(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GlobalResourcesSharedModelsTranslationRequest]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GlobalResourcesSharedModelsTranslationRequest]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/TranslationRequests/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GlobalResourcesSharedModelsTranslationRequest,
                    parse_obj_as(
                        type_=GlobalResourcesSharedModelsTranslationRequest,
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

    async def updatetranslationrequest(
        self,
        id_: int,
        *,
        cc_email_addresses: typing.Sequence[str],
        charge_to_account: str,
        deadline: dt.datetime,
        locale_ids: typing.Sequence[int],
        notes: str,
        state: GlobalResourcesSharedModelsTranslationRequestState,
        do_resend_request: typing.Optional[bool] = None,
        approval_user_id: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        questions_user_id: typing.Optional[int] = OMIT,
        submitted_by: typing.Optional[int] = OMIT,
        translator_email: typing.Optional[str] = OMIT,
        translator_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id_ : int


        cc_email_addresses : typing.Sequence[str]
            Additional email addresses to CC on emails pertaining to the request

        charge_to_account : str
            The account to charge for the request

        deadline : dt.datetime
            The date by which the translations in the request are needed. Defaults to 30 days from the current date

        locale_ids : typing.Sequence[int]
            Locale IDs to which these strings are requested to be translated

        notes : str
            Additional notes or comments about the request

        state : GlobalResourcesSharedModelsTranslationRequestState
            The state of the request

        do_resend_request : typing.Optional[bool]


        approval_user_id : typing.Optional[int]
            The ID of the user from which approval for the request is required

        id : typing.Optional[int]
            The ID of the request

        questions_user_id : typing.Optional[int]
            The ID of the user to which to address questions regarding the request

        submitted_by : typing.Optional[int]
            The ID of the User that submitted the request

        translator_email : typing.Optional[str]
            The email address for the translator

        translator_name : typing.Optional[str]
            The name of the translator

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/TranslationRequests/{encode_path_param(id_)}",
            method="PUT",
            params={
                "doResendRequest": do_resend_request,
            },
            json={
                "ApprovalUserId": approval_user_id,
                "CCEmailAddresses": cc_email_addresses,
                "ChargeToAccount": charge_to_account,
                "Deadline": deadline,
                "Id": id,
                "LocaleIds": locale_ids,
                "Notes": notes,
                "QuestionsUserId": questions_user_id,
                "State": state,
                "SubmittedBy": submitted_by,
                "TranslatorEmail": translator_email,
                "TranslatorName": translator_name,
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

    async def updatetranslationrequeststrings(
        self, id: int, *, request: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int

        request : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/TranslationRequests/{encode_path_param(id)}/Strings",
            method="PUT",
            json=request,
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

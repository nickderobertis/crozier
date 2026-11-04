

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.error_bad_request import ErrorBadRequest
from ..types.error_forbidden import ErrorForbidden
from ..types.error_internal_server_error import ErrorInternalServerError
from ..types.error_not_found import ErrorNotFound
from ..types.error_unauthorized import ErrorUnauthorized
from .types.ai_classify_survey_request_language_strategy import AiClassifySurveyRequestLanguageStrategy
from .types.ai_classify_survey_request_run_strategy import AiClassifySurveyRequestRunStrategy
from .types.ai_classify_survey_response import AiClassifySurveyResponse
from .types.ai_gateway_delete_response import AiGatewayDeleteResponse
from .types.ai_gateway_info_response import AiGatewayInfoResponse
from .types.ai_gateway_logs_response import AiGatewayLogsResponse
from .types.ai_gateway_model_pricing_response import AiGatewayModelPricingResponse
from .types.ai_gateway_quota_alert_get_response import AiGatewayQuotaAlertGetResponse
from .types.ai_gateway_quota_alert_upsert_response import AiGatewayQuotaAlertUpsertResponse
from .types.ai_gateway_update_response import AiGatewayUpdateResponse
from .types.ai_translate_survey_request_language_strategy import AiTranslateSurveyRequestLanguageStrategy
from .types.ai_translate_survey_request_run_strategy import AiTranslateSurveyRequestRunStrategy
from .types.ai_translate_survey_response import AiTranslateSurveyResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawAiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def classifysurvey(
        self,
        *,
        workspace_id: str,
        survey_id: str,
        start_at: float,
        end_at: float,
        run_strategy: AiClassifySurveyRequestRunStrategy,
        payload_content_field: str,
        suggestion_category: typing.Sequence[str],
        language_strategy: typing.Optional[AiClassifySurveyRequestLanguageStrategy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AiClassifySurveyResponse]:
        """
        classify survey

        Parameters
        ----------
        workspace_id : str

        survey_id : str

        start_at : float

        end_at : float

        run_strategy : AiClassifySurveyRequestRunStrategy

        payload_content_field : str

        suggestion_category : typing.Sequence[str]

        language_strategy : typing.Optional[AiClassifySurveyRequestLanguageStrategy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AiClassifySurveyResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "ai/classifySurvey",
            method="POST",
            json={
                "workspaceId": workspace_id,
                "surveyId": survey_id,
                "startAt": start_at,
                "endAt": end_at,
                "runStrategy": run_strategy,
                "languageStrategy": language_strategy,
                "payloadContentField": payload_content_field,
                "suggestionCategory": suggestion_category,
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
                    AiClassifySurveyResponse,
                    parse_obj_as(
                        type_=AiClassifySurveyResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorBadRequest,
                        parse_obj_as(
                            type_=ErrorBadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorUnauthorized,
                        parse_obj_as(
                            type_=ErrorUnauthorized,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorForbidden,
                        parse_obj_as(
                            type_=ErrorForbidden,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorInternalServerError,
                        parse_obj_as(
                            type_=ErrorInternalServerError,
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

    def translatesurvey(
        self,
        *,
        workspace_id: str,
        survey_id: str,
        start_at: float,
        end_at: float,
        run_strategy: AiTranslateSurveyRequestRunStrategy,
        payload_content_field: str,
        language_strategy: typing.Optional[AiTranslateSurveyRequestLanguageStrategy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AiTranslateSurveyResponse]:
        """
        translate survey

        Parameters
        ----------
        workspace_id : str

        survey_id : str

        start_at : float

        end_at : float

        run_strategy : AiTranslateSurveyRequestRunStrategy

        payload_content_field : str

        language_strategy : typing.Optional[AiTranslateSurveyRequestLanguageStrategy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AiTranslateSurveyResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "ai/translateSurvey",
            method="POST",
            json={
                "workspaceId": workspace_id,
                "surveyId": survey_id,
                "startAt": start_at,
                "endAt": end_at,
                "runStrategy": run_strategy,
                "languageStrategy": language_strategy,
                "payloadContentField": payload_content_field,
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
                    AiTranslateSurveyResponse,
                    parse_obj_as(
                        type_=AiTranslateSurveyResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorBadRequest,
                        parse_obj_as(
                            type_=ErrorBadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorUnauthorized,
                        parse_obj_as(
                            type_=ErrorUnauthorized,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorForbidden,
                        parse_obj_as(
                            type_=ErrorForbidden,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorInternalServerError,
                        parse_obj_as(
                            type_=ErrorInternalServerError,
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

    def ai_gateway_info(
        self, *, workspace_id: str, gateway_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[AiGatewayInfoResponse]]:
        """
        Parameters
        ----------
        workspace_id : str

        gateway_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[AiGatewayInfoResponse]]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "aiGateway/info",
            method="GET",
            params={
                "workspaceId": workspace_id,
                "gatewayId": gateway_id,
            },
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[AiGatewayInfoResponse],
                    parse_obj_as(
                        type_=typing.Optional[AiGatewayInfoResponse],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorBadRequest,
                        parse_obj_as(
                            type_=ErrorBadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorUnauthorized,
                        parse_obj_as(
                            type_=ErrorUnauthorized,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorForbidden,
                        parse_obj_as(
                            type_=ErrorForbidden,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorNotFound,
                        parse_obj_as(
                            type_=ErrorNotFound,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorInternalServerError,
                        parse_obj_as(
                            type_=ErrorInternalServerError,
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

    def ai_gateway_update(
        self,
        *,
        workspace_id: str,
        gateway_id: str,
        name: str,
        model_api_key: typing.Optional[str] = OMIT,
        custom_model_base_url: typing.Optional[str] = OMIT,
        custom_model_name: typing.Optional[str] = OMIT,
        custom_model_input_price: typing.Optional[float] = OMIT,
        custom_model_output_price: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AiGatewayUpdateResponse]:
        """
        Parameters
        ----------
        workspace_id : str

        gateway_id : str

        name : str

        model_api_key : typing.Optional[str]

        custom_model_base_url : typing.Optional[str]

        custom_model_name : typing.Optional[str]

        custom_model_input_price : typing.Optional[float]

        custom_model_output_price : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AiGatewayUpdateResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "aiGateway/update",
            method="PATCH",
            json={
                "workspaceId": workspace_id,
                "gatewayId": gateway_id,
                "name": name,
                "modelApiKey": model_api_key,
                "customModelBaseUrl": custom_model_base_url,
                "customModelName": custom_model_name,
                "customModelInputPrice": custom_model_input_price,
                "customModelOutputPrice": custom_model_output_price,
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
                    AiGatewayUpdateResponse,
                    parse_obj_as(
                        type_=AiGatewayUpdateResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorBadRequest,
                        parse_obj_as(
                            type_=ErrorBadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorUnauthorized,
                        parse_obj_as(
                            type_=ErrorUnauthorized,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorForbidden,
                        parse_obj_as(
                            type_=ErrorForbidden,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorNotFound,
                        parse_obj_as(
                            type_=ErrorNotFound,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorInternalServerError,
                        parse_obj_as(
                            type_=ErrorInternalServerError,
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

    def ai_gateway_delete(
        self, *, workspace_id: str, gateway_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[AiGatewayDeleteResponse]:
        """
        Parameters
        ----------
        workspace_id : str

        gateway_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AiGatewayDeleteResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "aiGateway/delete",
            method="DELETE",
            params={
                "workspaceId": workspace_id,
                "gatewayId": gateway_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AiGatewayDeleteResponse,
                    parse_obj_as(
                        type_=AiGatewayDeleteResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorBadRequest,
                        parse_obj_as(
                            type_=ErrorBadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorUnauthorized,
                        parse_obj_as(
                            type_=ErrorUnauthorized,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorForbidden,
                        parse_obj_as(
                            type_=ErrorForbidden,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorNotFound,
                        parse_obj_as(
                            type_=ErrorNotFound,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorInternalServerError,
                        parse_obj_as(
                            type_=ErrorInternalServerError,
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

    def ai_gateway_logs(
        self,
        *,
        workspace_id: str,
        gateway_id: str,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        log_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AiGatewayLogsResponse]:
        """
        Parameters
        ----------
        workspace_id : str

        gateway_id : str

        cursor : typing.Optional[str]

        limit : typing.Optional[int]

        log_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AiGatewayLogsResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "aiGateway/logs",
            method="GET",
            params={
                "workspaceId": workspace_id,
                "gatewayId": gateway_id,
                "cursor": cursor,
                "limit": limit,
                "logId": log_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AiGatewayLogsResponse,
                    parse_obj_as(
                        type_=AiGatewayLogsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorBadRequest,
                        parse_obj_as(
                            type_=ErrorBadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorUnauthorized,
                        parse_obj_as(
                            type_=ErrorUnauthorized,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorForbidden,
                        parse_obj_as(
                            type_=ErrorForbidden,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorNotFound,
                        parse_obj_as(
                            type_=ErrorNotFound,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorInternalServerError,
                        parse_obj_as(
                            type_=ErrorInternalServerError,
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

    def ai_gateway_model_pricing(
        self,
        *,
        workspace_id: str,
        search: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AiGatewayModelPricingResponse]:
        """
        Parameters
        ----------
        workspace_id : str

        search : typing.Optional[str]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AiGatewayModelPricingResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "aiGateway/model-pricing",
            method="GET",
            params={
                "workspaceId": workspace_id,
                "search": search,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AiGatewayModelPricingResponse,
                    parse_obj_as(
                        type_=AiGatewayModelPricingResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorBadRequest,
                        parse_obj_as(
                            type_=ErrorBadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorUnauthorized,
                        parse_obj_as(
                            type_=ErrorUnauthorized,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorForbidden,
                        parse_obj_as(
                            type_=ErrorForbidden,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorNotFound,
                        parse_obj_as(
                            type_=ErrorNotFound,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorInternalServerError,
                        parse_obj_as(
                            type_=ErrorInternalServerError,
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

    def ai_gateway_quota_alert_get(
        self, *, workspace_id: str, gateway_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[AiGatewayQuotaAlertGetResponse]]:
        """
        Parameters
        ----------
        workspace_id : str

        gateway_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[AiGatewayQuotaAlertGetResponse]]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "aiGateway/quota-alert",
            method="GET",
            params={
                "workspaceId": workspace_id,
                "gatewayId": gateway_id,
            },
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[AiGatewayQuotaAlertGetResponse],
                    parse_obj_as(
                        type_=typing.Optional[AiGatewayQuotaAlertGetResponse],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorBadRequest,
                        parse_obj_as(
                            type_=ErrorBadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorUnauthorized,
                        parse_obj_as(
                            type_=ErrorUnauthorized,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorForbidden,
                        parse_obj_as(
                            type_=ErrorForbidden,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorNotFound,
                        parse_obj_as(
                            type_=ErrorNotFound,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorInternalServerError,
                        parse_obj_as(
                            type_=ErrorInternalServerError,
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

    def ai_gateway_quota_alert_upsert(
        self,
        *,
        workspace_id: str,
        gateway_id: str,
        daily_quota: float,
        enabled: bool,
        notification_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AiGatewayQuotaAlertUpsertResponse]:
        """
        Parameters
        ----------
        workspace_id : str

        gateway_id : str

        daily_quota : float

        enabled : bool

        notification_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AiGatewayQuotaAlertUpsertResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "aiGateway/quota-alert/upsert",
            method="POST",
            json={
                "workspaceId": workspace_id,
                "gatewayId": gateway_id,
                "dailyQuota": daily_quota,
                "enabled": enabled,
                "notificationId": notification_id,
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
                    AiGatewayQuotaAlertUpsertResponse,
                    parse_obj_as(
                        type_=AiGatewayQuotaAlertUpsertResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorBadRequest,
                        parse_obj_as(
                            type_=ErrorBadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorUnauthorized,
                        parse_obj_as(
                            type_=ErrorUnauthorized,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorForbidden,
                        parse_obj_as(
                            type_=ErrorForbidden,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorInternalServerError,
                        parse_obj_as(
                            type_=ErrorInternalServerError,
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

    def ai_gateway_quota_alert_delete(
        self, *, workspace_id: str, gateway_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[bool]:
        """
        Parameters
        ----------
        workspace_id : str

        gateway_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[bool]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "aiGateway/quota-alert/delete",
            method="DELETE",
            params={
                "workspaceId": workspace_id,
                "gatewayId": gateway_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorBadRequest,
                        parse_obj_as(
                            type_=ErrorBadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorUnauthorized,
                        parse_obj_as(
                            type_=ErrorUnauthorized,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorForbidden,
                        parse_obj_as(
                            type_=ErrorForbidden,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorNotFound,
                        parse_obj_as(
                            type_=ErrorNotFound,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorInternalServerError,
                        parse_obj_as(
                            type_=ErrorInternalServerError,
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


class AsyncRawAiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def classifysurvey(
        self,
        *,
        workspace_id: str,
        survey_id: str,
        start_at: float,
        end_at: float,
        run_strategy: AiClassifySurveyRequestRunStrategy,
        payload_content_field: str,
        suggestion_category: typing.Sequence[str],
        language_strategy: typing.Optional[AiClassifySurveyRequestLanguageStrategy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AiClassifySurveyResponse]:
        """
        classify survey

        Parameters
        ----------
        workspace_id : str

        survey_id : str

        start_at : float

        end_at : float

        run_strategy : AiClassifySurveyRequestRunStrategy

        payload_content_field : str

        suggestion_category : typing.Sequence[str]

        language_strategy : typing.Optional[AiClassifySurveyRequestLanguageStrategy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AiClassifySurveyResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "ai/classifySurvey",
            method="POST",
            json={
                "workspaceId": workspace_id,
                "surveyId": survey_id,
                "startAt": start_at,
                "endAt": end_at,
                "runStrategy": run_strategy,
                "languageStrategy": language_strategy,
                "payloadContentField": payload_content_field,
                "suggestionCategory": suggestion_category,
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
                    AiClassifySurveyResponse,
                    parse_obj_as(
                        type_=AiClassifySurveyResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorBadRequest,
                        parse_obj_as(
                            type_=ErrorBadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorUnauthorized,
                        parse_obj_as(
                            type_=ErrorUnauthorized,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorForbidden,
                        parse_obj_as(
                            type_=ErrorForbidden,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorInternalServerError,
                        parse_obj_as(
                            type_=ErrorInternalServerError,
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

    async def translatesurvey(
        self,
        *,
        workspace_id: str,
        survey_id: str,
        start_at: float,
        end_at: float,
        run_strategy: AiTranslateSurveyRequestRunStrategy,
        payload_content_field: str,
        language_strategy: typing.Optional[AiTranslateSurveyRequestLanguageStrategy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AiTranslateSurveyResponse]:
        """
        translate survey

        Parameters
        ----------
        workspace_id : str

        survey_id : str

        start_at : float

        end_at : float

        run_strategy : AiTranslateSurveyRequestRunStrategy

        payload_content_field : str

        language_strategy : typing.Optional[AiTranslateSurveyRequestLanguageStrategy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AiTranslateSurveyResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "ai/translateSurvey",
            method="POST",
            json={
                "workspaceId": workspace_id,
                "surveyId": survey_id,
                "startAt": start_at,
                "endAt": end_at,
                "runStrategy": run_strategy,
                "languageStrategy": language_strategy,
                "payloadContentField": payload_content_field,
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
                    AiTranslateSurveyResponse,
                    parse_obj_as(
                        type_=AiTranslateSurveyResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorBadRequest,
                        parse_obj_as(
                            type_=ErrorBadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorUnauthorized,
                        parse_obj_as(
                            type_=ErrorUnauthorized,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorForbidden,
                        parse_obj_as(
                            type_=ErrorForbidden,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorInternalServerError,
                        parse_obj_as(
                            type_=ErrorInternalServerError,
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

    async def ai_gateway_info(
        self, *, workspace_id: str, gateway_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[AiGatewayInfoResponse]]:
        """
        Parameters
        ----------
        workspace_id : str

        gateway_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[AiGatewayInfoResponse]]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "aiGateway/info",
            method="GET",
            params={
                "workspaceId": workspace_id,
                "gatewayId": gateway_id,
            },
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[AiGatewayInfoResponse],
                    parse_obj_as(
                        type_=typing.Optional[AiGatewayInfoResponse],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorBadRequest,
                        parse_obj_as(
                            type_=ErrorBadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorUnauthorized,
                        parse_obj_as(
                            type_=ErrorUnauthorized,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorForbidden,
                        parse_obj_as(
                            type_=ErrorForbidden,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorNotFound,
                        parse_obj_as(
                            type_=ErrorNotFound,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorInternalServerError,
                        parse_obj_as(
                            type_=ErrorInternalServerError,
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

    async def ai_gateway_update(
        self,
        *,
        workspace_id: str,
        gateway_id: str,
        name: str,
        model_api_key: typing.Optional[str] = OMIT,
        custom_model_base_url: typing.Optional[str] = OMIT,
        custom_model_name: typing.Optional[str] = OMIT,
        custom_model_input_price: typing.Optional[float] = OMIT,
        custom_model_output_price: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AiGatewayUpdateResponse]:
        """
        Parameters
        ----------
        workspace_id : str

        gateway_id : str

        name : str

        model_api_key : typing.Optional[str]

        custom_model_base_url : typing.Optional[str]

        custom_model_name : typing.Optional[str]

        custom_model_input_price : typing.Optional[float]

        custom_model_output_price : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AiGatewayUpdateResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "aiGateway/update",
            method="PATCH",
            json={
                "workspaceId": workspace_id,
                "gatewayId": gateway_id,
                "name": name,
                "modelApiKey": model_api_key,
                "customModelBaseUrl": custom_model_base_url,
                "customModelName": custom_model_name,
                "customModelInputPrice": custom_model_input_price,
                "customModelOutputPrice": custom_model_output_price,
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
                    AiGatewayUpdateResponse,
                    parse_obj_as(
                        type_=AiGatewayUpdateResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorBadRequest,
                        parse_obj_as(
                            type_=ErrorBadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorUnauthorized,
                        parse_obj_as(
                            type_=ErrorUnauthorized,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorForbidden,
                        parse_obj_as(
                            type_=ErrorForbidden,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorNotFound,
                        parse_obj_as(
                            type_=ErrorNotFound,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorInternalServerError,
                        parse_obj_as(
                            type_=ErrorInternalServerError,
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

    async def ai_gateway_delete(
        self, *, workspace_id: str, gateway_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[AiGatewayDeleteResponse]:
        """
        Parameters
        ----------
        workspace_id : str

        gateway_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AiGatewayDeleteResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "aiGateway/delete",
            method="DELETE",
            params={
                "workspaceId": workspace_id,
                "gatewayId": gateway_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AiGatewayDeleteResponse,
                    parse_obj_as(
                        type_=AiGatewayDeleteResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorBadRequest,
                        parse_obj_as(
                            type_=ErrorBadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorUnauthorized,
                        parse_obj_as(
                            type_=ErrorUnauthorized,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorForbidden,
                        parse_obj_as(
                            type_=ErrorForbidden,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorNotFound,
                        parse_obj_as(
                            type_=ErrorNotFound,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorInternalServerError,
                        parse_obj_as(
                            type_=ErrorInternalServerError,
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

    async def ai_gateway_logs(
        self,
        *,
        workspace_id: str,
        gateway_id: str,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        log_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AiGatewayLogsResponse]:
        """
        Parameters
        ----------
        workspace_id : str

        gateway_id : str

        cursor : typing.Optional[str]

        limit : typing.Optional[int]

        log_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AiGatewayLogsResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "aiGateway/logs",
            method="GET",
            params={
                "workspaceId": workspace_id,
                "gatewayId": gateway_id,
                "cursor": cursor,
                "limit": limit,
                "logId": log_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AiGatewayLogsResponse,
                    parse_obj_as(
                        type_=AiGatewayLogsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorBadRequest,
                        parse_obj_as(
                            type_=ErrorBadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorUnauthorized,
                        parse_obj_as(
                            type_=ErrorUnauthorized,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorForbidden,
                        parse_obj_as(
                            type_=ErrorForbidden,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorNotFound,
                        parse_obj_as(
                            type_=ErrorNotFound,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorInternalServerError,
                        parse_obj_as(
                            type_=ErrorInternalServerError,
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

    async def ai_gateway_model_pricing(
        self,
        *,
        workspace_id: str,
        search: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AiGatewayModelPricingResponse]:
        """
        Parameters
        ----------
        workspace_id : str

        search : typing.Optional[str]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AiGatewayModelPricingResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "aiGateway/model-pricing",
            method="GET",
            params={
                "workspaceId": workspace_id,
                "search": search,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AiGatewayModelPricingResponse,
                    parse_obj_as(
                        type_=AiGatewayModelPricingResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorBadRequest,
                        parse_obj_as(
                            type_=ErrorBadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorUnauthorized,
                        parse_obj_as(
                            type_=ErrorUnauthorized,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorForbidden,
                        parse_obj_as(
                            type_=ErrorForbidden,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorNotFound,
                        parse_obj_as(
                            type_=ErrorNotFound,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorInternalServerError,
                        parse_obj_as(
                            type_=ErrorInternalServerError,
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

    async def ai_gateway_quota_alert_get(
        self, *, workspace_id: str, gateway_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[AiGatewayQuotaAlertGetResponse]]:
        """
        Parameters
        ----------
        workspace_id : str

        gateway_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[AiGatewayQuotaAlertGetResponse]]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "aiGateway/quota-alert",
            method="GET",
            params={
                "workspaceId": workspace_id,
                "gatewayId": gateway_id,
            },
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[AiGatewayQuotaAlertGetResponse],
                    parse_obj_as(
                        type_=typing.Optional[AiGatewayQuotaAlertGetResponse],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorBadRequest,
                        parse_obj_as(
                            type_=ErrorBadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorUnauthorized,
                        parse_obj_as(
                            type_=ErrorUnauthorized,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorForbidden,
                        parse_obj_as(
                            type_=ErrorForbidden,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorNotFound,
                        parse_obj_as(
                            type_=ErrorNotFound,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorInternalServerError,
                        parse_obj_as(
                            type_=ErrorInternalServerError,
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

    async def ai_gateway_quota_alert_upsert(
        self,
        *,
        workspace_id: str,
        gateway_id: str,
        daily_quota: float,
        enabled: bool,
        notification_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AiGatewayQuotaAlertUpsertResponse]:
        """
        Parameters
        ----------
        workspace_id : str

        gateway_id : str

        daily_quota : float

        enabled : bool

        notification_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AiGatewayQuotaAlertUpsertResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "aiGateway/quota-alert/upsert",
            method="POST",
            json={
                "workspaceId": workspace_id,
                "gatewayId": gateway_id,
                "dailyQuota": daily_quota,
                "enabled": enabled,
                "notificationId": notification_id,
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
                    AiGatewayQuotaAlertUpsertResponse,
                    parse_obj_as(
                        type_=AiGatewayQuotaAlertUpsertResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorBadRequest,
                        parse_obj_as(
                            type_=ErrorBadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorUnauthorized,
                        parse_obj_as(
                            type_=ErrorUnauthorized,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorForbidden,
                        parse_obj_as(
                            type_=ErrorForbidden,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorInternalServerError,
                        parse_obj_as(
                            type_=ErrorInternalServerError,
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

    async def ai_gateway_quota_alert_delete(
        self, *, workspace_id: str, gateway_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[bool]:
        """
        Parameters
        ----------
        workspace_id : str

        gateway_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[bool]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "aiGateway/quota-alert/delete",
            method="DELETE",
            params={
                "workspaceId": workspace_id,
                "gatewayId": gateway_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorBadRequest,
                        parse_obj_as(
                            type_=ErrorBadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorUnauthorized,
                        parse_obj_as(
                            type_=ErrorUnauthorized,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorForbidden,
                        parse_obj_as(
                            type_=ErrorForbidden,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorNotFound,
                        parse_obj_as(
                            type_=ErrorNotFound,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorInternalServerError,
                        parse_obj_as(
                            type_=ErrorInternalServerError,
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

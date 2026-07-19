

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.content_too_large_error import ContentTooLargeError
from ..errors.internal_server_error import InternalServerError
from ..errors.length_required_error import LengthRequiredError
from ..errors.service_unavailable_error import ServiceUnavailableError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unsupported_media_type_error import UnsupportedMediaTypeError
from ..types.n1message_class import N1MessageClass
from ..types.n2information_class import N2InformationClass
from ..types.problem_details import ProblemDetails
from ..types.ue_n1n2info_subscription_created_data import UeN1N2InfoSubscriptionCreatedData
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawN1N2SubscriptionsCollectionForIndividualUeContextsDocumentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def n1n2message_subscribe(
        self,
        ue_context_id: str,
        *,
        n2information_class: typing.Optional[N2InformationClass] = OMIT,
        n2notify_callback_uri: typing.Optional[str] = OMIT,
        n1message_class: typing.Optional[N1MessageClass] = OMIT,
        n1notify_callback_uri: typing.Optional[str] = OMIT,
        nf_id: typing.Optional[str] = OMIT,
        supported_features: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UeN1N2InfoSubscriptionCreatedData]:
        """
        Parameters
        ----------
        ue_context_id : str
            UE Context Identifier

        n2information_class : typing.Optional[N2InformationClass]

        n2notify_callback_uri : typing.Optional[str]

        n1message_class : typing.Optional[N1MessageClass]

        n1notify_callback_uri : typing.Optional[str]

        nf_id : typing.Optional[str]

        supported_features : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UeN1N2InfoSubscriptionCreatedData]
            N1N2 Message Subscription successfully created.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"ue-contexts/{encode_path_param(ue_context_id)}/n1-n2-messages/subscriptions",
            method="POST",
            json={
                "n2InformationClass": n2information_class,
                "n2NotifyCallbackUri": n2notify_callback_uri,
                "n1MessageClass": n1message_class,
                "n1NotifyCallbackUri": n1notify_callback_uri,
                "nfId": nf_id,
                "supportedFeatures": supported_features,
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
                    UeN1N2InfoSubscriptionCreatedData,
                    parse_obj_as(
                        type_=UeN1N2InfoSubscriptionCreatedData,
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
            if _response.status_code == 411:
                raise LengthRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProblemDetails,
                        parse_obj_as(
                            type_=ProblemDetails,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProblemDetails,
                        parse_obj_as(
                            type_=ProblemDetails,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProblemDetails,
                        parse_obj_as(
                            type_=ProblemDetails,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProblemDetails,
                        parse_obj_as(
                            type_=ProblemDetails,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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


class AsyncRawN1N2SubscriptionsCollectionForIndividualUeContextsDocumentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def n1n2message_subscribe(
        self,
        ue_context_id: str,
        *,
        n2information_class: typing.Optional[N2InformationClass] = OMIT,
        n2notify_callback_uri: typing.Optional[str] = OMIT,
        n1message_class: typing.Optional[N1MessageClass] = OMIT,
        n1notify_callback_uri: typing.Optional[str] = OMIT,
        nf_id: typing.Optional[str] = OMIT,
        supported_features: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UeN1N2InfoSubscriptionCreatedData]:
        """
        Parameters
        ----------
        ue_context_id : str
            UE Context Identifier

        n2information_class : typing.Optional[N2InformationClass]

        n2notify_callback_uri : typing.Optional[str]

        n1message_class : typing.Optional[N1MessageClass]

        n1notify_callback_uri : typing.Optional[str]

        nf_id : typing.Optional[str]

        supported_features : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UeN1N2InfoSubscriptionCreatedData]
            N1N2 Message Subscription successfully created.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ue-contexts/{encode_path_param(ue_context_id)}/n1-n2-messages/subscriptions",
            method="POST",
            json={
                "n2InformationClass": n2information_class,
                "n2NotifyCallbackUri": n2notify_callback_uri,
                "n1MessageClass": n1message_class,
                "n1NotifyCallbackUri": n1notify_callback_uri,
                "nfId": nf_id,
                "supportedFeatures": supported_features,
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
                    UeN1N2InfoSubscriptionCreatedData,
                    parse_obj_as(
                        type_=UeN1N2InfoSubscriptionCreatedData,
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
            if _response.status_code == 411:
                raise LengthRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProblemDetails,
                        parse_obj_as(
                            type_=ProblemDetails,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProblemDetails,
                        parse_obj_as(
                            type_=ProblemDetails,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProblemDetails,
                        parse_obj_as(
                            type_=ProblemDetails,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProblemDetails,
                        parse_obj_as(
                            type_=ProblemDetails,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

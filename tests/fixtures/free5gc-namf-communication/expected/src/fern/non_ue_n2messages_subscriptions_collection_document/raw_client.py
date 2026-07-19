

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.content_too_large_error import ContentTooLargeError
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from ..errors.length_required_error import LengthRequiredError
from ..errors.service_unavailable_error import ServiceUnavailableError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unsupported_media_type_error import UnsupportedMediaTypeError
from ..types.access_type import AccessType
from ..types.global_ran_node_id import GlobalRanNodeId
from ..types.n2information_class import N2InformationClass
from ..types.non_ue_n2info_subscription_created_data import NonUeN2InfoSubscriptionCreatedData
from ..types.problem_details import ProblemDetails
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawNonUeN2MessagesSubscriptionsCollectionDocumentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def non_ue_n2info_subscribe(
        self,
        *,
        n2information_class: N2InformationClass,
        n2notify_callback_uri: str,
        global_ran_node_list: typing.Optional[typing.Sequence[GlobalRanNodeId]] = OMIT,
        an_type_list: typing.Optional[typing.Sequence[AccessType]] = OMIT,
        nf_id: typing.Optional[str] = OMIT,
        supported_features: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NonUeN2InfoSubscriptionCreatedData]:
        """
        Parameters
        ----------
        n2information_class : N2InformationClass

        n2notify_callback_uri : str

        global_ran_node_list : typing.Optional[typing.Sequence[GlobalRanNodeId]]

        an_type_list : typing.Optional[typing.Sequence[AccessType]]

        nf_id : typing.Optional[str]

        supported_features : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[NonUeN2InfoSubscriptionCreatedData]
            Non UE N2 Info Subscription successfully created.
        """
        _response = self._client_wrapper.httpx_client.request(
            "non-ue-n2-messages/subscriptions",
            method="POST",
            json={
                "globalRanNodeList": convert_and_respect_annotation_metadata(
                    object_=global_ran_node_list, annotation=typing.Sequence[GlobalRanNodeId], direction="write"
                ),
                "anTypeList": an_type_list,
                "n2InformationClass": n2information_class,
                "n2NotifyCallbackUri": n2notify_callback_uri,
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
                    NonUeN2InfoSubscriptionCreatedData,
                    parse_obj_as(
                        type_=NonUeN2InfoSubscriptionCreatedData,
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


class AsyncRawNonUeN2MessagesSubscriptionsCollectionDocumentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def non_ue_n2info_subscribe(
        self,
        *,
        n2information_class: N2InformationClass,
        n2notify_callback_uri: str,
        global_ran_node_list: typing.Optional[typing.Sequence[GlobalRanNodeId]] = OMIT,
        an_type_list: typing.Optional[typing.Sequence[AccessType]] = OMIT,
        nf_id: typing.Optional[str] = OMIT,
        supported_features: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NonUeN2InfoSubscriptionCreatedData]:
        """
        Parameters
        ----------
        n2information_class : N2InformationClass

        n2notify_callback_uri : str

        global_ran_node_list : typing.Optional[typing.Sequence[GlobalRanNodeId]]

        an_type_list : typing.Optional[typing.Sequence[AccessType]]

        nf_id : typing.Optional[str]

        supported_features : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[NonUeN2InfoSubscriptionCreatedData]
            Non UE N2 Info Subscription successfully created.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "non-ue-n2-messages/subscriptions",
            method="POST",
            json={
                "globalRanNodeList": convert_and_respect_annotation_metadata(
                    object_=global_ran_node_list, annotation=typing.Sequence[GlobalRanNodeId], direction="write"
                ),
                "anTypeList": an_type_list,
                "n2InformationClass": n2information_class,
                "n2NotifyCallbackUri": n2notify_callback_uri,
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
                    NonUeN2InfoSubscriptionCreatedData,
                    parse_obj_as(
                        type_=NonUeN2InfoSubscriptionCreatedData,
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

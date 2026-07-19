

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
from ..errors.not_found_error import NotFoundError
from ..errors.service_unavailable_error import ServiceUnavailableError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unsupported_media_type_error import UnsupportedMediaTypeError
from ..types.ecgi import Ecgi
from ..types.global_ran_node_id import GlobalRanNodeId
from ..types.n2info_container import N2InfoContainer
from ..types.n2information_transfer_rsp_data import N2InformationTransferRspData
from ..types.ncgi import Ncgi
from ..types.problem_details import ProblemDetails
from ..types.rat_selector import RatSelector
from ..types.tai import Tai
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawNonUeN2MessagesCollectionDocumentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def non_ue_n2message_transfer(
        self,
        *,
        n2information: N2InfoContainer,
        tai_list: typing.Optional[typing.Sequence[Tai]] = OMIT,
        rat_selector: typing.Optional[RatSelector] = OMIT,
        ecgi_list: typing.Optional[typing.Sequence[Ecgi]] = OMIT,
        ncgi_list: typing.Optional[typing.Sequence[Ncgi]] = OMIT,
        global_ran_node_list: typing.Optional[typing.Sequence[GlobalRanNodeId]] = OMIT,
        supported_features: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[N2InformationTransferRspData]:
        """
        Parameters
        ----------
        n2information : N2InfoContainer

        tai_list : typing.Optional[typing.Sequence[Tai]]

        rat_selector : typing.Optional[RatSelector]

        ecgi_list : typing.Optional[typing.Sequence[Ecgi]]

        ncgi_list : typing.Optional[typing.Sequence[Ncgi]]

        global_ran_node_list : typing.Optional[typing.Sequence[GlobalRanNodeId]]

        supported_features : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[N2InformationTransferRspData]
            Non UE N2 Message Transfer successfully initiated.
        """
        _response = self._client_wrapper.httpx_client.request(
            "non-ue-n2-messages/transfer",
            method="POST",
            json={
                "taiList": convert_and_respect_annotation_metadata(
                    object_=tai_list, annotation=typing.Sequence[Tai], direction="write"
                ),
                "ratSelector": rat_selector,
                "ecgiList": convert_and_respect_annotation_metadata(
                    object_=ecgi_list, annotation=typing.Sequence[Ecgi], direction="write"
                ),
                "ncgiList": convert_and_respect_annotation_metadata(
                    object_=ncgi_list, annotation=typing.Sequence[Ncgi], direction="write"
                ),
                "globalRanNodeList": convert_and_respect_annotation_metadata(
                    object_=global_ran_node_list, annotation=typing.Sequence[GlobalRanNodeId], direction="write"
                ),
                "n2Information": convert_and_respect_annotation_metadata(
                    object_=n2information, annotation=N2InfoContainer, direction="write"
                ),
                "supportedFeatures": supported_features,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    N2InformationTransferRspData,
                    parse_obj_as(
                        type_=N2InformationTransferRspData,
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


class AsyncRawNonUeN2MessagesCollectionDocumentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def non_ue_n2message_transfer(
        self,
        *,
        n2information: N2InfoContainer,
        tai_list: typing.Optional[typing.Sequence[Tai]] = OMIT,
        rat_selector: typing.Optional[RatSelector] = OMIT,
        ecgi_list: typing.Optional[typing.Sequence[Ecgi]] = OMIT,
        ncgi_list: typing.Optional[typing.Sequence[Ncgi]] = OMIT,
        global_ran_node_list: typing.Optional[typing.Sequence[GlobalRanNodeId]] = OMIT,
        supported_features: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[N2InformationTransferRspData]:
        """
        Parameters
        ----------
        n2information : N2InfoContainer

        tai_list : typing.Optional[typing.Sequence[Tai]]

        rat_selector : typing.Optional[RatSelector]

        ecgi_list : typing.Optional[typing.Sequence[Ecgi]]

        ncgi_list : typing.Optional[typing.Sequence[Ncgi]]

        global_ran_node_list : typing.Optional[typing.Sequence[GlobalRanNodeId]]

        supported_features : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[N2InformationTransferRspData]
            Non UE N2 Message Transfer successfully initiated.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "non-ue-n2-messages/transfer",
            method="POST",
            json={
                "taiList": convert_and_respect_annotation_metadata(
                    object_=tai_list, annotation=typing.Sequence[Tai], direction="write"
                ),
                "ratSelector": rat_selector,
                "ecgiList": convert_and_respect_annotation_metadata(
                    object_=ecgi_list, annotation=typing.Sequence[Ecgi], direction="write"
                ),
                "ncgiList": convert_and_respect_annotation_metadata(
                    object_=ncgi_list, annotation=typing.Sequence[Ncgi], direction="write"
                ),
                "globalRanNodeList": convert_and_respect_annotation_metadata(
                    object_=global_ran_node_list, annotation=typing.Sequence[GlobalRanNodeId], direction="write"
                ),
                "n2Information": convert_and_respect_annotation_metadata(
                    object_=n2information, annotation=N2InfoContainer, direction="write"
                ),
                "supportedFeatures": supported_features,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    N2InformationTransferRspData,
                    parse_obj_as(
                        type_=N2InformationTransferRspData,
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

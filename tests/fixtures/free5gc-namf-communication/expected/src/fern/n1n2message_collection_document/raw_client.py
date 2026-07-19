

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
from ..errors.content_too_large_error import ContentTooLargeError
from ..errors.forbidden_error import ForbiddenError
from ..errors.gateway_timeout_error import GatewayTimeoutError
from ..errors.internal_server_error import InternalServerError
from ..errors.length_required_error import LengthRequiredError
from ..errors.not_found_error import NotFoundError
from ..errors.service_unavailable_error import ServiceUnavailableError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unsupported_media_type_error import UnsupportedMediaTypeError
from ..types.area_of_validity import AreaOfValidity
from ..types.arp import Arp
from ..types.n1message_container import N1MessageContainer
from ..types.n1n2message_transfer_error import N1N2MessageTransferError
from ..types.n1n2message_transfer_rsp_data import N1N2MessageTransferRspData
from ..types.n2info_container import N2InfoContainer
from ..types.problem_details import ProblemDetails
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawN1N2MessageCollectionDocumentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def n1n2message_transfer(
        self,
        ue_context_id: str,
        *,
        n1message_container: typing.Optional[N1MessageContainer] = OMIT,
        n2info_container: typing.Optional[N2InfoContainer] = OMIT,
        skip_ind: typing.Optional[bool] = OMIT,
        last_msg_indication: typing.Optional[bool] = OMIT,
        pdu_session_id: typing.Optional[int] = OMIT,
        lcs_correlation_id: typing.Optional[str] = OMIT,
        ppi: typing.Optional[int] = OMIT,
        arp: typing.Optional[Arp] = OMIT,
        _5qi: typing.Optional[int] = OMIT,
        n1n2failure_txf_notif_uri: typing.Optional[str] = OMIT,
        smf_reallocation_ind: typing.Optional[bool] = OMIT,
        area_of_validity: typing.Optional[AreaOfValidity] = OMIT,
        supported_features: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[N1N2MessageTransferRspData]:
        """
        Parameters
        ----------
        ue_context_id : str
            UE Context Identifier

        n1message_container : typing.Optional[N1MessageContainer]

        n2info_container : typing.Optional[N2InfoContainer]

        skip_ind : typing.Optional[bool]

        last_msg_indication : typing.Optional[bool]

        pdu_session_id : typing.Optional[int]

        lcs_correlation_id : typing.Optional[str]

        ppi : typing.Optional[int]

        arp : typing.Optional[Arp]

        _5qi : typing.Optional[int]

        n1n2failure_txf_notif_uri : typing.Optional[str]

        smf_reallocation_ind : typing.Optional[bool]

        area_of_validity : typing.Optional[AreaOfValidity]

        supported_features : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[N1N2MessageTransferRspData]
            N1N2 Message Transfer successfully initiated.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"ue-contexts/{encode_path_param(ue_context_id)}/n1-n2-messages",
            method="POST",
            json={
                "n1MessageContainer": convert_and_respect_annotation_metadata(
                    object_=n1message_container, annotation=N1MessageContainer, direction="write"
                ),
                "n2InfoContainer": convert_and_respect_annotation_metadata(
                    object_=n2info_container, annotation=N2InfoContainer, direction="write"
                ),
                "skipInd": skip_ind,
                "lastMsgIndication": last_msg_indication,
                "pduSessionId": pdu_session_id,
                "lcsCorrelationId": lcs_correlation_id,
                "ppi": ppi,
                "arp": convert_and_respect_annotation_metadata(object_=arp, annotation=Arp, direction="write"),
                "5qi": _5qi,
                "n1n2FailureTxfNotifURI": n1n2failure_txf_notif_uri,
                "smfReallocationInd": smf_reallocation_ind,
                "areaOfValidity": convert_and_respect_annotation_metadata(
                    object_=area_of_validity, annotation=AreaOfValidity, direction="write"
                ),
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
                    N1N2MessageTransferRspData,
                    parse_obj_as(
                        type_=N1N2MessageTransferRspData,
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
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        N1N2MessageTransferError,
                        parse_obj_as(
                            type_=N1N2MessageTransferError,
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
            if _response.status_code == 504:
                raise GatewayTimeoutError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        N1N2MessageTransferError,
                        parse_obj_as(
                            type_=N1N2MessageTransferError,
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


class AsyncRawN1N2MessageCollectionDocumentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def n1n2message_transfer(
        self,
        ue_context_id: str,
        *,
        n1message_container: typing.Optional[N1MessageContainer] = OMIT,
        n2info_container: typing.Optional[N2InfoContainer] = OMIT,
        skip_ind: typing.Optional[bool] = OMIT,
        last_msg_indication: typing.Optional[bool] = OMIT,
        pdu_session_id: typing.Optional[int] = OMIT,
        lcs_correlation_id: typing.Optional[str] = OMIT,
        ppi: typing.Optional[int] = OMIT,
        arp: typing.Optional[Arp] = OMIT,
        _5qi: typing.Optional[int] = OMIT,
        n1n2failure_txf_notif_uri: typing.Optional[str] = OMIT,
        smf_reallocation_ind: typing.Optional[bool] = OMIT,
        area_of_validity: typing.Optional[AreaOfValidity] = OMIT,
        supported_features: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[N1N2MessageTransferRspData]:
        """
        Parameters
        ----------
        ue_context_id : str
            UE Context Identifier

        n1message_container : typing.Optional[N1MessageContainer]

        n2info_container : typing.Optional[N2InfoContainer]

        skip_ind : typing.Optional[bool]

        last_msg_indication : typing.Optional[bool]

        pdu_session_id : typing.Optional[int]

        lcs_correlation_id : typing.Optional[str]

        ppi : typing.Optional[int]

        arp : typing.Optional[Arp]

        _5qi : typing.Optional[int]

        n1n2failure_txf_notif_uri : typing.Optional[str]

        smf_reallocation_ind : typing.Optional[bool]

        area_of_validity : typing.Optional[AreaOfValidity]

        supported_features : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[N1N2MessageTransferRspData]
            N1N2 Message Transfer successfully initiated.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ue-contexts/{encode_path_param(ue_context_id)}/n1-n2-messages",
            method="POST",
            json={
                "n1MessageContainer": convert_and_respect_annotation_metadata(
                    object_=n1message_container, annotation=N1MessageContainer, direction="write"
                ),
                "n2InfoContainer": convert_and_respect_annotation_metadata(
                    object_=n2info_container, annotation=N2InfoContainer, direction="write"
                ),
                "skipInd": skip_ind,
                "lastMsgIndication": last_msg_indication,
                "pduSessionId": pdu_session_id,
                "lcsCorrelationId": lcs_correlation_id,
                "ppi": ppi,
                "arp": convert_and_respect_annotation_metadata(object_=arp, annotation=Arp, direction="write"),
                "5qi": _5qi,
                "n1n2FailureTxfNotifURI": n1n2failure_txf_notif_uri,
                "smfReallocationInd": smf_reallocation_ind,
                "areaOfValidity": convert_and_respect_annotation_metadata(
                    object_=area_of_validity, annotation=AreaOfValidity, direction="write"
                ),
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
                    N1N2MessageTransferRspData,
                    parse_obj_as(
                        type_=N1N2MessageTransferRspData,
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
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        N1N2MessageTransferError,
                        parse_obj_as(
                            type_=N1N2MessageTransferError,
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
            if _response.status_code == 504:
                raise GatewayTimeoutError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        N1N2MessageTransferError,
                        parse_obj_as(
                            type_=N1N2MessageTransferError,
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

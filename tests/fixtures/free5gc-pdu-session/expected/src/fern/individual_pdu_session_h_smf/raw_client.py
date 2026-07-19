

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
from ..errors.content_too_large_error import ContentTooLargeError
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from ..errors.length_required_error import LengthRequiredError
from ..errors.not_found_error import NotFoundError
from ..errors.service_unavailable_error import ServiceUnavailableError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unsupported_media_type_error import UnsupportedMediaTypeError
from ..types.access_type import AccessType
from ..types.cause import Cause
from ..types.eps_bearer_id import EpsBearerId
from ..types.eps_interworking_indication import EpsInterworkingIndication
from ..types.hsmf_updated_data import HsmfUpdatedData
from ..types.ng_ap_cause import NgApCause
from ..types.pdu_session_notify_item import PduSessionNotifyItem
from ..types.plmn_id import PlmnId
from ..types.problem_details import ProblemDetails
from ..types.qos_flow_item import QosFlowItem
from ..types.qos_flow_notify_item import QosFlowNotifyItem
from ..types.rat_type import RatType
from ..types.ref_to_binary_data import RefToBinaryData
from ..types.request_indication import RequestIndication
from ..types.secondary_rat_usage_report import SecondaryRatUsageReport
from ..types.tunnel_info import TunnelInfo
from ..types.user_location import UserLocation
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawIndividualPduSessionHSmfClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def update_pdu_session(
        self,
        pdu_session_ref: str,
        *,
        request_indication: RequestIndication,
        pei: typing.Optional[str] = OMIT,
        vcn_tunnel_info: typing.Optional[TunnelInfo] = OMIT,
        serving_network: typing.Optional[PlmnId] = OMIT,
        an_type: typing.Optional[AccessType] = OMIT,
        rat_type: typing.Optional[RatType] = OMIT,
        ue_location: typing.Optional[UserLocation] = OMIT,
        ue_time_zone: typing.Optional[str] = OMIT,
        add_ue_location: typing.Optional[UserLocation] = OMIT,
        pause_charging: typing.Optional[bool] = OMIT,
        pti: typing.Optional[int] = OMIT,
        n1sm_info_from_ue: typing.Optional[RefToBinaryData] = OMIT,
        unknown_n1sm_info: typing.Optional[RefToBinaryData] = OMIT,
        qos_flows_rel_notify_list: typing.Optional[typing.Sequence[QosFlowItem]] = OMIT,
        qos_flows_notify_list: typing.Optional[typing.Sequence[QosFlowNotifyItem]] = OMIT,
        notify_list: typing.Optional[typing.Sequence[PduSessionNotifyItem]] = OMIT,
        eps_bearer_id: typing.Optional[typing.Sequence[EpsBearerId]] = OMIT,
        ho_preparation_indication: typing.Optional[bool] = OMIT,
        revoke_ebi_list: typing.Optional[typing.Sequence[EpsBearerId]] = OMIT,
        cause: typing.Optional[Cause] = OMIT,
        ng_ap_cause: typing.Optional[NgApCause] = OMIT,
        _5g_mm_cause_value: typing.Optional[int] = OMIT,
        always_on_requested: typing.Optional[bool] = OMIT,
        eps_interworking_ind: typing.Optional[EpsInterworkingIndication] = OMIT,
        secondary_rat_usage_report: typing.Optional[typing.Sequence[SecondaryRatUsageReport]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Optional[HsmfUpdatedData]]:
        """
        Parameters
        ----------
        pdu_session_ref : str
            PDU session reference

        request_indication : RequestIndication

        pei : typing.Optional[str]

        vcn_tunnel_info : typing.Optional[TunnelInfo]

        serving_network : typing.Optional[PlmnId]

        an_type : typing.Optional[AccessType]

        rat_type : typing.Optional[RatType]

        ue_location : typing.Optional[UserLocation]

        ue_time_zone : typing.Optional[str]

        add_ue_location : typing.Optional[UserLocation]

        pause_charging : typing.Optional[bool]

        pti : typing.Optional[int]

        n1sm_info_from_ue : typing.Optional[RefToBinaryData]

        unknown_n1sm_info : typing.Optional[RefToBinaryData]

        qos_flows_rel_notify_list : typing.Optional[typing.Sequence[QosFlowItem]]

        qos_flows_notify_list : typing.Optional[typing.Sequence[QosFlowNotifyItem]]

        notify_list : typing.Optional[typing.Sequence[PduSessionNotifyItem]]

        eps_bearer_id : typing.Optional[typing.Sequence[EpsBearerId]]

        ho_preparation_indication : typing.Optional[bool]

        revoke_ebi_list : typing.Optional[typing.Sequence[EpsBearerId]]

        cause : typing.Optional[Cause]

        ng_ap_cause : typing.Optional[NgApCause]

        _5g_mm_cause_value : typing.Optional[int]

        always_on_requested : typing.Optional[bool]

        eps_interworking_ind : typing.Optional[EpsInterworkingIndication]

        secondary_rat_usage_report : typing.Optional[typing.Sequence[SecondaryRatUsageReport]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[HsmfUpdatedData]]
            successful update of a PDU session with content in the response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"pdu-sessions/{encode_path_param(pdu_session_ref)}/modify",
            method="POST",
            json={
                "requestIndication": request_indication,
                "pei": pei,
                "vcnTunnelInfo": convert_and_respect_annotation_metadata(
                    object_=vcn_tunnel_info, annotation=TunnelInfo, direction="write"
                ),
                "servingNetwork": convert_and_respect_annotation_metadata(
                    object_=serving_network, annotation=PlmnId, direction="write"
                ),
                "anType": an_type,
                "ratType": rat_type,
                "ueLocation": convert_and_respect_annotation_metadata(
                    object_=ue_location, annotation=UserLocation, direction="write"
                ),
                "ueTimeZone": ue_time_zone,
                "addUeLocation": convert_and_respect_annotation_metadata(
                    object_=add_ue_location, annotation=UserLocation, direction="write"
                ),
                "pauseCharging": pause_charging,
                "pti": pti,
                "n1SmInfoFromUe": convert_and_respect_annotation_metadata(
                    object_=n1sm_info_from_ue, annotation=RefToBinaryData, direction="write"
                ),
                "unknownN1SmInfo": convert_and_respect_annotation_metadata(
                    object_=unknown_n1sm_info, annotation=RefToBinaryData, direction="write"
                ),
                "qosFlowsRelNotifyList": convert_and_respect_annotation_metadata(
                    object_=qos_flows_rel_notify_list, annotation=typing.Sequence[QosFlowItem], direction="write"
                ),
                "qosFlowsNotifyList": convert_and_respect_annotation_metadata(
                    object_=qos_flows_notify_list, annotation=typing.Sequence[QosFlowNotifyItem], direction="write"
                ),
                "NotifyList": convert_and_respect_annotation_metadata(
                    object_=notify_list, annotation=typing.Sequence[PduSessionNotifyItem], direction="write"
                ),
                "epsBearerId": eps_bearer_id,
                "hoPreparationIndication": ho_preparation_indication,
                "revokeEbiList": revoke_ebi_list,
                "cause": cause,
                "ngApCause": convert_and_respect_annotation_metadata(
                    object_=ng_ap_cause, annotation=NgApCause, direction="write"
                ),
                "5gMmCauseValue": _5g_mm_cause_value,
                "alwaysOnRequested": always_on_requested,
                "epsInterworkingInd": eps_interworking_ind,
                "secondaryRatUsageReport": convert_and_respect_annotation_metadata(
                    object_=secondary_rat_usage_report,
                    annotation=typing.Sequence[SecondaryRatUsageReport],
                    direction="write",
                ),
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
                    typing.Optional[HsmfUpdatedData],
                    parse_obj_as(
                        type_=typing.Optional[HsmfUpdatedData],
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

    def release_pdu_session(
        self,
        pdu_session_ref: str,
        *,
        cause: typing.Optional[Cause] = OMIT,
        ng_ap_cause: typing.Optional[NgApCause] = OMIT,
        _5g_mm_cause_value: typing.Optional[int] = OMIT,
        ue_location: typing.Optional[UserLocation] = OMIT,
        ue_time_zone: typing.Optional[str] = OMIT,
        add_ue_location: typing.Optional[UserLocation] = OMIT,
        secondary_rat_usage_report: typing.Optional[typing.Sequence[SecondaryRatUsageReport]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        pdu_session_ref : str
            PDU session reference

        cause : typing.Optional[Cause]

        ng_ap_cause : typing.Optional[NgApCause]

        _5g_mm_cause_value : typing.Optional[int]

        ue_location : typing.Optional[UserLocation]

        ue_time_zone : typing.Optional[str]

        add_ue_location : typing.Optional[UserLocation]

        secondary_rat_usage_report : typing.Optional[typing.Sequence[SecondaryRatUsageReport]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"pdu-sessions/{encode_path_param(pdu_session_ref)}/release",
            method="POST",
            json={
                "cause": cause,
                "ngApCause": convert_and_respect_annotation_metadata(
                    object_=ng_ap_cause, annotation=NgApCause, direction="write"
                ),
                "5gMmCauseValue": _5g_mm_cause_value,
                "ueLocation": convert_and_respect_annotation_metadata(
                    object_=ue_location, annotation=UserLocation, direction="write"
                ),
                "ueTimeZone": ue_time_zone,
                "addUeLocation": convert_and_respect_annotation_metadata(
                    object_=add_ue_location, annotation=UserLocation, direction="write"
                ),
                "secondaryRatUsageReport": convert_and_respect_annotation_metadata(
                    object_=secondary_rat_usage_report,
                    annotation=typing.Sequence[SecondaryRatUsageReport],
                    direction="write",
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


class AsyncRawIndividualPduSessionHSmfClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def update_pdu_session(
        self,
        pdu_session_ref: str,
        *,
        request_indication: RequestIndication,
        pei: typing.Optional[str] = OMIT,
        vcn_tunnel_info: typing.Optional[TunnelInfo] = OMIT,
        serving_network: typing.Optional[PlmnId] = OMIT,
        an_type: typing.Optional[AccessType] = OMIT,
        rat_type: typing.Optional[RatType] = OMIT,
        ue_location: typing.Optional[UserLocation] = OMIT,
        ue_time_zone: typing.Optional[str] = OMIT,
        add_ue_location: typing.Optional[UserLocation] = OMIT,
        pause_charging: typing.Optional[bool] = OMIT,
        pti: typing.Optional[int] = OMIT,
        n1sm_info_from_ue: typing.Optional[RefToBinaryData] = OMIT,
        unknown_n1sm_info: typing.Optional[RefToBinaryData] = OMIT,
        qos_flows_rel_notify_list: typing.Optional[typing.Sequence[QosFlowItem]] = OMIT,
        qos_flows_notify_list: typing.Optional[typing.Sequence[QosFlowNotifyItem]] = OMIT,
        notify_list: typing.Optional[typing.Sequence[PduSessionNotifyItem]] = OMIT,
        eps_bearer_id: typing.Optional[typing.Sequence[EpsBearerId]] = OMIT,
        ho_preparation_indication: typing.Optional[bool] = OMIT,
        revoke_ebi_list: typing.Optional[typing.Sequence[EpsBearerId]] = OMIT,
        cause: typing.Optional[Cause] = OMIT,
        ng_ap_cause: typing.Optional[NgApCause] = OMIT,
        _5g_mm_cause_value: typing.Optional[int] = OMIT,
        always_on_requested: typing.Optional[bool] = OMIT,
        eps_interworking_ind: typing.Optional[EpsInterworkingIndication] = OMIT,
        secondary_rat_usage_report: typing.Optional[typing.Sequence[SecondaryRatUsageReport]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Optional[HsmfUpdatedData]]:
        """
        Parameters
        ----------
        pdu_session_ref : str
            PDU session reference

        request_indication : RequestIndication

        pei : typing.Optional[str]

        vcn_tunnel_info : typing.Optional[TunnelInfo]

        serving_network : typing.Optional[PlmnId]

        an_type : typing.Optional[AccessType]

        rat_type : typing.Optional[RatType]

        ue_location : typing.Optional[UserLocation]

        ue_time_zone : typing.Optional[str]

        add_ue_location : typing.Optional[UserLocation]

        pause_charging : typing.Optional[bool]

        pti : typing.Optional[int]

        n1sm_info_from_ue : typing.Optional[RefToBinaryData]

        unknown_n1sm_info : typing.Optional[RefToBinaryData]

        qos_flows_rel_notify_list : typing.Optional[typing.Sequence[QosFlowItem]]

        qos_flows_notify_list : typing.Optional[typing.Sequence[QosFlowNotifyItem]]

        notify_list : typing.Optional[typing.Sequence[PduSessionNotifyItem]]

        eps_bearer_id : typing.Optional[typing.Sequence[EpsBearerId]]

        ho_preparation_indication : typing.Optional[bool]

        revoke_ebi_list : typing.Optional[typing.Sequence[EpsBearerId]]

        cause : typing.Optional[Cause]

        ng_ap_cause : typing.Optional[NgApCause]

        _5g_mm_cause_value : typing.Optional[int]

        always_on_requested : typing.Optional[bool]

        eps_interworking_ind : typing.Optional[EpsInterworkingIndication]

        secondary_rat_usage_report : typing.Optional[typing.Sequence[SecondaryRatUsageReport]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[HsmfUpdatedData]]
            successful update of a PDU session with content in the response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"pdu-sessions/{encode_path_param(pdu_session_ref)}/modify",
            method="POST",
            json={
                "requestIndication": request_indication,
                "pei": pei,
                "vcnTunnelInfo": convert_and_respect_annotation_metadata(
                    object_=vcn_tunnel_info, annotation=TunnelInfo, direction="write"
                ),
                "servingNetwork": convert_and_respect_annotation_metadata(
                    object_=serving_network, annotation=PlmnId, direction="write"
                ),
                "anType": an_type,
                "ratType": rat_type,
                "ueLocation": convert_and_respect_annotation_metadata(
                    object_=ue_location, annotation=UserLocation, direction="write"
                ),
                "ueTimeZone": ue_time_zone,
                "addUeLocation": convert_and_respect_annotation_metadata(
                    object_=add_ue_location, annotation=UserLocation, direction="write"
                ),
                "pauseCharging": pause_charging,
                "pti": pti,
                "n1SmInfoFromUe": convert_and_respect_annotation_metadata(
                    object_=n1sm_info_from_ue, annotation=RefToBinaryData, direction="write"
                ),
                "unknownN1SmInfo": convert_and_respect_annotation_metadata(
                    object_=unknown_n1sm_info, annotation=RefToBinaryData, direction="write"
                ),
                "qosFlowsRelNotifyList": convert_and_respect_annotation_metadata(
                    object_=qos_flows_rel_notify_list, annotation=typing.Sequence[QosFlowItem], direction="write"
                ),
                "qosFlowsNotifyList": convert_and_respect_annotation_metadata(
                    object_=qos_flows_notify_list, annotation=typing.Sequence[QosFlowNotifyItem], direction="write"
                ),
                "NotifyList": convert_and_respect_annotation_metadata(
                    object_=notify_list, annotation=typing.Sequence[PduSessionNotifyItem], direction="write"
                ),
                "epsBearerId": eps_bearer_id,
                "hoPreparationIndication": ho_preparation_indication,
                "revokeEbiList": revoke_ebi_list,
                "cause": cause,
                "ngApCause": convert_and_respect_annotation_metadata(
                    object_=ng_ap_cause, annotation=NgApCause, direction="write"
                ),
                "5gMmCauseValue": _5g_mm_cause_value,
                "alwaysOnRequested": always_on_requested,
                "epsInterworkingInd": eps_interworking_ind,
                "secondaryRatUsageReport": convert_and_respect_annotation_metadata(
                    object_=secondary_rat_usage_report,
                    annotation=typing.Sequence[SecondaryRatUsageReport],
                    direction="write",
                ),
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
                    typing.Optional[HsmfUpdatedData],
                    parse_obj_as(
                        type_=typing.Optional[HsmfUpdatedData],
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

    async def release_pdu_session(
        self,
        pdu_session_ref: str,
        *,
        cause: typing.Optional[Cause] = OMIT,
        ng_ap_cause: typing.Optional[NgApCause] = OMIT,
        _5g_mm_cause_value: typing.Optional[int] = OMIT,
        ue_location: typing.Optional[UserLocation] = OMIT,
        ue_time_zone: typing.Optional[str] = OMIT,
        add_ue_location: typing.Optional[UserLocation] = OMIT,
        secondary_rat_usage_report: typing.Optional[typing.Sequence[SecondaryRatUsageReport]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        pdu_session_ref : str
            PDU session reference

        cause : typing.Optional[Cause]

        ng_ap_cause : typing.Optional[NgApCause]

        _5g_mm_cause_value : typing.Optional[int]

        ue_location : typing.Optional[UserLocation]

        ue_time_zone : typing.Optional[str]

        add_ue_location : typing.Optional[UserLocation]

        secondary_rat_usage_report : typing.Optional[typing.Sequence[SecondaryRatUsageReport]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"pdu-sessions/{encode_path_param(pdu_session_ref)}/release",
            method="POST",
            json={
                "cause": cause,
                "ngApCause": convert_and_respect_annotation_metadata(
                    object_=ng_ap_cause, annotation=NgApCause, direction="write"
                ),
                "5gMmCauseValue": _5g_mm_cause_value,
                "ueLocation": convert_and_respect_annotation_metadata(
                    object_=ue_location, annotation=UserLocation, direction="write"
                ),
                "ueTimeZone": ue_time_zone,
                "addUeLocation": convert_and_respect_annotation_metadata(
                    object_=add_ue_location, annotation=UserLocation, direction="write"
                ),
                "secondaryRatUsageReport": convert_and_respect_annotation_metadata(
                    object_=secondary_rat_usage_report,
                    annotation=typing.Sequence[SecondaryRatUsageReport],
                    direction="write",
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



import datetime as dt
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
from ..types.access_type import AccessType
from ..types.dnn_selection_mode import DnnSelectionMode
from ..types.eps_bearer_id import EpsBearerId
from ..types.eps_interworking_indication import EpsInterworkingIndication
from ..types.pdu_session_created_data import PduSessionCreatedData
from ..types.plmn_id import PlmnId
from ..types.problem_details import ProblemDetails
from ..types.rat_type import RatType
from ..types.ref_to_binary_data import RefToBinaryData
from ..types.request_type import RequestType
from ..types.roaming_charging_profile import RoamingChargingProfile
from ..types.snssai import Snssai
from ..types.tunnel_info import TunnelInfo
from ..types.user_location import UserLocation
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawPduSessionsCollectionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def post_pdu_sessions(
        self,
        *,
        dnn: str,
        vsmf_id: str,
        serving_network: PlmnId,
        vsmf_pdu_session_uri: str,
        vcn_tunnel_info: TunnelInfo,
        an_type: AccessType,
        supi: typing.Optional[str] = OMIT,
        unauthenticated_supi: typing.Optional[bool] = OMIT,
        pei: typing.Optional[str] = OMIT,
        pdu_session_id: typing.Optional[int] = OMIT,
        s_nssai: typing.Optional[Snssai] = OMIT,
        request_type: typing.Optional[RequestType] = OMIT,
        eps_bearer_id: typing.Optional[typing.Sequence[EpsBearerId]] = OMIT,
        pgw_s8c_fteid: typing.Optional[str] = OMIT,
        rat_type: typing.Optional[RatType] = OMIT,
        ue_location: typing.Optional[UserLocation] = OMIT,
        ue_time_zone: typing.Optional[str] = OMIT,
        add_ue_location: typing.Optional[UserLocation] = OMIT,
        gpsi: typing.Optional[str] = OMIT,
        n1sm_info_from_ue: typing.Optional[RefToBinaryData] = OMIT,
        unknown_n1sm_info: typing.Optional[RefToBinaryData] = OMIT,
        supported_features: typing.Optional[str] = OMIT,
        h_pcf_id: typing.Optional[str] = OMIT,
        ho_preparation_indication: typing.Optional[bool] = OMIT,
        sel_mode: typing.Optional[DnnSelectionMode] = OMIT,
        always_on_requested: typing.Optional[bool] = OMIT,
        udm_group_id: typing.Optional[str] = OMIT,
        routing_indicator: typing.Optional[str] = OMIT,
        eps_interworking_ind: typing.Optional[EpsInterworkingIndication] = OMIT,
        v_smf_service_instance_id: typing.Optional[str] = OMIT,
        recovery_time: typing.Optional[dt.datetime] = OMIT,
        roaming_charging_profile: typing.Optional[RoamingChargingProfile] = OMIT,
        charging_id: typing.Optional[str] = OMIT,
        old_pdu_session_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PduSessionCreatedData]:
        """
        Parameters
        ----------
        dnn : str

        vsmf_id : str

        serving_network : PlmnId

        vsmf_pdu_session_uri : str

        vcn_tunnel_info : TunnelInfo

        an_type : AccessType

        supi : typing.Optional[str]

        unauthenticated_supi : typing.Optional[bool]

        pei : typing.Optional[str]

        pdu_session_id : typing.Optional[int]

        s_nssai : typing.Optional[Snssai]

        request_type : typing.Optional[RequestType]

        eps_bearer_id : typing.Optional[typing.Sequence[EpsBearerId]]

        pgw_s8c_fteid : typing.Optional[str]

        rat_type : typing.Optional[RatType]

        ue_location : typing.Optional[UserLocation]

        ue_time_zone : typing.Optional[str]

        add_ue_location : typing.Optional[UserLocation]

        gpsi : typing.Optional[str]

        n1sm_info_from_ue : typing.Optional[RefToBinaryData]

        unknown_n1sm_info : typing.Optional[RefToBinaryData]

        supported_features : typing.Optional[str]

        h_pcf_id : typing.Optional[str]

        ho_preparation_indication : typing.Optional[bool]

        sel_mode : typing.Optional[DnnSelectionMode]

        always_on_requested : typing.Optional[bool]

        udm_group_id : typing.Optional[str]

        routing_indicator : typing.Optional[str]

        eps_interworking_ind : typing.Optional[EpsInterworkingIndication]

        v_smf_service_instance_id : typing.Optional[str]

        recovery_time : typing.Optional[dt.datetime]

        roaming_charging_profile : typing.Optional[RoamingChargingProfile]

        charging_id : typing.Optional[str]

        old_pdu_session_id : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PduSessionCreatedData]
            successful creation of a PDU session
        """
        _response = self._client_wrapper.httpx_client.request(
            "pdu-sessions",
            method="POST",
            json={
                "supi": supi,
                "unauthenticatedSupi": unauthenticated_supi,
                "pei": pei,
                "pduSessionId": pdu_session_id,
                "dnn": dnn,
                "sNssai": convert_and_respect_annotation_metadata(
                    object_=s_nssai, annotation=Snssai, direction="write"
                ),
                "vsmfId": vsmf_id,
                "servingNetwork": convert_and_respect_annotation_metadata(
                    object_=serving_network, annotation=PlmnId, direction="write"
                ),
                "requestType": request_type,
                "epsBearerId": eps_bearer_id,
                "pgwS8cFteid": pgw_s8c_fteid,
                "vsmfPduSessionUri": vsmf_pdu_session_uri,
                "vcnTunnelInfo": convert_and_respect_annotation_metadata(
                    object_=vcn_tunnel_info, annotation=TunnelInfo, direction="write"
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
                "gpsi": gpsi,
                "n1SmInfoFromUe": convert_and_respect_annotation_metadata(
                    object_=n1sm_info_from_ue, annotation=RefToBinaryData, direction="write"
                ),
                "unknownN1SmInfo": convert_and_respect_annotation_metadata(
                    object_=unknown_n1sm_info, annotation=RefToBinaryData, direction="write"
                ),
                "supportedFeatures": supported_features,
                "hPcfId": h_pcf_id,
                "hoPreparationIndication": ho_preparation_indication,
                "selMode": sel_mode,
                "alwaysOnRequested": always_on_requested,
                "udmGroupId": udm_group_id,
                "routingIndicator": routing_indicator,
                "epsInterworkingInd": eps_interworking_ind,
                "vSmfServiceInstanceId": v_smf_service_instance_id,
                "recoveryTime": recovery_time,
                "roamingChargingProfile": convert_and_respect_annotation_metadata(
                    object_=roaming_charging_profile, annotation=RoamingChargingProfile, direction="write"
                ),
                "chargingId": charging_id,
                "oldPduSessionId": old_pdu_session_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PduSessionCreatedData,
                    parse_obj_as(
                        type_=PduSessionCreatedData,
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


class AsyncRawPduSessionsCollectionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def post_pdu_sessions(
        self,
        *,
        dnn: str,
        vsmf_id: str,
        serving_network: PlmnId,
        vsmf_pdu_session_uri: str,
        vcn_tunnel_info: TunnelInfo,
        an_type: AccessType,
        supi: typing.Optional[str] = OMIT,
        unauthenticated_supi: typing.Optional[bool] = OMIT,
        pei: typing.Optional[str] = OMIT,
        pdu_session_id: typing.Optional[int] = OMIT,
        s_nssai: typing.Optional[Snssai] = OMIT,
        request_type: typing.Optional[RequestType] = OMIT,
        eps_bearer_id: typing.Optional[typing.Sequence[EpsBearerId]] = OMIT,
        pgw_s8c_fteid: typing.Optional[str] = OMIT,
        rat_type: typing.Optional[RatType] = OMIT,
        ue_location: typing.Optional[UserLocation] = OMIT,
        ue_time_zone: typing.Optional[str] = OMIT,
        add_ue_location: typing.Optional[UserLocation] = OMIT,
        gpsi: typing.Optional[str] = OMIT,
        n1sm_info_from_ue: typing.Optional[RefToBinaryData] = OMIT,
        unknown_n1sm_info: typing.Optional[RefToBinaryData] = OMIT,
        supported_features: typing.Optional[str] = OMIT,
        h_pcf_id: typing.Optional[str] = OMIT,
        ho_preparation_indication: typing.Optional[bool] = OMIT,
        sel_mode: typing.Optional[DnnSelectionMode] = OMIT,
        always_on_requested: typing.Optional[bool] = OMIT,
        udm_group_id: typing.Optional[str] = OMIT,
        routing_indicator: typing.Optional[str] = OMIT,
        eps_interworking_ind: typing.Optional[EpsInterworkingIndication] = OMIT,
        v_smf_service_instance_id: typing.Optional[str] = OMIT,
        recovery_time: typing.Optional[dt.datetime] = OMIT,
        roaming_charging_profile: typing.Optional[RoamingChargingProfile] = OMIT,
        charging_id: typing.Optional[str] = OMIT,
        old_pdu_session_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PduSessionCreatedData]:
        """
        Parameters
        ----------
        dnn : str

        vsmf_id : str

        serving_network : PlmnId

        vsmf_pdu_session_uri : str

        vcn_tunnel_info : TunnelInfo

        an_type : AccessType

        supi : typing.Optional[str]

        unauthenticated_supi : typing.Optional[bool]

        pei : typing.Optional[str]

        pdu_session_id : typing.Optional[int]

        s_nssai : typing.Optional[Snssai]

        request_type : typing.Optional[RequestType]

        eps_bearer_id : typing.Optional[typing.Sequence[EpsBearerId]]

        pgw_s8c_fteid : typing.Optional[str]

        rat_type : typing.Optional[RatType]

        ue_location : typing.Optional[UserLocation]

        ue_time_zone : typing.Optional[str]

        add_ue_location : typing.Optional[UserLocation]

        gpsi : typing.Optional[str]

        n1sm_info_from_ue : typing.Optional[RefToBinaryData]

        unknown_n1sm_info : typing.Optional[RefToBinaryData]

        supported_features : typing.Optional[str]

        h_pcf_id : typing.Optional[str]

        ho_preparation_indication : typing.Optional[bool]

        sel_mode : typing.Optional[DnnSelectionMode]

        always_on_requested : typing.Optional[bool]

        udm_group_id : typing.Optional[str]

        routing_indicator : typing.Optional[str]

        eps_interworking_ind : typing.Optional[EpsInterworkingIndication]

        v_smf_service_instance_id : typing.Optional[str]

        recovery_time : typing.Optional[dt.datetime]

        roaming_charging_profile : typing.Optional[RoamingChargingProfile]

        charging_id : typing.Optional[str]

        old_pdu_session_id : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PduSessionCreatedData]
            successful creation of a PDU session
        """
        _response = await self._client_wrapper.httpx_client.request(
            "pdu-sessions",
            method="POST",
            json={
                "supi": supi,
                "unauthenticatedSupi": unauthenticated_supi,
                "pei": pei,
                "pduSessionId": pdu_session_id,
                "dnn": dnn,
                "sNssai": convert_and_respect_annotation_metadata(
                    object_=s_nssai, annotation=Snssai, direction="write"
                ),
                "vsmfId": vsmf_id,
                "servingNetwork": convert_and_respect_annotation_metadata(
                    object_=serving_network, annotation=PlmnId, direction="write"
                ),
                "requestType": request_type,
                "epsBearerId": eps_bearer_id,
                "pgwS8cFteid": pgw_s8c_fteid,
                "vsmfPduSessionUri": vsmf_pdu_session_uri,
                "vcnTunnelInfo": convert_and_respect_annotation_metadata(
                    object_=vcn_tunnel_info, annotation=TunnelInfo, direction="write"
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
                "gpsi": gpsi,
                "n1SmInfoFromUe": convert_and_respect_annotation_metadata(
                    object_=n1sm_info_from_ue, annotation=RefToBinaryData, direction="write"
                ),
                "unknownN1SmInfo": convert_and_respect_annotation_metadata(
                    object_=unknown_n1sm_info, annotation=RefToBinaryData, direction="write"
                ),
                "supportedFeatures": supported_features,
                "hPcfId": h_pcf_id,
                "hoPreparationIndication": ho_preparation_indication,
                "selMode": sel_mode,
                "alwaysOnRequested": always_on_requested,
                "udmGroupId": udm_group_id,
                "routingIndicator": routing_indicator,
                "epsInterworkingInd": eps_interworking_ind,
                "vSmfServiceInstanceId": v_smf_service_instance_id,
                "recoveryTime": recovery_time,
                "roamingChargingProfile": convert_and_respect_annotation_metadata(
                    object_=roaming_charging_profile, annotation=RoamingChargingProfile, direction="write"
                ),
                "chargingId": charging_id,
                "oldPduSessionId": old_pdu_session_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PduSessionCreatedData,
                    parse_obj_as(
                        type_=PduSessionCreatedData,
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

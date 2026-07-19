

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
from ..types.backup_amf_info import BackupAmfInfo
from ..types.cause import Cause
from ..types.eps_bearer_container import EpsBearerContainer
from ..types.eps_bearer_id import EpsBearerId
from ..types.eps_interworking_indication import EpsInterworkingIndication
from ..types.guami import Guami
from ..types.ho_state import HoState
from ..types.mme_capabilities import MmeCapabilities
from ..types.n2sm_info_type import N2SmInfoType
from ..types.ng_ap_cause import NgApCause
from ..types.plmn_id import PlmnId
from ..types.presence_state import PresenceState
from ..types.problem_details import ProblemDetails
from ..types.rat_type import RatType
from ..types.ref_to_binary_data import RefToBinaryData
from ..types.sm_context_retrieved_data import SmContextRetrievedData
from ..types.sm_context_updated_data import SmContextUpdatedData
from ..types.snssai import Snssai
from ..types.trace_data import TraceData
from ..types.up_cnx_state import UpCnxState
from ..types.user_location import UserLocation
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawIndividualSmContextClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def retrieve_sm_context(
        self,
        sm_context_ref: str,
        *,
        target_mme_cap: typing.Optional[MmeCapabilities] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SmContextRetrievedData]:
        """
        Parameters
        ----------
        sm_context_ref : str
            SM context reference

        target_mme_cap : typing.Optional[MmeCapabilities]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SmContextRetrievedData]
            successful retrieval of an SM context
        """
        _response = self._client_wrapper.httpx_client.request(
            f"sm-contexts/{encode_path_param(sm_context_ref)}/retrieve",
            method="POST",
            json={
                "targetMmeCap": convert_and_respect_annotation_metadata(
                    object_=target_mme_cap, annotation=MmeCapabilities, direction="write"
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
                    SmContextRetrievedData,
                    parse_obj_as(
                        type_=SmContextRetrievedData,
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

    def update_sm_context(
        self,
        sm_context_ref: str,
        *,
        pei: typing.Optional[str] = OMIT,
        gpsi: typing.Optional[str] = OMIT,
        serving_nf_id: typing.Optional[str] = OMIT,
        guami: typing.Optional[Guami] = OMIT,
        serving_network: typing.Optional[PlmnId] = OMIT,
        backup_amf_info: typing.Optional[typing.Sequence[BackupAmfInfo]] = OMIT,
        an_type: typing.Optional[AccessType] = OMIT,
        rat_type: typing.Optional[RatType] = OMIT,
        presence_in_ladn: typing.Optional[PresenceState] = OMIT,
        ue_location: typing.Optional[UserLocation] = OMIT,
        ue_time_zone: typing.Optional[str] = OMIT,
        add_ue_location: typing.Optional[UserLocation] = OMIT,
        up_cnx_state: typing.Optional[UpCnxState] = OMIT,
        ho_state: typing.Optional[HoState] = OMIT,
        to_be_switched: typing.Optional[bool] = OMIT,
        failed_to_be_switched: typing.Optional[bool] = OMIT,
        n1sm_msg: typing.Optional[RefToBinaryData] = OMIT,
        n2sm_info: typing.Optional[RefToBinaryData] = OMIT,
        n2sm_info_type: typing.Optional[N2SmInfoType] = OMIT,
        target_serving_nf_id: typing.Optional[str] = OMIT,
        sm_context_status_uri: typing.Optional[str] = OMIT,
        data_forwarding: typing.Optional[bool] = OMIT,
        eps_bearer_setup: typing.Optional[typing.Sequence[EpsBearerContainer]] = OMIT,
        revoke_ebi_list: typing.Optional[typing.Sequence[EpsBearerId]] = OMIT,
        release: typing.Optional[bool] = OMIT,
        cause: typing.Optional[Cause] = OMIT,
        ng_ap_cause: typing.Optional[NgApCause] = OMIT,
        _5g_mm_cause_value: typing.Optional[int] = OMIT,
        s_nssai: typing.Optional[Snssai] = OMIT,
        trace_data: typing.Optional[TraceData] = OMIT,
        eps_interworking_ind: typing.Optional[EpsInterworkingIndication] = OMIT,
        an_type_can_be_changed: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Optional[SmContextUpdatedData]]:
        """
        Parameters
        ----------
        sm_context_ref : str
            SM context reference

        pei : typing.Optional[str]

        gpsi : typing.Optional[str]

        serving_nf_id : typing.Optional[str]

        guami : typing.Optional[Guami]

        serving_network : typing.Optional[PlmnId]

        backup_amf_info : typing.Optional[typing.Sequence[BackupAmfInfo]]

        an_type : typing.Optional[AccessType]

        rat_type : typing.Optional[RatType]

        presence_in_ladn : typing.Optional[PresenceState]

        ue_location : typing.Optional[UserLocation]

        ue_time_zone : typing.Optional[str]

        add_ue_location : typing.Optional[UserLocation]

        up_cnx_state : typing.Optional[UpCnxState]

        ho_state : typing.Optional[HoState]

        to_be_switched : typing.Optional[bool]

        failed_to_be_switched : typing.Optional[bool]

        n1sm_msg : typing.Optional[RefToBinaryData]

        n2sm_info : typing.Optional[RefToBinaryData]

        n2sm_info_type : typing.Optional[N2SmInfoType]

        target_serving_nf_id : typing.Optional[str]

        sm_context_status_uri : typing.Optional[str]

        data_forwarding : typing.Optional[bool]

        eps_bearer_setup : typing.Optional[typing.Sequence[EpsBearerContainer]]

        revoke_ebi_list : typing.Optional[typing.Sequence[EpsBearerId]]

        release : typing.Optional[bool]

        cause : typing.Optional[Cause]

        ng_ap_cause : typing.Optional[NgApCause]

        _5g_mm_cause_value : typing.Optional[int]

        s_nssai : typing.Optional[Snssai]

        trace_data : typing.Optional[TraceData]

        eps_interworking_ind : typing.Optional[EpsInterworkingIndication]

        an_type_can_be_changed : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[SmContextUpdatedData]]
            successful update of an SM context with content in the response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"sm-contexts/{encode_path_param(sm_context_ref)}/modify",
            method="POST",
            json={
                "pei": pei,
                "gpsi": gpsi,
                "servingNfId": serving_nf_id,
                "guami": convert_and_respect_annotation_metadata(object_=guami, annotation=Guami, direction="write"),
                "servingNetwork": convert_and_respect_annotation_metadata(
                    object_=serving_network, annotation=PlmnId, direction="write"
                ),
                "backupAmfInfo": convert_and_respect_annotation_metadata(
                    object_=backup_amf_info,
                    annotation=typing.Optional[typing.Sequence[BackupAmfInfo]],
                    direction="write",
                ),
                "anType": an_type,
                "ratType": rat_type,
                "presenceInLadn": presence_in_ladn,
                "ueLocation": convert_and_respect_annotation_metadata(
                    object_=ue_location, annotation=UserLocation, direction="write"
                ),
                "ueTimeZone": ue_time_zone,
                "addUeLocation": convert_and_respect_annotation_metadata(
                    object_=add_ue_location, annotation=UserLocation, direction="write"
                ),
                "upCnxState": up_cnx_state,
                "hoState": ho_state,
                "toBeSwitched": to_be_switched,
                "failedToBeSwitched": failed_to_be_switched,
                "n1SmMsg": convert_and_respect_annotation_metadata(
                    object_=n1sm_msg, annotation=RefToBinaryData, direction="write"
                ),
                "n2SmInfo": convert_and_respect_annotation_metadata(
                    object_=n2sm_info, annotation=RefToBinaryData, direction="write"
                ),
                "n2SmInfoType": n2sm_info_type,
                "targetServingNfId": target_serving_nf_id,
                "smContextStatusUri": sm_context_status_uri,
                "dataForwarding": data_forwarding,
                "epsBearerSetup": eps_bearer_setup,
                "revokeEbiList": revoke_ebi_list,
                "release": release,
                "cause": cause,
                "ngApCause": convert_and_respect_annotation_metadata(
                    object_=ng_ap_cause, annotation=NgApCause, direction="write"
                ),
                "5gMmCauseValue": _5g_mm_cause_value,
                "sNssai": convert_and_respect_annotation_metadata(
                    object_=s_nssai, annotation=Snssai, direction="write"
                ),
                "traceData": convert_and_respect_annotation_metadata(
                    object_=trace_data, annotation=typing.Optional[TraceData], direction="write"
                ),
                "epsInterworkingInd": eps_interworking_ind,
                "anTypeCanBeChanged": an_type_can_be_changed,
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
                    typing.Optional[SmContextUpdatedData],
                    parse_obj_as(
                        type_=typing.Optional[SmContextUpdatedData],
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

    def release_sm_context(
        self,
        sm_context_ref: str,
        *,
        cause: typing.Optional[Cause] = OMIT,
        ng_ap_cause: typing.Optional[NgApCause] = OMIT,
        _5g_mm_cause_value: typing.Optional[int] = OMIT,
        ue_location: typing.Optional[UserLocation] = OMIT,
        ue_time_zone: typing.Optional[str] = OMIT,
        add_ue_location: typing.Optional[UserLocation] = OMIT,
        vsmf_release_only: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        sm_context_ref : str
            SM context reference

        cause : typing.Optional[Cause]

        ng_ap_cause : typing.Optional[NgApCause]

        _5g_mm_cause_value : typing.Optional[int]

        ue_location : typing.Optional[UserLocation]

        ue_time_zone : typing.Optional[str]

        add_ue_location : typing.Optional[UserLocation]

        vsmf_release_only : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"sm-contexts/{encode_path_param(sm_context_ref)}/release",
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
                "vsmfReleaseOnly": vsmf_release_only,
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


class AsyncRawIndividualSmContextClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def retrieve_sm_context(
        self,
        sm_context_ref: str,
        *,
        target_mme_cap: typing.Optional[MmeCapabilities] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SmContextRetrievedData]:
        """
        Parameters
        ----------
        sm_context_ref : str
            SM context reference

        target_mme_cap : typing.Optional[MmeCapabilities]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SmContextRetrievedData]
            successful retrieval of an SM context
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"sm-contexts/{encode_path_param(sm_context_ref)}/retrieve",
            method="POST",
            json={
                "targetMmeCap": convert_and_respect_annotation_metadata(
                    object_=target_mme_cap, annotation=MmeCapabilities, direction="write"
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
                    SmContextRetrievedData,
                    parse_obj_as(
                        type_=SmContextRetrievedData,
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

    async def update_sm_context(
        self,
        sm_context_ref: str,
        *,
        pei: typing.Optional[str] = OMIT,
        gpsi: typing.Optional[str] = OMIT,
        serving_nf_id: typing.Optional[str] = OMIT,
        guami: typing.Optional[Guami] = OMIT,
        serving_network: typing.Optional[PlmnId] = OMIT,
        backup_amf_info: typing.Optional[typing.Sequence[BackupAmfInfo]] = OMIT,
        an_type: typing.Optional[AccessType] = OMIT,
        rat_type: typing.Optional[RatType] = OMIT,
        presence_in_ladn: typing.Optional[PresenceState] = OMIT,
        ue_location: typing.Optional[UserLocation] = OMIT,
        ue_time_zone: typing.Optional[str] = OMIT,
        add_ue_location: typing.Optional[UserLocation] = OMIT,
        up_cnx_state: typing.Optional[UpCnxState] = OMIT,
        ho_state: typing.Optional[HoState] = OMIT,
        to_be_switched: typing.Optional[bool] = OMIT,
        failed_to_be_switched: typing.Optional[bool] = OMIT,
        n1sm_msg: typing.Optional[RefToBinaryData] = OMIT,
        n2sm_info: typing.Optional[RefToBinaryData] = OMIT,
        n2sm_info_type: typing.Optional[N2SmInfoType] = OMIT,
        target_serving_nf_id: typing.Optional[str] = OMIT,
        sm_context_status_uri: typing.Optional[str] = OMIT,
        data_forwarding: typing.Optional[bool] = OMIT,
        eps_bearer_setup: typing.Optional[typing.Sequence[EpsBearerContainer]] = OMIT,
        revoke_ebi_list: typing.Optional[typing.Sequence[EpsBearerId]] = OMIT,
        release: typing.Optional[bool] = OMIT,
        cause: typing.Optional[Cause] = OMIT,
        ng_ap_cause: typing.Optional[NgApCause] = OMIT,
        _5g_mm_cause_value: typing.Optional[int] = OMIT,
        s_nssai: typing.Optional[Snssai] = OMIT,
        trace_data: typing.Optional[TraceData] = OMIT,
        eps_interworking_ind: typing.Optional[EpsInterworkingIndication] = OMIT,
        an_type_can_be_changed: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Optional[SmContextUpdatedData]]:
        """
        Parameters
        ----------
        sm_context_ref : str
            SM context reference

        pei : typing.Optional[str]

        gpsi : typing.Optional[str]

        serving_nf_id : typing.Optional[str]

        guami : typing.Optional[Guami]

        serving_network : typing.Optional[PlmnId]

        backup_amf_info : typing.Optional[typing.Sequence[BackupAmfInfo]]

        an_type : typing.Optional[AccessType]

        rat_type : typing.Optional[RatType]

        presence_in_ladn : typing.Optional[PresenceState]

        ue_location : typing.Optional[UserLocation]

        ue_time_zone : typing.Optional[str]

        add_ue_location : typing.Optional[UserLocation]

        up_cnx_state : typing.Optional[UpCnxState]

        ho_state : typing.Optional[HoState]

        to_be_switched : typing.Optional[bool]

        failed_to_be_switched : typing.Optional[bool]

        n1sm_msg : typing.Optional[RefToBinaryData]

        n2sm_info : typing.Optional[RefToBinaryData]

        n2sm_info_type : typing.Optional[N2SmInfoType]

        target_serving_nf_id : typing.Optional[str]

        sm_context_status_uri : typing.Optional[str]

        data_forwarding : typing.Optional[bool]

        eps_bearer_setup : typing.Optional[typing.Sequence[EpsBearerContainer]]

        revoke_ebi_list : typing.Optional[typing.Sequence[EpsBearerId]]

        release : typing.Optional[bool]

        cause : typing.Optional[Cause]

        ng_ap_cause : typing.Optional[NgApCause]

        _5g_mm_cause_value : typing.Optional[int]

        s_nssai : typing.Optional[Snssai]

        trace_data : typing.Optional[TraceData]

        eps_interworking_ind : typing.Optional[EpsInterworkingIndication]

        an_type_can_be_changed : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[SmContextUpdatedData]]
            successful update of an SM context with content in the response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"sm-contexts/{encode_path_param(sm_context_ref)}/modify",
            method="POST",
            json={
                "pei": pei,
                "gpsi": gpsi,
                "servingNfId": serving_nf_id,
                "guami": convert_and_respect_annotation_metadata(object_=guami, annotation=Guami, direction="write"),
                "servingNetwork": convert_and_respect_annotation_metadata(
                    object_=serving_network, annotation=PlmnId, direction="write"
                ),
                "backupAmfInfo": convert_and_respect_annotation_metadata(
                    object_=backup_amf_info,
                    annotation=typing.Optional[typing.Sequence[BackupAmfInfo]],
                    direction="write",
                ),
                "anType": an_type,
                "ratType": rat_type,
                "presenceInLadn": presence_in_ladn,
                "ueLocation": convert_and_respect_annotation_metadata(
                    object_=ue_location, annotation=UserLocation, direction="write"
                ),
                "ueTimeZone": ue_time_zone,
                "addUeLocation": convert_and_respect_annotation_metadata(
                    object_=add_ue_location, annotation=UserLocation, direction="write"
                ),
                "upCnxState": up_cnx_state,
                "hoState": ho_state,
                "toBeSwitched": to_be_switched,
                "failedToBeSwitched": failed_to_be_switched,
                "n1SmMsg": convert_and_respect_annotation_metadata(
                    object_=n1sm_msg, annotation=RefToBinaryData, direction="write"
                ),
                "n2SmInfo": convert_and_respect_annotation_metadata(
                    object_=n2sm_info, annotation=RefToBinaryData, direction="write"
                ),
                "n2SmInfoType": n2sm_info_type,
                "targetServingNfId": target_serving_nf_id,
                "smContextStatusUri": sm_context_status_uri,
                "dataForwarding": data_forwarding,
                "epsBearerSetup": eps_bearer_setup,
                "revokeEbiList": revoke_ebi_list,
                "release": release,
                "cause": cause,
                "ngApCause": convert_and_respect_annotation_metadata(
                    object_=ng_ap_cause, annotation=NgApCause, direction="write"
                ),
                "5gMmCauseValue": _5g_mm_cause_value,
                "sNssai": convert_and_respect_annotation_metadata(
                    object_=s_nssai, annotation=Snssai, direction="write"
                ),
                "traceData": convert_and_respect_annotation_metadata(
                    object_=trace_data, annotation=typing.Optional[TraceData], direction="write"
                ),
                "epsInterworkingInd": eps_interworking_ind,
                "anTypeCanBeChanged": an_type_can_be_changed,
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
                    typing.Optional[SmContextUpdatedData],
                    parse_obj_as(
                        type_=typing.Optional[SmContextUpdatedData],
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

    async def release_sm_context(
        self,
        sm_context_ref: str,
        *,
        cause: typing.Optional[Cause] = OMIT,
        ng_ap_cause: typing.Optional[NgApCause] = OMIT,
        _5g_mm_cause_value: typing.Optional[int] = OMIT,
        ue_location: typing.Optional[UserLocation] = OMIT,
        ue_time_zone: typing.Optional[str] = OMIT,
        add_ue_location: typing.Optional[UserLocation] = OMIT,
        vsmf_release_only: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        sm_context_ref : str
            SM context reference

        cause : typing.Optional[Cause]

        ng_ap_cause : typing.Optional[NgApCause]

        _5g_mm_cause_value : typing.Optional[int]

        ue_location : typing.Optional[UserLocation]

        ue_time_zone : typing.Optional[str]

        add_ue_location : typing.Optional[UserLocation]

        vsmf_release_only : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"sm-contexts/{encode_path_param(sm_context_ref)}/release",
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
                "vsmfReleaseOnly": vsmf_release_only,
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

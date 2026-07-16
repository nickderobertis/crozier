

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.http_response import AsyncHttpResponse, HttpResponse
from .core.jsonable_encoder import jsonable_encoder
from .core.pydantic_utilities import parse_obj_as
from .core.request_options import RequestOptions
from .types.create_byoc_trunk_request_status_callback_method import CreateByocTrunkRequestStatusCallbackMethod
from .types.create_byoc_trunk_request_voice_fallback_method import CreateByocTrunkRequestVoiceFallbackMethod
from .types.create_byoc_trunk_request_voice_method import CreateByocTrunkRequestVoiceMethod
from .types.list_byoc_trunk_response import ListByocTrunkResponse
from .types.list_connection_policy_response import ListConnectionPolicyResponse
from .types.list_connection_policy_target_response import ListConnectionPolicyTargetResponse
from .types.list_dialing_permissions_country_response import ListDialingPermissionsCountryResponse
from .types.list_dialing_permissions_hrs_prefixes_response import ListDialingPermissionsHrsPrefixesResponse
from .types.list_ip_record_response import ListIpRecordResponse
from .types.list_source_ip_mapping_response import ListSourceIpMappingResponse
from .types.update_byoc_trunk_request_status_callback_method import UpdateByocTrunkRequestStatusCallbackMethod
from .types.update_byoc_trunk_request_voice_fallback_method import UpdateByocTrunkRequestVoiceFallbackMethod
from .types.update_byoc_trunk_request_voice_method import UpdateByocTrunkRequestVoiceMethod
from .types.voice_v1byoc_trunk import VoiceV1ByocTrunk
from .types.voice_v1connection_policy import VoiceV1ConnectionPolicy
from .types.voice_v1connection_policy_connection_policy_target import VoiceV1ConnectionPolicyConnectionPolicyTarget
from .types.voice_v1dialing_permissions_dialing_permissions_country_bulk_update import (
    VoiceV1DialingPermissionsDialingPermissionsCountryBulkUpdate,
)
from .types.voice_v1dialing_permissions_dialing_permissions_country_instance import (
    VoiceV1DialingPermissionsDialingPermissionsCountryInstance,
)
from .types.voice_v1dialing_permissions_dialing_permissions_settings import (
    VoiceV1DialingPermissionsDialingPermissionsSettings,
)
from .types.voice_v1ip_record import VoiceV1IpRecord
from .types.voice_v1source_ip_mapping import VoiceV1SourceIpMapping


OMIT = typing.cast(typing.Any, ...)


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def delete_archived_call(
        self, date: dt.date, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Delete an archived call record from Bulk Export. Note: this does not also delete the record from the Voice API.

        Parameters
        ----------
        date : dt.date
            The date of the Call in UTC.

        sid : str
            The Twilio-provided Call SID that uniquely identifies the Call resource to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/Archives/{jsonable_encoder(date)}/Calls/{jsonable_encoder(sid)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_byoc_trunk(
        self,
        *,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListByocTrunkResponse]:
        """


        Parameters
        ----------
        page_size : typing.Optional[int]
            How many resources to return in each list page. The default is 50, and the maximum is 1000.

        page : typing.Optional[int]
            The page index. This value is simply for client state.

        page_token : typing.Optional[str]
            The page token. This is provided by the API.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListByocTrunkResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/ByocTrunks",
            method="GET",
            params={
                "PageSize": page_size,
                "Page": page,
                "PageToken": page_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListByocTrunkResponse,
                    parse_obj_as(
                        type_=ListByocTrunkResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_byoc_trunk(
        self,
        *,
        cnam_lookup_enabled: typing.Optional[bool] = OMIT,
        connection_policy_sid: typing.Optional[str] = OMIT,
        friendly_name: typing.Optional[str] = OMIT,
        from_domain_sid: typing.Optional[str] = OMIT,
        status_callback_method: typing.Optional[CreateByocTrunkRequestStatusCallbackMethod] = OMIT,
        status_callback_url: typing.Optional[str] = OMIT,
        voice_fallback_method: typing.Optional[CreateByocTrunkRequestVoiceFallbackMethod] = OMIT,
        voice_fallback_url: typing.Optional[str] = OMIT,
        voice_method: typing.Optional[CreateByocTrunkRequestVoiceMethod] = OMIT,
        voice_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[VoiceV1ByocTrunk]:
        """


        Parameters
        ----------
        cnam_lookup_enabled : typing.Optional[bool]
            Whether Caller ID Name (CNAM) lookup is enabled for the trunk. If enabled, all inbound calls to the BYOC Trunk from the United States and Canada automatically perform a CNAM Lookup and display Caller ID data on your phone. See [CNAM Lookups](https://www.twilio.com/docs/sip-trunking#CNAM) for more information.

        connection_policy_sid : typing.Optional[str]
            The SID of the Connection Policy that Twilio will use when routing traffic to your communications infrastructure.

        friendly_name : typing.Optional[str]
            A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.

        from_domain_sid : typing.Optional[str]
            The SID of the SIP Domain that should be used in the `From` header of originating calls sent to your SIP infrastructure. If your SIP infrastructure allows users to "call back" an incoming call, configure this with a [SIP Domain](https://www.twilio.com/docs/voice/api/sending-sip) to ensure proper routing. If not configured, the from domain will default to "sip.twilio.com".

        status_callback_method : typing.Optional[CreateByocTrunkRequestStatusCallbackMethod]
            The HTTP method we should use to call `status_callback_url`. Can be: `GET` or `POST`.

        status_callback_url : typing.Optional[str]
            The URL that we should call to pass status parameters (such as call ended) to your application.

        voice_fallback_method : typing.Optional[CreateByocTrunkRequestVoiceFallbackMethod]
            The HTTP method we should use to call `voice_fallback_url`. Can be: `GET` or `POST`.

        voice_fallback_url : typing.Optional[str]
            The URL that we should call when an error occurs while retrieving or executing the TwiML from `voice_url`.

        voice_method : typing.Optional[CreateByocTrunkRequestVoiceMethod]
            The HTTP method we should use to call `voice_url`. Can be: `GET` or `POST`.

        voice_url : typing.Optional[str]
            The URL we should call when the BYOC Trunk receives a call.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[VoiceV1ByocTrunk]
            Created
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/ByocTrunks",
            method="POST",
            data={
                "CnamLookupEnabled": cnam_lookup_enabled,
                "ConnectionPolicySid": connection_policy_sid,
                "FriendlyName": friendly_name,
                "FromDomainSid": from_domain_sid,
                "StatusCallbackMethod": status_callback_method,
                "StatusCallbackUrl": status_callback_url,
                "VoiceFallbackMethod": voice_fallback_method,
                "VoiceFallbackUrl": voice_fallback_url,
                "VoiceMethod": voice_method,
                "VoiceUrl": voice_url,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VoiceV1ByocTrunk,
                    parse_obj_as(
                        type_=VoiceV1ByocTrunk,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def fetch_byoc_trunk(
        self, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[VoiceV1ByocTrunk]:
        """


        Parameters
        ----------
        sid : str
            The Twilio-provided string that uniquely identifies the BYOC Trunk resource to fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[VoiceV1ByocTrunk]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/ByocTrunks/{jsonable_encoder(sid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VoiceV1ByocTrunk,
                    parse_obj_as(
                        type_=VoiceV1ByocTrunk,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_byoc_trunk(
        self,
        sid: str,
        *,
        cnam_lookup_enabled: typing.Optional[bool] = OMIT,
        connection_policy_sid: typing.Optional[str] = OMIT,
        friendly_name: typing.Optional[str] = OMIT,
        from_domain_sid: typing.Optional[str] = OMIT,
        status_callback_method: typing.Optional[UpdateByocTrunkRequestStatusCallbackMethod] = OMIT,
        status_callback_url: typing.Optional[str] = OMIT,
        voice_fallback_method: typing.Optional[UpdateByocTrunkRequestVoiceFallbackMethod] = OMIT,
        voice_fallback_url: typing.Optional[str] = OMIT,
        voice_method: typing.Optional[UpdateByocTrunkRequestVoiceMethod] = OMIT,
        voice_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[VoiceV1ByocTrunk]:
        """


        Parameters
        ----------
        sid : str
            The Twilio-provided string that uniquely identifies the BYOC Trunk resource to update.

        cnam_lookup_enabled : typing.Optional[bool]
            Whether Caller ID Name (CNAM) lookup is enabled for the trunk. If enabled, all inbound calls to the BYOC Trunk from the United States and Canada automatically perform a CNAM Lookup and display Caller ID data on your phone. See [CNAM Lookups](https://www.twilio.com/docs/sip-trunking#CNAM) for more information.

        connection_policy_sid : typing.Optional[str]
            The SID of the Connection Policy that Twilio will use when routing traffic to your communications infrastructure.

        friendly_name : typing.Optional[str]
            A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.

        from_domain_sid : typing.Optional[str]
            The SID of the SIP Domain that should be used in the `From` header of originating calls sent to your SIP infrastructure. If your SIP infrastructure allows users to "call back" an incoming call, configure this with a [SIP Domain](https://www.twilio.com/docs/voice/api/sending-sip) to ensure proper routing. If not configured, the from domain will default to "sip.twilio.com".

        status_callback_method : typing.Optional[UpdateByocTrunkRequestStatusCallbackMethod]
            The HTTP method we should use to call `status_callback_url`. Can be: `GET` or `POST`.

        status_callback_url : typing.Optional[str]
            The URL that we should call to pass status parameters (such as call ended) to your application.

        voice_fallback_method : typing.Optional[UpdateByocTrunkRequestVoiceFallbackMethod]
            The HTTP method we should use to call `voice_fallback_url`. Can be: `GET` or `POST`.

        voice_fallback_url : typing.Optional[str]
            The URL that we should call when an error occurs while retrieving or executing the TwiML requested by `voice_url`.

        voice_method : typing.Optional[UpdateByocTrunkRequestVoiceMethod]
            The HTTP method we should use to call `voice_url`

        voice_url : typing.Optional[str]
            The URL we should call when the BYOC Trunk receives a call.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[VoiceV1ByocTrunk]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/ByocTrunks/{jsonable_encoder(sid)}",
            method="POST",
            data={
                "CnamLookupEnabled": cnam_lookup_enabled,
                "ConnectionPolicySid": connection_policy_sid,
                "FriendlyName": friendly_name,
                "FromDomainSid": from_domain_sid,
                "StatusCallbackMethod": status_callback_method,
                "StatusCallbackUrl": status_callback_url,
                "VoiceFallbackMethod": voice_fallback_method,
                "VoiceFallbackUrl": voice_fallback_url,
                "VoiceMethod": voice_method,
                "VoiceUrl": voice_url,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VoiceV1ByocTrunk,
                    parse_obj_as(
                        type_=VoiceV1ByocTrunk,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_byoc_trunk(
        self, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """


        Parameters
        ----------
        sid : str
            The Twilio-provided string that uniquely identifies the BYOC Trunk resource to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/ByocTrunks/{jsonable_encoder(sid)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_connection_policy(
        self,
        *,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListConnectionPolicyResponse]:
        """


        Parameters
        ----------
        page_size : typing.Optional[int]
            How many resources to return in each list page. The default is 50, and the maximum is 1000.

        page : typing.Optional[int]
            The page index. This value is simply for client state.

        page_token : typing.Optional[str]
            The page token. This is provided by the API.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListConnectionPolicyResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/ConnectionPolicies",
            method="GET",
            params={
                "PageSize": page_size,
                "Page": page,
                "PageToken": page_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListConnectionPolicyResponse,
                    parse_obj_as(
                        type_=ListConnectionPolicyResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_connection_policy(
        self, *, friendly_name: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[VoiceV1ConnectionPolicy]:
        """


        Parameters
        ----------
        friendly_name : typing.Optional[str]
            A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[VoiceV1ConnectionPolicy]
            Created
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/ConnectionPolicies",
            method="POST",
            data={
                "FriendlyName": friendly_name,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VoiceV1ConnectionPolicy,
                    parse_obj_as(
                        type_=VoiceV1ConnectionPolicy,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_connection_policy_target(
        self,
        connection_policy_sid: str,
        *,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListConnectionPolicyTargetResponse]:
        """


        Parameters
        ----------
        connection_policy_sid : str
            The SID of the Connection Policy from which to read the Targets.

        page_size : typing.Optional[int]
            How many resources to return in each list page. The default is 50, and the maximum is 1000.

        page : typing.Optional[int]
            The page index. This value is simply for client state.

        page_token : typing.Optional[str]
            The page token. This is provided by the API.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListConnectionPolicyTargetResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/ConnectionPolicies/{jsonable_encoder(connection_policy_sid)}/Targets",
            method="GET",
            params={
                "PageSize": page_size,
                "Page": page,
                "PageToken": page_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListConnectionPolicyTargetResponse,
                    parse_obj_as(
                        type_=ListConnectionPolicyTargetResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_connection_policy_target(
        self,
        connection_policy_sid: str,
        *,
        target: str,
        enabled: typing.Optional[bool] = OMIT,
        friendly_name: typing.Optional[str] = OMIT,
        priority: typing.Optional[int] = OMIT,
        weight: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[VoiceV1ConnectionPolicyConnectionPolicyTarget]:
        """


        Parameters
        ----------
        connection_policy_sid : str
            The SID of the Connection Policy that owns the Target.

        target : str
            The SIP address you want Twilio to route your calls to. This must be a `sip:` schema. `sips` is NOT supported.

        enabled : typing.Optional[bool]
            Whether the Target is enabled. The default is `true`.

        friendly_name : typing.Optional[str]
            A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.

        priority : typing.Optional[int]
            The relative importance of the target. Can be an integer from 0 to 65535, inclusive, and the default is 10. The lowest number represents the most important target.

        weight : typing.Optional[int]
            The value that determines the relative share of the load the Target should receive compared to other Targets with the same priority. Can be an integer from 1 to 65535, inclusive, and the default is 10. Targets with higher values receive more load than those with lower ones with the same priority.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[VoiceV1ConnectionPolicyConnectionPolicyTarget]
            Created
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/ConnectionPolicies/{jsonable_encoder(connection_policy_sid)}/Targets",
            method="POST",
            data={
                "Enabled": enabled,
                "FriendlyName": friendly_name,
                "Priority": priority,
                "Target": target,
                "Weight": weight,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VoiceV1ConnectionPolicyConnectionPolicyTarget,
                    parse_obj_as(
                        type_=VoiceV1ConnectionPolicyConnectionPolicyTarget,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def fetch_connection_policy_target(
        self, connection_policy_sid: str, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[VoiceV1ConnectionPolicyConnectionPolicyTarget]:
        """


        Parameters
        ----------
        connection_policy_sid : str
            The SID of the Connection Policy that owns the Target.

        sid : str
            The unique string that we created to identify the Target resource to fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[VoiceV1ConnectionPolicyConnectionPolicyTarget]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/ConnectionPolicies/{jsonable_encoder(connection_policy_sid)}/Targets/{jsonable_encoder(sid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VoiceV1ConnectionPolicyConnectionPolicyTarget,
                    parse_obj_as(
                        type_=VoiceV1ConnectionPolicyConnectionPolicyTarget,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_connection_policy_target(
        self,
        connection_policy_sid: str,
        sid: str,
        *,
        enabled: typing.Optional[bool] = OMIT,
        friendly_name: typing.Optional[str] = OMIT,
        priority: typing.Optional[int] = OMIT,
        target: typing.Optional[str] = OMIT,
        weight: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[VoiceV1ConnectionPolicyConnectionPolicyTarget]:
        """


        Parameters
        ----------
        connection_policy_sid : str
            The SID of the Connection Policy that owns the Target.

        sid : str
            The unique string that we created to identify the Target resource to update.

        enabled : typing.Optional[bool]
            Whether the Target is enabled.

        friendly_name : typing.Optional[str]
            A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.

        priority : typing.Optional[int]
            The relative importance of the target. Can be an integer from 0 to 65535, inclusive. The lowest number represents the most important target.

        target : typing.Optional[str]
            The SIP address you want Twilio to route your calls to. This must be a `sip:` schema. `sips` is NOT supported.

        weight : typing.Optional[int]
            The value that determines the relative share of the load the Target should receive compared to other Targets with the same priority. Can be an integer from 1 to 65535, inclusive. Targets with higher values receive more load than those with lower ones with the same priority.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[VoiceV1ConnectionPolicyConnectionPolicyTarget]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/ConnectionPolicies/{jsonable_encoder(connection_policy_sid)}/Targets/{jsonable_encoder(sid)}",
            method="POST",
            data={
                "Enabled": enabled,
                "FriendlyName": friendly_name,
                "Priority": priority,
                "Target": target,
                "Weight": weight,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VoiceV1ConnectionPolicyConnectionPolicyTarget,
                    parse_obj_as(
                        type_=VoiceV1ConnectionPolicyConnectionPolicyTarget,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_connection_policy_target(
        self, connection_policy_sid: str, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """


        Parameters
        ----------
        connection_policy_sid : str
            The SID of the Connection Policy that owns the Target.

        sid : str
            The unique string that we created to identify the Target resource to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/ConnectionPolicies/{jsonable_encoder(connection_policy_sid)}/Targets/{jsonable_encoder(sid)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def fetch_connection_policy(
        self, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[VoiceV1ConnectionPolicy]:
        """


        Parameters
        ----------
        sid : str
            The unique string that we created to identify the Connection Policy resource to fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[VoiceV1ConnectionPolicy]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/ConnectionPolicies/{jsonable_encoder(sid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VoiceV1ConnectionPolicy,
                    parse_obj_as(
                        type_=VoiceV1ConnectionPolicy,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_connection_policy(
        self,
        sid: str,
        *,
        friendly_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[VoiceV1ConnectionPolicy]:
        """


        Parameters
        ----------
        sid : str
            The unique string that we created to identify the Connection Policy resource to update.

        friendly_name : typing.Optional[str]
            A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[VoiceV1ConnectionPolicy]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/ConnectionPolicies/{jsonable_encoder(sid)}",
            method="POST",
            data={
                "FriendlyName": friendly_name,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VoiceV1ConnectionPolicy,
                    parse_obj_as(
                        type_=VoiceV1ConnectionPolicy,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_connection_policy(
        self, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """


        Parameters
        ----------
        sid : str
            The unique string that we created to identify the Connection Policy resource to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/ConnectionPolicies/{jsonable_encoder(sid)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_dialing_permissions_country_bulk_update(
        self, *, update_request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[VoiceV1DialingPermissionsDialingPermissionsCountryBulkUpdate]:
        """
        Create a bulk update request to change voice dialing country permissions of one or more countries identified by the corresponding [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)

        Parameters
        ----------
        update_request : str
            URL encoded JSON array of update objects. example : `[ { "iso_code": "GB", "low_risk_numbers_enabled": "true", "high_risk_special_numbers_enabled":"true", "high_risk_tollfraud_numbers_enabled": "false" } ]`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[VoiceV1DialingPermissionsDialingPermissionsCountryBulkUpdate]
            Created
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/DialingPermissions/BulkCountryUpdates",
            method="POST",
            data={
                "UpdateRequest": update_request,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VoiceV1DialingPermissionsDialingPermissionsCountryBulkUpdate,
                    parse_obj_as(
                        type_=VoiceV1DialingPermissionsDialingPermissionsCountryBulkUpdate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_dialing_permissions_country(
        self,
        *,
        iso_code: typing.Optional[str] = None,
        continent: typing.Optional[str] = None,
        country_code: typing.Optional[str] = None,
        low_risk_numbers_enabled: typing.Optional[bool] = None,
        high_risk_special_numbers_enabled: typing.Optional[bool] = None,
        high_risk_tollfraud_numbers_enabled: typing.Optional[bool] = None,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListDialingPermissionsCountryResponse]:
        """
        Retrieve all voice dialing country permissions for this account

        Parameters
        ----------
        iso_code : typing.Optional[str]
            Filter to retrieve the country permissions by specifying the [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)

        continent : typing.Optional[str]
            Filter to retrieve the country permissions by specifying the continent

        country_code : typing.Optional[str]
            Filter the results by specified [country codes](https://www.itu.int/itudoc/itu-t/ob-lists/icc/e164_763.html)

        low_risk_numbers_enabled : typing.Optional[bool]
            Filter to retrieve the country permissions with dialing to low-risk numbers enabled. Can be: `true` or `false`.

        high_risk_special_numbers_enabled : typing.Optional[bool]
            Filter to retrieve the country permissions with dialing to high-risk special service numbers enabled. Can be: `true` or `false`

        high_risk_tollfraud_numbers_enabled : typing.Optional[bool]
            Filter to retrieve the country permissions with dialing to high-risk [toll fraud](https://www.twilio.com/learn/voice-and-video/toll-fraud) numbers enabled. Can be: `true` or `false`.

        page_size : typing.Optional[int]
            How many resources to return in each list page. The default is 50, and the maximum is 1000.

        page : typing.Optional[int]
            The page index. This value is simply for client state.

        page_token : typing.Optional[str]
            The page token. This is provided by the API.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListDialingPermissionsCountryResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/DialingPermissions/Countries",
            method="GET",
            params={
                "IsoCode": iso_code,
                "Continent": continent,
                "CountryCode": country_code,
                "LowRiskNumbersEnabled": low_risk_numbers_enabled,
                "HighRiskSpecialNumbersEnabled": high_risk_special_numbers_enabled,
                "HighRiskTollfraudNumbersEnabled": high_risk_tollfraud_numbers_enabled,
                "PageSize": page_size,
                "Page": page,
                "PageToken": page_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListDialingPermissionsCountryResponse,
                    parse_obj_as(
                        type_=ListDialingPermissionsCountryResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def fetch_dialing_permissions_country(
        self, iso_code: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[VoiceV1DialingPermissionsDialingPermissionsCountryInstance]:
        """
        Retrieve voice dialing country permissions identified by the given ISO country code

        Parameters
        ----------
        iso_code : str
            The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the DialingPermissions Country resource to fetch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[VoiceV1DialingPermissionsDialingPermissionsCountryInstance]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/DialingPermissions/Countries/{jsonable_encoder(iso_code)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VoiceV1DialingPermissionsDialingPermissionsCountryInstance,
                    parse_obj_as(
                        type_=VoiceV1DialingPermissionsDialingPermissionsCountryInstance,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_dialing_permissions_hrs_prefixes(
        self,
        iso_code: str,
        *,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListDialingPermissionsHrsPrefixesResponse]:
        """
        Fetch the high-risk special services prefixes from the country resource corresponding to the [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)

        Parameters
        ----------
        iso_code : str
            The [ISO 3166-1 country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) to identify the country permissions from which high-risk special service number prefixes are fetched

        page_size : typing.Optional[int]
            How many resources to return in each list page. The default is 50, and the maximum is 1000.

        page : typing.Optional[int]
            The page index. This value is simply for client state.

        page_token : typing.Optional[str]
            The page token. This is provided by the API.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListDialingPermissionsHrsPrefixesResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/DialingPermissions/Countries/{jsonable_encoder(iso_code)}/HighRiskSpecialPrefixes",
            method="GET",
            params={
                "PageSize": page_size,
                "Page": page,
                "PageToken": page_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListDialingPermissionsHrsPrefixesResponse,
                    parse_obj_as(
                        type_=ListDialingPermissionsHrsPrefixesResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_ip_record(
        self,
        *,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListIpRecordResponse]:
        """


        Parameters
        ----------
        page_size : typing.Optional[int]
            How many resources to return in each list page. The default is 50, and the maximum is 1000.

        page : typing.Optional[int]
            The page index. This value is simply for client state.

        page_token : typing.Optional[str]
            The page token. This is provided by the API.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListIpRecordResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/IpRecords",
            method="GET",
            params={
                "PageSize": page_size,
                "Page": page,
                "PageToken": page_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListIpRecordResponse,
                    parse_obj_as(
                        type_=ListIpRecordResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_ip_record(
        self,
        *,
        ip_address: str,
        cidr_prefix_length: typing.Optional[int] = OMIT,
        friendly_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[VoiceV1IpRecord]:
        """


        Parameters
        ----------
        ip_address : str
            An IP address in dotted decimal notation, IPv4 only.

        cidr_prefix_length : typing.Optional[int]
            An integer representing the length of the [CIDR](https://tools.ietf.org/html/rfc4632) prefix to use with this IP address. By default the entire IP address is used, which for IPv4 is value 32.

        friendly_name : typing.Optional[str]
            A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[VoiceV1IpRecord]
            Created
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/IpRecords",
            method="POST",
            data={
                "CidrPrefixLength": cidr_prefix_length,
                "FriendlyName": friendly_name,
                "IpAddress": ip_address,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VoiceV1IpRecord,
                    parse_obj_as(
                        type_=VoiceV1IpRecord,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def fetch_ip_record(
        self, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[VoiceV1IpRecord]:
        """


        Parameters
        ----------
        sid : str
            The Twilio-provided string that uniquely identifies the IP Record resource to fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[VoiceV1IpRecord]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/IpRecords/{jsonable_encoder(sid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VoiceV1IpRecord,
                    parse_obj_as(
                        type_=VoiceV1IpRecord,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_ip_record(
        self,
        sid: str,
        *,
        friendly_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[VoiceV1IpRecord]:
        """


        Parameters
        ----------
        sid : str
            The Twilio-provided string that uniquely identifies the IP Record resource to update.

        friendly_name : typing.Optional[str]
            A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[VoiceV1IpRecord]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/IpRecords/{jsonable_encoder(sid)}",
            method="POST",
            data={
                "FriendlyName": friendly_name,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VoiceV1IpRecord,
                    parse_obj_as(
                        type_=VoiceV1IpRecord,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_ip_record(
        self, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """


        Parameters
        ----------
        sid : str
            The Twilio-provided string that uniquely identifies the IP Record resource to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/IpRecords/{jsonable_encoder(sid)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def fetch_dialing_permissions_settings(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[VoiceV1DialingPermissionsDialingPermissionsSettings]:
        """
        Retrieve voice dialing permissions inheritance for the sub-account

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[VoiceV1DialingPermissionsDialingPermissionsSettings]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/Settings",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VoiceV1DialingPermissionsDialingPermissionsSettings,
                    parse_obj_as(
                        type_=VoiceV1DialingPermissionsDialingPermissionsSettings,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_dialing_permissions_settings(
        self,
        *,
        dialing_permissions_inheritance: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[VoiceV1DialingPermissionsDialingPermissionsSettings]:
        """
        Update voice dialing permissions inheritance for the sub-account

        Parameters
        ----------
        dialing_permissions_inheritance : typing.Optional[bool]
            `true` for the sub-account to inherit voice dialing permissions from the Master Project; otherwise `false`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[VoiceV1DialingPermissionsDialingPermissionsSettings]
            Accepted
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/Settings",
            method="POST",
            data={
                "DialingPermissionsInheritance": dialing_permissions_inheritance,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VoiceV1DialingPermissionsDialingPermissionsSettings,
                    parse_obj_as(
                        type_=VoiceV1DialingPermissionsDialingPermissionsSettings,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_source_ip_mapping(
        self,
        *,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListSourceIpMappingResponse]:
        """


        Parameters
        ----------
        page_size : typing.Optional[int]
            How many resources to return in each list page. The default is 50, and the maximum is 1000.

        page : typing.Optional[int]
            The page index. This value is simply for client state.

        page_token : typing.Optional[str]
            The page token. This is provided by the API.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListSourceIpMappingResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/SourceIpMappings",
            method="GET",
            params={
                "PageSize": page_size,
                "Page": page,
                "PageToken": page_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListSourceIpMappingResponse,
                    parse_obj_as(
                        type_=ListSourceIpMappingResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_source_ip_mapping(
        self, *, ip_record_sid: str, sip_domain_sid: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[VoiceV1SourceIpMapping]:
        """


        Parameters
        ----------
        ip_record_sid : str
            The Twilio-provided string that uniquely identifies the IP Record resource to map from.

        sip_domain_sid : str
            The SID of the SIP Domain that the IP Record should be mapped to.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[VoiceV1SourceIpMapping]
            Created
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/SourceIpMappings",
            method="POST",
            data={
                "IpRecordSid": ip_record_sid,
                "SipDomainSid": sip_domain_sid,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VoiceV1SourceIpMapping,
                    parse_obj_as(
                        type_=VoiceV1SourceIpMapping,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def fetch_source_ip_mapping(
        self, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[VoiceV1SourceIpMapping]:
        """


        Parameters
        ----------
        sid : str
            The Twilio-provided string that uniquely identifies the IP Record resource to fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[VoiceV1SourceIpMapping]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/SourceIpMappings/{jsonable_encoder(sid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VoiceV1SourceIpMapping,
                    parse_obj_as(
                        type_=VoiceV1SourceIpMapping,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_source_ip_mapping(
        self, sid: str, *, sip_domain_sid: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[VoiceV1SourceIpMapping]:
        """


        Parameters
        ----------
        sid : str
            The Twilio-provided string that uniquely identifies the IP Record resource to update.

        sip_domain_sid : str
            The SID of the SIP Domain that the IP Record should be mapped to.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[VoiceV1SourceIpMapping]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/SourceIpMappings/{jsonable_encoder(sid)}",
            method="POST",
            data={
                "SipDomainSid": sip_domain_sid,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VoiceV1SourceIpMapping,
                    parse_obj_as(
                        type_=VoiceV1SourceIpMapping,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_source_ip_mapping(
        self, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """


        Parameters
        ----------
        sid : str
            The Twilio-provided string that uniquely identifies the IP Record resource to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/SourceIpMappings/{jsonable_encoder(sid)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawFernApi:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def delete_archived_call(
        self, date: dt.date, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Delete an archived call record from Bulk Export. Note: this does not also delete the record from the Voice API.

        Parameters
        ----------
        date : dt.date
            The date of the Call in UTC.

        sid : str
            The Twilio-provided Call SID that uniquely identifies the Call resource to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/Archives/{jsonable_encoder(date)}/Calls/{jsonable_encoder(sid)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_byoc_trunk(
        self,
        *,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListByocTrunkResponse]:
        """


        Parameters
        ----------
        page_size : typing.Optional[int]
            How many resources to return in each list page. The default is 50, and the maximum is 1000.

        page : typing.Optional[int]
            The page index. This value is simply for client state.

        page_token : typing.Optional[str]
            The page token. This is provided by the API.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListByocTrunkResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/ByocTrunks",
            method="GET",
            params={
                "PageSize": page_size,
                "Page": page,
                "PageToken": page_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListByocTrunkResponse,
                    parse_obj_as(
                        type_=ListByocTrunkResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_byoc_trunk(
        self,
        *,
        cnam_lookup_enabled: typing.Optional[bool] = OMIT,
        connection_policy_sid: typing.Optional[str] = OMIT,
        friendly_name: typing.Optional[str] = OMIT,
        from_domain_sid: typing.Optional[str] = OMIT,
        status_callback_method: typing.Optional[CreateByocTrunkRequestStatusCallbackMethod] = OMIT,
        status_callback_url: typing.Optional[str] = OMIT,
        voice_fallback_method: typing.Optional[CreateByocTrunkRequestVoiceFallbackMethod] = OMIT,
        voice_fallback_url: typing.Optional[str] = OMIT,
        voice_method: typing.Optional[CreateByocTrunkRequestVoiceMethod] = OMIT,
        voice_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[VoiceV1ByocTrunk]:
        """


        Parameters
        ----------
        cnam_lookup_enabled : typing.Optional[bool]
            Whether Caller ID Name (CNAM) lookup is enabled for the trunk. If enabled, all inbound calls to the BYOC Trunk from the United States and Canada automatically perform a CNAM Lookup and display Caller ID data on your phone. See [CNAM Lookups](https://www.twilio.com/docs/sip-trunking#CNAM) for more information.

        connection_policy_sid : typing.Optional[str]
            The SID of the Connection Policy that Twilio will use when routing traffic to your communications infrastructure.

        friendly_name : typing.Optional[str]
            A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.

        from_domain_sid : typing.Optional[str]
            The SID of the SIP Domain that should be used in the `From` header of originating calls sent to your SIP infrastructure. If your SIP infrastructure allows users to "call back" an incoming call, configure this with a [SIP Domain](https://www.twilio.com/docs/voice/api/sending-sip) to ensure proper routing. If not configured, the from domain will default to "sip.twilio.com".

        status_callback_method : typing.Optional[CreateByocTrunkRequestStatusCallbackMethod]
            The HTTP method we should use to call `status_callback_url`. Can be: `GET` or `POST`.

        status_callback_url : typing.Optional[str]
            The URL that we should call to pass status parameters (such as call ended) to your application.

        voice_fallback_method : typing.Optional[CreateByocTrunkRequestVoiceFallbackMethod]
            The HTTP method we should use to call `voice_fallback_url`. Can be: `GET` or `POST`.

        voice_fallback_url : typing.Optional[str]
            The URL that we should call when an error occurs while retrieving or executing the TwiML from `voice_url`.

        voice_method : typing.Optional[CreateByocTrunkRequestVoiceMethod]
            The HTTP method we should use to call `voice_url`. Can be: `GET` or `POST`.

        voice_url : typing.Optional[str]
            The URL we should call when the BYOC Trunk receives a call.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[VoiceV1ByocTrunk]
            Created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/ByocTrunks",
            method="POST",
            data={
                "CnamLookupEnabled": cnam_lookup_enabled,
                "ConnectionPolicySid": connection_policy_sid,
                "FriendlyName": friendly_name,
                "FromDomainSid": from_domain_sid,
                "StatusCallbackMethod": status_callback_method,
                "StatusCallbackUrl": status_callback_url,
                "VoiceFallbackMethod": voice_fallback_method,
                "VoiceFallbackUrl": voice_fallback_url,
                "VoiceMethod": voice_method,
                "VoiceUrl": voice_url,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VoiceV1ByocTrunk,
                    parse_obj_as(
                        type_=VoiceV1ByocTrunk,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def fetch_byoc_trunk(
        self, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[VoiceV1ByocTrunk]:
        """


        Parameters
        ----------
        sid : str
            The Twilio-provided string that uniquely identifies the BYOC Trunk resource to fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[VoiceV1ByocTrunk]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/ByocTrunks/{jsonable_encoder(sid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VoiceV1ByocTrunk,
                    parse_obj_as(
                        type_=VoiceV1ByocTrunk,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_byoc_trunk(
        self,
        sid: str,
        *,
        cnam_lookup_enabled: typing.Optional[bool] = OMIT,
        connection_policy_sid: typing.Optional[str] = OMIT,
        friendly_name: typing.Optional[str] = OMIT,
        from_domain_sid: typing.Optional[str] = OMIT,
        status_callback_method: typing.Optional[UpdateByocTrunkRequestStatusCallbackMethod] = OMIT,
        status_callback_url: typing.Optional[str] = OMIT,
        voice_fallback_method: typing.Optional[UpdateByocTrunkRequestVoiceFallbackMethod] = OMIT,
        voice_fallback_url: typing.Optional[str] = OMIT,
        voice_method: typing.Optional[UpdateByocTrunkRequestVoiceMethod] = OMIT,
        voice_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[VoiceV1ByocTrunk]:
        """


        Parameters
        ----------
        sid : str
            The Twilio-provided string that uniquely identifies the BYOC Trunk resource to update.

        cnam_lookup_enabled : typing.Optional[bool]
            Whether Caller ID Name (CNAM) lookup is enabled for the trunk. If enabled, all inbound calls to the BYOC Trunk from the United States and Canada automatically perform a CNAM Lookup and display Caller ID data on your phone. See [CNAM Lookups](https://www.twilio.com/docs/sip-trunking#CNAM) for more information.

        connection_policy_sid : typing.Optional[str]
            The SID of the Connection Policy that Twilio will use when routing traffic to your communications infrastructure.

        friendly_name : typing.Optional[str]
            A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.

        from_domain_sid : typing.Optional[str]
            The SID of the SIP Domain that should be used in the `From` header of originating calls sent to your SIP infrastructure. If your SIP infrastructure allows users to "call back" an incoming call, configure this with a [SIP Domain](https://www.twilio.com/docs/voice/api/sending-sip) to ensure proper routing. If not configured, the from domain will default to "sip.twilio.com".

        status_callback_method : typing.Optional[UpdateByocTrunkRequestStatusCallbackMethod]
            The HTTP method we should use to call `status_callback_url`. Can be: `GET` or `POST`.

        status_callback_url : typing.Optional[str]
            The URL that we should call to pass status parameters (such as call ended) to your application.

        voice_fallback_method : typing.Optional[UpdateByocTrunkRequestVoiceFallbackMethod]
            The HTTP method we should use to call `voice_fallback_url`. Can be: `GET` or `POST`.

        voice_fallback_url : typing.Optional[str]
            The URL that we should call when an error occurs while retrieving or executing the TwiML requested by `voice_url`.

        voice_method : typing.Optional[UpdateByocTrunkRequestVoiceMethod]
            The HTTP method we should use to call `voice_url`

        voice_url : typing.Optional[str]
            The URL we should call when the BYOC Trunk receives a call.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[VoiceV1ByocTrunk]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/ByocTrunks/{jsonable_encoder(sid)}",
            method="POST",
            data={
                "CnamLookupEnabled": cnam_lookup_enabled,
                "ConnectionPolicySid": connection_policy_sid,
                "FriendlyName": friendly_name,
                "FromDomainSid": from_domain_sid,
                "StatusCallbackMethod": status_callback_method,
                "StatusCallbackUrl": status_callback_url,
                "VoiceFallbackMethod": voice_fallback_method,
                "VoiceFallbackUrl": voice_fallback_url,
                "VoiceMethod": voice_method,
                "VoiceUrl": voice_url,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VoiceV1ByocTrunk,
                    parse_obj_as(
                        type_=VoiceV1ByocTrunk,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_byoc_trunk(
        self, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """


        Parameters
        ----------
        sid : str
            The Twilio-provided string that uniquely identifies the BYOC Trunk resource to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/ByocTrunks/{jsonable_encoder(sid)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_connection_policy(
        self,
        *,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListConnectionPolicyResponse]:
        """


        Parameters
        ----------
        page_size : typing.Optional[int]
            How many resources to return in each list page. The default is 50, and the maximum is 1000.

        page : typing.Optional[int]
            The page index. This value is simply for client state.

        page_token : typing.Optional[str]
            The page token. This is provided by the API.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListConnectionPolicyResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/ConnectionPolicies",
            method="GET",
            params={
                "PageSize": page_size,
                "Page": page,
                "PageToken": page_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListConnectionPolicyResponse,
                    parse_obj_as(
                        type_=ListConnectionPolicyResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_connection_policy(
        self, *, friendly_name: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[VoiceV1ConnectionPolicy]:
        """


        Parameters
        ----------
        friendly_name : typing.Optional[str]
            A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[VoiceV1ConnectionPolicy]
            Created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/ConnectionPolicies",
            method="POST",
            data={
                "FriendlyName": friendly_name,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VoiceV1ConnectionPolicy,
                    parse_obj_as(
                        type_=VoiceV1ConnectionPolicy,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_connection_policy_target(
        self,
        connection_policy_sid: str,
        *,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListConnectionPolicyTargetResponse]:
        """


        Parameters
        ----------
        connection_policy_sid : str
            The SID of the Connection Policy from which to read the Targets.

        page_size : typing.Optional[int]
            How many resources to return in each list page. The default is 50, and the maximum is 1000.

        page : typing.Optional[int]
            The page index. This value is simply for client state.

        page_token : typing.Optional[str]
            The page token. This is provided by the API.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListConnectionPolicyTargetResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/ConnectionPolicies/{jsonable_encoder(connection_policy_sid)}/Targets",
            method="GET",
            params={
                "PageSize": page_size,
                "Page": page,
                "PageToken": page_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListConnectionPolicyTargetResponse,
                    parse_obj_as(
                        type_=ListConnectionPolicyTargetResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_connection_policy_target(
        self,
        connection_policy_sid: str,
        *,
        target: str,
        enabled: typing.Optional[bool] = OMIT,
        friendly_name: typing.Optional[str] = OMIT,
        priority: typing.Optional[int] = OMIT,
        weight: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[VoiceV1ConnectionPolicyConnectionPolicyTarget]:
        """


        Parameters
        ----------
        connection_policy_sid : str
            The SID of the Connection Policy that owns the Target.

        target : str
            The SIP address you want Twilio to route your calls to. This must be a `sip:` schema. `sips` is NOT supported.

        enabled : typing.Optional[bool]
            Whether the Target is enabled. The default is `true`.

        friendly_name : typing.Optional[str]
            A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.

        priority : typing.Optional[int]
            The relative importance of the target. Can be an integer from 0 to 65535, inclusive, and the default is 10. The lowest number represents the most important target.

        weight : typing.Optional[int]
            The value that determines the relative share of the load the Target should receive compared to other Targets with the same priority. Can be an integer from 1 to 65535, inclusive, and the default is 10. Targets with higher values receive more load than those with lower ones with the same priority.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[VoiceV1ConnectionPolicyConnectionPolicyTarget]
            Created
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/ConnectionPolicies/{jsonable_encoder(connection_policy_sid)}/Targets",
            method="POST",
            data={
                "Enabled": enabled,
                "FriendlyName": friendly_name,
                "Priority": priority,
                "Target": target,
                "Weight": weight,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VoiceV1ConnectionPolicyConnectionPolicyTarget,
                    parse_obj_as(
                        type_=VoiceV1ConnectionPolicyConnectionPolicyTarget,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def fetch_connection_policy_target(
        self, connection_policy_sid: str, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[VoiceV1ConnectionPolicyConnectionPolicyTarget]:
        """


        Parameters
        ----------
        connection_policy_sid : str
            The SID of the Connection Policy that owns the Target.

        sid : str
            The unique string that we created to identify the Target resource to fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[VoiceV1ConnectionPolicyConnectionPolicyTarget]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/ConnectionPolicies/{jsonable_encoder(connection_policy_sid)}/Targets/{jsonable_encoder(sid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VoiceV1ConnectionPolicyConnectionPolicyTarget,
                    parse_obj_as(
                        type_=VoiceV1ConnectionPolicyConnectionPolicyTarget,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_connection_policy_target(
        self,
        connection_policy_sid: str,
        sid: str,
        *,
        enabled: typing.Optional[bool] = OMIT,
        friendly_name: typing.Optional[str] = OMIT,
        priority: typing.Optional[int] = OMIT,
        target: typing.Optional[str] = OMIT,
        weight: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[VoiceV1ConnectionPolicyConnectionPolicyTarget]:
        """


        Parameters
        ----------
        connection_policy_sid : str
            The SID of the Connection Policy that owns the Target.

        sid : str
            The unique string that we created to identify the Target resource to update.

        enabled : typing.Optional[bool]
            Whether the Target is enabled.

        friendly_name : typing.Optional[str]
            A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.

        priority : typing.Optional[int]
            The relative importance of the target. Can be an integer from 0 to 65535, inclusive. The lowest number represents the most important target.

        target : typing.Optional[str]
            The SIP address you want Twilio to route your calls to. This must be a `sip:` schema. `sips` is NOT supported.

        weight : typing.Optional[int]
            The value that determines the relative share of the load the Target should receive compared to other Targets with the same priority. Can be an integer from 1 to 65535, inclusive. Targets with higher values receive more load than those with lower ones with the same priority.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[VoiceV1ConnectionPolicyConnectionPolicyTarget]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/ConnectionPolicies/{jsonable_encoder(connection_policy_sid)}/Targets/{jsonable_encoder(sid)}",
            method="POST",
            data={
                "Enabled": enabled,
                "FriendlyName": friendly_name,
                "Priority": priority,
                "Target": target,
                "Weight": weight,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VoiceV1ConnectionPolicyConnectionPolicyTarget,
                    parse_obj_as(
                        type_=VoiceV1ConnectionPolicyConnectionPolicyTarget,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_connection_policy_target(
        self, connection_policy_sid: str, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """


        Parameters
        ----------
        connection_policy_sid : str
            The SID of the Connection Policy that owns the Target.

        sid : str
            The unique string that we created to identify the Target resource to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/ConnectionPolicies/{jsonable_encoder(connection_policy_sid)}/Targets/{jsonable_encoder(sid)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def fetch_connection_policy(
        self, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[VoiceV1ConnectionPolicy]:
        """


        Parameters
        ----------
        sid : str
            The unique string that we created to identify the Connection Policy resource to fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[VoiceV1ConnectionPolicy]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/ConnectionPolicies/{jsonable_encoder(sid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VoiceV1ConnectionPolicy,
                    parse_obj_as(
                        type_=VoiceV1ConnectionPolicy,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_connection_policy(
        self,
        sid: str,
        *,
        friendly_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[VoiceV1ConnectionPolicy]:
        """


        Parameters
        ----------
        sid : str
            The unique string that we created to identify the Connection Policy resource to update.

        friendly_name : typing.Optional[str]
            A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[VoiceV1ConnectionPolicy]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/ConnectionPolicies/{jsonable_encoder(sid)}",
            method="POST",
            data={
                "FriendlyName": friendly_name,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VoiceV1ConnectionPolicy,
                    parse_obj_as(
                        type_=VoiceV1ConnectionPolicy,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_connection_policy(
        self, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """


        Parameters
        ----------
        sid : str
            The unique string that we created to identify the Connection Policy resource to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/ConnectionPolicies/{jsonable_encoder(sid)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_dialing_permissions_country_bulk_update(
        self, *, update_request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[VoiceV1DialingPermissionsDialingPermissionsCountryBulkUpdate]:
        """
        Create a bulk update request to change voice dialing country permissions of one or more countries identified by the corresponding [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)

        Parameters
        ----------
        update_request : str
            URL encoded JSON array of update objects. example : `[ { "iso_code": "GB", "low_risk_numbers_enabled": "true", "high_risk_special_numbers_enabled":"true", "high_risk_tollfraud_numbers_enabled": "false" } ]`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[VoiceV1DialingPermissionsDialingPermissionsCountryBulkUpdate]
            Created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/DialingPermissions/BulkCountryUpdates",
            method="POST",
            data={
                "UpdateRequest": update_request,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VoiceV1DialingPermissionsDialingPermissionsCountryBulkUpdate,
                    parse_obj_as(
                        type_=VoiceV1DialingPermissionsDialingPermissionsCountryBulkUpdate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_dialing_permissions_country(
        self,
        *,
        iso_code: typing.Optional[str] = None,
        continent: typing.Optional[str] = None,
        country_code: typing.Optional[str] = None,
        low_risk_numbers_enabled: typing.Optional[bool] = None,
        high_risk_special_numbers_enabled: typing.Optional[bool] = None,
        high_risk_tollfraud_numbers_enabled: typing.Optional[bool] = None,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListDialingPermissionsCountryResponse]:
        """
        Retrieve all voice dialing country permissions for this account

        Parameters
        ----------
        iso_code : typing.Optional[str]
            Filter to retrieve the country permissions by specifying the [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)

        continent : typing.Optional[str]
            Filter to retrieve the country permissions by specifying the continent

        country_code : typing.Optional[str]
            Filter the results by specified [country codes](https://www.itu.int/itudoc/itu-t/ob-lists/icc/e164_763.html)

        low_risk_numbers_enabled : typing.Optional[bool]
            Filter to retrieve the country permissions with dialing to low-risk numbers enabled. Can be: `true` or `false`.

        high_risk_special_numbers_enabled : typing.Optional[bool]
            Filter to retrieve the country permissions with dialing to high-risk special service numbers enabled. Can be: `true` or `false`

        high_risk_tollfraud_numbers_enabled : typing.Optional[bool]
            Filter to retrieve the country permissions with dialing to high-risk [toll fraud](https://www.twilio.com/learn/voice-and-video/toll-fraud) numbers enabled. Can be: `true` or `false`.

        page_size : typing.Optional[int]
            How many resources to return in each list page. The default is 50, and the maximum is 1000.

        page : typing.Optional[int]
            The page index. This value is simply for client state.

        page_token : typing.Optional[str]
            The page token. This is provided by the API.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListDialingPermissionsCountryResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/DialingPermissions/Countries",
            method="GET",
            params={
                "IsoCode": iso_code,
                "Continent": continent,
                "CountryCode": country_code,
                "LowRiskNumbersEnabled": low_risk_numbers_enabled,
                "HighRiskSpecialNumbersEnabled": high_risk_special_numbers_enabled,
                "HighRiskTollfraudNumbersEnabled": high_risk_tollfraud_numbers_enabled,
                "PageSize": page_size,
                "Page": page,
                "PageToken": page_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListDialingPermissionsCountryResponse,
                    parse_obj_as(
                        type_=ListDialingPermissionsCountryResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def fetch_dialing_permissions_country(
        self, iso_code: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[VoiceV1DialingPermissionsDialingPermissionsCountryInstance]:
        """
        Retrieve voice dialing country permissions identified by the given ISO country code

        Parameters
        ----------
        iso_code : str
            The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the DialingPermissions Country resource to fetch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[VoiceV1DialingPermissionsDialingPermissionsCountryInstance]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/DialingPermissions/Countries/{jsonable_encoder(iso_code)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VoiceV1DialingPermissionsDialingPermissionsCountryInstance,
                    parse_obj_as(
                        type_=VoiceV1DialingPermissionsDialingPermissionsCountryInstance,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_dialing_permissions_hrs_prefixes(
        self,
        iso_code: str,
        *,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListDialingPermissionsHrsPrefixesResponse]:
        """
        Fetch the high-risk special services prefixes from the country resource corresponding to the [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)

        Parameters
        ----------
        iso_code : str
            The [ISO 3166-1 country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) to identify the country permissions from which high-risk special service number prefixes are fetched

        page_size : typing.Optional[int]
            How many resources to return in each list page. The default is 50, and the maximum is 1000.

        page : typing.Optional[int]
            The page index. This value is simply for client state.

        page_token : typing.Optional[str]
            The page token. This is provided by the API.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListDialingPermissionsHrsPrefixesResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/DialingPermissions/Countries/{jsonable_encoder(iso_code)}/HighRiskSpecialPrefixes",
            method="GET",
            params={
                "PageSize": page_size,
                "Page": page,
                "PageToken": page_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListDialingPermissionsHrsPrefixesResponse,
                    parse_obj_as(
                        type_=ListDialingPermissionsHrsPrefixesResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_ip_record(
        self,
        *,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListIpRecordResponse]:
        """


        Parameters
        ----------
        page_size : typing.Optional[int]
            How many resources to return in each list page. The default is 50, and the maximum is 1000.

        page : typing.Optional[int]
            The page index. This value is simply for client state.

        page_token : typing.Optional[str]
            The page token. This is provided by the API.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListIpRecordResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/IpRecords",
            method="GET",
            params={
                "PageSize": page_size,
                "Page": page,
                "PageToken": page_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListIpRecordResponse,
                    parse_obj_as(
                        type_=ListIpRecordResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_ip_record(
        self,
        *,
        ip_address: str,
        cidr_prefix_length: typing.Optional[int] = OMIT,
        friendly_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[VoiceV1IpRecord]:
        """


        Parameters
        ----------
        ip_address : str
            An IP address in dotted decimal notation, IPv4 only.

        cidr_prefix_length : typing.Optional[int]
            An integer representing the length of the [CIDR](https://tools.ietf.org/html/rfc4632) prefix to use with this IP address. By default the entire IP address is used, which for IPv4 is value 32.

        friendly_name : typing.Optional[str]
            A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[VoiceV1IpRecord]
            Created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/IpRecords",
            method="POST",
            data={
                "CidrPrefixLength": cidr_prefix_length,
                "FriendlyName": friendly_name,
                "IpAddress": ip_address,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VoiceV1IpRecord,
                    parse_obj_as(
                        type_=VoiceV1IpRecord,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def fetch_ip_record(
        self, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[VoiceV1IpRecord]:
        """


        Parameters
        ----------
        sid : str
            The Twilio-provided string that uniquely identifies the IP Record resource to fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[VoiceV1IpRecord]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/IpRecords/{jsonable_encoder(sid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VoiceV1IpRecord,
                    parse_obj_as(
                        type_=VoiceV1IpRecord,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_ip_record(
        self,
        sid: str,
        *,
        friendly_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[VoiceV1IpRecord]:
        """


        Parameters
        ----------
        sid : str
            The Twilio-provided string that uniquely identifies the IP Record resource to update.

        friendly_name : typing.Optional[str]
            A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[VoiceV1IpRecord]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/IpRecords/{jsonable_encoder(sid)}",
            method="POST",
            data={
                "FriendlyName": friendly_name,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VoiceV1IpRecord,
                    parse_obj_as(
                        type_=VoiceV1IpRecord,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_ip_record(
        self, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """


        Parameters
        ----------
        sid : str
            The Twilio-provided string that uniquely identifies the IP Record resource to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/IpRecords/{jsonable_encoder(sid)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def fetch_dialing_permissions_settings(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[VoiceV1DialingPermissionsDialingPermissionsSettings]:
        """
        Retrieve voice dialing permissions inheritance for the sub-account

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[VoiceV1DialingPermissionsDialingPermissionsSettings]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/Settings",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VoiceV1DialingPermissionsDialingPermissionsSettings,
                    parse_obj_as(
                        type_=VoiceV1DialingPermissionsDialingPermissionsSettings,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_dialing_permissions_settings(
        self,
        *,
        dialing_permissions_inheritance: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[VoiceV1DialingPermissionsDialingPermissionsSettings]:
        """
        Update voice dialing permissions inheritance for the sub-account

        Parameters
        ----------
        dialing_permissions_inheritance : typing.Optional[bool]
            `true` for the sub-account to inherit voice dialing permissions from the Master Project; otherwise `false`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[VoiceV1DialingPermissionsDialingPermissionsSettings]
            Accepted
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/Settings",
            method="POST",
            data={
                "DialingPermissionsInheritance": dialing_permissions_inheritance,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VoiceV1DialingPermissionsDialingPermissionsSettings,
                    parse_obj_as(
                        type_=VoiceV1DialingPermissionsDialingPermissionsSettings,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_source_ip_mapping(
        self,
        *,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListSourceIpMappingResponse]:
        """


        Parameters
        ----------
        page_size : typing.Optional[int]
            How many resources to return in each list page. The default is 50, and the maximum is 1000.

        page : typing.Optional[int]
            The page index. This value is simply for client state.

        page_token : typing.Optional[str]
            The page token. This is provided by the API.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListSourceIpMappingResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/SourceIpMappings",
            method="GET",
            params={
                "PageSize": page_size,
                "Page": page,
                "PageToken": page_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListSourceIpMappingResponse,
                    parse_obj_as(
                        type_=ListSourceIpMappingResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_source_ip_mapping(
        self, *, ip_record_sid: str, sip_domain_sid: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[VoiceV1SourceIpMapping]:
        """


        Parameters
        ----------
        ip_record_sid : str
            The Twilio-provided string that uniquely identifies the IP Record resource to map from.

        sip_domain_sid : str
            The SID of the SIP Domain that the IP Record should be mapped to.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[VoiceV1SourceIpMapping]
            Created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/SourceIpMappings",
            method="POST",
            data={
                "IpRecordSid": ip_record_sid,
                "SipDomainSid": sip_domain_sid,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VoiceV1SourceIpMapping,
                    parse_obj_as(
                        type_=VoiceV1SourceIpMapping,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def fetch_source_ip_mapping(
        self, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[VoiceV1SourceIpMapping]:
        """


        Parameters
        ----------
        sid : str
            The Twilio-provided string that uniquely identifies the IP Record resource to fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[VoiceV1SourceIpMapping]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/SourceIpMappings/{jsonable_encoder(sid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VoiceV1SourceIpMapping,
                    parse_obj_as(
                        type_=VoiceV1SourceIpMapping,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_source_ip_mapping(
        self, sid: str, *, sip_domain_sid: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[VoiceV1SourceIpMapping]:
        """


        Parameters
        ----------
        sid : str
            The Twilio-provided string that uniquely identifies the IP Record resource to update.

        sip_domain_sid : str
            The SID of the SIP Domain that the IP Record should be mapped to.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[VoiceV1SourceIpMapping]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/SourceIpMappings/{jsonable_encoder(sid)}",
            method="POST",
            data={
                "SipDomainSid": sip_domain_sid,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VoiceV1SourceIpMapping,
                    parse_obj_as(
                        type_=VoiceV1SourceIpMapping,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_source_ip_mapping(
        self, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """


        Parameters
        ----------
        sid : str
            The Twilio-provided string that uniquely identifies the IP Record resource to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/SourceIpMappings/{jsonable_encoder(sid)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

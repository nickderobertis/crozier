

import datetime as dt
import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.request_options import RequestOptions
from .environment import FernApiEnvironment
from .raw_client import AsyncRawFernApi, RawFernApi
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


class FernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : FernApiEnvironment
        The environment to use for requests from the client. from .environment import FernApiEnvironment



        Defaults to FernApiEnvironment.DEFAULT



    username : typing.Union[str, typing.Callable[[], str]]
    password : typing.Union[str, typing.Callable[[], str]]
    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.Client]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    Examples
    --------
    from fern import FernApi

    client = FernApi(
        username="YOUR_USERNAME",
        password="YOUR_PASSWORD",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        username: typing.Union[str, typing.Callable[[], str]],
        password: typing.Union[str, typing.Callable[[], str]],
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None,
    ):
        _defaulted_timeout = (
            timeout if timeout is not None else 60 if httpx_client is None else httpx_client.timeout.read
        )
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            username=username,
            password=password,
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.Client(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.Client(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self._raw_client = RawFernApi(client_wrapper=self._client_wrapper)

    @property
    def with_raw_response(self) -> RawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFernApi
        """
        return self._raw_client

    def delete_archived_call(
        self, date: dt.date, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
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
        None

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.delete_archived_call(
            date=datetime.date.fromisoformat(
                "2023-01-15",
            ),
            sid="Sid",
        )
        """
        _response = self._raw_client.delete_archived_call(date, sid, request_options=request_options)
        return _response.data

    def list_byoc_trunk(
        self,
        *,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListByocTrunkResponse:
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
        ListByocTrunkResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.list_byoc_trunk()
        """
        _response = self._raw_client.list_byoc_trunk(
            page_size=page_size, page=page, page_token=page_token, request_options=request_options
        )
        return _response.data

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
    ) -> VoiceV1ByocTrunk:
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
        VoiceV1ByocTrunk
            Created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.create_byoc_trunk()
        """
        _response = self._raw_client.create_byoc_trunk(
            cnam_lookup_enabled=cnam_lookup_enabled,
            connection_policy_sid=connection_policy_sid,
            friendly_name=friendly_name,
            from_domain_sid=from_domain_sid,
            status_callback_method=status_callback_method,
            status_callback_url=status_callback_url,
            voice_fallback_method=voice_fallback_method,
            voice_fallback_url=voice_fallback_url,
            voice_method=voice_method,
            voice_url=voice_url,
            request_options=request_options,
        )
        return _response.data

    def fetch_byoc_trunk(
        self, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> VoiceV1ByocTrunk:
        """


        Parameters
        ----------
        sid : str
            The Twilio-provided string that uniquely identifies the BYOC Trunk resource to fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VoiceV1ByocTrunk
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.fetch_byoc_trunk(
            sid="Sid",
        )
        """
        _response = self._raw_client.fetch_byoc_trunk(sid, request_options=request_options)
        return _response.data

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
    ) -> VoiceV1ByocTrunk:
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
        VoiceV1ByocTrunk
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.update_byoc_trunk(
            sid="Sid",
        )
        """
        _response = self._raw_client.update_byoc_trunk(
            sid,
            cnam_lookup_enabled=cnam_lookup_enabled,
            connection_policy_sid=connection_policy_sid,
            friendly_name=friendly_name,
            from_domain_sid=from_domain_sid,
            status_callback_method=status_callback_method,
            status_callback_url=status_callback_url,
            voice_fallback_method=voice_fallback_method,
            voice_fallback_url=voice_fallback_url,
            voice_method=voice_method,
            voice_url=voice_url,
            request_options=request_options,
        )
        return _response.data

    def delete_byoc_trunk(self, sid: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        sid : str
            The Twilio-provided string that uniquely identifies the BYOC Trunk resource to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.delete_byoc_trunk(
            sid="Sid",
        )
        """
        _response = self._raw_client.delete_byoc_trunk(sid, request_options=request_options)
        return _response.data

    def list_connection_policy(
        self,
        *,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListConnectionPolicyResponse:
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
        ListConnectionPolicyResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.list_connection_policy()
        """
        _response = self._raw_client.list_connection_policy(
            page_size=page_size, page=page, page_token=page_token, request_options=request_options
        )
        return _response.data

    def create_connection_policy(
        self, *, friendly_name: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> VoiceV1ConnectionPolicy:
        """


        Parameters
        ----------
        friendly_name : typing.Optional[str]
            A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VoiceV1ConnectionPolicy
            Created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.create_connection_policy()
        """
        _response = self._raw_client.create_connection_policy(
            friendly_name=friendly_name, request_options=request_options
        )
        return _response.data

    def list_connection_policy_target(
        self,
        connection_policy_sid: str,
        *,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListConnectionPolicyTargetResponse:
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
        ListConnectionPolicyTargetResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.list_connection_policy_target(
            connection_policy_sid="ConnectionPolicySid",
        )
        """
        _response = self._raw_client.list_connection_policy_target(
            connection_policy_sid,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        )
        return _response.data

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
    ) -> VoiceV1ConnectionPolicyConnectionPolicyTarget:
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
        VoiceV1ConnectionPolicyConnectionPolicyTarget
            Created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.create_connection_policy_target(
            connection_policy_sid="ConnectionPolicySid",
            target="Target",
        )
        """
        _response = self._raw_client.create_connection_policy_target(
            connection_policy_sid,
            target=target,
            enabled=enabled,
            friendly_name=friendly_name,
            priority=priority,
            weight=weight,
            request_options=request_options,
        )
        return _response.data

    def fetch_connection_policy_target(
        self, connection_policy_sid: str, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> VoiceV1ConnectionPolicyConnectionPolicyTarget:
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
        VoiceV1ConnectionPolicyConnectionPolicyTarget
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.fetch_connection_policy_target(
            connection_policy_sid="ConnectionPolicySid",
            sid="Sid",
        )
        """
        _response = self._raw_client.fetch_connection_policy_target(
            connection_policy_sid, sid, request_options=request_options
        )
        return _response.data

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
    ) -> VoiceV1ConnectionPolicyConnectionPolicyTarget:
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
        VoiceV1ConnectionPolicyConnectionPolicyTarget
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.update_connection_policy_target(
            connection_policy_sid="ConnectionPolicySid",
            sid="Sid",
        )
        """
        _response = self._raw_client.update_connection_policy_target(
            connection_policy_sid,
            sid,
            enabled=enabled,
            friendly_name=friendly_name,
            priority=priority,
            target=target,
            weight=weight,
            request_options=request_options,
        )
        return _response.data

    def delete_connection_policy_target(
        self, connection_policy_sid: str, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
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
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.delete_connection_policy_target(
            connection_policy_sid="ConnectionPolicySid",
            sid="Sid",
        )
        """
        _response = self._raw_client.delete_connection_policy_target(
            connection_policy_sid, sid, request_options=request_options
        )
        return _response.data

    def fetch_connection_policy(
        self, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> VoiceV1ConnectionPolicy:
        """


        Parameters
        ----------
        sid : str
            The unique string that we created to identify the Connection Policy resource to fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VoiceV1ConnectionPolicy
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.fetch_connection_policy(
            sid="Sid",
        )
        """
        _response = self._raw_client.fetch_connection_policy(sid, request_options=request_options)
        return _response.data

    def update_connection_policy(
        self,
        sid: str,
        *,
        friendly_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VoiceV1ConnectionPolicy:
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
        VoiceV1ConnectionPolicy
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.update_connection_policy(
            sid="Sid",
        )
        """
        _response = self._raw_client.update_connection_policy(
            sid, friendly_name=friendly_name, request_options=request_options
        )
        return _response.data

    def delete_connection_policy(self, sid: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        sid : str
            The unique string that we created to identify the Connection Policy resource to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.delete_connection_policy(
            sid="Sid",
        )
        """
        _response = self._raw_client.delete_connection_policy(sid, request_options=request_options)
        return _response.data

    def create_dialing_permissions_country_bulk_update(
        self, *, update_request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> VoiceV1DialingPermissionsDialingPermissionsCountryBulkUpdate:
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
        VoiceV1DialingPermissionsDialingPermissionsCountryBulkUpdate
            Created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.create_dialing_permissions_country_bulk_update(
            update_request="UpdateRequest",
        )
        """
        _response = self._raw_client.create_dialing_permissions_country_bulk_update(
            update_request=update_request, request_options=request_options
        )
        return _response.data

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
    ) -> ListDialingPermissionsCountryResponse:
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
        ListDialingPermissionsCountryResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.list_dialing_permissions_country()
        """
        _response = self._raw_client.list_dialing_permissions_country(
            iso_code=iso_code,
            continent=continent,
            country_code=country_code,
            low_risk_numbers_enabled=low_risk_numbers_enabled,
            high_risk_special_numbers_enabled=high_risk_special_numbers_enabled,
            high_risk_tollfraud_numbers_enabled=high_risk_tollfraud_numbers_enabled,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        )
        return _response.data

    def fetch_dialing_permissions_country(
        self, iso_code: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> VoiceV1DialingPermissionsDialingPermissionsCountryInstance:
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
        VoiceV1DialingPermissionsDialingPermissionsCountryInstance
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.fetch_dialing_permissions_country(
            iso_code="IsoCode",
        )
        """
        _response = self._raw_client.fetch_dialing_permissions_country(iso_code, request_options=request_options)
        return _response.data

    def list_dialing_permissions_hrs_prefixes(
        self,
        iso_code: str,
        *,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListDialingPermissionsHrsPrefixesResponse:
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
        ListDialingPermissionsHrsPrefixesResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.list_dialing_permissions_hrs_prefixes(
            iso_code="IsoCode",
        )
        """
        _response = self._raw_client.list_dialing_permissions_hrs_prefixes(
            iso_code, page_size=page_size, page=page, page_token=page_token, request_options=request_options
        )
        return _response.data

    def list_ip_record(
        self,
        *,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListIpRecordResponse:
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
        ListIpRecordResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.list_ip_record()
        """
        _response = self._raw_client.list_ip_record(
            page_size=page_size, page=page, page_token=page_token, request_options=request_options
        )
        return _response.data

    def create_ip_record(
        self,
        *,
        ip_address: str,
        cidr_prefix_length: typing.Optional[int] = OMIT,
        friendly_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VoiceV1IpRecord:
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
        VoiceV1IpRecord
            Created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.create_ip_record(
            ip_address="IpAddress",
        )
        """
        _response = self._raw_client.create_ip_record(
            ip_address=ip_address,
            cidr_prefix_length=cidr_prefix_length,
            friendly_name=friendly_name,
            request_options=request_options,
        )
        return _response.data

    def fetch_ip_record(self, sid: str, *, request_options: typing.Optional[RequestOptions] = None) -> VoiceV1IpRecord:
        """


        Parameters
        ----------
        sid : str
            The Twilio-provided string that uniquely identifies the IP Record resource to fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VoiceV1IpRecord
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.fetch_ip_record(
            sid="Sid",
        )
        """
        _response = self._raw_client.fetch_ip_record(sid, request_options=request_options)
        return _response.data

    def update_ip_record(
        self,
        sid: str,
        *,
        friendly_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VoiceV1IpRecord:
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
        VoiceV1IpRecord
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.update_ip_record(
            sid="Sid",
        )
        """
        _response = self._raw_client.update_ip_record(sid, friendly_name=friendly_name, request_options=request_options)
        return _response.data

    def delete_ip_record(self, sid: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        sid : str
            The Twilio-provided string that uniquely identifies the IP Record resource to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.delete_ip_record(
            sid="Sid",
        )
        """
        _response = self._raw_client.delete_ip_record(sid, request_options=request_options)
        return _response.data

    def fetch_dialing_permissions_settings(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> VoiceV1DialingPermissionsDialingPermissionsSettings:
        """
        Retrieve voice dialing permissions inheritance for the sub-account

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VoiceV1DialingPermissionsDialingPermissionsSettings
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.fetch_dialing_permissions_settings()
        """
        _response = self._raw_client.fetch_dialing_permissions_settings(request_options=request_options)
        return _response.data

    def update_dialing_permissions_settings(
        self,
        *,
        dialing_permissions_inheritance: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VoiceV1DialingPermissionsDialingPermissionsSettings:
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
        VoiceV1DialingPermissionsDialingPermissionsSettings
            Accepted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.update_dialing_permissions_settings()
        """
        _response = self._raw_client.update_dialing_permissions_settings(
            dialing_permissions_inheritance=dialing_permissions_inheritance, request_options=request_options
        )
        return _response.data

    def list_source_ip_mapping(
        self,
        *,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListSourceIpMappingResponse:
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
        ListSourceIpMappingResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.list_source_ip_mapping()
        """
        _response = self._raw_client.list_source_ip_mapping(
            page_size=page_size, page=page, page_token=page_token, request_options=request_options
        )
        return _response.data

    def create_source_ip_mapping(
        self, *, ip_record_sid: str, sip_domain_sid: str, request_options: typing.Optional[RequestOptions] = None
    ) -> VoiceV1SourceIpMapping:
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
        VoiceV1SourceIpMapping
            Created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.create_source_ip_mapping(
            ip_record_sid="IpRecordSid",
            sip_domain_sid="SipDomainSid",
        )
        """
        _response = self._raw_client.create_source_ip_mapping(
            ip_record_sid=ip_record_sid, sip_domain_sid=sip_domain_sid, request_options=request_options
        )
        return _response.data

    def fetch_source_ip_mapping(
        self, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> VoiceV1SourceIpMapping:
        """


        Parameters
        ----------
        sid : str
            The Twilio-provided string that uniquely identifies the IP Record resource to fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VoiceV1SourceIpMapping
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.fetch_source_ip_mapping(
            sid="Sid",
        )
        """
        _response = self._raw_client.fetch_source_ip_mapping(sid, request_options=request_options)
        return _response.data

    def update_source_ip_mapping(
        self, sid: str, *, sip_domain_sid: str, request_options: typing.Optional[RequestOptions] = None
    ) -> VoiceV1SourceIpMapping:
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
        VoiceV1SourceIpMapping
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.update_source_ip_mapping(
            sid="Sid",
            sip_domain_sid="SipDomainSid",
        )
        """
        _response = self._raw_client.update_source_ip_mapping(
            sid, sip_domain_sid=sip_domain_sid, request_options=request_options
        )
        return _response.data

    def delete_source_ip_mapping(self, sid: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        sid : str
            The Twilio-provided string that uniquely identifies the IP Record resource to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.delete_source_ip_mapping(
            sid="Sid",
        )
        """
        _response = self._raw_client.delete_source_ip_mapping(sid, request_options=request_options)
        return _response.data


class AsyncFernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : FernApiEnvironment
        The environment to use for requests from the client. from .environment import FernApiEnvironment



        Defaults to FernApiEnvironment.DEFAULT



    username : typing.Union[str, typing.Callable[[], str]]
    password : typing.Union[str, typing.Callable[[], str]]
    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.AsyncClient]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    Examples
    --------
    from fern import AsyncFernApi

    client = AsyncFernApi(
        username="YOUR_USERNAME",
        password="YOUR_PASSWORD",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        username: typing.Union[str, typing.Callable[[], str]],
        password: typing.Union[str, typing.Callable[[], str]],
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
    ):
        _defaulted_timeout = (
            timeout if timeout is not None else 60 if httpx_client is None else httpx_client.timeout.read
        )
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            username=username,
            password=password,
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self._raw_client = AsyncRawFernApi(client_wrapper=self._client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFernApi
        """
        return self._raw_client

    async def delete_archived_call(
        self, date: dt.date, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
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
        None

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.delete_archived_call(
                date=datetime.date.fromisoformat(
                    "2023-01-15",
                ),
                sid="Sid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_archived_call(date, sid, request_options=request_options)
        return _response.data

    async def list_byoc_trunk(
        self,
        *,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListByocTrunkResponse:
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
        ListByocTrunkResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.list_byoc_trunk()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_byoc_trunk(
            page_size=page_size, page=page, page_token=page_token, request_options=request_options
        )
        return _response.data

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
    ) -> VoiceV1ByocTrunk:
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
        VoiceV1ByocTrunk
            Created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.create_byoc_trunk()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_byoc_trunk(
            cnam_lookup_enabled=cnam_lookup_enabled,
            connection_policy_sid=connection_policy_sid,
            friendly_name=friendly_name,
            from_domain_sid=from_domain_sid,
            status_callback_method=status_callback_method,
            status_callback_url=status_callback_url,
            voice_fallback_method=voice_fallback_method,
            voice_fallback_url=voice_fallback_url,
            voice_method=voice_method,
            voice_url=voice_url,
            request_options=request_options,
        )
        return _response.data

    async def fetch_byoc_trunk(
        self, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> VoiceV1ByocTrunk:
        """


        Parameters
        ----------
        sid : str
            The Twilio-provided string that uniquely identifies the BYOC Trunk resource to fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VoiceV1ByocTrunk
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.fetch_byoc_trunk(
                sid="Sid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_byoc_trunk(sid, request_options=request_options)
        return _response.data

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
    ) -> VoiceV1ByocTrunk:
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
        VoiceV1ByocTrunk
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.update_byoc_trunk(
                sid="Sid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_byoc_trunk(
            sid,
            cnam_lookup_enabled=cnam_lookup_enabled,
            connection_policy_sid=connection_policy_sid,
            friendly_name=friendly_name,
            from_domain_sid=from_domain_sid,
            status_callback_method=status_callback_method,
            status_callback_url=status_callback_url,
            voice_fallback_method=voice_fallback_method,
            voice_fallback_url=voice_fallback_url,
            voice_method=voice_method,
            voice_url=voice_url,
            request_options=request_options,
        )
        return _response.data

    async def delete_byoc_trunk(self, sid: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        sid : str
            The Twilio-provided string that uniquely identifies the BYOC Trunk resource to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.delete_byoc_trunk(
                sid="Sid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_byoc_trunk(sid, request_options=request_options)
        return _response.data

    async def list_connection_policy(
        self,
        *,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListConnectionPolicyResponse:
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
        ListConnectionPolicyResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.list_connection_policy()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_connection_policy(
            page_size=page_size, page=page, page_token=page_token, request_options=request_options
        )
        return _response.data

    async def create_connection_policy(
        self, *, friendly_name: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> VoiceV1ConnectionPolicy:
        """


        Parameters
        ----------
        friendly_name : typing.Optional[str]
            A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VoiceV1ConnectionPolicy
            Created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.create_connection_policy()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_connection_policy(
            friendly_name=friendly_name, request_options=request_options
        )
        return _response.data

    async def list_connection_policy_target(
        self,
        connection_policy_sid: str,
        *,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListConnectionPolicyTargetResponse:
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
        ListConnectionPolicyTargetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.list_connection_policy_target(
                connection_policy_sid="ConnectionPolicySid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_connection_policy_target(
            connection_policy_sid,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        )
        return _response.data

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
    ) -> VoiceV1ConnectionPolicyConnectionPolicyTarget:
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
        VoiceV1ConnectionPolicyConnectionPolicyTarget
            Created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.create_connection_policy_target(
                connection_policy_sid="ConnectionPolicySid",
                target="Target",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_connection_policy_target(
            connection_policy_sid,
            target=target,
            enabled=enabled,
            friendly_name=friendly_name,
            priority=priority,
            weight=weight,
            request_options=request_options,
        )
        return _response.data

    async def fetch_connection_policy_target(
        self, connection_policy_sid: str, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> VoiceV1ConnectionPolicyConnectionPolicyTarget:
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
        VoiceV1ConnectionPolicyConnectionPolicyTarget
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.fetch_connection_policy_target(
                connection_policy_sid="ConnectionPolicySid",
                sid="Sid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_connection_policy_target(
            connection_policy_sid, sid, request_options=request_options
        )
        return _response.data

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
    ) -> VoiceV1ConnectionPolicyConnectionPolicyTarget:
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
        VoiceV1ConnectionPolicyConnectionPolicyTarget
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.update_connection_policy_target(
                connection_policy_sid="ConnectionPolicySid",
                sid="Sid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_connection_policy_target(
            connection_policy_sid,
            sid,
            enabled=enabled,
            friendly_name=friendly_name,
            priority=priority,
            target=target,
            weight=weight,
            request_options=request_options,
        )
        return _response.data

    async def delete_connection_policy_target(
        self, connection_policy_sid: str, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
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
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.delete_connection_policy_target(
                connection_policy_sid="ConnectionPolicySid",
                sid="Sid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_connection_policy_target(
            connection_policy_sid, sid, request_options=request_options
        )
        return _response.data

    async def fetch_connection_policy(
        self, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> VoiceV1ConnectionPolicy:
        """


        Parameters
        ----------
        sid : str
            The unique string that we created to identify the Connection Policy resource to fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VoiceV1ConnectionPolicy
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.fetch_connection_policy(
                sid="Sid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_connection_policy(sid, request_options=request_options)
        return _response.data

    async def update_connection_policy(
        self,
        sid: str,
        *,
        friendly_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VoiceV1ConnectionPolicy:
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
        VoiceV1ConnectionPolicy
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.update_connection_policy(
                sid="Sid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_connection_policy(
            sid, friendly_name=friendly_name, request_options=request_options
        )
        return _response.data

    async def delete_connection_policy(
        self, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """


        Parameters
        ----------
        sid : str
            The unique string that we created to identify the Connection Policy resource to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.delete_connection_policy(
                sid="Sid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_connection_policy(sid, request_options=request_options)
        return _response.data

    async def create_dialing_permissions_country_bulk_update(
        self, *, update_request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> VoiceV1DialingPermissionsDialingPermissionsCountryBulkUpdate:
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
        VoiceV1DialingPermissionsDialingPermissionsCountryBulkUpdate
            Created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.create_dialing_permissions_country_bulk_update(
                update_request="UpdateRequest",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_dialing_permissions_country_bulk_update(
            update_request=update_request, request_options=request_options
        )
        return _response.data

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
    ) -> ListDialingPermissionsCountryResponse:
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
        ListDialingPermissionsCountryResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.list_dialing_permissions_country()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_dialing_permissions_country(
            iso_code=iso_code,
            continent=continent,
            country_code=country_code,
            low_risk_numbers_enabled=low_risk_numbers_enabled,
            high_risk_special_numbers_enabled=high_risk_special_numbers_enabled,
            high_risk_tollfraud_numbers_enabled=high_risk_tollfraud_numbers_enabled,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        )
        return _response.data

    async def fetch_dialing_permissions_country(
        self, iso_code: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> VoiceV1DialingPermissionsDialingPermissionsCountryInstance:
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
        VoiceV1DialingPermissionsDialingPermissionsCountryInstance
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.fetch_dialing_permissions_country(
                iso_code="IsoCode",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_dialing_permissions_country(iso_code, request_options=request_options)
        return _response.data

    async def list_dialing_permissions_hrs_prefixes(
        self,
        iso_code: str,
        *,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListDialingPermissionsHrsPrefixesResponse:
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
        ListDialingPermissionsHrsPrefixesResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.list_dialing_permissions_hrs_prefixes(
                iso_code="IsoCode",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_dialing_permissions_hrs_prefixes(
            iso_code, page_size=page_size, page=page, page_token=page_token, request_options=request_options
        )
        return _response.data

    async def list_ip_record(
        self,
        *,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListIpRecordResponse:
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
        ListIpRecordResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.list_ip_record()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_ip_record(
            page_size=page_size, page=page, page_token=page_token, request_options=request_options
        )
        return _response.data

    async def create_ip_record(
        self,
        *,
        ip_address: str,
        cidr_prefix_length: typing.Optional[int] = OMIT,
        friendly_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VoiceV1IpRecord:
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
        VoiceV1IpRecord
            Created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.create_ip_record(
                ip_address="IpAddress",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_ip_record(
            ip_address=ip_address,
            cidr_prefix_length=cidr_prefix_length,
            friendly_name=friendly_name,
            request_options=request_options,
        )
        return _response.data

    async def fetch_ip_record(
        self, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> VoiceV1IpRecord:
        """


        Parameters
        ----------
        sid : str
            The Twilio-provided string that uniquely identifies the IP Record resource to fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VoiceV1IpRecord
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.fetch_ip_record(
                sid="Sid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_ip_record(sid, request_options=request_options)
        return _response.data

    async def update_ip_record(
        self,
        sid: str,
        *,
        friendly_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VoiceV1IpRecord:
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
        VoiceV1IpRecord
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.update_ip_record(
                sid="Sid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_ip_record(
            sid, friendly_name=friendly_name, request_options=request_options
        )
        return _response.data

    async def delete_ip_record(self, sid: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        sid : str
            The Twilio-provided string that uniquely identifies the IP Record resource to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.delete_ip_record(
                sid="Sid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_ip_record(sid, request_options=request_options)
        return _response.data

    async def fetch_dialing_permissions_settings(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> VoiceV1DialingPermissionsDialingPermissionsSettings:
        """
        Retrieve voice dialing permissions inheritance for the sub-account

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VoiceV1DialingPermissionsDialingPermissionsSettings
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.fetch_dialing_permissions_settings()


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_dialing_permissions_settings(request_options=request_options)
        return _response.data

    async def update_dialing_permissions_settings(
        self,
        *,
        dialing_permissions_inheritance: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VoiceV1DialingPermissionsDialingPermissionsSettings:
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
        VoiceV1DialingPermissionsDialingPermissionsSettings
            Accepted

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.update_dialing_permissions_settings()


        asyncio.run(main())
        """
        _response = await self._raw_client.update_dialing_permissions_settings(
            dialing_permissions_inheritance=dialing_permissions_inheritance, request_options=request_options
        )
        return _response.data

    async def list_source_ip_mapping(
        self,
        *,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListSourceIpMappingResponse:
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
        ListSourceIpMappingResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.list_source_ip_mapping()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_source_ip_mapping(
            page_size=page_size, page=page, page_token=page_token, request_options=request_options
        )
        return _response.data

    async def create_source_ip_mapping(
        self, *, ip_record_sid: str, sip_domain_sid: str, request_options: typing.Optional[RequestOptions] = None
    ) -> VoiceV1SourceIpMapping:
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
        VoiceV1SourceIpMapping
            Created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.create_source_ip_mapping(
                ip_record_sid="IpRecordSid",
                sip_domain_sid="SipDomainSid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_source_ip_mapping(
            ip_record_sid=ip_record_sid, sip_domain_sid=sip_domain_sid, request_options=request_options
        )
        return _response.data

    async def fetch_source_ip_mapping(
        self, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> VoiceV1SourceIpMapping:
        """


        Parameters
        ----------
        sid : str
            The Twilio-provided string that uniquely identifies the IP Record resource to fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VoiceV1SourceIpMapping
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.fetch_source_ip_mapping(
                sid="Sid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_source_ip_mapping(sid, request_options=request_options)
        return _response.data

    async def update_source_ip_mapping(
        self, sid: str, *, sip_domain_sid: str, request_options: typing.Optional[RequestOptions] = None
    ) -> VoiceV1SourceIpMapping:
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
        VoiceV1SourceIpMapping
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.update_source_ip_mapping(
                sid="Sid",
                sip_domain_sid="SipDomainSid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_source_ip_mapping(
            sid, sip_domain_sid=sip_domain_sid, request_options=request_options
        )
        return _response.data

    async def delete_source_ip_mapping(
        self, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """


        Parameters
        ----------
        sid : str
            The Twilio-provided string that uniquely identifies the IP Record resource to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.delete_source_ip_mapping(
                sid="Sid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_source_ip_mapping(sid, request_options=request_options)
        return _response.data


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")

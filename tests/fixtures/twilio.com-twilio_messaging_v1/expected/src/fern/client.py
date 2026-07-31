

import datetime as dt
import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .core.request_options import RequestOptions
from .environment import FernApiEnvironment
from .raw_client import AsyncRawFernApi, RawFernApi
from .types.brand_vetting_enum_vetting_provider import BrandVettingEnumVettingProvider
from .types.create_service_request_fallback_method import CreateServiceRequestFallbackMethod
from .types.create_service_request_inbound_method import CreateServiceRequestInboundMethod
from .types.list_alpha_sender_response import ListAlphaSenderResponse
from .types.list_brand_registrations_response import ListBrandRegistrationsResponse
from .types.list_brand_vetting_response import ListBrandVettingResponse
from .types.list_phone_number_response import ListPhoneNumberResponse
from .types.list_service_response import ListServiceResponse
from .types.list_short_code_response import ListShortCodeResponse
from .types.list_tollfree_verification_response import ListTollfreeVerificationResponse
from .types.list_us_app_to_person_response import ListUsAppToPersonResponse
from .types.messaging_v1brand_registrations import MessagingV1BrandRegistrations
from .types.messaging_v1brand_registrations_brand_registration_otp import (
    MessagingV1BrandRegistrationsBrandRegistrationOtp,
)
from .types.messaging_v1brand_registrations_brand_vetting import MessagingV1BrandRegistrationsBrandVetting
from .types.messaging_v1domain_cert_v4 import MessagingV1DomainCertV4
from .types.messaging_v1domain_config import MessagingV1DomainConfig
from .types.messaging_v1domain_config_messaging_service import MessagingV1DomainConfigMessagingService
from .types.messaging_v1external_campaign import MessagingV1ExternalCampaign
from .types.messaging_v1linkshortening_messaging_service import MessagingV1LinkshorteningMessagingService
from .types.messaging_v1service import MessagingV1Service
from .types.messaging_v1service_alpha_sender import MessagingV1ServiceAlphaSender
from .types.messaging_v1service_phone_number import MessagingV1ServicePhoneNumber
from .types.messaging_v1service_short_code import MessagingV1ServiceShortCode
from .types.messaging_v1service_us_app_to_person import MessagingV1ServiceUsAppToPerson
from .types.messaging_v1service_us_app_to_person_usecase import MessagingV1ServiceUsAppToPersonUsecase
from .types.messaging_v1tollfree_verification import MessagingV1TollfreeVerification
from .types.messaging_v1usecase import MessagingV1Usecase
from .types.service_enum_scan_message_content import ServiceEnumScanMessageContent
from .types.tollfree_verification_enum_opt_in_type import TollfreeVerificationEnumOptInType
from .types.tollfree_verification_enum_status import TollfreeVerificationEnumStatus
from .types.update_service_request_fallback_method import UpdateServiceRequestFallbackMethod
from .types.update_service_request_inbound_method import UpdateServiceRequestInboundMethod


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

    max_retries : typing.Optional[int]
        The default maximum number of retries for failed requests. Defaults to 2. Per-request `max_retries` in `request_options` takes precedence over this value.

    stream_reconnection_enabled : typing.Optional[bool]
        Whether to automatically reconnect on stream disconnection for resumable streaming endpoints. Defaults to True. Per-request `stream_reconnection_enabled` in `request_options` takes precedence over this value.

    max_stream_reconnection_attempts : typing.Optional[int]
        The maximum number of reconnection attempts for resumable streaming endpoints. Defaults to no limit. Per-request `max_stream_reconnection_attempts` in `request_options` takes precedence over this value.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.Client]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    logging : typing.Optional[typing.Union[LogConfig, Logger]]
        Configure logging for the SDK. Accepts a LogConfig dict with 'level' (debug/info/warn/error), 'logger' (custom logger implementation), and 'silent' (boolean, defaults to True) fields. You can also pass a pre-configured Logger instance.

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
        max_retries: typing.Optional[int] = None,
        stream_reconnection_enabled: typing.Optional[bool] = None,
        max_stream_reconnection_attempts: typing.Optional[int] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None,
        logging: typing.Optional[typing.Union[LogConfig, Logger]] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        _defaulted_max_retries = max_retries if max_retries is not None else 2
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
            max_retries=_defaulted_max_retries,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
            logging=logging,
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

    def fetch_deactivation(
        self, *, date: typing.Optional[dt.date] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Fetch a list of all United States numbers that have been deactivated on a specific date.

        Parameters
        ----------
        date : typing.Optional[dt.date]
            The request will return a list of all United States Phone Numbers that were deactivated on the day specified by this parameter. This date should be specified in YYYY-MM-DD format.

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
        client.fetch_deactivation()
        """
        _response = self._raw_client.fetch_deactivation(date=date, request_options=request_options)
        return _response.data

    def fetch_domain_cert_v4(
        self, domain_sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MessagingV1DomainCertV4:
        """


        Parameters
        ----------
        domain_sid : str
            Unique string used to identify the domain that this certificate should be associated with.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagingV1DomainCertV4
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.fetch_domain_cert_v4(
            domain_sid="DomainSid",
        )
        """
        _response = self._raw_client.fetch_domain_cert_v4(domain_sid, request_options=request_options)
        return _response.data

    def update_domain_cert_v4(
        self, domain_sid: str, *, tls_cert: str, request_options: typing.Optional[RequestOptions] = None
    ) -> MessagingV1DomainCertV4:
        """


        Parameters
        ----------
        domain_sid : str
            Unique string used to identify the domain that this certificate should be associated with.

        tls_cert : str
            Contains the full TLS certificate and private for this domain in PEM format: https://en.wikipedia.org/wiki/Privacy-Enhanced_Mail. Twilio uses this information to process HTTPS traffic sent to your domain.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagingV1DomainCertV4
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.update_domain_cert_v4(
            domain_sid="DomainSid",
            tls_cert="TlsCert",
        )
        """
        _response = self._raw_client.update_domain_cert_v4(
            domain_sid, tls_cert=tls_cert, request_options=request_options
        )
        return _response.data

    def delete_domain_cert_v4(
        self, domain_sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """


        Parameters
        ----------
        domain_sid : str
            Unique string used to identify the domain that this certificate should be associated with.

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
        client.delete_domain_cert_v4(
            domain_sid="DomainSid",
        )
        """
        _response = self._raw_client.delete_domain_cert_v4(domain_sid, request_options=request_options)
        return _response.data

    def fetch_domain_config(
        self, domain_sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MessagingV1DomainConfig:
        """


        Parameters
        ----------
        domain_sid : str
            Unique string used to identify the domain that this config should be associated with.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagingV1DomainConfig
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.fetch_domain_config(
            domain_sid="DomainSid",
        )
        """
        _response = self._raw_client.fetch_domain_config(domain_sid, request_options=request_options)
        return _response.data

    def update_domain_config(
        self,
        domain_sid: str,
        *,
        callback_url: typing.Optional[str] = OMIT,
        fallback_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MessagingV1DomainConfig:
        """


        Parameters
        ----------
        domain_sid : str
            Unique string used to identify the domain that this config should be associated with.

        callback_url : typing.Optional[str]
            URL to receive click events to your webhook whenever the recipients click on the shortened links

        fallback_url : typing.Optional[str]
            Any requests we receive to this domain that do not match an existing shortened message will be redirected to the fallback url. These will likely be either expired messages, random misdirected traffic, or intentional scraping.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagingV1DomainConfig
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.update_domain_config(
            domain_sid="DomainSid",
        )
        """
        _response = self._raw_client.update_domain_config(
            domain_sid, callback_url=callback_url, fallback_url=fallback_url, request_options=request_options
        )
        return _response.data

    def create_linkshortening_messaging_service(
        self, domain_sid: str, messaging_service_sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MessagingV1LinkshorteningMessagingService:
        """


        Parameters
        ----------
        domain_sid : str
            The domain SID to associate with a messaging service. With URL shortening enabled, links in messages sent with the associated messaging service will be shortened to the provided domain

        messaging_service_sid : str
            A messaging service SID to associate with a domain. With URL shortening enabled, links in messages sent with the provided messaging service will be shortened to the associated domain

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagingV1LinkshorteningMessagingService
            Created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.create_linkshortening_messaging_service(
            domain_sid="DomainSid",
            messaging_service_sid="MessagingServiceSid",
        )
        """
        _response = self._raw_client.create_linkshortening_messaging_service(
            domain_sid, messaging_service_sid, request_options=request_options
        )
        return _response.data

    def delete_linkshortening_messaging_service(
        self, domain_sid: str, messaging_service_sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """


        Parameters
        ----------
        domain_sid : str
            The domain SID to dissociate from a messaging service. With URL shortening enabled, links in messages sent with the associated messaging service will be shortened to the provided domain

        messaging_service_sid : str
            A messaging service SID to dissociate from a domain. With URL shortening enabled, links in messages sent with the provided messaging service will be shortened to the associated domain

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
        client.delete_linkshortening_messaging_service(
            domain_sid="DomainSid",
            messaging_service_sid="MessagingServiceSid",
        )
        """
        _response = self._raw_client.delete_linkshortening_messaging_service(
            domain_sid, messaging_service_sid, request_options=request_options
        )
        return _response.data

    def fetch_domain_config_messaging_service(
        self, messaging_service_sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MessagingV1DomainConfigMessagingService:
        """


        Parameters
        ----------
        messaging_service_sid : str
            Unique string used to identify the Messaging service that this domain should be associated with.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagingV1DomainConfigMessagingService
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.fetch_domain_config_messaging_service(
            messaging_service_sid="MessagingServiceSid",
        )
        """
        _response = self._raw_client.fetch_domain_config_messaging_service(
            messaging_service_sid, request_options=request_options
        )
        return _response.data

    def list_service(
        self,
        *,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListServiceResponse:
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
        ListServiceResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.list_service()
        """
        _response = self._raw_client.list_service(
            page_size=page_size, page=page, page_token=page_token, request_options=request_options
        )
        return _response.data

    def create_service(
        self,
        *,
        friendly_name: str,
        area_code_geomatch: typing.Optional[bool] = OMIT,
        fallback_method: typing.Optional[CreateServiceRequestFallbackMethod] = OMIT,
        fallback_to_long_code: typing.Optional[bool] = OMIT,
        fallback_url: typing.Optional[str] = OMIT,
        inbound_method: typing.Optional[CreateServiceRequestInboundMethod] = OMIT,
        inbound_request_url: typing.Optional[str] = OMIT,
        mms_converter: typing.Optional[bool] = OMIT,
        scan_message_content: typing.Optional[ServiceEnumScanMessageContent] = OMIT,
        smart_encoding: typing.Optional[bool] = OMIT,
        status_callback: typing.Optional[str] = OMIT,
        sticky_sender: typing.Optional[bool] = OMIT,
        synchronous_validation: typing.Optional[bool] = OMIT,
        use_inbound_webhook_on_number: typing.Optional[bool] = OMIT,
        usecase: typing.Optional[str] = OMIT,
        validity_period: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MessagingV1Service:
        """


        Parameters
        ----------
        friendly_name : str
            A descriptive string that you create to describe the resource. It can be up to 64 characters long.

        area_code_geomatch : typing.Optional[bool]
            Whether to enable [Area Code Geomatch](https://www.twilio.com/docs/sms/services#area-code-geomatch) on the Service Instance.

        fallback_method : typing.Optional[CreateServiceRequestFallbackMethod]
            The HTTP method we should use to call `fallback_url`. Can be: `GET` or `POST`.

        fallback_to_long_code : typing.Optional[bool]
            Whether to enable [Fallback to Long Code](https://www.twilio.com/docs/sms/services#fallback-to-long-code) for messages sent through the Service instance.

        fallback_url : typing.Optional[str]
            The URL that we call using `fallback_method` if an error occurs while retrieving or executing the TwiML from the Inbound Request URL. If the `use_inbound_webhook_on_number` field is enabled then the webhook url defined on the phone number will override the `fallback_url` defined for the Messaging Service.

        inbound_method : typing.Optional[CreateServiceRequestInboundMethod]
            The HTTP method we should use to call `inbound_request_url`. Can be `GET` or `POST` and the default is `POST`.

        inbound_request_url : typing.Optional[str]
            The URL we call using `inbound_method` when a message is received by any phone number or short code in the Service. When this property is `null`, receiving inbound messages is disabled. All messages sent to the Twilio phone number or short code will not be logged and received on the Account. If the `use_inbound_webhook_on_number` field is enabled then the webhook url defined on the phone number will override the `inbound_request_url` defined for the Messaging Service.

        mms_converter : typing.Optional[bool]
            Whether to enable the [MMS Converter](https://www.twilio.com/docs/sms/services#mms-converter) for messages sent through the Service instance.

        scan_message_content : typing.Optional[ServiceEnumScanMessageContent]
            Reserved.

        smart_encoding : typing.Optional[bool]
            Whether to enable [Smart Encoding](https://www.twilio.com/docs/sms/services#smart-encoding) for messages sent through the Service instance.

        status_callback : typing.Optional[str]
            The URL we should call to [pass status updates](https://www.twilio.com/docs/sms/api/message-resource#message-status-values) about message delivery.

        sticky_sender : typing.Optional[bool]
            Whether to enable [Sticky Sender](https://www.twilio.com/docs/sms/services#sticky-sender) on the Service instance.

        synchronous_validation : typing.Optional[bool]
            Reserved.

        use_inbound_webhook_on_number : typing.Optional[bool]
            A boolean value that indicates either the webhook url configured on the phone number will be used or `inbound_request_url`/`fallback_url` url will be called when a message is received from the phone number. If this field is enabled then the webhook url defined on the phone number will override the `inbound_request_url`/`fallback_url` defined for the Messaging Service.

        usecase : typing.Optional[str]
            A string that describes the scenario in which the Messaging Service will be used. Examples: [notification, marketing, verification, poll ..].

        validity_period : typing.Optional[int]
            How long, in seconds, messages sent from the Service are valid. Can be an integer from `1` to `14,400`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagingV1Service
            Created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.create_service(
            friendly_name="FriendlyName",
        )
        """
        _response = self._raw_client.create_service(
            friendly_name=friendly_name,
            area_code_geomatch=area_code_geomatch,
            fallback_method=fallback_method,
            fallback_to_long_code=fallback_to_long_code,
            fallback_url=fallback_url,
            inbound_method=inbound_method,
            inbound_request_url=inbound_request_url,
            mms_converter=mms_converter,
            scan_message_content=scan_message_content,
            smart_encoding=smart_encoding,
            status_callback=status_callback,
            sticky_sender=sticky_sender,
            synchronous_validation=synchronous_validation,
            use_inbound_webhook_on_number=use_inbound_webhook_on_number,
            usecase=usecase,
            validity_period=validity_period,
            request_options=request_options,
        )
        return _response.data

    def create_external_campaign(
        self, *, campaign_id: str, messaging_service_sid: str, request_options: typing.Optional[RequestOptions] = None
    ) -> MessagingV1ExternalCampaign:
        """


        Parameters
        ----------
        campaign_id : str
            ID of the preregistered campaign.

        messaging_service_sid : str
            The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/services/api) that the resource is associated with.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagingV1ExternalCampaign
            Created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.create_external_campaign(
            campaign_id="CampaignId",
            messaging_service_sid="MessagingServiceSid",
        )
        """
        _response = self._raw_client.create_external_campaign(
            campaign_id=campaign_id, messaging_service_sid=messaging_service_sid, request_options=request_options
        )
        return _response.data

    def fetch_usecase(self, *, request_options: typing.Optional[RequestOptions] = None) -> MessagingV1Usecase:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagingV1Usecase
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.fetch_usecase()
        """
        _response = self._raw_client.fetch_usecase(request_options=request_options)
        return _response.data

    def list_us_app_to_person(
        self,
        messaging_service_sid: str,
        *,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListUsAppToPersonResponse:
        """


        Parameters
        ----------
        messaging_service_sid : str
            The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/services/api) to fetch the resource from.

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
        ListUsAppToPersonResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.list_us_app_to_person(
            messaging_service_sid="MessagingServiceSid",
        )
        """
        _response = self._raw_client.list_us_app_to_person(
            messaging_service_sid,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        )
        return _response.data

    def create_us_app_to_person(
        self,
        messaging_service_sid: str,
        *,
        brand_registration_sid: str,
        description: str,
        has_embedded_links: bool,
        has_embedded_phone: bool,
        message_flow: str,
        message_samples: typing.Sequence[str],
        us_app_to_person_usecase: str,
        help_keywords: typing.Optional[typing.Sequence[str]] = OMIT,
        help_message: typing.Optional[str] = OMIT,
        opt_in_keywords: typing.Optional[typing.Sequence[str]] = OMIT,
        opt_in_message: typing.Optional[str] = OMIT,
        opt_out_keywords: typing.Optional[typing.Sequence[str]] = OMIT,
        opt_out_message: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MessagingV1ServiceUsAppToPerson:
        """


        Parameters
        ----------
        messaging_service_sid : str
            The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/services/api) to create the resources from.

        brand_registration_sid : str
            A2P Brand Registration SID

        description : str
            A short description of what this SMS campaign does. Min length: 40 characters. Max length: 4096 characters.

        has_embedded_links : bool
            Indicates that this SMS campaign will send messages that contain links.

        has_embedded_phone : bool
            Indicates that this SMS campaign will send messages that contain phone numbers.

        message_flow : str
            Required for all Campaigns. Details around how a consumer opts-in to their campaign, therefore giving consent to receive their messages. If multiple opt-in methods can be used for the same campaign, they must all be listed. 40 character minimum. 2048 character maximum.

        message_samples : typing.Sequence[str]
            Message samples, at least 1 and up to 5 sample messages (at least 2 for sole proprietor), >=20 chars, <=1024 chars each.

        us_app_to_person_usecase : str
            A2P Campaign Use Case. Examples: [ 2FA, EMERGENCY, MARKETING..]

        help_keywords : typing.Optional[typing.Sequence[str]]
            End users should be able to text in a keyword to receive help. Those keywords must be provided as part of the campaign registration request. This field is required if managing help keywords yourself (i.e. not using Twilio's Default or Advanced Opt Out features). Values must be alphanumeric. 255 character maximum.

        help_message : typing.Optional[str]
            When customers receive the help keywords from their end users, Twilio customers are expected to send back an auto-generated response; this may include the brand name and additional support contact information. This field is required if managing help keywords yourself (i.e. not using Twilio's Default or Advanced Opt Out features). 20 character minimum. 320 character maximum.

        opt_in_keywords : typing.Optional[typing.Sequence[str]]
            If end users can text in a keyword to start receiving messages from this campaign, those keywords must be provided. This field is required if end users can text in a keyword to start receiving messages from this campaign. Values must be alphanumeric. 255 character maximum.

        opt_in_message : typing.Optional[str]
            If end users can text in a keyword to start receiving messages from this campaign, the auto-reply messages sent to the end users must be provided. The opt-in response should include the Brand name, confirmation of opt-in enrollment to a recurring message campaign, how to get help, and clear description of how to opt-out. This field is required if end users can text in a keyword to start receiving messages from this campaign. 20 character minimum. 320 character maximum.

        opt_out_keywords : typing.Optional[typing.Sequence[str]]
            End users should be able to text in a keyword to stop receiving messages from this campaign. Those keywords must be provided. This field is required if managing opt out keywords yourself (i.e. not using Twilio's Default or Advanced Opt Out features). Values must be alphanumeric. 255 character maximum.

        opt_out_message : typing.Optional[str]
            Upon receiving the opt-out keywords from the end users, Twilio customers are expected to send back an auto-generated response, which must provide acknowledgment of the opt-out request and confirmation that no further messages will be sent. It is also recommended that these opt-out messages include the brand name. This field is required if managing opt out keywords yourself (i.e. not using Twilio's Default or Advanced Opt Out features). 20 character minimum. 320 character maximum.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagingV1ServiceUsAppToPerson
            Created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.create_us_app_to_person(
            messaging_service_sid="MessagingServiceSid",
            brand_registration_sid="BrandRegistrationSid",
            description="Description",
            has_embedded_links=True,
            has_embedded_phone=True,
            message_flow="MessageFlow",
            message_samples=["MessageSamples"],
            us_app_to_person_usecase="UsAppToPersonUsecase",
        )
        """
        _response = self._raw_client.create_us_app_to_person(
            messaging_service_sid,
            brand_registration_sid=brand_registration_sid,
            description=description,
            has_embedded_links=has_embedded_links,
            has_embedded_phone=has_embedded_phone,
            message_flow=message_flow,
            message_samples=message_samples,
            us_app_to_person_usecase=us_app_to_person_usecase,
            help_keywords=help_keywords,
            help_message=help_message,
            opt_in_keywords=opt_in_keywords,
            opt_in_message=opt_in_message,
            opt_out_keywords=opt_out_keywords,
            opt_out_message=opt_out_message,
            request_options=request_options,
        )
        return _response.data

    def fetch_us_app_to_person_usecase(
        self,
        messaging_service_sid: str,
        *,
        brand_registration_sid: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MessagingV1ServiceUsAppToPersonUsecase:
        """


        Parameters
        ----------
        messaging_service_sid : str
            The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/services/api) to fetch the resource from.

        brand_registration_sid : typing.Optional[str]
            The unique string to identify the A2P brand.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagingV1ServiceUsAppToPersonUsecase
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.fetch_us_app_to_person_usecase(
            messaging_service_sid="MessagingServiceSid",
        )
        """
        _response = self._raw_client.fetch_us_app_to_person_usecase(
            messaging_service_sid, brand_registration_sid=brand_registration_sid, request_options=request_options
        )
        return _response.data

    def fetch_us_app_to_person(
        self, messaging_service_sid: str, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MessagingV1ServiceUsAppToPerson:
        """


        Parameters
        ----------
        messaging_service_sid : str
            The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/services/api) to fetch the resource from.

        sid : str
            The SID of the US A2P Compliance resource to fetch `QE2c6890da8086d771620e9b13fadeba0b`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagingV1ServiceUsAppToPerson
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.fetch_us_app_to_person(
            messaging_service_sid="MessagingServiceSid",
            sid="Sid",
        )
        """
        _response = self._raw_client.fetch_us_app_to_person(messaging_service_sid, sid, request_options=request_options)
        return _response.data

    def delete_us_app_to_person(
        self, messaging_service_sid: str, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """


        Parameters
        ----------
        messaging_service_sid : str
            The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/services/api) to delete the resource from.

        sid : str
            The SID of the US A2P Compliance resource to delete `QE2c6890da8086d771620e9b13fadeba0b`.

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
        client.delete_us_app_to_person(
            messaging_service_sid="MessagingServiceSid",
            sid="Sid",
        )
        """
        _response = self._raw_client.delete_us_app_to_person(
            messaging_service_sid, sid, request_options=request_options
        )
        return _response.data

    def list_alpha_sender(
        self,
        service_sid: str,
        *,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListAlphaSenderResponse:
        """


        Parameters
        ----------
        service_sid : str
            The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to read the resources from.

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
        ListAlphaSenderResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.list_alpha_sender(
            service_sid="ServiceSid",
        )
        """
        _response = self._raw_client.list_alpha_sender(
            service_sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
        )
        return _response.data

    def create_alpha_sender(
        self, service_sid: str, *, alpha_sender: str, request_options: typing.Optional[RequestOptions] = None
    ) -> MessagingV1ServiceAlphaSender:
        """


        Parameters
        ----------
        service_sid : str
            The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to create the resource under.

        alpha_sender : str
            The Alphanumeric Sender ID string. Can be up to 11 characters long. Valid characters are A-Z, a-z, 0-9, space, hyphen `-`, plus `+`, underscore `_` and ampersand `&`. This value cannot contain only numbers.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagingV1ServiceAlphaSender
            Created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.create_alpha_sender(
            service_sid="ServiceSid",
            alpha_sender="AlphaSender",
        )
        """
        _response = self._raw_client.create_alpha_sender(
            service_sid, alpha_sender=alpha_sender, request_options=request_options
        )
        return _response.data

    def fetch_alpha_sender(
        self, service_sid: str, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MessagingV1ServiceAlphaSender:
        """


        Parameters
        ----------
        service_sid : str
            The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to fetch the resource from.

        sid : str
            The SID of the AlphaSender resource to fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagingV1ServiceAlphaSender
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.fetch_alpha_sender(
            service_sid="ServiceSid",
            sid="Sid",
        )
        """
        _response = self._raw_client.fetch_alpha_sender(service_sid, sid, request_options=request_options)
        return _response.data

    def delete_alpha_sender(
        self, service_sid: str, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """


        Parameters
        ----------
        service_sid : str
            The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to delete the resource from.

        sid : str
            The SID of the AlphaSender resource to delete.

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
        client.delete_alpha_sender(
            service_sid="ServiceSid",
            sid="Sid",
        )
        """
        _response = self._raw_client.delete_alpha_sender(service_sid, sid, request_options=request_options)
        return _response.data

    def list_phone_number(
        self,
        service_sid: str,
        *,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListPhoneNumberResponse:
        """


        Parameters
        ----------
        service_sid : str
            The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to read the resources from.

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
        ListPhoneNumberResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.list_phone_number(
            service_sid="ServiceSid",
        )
        """
        _response = self._raw_client.list_phone_number(
            service_sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
        )
        return _response.data

    def create_phone_number(
        self, service_sid: str, *, phone_number_sid: str, request_options: typing.Optional[RequestOptions] = None
    ) -> MessagingV1ServicePhoneNumber:
        """


        Parameters
        ----------
        service_sid : str
            The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to create the resource under.

        phone_number_sid : str
            The SID of the Phone Number being added to the Service.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagingV1ServicePhoneNumber
            Created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.create_phone_number(
            service_sid="ServiceSid",
            phone_number_sid="PhoneNumberSid",
        )
        """
        _response = self._raw_client.create_phone_number(
            service_sid, phone_number_sid=phone_number_sid, request_options=request_options
        )
        return _response.data

    def fetch_phone_number(
        self, service_sid: str, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MessagingV1ServicePhoneNumber:
        """


        Parameters
        ----------
        service_sid : str
            The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to fetch the resource from.

        sid : str
            The SID of the PhoneNumber resource to fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagingV1ServicePhoneNumber
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.fetch_phone_number(
            service_sid="ServiceSid",
            sid="Sid",
        )
        """
        _response = self._raw_client.fetch_phone_number(service_sid, sid, request_options=request_options)
        return _response.data

    def delete_phone_number(
        self, service_sid: str, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """


        Parameters
        ----------
        service_sid : str
            The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to delete the resource from.

        sid : str
            The SID of the PhoneNumber resource to delete.

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
        client.delete_phone_number(
            service_sid="ServiceSid",
            sid="Sid",
        )
        """
        _response = self._raw_client.delete_phone_number(service_sid, sid, request_options=request_options)
        return _response.data

    def list_short_code(
        self,
        service_sid: str,
        *,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListShortCodeResponse:
        """


        Parameters
        ----------
        service_sid : str
            The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to read the resources from.

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
        ListShortCodeResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.list_short_code(
            service_sid="ServiceSid",
        )
        """
        _response = self._raw_client.list_short_code(
            service_sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
        )
        return _response.data

    def create_short_code(
        self, service_sid: str, *, short_code_sid: str, request_options: typing.Optional[RequestOptions] = None
    ) -> MessagingV1ServiceShortCode:
        """


        Parameters
        ----------
        service_sid : str
            The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to create the resource under.

        short_code_sid : str
            The SID of the ShortCode resource being added to the Service.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagingV1ServiceShortCode
            Created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.create_short_code(
            service_sid="ServiceSid",
            short_code_sid="ShortCodeSid",
        )
        """
        _response = self._raw_client.create_short_code(
            service_sid, short_code_sid=short_code_sid, request_options=request_options
        )
        return _response.data

    def fetch_short_code(
        self, service_sid: str, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MessagingV1ServiceShortCode:
        """


        Parameters
        ----------
        service_sid : str
            The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to fetch the resource from.

        sid : str
            The SID of the ShortCode resource to fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagingV1ServiceShortCode
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.fetch_short_code(
            service_sid="ServiceSid",
            sid="Sid",
        )
        """
        _response = self._raw_client.fetch_short_code(service_sid, sid, request_options=request_options)
        return _response.data

    def delete_short_code(
        self, service_sid: str, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """


        Parameters
        ----------
        service_sid : str
            The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to delete the resource from.

        sid : str
            The SID of the ShortCode resource to delete.

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
        client.delete_short_code(
            service_sid="ServiceSid",
            sid="Sid",
        )
        """
        _response = self._raw_client.delete_short_code(service_sid, sid, request_options=request_options)
        return _response.data

    def fetch_service(self, sid: str, *, request_options: typing.Optional[RequestOptions] = None) -> MessagingV1Service:
        """


        Parameters
        ----------
        sid : str
            The SID of the Service resource to fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagingV1Service
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.fetch_service(
            sid="Sid",
        )
        """
        _response = self._raw_client.fetch_service(sid, request_options=request_options)
        return _response.data

    def update_service(
        self,
        sid: str,
        *,
        area_code_geomatch: typing.Optional[bool] = OMIT,
        fallback_method: typing.Optional[UpdateServiceRequestFallbackMethod] = OMIT,
        fallback_to_long_code: typing.Optional[bool] = OMIT,
        fallback_url: typing.Optional[str] = OMIT,
        friendly_name: typing.Optional[str] = OMIT,
        inbound_method: typing.Optional[UpdateServiceRequestInboundMethod] = OMIT,
        inbound_request_url: typing.Optional[str] = OMIT,
        mms_converter: typing.Optional[bool] = OMIT,
        scan_message_content: typing.Optional[ServiceEnumScanMessageContent] = OMIT,
        smart_encoding: typing.Optional[bool] = OMIT,
        status_callback: typing.Optional[str] = OMIT,
        sticky_sender: typing.Optional[bool] = OMIT,
        synchronous_validation: typing.Optional[bool] = OMIT,
        use_inbound_webhook_on_number: typing.Optional[bool] = OMIT,
        usecase: typing.Optional[str] = OMIT,
        validity_period: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MessagingV1Service:
        """


        Parameters
        ----------
        sid : str
            The SID of the Service resource to update.

        area_code_geomatch : typing.Optional[bool]
            Whether to enable [Area Code Geomatch](https://www.twilio.com/docs/sms/services#area-code-geomatch) on the Service Instance.

        fallback_method : typing.Optional[UpdateServiceRequestFallbackMethod]
            The HTTP method we should use to call `fallback_url`. Can be: `GET` or `POST`.

        fallback_to_long_code : typing.Optional[bool]
            Whether to enable [Fallback to Long Code](https://www.twilio.com/docs/sms/services#fallback-to-long-code) for messages sent through the Service instance.

        fallback_url : typing.Optional[str]
            The URL that we call using `fallback_method` if an error occurs while retrieving or executing the TwiML from the Inbound Request URL. If the `use_inbound_webhook_on_number` field is enabled then the webhook url defined on the phone number will override the `fallback_url` defined for the Messaging Service.

        friendly_name : typing.Optional[str]
            A descriptive string that you create to describe the resource. It can be up to 64 characters long.

        inbound_method : typing.Optional[UpdateServiceRequestInboundMethod]
            The HTTP method we should use to call `inbound_request_url`. Can be `GET` or `POST` and the default is `POST`.

        inbound_request_url : typing.Optional[str]
            The URL we call using `inbound_method` when a message is received by any phone number or short code in the Service. When this property is `null`, receiving inbound messages is disabled. All messages sent to the Twilio phone number or short code will not be logged and received on the Account. If the `use_inbound_webhook_on_number` field is enabled then the webhook url defined on the phone number will override the `inbound_request_url` defined for the Messaging Service.

        mms_converter : typing.Optional[bool]
            Whether to enable the [MMS Converter](https://www.twilio.com/docs/sms/services#mms-converter) for messages sent through the Service instance.

        scan_message_content : typing.Optional[ServiceEnumScanMessageContent]
            Reserved.

        smart_encoding : typing.Optional[bool]
            Whether to enable [Smart Encoding](https://www.twilio.com/docs/sms/services#smart-encoding) for messages sent through the Service instance.

        status_callback : typing.Optional[str]
            The URL we should call to [pass status updates](https://www.twilio.com/docs/sms/api/message-resource#message-status-values) about message delivery.

        sticky_sender : typing.Optional[bool]
            Whether to enable [Sticky Sender](https://www.twilio.com/docs/sms/services#sticky-sender) on the Service instance.

        synchronous_validation : typing.Optional[bool]
            Reserved.

        use_inbound_webhook_on_number : typing.Optional[bool]
            A boolean value that indicates either the webhook url configured on the phone number will be used or `inbound_request_url`/`fallback_url` url will be called when a message is received from the phone number. If this field is enabled then the webhook url defined on the phone number will override the `inbound_request_url`/`fallback_url` defined for the Messaging Service.

        usecase : typing.Optional[str]
            A string that describes the scenario in which the Messaging Service will be used. Examples: [notification, marketing, verification, poll ..]

        validity_period : typing.Optional[int]
            How long, in seconds, messages sent from the Service are valid. Can be an integer from `1` to `14,400`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagingV1Service
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.update_service(
            sid="Sid",
        )
        """
        _response = self._raw_client.update_service(
            sid,
            area_code_geomatch=area_code_geomatch,
            fallback_method=fallback_method,
            fallback_to_long_code=fallback_to_long_code,
            fallback_url=fallback_url,
            friendly_name=friendly_name,
            inbound_method=inbound_method,
            inbound_request_url=inbound_request_url,
            mms_converter=mms_converter,
            scan_message_content=scan_message_content,
            smart_encoding=smart_encoding,
            status_callback=status_callback,
            sticky_sender=sticky_sender,
            synchronous_validation=synchronous_validation,
            use_inbound_webhook_on_number=use_inbound_webhook_on_number,
            usecase=usecase,
            validity_period=validity_period,
            request_options=request_options,
        )
        return _response.data

    def delete_service(self, sid: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        sid : str
            The SID of the Service resource to delete.

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
        client.delete_service(
            sid="Sid",
        )
        """
        _response = self._raw_client.delete_service(sid, request_options=request_options)
        return _response.data

    def list_tollfree_verification(
        self,
        *,
        tollfree_phone_number_sid: typing.Optional[str] = None,
        status: typing.Optional[TollfreeVerificationEnumStatus] = None,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListTollfreeVerificationResponse:
        """


        Parameters
        ----------
        tollfree_phone_number_sid : typing.Optional[str]
            The SID of the Phone Number associated with the Tollfree Verification.

        status : typing.Optional[TollfreeVerificationEnumStatus]
            The compliance status of the Tollfree Verification record.

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
        ListTollfreeVerificationResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.list_tollfree_verification()
        """
        _response = self._raw_client.list_tollfree_verification(
            tollfree_phone_number_sid=tollfree_phone_number_sid,
            status=status,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        )
        return _response.data

    def create_tollfree_verification(
        self,
        *,
        business_name: str,
        business_website: str,
        message_volume: str,
        notification_email: str,
        opt_in_image_urls: typing.Sequence[str],
        opt_in_type: TollfreeVerificationEnumOptInType,
        production_message_sample: str,
        tollfree_phone_number_sid: str,
        use_case_categories: typing.Sequence[str],
        use_case_summary: str,
        additional_information: typing.Optional[str] = OMIT,
        business_city: typing.Optional[str] = OMIT,
        business_contact_email: typing.Optional[str] = OMIT,
        business_contact_first_name: typing.Optional[str] = OMIT,
        business_contact_last_name: typing.Optional[str] = OMIT,
        business_contact_phone: typing.Optional[str] = OMIT,
        business_country: typing.Optional[str] = OMIT,
        business_postal_code: typing.Optional[str] = OMIT,
        business_state_province_region: typing.Optional[str] = OMIT,
        business_street_address: typing.Optional[str] = OMIT,
        business_street_address2: typing.Optional[str] = OMIT,
        customer_profile_sid: typing.Optional[str] = OMIT,
        external_reference_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MessagingV1TollfreeVerification:
        """


        Parameters
        ----------
        business_name : str
            The name of the business or organization using the Tollfree number.

        business_website : str
            The website of the business or organization using the Tollfree number.

        message_volume : str
            Estimate monthly volume of messages from the Tollfree Number.

        notification_email : str
            The email address to receive the notification about the verification result. .

        opt_in_image_urls : typing.Sequence[str]
            Link to an image that shows the opt-in workflow. Multiple images allowed and must be a publicly hosted URL.

        opt_in_type : TollfreeVerificationEnumOptInType
            Describe how a user opts-in to text messages.

        production_message_sample : str
            An example of message content, i.e. a sample message.

        tollfree_phone_number_sid : str
            The SID of the Phone Number associated with the Tollfree Verification.

        use_case_categories : typing.Sequence[str]
            The category of the use case for the Tollfree Number. List as many are applicable..

        use_case_summary : str
            Use this to further explain how messaging is used by the business or organization.

        additional_information : typing.Optional[str]
            Additional information to be provided for verification.

        business_city : typing.Optional[str]
            The city of the business or organization using the Tollfree number.

        business_contact_email : typing.Optional[str]
            The email address of the contact for the business or organization using the Tollfree number.

        business_contact_first_name : typing.Optional[str]
            The first name of the contact for the business or organization using the Tollfree number.

        business_contact_last_name : typing.Optional[str]
            The last name of the contact for the business or organization using the Tollfree number.

        business_contact_phone : typing.Optional[str]
            The phone number of the contact for the business or organization using the Tollfree number.

        business_country : typing.Optional[str]
            The country of the business or organization using the Tollfree number.

        business_postal_code : typing.Optional[str]
            The postal code of the business or organization using the Tollfree number.

        business_state_province_region : typing.Optional[str]
            The state/province/region of the business or organization using the Tollfree number.

        business_street_address : typing.Optional[str]
            The address of the business or organization using the Tollfree number.

        business_street_address2 : typing.Optional[str]
            The address of the business or organization using the Tollfree number.

        customer_profile_sid : typing.Optional[str]
            Customer's Profile Bundle BundleSid.

        external_reference_id : typing.Optional[str]
            An optional external reference ID supplied by customer and echoed back on status retrieval.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagingV1TollfreeVerification
            Created

        Examples
        --------
        from fern import FernApi, TollfreeVerificationEnumOptInType

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.create_tollfree_verification(
            business_name="BusinessName",
            business_website="BusinessWebsite",
            message_volume="MessageVolume",
            notification_email="NotificationEmail",
            opt_in_image_urls=["OptInImageUrls"],
            opt_in_type=TollfreeVerificationEnumOptInType.VERBAL,
            production_message_sample="ProductionMessageSample",
            tollfree_phone_number_sid="TollfreePhoneNumberSid",
            use_case_categories=["UseCaseCategories"],
            use_case_summary="UseCaseSummary",
        )
        """
        _response = self._raw_client.create_tollfree_verification(
            business_name=business_name,
            business_website=business_website,
            message_volume=message_volume,
            notification_email=notification_email,
            opt_in_image_urls=opt_in_image_urls,
            opt_in_type=opt_in_type,
            production_message_sample=production_message_sample,
            tollfree_phone_number_sid=tollfree_phone_number_sid,
            use_case_categories=use_case_categories,
            use_case_summary=use_case_summary,
            additional_information=additional_information,
            business_city=business_city,
            business_contact_email=business_contact_email,
            business_contact_first_name=business_contact_first_name,
            business_contact_last_name=business_contact_last_name,
            business_contact_phone=business_contact_phone,
            business_country=business_country,
            business_postal_code=business_postal_code,
            business_state_province_region=business_state_province_region,
            business_street_address=business_street_address,
            business_street_address2=business_street_address2,
            customer_profile_sid=customer_profile_sid,
            external_reference_id=external_reference_id,
            request_options=request_options,
        )
        return _response.data

    def fetch_tollfree_verification(
        self, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MessagingV1TollfreeVerification:
        """


        Parameters
        ----------
        sid : str
            The unique string to identify Tollfree Verification.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagingV1TollfreeVerification
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.fetch_tollfree_verification(
            sid="Sid",
        )
        """
        _response = self._raw_client.fetch_tollfree_verification(sid, request_options=request_options)
        return _response.data

    def update_tollfree_verification(
        self,
        sid: str,
        *,
        additional_information: typing.Optional[str] = OMIT,
        business_city: typing.Optional[str] = OMIT,
        business_contact_email: typing.Optional[str] = OMIT,
        business_contact_first_name: typing.Optional[str] = OMIT,
        business_contact_last_name: typing.Optional[str] = OMIT,
        business_contact_phone: typing.Optional[str] = OMIT,
        business_country: typing.Optional[str] = OMIT,
        business_name: typing.Optional[str] = OMIT,
        business_postal_code: typing.Optional[str] = OMIT,
        business_state_province_region: typing.Optional[str] = OMIT,
        business_street_address: typing.Optional[str] = OMIT,
        business_street_address2: typing.Optional[str] = OMIT,
        business_website: typing.Optional[str] = OMIT,
        message_volume: typing.Optional[str] = OMIT,
        notification_email: typing.Optional[str] = OMIT,
        opt_in_image_urls: typing.Optional[typing.Sequence[str]] = OMIT,
        opt_in_type: typing.Optional[TollfreeVerificationEnumOptInType] = OMIT,
        production_message_sample: typing.Optional[str] = OMIT,
        use_case_categories: typing.Optional[typing.Sequence[str]] = OMIT,
        use_case_summary: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MessagingV1TollfreeVerification:
        """


        Parameters
        ----------
        sid : str
            The unique string to identify Tollfree Verification.

        additional_information : typing.Optional[str]
            Additional information to be provided for verification.

        business_city : typing.Optional[str]
            The city of the business or organization using the Tollfree number.

        business_contact_email : typing.Optional[str]
            The email address of the contact for the business or organization using the Tollfree number.

        business_contact_first_name : typing.Optional[str]
            The first name of the contact for the business or organization using the Tollfree number.

        business_contact_last_name : typing.Optional[str]
            The last name of the contact for the business or organization using the Tollfree number.

        business_contact_phone : typing.Optional[str]
            The phone number of the contact for the business or organization using the Tollfree number.

        business_country : typing.Optional[str]
            The country of the business or organization using the Tollfree number.

        business_name : typing.Optional[str]
            The name of the business or organization using the Tollfree number.

        business_postal_code : typing.Optional[str]
            The postal code of the business or organization using the Tollfree number.

        business_state_province_region : typing.Optional[str]
            The state/province/region of the business or organization using the Tollfree number.

        business_street_address : typing.Optional[str]
            The address of the business or organization using the Tollfree number.

        business_street_address2 : typing.Optional[str]
            The address of the business or organization using the Tollfree number.

        business_website : typing.Optional[str]
            The website of the business or organization using the Tollfree number.

        message_volume : typing.Optional[str]
            Estimate monthly volume of messages from the Tollfree Number.

        notification_email : typing.Optional[str]
            The email address to receive the notification about the verification result. .

        opt_in_image_urls : typing.Optional[typing.Sequence[str]]
            Link to an image that shows the opt-in workflow. Multiple images allowed and must be a publicly hosted URL.

        opt_in_type : typing.Optional[TollfreeVerificationEnumOptInType]
            Describe how a user opts-in to text messages.

        production_message_sample : typing.Optional[str]
            An example of message content, i.e. a sample message.

        use_case_categories : typing.Optional[typing.Sequence[str]]
            The category of the use case for the Tollfree Number. List as many are applicable..

        use_case_summary : typing.Optional[str]
            Use this to further explain how messaging is used by the business or organization.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagingV1TollfreeVerification
            Accepted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.update_tollfree_verification(
            sid="Sid",
        )
        """
        _response = self._raw_client.update_tollfree_verification(
            sid,
            additional_information=additional_information,
            business_city=business_city,
            business_contact_email=business_contact_email,
            business_contact_first_name=business_contact_first_name,
            business_contact_last_name=business_contact_last_name,
            business_contact_phone=business_contact_phone,
            business_country=business_country,
            business_name=business_name,
            business_postal_code=business_postal_code,
            business_state_province_region=business_state_province_region,
            business_street_address=business_street_address,
            business_street_address2=business_street_address2,
            business_website=business_website,
            message_volume=message_volume,
            notification_email=notification_email,
            opt_in_image_urls=opt_in_image_urls,
            opt_in_type=opt_in_type,
            production_message_sample=production_message_sample,
            use_case_categories=use_case_categories,
            use_case_summary=use_case_summary,
            request_options=request_options,
        )
        return _response.data

    def list_brand_registrations(
        self,
        *,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListBrandRegistrationsResponse:
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
        ListBrandRegistrationsResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.list_brand_registrations()
        """
        _response = self._raw_client.list_brand_registrations(
            page_size=page_size, page=page, page_token=page_token, request_options=request_options
        )
        return _response.data

    def create_brand_registrations(
        self,
        *,
        a2p_profile_bundle_sid: str,
        customer_profile_bundle_sid: str,
        brand_type: typing.Optional[str] = OMIT,
        mock: typing.Optional[bool] = OMIT,
        skip_automatic_sec_vet: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MessagingV1BrandRegistrations:
        """


        Parameters
        ----------
        a2p_profile_bundle_sid : str
            A2P Messaging Profile Bundle Sid.

        customer_profile_bundle_sid : str
            Customer Profile Bundle Sid.

        brand_type : typing.Optional[str]
            Type of brand being created. One of: "STANDARD", "SOLE_PROPRIETOR". SOLE_PROPRIETOR is for low volume, SOLE_PROPRIETOR use cases. STANDARD is for all other use cases.

        mock : typing.Optional[bool]
            A boolean that specifies whether brand should be a mock or not. If true, brand will be registered as a mock brand. Defaults to false if no value is provided.

        skip_automatic_sec_vet : typing.Optional[bool]
            A flag to disable automatic secondary vetting for brands which it would otherwise be done.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagingV1BrandRegistrations
            Created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.create_brand_registrations(
            a2p_profile_bundle_sid="A2PProfileBundleSid",
            customer_profile_bundle_sid="CustomerProfileBundleSid",
        )
        """
        _response = self._raw_client.create_brand_registrations(
            a2p_profile_bundle_sid=a2p_profile_bundle_sid,
            customer_profile_bundle_sid=customer_profile_bundle_sid,
            brand_type=brand_type,
            mock=mock,
            skip_automatic_sec_vet=skip_automatic_sec_vet,
            request_options=request_options,
        )
        return _response.data

    def create_brand_registration_otp(
        self, brand_registration_sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MessagingV1BrandRegistrationsBrandRegistrationOtp:
        """


        Parameters
        ----------
        brand_registration_sid : str
            Brand Registration Sid of Sole Proprietor Brand.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagingV1BrandRegistrationsBrandRegistrationOtp
            Created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.create_brand_registration_otp(
            brand_registration_sid="BrandRegistrationSid",
        )
        """
        _response = self._raw_client.create_brand_registration_otp(
            brand_registration_sid, request_options=request_options
        )
        return _response.data

    def list_brand_vetting(
        self,
        brand_sid: str,
        *,
        vetting_provider: typing.Optional[BrandVettingEnumVettingProvider] = None,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListBrandVettingResponse:
        """


        Parameters
        ----------
        brand_sid : str
            The SID of the Brand Registration resource of the vettings to read .

        vetting_provider : typing.Optional[BrandVettingEnumVettingProvider]
            The third-party provider of the vettings to read

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
        ListBrandVettingResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.list_brand_vetting(
            brand_sid="BrandSid",
        )
        """
        _response = self._raw_client.list_brand_vetting(
            brand_sid,
            vetting_provider=vetting_provider,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        )
        return _response.data

    def create_brand_vetting(
        self,
        brand_sid: str,
        *,
        vetting_provider: BrandVettingEnumVettingProvider,
        vetting_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MessagingV1BrandRegistrationsBrandVetting:
        """


        Parameters
        ----------
        brand_sid : str
            The SID of the Brand Registration resource of the vettings to create .

        vetting_provider : BrandVettingEnumVettingProvider
            The third-party provider of the vettings to create .

        vetting_id : typing.Optional[str]
            The unique ID of the vetting

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagingV1BrandRegistrationsBrandVetting
            Created

        Examples
        --------
        from fern import BrandVettingEnumVettingProvider, FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.create_brand_vetting(
            brand_sid="BrandSid",
            vetting_provider=BrandVettingEnumVettingProvider.CAMPAIGN_VERIFY,
        )
        """
        _response = self._raw_client.create_brand_vetting(
            brand_sid, vetting_provider=vetting_provider, vetting_id=vetting_id, request_options=request_options
        )
        return _response.data

    def fetch_brand_vetting(
        self, brand_sid: str, brand_vetting_sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MessagingV1BrandRegistrationsBrandVetting:
        """


        Parameters
        ----------
        brand_sid : str
            The SID of the Brand Registration resource of the vettings to read .

        brand_vetting_sid : str
            The Twilio SID of the third-party vetting record.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagingV1BrandRegistrationsBrandVetting
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.fetch_brand_vetting(
            brand_sid="BrandSid",
            brand_vetting_sid="BrandVettingSid",
        )
        """
        _response = self._raw_client.fetch_brand_vetting(brand_sid, brand_vetting_sid, request_options=request_options)
        return _response.data

    def fetch_brand_registrations(
        self, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MessagingV1BrandRegistrations:
        """


        Parameters
        ----------
        sid : str
            The SID of the Brand Registration resource to fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagingV1BrandRegistrations
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.fetch_brand_registrations(
            sid="Sid",
        )
        """
        _response = self._raw_client.fetch_brand_registrations(sid, request_options=request_options)
        return _response.data

    def update_brand_registrations(
        self, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MessagingV1BrandRegistrations:
        """


        Parameters
        ----------
        sid : str
            The SID of the Brand Registration resource to update.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagingV1BrandRegistrations
            Accepted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.update_brand_registrations(
            sid="Sid",
        )
        """
        _response = self._raw_client.update_brand_registrations(sid, request_options=request_options)
        return _response.data


def _make_default_async_client(
    timeout: typing.Optional[float],
    follow_redirects: typing.Optional[bool],
) -> httpx.AsyncClient:
    try:
        import httpx_aiohttp
    except ImportError:
        pass
    else:
        if follow_redirects is not None:
            return httpx_aiohttp.HttpxAiohttpClient(timeout=timeout, follow_redirects=follow_redirects)
        return httpx_aiohttp.HttpxAiohttpClient(timeout=timeout)

    if follow_redirects is not None:
        return httpx.AsyncClient(timeout=timeout, follow_redirects=follow_redirects)
    return httpx.AsyncClient(timeout=timeout)


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

    max_retries : typing.Optional[int]
        The default maximum number of retries for failed requests. Defaults to 2. Per-request `max_retries` in `request_options` takes precedence over this value.

    stream_reconnection_enabled : typing.Optional[bool]
        Whether to automatically reconnect on stream disconnection for resumable streaming endpoints. Defaults to True. Per-request `stream_reconnection_enabled` in `request_options` takes precedence over this value.

    max_stream_reconnection_attempts : typing.Optional[int]
        The maximum number of reconnection attempts for resumable streaming endpoints. Defaults to no limit. Per-request `max_stream_reconnection_attempts` in `request_options` takes precedence over this value.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.AsyncClient]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    logging : typing.Optional[typing.Union[LogConfig, Logger]]
        Configure logging for the SDK. Accepts a LogConfig dict with 'level' (debug/info/warn/error), 'logger' (custom logger implementation), and 'silent' (boolean, defaults to True) fields. You can also pass a pre-configured Logger instance.

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
        max_retries: typing.Optional[int] = None,
        stream_reconnection_enabled: typing.Optional[bool] = None,
        max_stream_reconnection_attempts: typing.Optional[int] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
        logging: typing.Optional[typing.Union[LogConfig, Logger]] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        _defaulted_max_retries = max_retries if max_retries is not None else 2
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            username=username,
            password=password,
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else _make_default_async_client(timeout=_defaulted_timeout, follow_redirects=follow_redirects),
            timeout=_defaulted_timeout,
            max_retries=_defaulted_max_retries,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
            logging=logging,
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

    async def fetch_deactivation(
        self, *, date: typing.Optional[dt.date] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Fetch a list of all United States numbers that have been deactivated on a specific date.

        Parameters
        ----------
        date : typing.Optional[dt.date]
            The request will return a list of all United States Phone Numbers that were deactivated on the day specified by this parameter. This date should be specified in YYYY-MM-DD format.

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
            await client.fetch_deactivation()


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_deactivation(date=date, request_options=request_options)
        return _response.data

    async def fetch_domain_cert_v4(
        self, domain_sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MessagingV1DomainCertV4:
        """


        Parameters
        ----------
        domain_sid : str
            Unique string used to identify the domain that this certificate should be associated with.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagingV1DomainCertV4
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
            await client.fetch_domain_cert_v4(
                domain_sid="DomainSid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_domain_cert_v4(domain_sid, request_options=request_options)
        return _response.data

    async def update_domain_cert_v4(
        self, domain_sid: str, *, tls_cert: str, request_options: typing.Optional[RequestOptions] = None
    ) -> MessagingV1DomainCertV4:
        """


        Parameters
        ----------
        domain_sid : str
            Unique string used to identify the domain that this certificate should be associated with.

        tls_cert : str
            Contains the full TLS certificate and private for this domain in PEM format: https://en.wikipedia.org/wiki/Privacy-Enhanced_Mail. Twilio uses this information to process HTTPS traffic sent to your domain.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagingV1DomainCertV4
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
            await client.update_domain_cert_v4(
                domain_sid="DomainSid",
                tls_cert="TlsCert",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_domain_cert_v4(
            domain_sid, tls_cert=tls_cert, request_options=request_options
        )
        return _response.data

    async def delete_domain_cert_v4(
        self, domain_sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """


        Parameters
        ----------
        domain_sid : str
            Unique string used to identify the domain that this certificate should be associated with.

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
            await client.delete_domain_cert_v4(
                domain_sid="DomainSid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_domain_cert_v4(domain_sid, request_options=request_options)
        return _response.data

    async def fetch_domain_config(
        self, domain_sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MessagingV1DomainConfig:
        """


        Parameters
        ----------
        domain_sid : str
            Unique string used to identify the domain that this config should be associated with.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagingV1DomainConfig
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
            await client.fetch_domain_config(
                domain_sid="DomainSid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_domain_config(domain_sid, request_options=request_options)
        return _response.data

    async def update_domain_config(
        self,
        domain_sid: str,
        *,
        callback_url: typing.Optional[str] = OMIT,
        fallback_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MessagingV1DomainConfig:
        """


        Parameters
        ----------
        domain_sid : str
            Unique string used to identify the domain that this config should be associated with.

        callback_url : typing.Optional[str]
            URL to receive click events to your webhook whenever the recipients click on the shortened links

        fallback_url : typing.Optional[str]
            Any requests we receive to this domain that do not match an existing shortened message will be redirected to the fallback url. These will likely be either expired messages, random misdirected traffic, or intentional scraping.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagingV1DomainConfig
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
            await client.update_domain_config(
                domain_sid="DomainSid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_domain_config(
            domain_sid, callback_url=callback_url, fallback_url=fallback_url, request_options=request_options
        )
        return _response.data

    async def create_linkshortening_messaging_service(
        self, domain_sid: str, messaging_service_sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MessagingV1LinkshorteningMessagingService:
        """


        Parameters
        ----------
        domain_sid : str
            The domain SID to associate with a messaging service. With URL shortening enabled, links in messages sent with the associated messaging service will be shortened to the provided domain

        messaging_service_sid : str
            A messaging service SID to associate with a domain. With URL shortening enabled, links in messages sent with the provided messaging service will be shortened to the associated domain

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagingV1LinkshorteningMessagingService
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
            await client.create_linkshortening_messaging_service(
                domain_sid="DomainSid",
                messaging_service_sid="MessagingServiceSid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_linkshortening_messaging_service(
            domain_sid, messaging_service_sid, request_options=request_options
        )
        return _response.data

    async def delete_linkshortening_messaging_service(
        self, domain_sid: str, messaging_service_sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """


        Parameters
        ----------
        domain_sid : str
            The domain SID to dissociate from a messaging service. With URL shortening enabled, links in messages sent with the associated messaging service will be shortened to the provided domain

        messaging_service_sid : str
            A messaging service SID to dissociate from a domain. With URL shortening enabled, links in messages sent with the provided messaging service will be shortened to the associated domain

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
            await client.delete_linkshortening_messaging_service(
                domain_sid="DomainSid",
                messaging_service_sid="MessagingServiceSid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_linkshortening_messaging_service(
            domain_sid, messaging_service_sid, request_options=request_options
        )
        return _response.data

    async def fetch_domain_config_messaging_service(
        self, messaging_service_sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MessagingV1DomainConfigMessagingService:
        """


        Parameters
        ----------
        messaging_service_sid : str
            Unique string used to identify the Messaging service that this domain should be associated with.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagingV1DomainConfigMessagingService
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
            await client.fetch_domain_config_messaging_service(
                messaging_service_sid="MessagingServiceSid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_domain_config_messaging_service(
            messaging_service_sid, request_options=request_options
        )
        return _response.data

    async def list_service(
        self,
        *,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListServiceResponse:
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
        ListServiceResponse
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
            await client.list_service()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_service(
            page_size=page_size, page=page, page_token=page_token, request_options=request_options
        )
        return _response.data

    async def create_service(
        self,
        *,
        friendly_name: str,
        area_code_geomatch: typing.Optional[bool] = OMIT,
        fallback_method: typing.Optional[CreateServiceRequestFallbackMethod] = OMIT,
        fallback_to_long_code: typing.Optional[bool] = OMIT,
        fallback_url: typing.Optional[str] = OMIT,
        inbound_method: typing.Optional[CreateServiceRequestInboundMethod] = OMIT,
        inbound_request_url: typing.Optional[str] = OMIT,
        mms_converter: typing.Optional[bool] = OMIT,
        scan_message_content: typing.Optional[ServiceEnumScanMessageContent] = OMIT,
        smart_encoding: typing.Optional[bool] = OMIT,
        status_callback: typing.Optional[str] = OMIT,
        sticky_sender: typing.Optional[bool] = OMIT,
        synchronous_validation: typing.Optional[bool] = OMIT,
        use_inbound_webhook_on_number: typing.Optional[bool] = OMIT,
        usecase: typing.Optional[str] = OMIT,
        validity_period: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MessagingV1Service:
        """


        Parameters
        ----------
        friendly_name : str
            A descriptive string that you create to describe the resource. It can be up to 64 characters long.

        area_code_geomatch : typing.Optional[bool]
            Whether to enable [Area Code Geomatch](https://www.twilio.com/docs/sms/services#area-code-geomatch) on the Service Instance.

        fallback_method : typing.Optional[CreateServiceRequestFallbackMethod]
            The HTTP method we should use to call `fallback_url`. Can be: `GET` or `POST`.

        fallback_to_long_code : typing.Optional[bool]
            Whether to enable [Fallback to Long Code](https://www.twilio.com/docs/sms/services#fallback-to-long-code) for messages sent through the Service instance.

        fallback_url : typing.Optional[str]
            The URL that we call using `fallback_method` if an error occurs while retrieving or executing the TwiML from the Inbound Request URL. If the `use_inbound_webhook_on_number` field is enabled then the webhook url defined on the phone number will override the `fallback_url` defined for the Messaging Service.

        inbound_method : typing.Optional[CreateServiceRequestInboundMethod]
            The HTTP method we should use to call `inbound_request_url`. Can be `GET` or `POST` and the default is `POST`.

        inbound_request_url : typing.Optional[str]
            The URL we call using `inbound_method` when a message is received by any phone number or short code in the Service. When this property is `null`, receiving inbound messages is disabled. All messages sent to the Twilio phone number or short code will not be logged and received on the Account. If the `use_inbound_webhook_on_number` field is enabled then the webhook url defined on the phone number will override the `inbound_request_url` defined for the Messaging Service.

        mms_converter : typing.Optional[bool]
            Whether to enable the [MMS Converter](https://www.twilio.com/docs/sms/services#mms-converter) for messages sent through the Service instance.

        scan_message_content : typing.Optional[ServiceEnumScanMessageContent]
            Reserved.

        smart_encoding : typing.Optional[bool]
            Whether to enable [Smart Encoding](https://www.twilio.com/docs/sms/services#smart-encoding) for messages sent through the Service instance.

        status_callback : typing.Optional[str]
            The URL we should call to [pass status updates](https://www.twilio.com/docs/sms/api/message-resource#message-status-values) about message delivery.

        sticky_sender : typing.Optional[bool]
            Whether to enable [Sticky Sender](https://www.twilio.com/docs/sms/services#sticky-sender) on the Service instance.

        synchronous_validation : typing.Optional[bool]
            Reserved.

        use_inbound_webhook_on_number : typing.Optional[bool]
            A boolean value that indicates either the webhook url configured on the phone number will be used or `inbound_request_url`/`fallback_url` url will be called when a message is received from the phone number. If this field is enabled then the webhook url defined on the phone number will override the `inbound_request_url`/`fallback_url` defined for the Messaging Service.

        usecase : typing.Optional[str]
            A string that describes the scenario in which the Messaging Service will be used. Examples: [notification, marketing, verification, poll ..].

        validity_period : typing.Optional[int]
            How long, in seconds, messages sent from the Service are valid. Can be an integer from `1` to `14,400`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagingV1Service
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
            await client.create_service(
                friendly_name="FriendlyName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_service(
            friendly_name=friendly_name,
            area_code_geomatch=area_code_geomatch,
            fallback_method=fallback_method,
            fallback_to_long_code=fallback_to_long_code,
            fallback_url=fallback_url,
            inbound_method=inbound_method,
            inbound_request_url=inbound_request_url,
            mms_converter=mms_converter,
            scan_message_content=scan_message_content,
            smart_encoding=smart_encoding,
            status_callback=status_callback,
            sticky_sender=sticky_sender,
            synchronous_validation=synchronous_validation,
            use_inbound_webhook_on_number=use_inbound_webhook_on_number,
            usecase=usecase,
            validity_period=validity_period,
            request_options=request_options,
        )
        return _response.data

    async def create_external_campaign(
        self, *, campaign_id: str, messaging_service_sid: str, request_options: typing.Optional[RequestOptions] = None
    ) -> MessagingV1ExternalCampaign:
        """


        Parameters
        ----------
        campaign_id : str
            ID of the preregistered campaign.

        messaging_service_sid : str
            The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/services/api) that the resource is associated with.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagingV1ExternalCampaign
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
            await client.create_external_campaign(
                campaign_id="CampaignId",
                messaging_service_sid="MessagingServiceSid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_external_campaign(
            campaign_id=campaign_id, messaging_service_sid=messaging_service_sid, request_options=request_options
        )
        return _response.data

    async def fetch_usecase(self, *, request_options: typing.Optional[RequestOptions] = None) -> MessagingV1Usecase:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagingV1Usecase
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
            await client.fetch_usecase()


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_usecase(request_options=request_options)
        return _response.data

    async def list_us_app_to_person(
        self,
        messaging_service_sid: str,
        *,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListUsAppToPersonResponse:
        """


        Parameters
        ----------
        messaging_service_sid : str
            The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/services/api) to fetch the resource from.

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
        ListUsAppToPersonResponse
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
            await client.list_us_app_to_person(
                messaging_service_sid="MessagingServiceSid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_us_app_to_person(
            messaging_service_sid,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        )
        return _response.data

    async def create_us_app_to_person(
        self,
        messaging_service_sid: str,
        *,
        brand_registration_sid: str,
        description: str,
        has_embedded_links: bool,
        has_embedded_phone: bool,
        message_flow: str,
        message_samples: typing.Sequence[str],
        us_app_to_person_usecase: str,
        help_keywords: typing.Optional[typing.Sequence[str]] = OMIT,
        help_message: typing.Optional[str] = OMIT,
        opt_in_keywords: typing.Optional[typing.Sequence[str]] = OMIT,
        opt_in_message: typing.Optional[str] = OMIT,
        opt_out_keywords: typing.Optional[typing.Sequence[str]] = OMIT,
        opt_out_message: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MessagingV1ServiceUsAppToPerson:
        """


        Parameters
        ----------
        messaging_service_sid : str
            The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/services/api) to create the resources from.

        brand_registration_sid : str
            A2P Brand Registration SID

        description : str
            A short description of what this SMS campaign does. Min length: 40 characters. Max length: 4096 characters.

        has_embedded_links : bool
            Indicates that this SMS campaign will send messages that contain links.

        has_embedded_phone : bool
            Indicates that this SMS campaign will send messages that contain phone numbers.

        message_flow : str
            Required for all Campaigns. Details around how a consumer opts-in to their campaign, therefore giving consent to receive their messages. If multiple opt-in methods can be used for the same campaign, they must all be listed. 40 character minimum. 2048 character maximum.

        message_samples : typing.Sequence[str]
            Message samples, at least 1 and up to 5 sample messages (at least 2 for sole proprietor), >=20 chars, <=1024 chars each.

        us_app_to_person_usecase : str
            A2P Campaign Use Case. Examples: [ 2FA, EMERGENCY, MARKETING..]

        help_keywords : typing.Optional[typing.Sequence[str]]
            End users should be able to text in a keyword to receive help. Those keywords must be provided as part of the campaign registration request. This field is required if managing help keywords yourself (i.e. not using Twilio's Default or Advanced Opt Out features). Values must be alphanumeric. 255 character maximum.

        help_message : typing.Optional[str]
            When customers receive the help keywords from their end users, Twilio customers are expected to send back an auto-generated response; this may include the brand name and additional support contact information. This field is required if managing help keywords yourself (i.e. not using Twilio's Default or Advanced Opt Out features). 20 character minimum. 320 character maximum.

        opt_in_keywords : typing.Optional[typing.Sequence[str]]
            If end users can text in a keyword to start receiving messages from this campaign, those keywords must be provided. This field is required if end users can text in a keyword to start receiving messages from this campaign. Values must be alphanumeric. 255 character maximum.

        opt_in_message : typing.Optional[str]
            If end users can text in a keyword to start receiving messages from this campaign, the auto-reply messages sent to the end users must be provided. The opt-in response should include the Brand name, confirmation of opt-in enrollment to a recurring message campaign, how to get help, and clear description of how to opt-out. This field is required if end users can text in a keyword to start receiving messages from this campaign. 20 character minimum. 320 character maximum.

        opt_out_keywords : typing.Optional[typing.Sequence[str]]
            End users should be able to text in a keyword to stop receiving messages from this campaign. Those keywords must be provided. This field is required if managing opt out keywords yourself (i.e. not using Twilio's Default or Advanced Opt Out features). Values must be alphanumeric. 255 character maximum.

        opt_out_message : typing.Optional[str]
            Upon receiving the opt-out keywords from the end users, Twilio customers are expected to send back an auto-generated response, which must provide acknowledgment of the opt-out request and confirmation that no further messages will be sent. It is also recommended that these opt-out messages include the brand name. This field is required if managing opt out keywords yourself (i.e. not using Twilio's Default or Advanced Opt Out features). 20 character minimum. 320 character maximum.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagingV1ServiceUsAppToPerson
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
            await client.create_us_app_to_person(
                messaging_service_sid="MessagingServiceSid",
                brand_registration_sid="BrandRegistrationSid",
                description="Description",
                has_embedded_links=True,
                has_embedded_phone=True,
                message_flow="MessageFlow",
                message_samples=["MessageSamples"],
                us_app_to_person_usecase="UsAppToPersonUsecase",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_us_app_to_person(
            messaging_service_sid,
            brand_registration_sid=brand_registration_sid,
            description=description,
            has_embedded_links=has_embedded_links,
            has_embedded_phone=has_embedded_phone,
            message_flow=message_flow,
            message_samples=message_samples,
            us_app_to_person_usecase=us_app_to_person_usecase,
            help_keywords=help_keywords,
            help_message=help_message,
            opt_in_keywords=opt_in_keywords,
            opt_in_message=opt_in_message,
            opt_out_keywords=opt_out_keywords,
            opt_out_message=opt_out_message,
            request_options=request_options,
        )
        return _response.data

    async def fetch_us_app_to_person_usecase(
        self,
        messaging_service_sid: str,
        *,
        brand_registration_sid: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MessagingV1ServiceUsAppToPersonUsecase:
        """


        Parameters
        ----------
        messaging_service_sid : str
            The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/services/api) to fetch the resource from.

        brand_registration_sid : typing.Optional[str]
            The unique string to identify the A2P brand.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagingV1ServiceUsAppToPersonUsecase
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
            await client.fetch_us_app_to_person_usecase(
                messaging_service_sid="MessagingServiceSid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_us_app_to_person_usecase(
            messaging_service_sid, brand_registration_sid=brand_registration_sid, request_options=request_options
        )
        return _response.data

    async def fetch_us_app_to_person(
        self, messaging_service_sid: str, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MessagingV1ServiceUsAppToPerson:
        """


        Parameters
        ----------
        messaging_service_sid : str
            The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/services/api) to fetch the resource from.

        sid : str
            The SID of the US A2P Compliance resource to fetch `QE2c6890da8086d771620e9b13fadeba0b`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagingV1ServiceUsAppToPerson
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
            await client.fetch_us_app_to_person(
                messaging_service_sid="MessagingServiceSid",
                sid="Sid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_us_app_to_person(
            messaging_service_sid, sid, request_options=request_options
        )
        return _response.data

    async def delete_us_app_to_person(
        self, messaging_service_sid: str, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """


        Parameters
        ----------
        messaging_service_sid : str
            The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/services/api) to delete the resource from.

        sid : str
            The SID of the US A2P Compliance resource to delete `QE2c6890da8086d771620e9b13fadeba0b`.

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
            await client.delete_us_app_to_person(
                messaging_service_sid="MessagingServiceSid",
                sid="Sid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_us_app_to_person(
            messaging_service_sid, sid, request_options=request_options
        )
        return _response.data

    async def list_alpha_sender(
        self,
        service_sid: str,
        *,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListAlphaSenderResponse:
        """


        Parameters
        ----------
        service_sid : str
            The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to read the resources from.

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
        ListAlphaSenderResponse
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
            await client.list_alpha_sender(
                service_sid="ServiceSid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_alpha_sender(
            service_sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
        )
        return _response.data

    async def create_alpha_sender(
        self, service_sid: str, *, alpha_sender: str, request_options: typing.Optional[RequestOptions] = None
    ) -> MessagingV1ServiceAlphaSender:
        """


        Parameters
        ----------
        service_sid : str
            The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to create the resource under.

        alpha_sender : str
            The Alphanumeric Sender ID string. Can be up to 11 characters long. Valid characters are A-Z, a-z, 0-9, space, hyphen `-`, plus `+`, underscore `_` and ampersand `&`. This value cannot contain only numbers.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagingV1ServiceAlphaSender
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
            await client.create_alpha_sender(
                service_sid="ServiceSid",
                alpha_sender="AlphaSender",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_alpha_sender(
            service_sid, alpha_sender=alpha_sender, request_options=request_options
        )
        return _response.data

    async def fetch_alpha_sender(
        self, service_sid: str, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MessagingV1ServiceAlphaSender:
        """


        Parameters
        ----------
        service_sid : str
            The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to fetch the resource from.

        sid : str
            The SID of the AlphaSender resource to fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagingV1ServiceAlphaSender
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
            await client.fetch_alpha_sender(
                service_sid="ServiceSid",
                sid="Sid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_alpha_sender(service_sid, sid, request_options=request_options)
        return _response.data

    async def delete_alpha_sender(
        self, service_sid: str, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """


        Parameters
        ----------
        service_sid : str
            The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to delete the resource from.

        sid : str
            The SID of the AlphaSender resource to delete.

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
            await client.delete_alpha_sender(
                service_sid="ServiceSid",
                sid="Sid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_alpha_sender(service_sid, sid, request_options=request_options)
        return _response.data

    async def list_phone_number(
        self,
        service_sid: str,
        *,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListPhoneNumberResponse:
        """


        Parameters
        ----------
        service_sid : str
            The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to read the resources from.

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
        ListPhoneNumberResponse
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
            await client.list_phone_number(
                service_sid="ServiceSid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_phone_number(
            service_sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
        )
        return _response.data

    async def create_phone_number(
        self, service_sid: str, *, phone_number_sid: str, request_options: typing.Optional[RequestOptions] = None
    ) -> MessagingV1ServicePhoneNumber:
        """


        Parameters
        ----------
        service_sid : str
            The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to create the resource under.

        phone_number_sid : str
            The SID of the Phone Number being added to the Service.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagingV1ServicePhoneNumber
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
            await client.create_phone_number(
                service_sid="ServiceSid",
                phone_number_sid="PhoneNumberSid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_phone_number(
            service_sid, phone_number_sid=phone_number_sid, request_options=request_options
        )
        return _response.data

    async def fetch_phone_number(
        self, service_sid: str, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MessagingV1ServicePhoneNumber:
        """


        Parameters
        ----------
        service_sid : str
            The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to fetch the resource from.

        sid : str
            The SID of the PhoneNumber resource to fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagingV1ServicePhoneNumber
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
            await client.fetch_phone_number(
                service_sid="ServiceSid",
                sid="Sid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_phone_number(service_sid, sid, request_options=request_options)
        return _response.data

    async def delete_phone_number(
        self, service_sid: str, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """


        Parameters
        ----------
        service_sid : str
            The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to delete the resource from.

        sid : str
            The SID of the PhoneNumber resource to delete.

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
            await client.delete_phone_number(
                service_sid="ServiceSid",
                sid="Sid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_phone_number(service_sid, sid, request_options=request_options)
        return _response.data

    async def list_short_code(
        self,
        service_sid: str,
        *,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListShortCodeResponse:
        """


        Parameters
        ----------
        service_sid : str
            The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to read the resources from.

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
        ListShortCodeResponse
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
            await client.list_short_code(
                service_sid="ServiceSid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_short_code(
            service_sid, page_size=page_size, page=page, page_token=page_token, request_options=request_options
        )
        return _response.data

    async def create_short_code(
        self, service_sid: str, *, short_code_sid: str, request_options: typing.Optional[RequestOptions] = None
    ) -> MessagingV1ServiceShortCode:
        """


        Parameters
        ----------
        service_sid : str
            The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to create the resource under.

        short_code_sid : str
            The SID of the ShortCode resource being added to the Service.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagingV1ServiceShortCode
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
            await client.create_short_code(
                service_sid="ServiceSid",
                short_code_sid="ShortCodeSid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_short_code(
            service_sid, short_code_sid=short_code_sid, request_options=request_options
        )
        return _response.data

    async def fetch_short_code(
        self, service_sid: str, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MessagingV1ServiceShortCode:
        """


        Parameters
        ----------
        service_sid : str
            The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to fetch the resource from.

        sid : str
            The SID of the ShortCode resource to fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagingV1ServiceShortCode
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
            await client.fetch_short_code(
                service_sid="ServiceSid",
                sid="Sid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_short_code(service_sid, sid, request_options=request_options)
        return _response.data

    async def delete_short_code(
        self, service_sid: str, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """


        Parameters
        ----------
        service_sid : str
            The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to delete the resource from.

        sid : str
            The SID of the ShortCode resource to delete.

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
            await client.delete_short_code(
                service_sid="ServiceSid",
                sid="Sid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_short_code(service_sid, sid, request_options=request_options)
        return _response.data

    async def fetch_service(
        self, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MessagingV1Service:
        """


        Parameters
        ----------
        sid : str
            The SID of the Service resource to fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagingV1Service
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
            await client.fetch_service(
                sid="Sid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_service(sid, request_options=request_options)
        return _response.data

    async def update_service(
        self,
        sid: str,
        *,
        area_code_geomatch: typing.Optional[bool] = OMIT,
        fallback_method: typing.Optional[UpdateServiceRequestFallbackMethod] = OMIT,
        fallback_to_long_code: typing.Optional[bool] = OMIT,
        fallback_url: typing.Optional[str] = OMIT,
        friendly_name: typing.Optional[str] = OMIT,
        inbound_method: typing.Optional[UpdateServiceRequestInboundMethod] = OMIT,
        inbound_request_url: typing.Optional[str] = OMIT,
        mms_converter: typing.Optional[bool] = OMIT,
        scan_message_content: typing.Optional[ServiceEnumScanMessageContent] = OMIT,
        smart_encoding: typing.Optional[bool] = OMIT,
        status_callback: typing.Optional[str] = OMIT,
        sticky_sender: typing.Optional[bool] = OMIT,
        synchronous_validation: typing.Optional[bool] = OMIT,
        use_inbound_webhook_on_number: typing.Optional[bool] = OMIT,
        usecase: typing.Optional[str] = OMIT,
        validity_period: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MessagingV1Service:
        """


        Parameters
        ----------
        sid : str
            The SID of the Service resource to update.

        area_code_geomatch : typing.Optional[bool]
            Whether to enable [Area Code Geomatch](https://www.twilio.com/docs/sms/services#area-code-geomatch) on the Service Instance.

        fallback_method : typing.Optional[UpdateServiceRequestFallbackMethod]
            The HTTP method we should use to call `fallback_url`. Can be: `GET` or `POST`.

        fallback_to_long_code : typing.Optional[bool]
            Whether to enable [Fallback to Long Code](https://www.twilio.com/docs/sms/services#fallback-to-long-code) for messages sent through the Service instance.

        fallback_url : typing.Optional[str]
            The URL that we call using `fallback_method` if an error occurs while retrieving or executing the TwiML from the Inbound Request URL. If the `use_inbound_webhook_on_number` field is enabled then the webhook url defined on the phone number will override the `fallback_url` defined for the Messaging Service.

        friendly_name : typing.Optional[str]
            A descriptive string that you create to describe the resource. It can be up to 64 characters long.

        inbound_method : typing.Optional[UpdateServiceRequestInboundMethod]
            The HTTP method we should use to call `inbound_request_url`. Can be `GET` or `POST` and the default is `POST`.

        inbound_request_url : typing.Optional[str]
            The URL we call using `inbound_method` when a message is received by any phone number or short code in the Service. When this property is `null`, receiving inbound messages is disabled. All messages sent to the Twilio phone number or short code will not be logged and received on the Account. If the `use_inbound_webhook_on_number` field is enabled then the webhook url defined on the phone number will override the `inbound_request_url` defined for the Messaging Service.

        mms_converter : typing.Optional[bool]
            Whether to enable the [MMS Converter](https://www.twilio.com/docs/sms/services#mms-converter) for messages sent through the Service instance.

        scan_message_content : typing.Optional[ServiceEnumScanMessageContent]
            Reserved.

        smart_encoding : typing.Optional[bool]
            Whether to enable [Smart Encoding](https://www.twilio.com/docs/sms/services#smart-encoding) for messages sent through the Service instance.

        status_callback : typing.Optional[str]
            The URL we should call to [pass status updates](https://www.twilio.com/docs/sms/api/message-resource#message-status-values) about message delivery.

        sticky_sender : typing.Optional[bool]
            Whether to enable [Sticky Sender](https://www.twilio.com/docs/sms/services#sticky-sender) on the Service instance.

        synchronous_validation : typing.Optional[bool]
            Reserved.

        use_inbound_webhook_on_number : typing.Optional[bool]
            A boolean value that indicates either the webhook url configured on the phone number will be used or `inbound_request_url`/`fallback_url` url will be called when a message is received from the phone number. If this field is enabled then the webhook url defined on the phone number will override the `inbound_request_url`/`fallback_url` defined for the Messaging Service.

        usecase : typing.Optional[str]
            A string that describes the scenario in which the Messaging Service will be used. Examples: [notification, marketing, verification, poll ..]

        validity_period : typing.Optional[int]
            How long, in seconds, messages sent from the Service are valid. Can be an integer from `1` to `14,400`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagingV1Service
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
            await client.update_service(
                sid="Sid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_service(
            sid,
            area_code_geomatch=area_code_geomatch,
            fallback_method=fallback_method,
            fallback_to_long_code=fallback_to_long_code,
            fallback_url=fallback_url,
            friendly_name=friendly_name,
            inbound_method=inbound_method,
            inbound_request_url=inbound_request_url,
            mms_converter=mms_converter,
            scan_message_content=scan_message_content,
            smart_encoding=smart_encoding,
            status_callback=status_callback,
            sticky_sender=sticky_sender,
            synchronous_validation=synchronous_validation,
            use_inbound_webhook_on_number=use_inbound_webhook_on_number,
            usecase=usecase,
            validity_period=validity_period,
            request_options=request_options,
        )
        return _response.data

    async def delete_service(self, sid: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        sid : str
            The SID of the Service resource to delete.

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
            await client.delete_service(
                sid="Sid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_service(sid, request_options=request_options)
        return _response.data

    async def list_tollfree_verification(
        self,
        *,
        tollfree_phone_number_sid: typing.Optional[str] = None,
        status: typing.Optional[TollfreeVerificationEnumStatus] = None,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListTollfreeVerificationResponse:
        """


        Parameters
        ----------
        tollfree_phone_number_sid : typing.Optional[str]
            The SID of the Phone Number associated with the Tollfree Verification.

        status : typing.Optional[TollfreeVerificationEnumStatus]
            The compliance status of the Tollfree Verification record.

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
        ListTollfreeVerificationResponse
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
            await client.list_tollfree_verification()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_tollfree_verification(
            tollfree_phone_number_sid=tollfree_phone_number_sid,
            status=status,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        )
        return _response.data

    async def create_tollfree_verification(
        self,
        *,
        business_name: str,
        business_website: str,
        message_volume: str,
        notification_email: str,
        opt_in_image_urls: typing.Sequence[str],
        opt_in_type: TollfreeVerificationEnumOptInType,
        production_message_sample: str,
        tollfree_phone_number_sid: str,
        use_case_categories: typing.Sequence[str],
        use_case_summary: str,
        additional_information: typing.Optional[str] = OMIT,
        business_city: typing.Optional[str] = OMIT,
        business_contact_email: typing.Optional[str] = OMIT,
        business_contact_first_name: typing.Optional[str] = OMIT,
        business_contact_last_name: typing.Optional[str] = OMIT,
        business_contact_phone: typing.Optional[str] = OMIT,
        business_country: typing.Optional[str] = OMIT,
        business_postal_code: typing.Optional[str] = OMIT,
        business_state_province_region: typing.Optional[str] = OMIT,
        business_street_address: typing.Optional[str] = OMIT,
        business_street_address2: typing.Optional[str] = OMIT,
        customer_profile_sid: typing.Optional[str] = OMIT,
        external_reference_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MessagingV1TollfreeVerification:
        """


        Parameters
        ----------
        business_name : str
            The name of the business or organization using the Tollfree number.

        business_website : str
            The website of the business or organization using the Tollfree number.

        message_volume : str
            Estimate monthly volume of messages from the Tollfree Number.

        notification_email : str
            The email address to receive the notification about the verification result. .

        opt_in_image_urls : typing.Sequence[str]
            Link to an image that shows the opt-in workflow. Multiple images allowed and must be a publicly hosted URL.

        opt_in_type : TollfreeVerificationEnumOptInType
            Describe how a user opts-in to text messages.

        production_message_sample : str
            An example of message content, i.e. a sample message.

        tollfree_phone_number_sid : str
            The SID of the Phone Number associated with the Tollfree Verification.

        use_case_categories : typing.Sequence[str]
            The category of the use case for the Tollfree Number. List as many are applicable..

        use_case_summary : str
            Use this to further explain how messaging is used by the business or organization.

        additional_information : typing.Optional[str]
            Additional information to be provided for verification.

        business_city : typing.Optional[str]
            The city of the business or organization using the Tollfree number.

        business_contact_email : typing.Optional[str]
            The email address of the contact for the business or organization using the Tollfree number.

        business_contact_first_name : typing.Optional[str]
            The first name of the contact for the business or organization using the Tollfree number.

        business_contact_last_name : typing.Optional[str]
            The last name of the contact for the business or organization using the Tollfree number.

        business_contact_phone : typing.Optional[str]
            The phone number of the contact for the business or organization using the Tollfree number.

        business_country : typing.Optional[str]
            The country of the business or organization using the Tollfree number.

        business_postal_code : typing.Optional[str]
            The postal code of the business or organization using the Tollfree number.

        business_state_province_region : typing.Optional[str]
            The state/province/region of the business or organization using the Tollfree number.

        business_street_address : typing.Optional[str]
            The address of the business or organization using the Tollfree number.

        business_street_address2 : typing.Optional[str]
            The address of the business or organization using the Tollfree number.

        customer_profile_sid : typing.Optional[str]
            Customer's Profile Bundle BundleSid.

        external_reference_id : typing.Optional[str]
            An optional external reference ID supplied by customer and echoed back on status retrieval.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagingV1TollfreeVerification
            Created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, TollfreeVerificationEnumOptInType

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.create_tollfree_verification(
                business_name="BusinessName",
                business_website="BusinessWebsite",
                message_volume="MessageVolume",
                notification_email="NotificationEmail",
                opt_in_image_urls=["OptInImageUrls"],
                opt_in_type=TollfreeVerificationEnumOptInType.VERBAL,
                production_message_sample="ProductionMessageSample",
                tollfree_phone_number_sid="TollfreePhoneNumberSid",
                use_case_categories=["UseCaseCategories"],
                use_case_summary="UseCaseSummary",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_tollfree_verification(
            business_name=business_name,
            business_website=business_website,
            message_volume=message_volume,
            notification_email=notification_email,
            opt_in_image_urls=opt_in_image_urls,
            opt_in_type=opt_in_type,
            production_message_sample=production_message_sample,
            tollfree_phone_number_sid=tollfree_phone_number_sid,
            use_case_categories=use_case_categories,
            use_case_summary=use_case_summary,
            additional_information=additional_information,
            business_city=business_city,
            business_contact_email=business_contact_email,
            business_contact_first_name=business_contact_first_name,
            business_contact_last_name=business_contact_last_name,
            business_contact_phone=business_contact_phone,
            business_country=business_country,
            business_postal_code=business_postal_code,
            business_state_province_region=business_state_province_region,
            business_street_address=business_street_address,
            business_street_address2=business_street_address2,
            customer_profile_sid=customer_profile_sid,
            external_reference_id=external_reference_id,
            request_options=request_options,
        )
        return _response.data

    async def fetch_tollfree_verification(
        self, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MessagingV1TollfreeVerification:
        """


        Parameters
        ----------
        sid : str
            The unique string to identify Tollfree Verification.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagingV1TollfreeVerification
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
            await client.fetch_tollfree_verification(
                sid="Sid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_tollfree_verification(sid, request_options=request_options)
        return _response.data

    async def update_tollfree_verification(
        self,
        sid: str,
        *,
        additional_information: typing.Optional[str] = OMIT,
        business_city: typing.Optional[str] = OMIT,
        business_contact_email: typing.Optional[str] = OMIT,
        business_contact_first_name: typing.Optional[str] = OMIT,
        business_contact_last_name: typing.Optional[str] = OMIT,
        business_contact_phone: typing.Optional[str] = OMIT,
        business_country: typing.Optional[str] = OMIT,
        business_name: typing.Optional[str] = OMIT,
        business_postal_code: typing.Optional[str] = OMIT,
        business_state_province_region: typing.Optional[str] = OMIT,
        business_street_address: typing.Optional[str] = OMIT,
        business_street_address2: typing.Optional[str] = OMIT,
        business_website: typing.Optional[str] = OMIT,
        message_volume: typing.Optional[str] = OMIT,
        notification_email: typing.Optional[str] = OMIT,
        opt_in_image_urls: typing.Optional[typing.Sequence[str]] = OMIT,
        opt_in_type: typing.Optional[TollfreeVerificationEnumOptInType] = OMIT,
        production_message_sample: typing.Optional[str] = OMIT,
        use_case_categories: typing.Optional[typing.Sequence[str]] = OMIT,
        use_case_summary: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MessagingV1TollfreeVerification:
        """


        Parameters
        ----------
        sid : str
            The unique string to identify Tollfree Verification.

        additional_information : typing.Optional[str]
            Additional information to be provided for verification.

        business_city : typing.Optional[str]
            The city of the business or organization using the Tollfree number.

        business_contact_email : typing.Optional[str]
            The email address of the contact for the business or organization using the Tollfree number.

        business_contact_first_name : typing.Optional[str]
            The first name of the contact for the business or organization using the Tollfree number.

        business_contact_last_name : typing.Optional[str]
            The last name of the contact for the business or organization using the Tollfree number.

        business_contact_phone : typing.Optional[str]
            The phone number of the contact for the business or organization using the Tollfree number.

        business_country : typing.Optional[str]
            The country of the business or organization using the Tollfree number.

        business_name : typing.Optional[str]
            The name of the business or organization using the Tollfree number.

        business_postal_code : typing.Optional[str]
            The postal code of the business or organization using the Tollfree number.

        business_state_province_region : typing.Optional[str]
            The state/province/region of the business or organization using the Tollfree number.

        business_street_address : typing.Optional[str]
            The address of the business or organization using the Tollfree number.

        business_street_address2 : typing.Optional[str]
            The address of the business or organization using the Tollfree number.

        business_website : typing.Optional[str]
            The website of the business or organization using the Tollfree number.

        message_volume : typing.Optional[str]
            Estimate monthly volume of messages from the Tollfree Number.

        notification_email : typing.Optional[str]
            The email address to receive the notification about the verification result. .

        opt_in_image_urls : typing.Optional[typing.Sequence[str]]
            Link to an image that shows the opt-in workflow. Multiple images allowed and must be a publicly hosted URL.

        opt_in_type : typing.Optional[TollfreeVerificationEnumOptInType]
            Describe how a user opts-in to text messages.

        production_message_sample : typing.Optional[str]
            An example of message content, i.e. a sample message.

        use_case_categories : typing.Optional[typing.Sequence[str]]
            The category of the use case for the Tollfree Number. List as many are applicable..

        use_case_summary : typing.Optional[str]
            Use this to further explain how messaging is used by the business or organization.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagingV1TollfreeVerification
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
            await client.update_tollfree_verification(
                sid="Sid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_tollfree_verification(
            sid,
            additional_information=additional_information,
            business_city=business_city,
            business_contact_email=business_contact_email,
            business_contact_first_name=business_contact_first_name,
            business_contact_last_name=business_contact_last_name,
            business_contact_phone=business_contact_phone,
            business_country=business_country,
            business_name=business_name,
            business_postal_code=business_postal_code,
            business_state_province_region=business_state_province_region,
            business_street_address=business_street_address,
            business_street_address2=business_street_address2,
            business_website=business_website,
            message_volume=message_volume,
            notification_email=notification_email,
            opt_in_image_urls=opt_in_image_urls,
            opt_in_type=opt_in_type,
            production_message_sample=production_message_sample,
            use_case_categories=use_case_categories,
            use_case_summary=use_case_summary,
            request_options=request_options,
        )
        return _response.data

    async def list_brand_registrations(
        self,
        *,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListBrandRegistrationsResponse:
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
        ListBrandRegistrationsResponse
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
            await client.list_brand_registrations()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_brand_registrations(
            page_size=page_size, page=page, page_token=page_token, request_options=request_options
        )
        return _response.data

    async def create_brand_registrations(
        self,
        *,
        a2p_profile_bundle_sid: str,
        customer_profile_bundle_sid: str,
        brand_type: typing.Optional[str] = OMIT,
        mock: typing.Optional[bool] = OMIT,
        skip_automatic_sec_vet: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MessagingV1BrandRegistrations:
        """


        Parameters
        ----------
        a2p_profile_bundle_sid : str
            A2P Messaging Profile Bundle Sid.

        customer_profile_bundle_sid : str
            Customer Profile Bundle Sid.

        brand_type : typing.Optional[str]
            Type of brand being created. One of: "STANDARD", "SOLE_PROPRIETOR". SOLE_PROPRIETOR is for low volume, SOLE_PROPRIETOR use cases. STANDARD is for all other use cases.

        mock : typing.Optional[bool]
            A boolean that specifies whether brand should be a mock or not. If true, brand will be registered as a mock brand. Defaults to false if no value is provided.

        skip_automatic_sec_vet : typing.Optional[bool]
            A flag to disable automatic secondary vetting for brands which it would otherwise be done.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagingV1BrandRegistrations
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
            await client.create_brand_registrations(
                a2p_profile_bundle_sid="A2PProfileBundleSid",
                customer_profile_bundle_sid="CustomerProfileBundleSid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_brand_registrations(
            a2p_profile_bundle_sid=a2p_profile_bundle_sid,
            customer_profile_bundle_sid=customer_profile_bundle_sid,
            brand_type=brand_type,
            mock=mock,
            skip_automatic_sec_vet=skip_automatic_sec_vet,
            request_options=request_options,
        )
        return _response.data

    async def create_brand_registration_otp(
        self, brand_registration_sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MessagingV1BrandRegistrationsBrandRegistrationOtp:
        """


        Parameters
        ----------
        brand_registration_sid : str
            Brand Registration Sid of Sole Proprietor Brand.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagingV1BrandRegistrationsBrandRegistrationOtp
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
            await client.create_brand_registration_otp(
                brand_registration_sid="BrandRegistrationSid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_brand_registration_otp(
            brand_registration_sid, request_options=request_options
        )
        return _response.data

    async def list_brand_vetting(
        self,
        brand_sid: str,
        *,
        vetting_provider: typing.Optional[BrandVettingEnumVettingProvider] = None,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListBrandVettingResponse:
        """


        Parameters
        ----------
        brand_sid : str
            The SID of the Brand Registration resource of the vettings to read .

        vetting_provider : typing.Optional[BrandVettingEnumVettingProvider]
            The third-party provider of the vettings to read

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
        ListBrandVettingResponse
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
            await client.list_brand_vetting(
                brand_sid="BrandSid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_brand_vetting(
            brand_sid,
            vetting_provider=vetting_provider,
            page_size=page_size,
            page=page,
            page_token=page_token,
            request_options=request_options,
        )
        return _response.data

    async def create_brand_vetting(
        self,
        brand_sid: str,
        *,
        vetting_provider: BrandVettingEnumVettingProvider,
        vetting_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MessagingV1BrandRegistrationsBrandVetting:
        """


        Parameters
        ----------
        brand_sid : str
            The SID of the Brand Registration resource of the vettings to create .

        vetting_provider : BrandVettingEnumVettingProvider
            The third-party provider of the vettings to create .

        vetting_id : typing.Optional[str]
            The unique ID of the vetting

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagingV1BrandRegistrationsBrandVetting
            Created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, BrandVettingEnumVettingProvider

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.create_brand_vetting(
                brand_sid="BrandSid",
                vetting_provider=BrandVettingEnumVettingProvider.CAMPAIGN_VERIFY,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_brand_vetting(
            brand_sid, vetting_provider=vetting_provider, vetting_id=vetting_id, request_options=request_options
        )
        return _response.data

    async def fetch_brand_vetting(
        self, brand_sid: str, brand_vetting_sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MessagingV1BrandRegistrationsBrandVetting:
        """


        Parameters
        ----------
        brand_sid : str
            The SID of the Brand Registration resource of the vettings to read .

        brand_vetting_sid : str
            The Twilio SID of the third-party vetting record.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagingV1BrandRegistrationsBrandVetting
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
            await client.fetch_brand_vetting(
                brand_sid="BrandSid",
                brand_vetting_sid="BrandVettingSid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_brand_vetting(
            brand_sid, brand_vetting_sid, request_options=request_options
        )
        return _response.data

    async def fetch_brand_registrations(
        self, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MessagingV1BrandRegistrations:
        """


        Parameters
        ----------
        sid : str
            The SID of the Brand Registration resource to fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagingV1BrandRegistrations
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
            await client.fetch_brand_registrations(
                sid="Sid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_brand_registrations(sid, request_options=request_options)
        return _response.data

    async def update_brand_registrations(
        self, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MessagingV1BrandRegistrations:
        """


        Parameters
        ----------
        sid : str
            The SID of the Brand Registration resource to update.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagingV1BrandRegistrations
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
            await client.update_brand_registrations(
                sid="Sid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_brand_registrations(sid, request_options=request_options)
        return _response.data


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")

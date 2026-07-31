

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.http_response import AsyncHttpResponse, HttpResponse
from .core.jsonable_encoder import encode_path_param
from .core.parse_error import ParsingError
from .core.pydantic_utilities import parse_obj_as
from .core.request_options import RequestOptions
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
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def fetch_deactivation(
        self, *, date: typing.Optional[dt.date] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/Deactivations",
            method="GET",
            params={
                "Date": str(date) if date is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def fetch_domain_cert_v4(
        self, domain_sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MessagingV1DomainCertV4]:
        """


        Parameters
        ----------
        domain_sid : str
            Unique string used to identify the domain that this certificate should be associated with.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MessagingV1DomainCertV4]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/LinkShortening/Domains/{encode_path_param(domain_sid)}/Certificate",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MessagingV1DomainCertV4,
                    parse_obj_as(
                        type_=MessagingV1DomainCertV4,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_domain_cert_v4(
        self, domain_sid: str, *, tls_cert: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MessagingV1DomainCertV4]:
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
        HttpResponse[MessagingV1DomainCertV4]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/LinkShortening/Domains/{encode_path_param(domain_sid)}/Certificate",
            method="POST",
            data={
                "TlsCert": tls_cert,
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
                    MessagingV1DomainCertV4,
                    parse_obj_as(
                        type_=MessagingV1DomainCertV4,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_domain_cert_v4(
        self, domain_sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """


        Parameters
        ----------
        domain_sid : str
            Unique string used to identify the domain that this certificate should be associated with.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/LinkShortening/Domains/{encode_path_param(domain_sid)}/Certificate",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def fetch_domain_config(
        self, domain_sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MessagingV1DomainConfig]:
        """


        Parameters
        ----------
        domain_sid : str
            Unique string used to identify the domain that this config should be associated with.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MessagingV1DomainConfig]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/LinkShortening/Domains/{encode_path_param(domain_sid)}/Config",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MessagingV1DomainConfig,
                    parse_obj_as(
                        type_=MessagingV1DomainConfig,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_domain_config(
        self,
        domain_sid: str,
        *,
        callback_url: typing.Optional[str] = OMIT,
        fallback_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[MessagingV1DomainConfig]:
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
        HttpResponse[MessagingV1DomainConfig]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/LinkShortening/Domains/{encode_path_param(domain_sid)}/Config",
            method="POST",
            data={
                "CallbackUrl": callback_url,
                "FallbackUrl": fallback_url,
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
                    MessagingV1DomainConfig,
                    parse_obj_as(
                        type_=MessagingV1DomainConfig,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_linkshortening_messaging_service(
        self, domain_sid: str, messaging_service_sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MessagingV1LinkshorteningMessagingService]:
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
        HttpResponse[MessagingV1LinkshorteningMessagingService]
            Created
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/LinkShortening/Domains/{encode_path_param(domain_sid)}/MessagingServices/{encode_path_param(messaging_service_sid)}",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MessagingV1LinkshorteningMessagingService,
                    parse_obj_as(
                        type_=MessagingV1LinkshorteningMessagingService,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_linkshortening_messaging_service(
        self, domain_sid: str, messaging_service_sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/LinkShortening/Domains/{encode_path_param(domain_sid)}/MessagingServices/{encode_path_param(messaging_service_sid)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def fetch_domain_config_messaging_service(
        self, messaging_service_sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MessagingV1DomainConfigMessagingService]:
        """


        Parameters
        ----------
        messaging_service_sid : str
            Unique string used to identify the Messaging service that this domain should be associated with.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MessagingV1DomainConfigMessagingService]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/LinkShortening/MessagingService/{encode_path_param(messaging_service_sid)}/DomainConfig",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MessagingV1DomainConfigMessagingService,
                    parse_obj_as(
                        type_=MessagingV1DomainConfigMessagingService,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_service(
        self,
        *,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListServiceResponse]:
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
        HttpResponse[ListServiceResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/Services",
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
                    ListServiceResponse,
                    parse_obj_as(
                        type_=ListServiceResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[MessagingV1Service]:
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
        HttpResponse[MessagingV1Service]
            Created
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/Services",
            method="POST",
            data={
                "AreaCodeGeomatch": area_code_geomatch,
                "FallbackMethod": fallback_method,
                "FallbackToLongCode": fallback_to_long_code,
                "FallbackUrl": fallback_url,
                "FriendlyName": friendly_name,
                "InboundMethod": inbound_method,
                "InboundRequestUrl": inbound_request_url,
                "MmsConverter": mms_converter,
                "ScanMessageContent": scan_message_content,
                "SmartEncoding": smart_encoding,
                "StatusCallback": status_callback,
                "StickySender": sticky_sender,
                "SynchronousValidation": synchronous_validation,
                "UseInboundWebhookOnNumber": use_inbound_webhook_on_number,
                "Usecase": usecase,
                "ValidityPeriod": validity_period,
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
                    MessagingV1Service,
                    parse_obj_as(
                        type_=MessagingV1Service,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_external_campaign(
        self, *, campaign_id: str, messaging_service_sid: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MessagingV1ExternalCampaign]:
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
        HttpResponse[MessagingV1ExternalCampaign]
            Created
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/Services/PreregisteredUsa2p",
            method="POST",
            data={
                "CampaignId": campaign_id,
                "MessagingServiceSid": messaging_service_sid,
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
                    MessagingV1ExternalCampaign,
                    parse_obj_as(
                        type_=MessagingV1ExternalCampaign,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def fetch_usecase(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MessagingV1Usecase]:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MessagingV1Usecase]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/Services/Usecases",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MessagingV1Usecase,
                    parse_obj_as(
                        type_=MessagingV1Usecase,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_us_app_to_person(
        self,
        messaging_service_sid: str,
        *,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListUsAppToPersonResponse]:
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
        HttpResponse[ListUsAppToPersonResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/Services/{encode_path_param(messaging_service_sid)}/Compliance/Usa2p",
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
                    ListUsAppToPersonResponse,
                    parse_obj_as(
                        type_=ListUsAppToPersonResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[MessagingV1ServiceUsAppToPerson]:
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
        HttpResponse[MessagingV1ServiceUsAppToPerson]
            Created
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/Services/{encode_path_param(messaging_service_sid)}/Compliance/Usa2p",
            method="POST",
            data={
                "BrandRegistrationSid": brand_registration_sid,
                "Description": description,
                "HasEmbeddedLinks": has_embedded_links,
                "HasEmbeddedPhone": has_embedded_phone,
                "HelpKeywords": help_keywords,
                "HelpMessage": help_message,
                "MessageFlow": message_flow,
                "MessageSamples": message_samples,
                "OptInKeywords": opt_in_keywords,
                "OptInMessage": opt_in_message,
                "OptOutKeywords": opt_out_keywords,
                "OptOutMessage": opt_out_message,
                "UsAppToPersonUsecase": us_app_to_person_usecase,
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
                    MessagingV1ServiceUsAppToPerson,
                    parse_obj_as(
                        type_=MessagingV1ServiceUsAppToPerson,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def fetch_us_app_to_person_usecase(
        self,
        messaging_service_sid: str,
        *,
        brand_registration_sid: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[MessagingV1ServiceUsAppToPersonUsecase]:
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
        HttpResponse[MessagingV1ServiceUsAppToPersonUsecase]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/Services/{encode_path_param(messaging_service_sid)}/Compliance/Usa2p/Usecases",
            method="GET",
            params={
                "BrandRegistrationSid": brand_registration_sid,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MessagingV1ServiceUsAppToPersonUsecase,
                    parse_obj_as(
                        type_=MessagingV1ServiceUsAppToPersonUsecase,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def fetch_us_app_to_person(
        self, messaging_service_sid: str, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MessagingV1ServiceUsAppToPerson]:
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
        HttpResponse[MessagingV1ServiceUsAppToPerson]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/Services/{encode_path_param(messaging_service_sid)}/Compliance/Usa2p/{encode_path_param(sid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MessagingV1ServiceUsAppToPerson,
                    parse_obj_as(
                        type_=MessagingV1ServiceUsAppToPerson,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_us_app_to_person(
        self, messaging_service_sid: str, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/Services/{encode_path_param(messaging_service_sid)}/Compliance/Usa2p/{encode_path_param(sid)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_alpha_sender(
        self,
        service_sid: str,
        *,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListAlphaSenderResponse]:
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
        HttpResponse[ListAlphaSenderResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/Services/{encode_path_param(service_sid)}/AlphaSenders",
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
                    ListAlphaSenderResponse,
                    parse_obj_as(
                        type_=ListAlphaSenderResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_alpha_sender(
        self, service_sid: str, *, alpha_sender: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MessagingV1ServiceAlphaSender]:
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
        HttpResponse[MessagingV1ServiceAlphaSender]
            Created
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/Services/{encode_path_param(service_sid)}/AlphaSenders",
            method="POST",
            data={
                "AlphaSender": alpha_sender,
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
                    MessagingV1ServiceAlphaSender,
                    parse_obj_as(
                        type_=MessagingV1ServiceAlphaSender,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def fetch_alpha_sender(
        self, service_sid: str, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MessagingV1ServiceAlphaSender]:
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
        HttpResponse[MessagingV1ServiceAlphaSender]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/Services/{encode_path_param(service_sid)}/AlphaSenders/{encode_path_param(sid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MessagingV1ServiceAlphaSender,
                    parse_obj_as(
                        type_=MessagingV1ServiceAlphaSender,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_alpha_sender(
        self, service_sid: str, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/Services/{encode_path_param(service_sid)}/AlphaSenders/{encode_path_param(sid)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_phone_number(
        self,
        service_sid: str,
        *,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListPhoneNumberResponse]:
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
        HttpResponse[ListPhoneNumberResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/Services/{encode_path_param(service_sid)}/PhoneNumbers",
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
                    ListPhoneNumberResponse,
                    parse_obj_as(
                        type_=ListPhoneNumberResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_phone_number(
        self, service_sid: str, *, phone_number_sid: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MessagingV1ServicePhoneNumber]:
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
        HttpResponse[MessagingV1ServicePhoneNumber]
            Created
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/Services/{encode_path_param(service_sid)}/PhoneNumbers",
            method="POST",
            data={
                "PhoneNumberSid": phone_number_sid,
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
                    MessagingV1ServicePhoneNumber,
                    parse_obj_as(
                        type_=MessagingV1ServicePhoneNumber,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def fetch_phone_number(
        self, service_sid: str, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MessagingV1ServicePhoneNumber]:
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
        HttpResponse[MessagingV1ServicePhoneNumber]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/Services/{encode_path_param(service_sid)}/PhoneNumbers/{encode_path_param(sid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MessagingV1ServicePhoneNumber,
                    parse_obj_as(
                        type_=MessagingV1ServicePhoneNumber,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_phone_number(
        self, service_sid: str, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/Services/{encode_path_param(service_sid)}/PhoneNumbers/{encode_path_param(sid)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_short_code(
        self,
        service_sid: str,
        *,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListShortCodeResponse]:
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
        HttpResponse[ListShortCodeResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/Services/{encode_path_param(service_sid)}/ShortCodes",
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
                    ListShortCodeResponse,
                    parse_obj_as(
                        type_=ListShortCodeResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_short_code(
        self, service_sid: str, *, short_code_sid: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MessagingV1ServiceShortCode]:
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
        HttpResponse[MessagingV1ServiceShortCode]
            Created
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/Services/{encode_path_param(service_sid)}/ShortCodes",
            method="POST",
            data={
                "ShortCodeSid": short_code_sid,
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
                    MessagingV1ServiceShortCode,
                    parse_obj_as(
                        type_=MessagingV1ServiceShortCode,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def fetch_short_code(
        self, service_sid: str, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MessagingV1ServiceShortCode]:
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
        HttpResponse[MessagingV1ServiceShortCode]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/Services/{encode_path_param(service_sid)}/ShortCodes/{encode_path_param(sid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MessagingV1ServiceShortCode,
                    parse_obj_as(
                        type_=MessagingV1ServiceShortCode,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_short_code(
        self, service_sid: str, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/Services/{encode_path_param(service_sid)}/ShortCodes/{encode_path_param(sid)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def fetch_service(
        self, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MessagingV1Service]:
        """


        Parameters
        ----------
        sid : str
            The SID of the Service resource to fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MessagingV1Service]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/Services/{encode_path_param(sid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MessagingV1Service,
                    parse_obj_as(
                        type_=MessagingV1Service,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[MessagingV1Service]:
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
        HttpResponse[MessagingV1Service]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/Services/{encode_path_param(sid)}",
            method="POST",
            data={
                "AreaCodeGeomatch": area_code_geomatch,
                "FallbackMethod": fallback_method,
                "FallbackToLongCode": fallback_to_long_code,
                "FallbackUrl": fallback_url,
                "FriendlyName": friendly_name,
                "InboundMethod": inbound_method,
                "InboundRequestUrl": inbound_request_url,
                "MmsConverter": mms_converter,
                "ScanMessageContent": scan_message_content,
                "SmartEncoding": smart_encoding,
                "StatusCallback": status_callback,
                "StickySender": sticky_sender,
                "SynchronousValidation": synchronous_validation,
                "UseInboundWebhookOnNumber": use_inbound_webhook_on_number,
                "Usecase": usecase,
                "ValidityPeriod": validity_period,
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
                    MessagingV1Service,
                    parse_obj_as(
                        type_=MessagingV1Service,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_service(
        self, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """


        Parameters
        ----------
        sid : str
            The SID of the Service resource to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/Services/{encode_path_param(sid)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_tollfree_verification(
        self,
        *,
        tollfree_phone_number_sid: typing.Optional[str] = None,
        status: typing.Optional[TollfreeVerificationEnumStatus] = None,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListTollfreeVerificationResponse]:
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
        HttpResponse[ListTollfreeVerificationResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/Tollfree/Verifications",
            method="GET",
            params={
                "TollfreePhoneNumberSid": tollfree_phone_number_sid,
                "Status": status,
                "PageSize": page_size,
                "Page": page,
                "PageToken": page_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListTollfreeVerificationResponse,
                    parse_obj_as(
                        type_=ListTollfreeVerificationResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[MessagingV1TollfreeVerification]:
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
        HttpResponse[MessagingV1TollfreeVerification]
            Created
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/Tollfree/Verifications",
            method="POST",
            data={
                "AdditionalInformation": additional_information,
                "BusinessCity": business_city,
                "BusinessContactEmail": business_contact_email,
                "BusinessContactFirstName": business_contact_first_name,
                "BusinessContactLastName": business_contact_last_name,
                "BusinessContactPhone": business_contact_phone,
                "BusinessCountry": business_country,
                "BusinessName": business_name,
                "BusinessPostalCode": business_postal_code,
                "BusinessStateProvinceRegion": business_state_province_region,
                "BusinessStreetAddress": business_street_address,
                "BusinessStreetAddress2": business_street_address2,
                "BusinessWebsite": business_website,
                "CustomerProfileSid": customer_profile_sid,
                "ExternalReferenceId": external_reference_id,
                "MessageVolume": message_volume,
                "NotificationEmail": notification_email,
                "OptInImageUrls": opt_in_image_urls,
                "OptInType": opt_in_type,
                "ProductionMessageSample": production_message_sample,
                "TollfreePhoneNumberSid": tollfree_phone_number_sid,
                "UseCaseCategories": use_case_categories,
                "UseCaseSummary": use_case_summary,
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
                    MessagingV1TollfreeVerification,
                    parse_obj_as(
                        type_=MessagingV1TollfreeVerification,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def fetch_tollfree_verification(
        self, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MessagingV1TollfreeVerification]:
        """


        Parameters
        ----------
        sid : str
            The unique string to identify Tollfree Verification.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MessagingV1TollfreeVerification]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/Tollfree/Verifications/{encode_path_param(sid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MessagingV1TollfreeVerification,
                    parse_obj_as(
                        type_=MessagingV1TollfreeVerification,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[MessagingV1TollfreeVerification]:
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
        HttpResponse[MessagingV1TollfreeVerification]
            Accepted
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/Tollfree/Verifications/{encode_path_param(sid)}",
            method="POST",
            data={
                "AdditionalInformation": additional_information,
                "BusinessCity": business_city,
                "BusinessContactEmail": business_contact_email,
                "BusinessContactFirstName": business_contact_first_name,
                "BusinessContactLastName": business_contact_last_name,
                "BusinessContactPhone": business_contact_phone,
                "BusinessCountry": business_country,
                "BusinessName": business_name,
                "BusinessPostalCode": business_postal_code,
                "BusinessStateProvinceRegion": business_state_province_region,
                "BusinessStreetAddress": business_street_address,
                "BusinessStreetAddress2": business_street_address2,
                "BusinessWebsite": business_website,
                "MessageVolume": message_volume,
                "NotificationEmail": notification_email,
                "OptInImageUrls": opt_in_image_urls,
                "OptInType": opt_in_type,
                "ProductionMessageSample": production_message_sample,
                "UseCaseCategories": use_case_categories,
                "UseCaseSummary": use_case_summary,
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
                    MessagingV1TollfreeVerification,
                    parse_obj_as(
                        type_=MessagingV1TollfreeVerification,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_brand_registrations(
        self,
        *,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListBrandRegistrationsResponse]:
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
        HttpResponse[ListBrandRegistrationsResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/a2p/BrandRegistrations",
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
                    ListBrandRegistrationsResponse,
                    parse_obj_as(
                        type_=ListBrandRegistrationsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_brand_registrations(
        self,
        *,
        a2p_profile_bundle_sid: str,
        customer_profile_bundle_sid: str,
        brand_type: typing.Optional[str] = OMIT,
        mock: typing.Optional[bool] = OMIT,
        skip_automatic_sec_vet: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[MessagingV1BrandRegistrations]:
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
        HttpResponse[MessagingV1BrandRegistrations]
            Created
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/a2p/BrandRegistrations",
            method="POST",
            data={
                "A2PProfileBundleSid": a2p_profile_bundle_sid,
                "BrandType": brand_type,
                "CustomerProfileBundleSid": customer_profile_bundle_sid,
                "Mock": mock,
                "SkipAutomaticSecVet": skip_automatic_sec_vet,
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
                    MessagingV1BrandRegistrations,
                    parse_obj_as(
                        type_=MessagingV1BrandRegistrations,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_brand_registration_otp(
        self, brand_registration_sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MessagingV1BrandRegistrationsBrandRegistrationOtp]:
        """


        Parameters
        ----------
        brand_registration_sid : str
            Brand Registration Sid of Sole Proprietor Brand.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MessagingV1BrandRegistrationsBrandRegistrationOtp]
            Created
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/a2p/BrandRegistrations/{encode_path_param(brand_registration_sid)}/SmsOtp",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MessagingV1BrandRegistrationsBrandRegistrationOtp,
                    parse_obj_as(
                        type_=MessagingV1BrandRegistrationsBrandRegistrationOtp,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_brand_vetting(
        self,
        brand_sid: str,
        *,
        vetting_provider: typing.Optional[BrandVettingEnumVettingProvider] = None,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListBrandVettingResponse]:
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
        HttpResponse[ListBrandVettingResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/a2p/BrandRegistrations/{encode_path_param(brand_sid)}/Vettings",
            method="GET",
            params={
                "VettingProvider": vetting_provider,
                "PageSize": page_size,
                "Page": page,
                "PageToken": page_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListBrandVettingResponse,
                    parse_obj_as(
                        type_=ListBrandVettingResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_brand_vetting(
        self,
        brand_sid: str,
        *,
        vetting_provider: BrandVettingEnumVettingProvider,
        vetting_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[MessagingV1BrandRegistrationsBrandVetting]:
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
        HttpResponse[MessagingV1BrandRegistrationsBrandVetting]
            Created
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/a2p/BrandRegistrations/{encode_path_param(brand_sid)}/Vettings",
            method="POST",
            data={
                "VettingId": vetting_id,
                "VettingProvider": vetting_provider,
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
                    MessagingV1BrandRegistrationsBrandVetting,
                    parse_obj_as(
                        type_=MessagingV1BrandRegistrationsBrandVetting,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def fetch_brand_vetting(
        self, brand_sid: str, brand_vetting_sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MessagingV1BrandRegistrationsBrandVetting]:
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
        HttpResponse[MessagingV1BrandRegistrationsBrandVetting]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/a2p/BrandRegistrations/{encode_path_param(brand_sid)}/Vettings/{encode_path_param(brand_vetting_sid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MessagingV1BrandRegistrationsBrandVetting,
                    parse_obj_as(
                        type_=MessagingV1BrandRegistrationsBrandVetting,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def fetch_brand_registrations(
        self, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MessagingV1BrandRegistrations]:
        """


        Parameters
        ----------
        sid : str
            The SID of the Brand Registration resource to fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MessagingV1BrandRegistrations]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/a2p/BrandRegistrations/{encode_path_param(sid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MessagingV1BrandRegistrations,
                    parse_obj_as(
                        type_=MessagingV1BrandRegistrations,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_brand_registrations(
        self, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MessagingV1BrandRegistrations]:
        """


        Parameters
        ----------
        sid : str
            The SID of the Brand Registration resource to update.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MessagingV1BrandRegistrations]
            Accepted
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/a2p/BrandRegistrations/{encode_path_param(sid)}",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MessagingV1BrandRegistrations,
                    parse_obj_as(
                        type_=MessagingV1BrandRegistrations,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawFernApi:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def fetch_deactivation(
        self, *, date: typing.Optional[dt.date] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/Deactivations",
            method="GET",
            params={
                "Date": str(date) if date is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def fetch_domain_cert_v4(
        self, domain_sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MessagingV1DomainCertV4]:
        """


        Parameters
        ----------
        domain_sid : str
            Unique string used to identify the domain that this certificate should be associated with.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MessagingV1DomainCertV4]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/LinkShortening/Domains/{encode_path_param(domain_sid)}/Certificate",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MessagingV1DomainCertV4,
                    parse_obj_as(
                        type_=MessagingV1DomainCertV4,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_domain_cert_v4(
        self, domain_sid: str, *, tls_cert: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MessagingV1DomainCertV4]:
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
        AsyncHttpResponse[MessagingV1DomainCertV4]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/LinkShortening/Domains/{encode_path_param(domain_sid)}/Certificate",
            method="POST",
            data={
                "TlsCert": tls_cert,
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
                    MessagingV1DomainCertV4,
                    parse_obj_as(
                        type_=MessagingV1DomainCertV4,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_domain_cert_v4(
        self, domain_sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """


        Parameters
        ----------
        domain_sid : str
            Unique string used to identify the domain that this certificate should be associated with.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/LinkShortening/Domains/{encode_path_param(domain_sid)}/Certificate",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def fetch_domain_config(
        self, domain_sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MessagingV1DomainConfig]:
        """


        Parameters
        ----------
        domain_sid : str
            Unique string used to identify the domain that this config should be associated with.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MessagingV1DomainConfig]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/LinkShortening/Domains/{encode_path_param(domain_sid)}/Config",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MessagingV1DomainConfig,
                    parse_obj_as(
                        type_=MessagingV1DomainConfig,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_domain_config(
        self,
        domain_sid: str,
        *,
        callback_url: typing.Optional[str] = OMIT,
        fallback_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[MessagingV1DomainConfig]:
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
        AsyncHttpResponse[MessagingV1DomainConfig]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/LinkShortening/Domains/{encode_path_param(domain_sid)}/Config",
            method="POST",
            data={
                "CallbackUrl": callback_url,
                "FallbackUrl": fallback_url,
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
                    MessagingV1DomainConfig,
                    parse_obj_as(
                        type_=MessagingV1DomainConfig,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_linkshortening_messaging_service(
        self, domain_sid: str, messaging_service_sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MessagingV1LinkshorteningMessagingService]:
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
        AsyncHttpResponse[MessagingV1LinkshorteningMessagingService]
            Created
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/LinkShortening/Domains/{encode_path_param(domain_sid)}/MessagingServices/{encode_path_param(messaging_service_sid)}",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MessagingV1LinkshorteningMessagingService,
                    parse_obj_as(
                        type_=MessagingV1LinkshorteningMessagingService,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_linkshortening_messaging_service(
        self, domain_sid: str, messaging_service_sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/LinkShortening/Domains/{encode_path_param(domain_sid)}/MessagingServices/{encode_path_param(messaging_service_sid)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def fetch_domain_config_messaging_service(
        self, messaging_service_sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MessagingV1DomainConfigMessagingService]:
        """


        Parameters
        ----------
        messaging_service_sid : str
            Unique string used to identify the Messaging service that this domain should be associated with.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MessagingV1DomainConfigMessagingService]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/LinkShortening/MessagingService/{encode_path_param(messaging_service_sid)}/DomainConfig",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MessagingV1DomainConfigMessagingService,
                    parse_obj_as(
                        type_=MessagingV1DomainConfigMessagingService,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_service(
        self,
        *,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListServiceResponse]:
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
        AsyncHttpResponse[ListServiceResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/Services",
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
                    ListServiceResponse,
                    parse_obj_as(
                        type_=ListServiceResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[MessagingV1Service]:
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
        AsyncHttpResponse[MessagingV1Service]
            Created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/Services",
            method="POST",
            data={
                "AreaCodeGeomatch": area_code_geomatch,
                "FallbackMethod": fallback_method,
                "FallbackToLongCode": fallback_to_long_code,
                "FallbackUrl": fallback_url,
                "FriendlyName": friendly_name,
                "InboundMethod": inbound_method,
                "InboundRequestUrl": inbound_request_url,
                "MmsConverter": mms_converter,
                "ScanMessageContent": scan_message_content,
                "SmartEncoding": smart_encoding,
                "StatusCallback": status_callback,
                "StickySender": sticky_sender,
                "SynchronousValidation": synchronous_validation,
                "UseInboundWebhookOnNumber": use_inbound_webhook_on_number,
                "Usecase": usecase,
                "ValidityPeriod": validity_period,
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
                    MessagingV1Service,
                    parse_obj_as(
                        type_=MessagingV1Service,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_external_campaign(
        self, *, campaign_id: str, messaging_service_sid: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MessagingV1ExternalCampaign]:
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
        AsyncHttpResponse[MessagingV1ExternalCampaign]
            Created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/Services/PreregisteredUsa2p",
            method="POST",
            data={
                "CampaignId": campaign_id,
                "MessagingServiceSid": messaging_service_sid,
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
                    MessagingV1ExternalCampaign,
                    parse_obj_as(
                        type_=MessagingV1ExternalCampaign,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def fetch_usecase(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MessagingV1Usecase]:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MessagingV1Usecase]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/Services/Usecases",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MessagingV1Usecase,
                    parse_obj_as(
                        type_=MessagingV1Usecase,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_us_app_to_person(
        self,
        messaging_service_sid: str,
        *,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListUsAppToPersonResponse]:
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
        AsyncHttpResponse[ListUsAppToPersonResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/Services/{encode_path_param(messaging_service_sid)}/Compliance/Usa2p",
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
                    ListUsAppToPersonResponse,
                    parse_obj_as(
                        type_=ListUsAppToPersonResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[MessagingV1ServiceUsAppToPerson]:
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
        AsyncHttpResponse[MessagingV1ServiceUsAppToPerson]
            Created
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/Services/{encode_path_param(messaging_service_sid)}/Compliance/Usa2p",
            method="POST",
            data={
                "BrandRegistrationSid": brand_registration_sid,
                "Description": description,
                "HasEmbeddedLinks": has_embedded_links,
                "HasEmbeddedPhone": has_embedded_phone,
                "HelpKeywords": help_keywords,
                "HelpMessage": help_message,
                "MessageFlow": message_flow,
                "MessageSamples": message_samples,
                "OptInKeywords": opt_in_keywords,
                "OptInMessage": opt_in_message,
                "OptOutKeywords": opt_out_keywords,
                "OptOutMessage": opt_out_message,
                "UsAppToPersonUsecase": us_app_to_person_usecase,
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
                    MessagingV1ServiceUsAppToPerson,
                    parse_obj_as(
                        type_=MessagingV1ServiceUsAppToPerson,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def fetch_us_app_to_person_usecase(
        self,
        messaging_service_sid: str,
        *,
        brand_registration_sid: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[MessagingV1ServiceUsAppToPersonUsecase]:
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
        AsyncHttpResponse[MessagingV1ServiceUsAppToPersonUsecase]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/Services/{encode_path_param(messaging_service_sid)}/Compliance/Usa2p/Usecases",
            method="GET",
            params={
                "BrandRegistrationSid": brand_registration_sid,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MessagingV1ServiceUsAppToPersonUsecase,
                    parse_obj_as(
                        type_=MessagingV1ServiceUsAppToPersonUsecase,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def fetch_us_app_to_person(
        self, messaging_service_sid: str, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MessagingV1ServiceUsAppToPerson]:
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
        AsyncHttpResponse[MessagingV1ServiceUsAppToPerson]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/Services/{encode_path_param(messaging_service_sid)}/Compliance/Usa2p/{encode_path_param(sid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MessagingV1ServiceUsAppToPerson,
                    parse_obj_as(
                        type_=MessagingV1ServiceUsAppToPerson,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_us_app_to_person(
        self, messaging_service_sid: str, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/Services/{encode_path_param(messaging_service_sid)}/Compliance/Usa2p/{encode_path_param(sid)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_alpha_sender(
        self,
        service_sid: str,
        *,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListAlphaSenderResponse]:
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
        AsyncHttpResponse[ListAlphaSenderResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/Services/{encode_path_param(service_sid)}/AlphaSenders",
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
                    ListAlphaSenderResponse,
                    parse_obj_as(
                        type_=ListAlphaSenderResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_alpha_sender(
        self, service_sid: str, *, alpha_sender: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MessagingV1ServiceAlphaSender]:
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
        AsyncHttpResponse[MessagingV1ServiceAlphaSender]
            Created
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/Services/{encode_path_param(service_sid)}/AlphaSenders",
            method="POST",
            data={
                "AlphaSender": alpha_sender,
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
                    MessagingV1ServiceAlphaSender,
                    parse_obj_as(
                        type_=MessagingV1ServiceAlphaSender,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def fetch_alpha_sender(
        self, service_sid: str, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MessagingV1ServiceAlphaSender]:
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
        AsyncHttpResponse[MessagingV1ServiceAlphaSender]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/Services/{encode_path_param(service_sid)}/AlphaSenders/{encode_path_param(sid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MessagingV1ServiceAlphaSender,
                    parse_obj_as(
                        type_=MessagingV1ServiceAlphaSender,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_alpha_sender(
        self, service_sid: str, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/Services/{encode_path_param(service_sid)}/AlphaSenders/{encode_path_param(sid)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_phone_number(
        self,
        service_sid: str,
        *,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListPhoneNumberResponse]:
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
        AsyncHttpResponse[ListPhoneNumberResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/Services/{encode_path_param(service_sid)}/PhoneNumbers",
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
                    ListPhoneNumberResponse,
                    parse_obj_as(
                        type_=ListPhoneNumberResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_phone_number(
        self, service_sid: str, *, phone_number_sid: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MessagingV1ServicePhoneNumber]:
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
        AsyncHttpResponse[MessagingV1ServicePhoneNumber]
            Created
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/Services/{encode_path_param(service_sid)}/PhoneNumbers",
            method="POST",
            data={
                "PhoneNumberSid": phone_number_sid,
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
                    MessagingV1ServicePhoneNumber,
                    parse_obj_as(
                        type_=MessagingV1ServicePhoneNumber,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def fetch_phone_number(
        self, service_sid: str, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MessagingV1ServicePhoneNumber]:
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
        AsyncHttpResponse[MessagingV1ServicePhoneNumber]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/Services/{encode_path_param(service_sid)}/PhoneNumbers/{encode_path_param(sid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MessagingV1ServicePhoneNumber,
                    parse_obj_as(
                        type_=MessagingV1ServicePhoneNumber,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_phone_number(
        self, service_sid: str, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/Services/{encode_path_param(service_sid)}/PhoneNumbers/{encode_path_param(sid)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_short_code(
        self,
        service_sid: str,
        *,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListShortCodeResponse]:
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
        AsyncHttpResponse[ListShortCodeResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/Services/{encode_path_param(service_sid)}/ShortCodes",
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
                    ListShortCodeResponse,
                    parse_obj_as(
                        type_=ListShortCodeResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_short_code(
        self, service_sid: str, *, short_code_sid: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MessagingV1ServiceShortCode]:
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
        AsyncHttpResponse[MessagingV1ServiceShortCode]
            Created
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/Services/{encode_path_param(service_sid)}/ShortCodes",
            method="POST",
            data={
                "ShortCodeSid": short_code_sid,
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
                    MessagingV1ServiceShortCode,
                    parse_obj_as(
                        type_=MessagingV1ServiceShortCode,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def fetch_short_code(
        self, service_sid: str, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MessagingV1ServiceShortCode]:
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
        AsyncHttpResponse[MessagingV1ServiceShortCode]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/Services/{encode_path_param(service_sid)}/ShortCodes/{encode_path_param(sid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MessagingV1ServiceShortCode,
                    parse_obj_as(
                        type_=MessagingV1ServiceShortCode,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_short_code(
        self, service_sid: str, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/Services/{encode_path_param(service_sid)}/ShortCodes/{encode_path_param(sid)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def fetch_service(
        self, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MessagingV1Service]:
        """


        Parameters
        ----------
        sid : str
            The SID of the Service resource to fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MessagingV1Service]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/Services/{encode_path_param(sid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MessagingV1Service,
                    parse_obj_as(
                        type_=MessagingV1Service,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[MessagingV1Service]:
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
        AsyncHttpResponse[MessagingV1Service]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/Services/{encode_path_param(sid)}",
            method="POST",
            data={
                "AreaCodeGeomatch": area_code_geomatch,
                "FallbackMethod": fallback_method,
                "FallbackToLongCode": fallback_to_long_code,
                "FallbackUrl": fallback_url,
                "FriendlyName": friendly_name,
                "InboundMethod": inbound_method,
                "InboundRequestUrl": inbound_request_url,
                "MmsConverter": mms_converter,
                "ScanMessageContent": scan_message_content,
                "SmartEncoding": smart_encoding,
                "StatusCallback": status_callback,
                "StickySender": sticky_sender,
                "SynchronousValidation": synchronous_validation,
                "UseInboundWebhookOnNumber": use_inbound_webhook_on_number,
                "Usecase": usecase,
                "ValidityPeriod": validity_period,
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
                    MessagingV1Service,
                    parse_obj_as(
                        type_=MessagingV1Service,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_service(
        self, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """


        Parameters
        ----------
        sid : str
            The SID of the Service resource to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/Services/{encode_path_param(sid)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_tollfree_verification(
        self,
        *,
        tollfree_phone_number_sid: typing.Optional[str] = None,
        status: typing.Optional[TollfreeVerificationEnumStatus] = None,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListTollfreeVerificationResponse]:
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
        AsyncHttpResponse[ListTollfreeVerificationResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/Tollfree/Verifications",
            method="GET",
            params={
                "TollfreePhoneNumberSid": tollfree_phone_number_sid,
                "Status": status,
                "PageSize": page_size,
                "Page": page,
                "PageToken": page_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListTollfreeVerificationResponse,
                    parse_obj_as(
                        type_=ListTollfreeVerificationResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[MessagingV1TollfreeVerification]:
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
        AsyncHttpResponse[MessagingV1TollfreeVerification]
            Created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/Tollfree/Verifications",
            method="POST",
            data={
                "AdditionalInformation": additional_information,
                "BusinessCity": business_city,
                "BusinessContactEmail": business_contact_email,
                "BusinessContactFirstName": business_contact_first_name,
                "BusinessContactLastName": business_contact_last_name,
                "BusinessContactPhone": business_contact_phone,
                "BusinessCountry": business_country,
                "BusinessName": business_name,
                "BusinessPostalCode": business_postal_code,
                "BusinessStateProvinceRegion": business_state_province_region,
                "BusinessStreetAddress": business_street_address,
                "BusinessStreetAddress2": business_street_address2,
                "BusinessWebsite": business_website,
                "CustomerProfileSid": customer_profile_sid,
                "ExternalReferenceId": external_reference_id,
                "MessageVolume": message_volume,
                "NotificationEmail": notification_email,
                "OptInImageUrls": opt_in_image_urls,
                "OptInType": opt_in_type,
                "ProductionMessageSample": production_message_sample,
                "TollfreePhoneNumberSid": tollfree_phone_number_sid,
                "UseCaseCategories": use_case_categories,
                "UseCaseSummary": use_case_summary,
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
                    MessagingV1TollfreeVerification,
                    parse_obj_as(
                        type_=MessagingV1TollfreeVerification,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def fetch_tollfree_verification(
        self, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MessagingV1TollfreeVerification]:
        """


        Parameters
        ----------
        sid : str
            The unique string to identify Tollfree Verification.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MessagingV1TollfreeVerification]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/Tollfree/Verifications/{encode_path_param(sid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MessagingV1TollfreeVerification,
                    parse_obj_as(
                        type_=MessagingV1TollfreeVerification,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[MessagingV1TollfreeVerification]:
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
        AsyncHttpResponse[MessagingV1TollfreeVerification]
            Accepted
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/Tollfree/Verifications/{encode_path_param(sid)}",
            method="POST",
            data={
                "AdditionalInformation": additional_information,
                "BusinessCity": business_city,
                "BusinessContactEmail": business_contact_email,
                "BusinessContactFirstName": business_contact_first_name,
                "BusinessContactLastName": business_contact_last_name,
                "BusinessContactPhone": business_contact_phone,
                "BusinessCountry": business_country,
                "BusinessName": business_name,
                "BusinessPostalCode": business_postal_code,
                "BusinessStateProvinceRegion": business_state_province_region,
                "BusinessStreetAddress": business_street_address,
                "BusinessStreetAddress2": business_street_address2,
                "BusinessWebsite": business_website,
                "MessageVolume": message_volume,
                "NotificationEmail": notification_email,
                "OptInImageUrls": opt_in_image_urls,
                "OptInType": opt_in_type,
                "ProductionMessageSample": production_message_sample,
                "UseCaseCategories": use_case_categories,
                "UseCaseSummary": use_case_summary,
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
                    MessagingV1TollfreeVerification,
                    parse_obj_as(
                        type_=MessagingV1TollfreeVerification,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_brand_registrations(
        self,
        *,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListBrandRegistrationsResponse]:
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
        AsyncHttpResponse[ListBrandRegistrationsResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/a2p/BrandRegistrations",
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
                    ListBrandRegistrationsResponse,
                    parse_obj_as(
                        type_=ListBrandRegistrationsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_brand_registrations(
        self,
        *,
        a2p_profile_bundle_sid: str,
        customer_profile_bundle_sid: str,
        brand_type: typing.Optional[str] = OMIT,
        mock: typing.Optional[bool] = OMIT,
        skip_automatic_sec_vet: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[MessagingV1BrandRegistrations]:
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
        AsyncHttpResponse[MessagingV1BrandRegistrations]
            Created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/a2p/BrandRegistrations",
            method="POST",
            data={
                "A2PProfileBundleSid": a2p_profile_bundle_sid,
                "BrandType": brand_type,
                "CustomerProfileBundleSid": customer_profile_bundle_sid,
                "Mock": mock,
                "SkipAutomaticSecVet": skip_automatic_sec_vet,
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
                    MessagingV1BrandRegistrations,
                    parse_obj_as(
                        type_=MessagingV1BrandRegistrations,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_brand_registration_otp(
        self, brand_registration_sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MessagingV1BrandRegistrationsBrandRegistrationOtp]:
        """


        Parameters
        ----------
        brand_registration_sid : str
            Brand Registration Sid of Sole Proprietor Brand.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MessagingV1BrandRegistrationsBrandRegistrationOtp]
            Created
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/a2p/BrandRegistrations/{encode_path_param(brand_registration_sid)}/SmsOtp",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MessagingV1BrandRegistrationsBrandRegistrationOtp,
                    parse_obj_as(
                        type_=MessagingV1BrandRegistrationsBrandRegistrationOtp,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_brand_vetting(
        self,
        brand_sid: str,
        *,
        vetting_provider: typing.Optional[BrandVettingEnumVettingProvider] = None,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListBrandVettingResponse]:
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
        AsyncHttpResponse[ListBrandVettingResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/a2p/BrandRegistrations/{encode_path_param(brand_sid)}/Vettings",
            method="GET",
            params={
                "VettingProvider": vetting_provider,
                "PageSize": page_size,
                "Page": page,
                "PageToken": page_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListBrandVettingResponse,
                    parse_obj_as(
                        type_=ListBrandVettingResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_brand_vetting(
        self,
        brand_sid: str,
        *,
        vetting_provider: BrandVettingEnumVettingProvider,
        vetting_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[MessagingV1BrandRegistrationsBrandVetting]:
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
        AsyncHttpResponse[MessagingV1BrandRegistrationsBrandVetting]
            Created
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/a2p/BrandRegistrations/{encode_path_param(brand_sid)}/Vettings",
            method="POST",
            data={
                "VettingId": vetting_id,
                "VettingProvider": vetting_provider,
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
                    MessagingV1BrandRegistrationsBrandVetting,
                    parse_obj_as(
                        type_=MessagingV1BrandRegistrationsBrandVetting,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def fetch_brand_vetting(
        self, brand_sid: str, brand_vetting_sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MessagingV1BrandRegistrationsBrandVetting]:
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
        AsyncHttpResponse[MessagingV1BrandRegistrationsBrandVetting]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/a2p/BrandRegistrations/{encode_path_param(brand_sid)}/Vettings/{encode_path_param(brand_vetting_sid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MessagingV1BrandRegistrationsBrandVetting,
                    parse_obj_as(
                        type_=MessagingV1BrandRegistrationsBrandVetting,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def fetch_brand_registrations(
        self, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MessagingV1BrandRegistrations]:
        """


        Parameters
        ----------
        sid : str
            The SID of the Brand Registration resource to fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MessagingV1BrandRegistrations]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/a2p/BrandRegistrations/{encode_path_param(sid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MessagingV1BrandRegistrations,
                    parse_obj_as(
                        type_=MessagingV1BrandRegistrations,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_brand_registrations(
        self, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MessagingV1BrandRegistrations]:
        """


        Parameters
        ----------
        sid : str
            The SID of the Brand Registration resource to update.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MessagingV1BrandRegistrations]
            Accepted
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/a2p/BrandRegistrations/{encode_path_param(sid)}",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MessagingV1BrandRegistrations,
                    parse_obj_as(
                        type_=MessagingV1BrandRegistrations,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

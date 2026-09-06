

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
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_found_error import NotFoundError
from ..errors.payment_required_error import PaymentRequiredError
from ..errors.unauthorized_error import UnauthorizedError
from .types.get_api_domains_response_item import GetApiDomainsResponseItem
from .types.get_domains_domain_id_response import GetDomainsDomainIdResponse
from .types.post_domains_request_link_type import PostDomainsRequestLinkType
from .types.post_domains_response import PostDomainsResponse
from .types.post_domains_settings_domain_id_request_https_level import PostDomainsSettingsDomainIdRequestHttpsLevel
from .types.post_domains_settings_domain_id_request_link_type import PostDomainsSettingsDomainIdRequestLinkType
from .types.post_domains_settings_domain_id_request_robots import PostDomainsSettingsDomainIdRequestRobots
from .types.post_domains_settings_domain_id_request_webhook_url import PostDomainsSettingsDomainIdRequestWebhookUrl
from .types.post_domains_settings_domain_id_response import PostDomainsSettingsDomainIdResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawDomainsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_domains(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        no_team_id: typing.Optional[bool] = None,
        pattern: typing.Optional[str] = None,
        team_id: typing.Optional[float] = None,
        type: typing.Optional[typing.Dict[str, typing.Any]] = None,
        additional_properties: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[GetApiDomainsResponseItem]]:
        """
        Shows all domains of current user

        Parameters
        ----------
        limit : typing.Optional[int]

        offset : typing.Optional[int]

        no_team_id : typing.Optional[bool]

        pattern : typing.Optional[str]

        team_id : typing.Optional[float]

        type : typing.Optional[typing.Dict[str, typing.Any]]

        additional_properties : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[GetApiDomainsResponseItem]]
            Default Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/domains",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "noTeamId": no_team_id,
                "pattern": pattern,
                "teamId": team_id,
            },
            headers={
                "type": str(type) if type is not None else None,
                "additionalProperties": str(additional_properties) if additional_properties is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GetApiDomainsResponseItem],
                    parse_obj_as(
                        type_=typing.List[GetApiDomainsResponseItem],
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

    def get_domain_details_by_id(
        self, domain_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetDomainsDomainIdResponse]:
        """
        Parameters
        ----------
        domain_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetDomainsDomainIdResponse]
            Default Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"domains/{encode_path_param(domain_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetDomainsDomainIdResponse,
                    parse_obj_as(
                        type_=GetDomainsDomainIdResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_domain_settings(
        self,
        domain_id: int,
        *,
        https_level: typing.Optional[PostDomainsSettingsDomainIdRequestHttpsLevel] = OMIT,
        robots: typing.Optional[PostDomainsSettingsDomainIdRequestRobots] = OMIT,
        segment_key: typing.Optional[str] = OMIT,
        link_type: typing.Optional[PostDomainsSettingsDomainIdRequestLinkType] = OMIT,
        cloaking: typing.Optional[bool] = OMIT,
        hide_referer: typing.Optional[bool] = OMIT,
        hide_visitor_ip: typing.Optional[bool] = OMIT,
        https_links: typing.Optional[bool] = OMIT,
        webhook_url: typing.Optional[PostDomainsSettingsDomainIdRequestWebhookUrl] = OMIT,
        integration_ga: typing.Optional[str] = OMIT,
        integration_fb: typing.Optional[str] = OMIT,
        integration_tt: typing.Optional[str] = OMIT,
        integration_adroll: typing.Optional[str] = OMIT,
        enable_conversion_tracking: typing.Optional[bool] = OMIT,
        qr_scan_tracking: typing.Optional[bool] = OMIT,
        integration_gtm: typing.Optional[str] = OMIT,
        client_storage: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        purge_expired_links: typing.Optional[bool] = OMIT,
        enable_ai: typing.Optional[bool] = OMIT,
        case_sensitive: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostDomainsSettingsDomainIdResponse]:
        """
        Update domain settings

        Parameters
        ----------
        domain_id : int

        https_level : typing.Optional[PostDomainsSettingsDomainIdRequestHttpsLevel]

        robots : typing.Optional[PostDomainsSettingsDomainIdRequestRobots]

        segment_key : typing.Optional[str]

        link_type : typing.Optional[PostDomainsSettingsDomainIdRequestLinkType]

        cloaking : typing.Optional[bool]
            Enable cloaking for all links on the domain

        hide_referer : typing.Optional[bool]

        hide_visitor_ip : typing.Optional[bool]
            Don't store visitor IPs in our database

        https_links : typing.Optional[bool]
            Set to null to reissue a certificate

        webhook_url : typing.Optional[PostDomainsSettingsDomainIdRequestWebhookUrl]

        integration_ga : typing.Optional[str]

        integration_fb : typing.Optional[str]

        integration_tt : typing.Optional[str]

        integration_adroll : typing.Optional[str]

        enable_conversion_tracking : typing.Optional[bool]

        qr_scan_tracking : typing.Optional[bool]

        integration_gtm : typing.Optional[str]

        client_storage : typing.Optional[typing.Dict[str, typing.Any]]
            For internal use

        purge_expired_links : typing.Optional[bool]
            [DEPRECATED] do not use

        enable_ai : typing.Optional[bool]

        case_sensitive : typing.Optional[bool]
            Enable case sensitivity for short links

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostDomainsSettingsDomainIdResponse]
            Default Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"domains/settings/{encode_path_param(domain_id)}",
            method="POST",
            json={
                "httpsLevel": https_level,
                "robots": robots,
                "segmentKey": segment_key,
                "linkType": link_type,
                "cloaking": cloaking,
                "hideReferer": hide_referer,
                "hideVisitorIp": hide_visitor_ip,
                "httpsLinks": https_links,
                "webhookURL": convert_and_respect_annotation_metadata(
                    object_=webhook_url,
                    annotation=typing.Optional[PostDomainsSettingsDomainIdRequestWebhookUrl],
                    direction="write",
                ),
                "integrationGA": integration_ga,
                "integrationFB": integration_fb,
                "integrationTT": integration_tt,
                "integrationAdroll": integration_adroll,
                "enableConversionTracking": enable_conversion_tracking,
                "qrScanTracking": qr_scan_tracking,
                "integrationGTM": integration_gtm,
                "clientStorage": client_storage,
                "purgeExpiredLinks": purge_expired_links,
                "enableAI": enable_ai,
                "caseSensitive": case_sensitive,
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
                    PostDomainsSettingsDomainIdResponse,
                    parse_obj_as(
                        type_=PostDomainsSettingsDomainIdResponse,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_a_domain(
        self,
        *,
        hostname: str,
        hide_referer: typing.Optional[bool] = OMIT,
        link_type: typing.Optional[PostDomainsRequestLinkType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostDomainsResponse]:
        """
        Parameters
        ----------
        hostname : str
            Domain hostname

        hide_referer : typing.Optional[bool]

        link_type : typing.Optional[PostDomainsRequestLinkType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostDomainsResponse]
            Default Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "domains",
            method="POST",
            json={
                "hostname": hostname,
                "hideReferer": hide_referer,
                "linkType": link_type,
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
                    PostDomainsResponse,
                    parse_obj_as(
                        type_=PostDomainsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 402:
                raise PaymentRequiredError(
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
            if _response.status_code == 409:
                raise ConflictError(
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


class AsyncRawDomainsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_domains(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        no_team_id: typing.Optional[bool] = None,
        pattern: typing.Optional[str] = None,
        team_id: typing.Optional[float] = None,
        type: typing.Optional[typing.Dict[str, typing.Any]] = None,
        additional_properties: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[GetApiDomainsResponseItem]]:
        """
        Shows all domains of current user

        Parameters
        ----------
        limit : typing.Optional[int]

        offset : typing.Optional[int]

        no_team_id : typing.Optional[bool]

        pattern : typing.Optional[str]

        team_id : typing.Optional[float]

        type : typing.Optional[typing.Dict[str, typing.Any]]

        additional_properties : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[GetApiDomainsResponseItem]]
            Default Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/domains",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "noTeamId": no_team_id,
                "pattern": pattern,
                "teamId": team_id,
            },
            headers={
                "type": str(type) if type is not None else None,
                "additionalProperties": str(additional_properties) if additional_properties is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GetApiDomainsResponseItem],
                    parse_obj_as(
                        type_=typing.List[GetApiDomainsResponseItem],
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

    async def get_domain_details_by_id(
        self, domain_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetDomainsDomainIdResponse]:
        """
        Parameters
        ----------
        domain_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetDomainsDomainIdResponse]
            Default Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"domains/{encode_path_param(domain_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetDomainsDomainIdResponse,
                    parse_obj_as(
                        type_=GetDomainsDomainIdResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_domain_settings(
        self,
        domain_id: int,
        *,
        https_level: typing.Optional[PostDomainsSettingsDomainIdRequestHttpsLevel] = OMIT,
        robots: typing.Optional[PostDomainsSettingsDomainIdRequestRobots] = OMIT,
        segment_key: typing.Optional[str] = OMIT,
        link_type: typing.Optional[PostDomainsSettingsDomainIdRequestLinkType] = OMIT,
        cloaking: typing.Optional[bool] = OMIT,
        hide_referer: typing.Optional[bool] = OMIT,
        hide_visitor_ip: typing.Optional[bool] = OMIT,
        https_links: typing.Optional[bool] = OMIT,
        webhook_url: typing.Optional[PostDomainsSettingsDomainIdRequestWebhookUrl] = OMIT,
        integration_ga: typing.Optional[str] = OMIT,
        integration_fb: typing.Optional[str] = OMIT,
        integration_tt: typing.Optional[str] = OMIT,
        integration_adroll: typing.Optional[str] = OMIT,
        enable_conversion_tracking: typing.Optional[bool] = OMIT,
        qr_scan_tracking: typing.Optional[bool] = OMIT,
        integration_gtm: typing.Optional[str] = OMIT,
        client_storage: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        purge_expired_links: typing.Optional[bool] = OMIT,
        enable_ai: typing.Optional[bool] = OMIT,
        case_sensitive: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostDomainsSettingsDomainIdResponse]:
        """
        Update domain settings

        Parameters
        ----------
        domain_id : int

        https_level : typing.Optional[PostDomainsSettingsDomainIdRequestHttpsLevel]

        robots : typing.Optional[PostDomainsSettingsDomainIdRequestRobots]

        segment_key : typing.Optional[str]

        link_type : typing.Optional[PostDomainsSettingsDomainIdRequestLinkType]

        cloaking : typing.Optional[bool]
            Enable cloaking for all links on the domain

        hide_referer : typing.Optional[bool]

        hide_visitor_ip : typing.Optional[bool]
            Don't store visitor IPs in our database

        https_links : typing.Optional[bool]
            Set to null to reissue a certificate

        webhook_url : typing.Optional[PostDomainsSettingsDomainIdRequestWebhookUrl]

        integration_ga : typing.Optional[str]

        integration_fb : typing.Optional[str]

        integration_tt : typing.Optional[str]

        integration_adroll : typing.Optional[str]

        enable_conversion_tracking : typing.Optional[bool]

        qr_scan_tracking : typing.Optional[bool]

        integration_gtm : typing.Optional[str]

        client_storage : typing.Optional[typing.Dict[str, typing.Any]]
            For internal use

        purge_expired_links : typing.Optional[bool]
            [DEPRECATED] do not use

        enable_ai : typing.Optional[bool]

        case_sensitive : typing.Optional[bool]
            Enable case sensitivity for short links

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostDomainsSettingsDomainIdResponse]
            Default Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"domains/settings/{encode_path_param(domain_id)}",
            method="POST",
            json={
                "httpsLevel": https_level,
                "robots": robots,
                "segmentKey": segment_key,
                "linkType": link_type,
                "cloaking": cloaking,
                "hideReferer": hide_referer,
                "hideVisitorIp": hide_visitor_ip,
                "httpsLinks": https_links,
                "webhookURL": convert_and_respect_annotation_metadata(
                    object_=webhook_url,
                    annotation=typing.Optional[PostDomainsSettingsDomainIdRequestWebhookUrl],
                    direction="write",
                ),
                "integrationGA": integration_ga,
                "integrationFB": integration_fb,
                "integrationTT": integration_tt,
                "integrationAdroll": integration_adroll,
                "enableConversionTracking": enable_conversion_tracking,
                "qrScanTracking": qr_scan_tracking,
                "integrationGTM": integration_gtm,
                "clientStorage": client_storage,
                "purgeExpiredLinks": purge_expired_links,
                "enableAI": enable_ai,
                "caseSensitive": case_sensitive,
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
                    PostDomainsSettingsDomainIdResponse,
                    parse_obj_as(
                        type_=PostDomainsSettingsDomainIdResponse,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_a_domain(
        self,
        *,
        hostname: str,
        hide_referer: typing.Optional[bool] = OMIT,
        link_type: typing.Optional[PostDomainsRequestLinkType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostDomainsResponse]:
        """
        Parameters
        ----------
        hostname : str
            Domain hostname

        hide_referer : typing.Optional[bool]

        link_type : typing.Optional[PostDomainsRequestLinkType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostDomainsResponse]
            Default Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "domains",
            method="POST",
            json={
                "hostname": hostname,
                "hideReferer": hide_referer,
                "linkType": link_type,
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
                    PostDomainsResponse,
                    parse_obj_as(
                        type_=PostDomainsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 402:
                raise PaymentRequiredError(
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
            if _response.status_code == 409:
                raise ConflictError(
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

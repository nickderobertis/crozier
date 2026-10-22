

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.conflict_error import ConflictError
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.service_unavailable_error import ServiceUnavailableError
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.domain import Domain
from ..types.error_response import ErrorResponse
from ..types.paginated_domains_response import PaginatedDomainsResponse
from ..types.success_response import SuccessResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawDomainsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_domains(
        self,
        account_id: str,
        *,
        dns_valid: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        after: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PaginatedDomainsResponse]:
        """
        Returns a list of domains for the account

        Parameters
        ----------
        account_id : str
            Account ID

        dns_valid : typing.Optional[bool]
            Filter results by DNS validation status

        limit : typing.Optional[int]
            Maximum number of items to return (1-100)

        after : typing.Optional[str]
            Pagination cursor for the next page. Provide the value provided in `next_cursor` from the response.

        before : typing.Optional[str]
            Pagination cursor for the previous page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PaginatedDomainsResponse]
            List of domains
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/accounts/{encode_path_param(account_id)}/domains",
            method="GET",
            params={
                "dns_valid": dns_valid,
                "limit": limit,
                "after": after,
                "before": before,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaginatedDomainsResponse,
                    parse_obj_as(
                        type_=PaginatedDomainsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def create_domain(
        self,
        account_id: str,
        *,
        domain: str,
        idempotency_key: typing.Optional[str] = None,
        dkim_private_key: typing.Optional[str] = OMIT,
        tracking_subdomain: typing.Optional[str] = OMIT,
        return_path_subdomain: typing.Optional[str] = OMIT,
        subscription_subdomain: typing.Optional[str] = OMIT,
        media_subdomain: typing.Optional[str] = OMIT,
        dkim_rotation_interval_days: typing.Optional[int] = OMIT,
        dkim_selector: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Domain]:
        """
        Creates a new domain

        Parameters
        ----------
        account_id : str
            Account ID

        domain : str
            Fully qualified domain name

        idempotency_key : typing.Optional[str]
            Optional idempotency key for safe request retries. Must be a unique string for each logical request.
            An identical request with a completed stored outcome returns the original status and body. An in-progress
            execution returns 409, a changed method/path/body returns 422, and a released 5xx execution may run again.
            Keys for non-secret responses expire after 24 hours. API-key create responses include a one-time `secret_key`,
            so successful encrypted replay responses for those operations expire after 5 minutes.

        dkim_private_key : typing.Optional[str]
            DKIM Private Key for the domain. Only RSA keys with a minimum key size of 1024 bits are supported.

            **Note:** This parameter is only supported on [Platform Partner](https://ahasend.com/partners) accounts.

            <Note>Key size of at least 1024 bits is supported; 2048 bit keys are strongly recommended for improved security.</Note>

        tracking_subdomain : typing.Optional[str]
            Optional custom tracking subdomain. Omit to use the default on create. Applies to both manual-DNS and managed-DNS domains.

        return_path_subdomain : typing.Optional[str]
            Optional custom return-path subdomain. Omit to use the default on create. Applies to both manual-DNS and managed-DNS domains.

        subscription_subdomain : typing.Optional[str]
            Optional custom subscription management subdomain. Omit to use the default on create. Applies to both manual-DNS and managed-DNS domains.

        media_subdomain : typing.Optional[str]
            Optional custom media subdomain. Omit to use the default on create. Applies to both manual-DNS and managed-DNS domains.

        dkim_rotation_interval_days : typing.Optional[int]
            Optional custom DKIM rotation interval in days. Only supported for managed DNS domains on eligible plans.

        dkim_selector : typing.Optional[str]
            Optional custom DKIM selector for the domain. Omit, send null, or send an empty or whitespace-only string to use the default selector (no per-domain override); the value is trimmed before it is interpreted, so whitespace-only input is treated as empty.

            When provided, it is normalized to lowercase and must be a single DNS label: 1-62 characters using lowercase letters, numbers, and hyphens only, without a leading or trailing hyphen.

            **Note:** This parameter is only supported on [Platform Partner](https://ahasend.com/partners) accounts.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Domain]
            Domain created successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/accounts/{encode_path_param(account_id)}/domains",
            method="POST",
            json={
                "domain": domain,
                "dkim_private_key": dkim_private_key,
                "tracking_subdomain": tracking_subdomain,
                "return_path_subdomain": return_path_subdomain,
                "subscription_subdomain": subscription_subdomain,
                "media_subdomain": media_subdomain,
                "dkim_rotation_interval_days": dkim_rotation_interval_days,
                "dkim_selector": dkim_selector,
            },
            headers={
                "content-type": "application/json",
                "Idempotency-Key": str(idempotency_key) if idempotency_key is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Domain,
                    parse_obj_as(
                        type_=Domain,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def get_domain(
        self, account_id: str, domain: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Domain]:
        """
        Returns a specific domain by name

        Parameters
        ----------
        account_id : str
            Account ID

        domain : str
            Domain name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Domain]
            Domain details
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/accounts/{encode_path_param(account_id)}/domains/{encode_path_param(domain)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Domain,
                    parse_obj_as(
                        type_=Domain,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def update_domain(
        self,
        account_id: str,
        domain: str,
        *,
        tracking_subdomain: typing.Optional[str] = OMIT,
        return_path_subdomain: typing.Optional[str] = OMIT,
        subscription_subdomain: typing.Optional[str] = OMIT,
        media_subdomain: typing.Optional[str] = OMIT,
        dkim_rotation_interval_days: typing.Optional[int] = OMIT,
        dkim_selector: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Domain]:
        """
        Updates DNS domain settings such as custom subdomains and DKIM rotation interval.

        Parameters
        ----------
        account_id : str
            Account ID

        domain : str
            Domain name

        tracking_subdomain : typing.Optional[str]
            Optional custom tracking subdomain. Omit to leave the current value unchanged. Applies to both manual-DNS and managed-DNS domains.

        return_path_subdomain : typing.Optional[str]
            Optional custom return-path subdomain. Omit to leave the current value unchanged. Applies to both manual-DNS and managed-DNS domains.

        subscription_subdomain : typing.Optional[str]
            Optional custom subscription management subdomain. Omit to leave the current value unchanged. Applies to both manual-DNS and managed-DNS domains.

        media_subdomain : typing.Optional[str]
            Optional custom media subdomain. Omit to leave the current value unchanged. Applies to both manual-DNS and managed-DNS domains.

        dkim_rotation_interval_days : typing.Optional[int]
            Optional custom DKIM rotation interval in days. Omit to leave the current value unchanged. Only supported for managed DNS domains on eligible plans.

        dkim_selector : typing.Optional[str]
            Optional custom DKIM selector for the domain. Omit or send null to leave the current value unchanged; send an empty or whitespace-only string to clear the override and revert to the default selector. The value is trimmed before it is interpreted, so whitespace-only input clears the override just like an empty string.

            When provided, it is normalized to lowercase and must be a single DNS label: 1-62 characters using lowercase letters, numbers, and hyphens only, without a leading or trailing hyphen. It cannot be changed once the selector locks after DNS verification or while a DKIM key rotation is in progress.

            **Note:** This parameter is only supported on [Platform Partner](https://ahasend.com/partners) accounts.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Domain]
            Domain updated successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/accounts/{encode_path_param(account_id)}/domains/{encode_path_param(domain)}",
            method="PUT",
            json={
                "tracking_subdomain": tracking_subdomain,
                "return_path_subdomain": return_path_subdomain,
                "subscription_subdomain": subscription_subdomain,
                "media_subdomain": media_subdomain,
                "dkim_rotation_interval_days": dkim_rotation_interval_days,
                "dkim_selector": dkim_selector,
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
                    Domain,
                    parse_obj_as(
                        type_=Domain,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def delete_domain(
        self, account_id: str, domain: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SuccessResponse]:
        """
        Deletes a domain

        Parameters
        ----------
        account_id : str
            Account ID

        domain : str
            Domain name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SuccessResponse]
            Domain deleted successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/accounts/{encode_path_param(account_id)}/domains/{encode_path_param(domain)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def check_domain_dns(
        self, account_id: str, domain: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Domain]:
        """
        Triggers a DNS validation check for the domain. If the domain was checked within the last 60 seconds, the cached validation result is returned instead of performing a fresh lookup.

        Parameters
        ----------
        account_id : str
            Account ID

        domain : str
            Domain name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Domain]
            Domain DNS status
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/accounts/{encode_path_param(account_id)}/domains/{encode_path_param(domain)}/check-dns",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Domain,
                    parse_obj_as(
                        type_=Domain,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def get_domains(
        self,
        account_id: str,
        *,
        dns_valid: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        after: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PaginatedDomainsResponse]:
        """
        Returns a list of domains for the account

        Parameters
        ----------
        account_id : str
            Account ID

        dns_valid : typing.Optional[bool]
            Filter results by DNS validation status

        limit : typing.Optional[int]
            Maximum number of items to return (1-100)

        after : typing.Optional[str]
            Pagination cursor for the next page. Provide the value provided in `next_cursor` from the response.

        before : typing.Optional[str]
            Pagination cursor for the previous page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PaginatedDomainsResponse]
            List of domains
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/accounts/{encode_path_param(account_id)}/domains",
            method="GET",
            params={
                "dns_valid": dns_valid,
                "limit": limit,
                "after": after,
                "before": before,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaginatedDomainsResponse,
                    parse_obj_as(
                        type_=PaginatedDomainsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def create_domain(
        self,
        account_id: str,
        *,
        domain: str,
        idempotency_key: typing.Optional[str] = None,
        dkim_private_key: typing.Optional[str] = OMIT,
        tracking_subdomain: typing.Optional[str] = OMIT,
        return_path_subdomain: typing.Optional[str] = OMIT,
        subscription_subdomain: typing.Optional[str] = OMIT,
        media_subdomain: typing.Optional[str] = OMIT,
        dkim_rotation_interval_days: typing.Optional[int] = OMIT,
        dkim_selector: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Domain]:
        """
        Creates a new domain

        Parameters
        ----------
        account_id : str
            Account ID

        domain : str
            Fully qualified domain name

        idempotency_key : typing.Optional[str]
            Optional idempotency key for safe request retries. Must be a unique string for each logical request.
            An identical request with a completed stored outcome returns the original status and body. An in-progress
            execution returns 409, a changed method/path/body returns 422, and a released 5xx execution may run again.
            Keys for non-secret responses expire after 24 hours. API-key create responses include a one-time `secret_key`,
            so successful encrypted replay responses for those operations expire after 5 minutes.

        dkim_private_key : typing.Optional[str]
            DKIM Private Key for the domain. Only RSA keys with a minimum key size of 1024 bits are supported.

            **Note:** This parameter is only supported on [Platform Partner](https://ahasend.com/partners) accounts.

            <Note>Key size of at least 1024 bits is supported; 2048 bit keys are strongly recommended for improved security.</Note>

        tracking_subdomain : typing.Optional[str]
            Optional custom tracking subdomain. Omit to use the default on create. Applies to both manual-DNS and managed-DNS domains.

        return_path_subdomain : typing.Optional[str]
            Optional custom return-path subdomain. Omit to use the default on create. Applies to both manual-DNS and managed-DNS domains.

        subscription_subdomain : typing.Optional[str]
            Optional custom subscription management subdomain. Omit to use the default on create. Applies to both manual-DNS and managed-DNS domains.

        media_subdomain : typing.Optional[str]
            Optional custom media subdomain. Omit to use the default on create. Applies to both manual-DNS and managed-DNS domains.

        dkim_rotation_interval_days : typing.Optional[int]
            Optional custom DKIM rotation interval in days. Only supported for managed DNS domains on eligible plans.

        dkim_selector : typing.Optional[str]
            Optional custom DKIM selector for the domain. Omit, send null, or send an empty or whitespace-only string to use the default selector (no per-domain override); the value is trimmed before it is interpreted, so whitespace-only input is treated as empty.

            When provided, it is normalized to lowercase and must be a single DNS label: 1-62 characters using lowercase letters, numbers, and hyphens only, without a leading or trailing hyphen.

            **Note:** This parameter is only supported on [Platform Partner](https://ahasend.com/partners) accounts.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Domain]
            Domain created successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/accounts/{encode_path_param(account_id)}/domains",
            method="POST",
            json={
                "domain": domain,
                "dkim_private_key": dkim_private_key,
                "tracking_subdomain": tracking_subdomain,
                "return_path_subdomain": return_path_subdomain,
                "subscription_subdomain": subscription_subdomain,
                "media_subdomain": media_subdomain,
                "dkim_rotation_interval_days": dkim_rotation_interval_days,
                "dkim_selector": dkim_selector,
            },
            headers={
                "content-type": "application/json",
                "Idempotency-Key": str(idempotency_key) if idempotency_key is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Domain,
                    parse_obj_as(
                        type_=Domain,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def get_domain(
        self, account_id: str, domain: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Domain]:
        """
        Returns a specific domain by name

        Parameters
        ----------
        account_id : str
            Account ID

        domain : str
            Domain name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Domain]
            Domain details
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/accounts/{encode_path_param(account_id)}/domains/{encode_path_param(domain)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Domain,
                    parse_obj_as(
                        type_=Domain,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def update_domain(
        self,
        account_id: str,
        domain: str,
        *,
        tracking_subdomain: typing.Optional[str] = OMIT,
        return_path_subdomain: typing.Optional[str] = OMIT,
        subscription_subdomain: typing.Optional[str] = OMIT,
        media_subdomain: typing.Optional[str] = OMIT,
        dkim_rotation_interval_days: typing.Optional[int] = OMIT,
        dkim_selector: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Domain]:
        """
        Updates DNS domain settings such as custom subdomains and DKIM rotation interval.

        Parameters
        ----------
        account_id : str
            Account ID

        domain : str
            Domain name

        tracking_subdomain : typing.Optional[str]
            Optional custom tracking subdomain. Omit to leave the current value unchanged. Applies to both manual-DNS and managed-DNS domains.

        return_path_subdomain : typing.Optional[str]
            Optional custom return-path subdomain. Omit to leave the current value unchanged. Applies to both manual-DNS and managed-DNS domains.

        subscription_subdomain : typing.Optional[str]
            Optional custom subscription management subdomain. Omit to leave the current value unchanged. Applies to both manual-DNS and managed-DNS domains.

        media_subdomain : typing.Optional[str]
            Optional custom media subdomain. Omit to leave the current value unchanged. Applies to both manual-DNS and managed-DNS domains.

        dkim_rotation_interval_days : typing.Optional[int]
            Optional custom DKIM rotation interval in days. Omit to leave the current value unchanged. Only supported for managed DNS domains on eligible plans.

        dkim_selector : typing.Optional[str]
            Optional custom DKIM selector for the domain. Omit or send null to leave the current value unchanged; send an empty or whitespace-only string to clear the override and revert to the default selector. The value is trimmed before it is interpreted, so whitespace-only input clears the override just like an empty string.

            When provided, it is normalized to lowercase and must be a single DNS label: 1-62 characters using lowercase letters, numbers, and hyphens only, without a leading or trailing hyphen. It cannot be changed once the selector locks after DNS verification or while a DKIM key rotation is in progress.

            **Note:** This parameter is only supported on [Platform Partner](https://ahasend.com/partners) accounts.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Domain]
            Domain updated successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/accounts/{encode_path_param(account_id)}/domains/{encode_path_param(domain)}",
            method="PUT",
            json={
                "tracking_subdomain": tracking_subdomain,
                "return_path_subdomain": return_path_subdomain,
                "subscription_subdomain": subscription_subdomain,
                "media_subdomain": media_subdomain,
                "dkim_rotation_interval_days": dkim_rotation_interval_days,
                "dkim_selector": dkim_selector,
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
                    Domain,
                    parse_obj_as(
                        type_=Domain,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def delete_domain(
        self, account_id: str, domain: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SuccessResponse]:
        """
        Deletes a domain

        Parameters
        ----------
        account_id : str
            Account ID

        domain : str
            Domain name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SuccessResponse]
            Domain deleted successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/accounts/{encode_path_param(account_id)}/domains/{encode_path_param(domain)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def check_domain_dns(
        self, account_id: str, domain: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Domain]:
        """
        Triggers a DNS validation check for the domain. If the domain was checked within the last 60 seconds, the cached validation result is returned instead of performing a fresh lookup.

        Parameters
        ----------
        account_id : str
            Account ID

        domain : str
            Domain name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Domain]
            Domain DNS status
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/accounts/{encode_path_param(account_id)}/domains/{encode_path_param(domain)}/check-dns",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Domain,
                    parse_obj_as(
                        type_=Domain,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

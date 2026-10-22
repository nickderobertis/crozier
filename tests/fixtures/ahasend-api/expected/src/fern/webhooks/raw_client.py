

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
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.created_webhook import CreatedWebhook
from ..types.error_response import ErrorResponse
from ..types.paginated_webhooks_response import PaginatedWebhooksResponse
from ..types.success_response import SuccessResponse
from ..types.webhook import Webhook
from .types.create_webhook_request_scope import CreateWebhookRequestScope
from .types.update_webhook_request_scope import UpdateWebhookRequestScope
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawWebhooksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_webhooks(
        self,
        account_id: str,
        *,
        enabled: typing.Optional[bool] = None,
        on_reception: typing.Optional[bool] = None,
        on_delivered: typing.Optional[bool] = None,
        on_transient_error: typing.Optional[bool] = None,
        on_failed: typing.Optional[bool] = None,
        on_bounced: typing.Optional[bool] = None,
        on_suppressed: typing.Optional[bool] = None,
        on_opened: typing.Optional[bool] = None,
        on_clicked: typing.Optional[bool] = None,
        on_suppression_created: typing.Optional[bool] = None,
        on_dns_error: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        after: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PaginatedWebhooksResponse]:
        """
        Returns a list of webhooks for the account

        The global read role sees all webhooks. Domain-scoped read roles return
        only webhooks associated with at least one authorized domain.

        **Query Parameters:**
        - `enabled`: Filter by enabled status
        - Event filters: `on_reception`, `on_delivered`, `on_transient_error`, `on_failed`, `on_bounced`, `on_suppressed`, `on_opened`, `on_clicked`, `on_suppression_created`, `on_dns_error`
        - `limit`: Maximum number of items to return (1-100, default: 100)
        - `after`: Pagination cursor for the next page
        - `before`: Pagination cursor for the previous page

        Parameters
        ----------
        account_id : str
            Account ID

        enabled : typing.Optional[bool]
            Filter by enabled status

        on_reception : typing.Optional[bool]
            Filter by reception event trigger

        on_delivered : typing.Optional[bool]
            Filter by delivery event trigger

        on_transient_error : typing.Optional[bool]
            Filter by transient error event trigger

        on_failed : typing.Optional[bool]
            Filter by failure event trigger

        on_bounced : typing.Optional[bool]
            Filter by bounce event trigger

        on_suppressed : typing.Optional[bool]
            Filter by suppression event trigger

        on_opened : typing.Optional[bool]
            Filter by open event trigger

        on_clicked : typing.Optional[bool]
            Filter by click event trigger

        on_suppression_created : typing.Optional[bool]
            Filter by suppression creation event trigger

        on_dns_error : typing.Optional[bool]
            Filter by DNS error event trigger

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
        HttpResponse[PaginatedWebhooksResponse]
            List of webhooks
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/accounts/{encode_path_param(account_id)}/webhooks",
            method="GET",
            params={
                "enabled": enabled,
                "on_reception": on_reception,
                "on_delivered": on_delivered,
                "on_transient_error": on_transient_error,
                "on_failed": on_failed,
                "on_bounced": on_bounced,
                "on_suppressed": on_suppressed,
                "on_opened": on_opened,
                "on_clicked": on_clicked,
                "on_suppression_created": on_suppression_created,
                "on_dns_error": on_dns_error,
                "limit": limit,
                "after": after,
                "before": before,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaginatedWebhooksResponse,
                    parse_obj_as(
                        type_=PaginatedWebhooksResponse,
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

    def create_webhook(
        self,
        account_id: str,
        *,
        name: str,
        url: str,
        scope: CreateWebhookRequestScope,
        idempotency_key: typing.Optional[str] = None,
        enabled: typing.Optional[bool] = OMIT,
        on_reception: typing.Optional[bool] = OMIT,
        on_delivered: typing.Optional[bool] = OMIT,
        on_transient_error: typing.Optional[bool] = OMIT,
        on_failed: typing.Optional[bool] = OMIT,
        on_bounced: typing.Optional[bool] = OMIT,
        on_suppressed: typing.Optional[bool] = OMIT,
        on_opened: typing.Optional[bool] = OMIT,
        on_clicked: typing.Optional[bool] = OMIT,
        on_suppression_created: typing.Optional[bool] = OMIT,
        on_dns_error: typing.Optional[bool] = OMIT,
        domains: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreatedWebhook]:
        """
        Creates a new webhook for event notifications. A `scoped` webhook
        requires at least one domain and the key must have write permission for
        every supplied domain. A `global` webhook requires
        `webhooks:write:all`; supplied domains are accepted but ignored, and
        the response contains `domains: []`.

        Parameters
        ----------
        account_id : str
            Account ID

        name : str
            Webhook name

        url : str
            Webhook URL

        scope : CreateWebhookRequestScope
            Webhook scope

        idempotency_key : typing.Optional[str]
            Optional idempotency key for safe request retries. Must be a unique string for each logical request.
            An identical request with a completed stored outcome returns the original status and body. An in-progress
            execution returns 409, a changed method/path/body returns 422, and a released 5xx execution may run again.
            Keys for non-secret responses expire after 24 hours. API-key create responses include a one-time `secret_key`,
            so successful encrypted replay responses for those operations expire after 5 minutes.

        enabled : typing.Optional[bool]
            Whether the webhook is enabled

        on_reception : typing.Optional[bool]
            Trigger on message reception

        on_delivered : typing.Optional[bool]
            Trigger on message delivery

        on_transient_error : typing.Optional[bool]
            Trigger on transient errors

        on_failed : typing.Optional[bool]
            Trigger on permanent failures

        on_bounced : typing.Optional[bool]
            Trigger on bounces

        on_suppressed : typing.Optional[bool]
            Trigger on suppressions

        on_opened : typing.Optional[bool]
            Trigger on opens

        on_clicked : typing.Optional[bool]
            Trigger on clicks

        on_suppression_created : typing.Optional[bool]
            Trigger on suppression creation

        on_dns_error : typing.Optional[bool]
            Trigger on DNS errors

        domains : typing.Optional[typing.Sequence[str]]
            For `scoped`, a non-empty array is required. For `global`, this may
            be omitted, null, empty, or non-empty; supplied values are accepted
            but ignored.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreatedWebhook]
            Webhook created successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/accounts/{encode_path_param(account_id)}/webhooks",
            method="POST",
            json={
                "name": name,
                "url": url,
                "enabled": enabled,
                "on_reception": on_reception,
                "on_delivered": on_delivered,
                "on_transient_error": on_transient_error,
                "on_failed": on_failed,
                "on_bounced": on_bounced,
                "on_suppressed": on_suppressed,
                "on_opened": on_opened,
                "on_clicked": on_clicked,
                "on_suppression_created": on_suppression_created,
                "on_dns_error": on_dns_error,
                "scope": scope,
                "domains": domains,
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
                    CreatedWebhook,
                    parse_obj_as(
                        type_=CreatedWebhook,
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

    def get_webhook(
        self, account_id: str, webhook_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Webhook]:
        """
        Returns a specific webhook by ID. Access requires the global read role
        or a read role matching at least one associated domain.

        Parameters
        ----------
        account_id : str
            Account ID

        webhook_id : str
            Webhook ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Webhook]
            Webhook details
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/accounts/{encode_path_param(account_id)}/webhooks/{encode_path_param(webhook_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Webhook,
                    parse_obj_as(
                        type_=Webhook,
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

    def update_webhook(
        self,
        account_id: str,
        webhook_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        on_reception: typing.Optional[bool] = OMIT,
        on_delivered: typing.Optional[bool] = OMIT,
        on_transient_error: typing.Optional[bool] = OMIT,
        on_failed: typing.Optional[bool] = OMIT,
        on_bounced: typing.Optional[bool] = OMIT,
        on_suppressed: typing.Optional[bool] = OMIT,
        on_opened: typing.Optional[bool] = OMIT,
        on_clicked: typing.Optional[bool] = OMIT,
        on_suppression_created: typing.Optional[bool] = OMIT,
        on_dns_error: typing.Optional[bool] = OMIT,
        scope: typing.Optional[UpdateWebhookRequestScope] = OMIT,
        domains: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Webhook]:
        """
        Updates an existing webhook. Omitted or null fields are unchanged.
        Omitted/null `domains` preserves associations, while `[]` clears the
        associations of a resulting-scoped webhook. Moving from global to
        scoped requires a non-empty `domains` array in the same request. Moving
        to global clears associations and ignores supplied domains.

        A domain-scoped key must be authorized for the existing webhook and
        every newly supplied domain; changing to global requires
        `webhooks:write:all`.

        **Note:** The webhook secret is not updatable

        Parameters
        ----------
        account_id : str
            Account ID

        webhook_id : str
            Webhook ID

        name : typing.Optional[str]
            Webhook name

        url : typing.Optional[str]
            Webhook URL

        enabled : typing.Optional[bool]
            Whether the webhook is enabled

        on_reception : typing.Optional[bool]
            Trigger on message reception

        on_delivered : typing.Optional[bool]
            Trigger on message delivery

        on_transient_error : typing.Optional[bool]
            Trigger on transient errors

        on_failed : typing.Optional[bool]
            Trigger on permanent failures

        on_bounced : typing.Optional[bool]
            Trigger on bounces

        on_suppressed : typing.Optional[bool]
            Trigger on suppressions

        on_opened : typing.Optional[bool]
            Trigger on opens

        on_clicked : typing.Optional[bool]
            Trigger on clicks

        on_suppression_created : typing.Optional[bool]
            Trigger on suppression creation

        on_dns_error : typing.Optional[bool]
            Trigger on DNS errors

        scope : typing.Optional[UpdateWebhookRequestScope]
            Webhook scope. Omit or send null to keep the current scope.

        domains : typing.Optional[typing.Sequence[str]]
            Omit or send null to leave domain associations unchanged. An array
            replaces associations when the resulting scope is `scoped`; `[]`
            explicitly clears them. Changing a global webhook to `scoped`
            requires a non-empty array in the same request and otherwise
            returns HTTP 400. Changing to `global` clears all associations;
            supplied domains are ignored when the resulting scope is global.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Webhook]
            Webhook updated successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/accounts/{encode_path_param(account_id)}/webhooks/{encode_path_param(webhook_id)}",
            method="PUT",
            json={
                "name": name,
                "url": url,
                "enabled": enabled,
                "on_reception": on_reception,
                "on_delivered": on_delivered,
                "on_transient_error": on_transient_error,
                "on_failed": on_failed,
                "on_bounced": on_bounced,
                "on_suppressed": on_suppressed,
                "on_opened": on_opened,
                "on_clicked": on_clicked,
                "on_suppression_created": on_suppression_created,
                "on_dns_error": on_dns_error,
                "scope": scope,
                "domains": domains,
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
                    Webhook,
                    parse_obj_as(
                        type_=Webhook,
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

    def delete_webhook(
        self, account_id: str, webhook_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SuccessResponse]:
        """
        Deletes a webhook. Access requires the global delete role or a delete
        role matching at least one associated domain.

        Parameters
        ----------
        account_id : str
            Account ID

        webhook_id : str
            Webhook ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SuccessResponse]
            Webhook deleted successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/accounts/{encode_path_param(account_id)}/webhooks/{encode_path_param(webhook_id)}",
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


class AsyncRawWebhooksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_webhooks(
        self,
        account_id: str,
        *,
        enabled: typing.Optional[bool] = None,
        on_reception: typing.Optional[bool] = None,
        on_delivered: typing.Optional[bool] = None,
        on_transient_error: typing.Optional[bool] = None,
        on_failed: typing.Optional[bool] = None,
        on_bounced: typing.Optional[bool] = None,
        on_suppressed: typing.Optional[bool] = None,
        on_opened: typing.Optional[bool] = None,
        on_clicked: typing.Optional[bool] = None,
        on_suppression_created: typing.Optional[bool] = None,
        on_dns_error: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        after: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PaginatedWebhooksResponse]:
        """
        Returns a list of webhooks for the account

        The global read role sees all webhooks. Domain-scoped read roles return
        only webhooks associated with at least one authorized domain.

        **Query Parameters:**
        - `enabled`: Filter by enabled status
        - Event filters: `on_reception`, `on_delivered`, `on_transient_error`, `on_failed`, `on_bounced`, `on_suppressed`, `on_opened`, `on_clicked`, `on_suppression_created`, `on_dns_error`
        - `limit`: Maximum number of items to return (1-100, default: 100)
        - `after`: Pagination cursor for the next page
        - `before`: Pagination cursor for the previous page

        Parameters
        ----------
        account_id : str
            Account ID

        enabled : typing.Optional[bool]
            Filter by enabled status

        on_reception : typing.Optional[bool]
            Filter by reception event trigger

        on_delivered : typing.Optional[bool]
            Filter by delivery event trigger

        on_transient_error : typing.Optional[bool]
            Filter by transient error event trigger

        on_failed : typing.Optional[bool]
            Filter by failure event trigger

        on_bounced : typing.Optional[bool]
            Filter by bounce event trigger

        on_suppressed : typing.Optional[bool]
            Filter by suppression event trigger

        on_opened : typing.Optional[bool]
            Filter by open event trigger

        on_clicked : typing.Optional[bool]
            Filter by click event trigger

        on_suppression_created : typing.Optional[bool]
            Filter by suppression creation event trigger

        on_dns_error : typing.Optional[bool]
            Filter by DNS error event trigger

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
        AsyncHttpResponse[PaginatedWebhooksResponse]
            List of webhooks
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/accounts/{encode_path_param(account_id)}/webhooks",
            method="GET",
            params={
                "enabled": enabled,
                "on_reception": on_reception,
                "on_delivered": on_delivered,
                "on_transient_error": on_transient_error,
                "on_failed": on_failed,
                "on_bounced": on_bounced,
                "on_suppressed": on_suppressed,
                "on_opened": on_opened,
                "on_clicked": on_clicked,
                "on_suppression_created": on_suppression_created,
                "on_dns_error": on_dns_error,
                "limit": limit,
                "after": after,
                "before": before,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaginatedWebhooksResponse,
                    parse_obj_as(
                        type_=PaginatedWebhooksResponse,
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

    async def create_webhook(
        self,
        account_id: str,
        *,
        name: str,
        url: str,
        scope: CreateWebhookRequestScope,
        idempotency_key: typing.Optional[str] = None,
        enabled: typing.Optional[bool] = OMIT,
        on_reception: typing.Optional[bool] = OMIT,
        on_delivered: typing.Optional[bool] = OMIT,
        on_transient_error: typing.Optional[bool] = OMIT,
        on_failed: typing.Optional[bool] = OMIT,
        on_bounced: typing.Optional[bool] = OMIT,
        on_suppressed: typing.Optional[bool] = OMIT,
        on_opened: typing.Optional[bool] = OMIT,
        on_clicked: typing.Optional[bool] = OMIT,
        on_suppression_created: typing.Optional[bool] = OMIT,
        on_dns_error: typing.Optional[bool] = OMIT,
        domains: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreatedWebhook]:
        """
        Creates a new webhook for event notifications. A `scoped` webhook
        requires at least one domain and the key must have write permission for
        every supplied domain. A `global` webhook requires
        `webhooks:write:all`; supplied domains are accepted but ignored, and
        the response contains `domains: []`.

        Parameters
        ----------
        account_id : str
            Account ID

        name : str
            Webhook name

        url : str
            Webhook URL

        scope : CreateWebhookRequestScope
            Webhook scope

        idempotency_key : typing.Optional[str]
            Optional idempotency key for safe request retries. Must be a unique string for each logical request.
            An identical request with a completed stored outcome returns the original status and body. An in-progress
            execution returns 409, a changed method/path/body returns 422, and a released 5xx execution may run again.
            Keys for non-secret responses expire after 24 hours. API-key create responses include a one-time `secret_key`,
            so successful encrypted replay responses for those operations expire after 5 minutes.

        enabled : typing.Optional[bool]
            Whether the webhook is enabled

        on_reception : typing.Optional[bool]
            Trigger on message reception

        on_delivered : typing.Optional[bool]
            Trigger on message delivery

        on_transient_error : typing.Optional[bool]
            Trigger on transient errors

        on_failed : typing.Optional[bool]
            Trigger on permanent failures

        on_bounced : typing.Optional[bool]
            Trigger on bounces

        on_suppressed : typing.Optional[bool]
            Trigger on suppressions

        on_opened : typing.Optional[bool]
            Trigger on opens

        on_clicked : typing.Optional[bool]
            Trigger on clicks

        on_suppression_created : typing.Optional[bool]
            Trigger on suppression creation

        on_dns_error : typing.Optional[bool]
            Trigger on DNS errors

        domains : typing.Optional[typing.Sequence[str]]
            For `scoped`, a non-empty array is required. For `global`, this may
            be omitted, null, empty, or non-empty; supplied values are accepted
            but ignored.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreatedWebhook]
            Webhook created successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/accounts/{encode_path_param(account_id)}/webhooks",
            method="POST",
            json={
                "name": name,
                "url": url,
                "enabled": enabled,
                "on_reception": on_reception,
                "on_delivered": on_delivered,
                "on_transient_error": on_transient_error,
                "on_failed": on_failed,
                "on_bounced": on_bounced,
                "on_suppressed": on_suppressed,
                "on_opened": on_opened,
                "on_clicked": on_clicked,
                "on_suppression_created": on_suppression_created,
                "on_dns_error": on_dns_error,
                "scope": scope,
                "domains": domains,
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
                    CreatedWebhook,
                    parse_obj_as(
                        type_=CreatedWebhook,
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

    async def get_webhook(
        self, account_id: str, webhook_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Webhook]:
        """
        Returns a specific webhook by ID. Access requires the global read role
        or a read role matching at least one associated domain.

        Parameters
        ----------
        account_id : str
            Account ID

        webhook_id : str
            Webhook ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Webhook]
            Webhook details
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/accounts/{encode_path_param(account_id)}/webhooks/{encode_path_param(webhook_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Webhook,
                    parse_obj_as(
                        type_=Webhook,
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

    async def update_webhook(
        self,
        account_id: str,
        webhook_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        on_reception: typing.Optional[bool] = OMIT,
        on_delivered: typing.Optional[bool] = OMIT,
        on_transient_error: typing.Optional[bool] = OMIT,
        on_failed: typing.Optional[bool] = OMIT,
        on_bounced: typing.Optional[bool] = OMIT,
        on_suppressed: typing.Optional[bool] = OMIT,
        on_opened: typing.Optional[bool] = OMIT,
        on_clicked: typing.Optional[bool] = OMIT,
        on_suppression_created: typing.Optional[bool] = OMIT,
        on_dns_error: typing.Optional[bool] = OMIT,
        scope: typing.Optional[UpdateWebhookRequestScope] = OMIT,
        domains: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Webhook]:
        """
        Updates an existing webhook. Omitted or null fields are unchanged.
        Omitted/null `domains` preserves associations, while `[]` clears the
        associations of a resulting-scoped webhook. Moving from global to
        scoped requires a non-empty `domains` array in the same request. Moving
        to global clears associations and ignores supplied domains.

        A domain-scoped key must be authorized for the existing webhook and
        every newly supplied domain; changing to global requires
        `webhooks:write:all`.

        **Note:** The webhook secret is not updatable

        Parameters
        ----------
        account_id : str
            Account ID

        webhook_id : str
            Webhook ID

        name : typing.Optional[str]
            Webhook name

        url : typing.Optional[str]
            Webhook URL

        enabled : typing.Optional[bool]
            Whether the webhook is enabled

        on_reception : typing.Optional[bool]
            Trigger on message reception

        on_delivered : typing.Optional[bool]
            Trigger on message delivery

        on_transient_error : typing.Optional[bool]
            Trigger on transient errors

        on_failed : typing.Optional[bool]
            Trigger on permanent failures

        on_bounced : typing.Optional[bool]
            Trigger on bounces

        on_suppressed : typing.Optional[bool]
            Trigger on suppressions

        on_opened : typing.Optional[bool]
            Trigger on opens

        on_clicked : typing.Optional[bool]
            Trigger on clicks

        on_suppression_created : typing.Optional[bool]
            Trigger on suppression creation

        on_dns_error : typing.Optional[bool]
            Trigger on DNS errors

        scope : typing.Optional[UpdateWebhookRequestScope]
            Webhook scope. Omit or send null to keep the current scope.

        domains : typing.Optional[typing.Sequence[str]]
            Omit or send null to leave domain associations unchanged. An array
            replaces associations when the resulting scope is `scoped`; `[]`
            explicitly clears them. Changing a global webhook to `scoped`
            requires a non-empty array in the same request and otherwise
            returns HTTP 400. Changing to `global` clears all associations;
            supplied domains are ignored when the resulting scope is global.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Webhook]
            Webhook updated successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/accounts/{encode_path_param(account_id)}/webhooks/{encode_path_param(webhook_id)}",
            method="PUT",
            json={
                "name": name,
                "url": url,
                "enabled": enabled,
                "on_reception": on_reception,
                "on_delivered": on_delivered,
                "on_transient_error": on_transient_error,
                "on_failed": on_failed,
                "on_bounced": on_bounced,
                "on_suppressed": on_suppressed,
                "on_opened": on_opened,
                "on_clicked": on_clicked,
                "on_suppression_created": on_suppression_created,
                "on_dns_error": on_dns_error,
                "scope": scope,
                "domains": domains,
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
                    Webhook,
                    parse_obj_as(
                        type_=Webhook,
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

    async def delete_webhook(
        self, account_id: str, webhook_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SuccessResponse]:
        """
        Deletes a webhook. Access requires the global delete role or a delete
        role matching at least one associated domain.

        Parameters
        ----------
        account_id : str
            Account ID

        webhook_id : str
            Webhook ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SuccessResponse]
            Webhook deleted successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/accounts/{encode_path_param(account_id)}/webhooks/{encode_path_param(webhook_id)}",
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

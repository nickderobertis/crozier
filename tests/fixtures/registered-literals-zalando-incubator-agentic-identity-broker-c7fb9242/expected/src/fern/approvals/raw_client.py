

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
from ..errors.forbidden_error import ForbiddenError
from ..errors.gone_error import GoneError
from ..errors.not_found_error import NotFoundError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.approval_detail_response import ApprovalDetailResponse
from ..types.approval_error import ApprovalError
from ..types.approval_sync_response import ApprovalSyncResponse
from ..types.approve_response import ApproveResponse
from ..types.consume_response import ConsumeResponse
from ..types.create_approval_response import CreateApprovalResponse
from ..types.deny_response import DenyResponse
from ..types.scope_preview_response import ScopePreviewResponse
from .types.approve_request_persistence import ApproveRequestPersistence
from .types.create_approval_request_metadata import CreateApprovalRequestMetadata
from .types.create_approval_request_risk_level import CreateApprovalRequestRiskLevel
from .types.deny_request_persistence import DenyRequestPersistence
from .types.list_pending_approvals_response import ListPendingApprovalsResponse
from .types.list_permanent_approvals_response import ListPermanentApprovalsResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawApprovalsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def sync_approvals(
        self,
        *,
        principal: typing.Optional[str] = None,
        agent_session_id: typing.Optional[str] = None,
        if_none_match: typing.Optional[str] = None,
        long_poll_timeout: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApprovalSyncResponse]:
        """
        Returns all active approvals grouped by (principal, agent) pair.
        Supports long-poll via If-None-Match + X-Long-Poll-Timeout headers.
        Auth: client assertion only (CEL-validated). No subject token is required because this is a gateway control-plane sync channel rather than a user-facing operation.

        Parameters
        ----------
        principal : typing.Optional[str]

        agent_session_id : typing.Optional[str]
            Repeat for each active agent session. Session-scoped approvals are returned only for matching IDs.

        if_none_match : typing.Optional[str]

        long_poll_timeout : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApprovalSyncResponse]
            Current approval state with ETag
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/approvals",
            method="GET",
            params={
                "principal": principal,
                "agent_session_id": agent_session_id,
            },
            headers={
                "If-None-Match": str(if_none_match) if if_none_match is not None else None,
                "X-Long-Poll-Timeout": str(long_poll_timeout) if long_poll_timeout is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApprovalSyncResponse,
                    parse_obj_as(
                        type_=ApprovalSyncResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_approval(
        self,
        *,
        metadata: CreateApprovalRequestMetadata,
        tool_name: str,
        arguments: typing.Dict[str, typing.Any],
        traceparent: typing.Optional[str] = None,
        risk_level: typing.Optional[CreateApprovalRequestRiskLevel] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateApprovalResponse]:
        """
        Creates a pending approval record for a tool invocation that requires human-in-the-loop authorization.
        Called by ExtProc when a tool call is intercepted that requires approval.
        Dual-auth required: subject token + client assertion. The subject token binds the request to user/agent context, while the client assertion proves the trusted gateway caller that is allowed to mint approval prompts.
        Idempotent: returns existing record for duplicate pending requests.

        Parameters
        ----------
        metadata : CreateApprovalRequestMetadata

        tool_name : str

        arguments : typing.Dict[str, typing.Any]

        traceparent : typing.Optional[str]
            W3C Trace Context propagation header.

        risk_level : typing.Optional[CreateApprovalRequestRiskLevel]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateApprovalResponse]
            Existing pending approval returned (idempotent)
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/approvals",
            method="POST",
            json={
                "metadata": convert_and_respect_annotation_metadata(
                    object_=metadata, annotation=CreateApprovalRequestMetadata, direction="write"
                ),
                "tool_name": tool_name,
                "arguments": arguments,
                "risk_level": risk_level,
            },
            headers={
                "content-type": "application/json",
                "traceparent": str(traceparent) if traceparent is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateApprovalResponse,
                    parse_obj_as(
                        type_=CreateApprovalResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApprovalError,
                        parse_obj_as(
                            type_=ApprovalError,
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

    def list_pending_approvals(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ListPendingApprovalsResponse]:
        """
        Returns all pending approvals for the authenticated user.
        Used by the approval and tool authorization UIs.
        Auth: acting user principal from the browser auth layer (for example `X-Remote-User` in pre-auth deployments).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListPendingApprovalsResponse]
            List of pending approvals
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/approvals/pending",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListPendingApprovalsResponse,
                    parse_obj_as(
                        type_=ListPendingApprovalsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_permanent_approvals(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ListPermanentApprovalsResponse]:
        """
        Returns all permanent approvals and denials for the authenticated user.
        Used by the consent management UI.
        Auth: acting user principal from the browser auth layer (for example `X-Remote-User` in pre-auth deployments).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListPermanentApprovalsResponse]
            List of permanent approvals
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/approvals/permanent",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListPermanentApprovalsResponse,
                    parse_obj_as(
                        type_=ListPermanentApprovalsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_approval(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ApprovalDetailResponse]:
        """
        Retrieves a tool approval record by ID for the Approval UI.
        Auth: acting user principal from the browser auth layer; principal must match.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApprovalDetailResponse]
            Approval record
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/approvals/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApprovalDetailResponse,
                    parse_obj_as(
                        type_=ApprovalDetailResponse,
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
            if _response.status_code == 410:
                raise GoneError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApprovalError,
                        parse_obj_as(
                            type_=ApprovalError,
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

    def approve_approval(
        self,
        id: str,
        *,
        persistence: ApproveRequestPersistence,
        params_pattern: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApproveResponse]:
        """
        Transitions a pending approval to approved state with selected persistence scope.
        Auth: acting user principal from the browser auth layer; principal must match.

        Parameters
        ----------
        id : str

        persistence : ApproveRequestPersistence

        params_pattern : typing.Optional[typing.Dict[str, str]]
            Constrained argument names mapped to globs. Omit the field to cover only the reviewed argument values. This field is permitted only for session or permanent persistence. With once persistence, every supplied value, including an empty object, returns 422 invalid_pattern. The resulting pattern must cover the reviewed arguments.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApproveResponse]
            Approval accepted
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/approvals/{encode_path_param(id)}/approve",
            method="POST",
            json={
                "persistence": persistence,
                "params_pattern": params_pattern,
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
                    ApproveResponse,
                    parse_obj_as(
                        type_=ApproveResponse,
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
            if _response.status_code == 410:
                raise GoneError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApprovalError,
                        parse_obj_as(
                            type_=ApprovalError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApprovalError,
                        parse_obj_as(
                            type_=ApprovalError,
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

    def preview_approval_scope(
        self,
        id: str,
        *,
        params_pattern: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ScopePreviewResponse]:
        """
        Parameters
        ----------
        id : str

        params_pattern : typing.Optional[typing.Dict[str, str]]
            Constrained argument names mapped to globs. Omit the field entirely to cover only the reviewed argument values; send an empty object to leave every argument unconstrained.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ScopePreviewResponse]
            Resolved approval scope
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/approvals/{encode_path_param(id)}/scope-preview",
            method="POST",
            json={
                "params_pattern": params_pattern,
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
                    ScopePreviewResponse,
                    parse_obj_as(
                        type_=ScopePreviewResponse,
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApprovalError,
                        parse_obj_as(
                            type_=ApprovalError,
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

    def deny_approval(
        self,
        id: str,
        *,
        persistence: typing.Optional[DenyRequestPersistence] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DenyResponse]:
        """
        Transitions a pending approval to denied state.
        Auth: acting user principal from the browser auth layer; principal must match.

        Parameters
        ----------
        id : str

        persistence : typing.Optional[DenyRequestPersistence]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DenyResponse]
            Denial recorded
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/approvals/{encode_path_param(id)}/deny",
            method="POST",
            json={
                "persistence": persistence,
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
                    DenyResponse,
                    parse_obj_as(
                        type_=DenyResponse,
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
            if _response.status_code == 410:
                raise GoneError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApprovalError,
                        parse_obj_as(
                            type_=ApprovalError,
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

    def consume_approval(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ConsumeResponse]:
        """
        Marks an approved once-persistence approval as consumed.
        Auth: subject token only (Bearer); principal must match.
        Idempotent: consuming already-consumed returns 200.
        No client assertion is required because this is a per-approval, principal-scoped machine mutation.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ConsumeResponse]
            Approval consumed (or already consumed)
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/approvals/{encode_path_param(id)}/consume",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConsumeResponse,
                    parse_obj_as(
                        type_=ConsumeResponse,
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApprovalError,
                        parse_obj_as(
                            type_=ApprovalError,
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

    def revoke_permanent_approval(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DenyResponse]:
        """
        Revokes a permanent approval or denial.
        Auth: acting user principal from the browser auth layer; principal must match.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DenyResponse]
            Permanent approval revoked
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/approvals/{encode_path_param(id)}/revoke",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DenyResponse,
                    parse_obj_as(
                        type_=DenyResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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


class AsyncRawApprovalsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def sync_approvals(
        self,
        *,
        principal: typing.Optional[str] = None,
        agent_session_id: typing.Optional[str] = None,
        if_none_match: typing.Optional[str] = None,
        long_poll_timeout: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApprovalSyncResponse]:
        """
        Returns all active approvals grouped by (principal, agent) pair.
        Supports long-poll via If-None-Match + X-Long-Poll-Timeout headers.
        Auth: client assertion only (CEL-validated). No subject token is required because this is a gateway control-plane sync channel rather than a user-facing operation.

        Parameters
        ----------
        principal : typing.Optional[str]

        agent_session_id : typing.Optional[str]
            Repeat for each active agent session. Session-scoped approvals are returned only for matching IDs.

        if_none_match : typing.Optional[str]

        long_poll_timeout : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApprovalSyncResponse]
            Current approval state with ETag
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/approvals",
            method="GET",
            params={
                "principal": principal,
                "agent_session_id": agent_session_id,
            },
            headers={
                "If-None-Match": str(if_none_match) if if_none_match is not None else None,
                "X-Long-Poll-Timeout": str(long_poll_timeout) if long_poll_timeout is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApprovalSyncResponse,
                    parse_obj_as(
                        type_=ApprovalSyncResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_approval(
        self,
        *,
        metadata: CreateApprovalRequestMetadata,
        tool_name: str,
        arguments: typing.Dict[str, typing.Any],
        traceparent: typing.Optional[str] = None,
        risk_level: typing.Optional[CreateApprovalRequestRiskLevel] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateApprovalResponse]:
        """
        Creates a pending approval record for a tool invocation that requires human-in-the-loop authorization.
        Called by ExtProc when a tool call is intercepted that requires approval.
        Dual-auth required: subject token + client assertion. The subject token binds the request to user/agent context, while the client assertion proves the trusted gateway caller that is allowed to mint approval prompts.
        Idempotent: returns existing record for duplicate pending requests.

        Parameters
        ----------
        metadata : CreateApprovalRequestMetadata

        tool_name : str

        arguments : typing.Dict[str, typing.Any]

        traceparent : typing.Optional[str]
            W3C Trace Context propagation header.

        risk_level : typing.Optional[CreateApprovalRequestRiskLevel]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateApprovalResponse]
            Existing pending approval returned (idempotent)
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/approvals",
            method="POST",
            json={
                "metadata": convert_and_respect_annotation_metadata(
                    object_=metadata, annotation=CreateApprovalRequestMetadata, direction="write"
                ),
                "tool_name": tool_name,
                "arguments": arguments,
                "risk_level": risk_level,
            },
            headers={
                "content-type": "application/json",
                "traceparent": str(traceparent) if traceparent is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateApprovalResponse,
                    parse_obj_as(
                        type_=CreateApprovalResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApprovalError,
                        parse_obj_as(
                            type_=ApprovalError,
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

    async def list_pending_approvals(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ListPendingApprovalsResponse]:
        """
        Returns all pending approvals for the authenticated user.
        Used by the approval and tool authorization UIs.
        Auth: acting user principal from the browser auth layer (for example `X-Remote-User` in pre-auth deployments).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListPendingApprovalsResponse]
            List of pending approvals
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/approvals/pending",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListPendingApprovalsResponse,
                    parse_obj_as(
                        type_=ListPendingApprovalsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_permanent_approvals(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ListPermanentApprovalsResponse]:
        """
        Returns all permanent approvals and denials for the authenticated user.
        Used by the consent management UI.
        Auth: acting user principal from the browser auth layer (for example `X-Remote-User` in pre-auth deployments).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListPermanentApprovalsResponse]
            List of permanent approvals
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/approvals/permanent",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListPermanentApprovalsResponse,
                    parse_obj_as(
                        type_=ListPermanentApprovalsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_approval(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ApprovalDetailResponse]:
        """
        Retrieves a tool approval record by ID for the Approval UI.
        Auth: acting user principal from the browser auth layer; principal must match.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApprovalDetailResponse]
            Approval record
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/approvals/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApprovalDetailResponse,
                    parse_obj_as(
                        type_=ApprovalDetailResponse,
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
            if _response.status_code == 410:
                raise GoneError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApprovalError,
                        parse_obj_as(
                            type_=ApprovalError,
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

    async def approve_approval(
        self,
        id: str,
        *,
        persistence: ApproveRequestPersistence,
        params_pattern: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApproveResponse]:
        """
        Transitions a pending approval to approved state with selected persistence scope.
        Auth: acting user principal from the browser auth layer; principal must match.

        Parameters
        ----------
        id : str

        persistence : ApproveRequestPersistence

        params_pattern : typing.Optional[typing.Dict[str, str]]
            Constrained argument names mapped to globs. Omit the field to cover only the reviewed argument values. This field is permitted only for session or permanent persistence. With once persistence, every supplied value, including an empty object, returns 422 invalid_pattern. The resulting pattern must cover the reviewed arguments.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApproveResponse]
            Approval accepted
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/approvals/{encode_path_param(id)}/approve",
            method="POST",
            json={
                "persistence": persistence,
                "params_pattern": params_pattern,
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
                    ApproveResponse,
                    parse_obj_as(
                        type_=ApproveResponse,
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
            if _response.status_code == 410:
                raise GoneError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApprovalError,
                        parse_obj_as(
                            type_=ApprovalError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApprovalError,
                        parse_obj_as(
                            type_=ApprovalError,
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

    async def preview_approval_scope(
        self,
        id: str,
        *,
        params_pattern: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ScopePreviewResponse]:
        """
        Parameters
        ----------
        id : str

        params_pattern : typing.Optional[typing.Dict[str, str]]
            Constrained argument names mapped to globs. Omit the field entirely to cover only the reviewed argument values; send an empty object to leave every argument unconstrained.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ScopePreviewResponse]
            Resolved approval scope
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/approvals/{encode_path_param(id)}/scope-preview",
            method="POST",
            json={
                "params_pattern": params_pattern,
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
                    ScopePreviewResponse,
                    parse_obj_as(
                        type_=ScopePreviewResponse,
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApprovalError,
                        parse_obj_as(
                            type_=ApprovalError,
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

    async def deny_approval(
        self,
        id: str,
        *,
        persistence: typing.Optional[DenyRequestPersistence] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DenyResponse]:
        """
        Transitions a pending approval to denied state.
        Auth: acting user principal from the browser auth layer; principal must match.

        Parameters
        ----------
        id : str

        persistence : typing.Optional[DenyRequestPersistence]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DenyResponse]
            Denial recorded
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/approvals/{encode_path_param(id)}/deny",
            method="POST",
            json={
                "persistence": persistence,
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
                    DenyResponse,
                    parse_obj_as(
                        type_=DenyResponse,
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
            if _response.status_code == 410:
                raise GoneError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApprovalError,
                        parse_obj_as(
                            type_=ApprovalError,
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

    async def consume_approval(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ConsumeResponse]:
        """
        Marks an approved once-persistence approval as consumed.
        Auth: subject token only (Bearer); principal must match.
        Idempotent: consuming already-consumed returns 200.
        No client assertion is required because this is a per-approval, principal-scoped machine mutation.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ConsumeResponse]
            Approval consumed (or already consumed)
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/approvals/{encode_path_param(id)}/consume",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConsumeResponse,
                    parse_obj_as(
                        type_=ConsumeResponse,
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApprovalError,
                        parse_obj_as(
                            type_=ApprovalError,
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

    async def revoke_permanent_approval(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DenyResponse]:
        """
        Revokes a permanent approval or denial.
        Auth: acting user principal from the browser auth layer; principal must match.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DenyResponse]
            Permanent approval revoked
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/approvals/{encode_path_param(id)}/revoke",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DenyResponse,
                    parse_obj_as(
                        type_=DenyResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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

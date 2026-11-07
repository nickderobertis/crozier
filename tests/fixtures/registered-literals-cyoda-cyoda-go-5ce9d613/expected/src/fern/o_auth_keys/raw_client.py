

import datetime as dt
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
from ..types.error_response_dto import ErrorResponseDto
from ..types.jwt_key_pair_response_dto import JwtKeyPairResponseDto
from ..types.trusted_key_response_dto import TrustedKeyResponseDto
from .types.get_current_jwt_key_pair_request_audience import GetCurrentJwtKeyPairRequestAudience
from .types.issue_jwt_key_pair_request_dto_algorithm import IssueJwtKeyPairRequestDtoAlgorithm
from .types.issue_jwt_key_pair_request_dto_audience import IssueJwtKeyPairRequestDtoAudience
from .types.register_trusted_key_request_dto_audience import RegisterTrustedKeyRequestDtoAudience
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawOAuthKeysClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def issue_jwt_key_pair(
        self,
        *,
        audience: IssueJwtKeyPairRequestDtoAudience,
        algorithm: IssueJwtKeyPairRequestDtoAlgorithm,
        valid_from: typing.Optional[dt.datetime] = OMIT,
        valid_to: typing.Optional[dt.datetime] = OMIT,
        invalidate_current: typing.Optional[bool] = OMIT,
        invalidate_grace_period_sec: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[JwtKeyPairResponseDto]:
        """
        Generates and stores a new asymmetric key-pair (public/private) for signing and validating OAuth 2.0 JWT
        access tokens.

        Parameters
        ----------
        audience : IssueJwtKeyPairRequestDtoAudience

        algorithm : IssueJwtKeyPairRequestDtoAlgorithm

        valid_from : typing.Optional[dt.datetime]
            When the key-pair becomes valid. Defaults to current date-time if not specified.

        valid_to : typing.Optional[dt.datetime]
            When the key-pair expires. Defaults to validFrom + <configured validity, default is 365 days> if not specified.

        invalidate_current : typing.Optional[bool]
            If true, invalidates the currently active key-pair for this audience.

        invalidate_grace_period_sec : typing.Optional[int]
            Number of seconds to keep the old key valid after invalidation. Only applicable when invalidateCurrent is true.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JwtKeyPairResponseDto]
            JWT key-pair issued successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "oauth/keys/keypair",
            method="POST",
            json={
                "audience": audience,
                "algorithm": algorithm,
                "validFrom": valid_from,
                "validTo": valid_to,
                "invalidateCurrent": invalidate_current,
                "invalidateGracePeriodSec": invalidate_grace_period_sec,
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
                    JwtKeyPairResponseDto,
                    parse_obj_as(
                        type_=JwtKeyPairResponseDto,
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
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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

    def get_current_jwt_key_pair(
        self, *, audience: GetCurrentJwtKeyPairRequestAudience, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[JwtKeyPairResponseDto]:
        """
        Retrieves information about the currently active JWT signing key-pair for the specified audience.

        Parameters
        ----------
        audience : GetCurrentJwtKeyPairRequestAudience

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JwtKeyPairResponseDto]
            Current key-pair information retrieved successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "oauth/keys/keypair/current",
            method="GET",
            params={
                "audience": audience,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JwtKeyPairResponseDto,
                    parse_obj_as(
                        type_=JwtKeyPairResponseDto,
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
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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

    def delete_jwt_key_pair(
        self, key_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Deletes a JWT signing key-pair. The key will first be invalidated (if not already)
        and then removed from storage.

        Parameters
        ----------
        key_id : str
            The unique identifier (kid) of the key-pair to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"oauth/keys/keypair/{encode_path_param(key_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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

    def invalidate_jwt_key_pair(
        self,
        key_id: str,
        *,
        grace_period_sec: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Invalidates a specific JWT signing key-pair.
        After invalidation, the key will no longer be used for signing new tokens,
        and existing tokens signed with this key pair would not be accepted.

        Parameters
        ----------
        key_id : str
            The unique identifier (kid) of the key-pair to invalidate

        grace_period_sec : typing.Optional[int]
            Number of seconds to keep the key valid after invalidation. Default is 0 (immediate invalidation).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"oauth/keys/keypair/{encode_path_param(key_id)}/invalidate",
            method="POST",
            json={
                "gracePeriodSec": grace_period_sec,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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

    def reactivate_jwt_key_pair(
        self, key_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[JwtKeyPairResponseDto]:
        """
        Reactivates a previously invalidated JWT signing key-pair.
        This allows the key to be used for signing and validating tokens again.
        This operation is idempotent - if the key-pair is already active, it returns the current state.

        Parameters
        ----------
        key_id : str
            The unique identifier (kid) of the key-pair to reactivate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JwtKeyPairResponseDto]
            JWT key-pair reactivated successfully or already active
        """
        _response = self._client_wrapper.httpx_client.request(
            f"oauth/keys/keypair/{encode_path_param(key_id)}/reactivate",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JwtKeyPairResponseDto,
                    parse_obj_as(
                        type_=JwtKeyPairResponseDto,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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

    def list_trusted_keys(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[TrustedKeyResponseDto]]:
        """
        Returns all trusted public keys registered for the caller's tenant.
        Requires ADMIN or SUPER_USER role.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[TrustedKeyResponseDto]]
            List of trusted keys
        """
        _response = self._client_wrapper.httpx_client.request(
            "oauth/keys/trusted",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[TrustedKeyResponseDto],
                    parse_obj_as(
                        type_=typing.List[TrustedKeyResponseDto],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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

    def register_trusted_key(
        self,
        *,
        key_id: str,
        jwk: typing.Dict[str, typing.Dict[str, typing.Any]],
        audience: RegisterTrustedKeyRequestDtoAudience,
        issuers: typing.Optional[typing.Sequence[str]] = OMIT,
        valid_from: typing.Optional[dt.datetime] = OMIT,
        valid_to: typing.Optional[dt.datetime] = OMIT,
        invalidate_previous: typing.Optional[bool] = OMIT,
        invalidate_grace_period_sec: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TrustedKeyResponseDto]:
        """
        Registers a pre-shared public key for JWT validation. This enables external applications
        to sign user JWTs that Cyoda can verify without requiring a reachable OIDC discovery endpoint.
        The key is bound to the caller's tenant (legalEntityId).

        If a key with the same `keyId` already exists and belongs to the caller's tenant, it is
        replaced atomically (upsert semantics). This makes the endpoint retry-safe during key
        rotation — a retried request after a partial failure will succeed rather than conflict.
        If the key belongs to a different tenant, the request is rejected with `409 Conflict`.

        Use `invalidatePrevious` to retire all other active trusted keys for this tenant
        in a single atomic operation, with an optional grace period (`invalidateGracePeriodSec`)
        during which the old keys continue to be accepted.

        Requires ADMIN or SUPER_USER role. Disabled by default — enable via
        `cyoda.security.web.iam.trustedKeyRegistrationEnabled`.

        Parameters
        ----------
        key_id : str
            Unique key identifier. Will be matched against the `kid` header in JWTs.

        jwk : typing.Dict[str, typing.Dict[str, typing.Any]]
            A JSON Web Key (JWK) as defined in RFC 7517. Must contain the public key components only. Supported key types: RSA (`kty: "RSA"`), EC (`kty: "EC"`), and OKP/EdDSA (`kty: "OKP"`). See RFC 7517, RFC 7518, and RFC 8037 for field definitions.

        audience : RegisterTrustedKeyRequestDtoAudience

        issuers : typing.Optional[typing.Sequence[str]]
            List of allowed issuer URIs. When this parameter is configured, the JWT must contain an iss claim, and its value must match one of the entries in this list.

        valid_from : typing.Optional[dt.datetime]
            When the key becomes valid. Defaults to current time if not specified.

        valid_to : typing.Optional[dt.datetime]
            When the key expires. Defaults to the system-configured maximum validity.

        invalidate_previous : typing.Optional[bool]
            If true, invalidates all other keys for the same audience belonging to the caller's tenant. Enables atomic key rotation.

        invalidate_grace_period_sec : typing.Optional[int]
            Grace period in seconds for invalidating previous keys (only used when invalidatePrevious is true). Default is 0 (immediate invalidation).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TrustedKeyResponseDto]
            Trusted key registered successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "oauth/keys/trusted",
            method="POST",
            json={
                "keyId": key_id,
                "jwk": jwk,
                "audience": audience,
                "issuers": issuers,
                "validFrom": valid_from,
                "validTo": valid_to,
                "invalidatePrevious": invalidate_previous,
                "invalidateGracePeriodSec": invalidate_grace_period_sec,
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
                    TrustedKeyResponseDto,
                    parse_obj_as(
                        type_=TrustedKeyResponseDto,
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
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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

    def delete_trusted_key(
        self, key_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Deletes a registered trusted public key. The key must belong to the caller's tenant.
        Requires ADMIN or SUPER_USER role.

        Parameters
        ----------
        key_id : str
            The key ID of the trusted key to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"oauth/keys/trusted/{encode_path_param(key_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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

    def invalidate_trusted_key(
        self,
        key_id: str,
        *,
        grace_period_sec: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Invalidates a registered trusted public key. After invalidation, JWTs signed with the
        corresponding private key will no longer be accepted for validation (after the grace period).
        Requires ADMIN or SUPER_USER role.

        Parameters
        ----------
        key_id : str
            The key ID of the trusted key to invalidate

        grace_period_sec : typing.Optional[int]
            Number of seconds to keep the key valid after invalidation. Default is 0 (immediate invalidation).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"oauth/keys/trusted/{encode_path_param(key_id)}/invalidate",
            method="POST",
            json={
                "gracePeriodSec": grace_period_sec,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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

    def reactivate_trusted_key(
        self, key_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[TrustedKeyResponseDto]:
        """
        Reactivates a previously invalidated trusted public key, allowing JWTs signed with it to
        be accepted again. This operation is idempotent.
        Requires ADMIN or SUPER_USER role.

        **Important**: Reactivation removes the key's expiration entirely (`validTo` is cleared to null),
        regardless of the original `validTo` value the key was registered with. The key will remain valid
        indefinitely until explicitly invalidated or deleted again.

        Parameters
        ----------
        key_id : str
            The key ID of the trusted key to reactivate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TrustedKeyResponseDto]
            Trusted key reactivated successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"oauth/keys/trusted/{encode_path_param(key_id)}/reactivate",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TrustedKeyResponseDto,
                    parse_obj_as(
                        type_=TrustedKeyResponseDto,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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


class AsyncRawOAuthKeysClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def issue_jwt_key_pair(
        self,
        *,
        audience: IssueJwtKeyPairRequestDtoAudience,
        algorithm: IssueJwtKeyPairRequestDtoAlgorithm,
        valid_from: typing.Optional[dt.datetime] = OMIT,
        valid_to: typing.Optional[dt.datetime] = OMIT,
        invalidate_current: typing.Optional[bool] = OMIT,
        invalidate_grace_period_sec: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[JwtKeyPairResponseDto]:
        """
        Generates and stores a new asymmetric key-pair (public/private) for signing and validating OAuth 2.0 JWT
        access tokens.

        Parameters
        ----------
        audience : IssueJwtKeyPairRequestDtoAudience

        algorithm : IssueJwtKeyPairRequestDtoAlgorithm

        valid_from : typing.Optional[dt.datetime]
            When the key-pair becomes valid. Defaults to current date-time if not specified.

        valid_to : typing.Optional[dt.datetime]
            When the key-pair expires. Defaults to validFrom + <configured validity, default is 365 days> if not specified.

        invalidate_current : typing.Optional[bool]
            If true, invalidates the currently active key-pair for this audience.

        invalidate_grace_period_sec : typing.Optional[int]
            Number of seconds to keep the old key valid after invalidation. Only applicable when invalidateCurrent is true.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JwtKeyPairResponseDto]
            JWT key-pair issued successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "oauth/keys/keypair",
            method="POST",
            json={
                "audience": audience,
                "algorithm": algorithm,
                "validFrom": valid_from,
                "validTo": valid_to,
                "invalidateCurrent": invalidate_current,
                "invalidateGracePeriodSec": invalidate_grace_period_sec,
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
                    JwtKeyPairResponseDto,
                    parse_obj_as(
                        type_=JwtKeyPairResponseDto,
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
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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

    async def get_current_jwt_key_pair(
        self, *, audience: GetCurrentJwtKeyPairRequestAudience, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[JwtKeyPairResponseDto]:
        """
        Retrieves information about the currently active JWT signing key-pair for the specified audience.

        Parameters
        ----------
        audience : GetCurrentJwtKeyPairRequestAudience

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JwtKeyPairResponseDto]
            Current key-pair information retrieved successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "oauth/keys/keypair/current",
            method="GET",
            params={
                "audience": audience,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JwtKeyPairResponseDto,
                    parse_obj_as(
                        type_=JwtKeyPairResponseDto,
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
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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

    async def delete_jwt_key_pair(
        self, key_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Deletes a JWT signing key-pair. The key will first be invalidated (if not already)
        and then removed from storage.

        Parameters
        ----------
        key_id : str
            The unique identifier (kid) of the key-pair to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"oauth/keys/keypair/{encode_path_param(key_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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

    async def invalidate_jwt_key_pair(
        self,
        key_id: str,
        *,
        grace_period_sec: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Invalidates a specific JWT signing key-pair.
        After invalidation, the key will no longer be used for signing new tokens,
        and existing tokens signed with this key pair would not be accepted.

        Parameters
        ----------
        key_id : str
            The unique identifier (kid) of the key-pair to invalidate

        grace_period_sec : typing.Optional[int]
            Number of seconds to keep the key valid after invalidation. Default is 0 (immediate invalidation).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"oauth/keys/keypair/{encode_path_param(key_id)}/invalidate",
            method="POST",
            json={
                "gracePeriodSec": grace_period_sec,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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

    async def reactivate_jwt_key_pair(
        self, key_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[JwtKeyPairResponseDto]:
        """
        Reactivates a previously invalidated JWT signing key-pair.
        This allows the key to be used for signing and validating tokens again.
        This operation is idempotent - if the key-pair is already active, it returns the current state.

        Parameters
        ----------
        key_id : str
            The unique identifier (kid) of the key-pair to reactivate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JwtKeyPairResponseDto]
            JWT key-pair reactivated successfully or already active
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"oauth/keys/keypair/{encode_path_param(key_id)}/reactivate",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JwtKeyPairResponseDto,
                    parse_obj_as(
                        type_=JwtKeyPairResponseDto,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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

    async def list_trusted_keys(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[TrustedKeyResponseDto]]:
        """
        Returns all trusted public keys registered for the caller's tenant.
        Requires ADMIN or SUPER_USER role.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[TrustedKeyResponseDto]]
            List of trusted keys
        """
        _response = await self._client_wrapper.httpx_client.request(
            "oauth/keys/trusted",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[TrustedKeyResponseDto],
                    parse_obj_as(
                        type_=typing.List[TrustedKeyResponseDto],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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

    async def register_trusted_key(
        self,
        *,
        key_id: str,
        jwk: typing.Dict[str, typing.Dict[str, typing.Any]],
        audience: RegisterTrustedKeyRequestDtoAudience,
        issuers: typing.Optional[typing.Sequence[str]] = OMIT,
        valid_from: typing.Optional[dt.datetime] = OMIT,
        valid_to: typing.Optional[dt.datetime] = OMIT,
        invalidate_previous: typing.Optional[bool] = OMIT,
        invalidate_grace_period_sec: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TrustedKeyResponseDto]:
        """
        Registers a pre-shared public key for JWT validation. This enables external applications
        to sign user JWTs that Cyoda can verify without requiring a reachable OIDC discovery endpoint.
        The key is bound to the caller's tenant (legalEntityId).

        If a key with the same `keyId` already exists and belongs to the caller's tenant, it is
        replaced atomically (upsert semantics). This makes the endpoint retry-safe during key
        rotation — a retried request after a partial failure will succeed rather than conflict.
        If the key belongs to a different tenant, the request is rejected with `409 Conflict`.

        Use `invalidatePrevious` to retire all other active trusted keys for this tenant
        in a single atomic operation, with an optional grace period (`invalidateGracePeriodSec`)
        during which the old keys continue to be accepted.

        Requires ADMIN or SUPER_USER role. Disabled by default — enable via
        `cyoda.security.web.iam.trustedKeyRegistrationEnabled`.

        Parameters
        ----------
        key_id : str
            Unique key identifier. Will be matched against the `kid` header in JWTs.

        jwk : typing.Dict[str, typing.Dict[str, typing.Any]]
            A JSON Web Key (JWK) as defined in RFC 7517. Must contain the public key components only. Supported key types: RSA (`kty: "RSA"`), EC (`kty: "EC"`), and OKP/EdDSA (`kty: "OKP"`). See RFC 7517, RFC 7518, and RFC 8037 for field definitions.

        audience : RegisterTrustedKeyRequestDtoAudience

        issuers : typing.Optional[typing.Sequence[str]]
            List of allowed issuer URIs. When this parameter is configured, the JWT must contain an iss claim, and its value must match one of the entries in this list.

        valid_from : typing.Optional[dt.datetime]
            When the key becomes valid. Defaults to current time if not specified.

        valid_to : typing.Optional[dt.datetime]
            When the key expires. Defaults to the system-configured maximum validity.

        invalidate_previous : typing.Optional[bool]
            If true, invalidates all other keys for the same audience belonging to the caller's tenant. Enables atomic key rotation.

        invalidate_grace_period_sec : typing.Optional[int]
            Grace period in seconds for invalidating previous keys (only used when invalidatePrevious is true). Default is 0 (immediate invalidation).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TrustedKeyResponseDto]
            Trusted key registered successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "oauth/keys/trusted",
            method="POST",
            json={
                "keyId": key_id,
                "jwk": jwk,
                "audience": audience,
                "issuers": issuers,
                "validFrom": valid_from,
                "validTo": valid_to,
                "invalidatePrevious": invalidate_previous,
                "invalidateGracePeriodSec": invalidate_grace_period_sec,
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
                    TrustedKeyResponseDto,
                    parse_obj_as(
                        type_=TrustedKeyResponseDto,
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
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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

    async def delete_trusted_key(
        self, key_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Deletes a registered trusted public key. The key must belong to the caller's tenant.
        Requires ADMIN or SUPER_USER role.

        Parameters
        ----------
        key_id : str
            The key ID of the trusted key to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"oauth/keys/trusted/{encode_path_param(key_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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

    async def invalidate_trusted_key(
        self,
        key_id: str,
        *,
        grace_period_sec: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Invalidates a registered trusted public key. After invalidation, JWTs signed with the
        corresponding private key will no longer be accepted for validation (after the grace period).
        Requires ADMIN or SUPER_USER role.

        Parameters
        ----------
        key_id : str
            The key ID of the trusted key to invalidate

        grace_period_sec : typing.Optional[int]
            Number of seconds to keep the key valid after invalidation. Default is 0 (immediate invalidation).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"oauth/keys/trusted/{encode_path_param(key_id)}/invalidate",
            method="POST",
            json={
                "gracePeriodSec": grace_period_sec,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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

    async def reactivate_trusted_key(
        self, key_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[TrustedKeyResponseDto]:
        """
        Reactivates a previously invalidated trusted public key, allowing JWTs signed with it to
        be accepted again. This operation is idempotent.
        Requires ADMIN or SUPER_USER role.

        **Important**: Reactivation removes the key's expiration entirely (`validTo` is cleared to null),
        regardless of the original `validTo` value the key was registered with. The key will remain valid
        indefinitely until explicitly invalidated or deleted again.

        Parameters
        ----------
        key_id : str
            The key ID of the trusted key to reactivate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TrustedKeyResponseDto]
            Trusted key reactivated successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"oauth/keys/trusted/{encode_path_param(key_id)}/reactivate",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TrustedKeyResponseDto,
                    parse_obj_as(
                        type_=TrustedKeyResponseDto,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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

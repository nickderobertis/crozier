

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.jwt_key_pair_response_dto import JwtKeyPairResponseDto
from ..types.trusted_key_response_dto import TrustedKeyResponseDto
from .raw_client import AsyncRawOAuthKeysClient, RawOAuthKeysClient
from .types.get_current_jwt_key_pair_request_audience import GetCurrentJwtKeyPairRequestAudience
from .types.issue_jwt_key_pair_request_dto_algorithm import IssueJwtKeyPairRequestDtoAlgorithm
from .types.issue_jwt_key_pair_request_dto_audience import IssueJwtKeyPairRequestDtoAudience
from .types.register_trusted_key_request_dto_audience import RegisterTrustedKeyRequestDtoAudience


OMIT = typing.cast(typing.Any, ...)


class OAuthKeysClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOAuthKeysClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOAuthKeysClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOAuthKeysClient
        """
        return self._raw_client

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
    ) -> JwtKeyPairResponseDto:
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
        JwtKeyPairResponseDto
            JWT key-pair issued successfully

        Examples
        --------
        from fern.o_auth_keys import (
            IssueJwtKeyPairRequestDtoAlgorithm,
            IssueJwtKeyPairRequestDtoAudience,
        )

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.o_auth_keys.issue_jwt_key_pair(
            audience=IssueJwtKeyPairRequestDtoAudience.HUMAN,
            algorithm=IssueJwtKeyPairRequestDtoAlgorithm.RS256,
        )
        """
        _response = self._raw_client.issue_jwt_key_pair(
            audience=audience,
            algorithm=algorithm,
            valid_from=valid_from,
            valid_to=valid_to,
            invalidate_current=invalidate_current,
            invalidate_grace_period_sec=invalidate_grace_period_sec,
            request_options=request_options,
        )
        return _response.data

    def get_current_jwt_key_pair(
        self, *, audience: GetCurrentJwtKeyPairRequestAudience, request_options: typing.Optional[RequestOptions] = None
    ) -> JwtKeyPairResponseDto:
        """
        Retrieves information about the currently active JWT signing key-pair for the specified audience.

        Parameters
        ----------
        audience : GetCurrentJwtKeyPairRequestAudience

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JwtKeyPairResponseDto
            Current key-pair information retrieved successfully

        Examples
        --------
        from fern.o_auth_keys import GetCurrentJwtKeyPairRequestAudience

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.o_auth_keys.get_current_jwt_key_pair(
            audience=GetCurrentJwtKeyPairRequestAudience.HUMAN,
        )
        """
        _response = self._raw_client.get_current_jwt_key_pair(audience=audience, request_options=request_options)
        return _response.data

    def delete_jwt_key_pair(self, key_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.o_auth_keys.delete_jwt_key_pair(
            key_id="keyId",
        )
        """
        _response = self._raw_client.delete_jwt_key_pair(key_id, request_options=request_options)
        return _response.data

    def invalidate_jwt_key_pair(
        self,
        key_id: str,
        *,
        grace_period_sec: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
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
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.o_auth_keys.invalidate_jwt_key_pair(
            key_id="keyId",
        )
        """
        _response = self._raw_client.invalidate_jwt_key_pair(
            key_id, grace_period_sec=grace_period_sec, request_options=request_options
        )
        return _response.data

    def reactivate_jwt_key_pair(
        self, key_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> JwtKeyPairResponseDto:
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
        JwtKeyPairResponseDto
            JWT key-pair reactivated successfully or already active

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.o_auth_keys.reactivate_jwt_key_pair(
            key_id="keyId",
        )
        """
        _response = self._raw_client.reactivate_jwt_key_pair(key_id, request_options=request_options)
        return _response.data

    def list_trusted_keys(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TrustedKeyResponseDto]:
        """
        Returns all trusted public keys registered for the caller's tenant.
        Requires ADMIN or SUPER_USER role.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TrustedKeyResponseDto]
            List of trusted keys

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.o_auth_keys.list_trusted_keys()
        """
        _response = self._raw_client.list_trusted_keys(request_options=request_options)
        return _response.data

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
    ) -> TrustedKeyResponseDto:
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
        TrustedKeyResponseDto
            Trusted key registered successfully

        Examples
        --------
        from fern.o_auth_keys import RegisterTrustedKeyRequestDtoAudience

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.o_auth_keys.register_trusted_key(
            key_id="my-app-key-1",
            jwk={"key": {"key": "value"}},
            audience=RegisterTrustedKeyRequestDtoAudience.HUMAN,
        )
        """
        _response = self._raw_client.register_trusted_key(
            key_id=key_id,
            jwk=jwk,
            audience=audience,
            issuers=issuers,
            valid_from=valid_from,
            valid_to=valid_to,
            invalidate_previous=invalidate_previous,
            invalidate_grace_period_sec=invalidate_grace_period_sec,
            request_options=request_options,
        )
        return _response.data

    def delete_trusted_key(self, key_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.o_auth_keys.delete_trusted_key(
            key_id="keyId",
        )
        """
        _response = self._raw_client.delete_trusted_key(key_id, request_options=request_options)
        return _response.data

    def invalidate_trusted_key(
        self,
        key_id: str,
        *,
        grace_period_sec: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
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
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.o_auth_keys.invalidate_trusted_key(
            key_id="keyId",
        )
        """
        _response = self._raw_client.invalidate_trusted_key(
            key_id, grace_period_sec=grace_period_sec, request_options=request_options
        )
        return _response.data

    def reactivate_trusted_key(
        self, key_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TrustedKeyResponseDto:
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
        TrustedKeyResponseDto
            Trusted key reactivated successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.o_auth_keys.reactivate_trusted_key(
            key_id="keyId",
        )
        """
        _response = self._raw_client.reactivate_trusted_key(key_id, request_options=request_options)
        return _response.data


class AsyncOAuthKeysClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOAuthKeysClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOAuthKeysClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOAuthKeysClient
        """
        return self._raw_client

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
    ) -> JwtKeyPairResponseDto:
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
        JwtKeyPairResponseDto
            JWT key-pair issued successfully

        Examples
        --------
        import asyncio

        from fern.o_auth_keys import (
            IssueJwtKeyPairRequestDtoAlgorithm,
            IssueJwtKeyPairRequestDtoAudience,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.o_auth_keys.issue_jwt_key_pair(
                audience=IssueJwtKeyPairRequestDtoAudience.HUMAN,
                algorithm=IssueJwtKeyPairRequestDtoAlgorithm.RS256,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.issue_jwt_key_pair(
            audience=audience,
            algorithm=algorithm,
            valid_from=valid_from,
            valid_to=valid_to,
            invalidate_current=invalidate_current,
            invalidate_grace_period_sec=invalidate_grace_period_sec,
            request_options=request_options,
        )
        return _response.data

    async def get_current_jwt_key_pair(
        self, *, audience: GetCurrentJwtKeyPairRequestAudience, request_options: typing.Optional[RequestOptions] = None
    ) -> JwtKeyPairResponseDto:
        """
        Retrieves information about the currently active JWT signing key-pair for the specified audience.

        Parameters
        ----------
        audience : GetCurrentJwtKeyPairRequestAudience

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JwtKeyPairResponseDto
            Current key-pair information retrieved successfully

        Examples
        --------
        import asyncio

        from fern.o_auth_keys import GetCurrentJwtKeyPairRequestAudience

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.o_auth_keys.get_current_jwt_key_pair(
                audience=GetCurrentJwtKeyPairRequestAudience.HUMAN,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_current_jwt_key_pair(audience=audience, request_options=request_options)
        return _response.data

    async def delete_jwt_key_pair(
        self, key_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
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
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.o_auth_keys.delete_jwt_key_pair(
                key_id="keyId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_jwt_key_pair(key_id, request_options=request_options)
        return _response.data

    async def invalidate_jwt_key_pair(
        self,
        key_id: str,
        *,
        grace_period_sec: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
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
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.o_auth_keys.invalidate_jwt_key_pair(
                key_id="keyId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.invalidate_jwt_key_pair(
            key_id, grace_period_sec=grace_period_sec, request_options=request_options
        )
        return _response.data

    async def reactivate_jwt_key_pair(
        self, key_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> JwtKeyPairResponseDto:
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
        JwtKeyPairResponseDto
            JWT key-pair reactivated successfully or already active

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.o_auth_keys.reactivate_jwt_key_pair(
                key_id="keyId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.reactivate_jwt_key_pair(key_id, request_options=request_options)
        return _response.data

    async def list_trusted_keys(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TrustedKeyResponseDto]:
        """
        Returns all trusted public keys registered for the caller's tenant.
        Requires ADMIN or SUPER_USER role.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TrustedKeyResponseDto]
            List of trusted keys

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.o_auth_keys.list_trusted_keys()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_trusted_keys(request_options=request_options)
        return _response.data

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
    ) -> TrustedKeyResponseDto:
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
        TrustedKeyResponseDto
            Trusted key registered successfully

        Examples
        --------
        import asyncio

        from fern.o_auth_keys import RegisterTrustedKeyRequestDtoAudience

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.o_auth_keys.register_trusted_key(
                key_id="my-app-key-1",
                jwk={"key": {"key": "value"}},
                audience=RegisterTrustedKeyRequestDtoAudience.HUMAN,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.register_trusted_key(
            key_id=key_id,
            jwk=jwk,
            audience=audience,
            issuers=issuers,
            valid_from=valid_from,
            valid_to=valid_to,
            invalidate_previous=invalidate_previous,
            invalidate_grace_period_sec=invalidate_grace_period_sec,
            request_options=request_options,
        )
        return _response.data

    async def delete_trusted_key(self, key_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.o_auth_keys.delete_trusted_key(
                key_id="keyId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_trusted_key(key_id, request_options=request_options)
        return _response.data

    async def invalidate_trusted_key(
        self,
        key_id: str,
        *,
        grace_period_sec: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
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
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.o_auth_keys.invalidate_trusted_key(
                key_id="keyId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.invalidate_trusted_key(
            key_id, grace_period_sec=grace_period_sec, request_options=request_options
        )
        return _response.data

    async def reactivate_trusted_key(
        self, key_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TrustedKeyResponseDto:
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
        TrustedKeyResponseDto
            Trusted key reactivated successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.o_auth_keys.reactivate_trusted_key(
                key_id="keyId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.reactivate_trusted_key(key_id, request_options=request_options)
        return _response.data

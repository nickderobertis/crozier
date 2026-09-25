

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_gateway_error import BadGatewayError
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..types.bad_gateway_error_body import BadGatewayErrorBody
from ..types.json_success import JsonSuccess
from .types.register_client_device_response import RegisterClientDeviceResponse
from .types.register_push_device_request_token_kind import RegisterPushDeviceRequestTokenKind
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawMobileClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def test_notify(
        self, *, token: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[JsonSuccess]:
        """
        Trigger sending a test push notification to the user's
        selected mobile device or all of their mobile devices.

        **Changes**: Deprecated in Zulip 11.0 (feature level 420).
        Clients connecting to newer servers and with E2EE push
        notifications support should use the
        [Send an E2EE test notification to mobile device(s)](/api/e2ee-test-notify)
        endpoint, as this endpoint will be removed in a future release.

        Starting with Zulip 8.0 (feature level 234), test
        notifications sent via this endpoint use `test` rather than
        `test-by-device-token` in the `event` field. Also, as of this
        feature level, all mobile push notifications now include a
        `realm_name` field.

        New in Zulip 8.0 (feature level 217).

        Parameters
        ----------
        token : typing.Optional[str]
            The push token for the device to which to send the test notification.

            If this parameter is not submitted, the test notification will be sent
            to all of the user's devices registered on the server.

            A mobile client should pass this parameter, to avoid triggering a test
            notification for other clients.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JsonSuccess]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            "mobile_push/test_notification",
            method="POST",
            data={
                "token": token,
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
                    JsonSuccess,
                    parse_obj_as(
                        type_=JsonSuccess,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def e2ee_test_notify(
        self, *, device_id: typing.Optional[int] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[JsonSuccess]:
        """
        Trigger sending an end-to-end encrypted (E2EE) test push notification
        to the user's selected mobile device or all of their mobile devices.

        **Changes**: New in Zulip 11.0 (feature level 420).

        Parameters
        ----------
        device_id : typing.Optional[int]
            The ID for the device to which to send the test notification.

            If this parameter is not submitted, the E2EE test notification will
            be sent to all of the user's devices registered on the server.

            A mobile client should pass this parameter, to avoid triggering a test
            notification for other clients.

            See [`POST /register_client_device`](/api/register-client-device)
            for details on device ID.

            **Changes**: New in Zulip 12.0 (feature level 468).

            Previously, `push_account_id` was used.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JsonSuccess]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            "mobile_push/e2ee/test_notification",
            method="POST",
            data={
                "device_id": device_id,
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
                    JsonSuccess,
                    parse_obj_as(
                        type_=JsonSuccess,
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
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadGatewayErrorBody,
                        parse_obj_as(
                            type_=BadGatewayErrorBody,
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

    def register_push_device(
        self,
        *,
        device_id: int,
        push_key_id: typing.Optional[int] = OMIT,
        push_key: typing.Optional[str] = OMIT,
        token_kind: typing.Optional[RegisterPushDeviceRequestTokenKind] = OMIT,
        token_id: typing.Optional[str] = OMIT,
        bouncer_public_key: typing.Optional[str] = OMIT,
        encrypted_push_registration: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[JsonSuccess]:
        """
        Register a device to receive end-to-end encrypted mobile push notifications,
        or update such a registration.

        To perform an initial registration, clients must provide both the
        push key fields (`push_key` and `push_key_id`) and the token fields
        (`token_kind`, `token_id`, `bouncer_public_key`, and `encrypted_push_registration`).

        Once registered, clients should use this endpoint to rotate `push_key` or
        FCM/APNs provided token:

        - **Rotate push key**: Provide only the push key fields.
        - **Rotate token**: Provide only the token fields.

        On a successful registration, the server automatically removes
        any legacy push device registration with a matching token for
        the user. For self-hosted servers, if removing the legacy
        registration from the push notification bouncer fails (e.g.,
        due to a network error), legacy notifications to that token
        will continue until all of the user's legacy registrations
        have been removed from the local server, at which point the
        server will stop sending legacy notification requests to the
        bouncer entirely.

        **Changes**: In Zulip 12.0 (feature level 483),
        the server began automatically removing legacy registrations
        with a matching token on successful E2EE registration.

        In Zulip 12.0 (feature level 468), the endpoint was significantly
        redesigned to support rotation of `push_key` and token provided by FCM/APNs.

        New in Zulip 11.0 (feature level 406).

        Parameters
        ----------
        device_id : int
            The ID of the device to configure for push notifications.

            See [`POST /register_client_device`](/api/register-client-device)
            for how to obtain a device ID.

        push_key_id : typing.Optional[int]
            A random unsigned 32-bit integer generated by the client as an identifier
            for `push_key`. It will be included in mobile push notifications
            along with encrypted payloads to identify the `push_key` to decrypt.

        push_key : typing.Optional[str]
            Key that the client would like the server to use to encrypt notifications,
            encoded with Base64.

            The key is a byte sequence beginning with a single byte that encodes which
            cryptosystem to use, followed by the key to use for that cryptosystem.
            This byte sequence is encoded using standard Base64 encoding as defined in RFC 4648.

            The client should avoid sharing the key anywhere else: in particular it should
            generate a fresh key for each server, and to the extent possible keep the key
            out of any backups of the client's data.

            Supported cryptosystems are:

            - `0x31`: LibSodium's [SecretBox][libsodium-secretbox] symmetric key encryption
              system. Keys are 32 bytes, which the server will use with libsodium's
              `crypto_secretbox_easy`. See the [NaCl documentation][nacl-secretbox], which
              details how this system uses `XSalsa20` and `Poly1305` to provide authenticated
              encryption.

            [libsodium-secretbox]: https://libsodium.gitbook.io/doc/secret-key_cryptography/secretbox
            [nacl-secretbox]: https://nacl.cr.yp.to/secretbox.html

            **Changes**: New in Zulip 12.0 (feature level 432). This replaced the
            `push_public_key` parameter which had a prototype asymmetric cryptosystem, and
            did not have a natural way to support multiple cryptosystems.

        token_kind : typing.Optional[RegisterPushDeviceRequestTokenKind]
            Whether the token was generated by FCM or APNs.

        token_id : typing.Optional[str]
            Identifier for the FCM/APNs provided token to the device,
            produced by taking the first 8 bytes of the SHA-256 hash of
            the token, then encoding those bytes using standard Base64 encoding
            as defined in RFC 4648.

        bouncer_public_key : typing.Optional[str]
            Which of the bouncer's public keys the client used to encrypt the
            `PushRegistration` dictionary.

            When the bouncer rotates the key, a new asymmetric key pair is created,
            and the new public key is baked into a new client release. Because
            the bouncer routinely rotates key, this field clarifies which
            public key the client is using.

            The public key is encoded using standard Base64 encoding as defined
            in RFC 4648.

        encrypted_push_registration : typing.Optional[str]
            Ciphertext generated by encrypting a `PushRegistration` dictionary
            using the `bouncer_public_key`, encoded using a RFC 4648 standard
            base64 encoder.

            The `PushRegistration` dictionary contains the fields `token`,
            `token_kind`, `timestamp`, and (for iOS devices) `ios_app_id`.
            The dictionary is JSON-encoded before encryption.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JsonSuccess]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            "mobile_push/register",
            method="POST",
            data={
                "device_id": device_id,
                "push_key_id": push_key_id,
                "push_key": push_key,
                "token_kind": token_kind,
                "token_id": token_id,
                "bouncer_public_key": bouncer_public_key,
                "encrypted_push_registration": encrypted_push_registration,
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
                    JsonSuccess,
                    parse_obj_as(
                        type_=JsonSuccess,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def register_remote_push_device(
        self,
        *,
        realm_uuid: str,
        token_id: str,
        encrypted_push_registration: str,
        bouncer_public_key: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[JsonSuccess]:
        """
        Register a push device to bouncer to receive end-to-end encrypted
        mobile push notifications.

        Self-hosted servers use this endpoint to asynchronously register
        a push device to the bouncer server after receiving a request from
        the mobile client to [register E2EE push device](/api/register-push-device).

        It is not meant to be used by mobile clients directly.

        **Changes**: New in Zulip 11.0 (feature level 406).

        Parameters
        ----------
        realm_uuid : str
            The UUID of the realm to which the push device
            being registered belongs.

        token_id : str
            The `token_id` value provided by the mobile client
            to [register E2EE push device](/api/register-push-device).

            **Changes**: New in Zulip 12.0 (feature level 468),
            replacing `push_account_id`.

        encrypted_push_registration : str
            The `encrypted_push_registration` value provided by the mobile client
            to [register E2EE push device](/api/register-push-device).

        bouncer_public_key : str
            The `bouncer_public_key` value provided by the mobile client
            to [register E2EE push device](/api/register-push-device).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JsonSuccess]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            "remotes/push/e2ee/register",
            method="POST",
            data={
                "realm_uuid": realm_uuid,
                "token_id": token_id,
                "encrypted_push_registration": encrypted_push_registration,
                "bouncer_public_key": bouncer_public_key,
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
                    JsonSuccess,
                    parse_obj_as(
                        type_=JsonSuccess,
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

    def register_client_device(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RegisterClientDeviceResponse]:
        """
        Logged-in mobile devices use this endpoint as an initial step to
        register themselves, before registering for E2EE push notifications.

        This endpoint is currently not useful for clients other than mobile.

        **Changes**: New in Zulip 12.0 (feature level 468).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RegisterClientDeviceResponse]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            "register_client_device",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RegisterClientDeviceResponse,
                    parse_obj_as(
                        type_=RegisterClientDeviceResponse,
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

    def remove_client_device(
        self, *, device_id: int, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[JsonSuccess]:
        """
        Mobile devices use this endpoint to remove their device record
        registered using [`POST /register_client_device`](/api/register-client-device)
        when the user logs out.

        This endpoint is currently not useful for clients other than mobile.

        **Changes**: New in Zulip 12.0 (feature level 470).

        Parameters
        ----------
        device_id : int
            The ID of the device to remove.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JsonSuccess]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            "remove_client_device",
            method="POST",
            data={
                "device_id": device_id,
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
                    JsonSuccess,
                    parse_obj_as(
                        type_=JsonSuccess,
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


class AsyncRawMobileClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def test_notify(
        self, *, token: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[JsonSuccess]:
        """
        Trigger sending a test push notification to the user's
        selected mobile device or all of their mobile devices.

        **Changes**: Deprecated in Zulip 11.0 (feature level 420).
        Clients connecting to newer servers and with E2EE push
        notifications support should use the
        [Send an E2EE test notification to mobile device(s)](/api/e2ee-test-notify)
        endpoint, as this endpoint will be removed in a future release.

        Starting with Zulip 8.0 (feature level 234), test
        notifications sent via this endpoint use `test` rather than
        `test-by-device-token` in the `event` field. Also, as of this
        feature level, all mobile push notifications now include a
        `realm_name` field.

        New in Zulip 8.0 (feature level 217).

        Parameters
        ----------
        token : typing.Optional[str]
            The push token for the device to which to send the test notification.

            If this parameter is not submitted, the test notification will be sent
            to all of the user's devices registered on the server.

            A mobile client should pass this parameter, to avoid triggering a test
            notification for other clients.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JsonSuccess]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mobile_push/test_notification",
            method="POST",
            data={
                "token": token,
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
                    JsonSuccess,
                    parse_obj_as(
                        type_=JsonSuccess,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def e2ee_test_notify(
        self, *, device_id: typing.Optional[int] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[JsonSuccess]:
        """
        Trigger sending an end-to-end encrypted (E2EE) test push notification
        to the user's selected mobile device or all of their mobile devices.

        **Changes**: New in Zulip 11.0 (feature level 420).

        Parameters
        ----------
        device_id : typing.Optional[int]
            The ID for the device to which to send the test notification.

            If this parameter is not submitted, the E2EE test notification will
            be sent to all of the user's devices registered on the server.

            A mobile client should pass this parameter, to avoid triggering a test
            notification for other clients.

            See [`POST /register_client_device`](/api/register-client-device)
            for details on device ID.

            **Changes**: New in Zulip 12.0 (feature level 468).

            Previously, `push_account_id` was used.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JsonSuccess]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mobile_push/e2ee/test_notification",
            method="POST",
            data={
                "device_id": device_id,
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
                    JsonSuccess,
                    parse_obj_as(
                        type_=JsonSuccess,
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
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadGatewayErrorBody,
                        parse_obj_as(
                            type_=BadGatewayErrorBody,
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

    async def register_push_device(
        self,
        *,
        device_id: int,
        push_key_id: typing.Optional[int] = OMIT,
        push_key: typing.Optional[str] = OMIT,
        token_kind: typing.Optional[RegisterPushDeviceRequestTokenKind] = OMIT,
        token_id: typing.Optional[str] = OMIT,
        bouncer_public_key: typing.Optional[str] = OMIT,
        encrypted_push_registration: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[JsonSuccess]:
        """
        Register a device to receive end-to-end encrypted mobile push notifications,
        or update such a registration.

        To perform an initial registration, clients must provide both the
        push key fields (`push_key` and `push_key_id`) and the token fields
        (`token_kind`, `token_id`, `bouncer_public_key`, and `encrypted_push_registration`).

        Once registered, clients should use this endpoint to rotate `push_key` or
        FCM/APNs provided token:

        - **Rotate push key**: Provide only the push key fields.
        - **Rotate token**: Provide only the token fields.

        On a successful registration, the server automatically removes
        any legacy push device registration with a matching token for
        the user. For self-hosted servers, if removing the legacy
        registration from the push notification bouncer fails (e.g.,
        due to a network error), legacy notifications to that token
        will continue until all of the user's legacy registrations
        have been removed from the local server, at which point the
        server will stop sending legacy notification requests to the
        bouncer entirely.

        **Changes**: In Zulip 12.0 (feature level 483),
        the server began automatically removing legacy registrations
        with a matching token on successful E2EE registration.

        In Zulip 12.0 (feature level 468), the endpoint was significantly
        redesigned to support rotation of `push_key` and token provided by FCM/APNs.

        New in Zulip 11.0 (feature level 406).

        Parameters
        ----------
        device_id : int
            The ID of the device to configure for push notifications.

            See [`POST /register_client_device`](/api/register-client-device)
            for how to obtain a device ID.

        push_key_id : typing.Optional[int]
            A random unsigned 32-bit integer generated by the client as an identifier
            for `push_key`. It will be included in mobile push notifications
            along with encrypted payloads to identify the `push_key` to decrypt.

        push_key : typing.Optional[str]
            Key that the client would like the server to use to encrypt notifications,
            encoded with Base64.

            The key is a byte sequence beginning with a single byte that encodes which
            cryptosystem to use, followed by the key to use for that cryptosystem.
            This byte sequence is encoded using standard Base64 encoding as defined in RFC 4648.

            The client should avoid sharing the key anywhere else: in particular it should
            generate a fresh key for each server, and to the extent possible keep the key
            out of any backups of the client's data.

            Supported cryptosystems are:

            - `0x31`: LibSodium's [SecretBox][libsodium-secretbox] symmetric key encryption
              system. Keys are 32 bytes, which the server will use with libsodium's
              `crypto_secretbox_easy`. See the [NaCl documentation][nacl-secretbox], which
              details how this system uses `XSalsa20` and `Poly1305` to provide authenticated
              encryption.

            [libsodium-secretbox]: https://libsodium.gitbook.io/doc/secret-key_cryptography/secretbox
            [nacl-secretbox]: https://nacl.cr.yp.to/secretbox.html

            **Changes**: New in Zulip 12.0 (feature level 432). This replaced the
            `push_public_key` parameter which had a prototype asymmetric cryptosystem, and
            did not have a natural way to support multiple cryptosystems.

        token_kind : typing.Optional[RegisterPushDeviceRequestTokenKind]
            Whether the token was generated by FCM or APNs.

        token_id : typing.Optional[str]
            Identifier for the FCM/APNs provided token to the device,
            produced by taking the first 8 bytes of the SHA-256 hash of
            the token, then encoding those bytes using standard Base64 encoding
            as defined in RFC 4648.

        bouncer_public_key : typing.Optional[str]
            Which of the bouncer's public keys the client used to encrypt the
            `PushRegistration` dictionary.

            When the bouncer rotates the key, a new asymmetric key pair is created,
            and the new public key is baked into a new client release. Because
            the bouncer routinely rotates key, this field clarifies which
            public key the client is using.

            The public key is encoded using standard Base64 encoding as defined
            in RFC 4648.

        encrypted_push_registration : typing.Optional[str]
            Ciphertext generated by encrypting a `PushRegistration` dictionary
            using the `bouncer_public_key`, encoded using a RFC 4648 standard
            base64 encoder.

            The `PushRegistration` dictionary contains the fields `token`,
            `token_kind`, `timestamp`, and (for iOS devices) `ios_app_id`.
            The dictionary is JSON-encoded before encryption.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JsonSuccess]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mobile_push/register",
            method="POST",
            data={
                "device_id": device_id,
                "push_key_id": push_key_id,
                "push_key": push_key,
                "token_kind": token_kind,
                "token_id": token_id,
                "bouncer_public_key": bouncer_public_key,
                "encrypted_push_registration": encrypted_push_registration,
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
                    JsonSuccess,
                    parse_obj_as(
                        type_=JsonSuccess,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def register_remote_push_device(
        self,
        *,
        realm_uuid: str,
        token_id: str,
        encrypted_push_registration: str,
        bouncer_public_key: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[JsonSuccess]:
        """
        Register a push device to bouncer to receive end-to-end encrypted
        mobile push notifications.

        Self-hosted servers use this endpoint to asynchronously register
        a push device to the bouncer server after receiving a request from
        the mobile client to [register E2EE push device](/api/register-push-device).

        It is not meant to be used by mobile clients directly.

        **Changes**: New in Zulip 11.0 (feature level 406).

        Parameters
        ----------
        realm_uuid : str
            The UUID of the realm to which the push device
            being registered belongs.

        token_id : str
            The `token_id` value provided by the mobile client
            to [register E2EE push device](/api/register-push-device).

            **Changes**: New in Zulip 12.0 (feature level 468),
            replacing `push_account_id`.

        encrypted_push_registration : str
            The `encrypted_push_registration` value provided by the mobile client
            to [register E2EE push device](/api/register-push-device).

        bouncer_public_key : str
            The `bouncer_public_key` value provided by the mobile client
            to [register E2EE push device](/api/register-push-device).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JsonSuccess]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "remotes/push/e2ee/register",
            method="POST",
            data={
                "realm_uuid": realm_uuid,
                "token_id": token_id,
                "encrypted_push_registration": encrypted_push_registration,
                "bouncer_public_key": bouncer_public_key,
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
                    JsonSuccess,
                    parse_obj_as(
                        type_=JsonSuccess,
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

    async def register_client_device(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RegisterClientDeviceResponse]:
        """
        Logged-in mobile devices use this endpoint as an initial step to
        register themselves, before registering for E2EE push notifications.

        This endpoint is currently not useful for clients other than mobile.

        **Changes**: New in Zulip 12.0 (feature level 468).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RegisterClientDeviceResponse]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "register_client_device",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RegisterClientDeviceResponse,
                    parse_obj_as(
                        type_=RegisterClientDeviceResponse,
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

    async def remove_client_device(
        self, *, device_id: int, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[JsonSuccess]:
        """
        Mobile devices use this endpoint to remove their device record
        registered using [`POST /register_client_device`](/api/register-client-device)
        when the user logs out.

        This endpoint is currently not useful for clients other than mobile.

        **Changes**: New in Zulip 12.0 (feature level 470).

        Parameters
        ----------
        device_id : int
            The ID of the device to remove.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JsonSuccess]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "remove_client_device",
            method="POST",
            data={
                "device_id": device_id,
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
                    JsonSuccess,
                    parse_obj_as(
                        type_=JsonSuccess,
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

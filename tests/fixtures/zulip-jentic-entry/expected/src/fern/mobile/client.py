

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.json_success import JsonSuccess
from .raw_client import AsyncRawMobileClient, RawMobileClient
from .types.register_client_device_response import RegisterClientDeviceResponse
from .types.register_push_device_request_token_kind import RegisterPushDeviceRequestTokenKind


OMIT = typing.cast(typing.Any, ...)


class MobileClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMobileClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMobileClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMobileClient
        """
        return self._raw_client

    def test_notify(
        self, *, token: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> JsonSuccess:
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
        JsonSuccess
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.mobile.test_notify()
        """
        _response = self._raw_client.test_notify(token=token, request_options=request_options)
        return _response.data

    def e2ee_test_notify(
        self, *, device_id: typing.Optional[int] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> JsonSuccess:
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
        JsonSuccess
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.mobile.e2ee_test_notify()
        """
        _response = self._raw_client.e2ee_test_notify(device_id=device_id, request_options=request_options)
        return _response.data

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
    ) -> JsonSuccess:
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

        **Changes**: In Zulip 12.0 (feature level 468), the endpoint
        was significantly redesigned to support rotation of `push_key` and
        token provided by FCM/APNs.

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
        JsonSuccess
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.mobile.register_push_device(
            device_id=1,
        )
        """
        _response = self._raw_client.register_push_device(
            device_id=device_id,
            push_key_id=push_key_id,
            push_key=push_key,
            token_kind=token_kind,
            token_id=token_id,
            bouncer_public_key=bouncer_public_key,
            encrypted_push_registration=encrypted_push_registration,
            request_options=request_options,
        )
        return _response.data

    def register_remote_push_device(
        self,
        *,
        realm_uuid: str,
        token_id: str,
        encrypted_push_registration: str,
        bouncer_public_key: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JsonSuccess:
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
        JsonSuccess
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.mobile.register_remote_push_device(
            realm_uuid="9aa61d0b-8ce5-488d-8e9e-fedc346e6836",
            token_id="+wKIhyAx/Eg=",
            encrypted_push_registration="encrypted-push-registration-data",
            bouncer_public_key="bouncer-public-key",
        )
        """
        _response = self._raw_client.register_remote_push_device(
            realm_uuid=realm_uuid,
            token_id=token_id,
            encrypted_push_registration=encrypted_push_registration,
            bouncer_public_key=bouncer_public_key,
            request_options=request_options,
        )
        return _response.data

    def register_client_device(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RegisterClientDeviceResponse:
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
        RegisterClientDeviceResponse
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.mobile.register_client_device()
        """
        _response = self._raw_client.register_client_device(request_options=request_options)
        return _response.data

    def remove_client_device(
        self, *, device_id: int, request_options: typing.Optional[RequestOptions] = None
    ) -> JsonSuccess:
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
        JsonSuccess
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.mobile.remove_client_device(
            device_id=2,
        )
        """
        _response = self._raw_client.remove_client_device(device_id=device_id, request_options=request_options)
        return _response.data


class AsyncMobileClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMobileClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMobileClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMobileClient
        """
        return self._raw_client

    async def test_notify(
        self, *, token: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> JsonSuccess:
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
        JsonSuccess
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.mobile.test_notify()


        asyncio.run(main())
        """
        _response = await self._raw_client.test_notify(token=token, request_options=request_options)
        return _response.data

    async def e2ee_test_notify(
        self, *, device_id: typing.Optional[int] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> JsonSuccess:
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
        JsonSuccess
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.mobile.e2ee_test_notify()


        asyncio.run(main())
        """
        _response = await self._raw_client.e2ee_test_notify(device_id=device_id, request_options=request_options)
        return _response.data

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
    ) -> JsonSuccess:
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

        **Changes**: In Zulip 12.0 (feature level 468), the endpoint
        was significantly redesigned to support rotation of `push_key` and
        token provided by FCM/APNs.

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
        JsonSuccess
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.mobile.register_push_device(
                device_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.register_push_device(
            device_id=device_id,
            push_key_id=push_key_id,
            push_key=push_key,
            token_kind=token_kind,
            token_id=token_id,
            bouncer_public_key=bouncer_public_key,
            encrypted_push_registration=encrypted_push_registration,
            request_options=request_options,
        )
        return _response.data

    async def register_remote_push_device(
        self,
        *,
        realm_uuid: str,
        token_id: str,
        encrypted_push_registration: str,
        bouncer_public_key: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JsonSuccess:
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
        JsonSuccess
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.mobile.register_remote_push_device(
                realm_uuid="9aa61d0b-8ce5-488d-8e9e-fedc346e6836",
                token_id="+wKIhyAx/Eg=",
                encrypted_push_registration="encrypted-push-registration-data",
                bouncer_public_key="bouncer-public-key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.register_remote_push_device(
            realm_uuid=realm_uuid,
            token_id=token_id,
            encrypted_push_registration=encrypted_push_registration,
            bouncer_public_key=bouncer_public_key,
            request_options=request_options,
        )
        return _response.data

    async def register_client_device(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RegisterClientDeviceResponse:
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
        RegisterClientDeviceResponse
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.mobile.register_client_device()


        asyncio.run(main())
        """
        _response = await self._raw_client.register_client_device(request_options=request_options)
        return _response.data

    async def remove_client_device(
        self, *, device_id: int, request_options: typing.Optional[RequestOptions] = None
    ) -> JsonSuccess:
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
        JsonSuccess
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.mobile.remove_client_device(
                device_id=2,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_client_device(device_id=device_id, request_options=request_options)
        return _response.data

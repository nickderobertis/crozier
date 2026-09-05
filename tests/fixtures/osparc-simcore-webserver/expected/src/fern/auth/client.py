

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.envelope_api_key_create_response import EnvelopeApiKeyCreateResponse
from ..types.envelope_api_key_get import EnvelopeApiKeyGet
from ..types.envelope_invitation_info import EnvelopeInvitationInfo
from ..types.envelope_list_api_key_get import EnvelopeListApiKeyGet
from ..types.envelope_log import EnvelopeLog
from ..types.envelope_login_next_page import EnvelopeLoginNextPage
from ..types.envelope_register_phone_next_page import EnvelopeRegisterPhoneNextPage
from ..types.lower_case_email_str import LowerCaseEmailStr
from ..types.phone_number_str import PhoneNumberStr
from .raw_client import AsyncRawAuthClient, RawAuthClient
from .types.resend2fa_body_via import Resend2FaBodyVia


OMIT = typing.cast(typing.Any, ...)


class AuthClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAuthClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAuthClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAuthClient
        """
        return self._raw_client

    def request_product_account(
        self,
        *,
        form: typing.Dict[str, typing.Any],
        captcha: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        form : typing.Dict[str, typing.Any]

        captcha : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.auth.request_product_account(
            form={
                "address": "Infinite Loop",
                "application": "Antenna_Design",
                "city": "Washington",
                "company": "EM Com",
                "country": "Switzerland",
                "description": "Description of something",
                "email": "maxwel@email.com",
                "eula": True,
                "firstName": "James",
                "hear": "Search_Engine",
                "lastName": "Maxwel",
                "phone": "+41 44 245 96 96",
                "postalCode": "98001",
                "privacyPolicy": True,
            },
            captcha="A12B34",
        )
        """
        _response = self._raw_client.request_product_account(
            form=form, captcha=captcha, request_options=request_options
        )
        return _response.data

    def check_registration_invitation(
        self, *, invitation: str, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeInvitationInfo:
        """
        Check invitation and returns associated email or None

        Parameters
        ----------
        invitation : str
            Invitation code

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeInvitationInfo
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.auth.check_registration_invitation(
            invitation="invitation",
        )
        """
        _response = self._raw_client.check_registration_invitation(
            invitation=invitation, request_options=request_options
        )
        return _response.data

    def register(
        self,
        *,
        email: LowerCaseEmailStr,
        password: str,
        confirm: typing.Optional[str] = OMIT,
        invitation: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeLog:
        """
        User registration

        Parameters
        ----------
        email : LowerCaseEmailStr

        password : str

        confirm : typing.Optional[str]
            Password confirmation

        invitation : typing.Optional[str]
            Invitation code

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeLog
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.auth.register(
            email="email",
            password="password",
        )
        """
        _response = self._raw_client.register(
            email=email, password=password, confirm=confirm, invitation=invitation, request_options=request_options
        )
        return _response.data

    def unregister_account(
        self, *, email: LowerCaseEmailStr, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeLog:
        """
        Parameters
        ----------
        email : LowerCaseEmailStr

        password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeLog
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.auth.unregister_account(
            email="email",
            password="password",
        )
        """
        _response = self._raw_client.unregister_account(email=email, password=password, request_options=request_options)
        return _response.data

    def register_phone(
        self,
        *,
        email: LowerCaseEmailStr,
        phone: PhoneNumberStr,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeRegisterPhoneNextPage:
        """
        user tries to verify phone number for 2 Factor Authentication when registering

        Parameters
        ----------
        email : LowerCaseEmailStr

        phone : PhoneNumberStr
            Phone number E.164, needed on the deployments with 2FA

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeRegisterPhoneNextPage
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.auth.register_phone(
            email="email",
            phone="phone",
        )
        """
        _response = self._raw_client.register_phone(email=email, phone=phone, request_options=request_options)
        return _response.data

    def phone_confirmation(
        self,
        *,
        email: LowerCaseEmailStr,
        phone: str,
        code: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeLog:
        """
        user enters 2 Factor Authentication code when registering

        Parameters
        ----------
        email : LowerCaseEmailStr

        phone : str
            Phone number E.164, needed on the deployments with 2FA

        code : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeLog
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.auth.phone_confirmation(
            email="email",
            phone="phone",
            code="code",
        )
        """
        _response = self._raw_client.phone_confirmation(
            email=email, phone=phone, code=code, request_options=request_options
        )
        return _response.data

    def login(
        self, *, email: LowerCaseEmailStr, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeLoginNextPage:
        """
        user logs in

        Parameters
        ----------
        email : LowerCaseEmailStr

        password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeLoginNextPage
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.auth.login(
            email="email",
            password="password",
        )
        """
        _response = self._raw_client.login(email=email, password=password, request_options=request_options)
        return _response.data

    def login2fa(
        self, *, email: LowerCaseEmailStr, code: str, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeLog:
        """
        user enters 2 Factor Authentication code when login in

        Parameters
        ----------
        email : LowerCaseEmailStr

        code : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeLog
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.auth.login2fa(
            email="email",
            code="code",
        )
        """
        _response = self._raw_client.login2fa(email=email, code=code, request_options=request_options)
        return _response.data

    def resend2fa_code(
        self,
        *,
        email: LowerCaseEmailStr,
        via: typing.Optional[Resend2FaBodyVia] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeLog:
        """
        Resends 2FA either via email or sms

        Parameters
        ----------
        email : LowerCaseEmailStr
            User email (identifier)

        via : typing.Optional[Resend2FaBodyVia]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeLog
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.auth.resend2fa_code(
            email="email",
        )
        """
        _response = self._raw_client.resend2fa_code(email=email, via=via, request_options=request_options)
        return _response.data

    def logout(
        self, *, client_session_id: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeLog:
        """
        user logout

        Parameters
        ----------
        client_session_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeLog
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.auth.logout()
        """
        _response = self._raw_client.logout(client_session_id=client_session_id, request_options=request_options)
        return _response.data

    def check_auth(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        checks whether user request is authenticated

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.auth.check_auth()
        """
        _response = self._raw_client.check_auth(request_options=request_options)
        return _response.data

    def initiate_reset_password(
        self, *, email: LowerCaseEmailStr, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeLog:
        """
        Parameters
        ----------
        email : LowerCaseEmailStr

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeLog
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.auth.initiate_reset_password(
            email="email",
        )
        """
        _response = self._raw_client.initiate_reset_password(email=email, request_options=request_options)
        return _response.data

    def complete_reset_password(
        self, code: str, *, password: str, confirm: str, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeLog:
        """
        Parameters
        ----------
        code : str

        password : str

        confirm : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeLog
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.auth.complete_reset_password(
            code="code",
            password="password",
            confirm="confirm",
        )
        """
        _response = self._raw_client.complete_reset_password(
            code, password=password, confirm=confirm, request_options=request_options
        )
        return _response.data

    def change_password(
        self, *, current: str, new: str, confirm: str, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeLog:
        """
        logged in user changes password

        Parameters
        ----------
        current : str

        new : str

        confirm : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeLog
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.auth.change_password(
            current="current",
            new="new",
            confirm="confirm",
        )
        """
        _response = self._raw_client.change_password(
            current=current, new=new, confirm=confirm, request_options=request_options
        )
        return _response.data

    def confirmation(self, code: str, *, request_options: typing.Optional[RequestOptions] = None) -> EnvelopeLog:
        """
        email link sent to user to confirm an action

        Parameters
        ----------
        code : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeLog
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.auth.confirmation(
            code="code",
        )
        """
        _response = self._raw_client.confirmation(code, request_options=request_options)
        return _response.data

    def create_captcha(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.auth.create_captcha()
        """
        _response = self._raw_client.create_captcha(request_options=request_options)
        return _response.data

    def list_api_keys(
        self,
        *,
        include_autogenerated: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeListApiKeyGet:
        """
        lists API keys by this user

        Parameters
        ----------
        include_autogenerated : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListApiKeyGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.auth.list_api_keys()
        """
        _response = self._raw_client.list_api_keys(
            include_autogenerated=include_autogenerated, request_options=request_options
        )
        return _response.data

    def create_api_key(
        self,
        *,
        display_name: str,
        expiration: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeApiKeyCreateResponse:
        """
        creates API keys to access public API

        Parameters
        ----------
        display_name : str

        expiration : typing.Optional[str]
            Time delta from creation time to expiration. If None, then it does not expire.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeApiKeyCreateResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.auth.create_api_key(
            display_name="displayName",
        )
        """
        _response = self._raw_client.create_api_key(
            display_name=display_name, expiration=expiration, request_options=request_options
        )
        return _response.data

    def get_api_key(
        self, api_key_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeApiKeyGet:
        """
        returns the API Key with the given ID

        Parameters
        ----------
        api_key_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeApiKeyGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.auth.get_api_key(
            api_key_id="api_key_id",
        )
        """
        _response = self._raw_client.get_api_key(api_key_id, request_options=request_options)
        return _response.data

    def delete_api_key(self, api_key_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        deletes the API key with the given ID

        Parameters
        ----------
        api_key_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.auth.delete_api_key(
            api_key_id="api_key_id",
        )
        """
        _response = self._raw_client.delete_api_key(api_key_id, request_options=request_options)
        return _response.data


class AsyncAuthClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAuthClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAuthClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAuthClient
        """
        return self._raw_client

    async def request_product_account(
        self,
        *,
        form: typing.Dict[str, typing.Any],
        captcha: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        form : typing.Dict[str, typing.Any]

        captcha : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.auth.request_product_account(
                form={
                    "address": "Infinite Loop",
                    "application": "Antenna_Design",
                    "city": "Washington",
                    "company": "EM Com",
                    "country": "Switzerland",
                    "description": "Description of something",
                    "email": "maxwel@email.com",
                    "eula": True,
                    "firstName": "James",
                    "hear": "Search_Engine",
                    "lastName": "Maxwel",
                    "phone": "+41 44 245 96 96",
                    "postalCode": "98001",
                    "privacyPolicy": True,
                },
                captcha="A12B34",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.request_product_account(
            form=form, captcha=captcha, request_options=request_options
        )
        return _response.data

    async def check_registration_invitation(
        self, *, invitation: str, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeInvitationInfo:
        """
        Check invitation and returns associated email or None

        Parameters
        ----------
        invitation : str
            Invitation code

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeInvitationInfo
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.auth.check_registration_invitation(
                invitation="invitation",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.check_registration_invitation(
            invitation=invitation, request_options=request_options
        )
        return _response.data

    async def register(
        self,
        *,
        email: LowerCaseEmailStr,
        password: str,
        confirm: typing.Optional[str] = OMIT,
        invitation: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeLog:
        """
        User registration

        Parameters
        ----------
        email : LowerCaseEmailStr

        password : str

        confirm : typing.Optional[str]
            Password confirmation

        invitation : typing.Optional[str]
            Invitation code

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeLog
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.auth.register(
                email="email",
                password="password",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.register(
            email=email, password=password, confirm=confirm, invitation=invitation, request_options=request_options
        )
        return _response.data

    async def unregister_account(
        self, *, email: LowerCaseEmailStr, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeLog:
        """
        Parameters
        ----------
        email : LowerCaseEmailStr

        password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeLog
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.auth.unregister_account(
                email="email",
                password="password",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.unregister_account(
            email=email, password=password, request_options=request_options
        )
        return _response.data

    async def register_phone(
        self,
        *,
        email: LowerCaseEmailStr,
        phone: PhoneNumberStr,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeRegisterPhoneNextPage:
        """
        user tries to verify phone number for 2 Factor Authentication when registering

        Parameters
        ----------
        email : LowerCaseEmailStr

        phone : PhoneNumberStr
            Phone number E.164, needed on the deployments with 2FA

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeRegisterPhoneNextPage
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.auth.register_phone(
                email="email",
                phone="phone",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.register_phone(email=email, phone=phone, request_options=request_options)
        return _response.data

    async def phone_confirmation(
        self,
        *,
        email: LowerCaseEmailStr,
        phone: str,
        code: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeLog:
        """
        user enters 2 Factor Authentication code when registering

        Parameters
        ----------
        email : LowerCaseEmailStr

        phone : str
            Phone number E.164, needed on the deployments with 2FA

        code : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeLog
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.auth.phone_confirmation(
                email="email",
                phone="phone",
                code="code",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.phone_confirmation(
            email=email, phone=phone, code=code, request_options=request_options
        )
        return _response.data

    async def login(
        self, *, email: LowerCaseEmailStr, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeLoginNextPage:
        """
        user logs in

        Parameters
        ----------
        email : LowerCaseEmailStr

        password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeLoginNextPage
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.auth.login(
                email="email",
                password="password",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.login(email=email, password=password, request_options=request_options)
        return _response.data

    async def login2fa(
        self, *, email: LowerCaseEmailStr, code: str, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeLog:
        """
        user enters 2 Factor Authentication code when login in

        Parameters
        ----------
        email : LowerCaseEmailStr

        code : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeLog
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.auth.login2fa(
                email="email",
                code="code",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.login2fa(email=email, code=code, request_options=request_options)
        return _response.data

    async def resend2fa_code(
        self,
        *,
        email: LowerCaseEmailStr,
        via: typing.Optional[Resend2FaBodyVia] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeLog:
        """
        Resends 2FA either via email or sms

        Parameters
        ----------
        email : LowerCaseEmailStr
            User email (identifier)

        via : typing.Optional[Resend2FaBodyVia]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeLog
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.auth.resend2fa_code(
                email="email",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.resend2fa_code(email=email, via=via, request_options=request_options)
        return _response.data

    async def logout(
        self, *, client_session_id: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeLog:
        """
        user logout

        Parameters
        ----------
        client_session_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeLog
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.auth.logout()


        asyncio.run(main())
        """
        _response = await self._raw_client.logout(client_session_id=client_session_id, request_options=request_options)
        return _response.data

    async def check_auth(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        checks whether user request is authenticated

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.auth.check_auth()


        asyncio.run(main())
        """
        _response = await self._raw_client.check_auth(request_options=request_options)
        return _response.data

    async def initiate_reset_password(
        self, *, email: LowerCaseEmailStr, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeLog:
        """
        Parameters
        ----------
        email : LowerCaseEmailStr

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeLog
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.auth.initiate_reset_password(
                email="email",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.initiate_reset_password(email=email, request_options=request_options)
        return _response.data

    async def complete_reset_password(
        self, code: str, *, password: str, confirm: str, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeLog:
        """
        Parameters
        ----------
        code : str

        password : str

        confirm : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeLog
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.auth.complete_reset_password(
                code="code",
                password="password",
                confirm="confirm",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.complete_reset_password(
            code, password=password, confirm=confirm, request_options=request_options
        )
        return _response.data

    async def change_password(
        self, *, current: str, new: str, confirm: str, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeLog:
        """
        logged in user changes password

        Parameters
        ----------
        current : str

        new : str

        confirm : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeLog
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.auth.change_password(
                current="current",
                new="new",
                confirm="confirm",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.change_password(
            current=current, new=new, confirm=confirm, request_options=request_options
        )
        return _response.data

    async def confirmation(self, code: str, *, request_options: typing.Optional[RequestOptions] = None) -> EnvelopeLog:
        """
        email link sent to user to confirm an action

        Parameters
        ----------
        code : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeLog
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.auth.confirmation(
                code="code",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.confirmation(code, request_options=request_options)
        return _response.data

    async def create_captcha(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.auth.create_captcha()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_captcha(request_options=request_options)
        return _response.data

    async def list_api_keys(
        self,
        *,
        include_autogenerated: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeListApiKeyGet:
        """
        lists API keys by this user

        Parameters
        ----------
        include_autogenerated : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListApiKeyGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.auth.list_api_keys()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_api_keys(
            include_autogenerated=include_autogenerated, request_options=request_options
        )
        return _response.data

    async def create_api_key(
        self,
        *,
        display_name: str,
        expiration: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeApiKeyCreateResponse:
        """
        creates API keys to access public API

        Parameters
        ----------
        display_name : str

        expiration : typing.Optional[str]
            Time delta from creation time to expiration. If None, then it does not expire.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeApiKeyCreateResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.auth.create_api_key(
                display_name="displayName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_api_key(
            display_name=display_name, expiration=expiration, request_options=request_options
        )
        return _response.data

    async def get_api_key(
        self, api_key_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeApiKeyGet:
        """
        returns the API Key with the given ID

        Parameters
        ----------
        api_key_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeApiKeyGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.auth.get_api_key(
                api_key_id="api_key_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_key(api_key_id, request_options=request_options)
        return _response.data

    async def delete_api_key(self, api_key_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        deletes the API key with the given ID

        Parameters
        ----------
        api_key_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.auth.delete_api_key(
                api_key_id="api_key_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_api_key(api_key_id, request_options=request_options)
        return _response.data

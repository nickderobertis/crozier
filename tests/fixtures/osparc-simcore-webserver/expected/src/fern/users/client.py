

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.address_line_safe_str import AddressLineSafeStr
from ..types.country_name_str import CountryNameStr
from ..types.display_safe_str import DisplaySafeStr
from ..types.envelope_list_my_permission_get import EnvelopeListMyPermissionGet
from ..types.envelope_list_my_token_get import EnvelopeListMyTokenGet
from ..types.envelope_list_user_account_get import EnvelopeListUserAccountGet
from ..types.envelope_list_user_account_product_option_get import EnvelopeListUserAccountProductOptionGet
from ..types.envelope_list_user_get import EnvelopeListUserGet
from ..types.envelope_list_user_notification import EnvelopeListUserNotification
from ..types.envelope_my_function_permissions_get import EnvelopeMyFunctionPermissionsGet
from ..types.envelope_my_profile_rest_get import EnvelopeMyProfileRestGet
from ..types.envelope_my_token_get import EnvelopeMyTokenGet
from ..types.envelope_user_account_get import EnvelopeUserAccountGet
from ..types.envelope_user_account_preview_approval_get import EnvelopeUserAccountPreviewApprovalGet
from ..types.envelope_user_account_preview_rejection_get import EnvelopeUserAccountPreviewRejectionGet
from ..types.first_name_str import FirstNameStr
from ..types.glob_pattern_safe_str import GlobPatternSafeStr
from ..types.group_id_int import GroupIdInt
from ..types.invitation_details import InvitationDetails
from ..types.last_name_str import LastNameStr
from ..types.lower_case_email_str import LowerCaseEmailStr
from ..types.message_content import MessageContent
from ..types.my_profile_address_rest_patch import MyProfileAddressRestPatch
from ..types.my_profile_privacy_patch import MyProfilePrivacyPatch
from ..types.notification_category import NotificationCategory
from ..types.page_user_account_get import PageUserAccountGet
from ..types.phone_number_str import PhoneNumberStr
from ..types.postal_code_safe_str import PostalCodeSafeStr
from ..types.search_pattern_safe_str import SearchPatternSafeStr
from ..types.supported_locale import SupportedLocale
from ..types.user_id_int import UserIdInt
from ..types.user_name_safe_id import UserNameSafeId
from .raw_client import AsyncRawUsersClient, RawUsersClient
from .types.list_users_accounts_request_review_status import ListUsersAccountsRequestReviewStatus
from .types.user_notification_create_product import UserNotificationCreateProduct
from .types.user_notification_create_resource_id import UserNotificationCreateResourceId


OMIT = typing.cast(typing.Any, ...)


class UsersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUsersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUsersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUsersClient
        """
        return self._raw_client

    def get_my_profile(self, *, request_options: typing.Optional[RequestOptions] = None) -> EnvelopeMyProfileRestGet:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeMyProfileRestGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.get_my_profile()
        """
        _response = self._raw_client.get_my_profile(request_options=request_options)
        return _response.data

    def update_my_profile(
        self,
        *,
        first_name: typing.Optional[FirstNameStr] = OMIT,
        last_name: typing.Optional[LastNameStr] = OMIT,
        user_name: typing.Optional[UserNameSafeId] = OMIT,
        language: typing.Optional[SupportedLocale] = OMIT,
        privacy: typing.Optional[MyProfilePrivacyPatch] = OMIT,
        contact: typing.Optional[MyProfileAddressRestPatch] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        first_name : typing.Optional[FirstNameStr]

        last_name : typing.Optional[LastNameStr]

        user_name : typing.Optional[UserNameSafeId]

        language : typing.Optional[SupportedLocale]
            Persisted UI/communications language. The user owns and can edit it directly.

        privacy : typing.Optional[MyProfilePrivacyPatch]

        contact : typing.Optional[MyProfileAddressRestPatch]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.update_my_profile()
        """
        _response = self._raw_client.update_my_profile(
            first_name=first_name,
            last_name=last_name,
            user_name=user_name,
            language=language,
            privacy=privacy,
            contact=contact,
            request_options=request_options,
        )
        return _response.data

    def my_phone_register(
        self, *, phone: PhoneNumberStr, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Starts the phone registration process

        Parameters
        ----------
        phone : PhoneNumberStr
            Phone number to register

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Phone registration initiated

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.my_phone_register(
            phone="phone",
        )
        """
        _response = self._raw_client.my_phone_register(phone=phone, request_options=request_options)
        return _response.data

    def my_phone_resend(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Resends the phone registration code

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Phone code resent

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.my_phone_resend()
        """
        _response = self._raw_client.my_phone_resend(request_options=request_options)
        return _response.data

    def my_phone_confirm(self, *, code: str, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Confirms the phone registration

        Parameters
        ----------
        code : str
            Alphanumeric confirmation code

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.my_phone_confirm(
            code="code",
        )
        """
        _response = self._raw_client.my_phone_confirm(code=code, request_options=request_options)
        return _response.data

    def set_frontend_preference(
        self, preference_id: str, *, value: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        preference_id : str

        value : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.set_frontend_preference(
            preference_id="preference_id",
            value={"key": "value"},
        )
        """
        _response = self._raw_client.set_frontend_preference(
            preference_id, value=value, request_options=request_options
        )
        return _response.data

    def list_tokens(self, *, request_options: typing.Optional[RequestOptions] = None) -> EnvelopeListMyTokenGet:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListMyTokenGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.list_tokens()
        """
        _response = self._raw_client.list_tokens(request_options=request_options)
        return _response.data

    def create_token(
        self,
        *,
        service: str,
        token_key: str,
        token_secret: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeMyTokenGet:
        """
        Parameters
        ----------
        service : str
            uniquely identifies the service where this token is used

        token_key : str

        token_secret : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeMyTokenGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.create_token(
            service="service",
            token_key="token_key",
            token_secret="token_secret",
        )
        """
        _response = self._raw_client.create_token(
            service=service, token_key=token_key, token_secret=token_secret, request_options=request_options
        )
        return _response.data

    def get_token(self, service: str, *, request_options: typing.Optional[RequestOptions] = None) -> EnvelopeMyTokenGet:
        """
        Parameters
        ----------
        service : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeMyTokenGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.get_token(
            service="service",
        )
        """
        _response = self._raw_client.get_token(service, request_options=request_options)
        return _response.data

    def delete_token(self, service: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        service : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.delete_token(
            service="service",
        )
        """
        _response = self._raw_client.delete_token(service, request_options=request_options)
        return _response.data

    def list_user_notifications(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeListUserNotification:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListUserNotification
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.list_user_notifications()
        """
        _response = self._raw_client.list_user_notifications(request_options=request_options)
        return _response.data

    def create_user_notification(
        self,
        *,
        user_id: UserIdInt,
        category: NotificationCategory,
        actionable_path: str,
        title: str,
        text: str,
        date: dt.datetime,
        product: typing.Optional[UserNotificationCreateProduct] = OMIT,
        resource_id: typing.Optional[UserNotificationCreateResourceId] = OMIT,
        user_from_id: typing.Optional[UserIdInt] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        user_id : UserIdInt

        category : NotificationCategory

        actionable_path : str

        title : str

        text : str

        date : dt.datetime

        product : typing.Optional[UserNotificationCreateProduct]

        resource_id : typing.Optional[UserNotificationCreateResourceId]

        user_from_id : typing.Optional[UserIdInt]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import datetime

        from fern import FernApi, NotificationCategory

        client = FernApi()
        client.users.create_user_notification(
            user_id=1,
            category=NotificationCategory.NEW_ORGANIZATION,
            actionable_path="actionable_path",
            title="title",
            text="text",
            date=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
        )
        """
        _response = self._raw_client.create_user_notification(
            user_id=user_id,
            category=category,
            actionable_path=actionable_path,
            title=title,
            text=text,
            date=date,
            product=product,
            resource_id=resource_id,
            user_from_id=user_from_id,
            request_options=request_options,
        )
        return _response.data

    def mark_notification_as_read(
        self, notification_id: str, *, read: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        notification_id : str

        read : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.mark_notification_as_read(
            notification_id="notification_id",
            read=True,
        )
        """
        _response = self._raw_client.mark_notification_as_read(
            notification_id, read=read, request_options=request_options
        )
        return _response.data

    def list_user_permissions(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeListMyPermissionGet:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListMyPermissionGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.list_user_permissions()
        """
        _response = self._raw_client.list_user_permissions(request_options=request_options)
        return _response.data

    def list_user_functions_permissions(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeMyFunctionPermissionsGet:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeMyFunctionPermissionsGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.list_user_functions_permissions()
        """
        _response = self._raw_client.list_user_functions_permissions(request_options=request_options)
        return _response.data

    def search_users(
        self,
        *,
        match: SearchPatternSafeStr,
        limit: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeListUserGet:
        """
        Search among users who are publicly visible to the caller (i.e., me) based on their privacy settings.

        Parameters
        ----------
        match : SearchPatternSafeStr
            Search string to match with usernames and public profiles (e.g. emails, first/last name)

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListUserGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.search_users(
            match="match",
        )
        """
        _response = self._raw_client.search_users(match=match, limit=limit, request_options=request_options)
        return _response.data

    def list_users_accounts(
        self,
        *,
        order_by: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        review_status: typing.Optional[ListUsersAccountsRequestReviewStatus] = None,
        registered: typing.Optional[bool] = None,
        product_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageUserAccountGet:
        """
        Parameters
        ----------
        order_by : typing.Optional[str]
            Comma-separated list of field names for sorting. Prefix with '-' for descending, '+' or no prefix for ascending.

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        review_status : typing.Optional[ListUsersAccountsRequestReviewStatus]

        registered : typing.Optional[bool]

        product_name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageUserAccountGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.list_users_accounts(
            order_by="-name,email",
        )
        """
        _response = self._raw_client.list_users_accounts(
            order_by=order_by,
            limit=limit,
            offset=offset,
            review_status=review_status,
            registered=registered,
            product_name=product_name,
            request_options=request_options,
        )
        return _response.data

    def approve_user_account(
        self,
        *,
        email: str,
        bcc_emails: typing.Optional[typing.Sequence[str]] = OMIT,
        invitation_url: typing.Optional[str] = OMIT,
        message_content: typing.Optional[MessageContent] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        email : str

        bcc_emails : typing.Optional[typing.Sequence[str]]

        invitation_url : typing.Optional[str]

        message_content : typing.Optional[MessageContent]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.approve_user_account(
            email="email",
        )
        """
        _response = self._raw_client.approve_user_account(
            email=email,
            bcc_emails=bcc_emails,
            invitation_url=invitation_url,
            message_content=message_content,
            request_options=request_options,
        )
        return _response.data

    def preview_approval_user_account(
        self, *, email: str, invitation: InvitationDetails, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeUserAccountPreviewApprovalGet:
        """
        Parameters
        ----------
        email : str

        invitation : InvitationDetails

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeUserAccountPreviewApprovalGet
            Successful Response

        Examples
        --------
        from fern import FernApi, InvitationDetails

        client = FernApi()
        client.users.preview_approval_user_account(
            email="email",
            invitation=InvitationDetails(),
        )
        """
        _response = self._raw_client.preview_approval_user_account(
            email=email, invitation=invitation, request_options=request_options
        )
        return _response.data

    def reject_user_account(
        self,
        *,
        email: str,
        bcc_emails: typing.Optional[typing.Sequence[str]] = OMIT,
        message_content: typing.Optional[MessageContent] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        email : str

        bcc_emails : typing.Optional[typing.Sequence[str]]

        message_content : typing.Optional[MessageContent]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.reject_user_account(
            email="email",
        )
        """
        _response = self._raw_client.reject_user_account(
            email=email, bcc_emails=bcc_emails, message_content=message_content, request_options=request_options
        )
        return _response.data

    def preview_rejection_user_account(
        self, *, email: str, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeUserAccountPreviewRejectionGet:
        """
        Parameters
        ----------
        email : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeUserAccountPreviewRejectionGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.preview_rejection_user_account(
            email="email",
        )
        """
        _response = self._raw_client.preview_rejection_user_account(email=email, request_options=request_options)
        return _response.data

    def search_user_accounts(
        self,
        *,
        email: typing.Optional[GlobPatternSafeStr] = None,
        primary_group_id: typing.Optional[GroupIdInt] = None,
        user_name: typing.Optional[GlobPatternSafeStr] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeListUserAccountGet:
        """
        Parameters
        ----------
        email : typing.Optional[GlobPatternSafeStr]

        primary_group_id : typing.Optional[GroupIdInt]

        user_name : typing.Optional[GlobPatternSafeStr]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListUserAccountGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.search_user_accounts()
        """
        _response = self._raw_client.search_user_accounts(
            email=email, primary_group_id=primary_group_id, user_name=user_name, request_options=request_options
        )
        return _response.data

    def move_user_account(
        self,
        *,
        pre_registration_id: int,
        new_product_name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        pre_registration_id : int

        new_product_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.move_user_account(
            pre_registration_id=1,
            new_product_name="newProductName",
        )
        """
        _response = self._raw_client.move_user_account(
            pre_registration_id=pre_registration_id, new_product_name=new_product_name, request_options=request_options
        )
        return _response.data

    def list_products_for_user_accounts(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeListUserAccountProductOptionGet:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListUserAccountProductOptionGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.list_products_for_user_accounts()
        """
        _response = self._raw_client.list_products_for_user_accounts(request_options=request_options)
        return _response.data

    def pre_register_user_account(
        self,
        *,
        first_name: FirstNameStr,
        last_name: LastNameStr,
        email: LowerCaseEmailStr,
        address: AddressLineSafeStr,
        city: DisplaySafeStr,
        postal_code: PostalCodeSafeStr,
        country: CountryNameStr,
        institution: typing.Optional[DisplaySafeStr] = OMIT,
        phone: typing.Optional[PhoneNumberStr] = OMIT,
        state: typing.Optional[DisplaySafeStr] = OMIT,
        extras: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeUserAccountGet:
        """
        Parameters
        ----------
        first_name : FirstNameStr

        last_name : LastNameStr

        email : LowerCaseEmailStr

        address : AddressLineSafeStr

        city : DisplaySafeStr

        postal_code : PostalCodeSafeStr

        country : CountryNameStr

        institution : typing.Optional[DisplaySafeStr]
            company, university, ...

        phone : typing.Optional[PhoneNumberStr]

        state : typing.Optional[DisplaySafeStr]

        extras : typing.Optional[typing.Dict[str, typing.Any]]
            Keeps extra information provided in the request form.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeUserAccountGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.pre_register_user_account(
            first_name="firstName",
            last_name="lastName",
            email="email",
            address="address",
            city="city",
            postal_code="postalCode",
            country="country",
        )
        """
        _response = self._raw_client.pre_register_user_account(
            first_name=first_name,
            last_name=last_name,
            email=email,
            address=address,
            city=city,
            postal_code=postal_code,
            country=country,
            institution=institution,
            phone=phone,
            state=state,
            extras=extras,
            request_options=request_options,
        )
        return _response.data


class AsyncUsersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUsersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUsersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUsersClient
        """
        return self._raw_client

    async def get_my_profile(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeMyProfileRestGet:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeMyProfileRestGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.get_my_profile()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_my_profile(request_options=request_options)
        return _response.data

    async def update_my_profile(
        self,
        *,
        first_name: typing.Optional[FirstNameStr] = OMIT,
        last_name: typing.Optional[LastNameStr] = OMIT,
        user_name: typing.Optional[UserNameSafeId] = OMIT,
        language: typing.Optional[SupportedLocale] = OMIT,
        privacy: typing.Optional[MyProfilePrivacyPatch] = OMIT,
        contact: typing.Optional[MyProfileAddressRestPatch] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        first_name : typing.Optional[FirstNameStr]

        last_name : typing.Optional[LastNameStr]

        user_name : typing.Optional[UserNameSafeId]

        language : typing.Optional[SupportedLocale]
            Persisted UI/communications language. The user owns and can edit it directly.

        privacy : typing.Optional[MyProfilePrivacyPatch]

        contact : typing.Optional[MyProfileAddressRestPatch]

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
            await client.users.update_my_profile()


        asyncio.run(main())
        """
        _response = await self._raw_client.update_my_profile(
            first_name=first_name,
            last_name=last_name,
            user_name=user_name,
            language=language,
            privacy=privacy,
            contact=contact,
            request_options=request_options,
        )
        return _response.data

    async def my_phone_register(
        self, *, phone: PhoneNumberStr, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Starts the phone registration process

        Parameters
        ----------
        phone : PhoneNumberStr
            Phone number to register

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Phone registration initiated

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.my_phone_register(
                phone="phone",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.my_phone_register(phone=phone, request_options=request_options)
        return _response.data

    async def my_phone_resend(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Resends the phone registration code

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Phone code resent

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.my_phone_resend()


        asyncio.run(main())
        """
        _response = await self._raw_client.my_phone_resend(request_options=request_options)
        return _response.data

    async def my_phone_confirm(self, *, code: str, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Confirms the phone registration

        Parameters
        ----------
        code : str
            Alphanumeric confirmation code

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
            await client.users.my_phone_confirm(
                code="code",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.my_phone_confirm(code=code, request_options=request_options)
        return _response.data

    async def set_frontend_preference(
        self, preference_id: str, *, value: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        preference_id : str

        value : typing.Any

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
            await client.users.set_frontend_preference(
                preference_id="preference_id",
                value={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_frontend_preference(
            preference_id, value=value, request_options=request_options
        )
        return _response.data

    async def list_tokens(self, *, request_options: typing.Optional[RequestOptions] = None) -> EnvelopeListMyTokenGet:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListMyTokenGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.list_tokens()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_tokens(request_options=request_options)
        return _response.data

    async def create_token(
        self,
        *,
        service: str,
        token_key: str,
        token_secret: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeMyTokenGet:
        """
        Parameters
        ----------
        service : str
            uniquely identifies the service where this token is used

        token_key : str

        token_secret : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeMyTokenGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.create_token(
                service="service",
                token_key="token_key",
                token_secret="token_secret",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_token(
            service=service, token_key=token_key, token_secret=token_secret, request_options=request_options
        )
        return _response.data

    async def get_token(
        self, service: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeMyTokenGet:
        """
        Parameters
        ----------
        service : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeMyTokenGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.get_token(
                service="service",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_token(service, request_options=request_options)
        return _response.data

    async def delete_token(self, service: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        service : str

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
            await client.users.delete_token(
                service="service",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_token(service, request_options=request_options)
        return _response.data

    async def list_user_notifications(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeListUserNotification:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListUserNotification
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.list_user_notifications()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_user_notifications(request_options=request_options)
        return _response.data

    async def create_user_notification(
        self,
        *,
        user_id: UserIdInt,
        category: NotificationCategory,
        actionable_path: str,
        title: str,
        text: str,
        date: dt.datetime,
        product: typing.Optional[UserNotificationCreateProduct] = OMIT,
        resource_id: typing.Optional[UserNotificationCreateResourceId] = OMIT,
        user_from_id: typing.Optional[UserIdInt] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        user_id : UserIdInt

        category : NotificationCategory

        actionable_path : str

        title : str

        text : str

        date : dt.datetime

        product : typing.Optional[UserNotificationCreateProduct]

        resource_id : typing.Optional[UserNotificationCreateResourceId]

        user_from_id : typing.Optional[UserIdInt]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi, NotificationCategory

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.create_user_notification(
                user_id=1,
                category=NotificationCategory.NEW_ORGANIZATION,
                actionable_path="actionable_path",
                title="title",
                text="text",
                date=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_user_notification(
            user_id=user_id,
            category=category,
            actionable_path=actionable_path,
            title=title,
            text=text,
            date=date,
            product=product,
            resource_id=resource_id,
            user_from_id=user_from_id,
            request_options=request_options,
        )
        return _response.data

    async def mark_notification_as_read(
        self, notification_id: str, *, read: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        notification_id : str

        read : bool

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
            await client.users.mark_notification_as_read(
                notification_id="notification_id",
                read=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.mark_notification_as_read(
            notification_id, read=read, request_options=request_options
        )
        return _response.data

    async def list_user_permissions(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeListMyPermissionGet:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListMyPermissionGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.list_user_permissions()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_user_permissions(request_options=request_options)
        return _response.data

    async def list_user_functions_permissions(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeMyFunctionPermissionsGet:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeMyFunctionPermissionsGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.list_user_functions_permissions()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_user_functions_permissions(request_options=request_options)
        return _response.data

    async def search_users(
        self,
        *,
        match: SearchPatternSafeStr,
        limit: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeListUserGet:
        """
        Search among users who are publicly visible to the caller (i.e., me) based on their privacy settings.

        Parameters
        ----------
        match : SearchPatternSafeStr
            Search string to match with usernames and public profiles (e.g. emails, first/last name)

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListUserGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.search_users(
                match="match",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.search_users(match=match, limit=limit, request_options=request_options)
        return _response.data

    async def list_users_accounts(
        self,
        *,
        order_by: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        review_status: typing.Optional[ListUsersAccountsRequestReviewStatus] = None,
        registered: typing.Optional[bool] = None,
        product_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageUserAccountGet:
        """
        Parameters
        ----------
        order_by : typing.Optional[str]
            Comma-separated list of field names for sorting. Prefix with '-' for descending, '+' or no prefix for ascending.

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        review_status : typing.Optional[ListUsersAccountsRequestReviewStatus]

        registered : typing.Optional[bool]

        product_name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageUserAccountGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.list_users_accounts(
                order_by="-name,email",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_users_accounts(
            order_by=order_by,
            limit=limit,
            offset=offset,
            review_status=review_status,
            registered=registered,
            product_name=product_name,
            request_options=request_options,
        )
        return _response.data

    async def approve_user_account(
        self,
        *,
        email: str,
        bcc_emails: typing.Optional[typing.Sequence[str]] = OMIT,
        invitation_url: typing.Optional[str] = OMIT,
        message_content: typing.Optional[MessageContent] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        email : str

        bcc_emails : typing.Optional[typing.Sequence[str]]

        invitation_url : typing.Optional[str]

        message_content : typing.Optional[MessageContent]

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
            await client.users.approve_user_account(
                email="email",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.approve_user_account(
            email=email,
            bcc_emails=bcc_emails,
            invitation_url=invitation_url,
            message_content=message_content,
            request_options=request_options,
        )
        return _response.data

    async def preview_approval_user_account(
        self, *, email: str, invitation: InvitationDetails, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeUserAccountPreviewApprovalGet:
        """
        Parameters
        ----------
        email : str

        invitation : InvitationDetails

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeUserAccountPreviewApprovalGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, InvitationDetails

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.preview_approval_user_account(
                email="email",
                invitation=InvitationDetails(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.preview_approval_user_account(
            email=email, invitation=invitation, request_options=request_options
        )
        return _response.data

    async def reject_user_account(
        self,
        *,
        email: str,
        bcc_emails: typing.Optional[typing.Sequence[str]] = OMIT,
        message_content: typing.Optional[MessageContent] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        email : str

        bcc_emails : typing.Optional[typing.Sequence[str]]

        message_content : typing.Optional[MessageContent]

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
            await client.users.reject_user_account(
                email="email",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.reject_user_account(
            email=email, bcc_emails=bcc_emails, message_content=message_content, request_options=request_options
        )
        return _response.data

    async def preview_rejection_user_account(
        self, *, email: str, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeUserAccountPreviewRejectionGet:
        """
        Parameters
        ----------
        email : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeUserAccountPreviewRejectionGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.preview_rejection_user_account(
                email="email",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.preview_rejection_user_account(email=email, request_options=request_options)
        return _response.data

    async def search_user_accounts(
        self,
        *,
        email: typing.Optional[GlobPatternSafeStr] = None,
        primary_group_id: typing.Optional[GroupIdInt] = None,
        user_name: typing.Optional[GlobPatternSafeStr] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeListUserAccountGet:
        """
        Parameters
        ----------
        email : typing.Optional[GlobPatternSafeStr]

        primary_group_id : typing.Optional[GroupIdInt]

        user_name : typing.Optional[GlobPatternSafeStr]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListUserAccountGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.search_user_accounts()


        asyncio.run(main())
        """
        _response = await self._raw_client.search_user_accounts(
            email=email, primary_group_id=primary_group_id, user_name=user_name, request_options=request_options
        )
        return _response.data

    async def move_user_account(
        self,
        *,
        pre_registration_id: int,
        new_product_name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        pre_registration_id : int

        new_product_name : str

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
            await client.users.move_user_account(
                pre_registration_id=1,
                new_product_name="newProductName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.move_user_account(
            pre_registration_id=pre_registration_id, new_product_name=new_product_name, request_options=request_options
        )
        return _response.data

    async def list_products_for_user_accounts(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeListUserAccountProductOptionGet:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListUserAccountProductOptionGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.list_products_for_user_accounts()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_products_for_user_accounts(request_options=request_options)
        return _response.data

    async def pre_register_user_account(
        self,
        *,
        first_name: FirstNameStr,
        last_name: LastNameStr,
        email: LowerCaseEmailStr,
        address: AddressLineSafeStr,
        city: DisplaySafeStr,
        postal_code: PostalCodeSafeStr,
        country: CountryNameStr,
        institution: typing.Optional[DisplaySafeStr] = OMIT,
        phone: typing.Optional[PhoneNumberStr] = OMIT,
        state: typing.Optional[DisplaySafeStr] = OMIT,
        extras: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeUserAccountGet:
        """
        Parameters
        ----------
        first_name : FirstNameStr

        last_name : LastNameStr

        email : LowerCaseEmailStr

        address : AddressLineSafeStr

        city : DisplaySafeStr

        postal_code : PostalCodeSafeStr

        country : CountryNameStr

        institution : typing.Optional[DisplaySafeStr]
            company, university, ...

        phone : typing.Optional[PhoneNumberStr]

        state : typing.Optional[DisplaySafeStr]

        extras : typing.Optional[typing.Dict[str, typing.Any]]
            Keeps extra information provided in the request form.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeUserAccountGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.pre_register_user_account(
                first_name="firstName",
                last_name="lastName",
                email="email",
                address="address",
                city="city",
                postal_code="postalCode",
                country="country",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.pre_register_user_account(
            first_name=first_name,
            last_name=last_name,
            email=email,
            address=address,
            city=city,
            postal_code=postal_code,
            country=country,
            institution=institution,
            phone=phone,
            state=state,
            extras=extras,
            request_options=request_options,
        )
        return _response.data

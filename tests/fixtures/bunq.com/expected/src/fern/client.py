

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .attachment.client import AsyncAttachmentClient, AttachmentClient
    from .attachment_public.client import AsyncAttachmentPublicClient, AttachmentPublicClient
    from .avatar.client import AsyncAvatarClient, AvatarClient
    from .billing_contract_subscription.client import (
        AsyncBillingContractSubscriptionClient,
        BillingContractSubscriptionClient,
    )
    from .bunqme_fundraiser_profile.client import AsyncBunqmeFundraiserProfileClient, BunqmeFundraiserProfileClient
    from .bunqme_fundraiser_result.client import AsyncBunqmeFundraiserResultClient, BunqmeFundraiserResultClient
    from .bunqme_tab.client import AsyncBunqmeTabClient, BunqmeTabClient
    from .bunqme_tab_result_response.client import AsyncBunqmeTabResultResponseClient, BunqmeTabResultResponseClient
    from .callback_url.client import AsyncCallbackUrlClient, CallbackUrlClient
    from .card.client import AsyncCardClient, CardClient
    from .card_batch.client import AsyncCardBatchClient, CardBatchClient
    from .card_batch_replace.client import AsyncCardBatchReplaceClient, CardBatchReplaceClient
    from .card_credit.client import AsyncCardCreditClient, CardCreditClient
    from .card_debit.client import AsyncCardDebitClient, CardDebitClient
    from .card_name.client import AsyncCardNameClient, CardNameClient
    from .certificate_pinned.client import AsyncCertificatePinnedClient, CertificatePinnedClient
    from .challenge_request.client import AsyncChallengeRequestClient, ChallengeRequestClient
    from .company.client import AsyncCompanyClient, CompanyClient
    from .confirmation_of_funds.client import AsyncConfirmationOfFundsClient, ConfirmationOfFundsClient
    from .content.client import AsyncContentClient, ContentClient
    from .credential_password_ip.client import AsyncCredentialPasswordIpClient, CredentialPasswordIpClient
    from .currency_cloud_beneficiary.client import AsyncCurrencyCloudBeneficiaryClient, CurrencyCloudBeneficiaryClient
    from .currency_cloud_beneficiary_requirement.client import (
        AsyncCurrencyCloudBeneficiaryRequirementClient,
        CurrencyCloudBeneficiaryRequirementClient,
    )
    from .currency_cloud_payment_quote.client import (
        AsyncCurrencyCloudPaymentQuoteClient,
        CurrencyCloudPaymentQuoteClient,
    )
    from .currency_conversion.client import AsyncCurrencyConversionClient, CurrencyConversionClient
    from .currency_conversion_quote.client import AsyncCurrencyConversionQuoteClient, CurrencyConversionQuoteClient
    from .customer_statement.client import AsyncCustomerStatementClient, CustomerStatementClient
    from .definition.client import AsyncDefinitionClient, DefinitionClient
    from .device.client import AsyncDeviceClient, DeviceClient
    from .device_server.client import AsyncDeviceServerClient, DeviceServerClient
    from .draft_payment.client import AsyncDraftPaymentClient, DraftPaymentClient
    from .event.client import AsyncEventClient, EventClient
    from .export_annual_overview.client import AsyncExportAnnualOverviewClient, ExportAnnualOverviewClient
    from .export_rib.client import AsyncExportRibClient, ExportRibClient
    from .export_statement_card.client import AsyncExportStatementCardClient, ExportStatementCardClient
    from .export_statement_card_csv.client import AsyncExportStatementCardCsvClient, ExportStatementCardCsvClient
    from .export_statement_card_pdf.client import AsyncExportStatementCardPdfClient, ExportStatementCardPdfClient
    from .feature_announcement.client import AsyncFeatureAnnouncementClient, FeatureAnnouncementClient
    from .generated_cvc2.client import AsyncGeneratedCvc2Client, GeneratedCvc2Client
    from .ideal_merchant_transaction.client import AsyncIdealMerchantTransactionClient, IdealMerchantTransactionClient
    from .insight_preference_date.client import AsyncInsightPreferenceDateClient, InsightPreferenceDateClient
    from .insights.client import AsyncInsightsClient, InsightsClient
    from .insights_search.client import AsyncInsightsSearchClient, InsightsSearchClient
    from .installation.client import AsyncInstallationClient, InstallationClient
    from .instance.client import AsyncInstanceClient, InstanceClient
    from .invoice.client import AsyncInvoiceClient, InvoiceClient
    from .ip.client import AsyncIpClient, IpClient
    from .legal_name.client import AsyncLegalNameClient, LegalNameClient
    from .limit.client import AsyncLimitClient, LimitClient
    from .mastercard_action.client import AsyncMastercardActionClient, MastercardActionClient
    from .monetary_account.client import AsyncMonetaryAccountClient, MonetaryAccountClient
    from .monetary_account_bank.client import AsyncMonetaryAccountBankClient, MonetaryAccountBankClient
    from .monetary_account_external.client import AsyncMonetaryAccountExternalClient, MonetaryAccountExternalClient
    from .monetary_account_joint.client import AsyncMonetaryAccountJointClient, MonetaryAccountJointClient
    from .monetary_account_savings.client import AsyncMonetaryAccountSavingsClient, MonetaryAccountSavingsClient
    from .name.client import AsyncNameClient, NameClient
    from .note_attachment.client import AsyncNoteAttachmentClient, NoteAttachmentClient
    from .note_text.client import AsyncNoteTextClient, NoteTextClient
    from .notification_filter_email.client import AsyncNotificationFilterEmailClient, NotificationFilterEmailClient
    from .notification_filter_push.client import AsyncNotificationFilterPushClient, NotificationFilterPushClient
    from .notification_filter_url.client import AsyncNotificationFilterUrlClient, NotificationFilterUrlClient
    from .oauth_client.client import AsyncOauthClientClient, OauthClientClient
    from .payment.client import AsyncPaymentClient, PaymentClient
    from .payment_auto_allocate.client import AsyncPaymentAutoAllocateClient, PaymentAutoAllocateClient
    from .payment_batch.client import AsyncPaymentBatchClient, PaymentBatchClient
    from .payment_service_provider_credential.client import (
        AsyncPaymentServiceProviderCredentialClient,
        PaymentServiceProviderCredentialClient,
    )
    from .payment_service_provider_draft_payment.client import (
        AsyncPaymentServiceProviderDraftPaymentClient,
        PaymentServiceProviderDraftPaymentClient,
    )
    from .pdf_content.client import AsyncPdfContentClient, PdfContentClient
    from .registry_settlement.client import AsyncRegistrySettlementClient, RegistrySettlementClient
    from .replace.client import AsyncReplaceClient, ReplaceClient
    from .request_inquiry.client import AsyncRequestInquiryClient, RequestInquiryClient
    from .request_inquiry_batch.client import AsyncRequestInquiryBatchClient, RequestInquiryBatchClient
    from .request_response.client import AsyncRequestResponseClient, RequestResponseClient
    from .reward.client import AsyncRewardClient, RewardClient
    from .reward_recipient.client import AsyncRewardRecipientClient, RewardRecipientClient
    from .reward_sender.client import AsyncRewardSenderClient, RewardSenderClient
    from .sandbox_user_company.client import AsyncSandboxUserCompanyClient, SandboxUserCompanyClient
    from .sandbox_user_person.client import AsyncSandboxUserPersonClient, SandboxUserPersonClient
    from .schedule.client import AsyncScheduleClient, ScheduleClient
    from .schedule_instance.client import AsyncScheduleInstanceClient, ScheduleInstanceClient
    from .schedule_payment.client import AsyncSchedulePaymentClient, SchedulePaymentClient
    from .schedule_payment_batch.client import AsyncSchedulePaymentBatchClient, SchedulePaymentBatchClient
    from .server_error.client import AsyncServerErrorClient, ServerErrorClient
    from .server_public_key.client import AsyncServerPublicKeyClient, ServerPublicKeyClient
    from .session.client import AsyncSessionClient, SessionClient
    from .session_server.client import AsyncSessionServerClient, SessionServerClient
    from .share_invite_monetary_account_inquiry.client import (
        AsyncShareInviteMonetaryAccountInquiryClient,
        ShareInviteMonetaryAccountInquiryClient,
    )
    from .share_invite_monetary_account_response.client import (
        AsyncShareInviteMonetaryAccountResponseClient,
        ShareInviteMonetaryAccountResponseClient,
    )
    from .sofort_merchant_transaction.client import (
        AsyncSofortMerchantTransactionClient,
        SofortMerchantTransactionClient,
    )
    from .statement.client import AsyncStatementClient, StatementClient
    from .switch_service_payment.client import AsyncSwitchServicePaymentClient, SwitchServicePaymentClient
    from .token_qr_request_ideal.client import AsyncTokenQrRequestIdealClient, TokenQrRequestIdealClient
    from .token_qr_request_sofort.client import AsyncTokenQrRequestSofortClient, TokenQrRequestSofortClient
    from .transferwise_currency.client import AsyncTransferwiseCurrencyClient, TransferwiseCurrencyClient
    from .transferwise_quote.client import AsyncTransferwiseQuoteClient, TransferwiseQuoteClient
    from .transferwise_quote_temporary.client import (
        AsyncTransferwiseQuoteTemporaryClient,
        TransferwiseQuoteTemporaryClient,
    )
    from .transferwise_recipient.client import AsyncTransferwiseRecipientClient, TransferwiseRecipientClient
    from .transferwise_recipient_requirement.client import (
        AsyncTransferwiseRecipientRequirementClient,
        TransferwiseRecipientRequirementClient,
    )
    from .transferwise_transfer.client import AsyncTransferwiseTransferClient, TransferwiseTransferClient
    from .transferwise_transfer_requirement.client import (
        AsyncTransferwiseTransferRequirementClient,
        TransferwiseTransferRequirementClient,
    )
    from .transferwise_user.client import AsyncTransferwiseUserClient, TransferwiseUserClient
    from .translink_transaction.client import AsyncTranslinkTransactionClient, TranslinkTransactionClient
    from .tree_progress.client import AsyncTreeProgressClient, TreeProgressClient
    from .user.client import AsyncUserClient, UserClient
    from .user_company.client import AsyncUserCompanyClient, UserCompanyClient
    from .user_payment_service_provider.client import (
        AsyncUserPaymentServiceProviderClient,
        UserPaymentServiceProviderClient,
    )
    from .user_person.client import AsyncUserPersonClient, UserPersonClient
    from .whitelist_sdd.client import AsyncWhitelistSddClient, WhitelistSddClient
    from .whitelist_sdd_one_off.client import AsyncWhitelistSddOneOffClient, WhitelistSddOneOffClient
    from .whitelist_sdd_recurring.client import AsyncWhitelistSddRecurringClient, WhitelistSddRecurringClient


class FernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : FernApiEnvironment
        The environment to use for requests from the client. from .environment import FernApiEnvironment



        Defaults to FernApiEnvironment.DEFAULT



    base_path : typing.Optional[str]
        Server URL variable for 'basePath'. Defaults to 'v1'.

    cache_control : typing.Optional[str]
    bunq_language : typing.Optional[str]
    bunq_region : typing.Optional[str]
    bunq_client_request_id : typing.Optional[str]
    bunq_geolocation : typing.Optional[str]
    bunq_client_authentication : str
    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    max_retries : typing.Optional[int]
        The default maximum number of retries for failed requests. Defaults to 2. Per-request `max_retries` in `request_options` takes precedence over this value.

    stream_reconnection_enabled : typing.Optional[bool]
        Whether to automatically reconnect on stream disconnection for resumable streaming endpoints. Defaults to True. Per-request `stream_reconnection_enabled` in `request_options` takes precedence over this value.

    max_stream_reconnection_attempts : typing.Optional[int]
        The maximum number of reconnection attempts for resumable streaming endpoints. Defaults to no limit. Per-request `max_stream_reconnection_attempts` in `request_options` takes precedence over this value.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.Client]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    logging : typing.Optional[typing.Union[LogConfig, Logger]]
        Configure logging for the SDK. Accepts a LogConfig dict with 'level' (debug/info/warn/error), 'logger' (custom logger implementation), and 'silent' (boolean, defaults to True) fields. You can also pass a pre-configured Logger instance.

    Examples
    --------
    from fern import FernApi

    client = FernApi(
        cache_control="YOUR_CACHE_CONTROL",
        bunq_language="YOUR_BUNQ_LANGUAGE",
        bunq_region="YOUR_BUNQ_REGION",
        bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
        bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
        bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        base_path: typing.Optional[str] = None,
        cache_control: typing.Optional[str] = None,
        bunq_language: typing.Optional[str] = None,
        bunq_region: typing.Optional[str] = None,
        bunq_client_request_id: typing.Optional[str] = None,
        bunq_geolocation: typing.Optional[str] = None,
        bunq_client_authentication: str,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        max_retries: typing.Optional[int] = None,
        stream_reconnection_enabled: typing.Optional[bool] = None,
        max_stream_reconnection_attempts: typing.Optional[int] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None,
        logging: typing.Optional[typing.Union[LogConfig, Logger]] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        _defaulted_max_retries = max_retries if max_retries is not None else 2
        if base_path is not None:
            _base_path = base_path if base_path is not None else "v1"
            base_url = "https://public-api.sandbox.bunq.com/{basePath}".format(basePath=_base_path)
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            cache_control=cache_control,
            bunq_language=bunq_language,
            bunq_region=bunq_region,
            bunq_client_request_id=bunq_client_request_id,
            bunq_geolocation=bunq_geolocation,
            bunq_client_authentication=bunq_client_authentication,
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.Client(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.Client(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
            max_retries=_defaulted_max_retries,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
            logging=logging,
        )
        self._attachment_public: typing.Optional[AttachmentPublicClient] = None
        self._content: typing.Optional[ContentClient] = None
        self._avatar: typing.Optional[AvatarClient] = None
        self._device: typing.Optional[DeviceClient] = None
        self._device_server: typing.Optional[DeviceServerClient] = None
        self._installation: typing.Optional[InstallationClient] = None
        self._server_public_key: typing.Optional[ServerPublicKeyClient] = None
        self._payment_service_provider_credential: typing.Optional[PaymentServiceProviderCredentialClient] = None
        self._sandbox_user_company: typing.Optional[SandboxUserCompanyClient] = None
        self._sandbox_user_person: typing.Optional[SandboxUserPersonClient] = None
        self._server_error: typing.Optional[ServerErrorClient] = None
        self._session_server: typing.Optional[SessionServerClient] = None
        self._session: typing.Optional[SessionClient] = None
        self._user: typing.Optional[UserClient] = None
        self._user_company: typing.Optional[UserCompanyClient] = None
        self._name: typing.Optional[NameClient] = None
        self._user_payment_service_provider: typing.Optional[UserPaymentServiceProviderClient] = None
        self._user_person: typing.Optional[UserPersonClient] = None
        self._attachment: typing.Optional[AttachmentClient] = None
        self._billing_contract_subscription: typing.Optional[BillingContractSubscriptionClient] = None
        self._bunqme_fundraiser_profile: typing.Optional[BunqmeFundraiserProfileClient] = None
        self._card: typing.Optional[CardClient] = None
        self._card_batch: typing.Optional[CardBatchClient] = None
        self._card_batch_replace: typing.Optional[CardBatchReplaceClient] = None
        self._card_credit: typing.Optional[CardCreditClient] = None
        self._card_debit: typing.Optional[CardDebitClient] = None
        self._card_name: typing.Optional[CardNameClient] = None
        self._export_statement_card: typing.Optional[ExportStatementCardClient] = None
        self._export_statement_card_csv: typing.Optional[ExportStatementCardCsvClient] = None
        self._export_statement_card_pdf: typing.Optional[ExportStatementCardPdfClient] = None
        self._generated_cvc2: typing.Optional[GeneratedCvc2Client] = None
        self._replace: typing.Optional[ReplaceClient] = None
        self._certificate_pinned: typing.Optional[CertificatePinnedClient] = None
        self._challenge_request: typing.Optional[ChallengeRequestClient] = None
        self._company: typing.Optional[CompanyClient] = None
        self._confirmation_of_funds: typing.Optional[ConfirmationOfFundsClient] = None
        self._credential_password_ip: typing.Optional[CredentialPasswordIpClient] = None
        self._ip: typing.Optional[IpClient] = None
        self._currency_cloud_beneficiary: typing.Optional[CurrencyCloudBeneficiaryClient] = None
        self._currency_cloud_beneficiary_requirement: typing.Optional[CurrencyCloudBeneficiaryRequirementClient] = None
        self._event: typing.Optional[EventClient] = None
        self._export_annual_overview: typing.Optional[ExportAnnualOverviewClient] = None
        self._feature_announcement: typing.Optional[FeatureAnnouncementClient] = None
        self._insight_preference_date: typing.Optional[InsightPreferenceDateClient] = None
        self._insights: typing.Optional[InsightsClient] = None
        self._insights_search: typing.Optional[InsightsSearchClient] = None
        self._invoice: typing.Optional[InvoiceClient] = None
        self._pdf_content: typing.Optional[PdfContentClient] = None
        self._legal_name: typing.Optional[LegalNameClient] = None
        self._limit: typing.Optional[LimitClient] = None
        self._monetary_account: typing.Optional[MonetaryAccountClient] = None
        self._monetary_account_bank: typing.Optional[MonetaryAccountBankClient] = None
        self._monetary_account_external: typing.Optional[MonetaryAccountExternalClient] = None
        self._monetary_account_joint: typing.Optional[MonetaryAccountJointClient] = None
        self._monetary_account_savings: typing.Optional[MonetaryAccountSavingsClient] = None
        self._note_attachment: typing.Optional[NoteAttachmentClient] = None
        self._note_text: typing.Optional[NoteTextClient] = None
        self._bunqme_fundraiser_result: typing.Optional[BunqmeFundraiserResultClient] = None
        self._bunqme_tab: typing.Optional[BunqmeTabClient] = None
        self._bunqme_tab_result_response: typing.Optional[BunqmeTabResultResponseClient] = None
        self._currency_cloud_payment_quote: typing.Optional[CurrencyCloudPaymentQuoteClient] = None
        self._currency_conversion: typing.Optional[CurrencyConversionClient] = None
        self._currency_conversion_quote: typing.Optional[CurrencyConversionQuoteClient] = None
        self._customer_statement: typing.Optional[CustomerStatementClient] = None
        self._draft_payment: typing.Optional[DraftPaymentClient] = None
        self._statement: typing.Optional[StatementClient] = None
        self._export_rib: typing.Optional[ExportRibClient] = None
        self._ideal_merchant_transaction: typing.Optional[IdealMerchantTransactionClient] = None
        self._mastercard_action: typing.Optional[MastercardActionClient] = None
        self._payment: typing.Optional[PaymentClient] = None
        self._notification_filter_url: typing.Optional[NotificationFilterUrlClient] = None
        self._payment_auto_allocate: typing.Optional[PaymentAutoAllocateClient] = None
        self._definition: typing.Optional[DefinitionClient] = None
        self._instance: typing.Optional[InstanceClient] = None
        self._payment_batch: typing.Optional[PaymentBatchClient] = None
        self._request_inquiry: typing.Optional[RequestInquiryClient] = None
        self._request_inquiry_batch: typing.Optional[RequestInquiryBatchClient] = None
        self._request_response: typing.Optional[RequestResponseClient] = None
        self._schedule: typing.Optional[ScheduleClient] = None
        self._schedule_payment: typing.Optional[SchedulePaymentClient] = None
        self._schedule_payment_batch: typing.Optional[SchedulePaymentBatchClient] = None
        self._schedule_instance: typing.Optional[ScheduleInstanceClient] = None
        self._share_invite_monetary_account_inquiry: typing.Optional[ShareInviteMonetaryAccountInquiryClient] = None
        self._sofort_merchant_transaction: typing.Optional[SofortMerchantTransactionClient] = None
        self._switch_service_payment: typing.Optional[SwitchServicePaymentClient] = None
        self._translink_transaction: typing.Optional[TranslinkTransactionClient] = None
        self._whitelist_sdd: typing.Optional[WhitelistSddClient] = None
        self._notification_filter_email: typing.Optional[NotificationFilterEmailClient] = None
        self._notification_filter_push: typing.Optional[NotificationFilterPushClient] = None
        self._oauth_client: typing.Optional[OauthClientClient] = None
        self._callback_url: typing.Optional[CallbackUrlClient] = None
        self._payment_service_provider_draft_payment: typing.Optional[PaymentServiceProviderDraftPaymentClient] = None
        self._registry_settlement: typing.Optional[RegistrySettlementClient] = None
        self._reward: typing.Optional[RewardClient] = None
        self._reward_recipient: typing.Optional[RewardRecipientClient] = None
        self._reward_sender: typing.Optional[RewardSenderClient] = None
        self._share_invite_monetary_account_response: typing.Optional[ShareInviteMonetaryAccountResponseClient] = None
        self._token_qr_request_ideal: typing.Optional[TokenQrRequestIdealClient] = None
        self._token_qr_request_sofort: typing.Optional[TokenQrRequestSofortClient] = None
        self._transferwise_currency: typing.Optional[TransferwiseCurrencyClient] = None
        self._transferwise_quote: typing.Optional[TransferwiseQuoteClient] = None
        self._transferwise_quote_temporary: typing.Optional[TransferwiseQuoteTemporaryClient] = None
        self._transferwise_recipient: typing.Optional[TransferwiseRecipientClient] = None
        self._transferwise_recipient_requirement: typing.Optional[TransferwiseRecipientRequirementClient] = None
        self._transferwise_transfer: typing.Optional[TransferwiseTransferClient] = None
        self._transferwise_transfer_requirement: typing.Optional[TransferwiseTransferRequirementClient] = None
        self._transferwise_user: typing.Optional[TransferwiseUserClient] = None
        self._tree_progress: typing.Optional[TreeProgressClient] = None
        self._whitelist_sdd_one_off: typing.Optional[WhitelistSddOneOffClient] = None
        self._whitelist_sdd_recurring: typing.Optional[WhitelistSddRecurringClient] = None

    @property
    def attachment_public(self):
        if self._attachment_public is None:
            from .attachment_public.client import AttachmentPublicClient

            self._attachment_public = AttachmentPublicClient(client_wrapper=self._client_wrapper)
        return self._attachment_public

    @property
    def content(self):
        if self._content is None:
            from .content.client import ContentClient

            self._content = ContentClient(client_wrapper=self._client_wrapper)
        return self._content

    @property
    def avatar(self):
        if self._avatar is None:
            from .avatar.client import AvatarClient

            self._avatar = AvatarClient(client_wrapper=self._client_wrapper)
        return self._avatar

    @property
    def device(self):
        if self._device is None:
            from .device.client import DeviceClient

            self._device = DeviceClient(client_wrapper=self._client_wrapper)
        return self._device

    @property
    def device_server(self):
        if self._device_server is None:
            from .device_server.client import DeviceServerClient

            self._device_server = DeviceServerClient(client_wrapper=self._client_wrapper)
        return self._device_server

    @property
    def installation(self):
        if self._installation is None:
            from .installation.client import InstallationClient

            self._installation = InstallationClient(client_wrapper=self._client_wrapper)
        return self._installation

    @property
    def server_public_key(self):
        if self._server_public_key is None:
            from .server_public_key.client import ServerPublicKeyClient

            self._server_public_key = ServerPublicKeyClient(client_wrapper=self._client_wrapper)
        return self._server_public_key

    @property
    def payment_service_provider_credential(self):
        if self._payment_service_provider_credential is None:
            from .payment_service_provider_credential.client import PaymentServiceProviderCredentialClient

            self._payment_service_provider_credential = PaymentServiceProviderCredentialClient(
                client_wrapper=self._client_wrapper
            )
        return self._payment_service_provider_credential

    @property
    def sandbox_user_company(self):
        if self._sandbox_user_company is None:
            from .sandbox_user_company.client import SandboxUserCompanyClient

            self._sandbox_user_company = SandboxUserCompanyClient(client_wrapper=self._client_wrapper)
        return self._sandbox_user_company

    @property
    def sandbox_user_person(self):
        if self._sandbox_user_person is None:
            from .sandbox_user_person.client import SandboxUserPersonClient

            self._sandbox_user_person = SandboxUserPersonClient(client_wrapper=self._client_wrapper)
        return self._sandbox_user_person

    @property
    def server_error(self):
        if self._server_error is None:
            from .server_error.client import ServerErrorClient

            self._server_error = ServerErrorClient(client_wrapper=self._client_wrapper)
        return self._server_error

    @property
    def session_server(self):
        if self._session_server is None:
            from .session_server.client import SessionServerClient

            self._session_server = SessionServerClient(client_wrapper=self._client_wrapper)
        return self._session_server

    @property
    def session(self):
        if self._session is None:
            from .session.client import SessionClient

            self._session = SessionClient(client_wrapper=self._client_wrapper)
        return self._session

    @property
    def user(self):
        if self._user is None:
            from .user.client import UserClient

            self._user = UserClient(client_wrapper=self._client_wrapper)
        return self._user

    @property
    def user_company(self):
        if self._user_company is None:
            from .user_company.client import UserCompanyClient

            self._user_company = UserCompanyClient(client_wrapper=self._client_wrapper)
        return self._user_company

    @property
    def name(self):
        if self._name is None:
            from .name.client import NameClient

            self._name = NameClient(client_wrapper=self._client_wrapper)
        return self._name

    @property
    def user_payment_service_provider(self):
        if self._user_payment_service_provider is None:
            from .user_payment_service_provider.client import UserPaymentServiceProviderClient

            self._user_payment_service_provider = UserPaymentServiceProviderClient(client_wrapper=self._client_wrapper)
        return self._user_payment_service_provider

    @property
    def user_person(self):
        if self._user_person is None:
            from .user_person.client import UserPersonClient

            self._user_person = UserPersonClient(client_wrapper=self._client_wrapper)
        return self._user_person

    @property
    def attachment(self):
        if self._attachment is None:
            from .attachment.client import AttachmentClient

            self._attachment = AttachmentClient(client_wrapper=self._client_wrapper)
        return self._attachment

    @property
    def billing_contract_subscription(self):
        if self._billing_contract_subscription is None:
            from .billing_contract_subscription.client import BillingContractSubscriptionClient

            self._billing_contract_subscription = BillingContractSubscriptionClient(client_wrapper=self._client_wrapper)
        return self._billing_contract_subscription

    @property
    def bunqme_fundraiser_profile(self):
        if self._bunqme_fundraiser_profile is None:
            from .bunqme_fundraiser_profile.client import BunqmeFundraiserProfileClient

            self._bunqme_fundraiser_profile = BunqmeFundraiserProfileClient(client_wrapper=self._client_wrapper)
        return self._bunqme_fundraiser_profile

    @property
    def card(self):
        if self._card is None:
            from .card.client import CardClient

            self._card = CardClient(client_wrapper=self._client_wrapper)
        return self._card

    @property
    def card_batch(self):
        if self._card_batch is None:
            from .card_batch.client import CardBatchClient

            self._card_batch = CardBatchClient(client_wrapper=self._client_wrapper)
        return self._card_batch

    @property
    def card_batch_replace(self):
        if self._card_batch_replace is None:
            from .card_batch_replace.client import CardBatchReplaceClient

            self._card_batch_replace = CardBatchReplaceClient(client_wrapper=self._client_wrapper)
        return self._card_batch_replace

    @property
    def card_credit(self):
        if self._card_credit is None:
            from .card_credit.client import CardCreditClient

            self._card_credit = CardCreditClient(client_wrapper=self._client_wrapper)
        return self._card_credit

    @property
    def card_debit(self):
        if self._card_debit is None:
            from .card_debit.client import CardDebitClient

            self._card_debit = CardDebitClient(client_wrapper=self._client_wrapper)
        return self._card_debit

    @property
    def card_name(self):
        if self._card_name is None:
            from .card_name.client import CardNameClient

            self._card_name = CardNameClient(client_wrapper=self._client_wrapper)
        return self._card_name

    @property
    def export_statement_card(self):
        if self._export_statement_card is None:
            from .export_statement_card.client import ExportStatementCardClient

            self._export_statement_card = ExportStatementCardClient(client_wrapper=self._client_wrapper)
        return self._export_statement_card

    @property
    def export_statement_card_csv(self):
        if self._export_statement_card_csv is None:
            from .export_statement_card_csv.client import ExportStatementCardCsvClient

            self._export_statement_card_csv = ExportStatementCardCsvClient(client_wrapper=self._client_wrapper)
        return self._export_statement_card_csv

    @property
    def export_statement_card_pdf(self):
        if self._export_statement_card_pdf is None:
            from .export_statement_card_pdf.client import ExportStatementCardPdfClient

            self._export_statement_card_pdf = ExportStatementCardPdfClient(client_wrapper=self._client_wrapper)
        return self._export_statement_card_pdf

    @property
    def generated_cvc2(self):
        if self._generated_cvc2 is None:
            from .generated_cvc2.client import GeneratedCvc2Client

            self._generated_cvc2 = GeneratedCvc2Client(client_wrapper=self._client_wrapper)
        return self._generated_cvc2

    @property
    def replace(self):
        if self._replace is None:
            from .replace.client import ReplaceClient

            self._replace = ReplaceClient(client_wrapper=self._client_wrapper)
        return self._replace

    @property
    def certificate_pinned(self):
        if self._certificate_pinned is None:
            from .certificate_pinned.client import CertificatePinnedClient

            self._certificate_pinned = CertificatePinnedClient(client_wrapper=self._client_wrapper)
        return self._certificate_pinned

    @property
    def challenge_request(self):
        if self._challenge_request is None:
            from .challenge_request.client import ChallengeRequestClient

            self._challenge_request = ChallengeRequestClient(client_wrapper=self._client_wrapper)
        return self._challenge_request

    @property
    def company(self):
        if self._company is None:
            from .company.client import CompanyClient

            self._company = CompanyClient(client_wrapper=self._client_wrapper)
        return self._company

    @property
    def confirmation_of_funds(self):
        if self._confirmation_of_funds is None:
            from .confirmation_of_funds.client import ConfirmationOfFundsClient

            self._confirmation_of_funds = ConfirmationOfFundsClient(client_wrapper=self._client_wrapper)
        return self._confirmation_of_funds

    @property
    def credential_password_ip(self):
        if self._credential_password_ip is None:
            from .credential_password_ip.client import CredentialPasswordIpClient

            self._credential_password_ip = CredentialPasswordIpClient(client_wrapper=self._client_wrapper)
        return self._credential_password_ip

    @property
    def ip(self):
        if self._ip is None:
            from .ip.client import IpClient

            self._ip = IpClient(client_wrapper=self._client_wrapper)
        return self._ip

    @property
    def currency_cloud_beneficiary(self):
        if self._currency_cloud_beneficiary is None:
            from .currency_cloud_beneficiary.client import CurrencyCloudBeneficiaryClient

            self._currency_cloud_beneficiary = CurrencyCloudBeneficiaryClient(client_wrapper=self._client_wrapper)
        return self._currency_cloud_beneficiary

    @property
    def currency_cloud_beneficiary_requirement(self):
        if self._currency_cloud_beneficiary_requirement is None:
            from .currency_cloud_beneficiary_requirement.client import (
                CurrencyCloudBeneficiaryRequirementClient,
            )

            self._currency_cloud_beneficiary_requirement = CurrencyCloudBeneficiaryRequirementClient(
                client_wrapper=self._client_wrapper
            )
        return self._currency_cloud_beneficiary_requirement

    @property
    def event(self):
        if self._event is None:
            from .event.client import EventClient

            self._event = EventClient(client_wrapper=self._client_wrapper)
        return self._event

    @property
    def export_annual_overview(self):
        if self._export_annual_overview is None:
            from .export_annual_overview.client import ExportAnnualOverviewClient

            self._export_annual_overview = ExportAnnualOverviewClient(client_wrapper=self._client_wrapper)
        return self._export_annual_overview

    @property
    def feature_announcement(self):
        if self._feature_announcement is None:
            from .feature_announcement.client import FeatureAnnouncementClient

            self._feature_announcement = FeatureAnnouncementClient(client_wrapper=self._client_wrapper)
        return self._feature_announcement

    @property
    def insight_preference_date(self):
        if self._insight_preference_date is None:
            from .insight_preference_date.client import InsightPreferenceDateClient

            self._insight_preference_date = InsightPreferenceDateClient(client_wrapper=self._client_wrapper)
        return self._insight_preference_date

    @property
    def insights(self):
        if self._insights is None:
            from .insights.client import InsightsClient

            self._insights = InsightsClient(client_wrapper=self._client_wrapper)
        return self._insights

    @property
    def insights_search(self):
        if self._insights_search is None:
            from .insights_search.client import InsightsSearchClient

            self._insights_search = InsightsSearchClient(client_wrapper=self._client_wrapper)
        return self._insights_search

    @property
    def invoice(self):
        if self._invoice is None:
            from .invoice.client import InvoiceClient

            self._invoice = InvoiceClient(client_wrapper=self._client_wrapper)
        return self._invoice

    @property
    def pdf_content(self):
        if self._pdf_content is None:
            from .pdf_content.client import PdfContentClient

            self._pdf_content = PdfContentClient(client_wrapper=self._client_wrapper)
        return self._pdf_content

    @property
    def legal_name(self):
        if self._legal_name is None:
            from .legal_name.client import LegalNameClient

            self._legal_name = LegalNameClient(client_wrapper=self._client_wrapper)
        return self._legal_name

    @property
    def limit(self):
        if self._limit is None:
            from .limit.client import LimitClient

            self._limit = LimitClient(client_wrapper=self._client_wrapper)
        return self._limit

    @property
    def monetary_account(self):
        if self._monetary_account is None:
            from .monetary_account.client import MonetaryAccountClient

            self._monetary_account = MonetaryAccountClient(client_wrapper=self._client_wrapper)
        return self._monetary_account

    @property
    def monetary_account_bank(self):
        if self._monetary_account_bank is None:
            from .monetary_account_bank.client import MonetaryAccountBankClient

            self._monetary_account_bank = MonetaryAccountBankClient(client_wrapper=self._client_wrapper)
        return self._monetary_account_bank

    @property
    def monetary_account_external(self):
        if self._monetary_account_external is None:
            from .monetary_account_external.client import MonetaryAccountExternalClient

            self._monetary_account_external = MonetaryAccountExternalClient(client_wrapper=self._client_wrapper)
        return self._monetary_account_external

    @property
    def monetary_account_joint(self):
        if self._monetary_account_joint is None:
            from .monetary_account_joint.client import MonetaryAccountJointClient

            self._monetary_account_joint = MonetaryAccountJointClient(client_wrapper=self._client_wrapper)
        return self._monetary_account_joint

    @property
    def monetary_account_savings(self):
        if self._monetary_account_savings is None:
            from .monetary_account_savings.client import MonetaryAccountSavingsClient

            self._monetary_account_savings = MonetaryAccountSavingsClient(client_wrapper=self._client_wrapper)
        return self._monetary_account_savings

    @property
    def note_attachment(self):
        if self._note_attachment is None:
            from .note_attachment.client import NoteAttachmentClient

            self._note_attachment = NoteAttachmentClient(client_wrapper=self._client_wrapper)
        return self._note_attachment

    @property
    def note_text(self):
        if self._note_text is None:
            from .note_text.client import NoteTextClient

            self._note_text = NoteTextClient(client_wrapper=self._client_wrapper)
        return self._note_text

    @property
    def bunqme_fundraiser_result(self):
        if self._bunqme_fundraiser_result is None:
            from .bunqme_fundraiser_result.client import BunqmeFundraiserResultClient

            self._bunqme_fundraiser_result = BunqmeFundraiserResultClient(client_wrapper=self._client_wrapper)
        return self._bunqme_fundraiser_result

    @property
    def bunqme_tab(self):
        if self._bunqme_tab is None:
            from .bunqme_tab.client import BunqmeTabClient

            self._bunqme_tab = BunqmeTabClient(client_wrapper=self._client_wrapper)
        return self._bunqme_tab

    @property
    def bunqme_tab_result_response(self):
        if self._bunqme_tab_result_response is None:
            from .bunqme_tab_result_response.client import BunqmeTabResultResponseClient

            self._bunqme_tab_result_response = BunqmeTabResultResponseClient(client_wrapper=self._client_wrapper)
        return self._bunqme_tab_result_response

    @property
    def currency_cloud_payment_quote(self):
        if self._currency_cloud_payment_quote is None:
            from .currency_cloud_payment_quote.client import CurrencyCloudPaymentQuoteClient

            self._currency_cloud_payment_quote = CurrencyCloudPaymentQuoteClient(client_wrapper=self._client_wrapper)
        return self._currency_cloud_payment_quote

    @property
    def currency_conversion(self):
        if self._currency_conversion is None:
            from .currency_conversion.client import CurrencyConversionClient

            self._currency_conversion = CurrencyConversionClient(client_wrapper=self._client_wrapper)
        return self._currency_conversion

    @property
    def currency_conversion_quote(self):
        if self._currency_conversion_quote is None:
            from .currency_conversion_quote.client import CurrencyConversionQuoteClient

            self._currency_conversion_quote = CurrencyConversionQuoteClient(client_wrapper=self._client_wrapper)
        return self._currency_conversion_quote

    @property
    def customer_statement(self):
        if self._customer_statement is None:
            from .customer_statement.client import CustomerStatementClient

            self._customer_statement = CustomerStatementClient(client_wrapper=self._client_wrapper)
        return self._customer_statement

    @property
    def draft_payment(self):
        if self._draft_payment is None:
            from .draft_payment.client import DraftPaymentClient

            self._draft_payment = DraftPaymentClient(client_wrapper=self._client_wrapper)
        return self._draft_payment

    @property
    def statement(self):
        if self._statement is None:
            from .statement.client import StatementClient

            self._statement = StatementClient(client_wrapper=self._client_wrapper)
        return self._statement

    @property
    def export_rib(self):
        if self._export_rib is None:
            from .export_rib.client import ExportRibClient

            self._export_rib = ExportRibClient(client_wrapper=self._client_wrapper)
        return self._export_rib

    @property
    def ideal_merchant_transaction(self):
        if self._ideal_merchant_transaction is None:
            from .ideal_merchant_transaction.client import IdealMerchantTransactionClient

            self._ideal_merchant_transaction = IdealMerchantTransactionClient(client_wrapper=self._client_wrapper)
        return self._ideal_merchant_transaction

    @property
    def mastercard_action(self):
        if self._mastercard_action is None:
            from .mastercard_action.client import MastercardActionClient

            self._mastercard_action = MastercardActionClient(client_wrapper=self._client_wrapper)
        return self._mastercard_action

    @property
    def payment(self):
        if self._payment is None:
            from .payment.client import PaymentClient

            self._payment = PaymentClient(client_wrapper=self._client_wrapper)
        return self._payment

    @property
    def notification_filter_url(self):
        if self._notification_filter_url is None:
            from .notification_filter_url.client import NotificationFilterUrlClient

            self._notification_filter_url = NotificationFilterUrlClient(client_wrapper=self._client_wrapper)
        return self._notification_filter_url

    @property
    def payment_auto_allocate(self):
        if self._payment_auto_allocate is None:
            from .payment_auto_allocate.client import PaymentAutoAllocateClient

            self._payment_auto_allocate = PaymentAutoAllocateClient(client_wrapper=self._client_wrapper)
        return self._payment_auto_allocate

    @property
    def definition(self):
        if self._definition is None:
            from .definition.client import DefinitionClient

            self._definition = DefinitionClient(client_wrapper=self._client_wrapper)
        return self._definition

    @property
    def instance(self):
        if self._instance is None:
            from .instance.client import InstanceClient

            self._instance = InstanceClient(client_wrapper=self._client_wrapper)
        return self._instance

    @property
    def payment_batch(self):
        if self._payment_batch is None:
            from .payment_batch.client import PaymentBatchClient

            self._payment_batch = PaymentBatchClient(client_wrapper=self._client_wrapper)
        return self._payment_batch

    @property
    def request_inquiry(self):
        if self._request_inquiry is None:
            from .request_inquiry.client import RequestInquiryClient

            self._request_inquiry = RequestInquiryClient(client_wrapper=self._client_wrapper)
        return self._request_inquiry

    @property
    def request_inquiry_batch(self):
        if self._request_inquiry_batch is None:
            from .request_inquiry_batch.client import RequestInquiryBatchClient

            self._request_inquiry_batch = RequestInquiryBatchClient(client_wrapper=self._client_wrapper)
        return self._request_inquiry_batch

    @property
    def request_response(self):
        if self._request_response is None:
            from .request_response.client import RequestResponseClient

            self._request_response = RequestResponseClient(client_wrapper=self._client_wrapper)
        return self._request_response

    @property
    def schedule(self):
        if self._schedule is None:
            from .schedule.client import ScheduleClient

            self._schedule = ScheduleClient(client_wrapper=self._client_wrapper)
        return self._schedule

    @property
    def schedule_payment(self):
        if self._schedule_payment is None:
            from .schedule_payment.client import SchedulePaymentClient

            self._schedule_payment = SchedulePaymentClient(client_wrapper=self._client_wrapper)
        return self._schedule_payment

    @property
    def schedule_payment_batch(self):
        if self._schedule_payment_batch is None:
            from .schedule_payment_batch.client import SchedulePaymentBatchClient

            self._schedule_payment_batch = SchedulePaymentBatchClient(client_wrapper=self._client_wrapper)
        return self._schedule_payment_batch

    @property
    def schedule_instance(self):
        if self._schedule_instance is None:
            from .schedule_instance.client import ScheduleInstanceClient

            self._schedule_instance = ScheduleInstanceClient(client_wrapper=self._client_wrapper)
        return self._schedule_instance

    @property
    def share_invite_monetary_account_inquiry(self):
        if self._share_invite_monetary_account_inquiry is None:
            from .share_invite_monetary_account_inquiry.client import (
                ShareInviteMonetaryAccountInquiryClient,
            )

            self._share_invite_monetary_account_inquiry = ShareInviteMonetaryAccountInquiryClient(
                client_wrapper=self._client_wrapper
            )
        return self._share_invite_monetary_account_inquiry

    @property
    def sofort_merchant_transaction(self):
        if self._sofort_merchant_transaction is None:
            from .sofort_merchant_transaction.client import SofortMerchantTransactionClient

            self._sofort_merchant_transaction = SofortMerchantTransactionClient(client_wrapper=self._client_wrapper)
        return self._sofort_merchant_transaction

    @property
    def switch_service_payment(self):
        if self._switch_service_payment is None:
            from .switch_service_payment.client import SwitchServicePaymentClient

            self._switch_service_payment = SwitchServicePaymentClient(client_wrapper=self._client_wrapper)
        return self._switch_service_payment

    @property
    def translink_transaction(self):
        if self._translink_transaction is None:
            from .translink_transaction.client import TranslinkTransactionClient

            self._translink_transaction = TranslinkTransactionClient(client_wrapper=self._client_wrapper)
        return self._translink_transaction

    @property
    def whitelist_sdd(self):
        if self._whitelist_sdd is None:
            from .whitelist_sdd.client import WhitelistSddClient

            self._whitelist_sdd = WhitelistSddClient(client_wrapper=self._client_wrapper)
        return self._whitelist_sdd

    @property
    def notification_filter_email(self):
        if self._notification_filter_email is None:
            from .notification_filter_email.client import NotificationFilterEmailClient

            self._notification_filter_email = NotificationFilterEmailClient(client_wrapper=self._client_wrapper)
        return self._notification_filter_email

    @property
    def notification_filter_push(self):
        if self._notification_filter_push is None:
            from .notification_filter_push.client import NotificationFilterPushClient

            self._notification_filter_push = NotificationFilterPushClient(client_wrapper=self._client_wrapper)
        return self._notification_filter_push

    @property
    def oauth_client(self):
        if self._oauth_client is None:
            from .oauth_client.client import OauthClientClient

            self._oauth_client = OauthClientClient(client_wrapper=self._client_wrapper)
        return self._oauth_client

    @property
    def callback_url(self):
        if self._callback_url is None:
            from .callback_url.client import CallbackUrlClient

            self._callback_url = CallbackUrlClient(client_wrapper=self._client_wrapper)
        return self._callback_url

    @property
    def payment_service_provider_draft_payment(self):
        if self._payment_service_provider_draft_payment is None:
            from .payment_service_provider_draft_payment.client import (
                PaymentServiceProviderDraftPaymentClient,
            )

            self._payment_service_provider_draft_payment = PaymentServiceProviderDraftPaymentClient(
                client_wrapper=self._client_wrapper
            )
        return self._payment_service_provider_draft_payment

    @property
    def registry_settlement(self):
        if self._registry_settlement is None:
            from .registry_settlement.client import RegistrySettlementClient

            self._registry_settlement = RegistrySettlementClient(client_wrapper=self._client_wrapper)
        return self._registry_settlement

    @property
    def reward(self):
        if self._reward is None:
            from .reward.client import RewardClient

            self._reward = RewardClient(client_wrapper=self._client_wrapper)
        return self._reward

    @property
    def reward_recipient(self):
        if self._reward_recipient is None:
            from .reward_recipient.client import RewardRecipientClient

            self._reward_recipient = RewardRecipientClient(client_wrapper=self._client_wrapper)
        return self._reward_recipient

    @property
    def reward_sender(self):
        if self._reward_sender is None:
            from .reward_sender.client import RewardSenderClient

            self._reward_sender = RewardSenderClient(client_wrapper=self._client_wrapper)
        return self._reward_sender

    @property
    def share_invite_monetary_account_response(self):
        if self._share_invite_monetary_account_response is None:
            from .share_invite_monetary_account_response.client import (
                ShareInviteMonetaryAccountResponseClient,
            )

            self._share_invite_monetary_account_response = ShareInviteMonetaryAccountResponseClient(
                client_wrapper=self._client_wrapper
            )
        return self._share_invite_monetary_account_response

    @property
    def token_qr_request_ideal(self):
        if self._token_qr_request_ideal is None:
            from .token_qr_request_ideal.client import TokenQrRequestIdealClient

            self._token_qr_request_ideal = TokenQrRequestIdealClient(client_wrapper=self._client_wrapper)
        return self._token_qr_request_ideal

    @property
    def token_qr_request_sofort(self):
        if self._token_qr_request_sofort is None:
            from .token_qr_request_sofort.client import TokenQrRequestSofortClient

            self._token_qr_request_sofort = TokenQrRequestSofortClient(client_wrapper=self._client_wrapper)
        return self._token_qr_request_sofort

    @property
    def transferwise_currency(self):
        if self._transferwise_currency is None:
            from .transferwise_currency.client import TransferwiseCurrencyClient

            self._transferwise_currency = TransferwiseCurrencyClient(client_wrapper=self._client_wrapper)
        return self._transferwise_currency

    @property
    def transferwise_quote(self):
        if self._transferwise_quote is None:
            from .transferwise_quote.client import TransferwiseQuoteClient

            self._transferwise_quote = TransferwiseQuoteClient(client_wrapper=self._client_wrapper)
        return self._transferwise_quote

    @property
    def transferwise_quote_temporary(self):
        if self._transferwise_quote_temporary is None:
            from .transferwise_quote_temporary.client import TransferwiseQuoteTemporaryClient

            self._transferwise_quote_temporary = TransferwiseQuoteTemporaryClient(client_wrapper=self._client_wrapper)
        return self._transferwise_quote_temporary

    @property
    def transferwise_recipient(self):
        if self._transferwise_recipient is None:
            from .transferwise_recipient.client import TransferwiseRecipientClient

            self._transferwise_recipient = TransferwiseRecipientClient(client_wrapper=self._client_wrapper)
        return self._transferwise_recipient

    @property
    def transferwise_recipient_requirement(self):
        if self._transferwise_recipient_requirement is None:
            from .transferwise_recipient_requirement.client import TransferwiseRecipientRequirementClient

            self._transferwise_recipient_requirement = TransferwiseRecipientRequirementClient(
                client_wrapper=self._client_wrapper
            )
        return self._transferwise_recipient_requirement

    @property
    def transferwise_transfer(self):
        if self._transferwise_transfer is None:
            from .transferwise_transfer.client import TransferwiseTransferClient

            self._transferwise_transfer = TransferwiseTransferClient(client_wrapper=self._client_wrapper)
        return self._transferwise_transfer

    @property
    def transferwise_transfer_requirement(self):
        if self._transferwise_transfer_requirement is None:
            from .transferwise_transfer_requirement.client import TransferwiseTransferRequirementClient

            self._transferwise_transfer_requirement = TransferwiseTransferRequirementClient(
                client_wrapper=self._client_wrapper
            )
        return self._transferwise_transfer_requirement

    @property
    def transferwise_user(self):
        if self._transferwise_user is None:
            from .transferwise_user.client import TransferwiseUserClient

            self._transferwise_user = TransferwiseUserClient(client_wrapper=self._client_wrapper)
        return self._transferwise_user

    @property
    def tree_progress(self):
        if self._tree_progress is None:
            from .tree_progress.client import TreeProgressClient

            self._tree_progress = TreeProgressClient(client_wrapper=self._client_wrapper)
        return self._tree_progress

    @property
    def whitelist_sdd_one_off(self):
        if self._whitelist_sdd_one_off is None:
            from .whitelist_sdd_one_off.client import WhitelistSddOneOffClient

            self._whitelist_sdd_one_off = WhitelistSddOneOffClient(client_wrapper=self._client_wrapper)
        return self._whitelist_sdd_one_off

    @property
    def whitelist_sdd_recurring(self):
        if self._whitelist_sdd_recurring is None:
            from .whitelist_sdd_recurring.client import WhitelistSddRecurringClient

            self._whitelist_sdd_recurring = WhitelistSddRecurringClient(client_wrapper=self._client_wrapper)
        return self._whitelist_sdd_recurring


def _make_default_async_client(
    timeout: typing.Optional[float],
    follow_redirects: typing.Optional[bool],
) -> httpx.AsyncClient:
    try:
        import httpx_aiohttp
    except ImportError:
        pass
    else:
        if follow_redirects is not None:
            return httpx_aiohttp.HttpxAiohttpClient(timeout=timeout, follow_redirects=follow_redirects)
        return httpx_aiohttp.HttpxAiohttpClient(timeout=timeout)

    if follow_redirects is not None:
        return httpx.AsyncClient(timeout=timeout, follow_redirects=follow_redirects)
    return httpx.AsyncClient(timeout=timeout)


class AsyncFernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : FernApiEnvironment
        The environment to use for requests from the client. from .environment import FernApiEnvironment



        Defaults to FernApiEnvironment.DEFAULT



    base_path : typing.Optional[str]
        Server URL variable for 'basePath'. Defaults to 'v1'.

    cache_control : typing.Optional[str]
    bunq_language : typing.Optional[str]
    bunq_region : typing.Optional[str]
    bunq_client_request_id : typing.Optional[str]
    bunq_geolocation : typing.Optional[str]
    bunq_client_authentication : str
    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    max_retries : typing.Optional[int]
        The default maximum number of retries for failed requests. Defaults to 2. Per-request `max_retries` in `request_options` takes precedence over this value.

    stream_reconnection_enabled : typing.Optional[bool]
        Whether to automatically reconnect on stream disconnection for resumable streaming endpoints. Defaults to True. Per-request `stream_reconnection_enabled` in `request_options` takes precedence over this value.

    max_stream_reconnection_attempts : typing.Optional[int]
        The maximum number of reconnection attempts for resumable streaming endpoints. Defaults to no limit. Per-request `max_stream_reconnection_attempts` in `request_options` takes precedence over this value.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.AsyncClient]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    logging : typing.Optional[typing.Union[LogConfig, Logger]]
        Configure logging for the SDK. Accepts a LogConfig dict with 'level' (debug/info/warn/error), 'logger' (custom logger implementation), and 'silent' (boolean, defaults to True) fields. You can also pass a pre-configured Logger instance.

    Examples
    --------
    from fern import AsyncFernApi

    client = AsyncFernApi(
        cache_control="YOUR_CACHE_CONTROL",
        bunq_language="YOUR_BUNQ_LANGUAGE",
        bunq_region="YOUR_BUNQ_REGION",
        bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
        bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
        bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        base_path: typing.Optional[str] = None,
        cache_control: typing.Optional[str] = None,
        bunq_language: typing.Optional[str] = None,
        bunq_region: typing.Optional[str] = None,
        bunq_client_request_id: typing.Optional[str] = None,
        bunq_geolocation: typing.Optional[str] = None,
        bunq_client_authentication: str,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        max_retries: typing.Optional[int] = None,
        stream_reconnection_enabled: typing.Optional[bool] = None,
        max_stream_reconnection_attempts: typing.Optional[int] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
        logging: typing.Optional[typing.Union[LogConfig, Logger]] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        _defaulted_max_retries = max_retries if max_retries is not None else 2
        if base_path is not None:
            _base_path = base_path if base_path is not None else "v1"
            base_url = "https://public-api.sandbox.bunq.com/{basePath}".format(basePath=_base_path)
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            cache_control=cache_control,
            bunq_language=bunq_language,
            bunq_region=bunq_region,
            bunq_client_request_id=bunq_client_request_id,
            bunq_geolocation=bunq_geolocation,
            bunq_client_authentication=bunq_client_authentication,
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else _make_default_async_client(timeout=_defaulted_timeout, follow_redirects=follow_redirects),
            timeout=_defaulted_timeout,
            max_retries=_defaulted_max_retries,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
            logging=logging,
        )
        self._attachment_public: typing.Optional[AsyncAttachmentPublicClient] = None
        self._content: typing.Optional[AsyncContentClient] = None
        self._avatar: typing.Optional[AsyncAvatarClient] = None
        self._device: typing.Optional[AsyncDeviceClient] = None
        self._device_server: typing.Optional[AsyncDeviceServerClient] = None
        self._installation: typing.Optional[AsyncInstallationClient] = None
        self._server_public_key: typing.Optional[AsyncServerPublicKeyClient] = None
        self._payment_service_provider_credential: typing.Optional[AsyncPaymentServiceProviderCredentialClient] = None
        self._sandbox_user_company: typing.Optional[AsyncSandboxUserCompanyClient] = None
        self._sandbox_user_person: typing.Optional[AsyncSandboxUserPersonClient] = None
        self._server_error: typing.Optional[AsyncServerErrorClient] = None
        self._session_server: typing.Optional[AsyncSessionServerClient] = None
        self._session: typing.Optional[AsyncSessionClient] = None
        self._user: typing.Optional[AsyncUserClient] = None
        self._user_company: typing.Optional[AsyncUserCompanyClient] = None
        self._name: typing.Optional[AsyncNameClient] = None
        self._user_payment_service_provider: typing.Optional[AsyncUserPaymentServiceProviderClient] = None
        self._user_person: typing.Optional[AsyncUserPersonClient] = None
        self._attachment: typing.Optional[AsyncAttachmentClient] = None
        self._billing_contract_subscription: typing.Optional[AsyncBillingContractSubscriptionClient] = None
        self._bunqme_fundraiser_profile: typing.Optional[AsyncBunqmeFundraiserProfileClient] = None
        self._card: typing.Optional[AsyncCardClient] = None
        self._card_batch: typing.Optional[AsyncCardBatchClient] = None
        self._card_batch_replace: typing.Optional[AsyncCardBatchReplaceClient] = None
        self._card_credit: typing.Optional[AsyncCardCreditClient] = None
        self._card_debit: typing.Optional[AsyncCardDebitClient] = None
        self._card_name: typing.Optional[AsyncCardNameClient] = None
        self._export_statement_card: typing.Optional[AsyncExportStatementCardClient] = None
        self._export_statement_card_csv: typing.Optional[AsyncExportStatementCardCsvClient] = None
        self._export_statement_card_pdf: typing.Optional[AsyncExportStatementCardPdfClient] = None
        self._generated_cvc2: typing.Optional[AsyncGeneratedCvc2Client] = None
        self._replace: typing.Optional[AsyncReplaceClient] = None
        self._certificate_pinned: typing.Optional[AsyncCertificatePinnedClient] = None
        self._challenge_request: typing.Optional[AsyncChallengeRequestClient] = None
        self._company: typing.Optional[AsyncCompanyClient] = None
        self._confirmation_of_funds: typing.Optional[AsyncConfirmationOfFundsClient] = None
        self._credential_password_ip: typing.Optional[AsyncCredentialPasswordIpClient] = None
        self._ip: typing.Optional[AsyncIpClient] = None
        self._currency_cloud_beneficiary: typing.Optional[AsyncCurrencyCloudBeneficiaryClient] = None
        self._currency_cloud_beneficiary_requirement: typing.Optional[
            AsyncCurrencyCloudBeneficiaryRequirementClient
        ] = None
        self._event: typing.Optional[AsyncEventClient] = None
        self._export_annual_overview: typing.Optional[AsyncExportAnnualOverviewClient] = None
        self._feature_announcement: typing.Optional[AsyncFeatureAnnouncementClient] = None
        self._insight_preference_date: typing.Optional[AsyncInsightPreferenceDateClient] = None
        self._insights: typing.Optional[AsyncInsightsClient] = None
        self._insights_search: typing.Optional[AsyncInsightsSearchClient] = None
        self._invoice: typing.Optional[AsyncInvoiceClient] = None
        self._pdf_content: typing.Optional[AsyncPdfContentClient] = None
        self._legal_name: typing.Optional[AsyncLegalNameClient] = None
        self._limit: typing.Optional[AsyncLimitClient] = None
        self._monetary_account: typing.Optional[AsyncMonetaryAccountClient] = None
        self._monetary_account_bank: typing.Optional[AsyncMonetaryAccountBankClient] = None
        self._monetary_account_external: typing.Optional[AsyncMonetaryAccountExternalClient] = None
        self._monetary_account_joint: typing.Optional[AsyncMonetaryAccountJointClient] = None
        self._monetary_account_savings: typing.Optional[AsyncMonetaryAccountSavingsClient] = None
        self._note_attachment: typing.Optional[AsyncNoteAttachmentClient] = None
        self._note_text: typing.Optional[AsyncNoteTextClient] = None
        self._bunqme_fundraiser_result: typing.Optional[AsyncBunqmeFundraiserResultClient] = None
        self._bunqme_tab: typing.Optional[AsyncBunqmeTabClient] = None
        self._bunqme_tab_result_response: typing.Optional[AsyncBunqmeTabResultResponseClient] = None
        self._currency_cloud_payment_quote: typing.Optional[AsyncCurrencyCloudPaymentQuoteClient] = None
        self._currency_conversion: typing.Optional[AsyncCurrencyConversionClient] = None
        self._currency_conversion_quote: typing.Optional[AsyncCurrencyConversionQuoteClient] = None
        self._customer_statement: typing.Optional[AsyncCustomerStatementClient] = None
        self._draft_payment: typing.Optional[AsyncDraftPaymentClient] = None
        self._statement: typing.Optional[AsyncStatementClient] = None
        self._export_rib: typing.Optional[AsyncExportRibClient] = None
        self._ideal_merchant_transaction: typing.Optional[AsyncIdealMerchantTransactionClient] = None
        self._mastercard_action: typing.Optional[AsyncMastercardActionClient] = None
        self._payment: typing.Optional[AsyncPaymentClient] = None
        self._notification_filter_url: typing.Optional[AsyncNotificationFilterUrlClient] = None
        self._payment_auto_allocate: typing.Optional[AsyncPaymentAutoAllocateClient] = None
        self._definition: typing.Optional[AsyncDefinitionClient] = None
        self._instance: typing.Optional[AsyncInstanceClient] = None
        self._payment_batch: typing.Optional[AsyncPaymentBatchClient] = None
        self._request_inquiry: typing.Optional[AsyncRequestInquiryClient] = None
        self._request_inquiry_batch: typing.Optional[AsyncRequestInquiryBatchClient] = None
        self._request_response: typing.Optional[AsyncRequestResponseClient] = None
        self._schedule: typing.Optional[AsyncScheduleClient] = None
        self._schedule_payment: typing.Optional[AsyncSchedulePaymentClient] = None
        self._schedule_payment_batch: typing.Optional[AsyncSchedulePaymentBatchClient] = None
        self._schedule_instance: typing.Optional[AsyncScheduleInstanceClient] = None
        self._share_invite_monetary_account_inquiry: typing.Optional[AsyncShareInviteMonetaryAccountInquiryClient] = (
            None
        )
        self._sofort_merchant_transaction: typing.Optional[AsyncSofortMerchantTransactionClient] = None
        self._switch_service_payment: typing.Optional[AsyncSwitchServicePaymentClient] = None
        self._translink_transaction: typing.Optional[AsyncTranslinkTransactionClient] = None
        self._whitelist_sdd: typing.Optional[AsyncWhitelistSddClient] = None
        self._notification_filter_email: typing.Optional[AsyncNotificationFilterEmailClient] = None
        self._notification_filter_push: typing.Optional[AsyncNotificationFilterPushClient] = None
        self._oauth_client: typing.Optional[AsyncOauthClientClient] = None
        self._callback_url: typing.Optional[AsyncCallbackUrlClient] = None
        self._payment_service_provider_draft_payment: typing.Optional[AsyncPaymentServiceProviderDraftPaymentClient] = (
            None
        )
        self._registry_settlement: typing.Optional[AsyncRegistrySettlementClient] = None
        self._reward: typing.Optional[AsyncRewardClient] = None
        self._reward_recipient: typing.Optional[AsyncRewardRecipientClient] = None
        self._reward_sender: typing.Optional[AsyncRewardSenderClient] = None
        self._share_invite_monetary_account_response: typing.Optional[AsyncShareInviteMonetaryAccountResponseClient] = (
            None
        )
        self._token_qr_request_ideal: typing.Optional[AsyncTokenQrRequestIdealClient] = None
        self._token_qr_request_sofort: typing.Optional[AsyncTokenQrRequestSofortClient] = None
        self._transferwise_currency: typing.Optional[AsyncTransferwiseCurrencyClient] = None
        self._transferwise_quote: typing.Optional[AsyncTransferwiseQuoteClient] = None
        self._transferwise_quote_temporary: typing.Optional[AsyncTransferwiseQuoteTemporaryClient] = None
        self._transferwise_recipient: typing.Optional[AsyncTransferwiseRecipientClient] = None
        self._transferwise_recipient_requirement: typing.Optional[AsyncTransferwiseRecipientRequirementClient] = None
        self._transferwise_transfer: typing.Optional[AsyncTransferwiseTransferClient] = None
        self._transferwise_transfer_requirement: typing.Optional[AsyncTransferwiseTransferRequirementClient] = None
        self._transferwise_user: typing.Optional[AsyncTransferwiseUserClient] = None
        self._tree_progress: typing.Optional[AsyncTreeProgressClient] = None
        self._whitelist_sdd_one_off: typing.Optional[AsyncWhitelistSddOneOffClient] = None
        self._whitelist_sdd_recurring: typing.Optional[AsyncWhitelistSddRecurringClient] = None

    @property
    def attachment_public(self):
        if self._attachment_public is None:
            from .attachment_public.client import AsyncAttachmentPublicClient

            self._attachment_public = AsyncAttachmentPublicClient(client_wrapper=self._client_wrapper)
        return self._attachment_public

    @property
    def content(self):
        if self._content is None:
            from .content.client import AsyncContentClient

            self._content = AsyncContentClient(client_wrapper=self._client_wrapper)
        return self._content

    @property
    def avatar(self):
        if self._avatar is None:
            from .avatar.client import AsyncAvatarClient

            self._avatar = AsyncAvatarClient(client_wrapper=self._client_wrapper)
        return self._avatar

    @property
    def device(self):
        if self._device is None:
            from .device.client import AsyncDeviceClient

            self._device = AsyncDeviceClient(client_wrapper=self._client_wrapper)
        return self._device

    @property
    def device_server(self):
        if self._device_server is None:
            from .device_server.client import AsyncDeviceServerClient

            self._device_server = AsyncDeviceServerClient(client_wrapper=self._client_wrapper)
        return self._device_server

    @property
    def installation(self):
        if self._installation is None:
            from .installation.client import AsyncInstallationClient

            self._installation = AsyncInstallationClient(client_wrapper=self._client_wrapper)
        return self._installation

    @property
    def server_public_key(self):
        if self._server_public_key is None:
            from .server_public_key.client import AsyncServerPublicKeyClient

            self._server_public_key = AsyncServerPublicKeyClient(client_wrapper=self._client_wrapper)
        return self._server_public_key

    @property
    def payment_service_provider_credential(self):
        if self._payment_service_provider_credential is None:
            from .payment_service_provider_credential.client import (
                AsyncPaymentServiceProviderCredentialClient,
            )

            self._payment_service_provider_credential = AsyncPaymentServiceProviderCredentialClient(
                client_wrapper=self._client_wrapper
            )
        return self._payment_service_provider_credential

    @property
    def sandbox_user_company(self):
        if self._sandbox_user_company is None:
            from .sandbox_user_company.client import AsyncSandboxUserCompanyClient

            self._sandbox_user_company = AsyncSandboxUserCompanyClient(client_wrapper=self._client_wrapper)
        return self._sandbox_user_company

    @property
    def sandbox_user_person(self):
        if self._sandbox_user_person is None:
            from .sandbox_user_person.client import AsyncSandboxUserPersonClient

            self._sandbox_user_person = AsyncSandboxUserPersonClient(client_wrapper=self._client_wrapper)
        return self._sandbox_user_person

    @property
    def server_error(self):
        if self._server_error is None:
            from .server_error.client import AsyncServerErrorClient

            self._server_error = AsyncServerErrorClient(client_wrapper=self._client_wrapper)
        return self._server_error

    @property
    def session_server(self):
        if self._session_server is None:
            from .session_server.client import AsyncSessionServerClient

            self._session_server = AsyncSessionServerClient(client_wrapper=self._client_wrapper)
        return self._session_server

    @property
    def session(self):
        if self._session is None:
            from .session.client import AsyncSessionClient

            self._session = AsyncSessionClient(client_wrapper=self._client_wrapper)
        return self._session

    @property
    def user(self):
        if self._user is None:
            from .user.client import AsyncUserClient

            self._user = AsyncUserClient(client_wrapper=self._client_wrapper)
        return self._user

    @property
    def user_company(self):
        if self._user_company is None:
            from .user_company.client import AsyncUserCompanyClient

            self._user_company = AsyncUserCompanyClient(client_wrapper=self._client_wrapper)
        return self._user_company

    @property
    def name(self):
        if self._name is None:
            from .name.client import AsyncNameClient

            self._name = AsyncNameClient(client_wrapper=self._client_wrapper)
        return self._name

    @property
    def user_payment_service_provider(self):
        if self._user_payment_service_provider is None:
            from .user_payment_service_provider.client import AsyncUserPaymentServiceProviderClient

            self._user_payment_service_provider = AsyncUserPaymentServiceProviderClient(
                client_wrapper=self._client_wrapper
            )
        return self._user_payment_service_provider

    @property
    def user_person(self):
        if self._user_person is None:
            from .user_person.client import AsyncUserPersonClient

            self._user_person = AsyncUserPersonClient(client_wrapper=self._client_wrapper)
        return self._user_person

    @property
    def attachment(self):
        if self._attachment is None:
            from .attachment.client import AsyncAttachmentClient

            self._attachment = AsyncAttachmentClient(client_wrapper=self._client_wrapper)
        return self._attachment

    @property
    def billing_contract_subscription(self):
        if self._billing_contract_subscription is None:
            from .billing_contract_subscription.client import AsyncBillingContractSubscriptionClient

            self._billing_contract_subscription = AsyncBillingContractSubscriptionClient(
                client_wrapper=self._client_wrapper
            )
        return self._billing_contract_subscription

    @property
    def bunqme_fundraiser_profile(self):
        if self._bunqme_fundraiser_profile is None:
            from .bunqme_fundraiser_profile.client import AsyncBunqmeFundraiserProfileClient

            self._bunqme_fundraiser_profile = AsyncBunqmeFundraiserProfileClient(client_wrapper=self._client_wrapper)
        return self._bunqme_fundraiser_profile

    @property
    def card(self):
        if self._card is None:
            from .card.client import AsyncCardClient

            self._card = AsyncCardClient(client_wrapper=self._client_wrapper)
        return self._card

    @property
    def card_batch(self):
        if self._card_batch is None:
            from .card_batch.client import AsyncCardBatchClient

            self._card_batch = AsyncCardBatchClient(client_wrapper=self._client_wrapper)
        return self._card_batch

    @property
    def card_batch_replace(self):
        if self._card_batch_replace is None:
            from .card_batch_replace.client import AsyncCardBatchReplaceClient

            self._card_batch_replace = AsyncCardBatchReplaceClient(client_wrapper=self._client_wrapper)
        return self._card_batch_replace

    @property
    def card_credit(self):
        if self._card_credit is None:
            from .card_credit.client import AsyncCardCreditClient

            self._card_credit = AsyncCardCreditClient(client_wrapper=self._client_wrapper)
        return self._card_credit

    @property
    def card_debit(self):
        if self._card_debit is None:
            from .card_debit.client import AsyncCardDebitClient

            self._card_debit = AsyncCardDebitClient(client_wrapper=self._client_wrapper)
        return self._card_debit

    @property
    def card_name(self):
        if self._card_name is None:
            from .card_name.client import AsyncCardNameClient

            self._card_name = AsyncCardNameClient(client_wrapper=self._client_wrapper)
        return self._card_name

    @property
    def export_statement_card(self):
        if self._export_statement_card is None:
            from .export_statement_card.client import AsyncExportStatementCardClient

            self._export_statement_card = AsyncExportStatementCardClient(client_wrapper=self._client_wrapper)
        return self._export_statement_card

    @property
    def export_statement_card_csv(self):
        if self._export_statement_card_csv is None:
            from .export_statement_card_csv.client import AsyncExportStatementCardCsvClient

            self._export_statement_card_csv = AsyncExportStatementCardCsvClient(client_wrapper=self._client_wrapper)
        return self._export_statement_card_csv

    @property
    def export_statement_card_pdf(self):
        if self._export_statement_card_pdf is None:
            from .export_statement_card_pdf.client import AsyncExportStatementCardPdfClient

            self._export_statement_card_pdf = AsyncExportStatementCardPdfClient(client_wrapper=self._client_wrapper)
        return self._export_statement_card_pdf

    @property
    def generated_cvc2(self):
        if self._generated_cvc2 is None:
            from .generated_cvc2.client import AsyncGeneratedCvc2Client

            self._generated_cvc2 = AsyncGeneratedCvc2Client(client_wrapper=self._client_wrapper)
        return self._generated_cvc2

    @property
    def replace(self):
        if self._replace is None:
            from .replace.client import AsyncReplaceClient

            self._replace = AsyncReplaceClient(client_wrapper=self._client_wrapper)
        return self._replace

    @property
    def certificate_pinned(self):
        if self._certificate_pinned is None:
            from .certificate_pinned.client import AsyncCertificatePinnedClient

            self._certificate_pinned = AsyncCertificatePinnedClient(client_wrapper=self._client_wrapper)
        return self._certificate_pinned

    @property
    def challenge_request(self):
        if self._challenge_request is None:
            from .challenge_request.client import AsyncChallengeRequestClient

            self._challenge_request = AsyncChallengeRequestClient(client_wrapper=self._client_wrapper)
        return self._challenge_request

    @property
    def company(self):
        if self._company is None:
            from .company.client import AsyncCompanyClient

            self._company = AsyncCompanyClient(client_wrapper=self._client_wrapper)
        return self._company

    @property
    def confirmation_of_funds(self):
        if self._confirmation_of_funds is None:
            from .confirmation_of_funds.client import AsyncConfirmationOfFundsClient

            self._confirmation_of_funds = AsyncConfirmationOfFundsClient(client_wrapper=self._client_wrapper)
        return self._confirmation_of_funds

    @property
    def credential_password_ip(self):
        if self._credential_password_ip is None:
            from .credential_password_ip.client import AsyncCredentialPasswordIpClient

            self._credential_password_ip = AsyncCredentialPasswordIpClient(client_wrapper=self._client_wrapper)
        return self._credential_password_ip

    @property
    def ip(self):
        if self._ip is None:
            from .ip.client import AsyncIpClient

            self._ip = AsyncIpClient(client_wrapper=self._client_wrapper)
        return self._ip

    @property
    def currency_cloud_beneficiary(self):
        if self._currency_cloud_beneficiary is None:
            from .currency_cloud_beneficiary.client import AsyncCurrencyCloudBeneficiaryClient

            self._currency_cloud_beneficiary = AsyncCurrencyCloudBeneficiaryClient(client_wrapper=self._client_wrapper)
        return self._currency_cloud_beneficiary

    @property
    def currency_cloud_beneficiary_requirement(self):
        if self._currency_cloud_beneficiary_requirement is None:
            from .currency_cloud_beneficiary_requirement.client import (
                AsyncCurrencyCloudBeneficiaryRequirementClient,
            )

            self._currency_cloud_beneficiary_requirement = AsyncCurrencyCloudBeneficiaryRequirementClient(
                client_wrapper=self._client_wrapper
            )
        return self._currency_cloud_beneficiary_requirement

    @property
    def event(self):
        if self._event is None:
            from .event.client import AsyncEventClient

            self._event = AsyncEventClient(client_wrapper=self._client_wrapper)
        return self._event

    @property
    def export_annual_overview(self):
        if self._export_annual_overview is None:
            from .export_annual_overview.client import AsyncExportAnnualOverviewClient

            self._export_annual_overview = AsyncExportAnnualOverviewClient(client_wrapper=self._client_wrapper)
        return self._export_annual_overview

    @property
    def feature_announcement(self):
        if self._feature_announcement is None:
            from .feature_announcement.client import AsyncFeatureAnnouncementClient

            self._feature_announcement = AsyncFeatureAnnouncementClient(client_wrapper=self._client_wrapper)
        return self._feature_announcement

    @property
    def insight_preference_date(self):
        if self._insight_preference_date is None:
            from .insight_preference_date.client import AsyncInsightPreferenceDateClient

            self._insight_preference_date = AsyncInsightPreferenceDateClient(client_wrapper=self._client_wrapper)
        return self._insight_preference_date

    @property
    def insights(self):
        if self._insights is None:
            from .insights.client import AsyncInsightsClient

            self._insights = AsyncInsightsClient(client_wrapper=self._client_wrapper)
        return self._insights

    @property
    def insights_search(self):
        if self._insights_search is None:
            from .insights_search.client import AsyncInsightsSearchClient

            self._insights_search = AsyncInsightsSearchClient(client_wrapper=self._client_wrapper)
        return self._insights_search

    @property
    def invoice(self):
        if self._invoice is None:
            from .invoice.client import AsyncInvoiceClient

            self._invoice = AsyncInvoiceClient(client_wrapper=self._client_wrapper)
        return self._invoice

    @property
    def pdf_content(self):
        if self._pdf_content is None:
            from .pdf_content.client import AsyncPdfContentClient

            self._pdf_content = AsyncPdfContentClient(client_wrapper=self._client_wrapper)
        return self._pdf_content

    @property
    def legal_name(self):
        if self._legal_name is None:
            from .legal_name.client import AsyncLegalNameClient

            self._legal_name = AsyncLegalNameClient(client_wrapper=self._client_wrapper)
        return self._legal_name

    @property
    def limit(self):
        if self._limit is None:
            from .limit.client import AsyncLimitClient

            self._limit = AsyncLimitClient(client_wrapper=self._client_wrapper)
        return self._limit

    @property
    def monetary_account(self):
        if self._monetary_account is None:
            from .monetary_account.client import AsyncMonetaryAccountClient

            self._monetary_account = AsyncMonetaryAccountClient(client_wrapper=self._client_wrapper)
        return self._monetary_account

    @property
    def monetary_account_bank(self):
        if self._monetary_account_bank is None:
            from .monetary_account_bank.client import AsyncMonetaryAccountBankClient

            self._monetary_account_bank = AsyncMonetaryAccountBankClient(client_wrapper=self._client_wrapper)
        return self._monetary_account_bank

    @property
    def monetary_account_external(self):
        if self._monetary_account_external is None:
            from .monetary_account_external.client import AsyncMonetaryAccountExternalClient

            self._monetary_account_external = AsyncMonetaryAccountExternalClient(client_wrapper=self._client_wrapper)
        return self._monetary_account_external

    @property
    def monetary_account_joint(self):
        if self._monetary_account_joint is None:
            from .monetary_account_joint.client import AsyncMonetaryAccountJointClient

            self._monetary_account_joint = AsyncMonetaryAccountJointClient(client_wrapper=self._client_wrapper)
        return self._monetary_account_joint

    @property
    def monetary_account_savings(self):
        if self._monetary_account_savings is None:
            from .monetary_account_savings.client import AsyncMonetaryAccountSavingsClient

            self._monetary_account_savings = AsyncMonetaryAccountSavingsClient(client_wrapper=self._client_wrapper)
        return self._monetary_account_savings

    @property
    def note_attachment(self):
        if self._note_attachment is None:
            from .note_attachment.client import AsyncNoteAttachmentClient

            self._note_attachment = AsyncNoteAttachmentClient(client_wrapper=self._client_wrapper)
        return self._note_attachment

    @property
    def note_text(self):
        if self._note_text is None:
            from .note_text.client import AsyncNoteTextClient

            self._note_text = AsyncNoteTextClient(client_wrapper=self._client_wrapper)
        return self._note_text

    @property
    def bunqme_fundraiser_result(self):
        if self._bunqme_fundraiser_result is None:
            from .bunqme_fundraiser_result.client import AsyncBunqmeFundraiserResultClient

            self._bunqme_fundraiser_result = AsyncBunqmeFundraiserResultClient(client_wrapper=self._client_wrapper)
        return self._bunqme_fundraiser_result

    @property
    def bunqme_tab(self):
        if self._bunqme_tab is None:
            from .bunqme_tab.client import AsyncBunqmeTabClient

            self._bunqme_tab = AsyncBunqmeTabClient(client_wrapper=self._client_wrapper)
        return self._bunqme_tab

    @property
    def bunqme_tab_result_response(self):
        if self._bunqme_tab_result_response is None:
            from .bunqme_tab_result_response.client import AsyncBunqmeTabResultResponseClient

            self._bunqme_tab_result_response = AsyncBunqmeTabResultResponseClient(client_wrapper=self._client_wrapper)
        return self._bunqme_tab_result_response

    @property
    def currency_cloud_payment_quote(self):
        if self._currency_cloud_payment_quote is None:
            from .currency_cloud_payment_quote.client import AsyncCurrencyCloudPaymentQuoteClient

            self._currency_cloud_payment_quote = AsyncCurrencyCloudPaymentQuoteClient(
                client_wrapper=self._client_wrapper
            )
        return self._currency_cloud_payment_quote

    @property
    def currency_conversion(self):
        if self._currency_conversion is None:
            from .currency_conversion.client import AsyncCurrencyConversionClient

            self._currency_conversion = AsyncCurrencyConversionClient(client_wrapper=self._client_wrapper)
        return self._currency_conversion

    @property
    def currency_conversion_quote(self):
        if self._currency_conversion_quote is None:
            from .currency_conversion_quote.client import AsyncCurrencyConversionQuoteClient

            self._currency_conversion_quote = AsyncCurrencyConversionQuoteClient(client_wrapper=self._client_wrapper)
        return self._currency_conversion_quote

    @property
    def customer_statement(self):
        if self._customer_statement is None:
            from .customer_statement.client import AsyncCustomerStatementClient

            self._customer_statement = AsyncCustomerStatementClient(client_wrapper=self._client_wrapper)
        return self._customer_statement

    @property
    def draft_payment(self):
        if self._draft_payment is None:
            from .draft_payment.client import AsyncDraftPaymentClient

            self._draft_payment = AsyncDraftPaymentClient(client_wrapper=self._client_wrapper)
        return self._draft_payment

    @property
    def statement(self):
        if self._statement is None:
            from .statement.client import AsyncStatementClient

            self._statement = AsyncStatementClient(client_wrapper=self._client_wrapper)
        return self._statement

    @property
    def export_rib(self):
        if self._export_rib is None:
            from .export_rib.client import AsyncExportRibClient

            self._export_rib = AsyncExportRibClient(client_wrapper=self._client_wrapper)
        return self._export_rib

    @property
    def ideal_merchant_transaction(self):
        if self._ideal_merchant_transaction is None:
            from .ideal_merchant_transaction.client import AsyncIdealMerchantTransactionClient

            self._ideal_merchant_transaction = AsyncIdealMerchantTransactionClient(client_wrapper=self._client_wrapper)
        return self._ideal_merchant_transaction

    @property
    def mastercard_action(self):
        if self._mastercard_action is None:
            from .mastercard_action.client import AsyncMastercardActionClient

            self._mastercard_action = AsyncMastercardActionClient(client_wrapper=self._client_wrapper)
        return self._mastercard_action

    @property
    def payment(self):
        if self._payment is None:
            from .payment.client import AsyncPaymentClient

            self._payment = AsyncPaymentClient(client_wrapper=self._client_wrapper)
        return self._payment

    @property
    def notification_filter_url(self):
        if self._notification_filter_url is None:
            from .notification_filter_url.client import AsyncNotificationFilterUrlClient

            self._notification_filter_url = AsyncNotificationFilterUrlClient(client_wrapper=self._client_wrapper)
        return self._notification_filter_url

    @property
    def payment_auto_allocate(self):
        if self._payment_auto_allocate is None:
            from .payment_auto_allocate.client import AsyncPaymentAutoAllocateClient

            self._payment_auto_allocate = AsyncPaymentAutoAllocateClient(client_wrapper=self._client_wrapper)
        return self._payment_auto_allocate

    @property
    def definition(self):
        if self._definition is None:
            from .definition.client import AsyncDefinitionClient

            self._definition = AsyncDefinitionClient(client_wrapper=self._client_wrapper)
        return self._definition

    @property
    def instance(self):
        if self._instance is None:
            from .instance.client import AsyncInstanceClient

            self._instance = AsyncInstanceClient(client_wrapper=self._client_wrapper)
        return self._instance

    @property
    def payment_batch(self):
        if self._payment_batch is None:
            from .payment_batch.client import AsyncPaymentBatchClient

            self._payment_batch = AsyncPaymentBatchClient(client_wrapper=self._client_wrapper)
        return self._payment_batch

    @property
    def request_inquiry(self):
        if self._request_inquiry is None:
            from .request_inquiry.client import AsyncRequestInquiryClient

            self._request_inquiry = AsyncRequestInquiryClient(client_wrapper=self._client_wrapper)
        return self._request_inquiry

    @property
    def request_inquiry_batch(self):
        if self._request_inquiry_batch is None:
            from .request_inquiry_batch.client import AsyncRequestInquiryBatchClient

            self._request_inquiry_batch = AsyncRequestInquiryBatchClient(client_wrapper=self._client_wrapper)
        return self._request_inquiry_batch

    @property
    def request_response(self):
        if self._request_response is None:
            from .request_response.client import AsyncRequestResponseClient

            self._request_response = AsyncRequestResponseClient(client_wrapper=self._client_wrapper)
        return self._request_response

    @property
    def schedule(self):
        if self._schedule is None:
            from .schedule.client import AsyncScheduleClient

            self._schedule = AsyncScheduleClient(client_wrapper=self._client_wrapper)
        return self._schedule

    @property
    def schedule_payment(self):
        if self._schedule_payment is None:
            from .schedule_payment.client import AsyncSchedulePaymentClient

            self._schedule_payment = AsyncSchedulePaymentClient(client_wrapper=self._client_wrapper)
        return self._schedule_payment

    @property
    def schedule_payment_batch(self):
        if self._schedule_payment_batch is None:
            from .schedule_payment_batch.client import AsyncSchedulePaymentBatchClient

            self._schedule_payment_batch = AsyncSchedulePaymentBatchClient(client_wrapper=self._client_wrapper)
        return self._schedule_payment_batch

    @property
    def schedule_instance(self):
        if self._schedule_instance is None:
            from .schedule_instance.client import AsyncScheduleInstanceClient

            self._schedule_instance = AsyncScheduleInstanceClient(client_wrapper=self._client_wrapper)
        return self._schedule_instance

    @property
    def share_invite_monetary_account_inquiry(self):
        if self._share_invite_monetary_account_inquiry is None:
            from .share_invite_monetary_account_inquiry.client import (
                AsyncShareInviteMonetaryAccountInquiryClient,
            )

            self._share_invite_monetary_account_inquiry = AsyncShareInviteMonetaryAccountInquiryClient(
                client_wrapper=self._client_wrapper
            )
        return self._share_invite_monetary_account_inquiry

    @property
    def sofort_merchant_transaction(self):
        if self._sofort_merchant_transaction is None:
            from .sofort_merchant_transaction.client import AsyncSofortMerchantTransactionClient

            self._sofort_merchant_transaction = AsyncSofortMerchantTransactionClient(
                client_wrapper=self._client_wrapper
            )
        return self._sofort_merchant_transaction

    @property
    def switch_service_payment(self):
        if self._switch_service_payment is None:
            from .switch_service_payment.client import AsyncSwitchServicePaymentClient

            self._switch_service_payment = AsyncSwitchServicePaymentClient(client_wrapper=self._client_wrapper)
        return self._switch_service_payment

    @property
    def translink_transaction(self):
        if self._translink_transaction is None:
            from .translink_transaction.client import AsyncTranslinkTransactionClient

            self._translink_transaction = AsyncTranslinkTransactionClient(client_wrapper=self._client_wrapper)
        return self._translink_transaction

    @property
    def whitelist_sdd(self):
        if self._whitelist_sdd is None:
            from .whitelist_sdd.client import AsyncWhitelistSddClient

            self._whitelist_sdd = AsyncWhitelistSddClient(client_wrapper=self._client_wrapper)
        return self._whitelist_sdd

    @property
    def notification_filter_email(self):
        if self._notification_filter_email is None:
            from .notification_filter_email.client import AsyncNotificationFilterEmailClient

            self._notification_filter_email = AsyncNotificationFilterEmailClient(client_wrapper=self._client_wrapper)
        return self._notification_filter_email

    @property
    def notification_filter_push(self):
        if self._notification_filter_push is None:
            from .notification_filter_push.client import AsyncNotificationFilterPushClient

            self._notification_filter_push = AsyncNotificationFilterPushClient(client_wrapper=self._client_wrapper)
        return self._notification_filter_push

    @property
    def oauth_client(self):
        if self._oauth_client is None:
            from .oauth_client.client import AsyncOauthClientClient

            self._oauth_client = AsyncOauthClientClient(client_wrapper=self._client_wrapper)
        return self._oauth_client

    @property
    def callback_url(self):
        if self._callback_url is None:
            from .callback_url.client import AsyncCallbackUrlClient

            self._callback_url = AsyncCallbackUrlClient(client_wrapper=self._client_wrapper)
        return self._callback_url

    @property
    def payment_service_provider_draft_payment(self):
        if self._payment_service_provider_draft_payment is None:
            from .payment_service_provider_draft_payment.client import (
                AsyncPaymentServiceProviderDraftPaymentClient,
            )

            self._payment_service_provider_draft_payment = AsyncPaymentServiceProviderDraftPaymentClient(
                client_wrapper=self._client_wrapper
            )
        return self._payment_service_provider_draft_payment

    @property
    def registry_settlement(self):
        if self._registry_settlement is None:
            from .registry_settlement.client import AsyncRegistrySettlementClient

            self._registry_settlement = AsyncRegistrySettlementClient(client_wrapper=self._client_wrapper)
        return self._registry_settlement

    @property
    def reward(self):
        if self._reward is None:
            from .reward.client import AsyncRewardClient

            self._reward = AsyncRewardClient(client_wrapper=self._client_wrapper)
        return self._reward

    @property
    def reward_recipient(self):
        if self._reward_recipient is None:
            from .reward_recipient.client import AsyncRewardRecipientClient

            self._reward_recipient = AsyncRewardRecipientClient(client_wrapper=self._client_wrapper)
        return self._reward_recipient

    @property
    def reward_sender(self):
        if self._reward_sender is None:
            from .reward_sender.client import AsyncRewardSenderClient

            self._reward_sender = AsyncRewardSenderClient(client_wrapper=self._client_wrapper)
        return self._reward_sender

    @property
    def share_invite_monetary_account_response(self):
        if self._share_invite_monetary_account_response is None:
            from .share_invite_monetary_account_response.client import (
                AsyncShareInviteMonetaryAccountResponseClient,
            )

            self._share_invite_monetary_account_response = AsyncShareInviteMonetaryAccountResponseClient(
                client_wrapper=self._client_wrapper
            )
        return self._share_invite_monetary_account_response

    @property
    def token_qr_request_ideal(self):
        if self._token_qr_request_ideal is None:
            from .token_qr_request_ideal.client import AsyncTokenQrRequestIdealClient

            self._token_qr_request_ideal = AsyncTokenQrRequestIdealClient(client_wrapper=self._client_wrapper)
        return self._token_qr_request_ideal

    @property
    def token_qr_request_sofort(self):
        if self._token_qr_request_sofort is None:
            from .token_qr_request_sofort.client import AsyncTokenQrRequestSofortClient

            self._token_qr_request_sofort = AsyncTokenQrRequestSofortClient(client_wrapper=self._client_wrapper)
        return self._token_qr_request_sofort

    @property
    def transferwise_currency(self):
        if self._transferwise_currency is None:
            from .transferwise_currency.client import AsyncTransferwiseCurrencyClient

            self._transferwise_currency = AsyncTransferwiseCurrencyClient(client_wrapper=self._client_wrapper)
        return self._transferwise_currency

    @property
    def transferwise_quote(self):
        if self._transferwise_quote is None:
            from .transferwise_quote.client import AsyncTransferwiseQuoteClient

            self._transferwise_quote = AsyncTransferwiseQuoteClient(client_wrapper=self._client_wrapper)
        return self._transferwise_quote

    @property
    def transferwise_quote_temporary(self):
        if self._transferwise_quote_temporary is None:
            from .transferwise_quote_temporary.client import AsyncTransferwiseQuoteTemporaryClient

            self._transferwise_quote_temporary = AsyncTransferwiseQuoteTemporaryClient(
                client_wrapper=self._client_wrapper
            )
        return self._transferwise_quote_temporary

    @property
    def transferwise_recipient(self):
        if self._transferwise_recipient is None:
            from .transferwise_recipient.client import AsyncTransferwiseRecipientClient

            self._transferwise_recipient = AsyncTransferwiseRecipientClient(client_wrapper=self._client_wrapper)
        return self._transferwise_recipient

    @property
    def transferwise_recipient_requirement(self):
        if self._transferwise_recipient_requirement is None:
            from .transferwise_recipient_requirement.client import (
                AsyncTransferwiseRecipientRequirementClient,
            )

            self._transferwise_recipient_requirement = AsyncTransferwiseRecipientRequirementClient(
                client_wrapper=self._client_wrapper
            )
        return self._transferwise_recipient_requirement

    @property
    def transferwise_transfer(self):
        if self._transferwise_transfer is None:
            from .transferwise_transfer.client import AsyncTransferwiseTransferClient

            self._transferwise_transfer = AsyncTransferwiseTransferClient(client_wrapper=self._client_wrapper)
        return self._transferwise_transfer

    @property
    def transferwise_transfer_requirement(self):
        if self._transferwise_transfer_requirement is None:
            from .transferwise_transfer_requirement.client import (
                AsyncTransferwiseTransferRequirementClient,
            )

            self._transferwise_transfer_requirement = AsyncTransferwiseTransferRequirementClient(
                client_wrapper=self._client_wrapper
            )
        return self._transferwise_transfer_requirement

    @property
    def transferwise_user(self):
        if self._transferwise_user is None:
            from .transferwise_user.client import AsyncTransferwiseUserClient

            self._transferwise_user = AsyncTransferwiseUserClient(client_wrapper=self._client_wrapper)
        return self._transferwise_user

    @property
    def tree_progress(self):
        if self._tree_progress is None:
            from .tree_progress.client import AsyncTreeProgressClient

            self._tree_progress = AsyncTreeProgressClient(client_wrapper=self._client_wrapper)
        return self._tree_progress

    @property
    def whitelist_sdd_one_off(self):
        if self._whitelist_sdd_one_off is None:
            from .whitelist_sdd_one_off.client import AsyncWhitelistSddOneOffClient

            self._whitelist_sdd_one_off = AsyncWhitelistSddOneOffClient(client_wrapper=self._client_wrapper)
        return self._whitelist_sdd_one_off

    @property
    def whitelist_sdd_recurring(self):
        if self._whitelist_sdd_recurring is None:
            from .whitelist_sdd_recurring.client import AsyncWhitelistSddRecurringClient

            self._whitelist_sdd_recurring = AsyncWhitelistSddRecurringClient(client_wrapper=self._client_wrapper)
        return self._whitelist_sdd_recurring


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")

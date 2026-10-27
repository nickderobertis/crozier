

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChatMessageFromUserUserIdentityType(enum.StrEnum):
    AAD_USER = "aadUser"
    ON_PREMISE_AAD_USER = "onPremiseAadUser"
    ANONYMOUS_GUEST = "anonymousGuest"
    FEDERATED_USER = "federatedUser"
    PERSONAL_MICROSOFT_ACCOUNT_USER = "personalMicrosoftAccountUser"
    SKYPE_USER = "skypeUser"
    PHONE_USER = "phoneUser"
    EMAIL_USER = "emailUser"
    AZURE_COMMUNICATION_SERVICES_USER = "azureCommunicationServicesUser"

    def visit(
        self,
        aad_user: typing.Callable[[], T_Result],
        on_premise_aad_user: typing.Callable[[], T_Result],
        anonymous_guest: typing.Callable[[], T_Result],
        federated_user: typing.Callable[[], T_Result],
        personal_microsoft_account_user: typing.Callable[[], T_Result],
        skype_user: typing.Callable[[], T_Result],
        phone_user: typing.Callable[[], T_Result],
        email_user: typing.Callable[[], T_Result],
        azure_communication_services_user: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ChatMessageFromUserUserIdentityType.AAD_USER:
            return aad_user()
        if self is ChatMessageFromUserUserIdentityType.ON_PREMISE_AAD_USER:
            return on_premise_aad_user()
        if self is ChatMessageFromUserUserIdentityType.ANONYMOUS_GUEST:
            return anonymous_guest()
        if self is ChatMessageFromUserUserIdentityType.FEDERATED_USER:
            return federated_user()
        if self is ChatMessageFromUserUserIdentityType.PERSONAL_MICROSOFT_ACCOUNT_USER:
            return personal_microsoft_account_user()
        if self is ChatMessageFromUserUserIdentityType.SKYPE_USER:
            return skype_user()
        if self is ChatMessageFromUserUserIdentityType.PHONE_USER:
            return phone_user()
        if self is ChatMessageFromUserUserIdentityType.EMAIL_USER:
            return email_user()
        if self is ChatMessageFromUserUserIdentityType.AZURE_COMMUNICATION_SERVICES_USER:
            return azure_communication_services_user()

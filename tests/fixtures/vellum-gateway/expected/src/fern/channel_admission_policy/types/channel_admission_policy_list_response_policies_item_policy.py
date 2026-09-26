

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ChannelAdmissionPolicyListResponsePoliciesItemPolicy(enum.StrEnum):
    NO_ONE = "no_one"
    GUARDIAN_ONLY = "guardian_only"
    TRUSTED_CONTACTS = "trusted_contacts"
    ANY_CONTACT = "any_contact"
    STRANGERS = "strangers"

    def visit(
        self,
        no_one: typing.Callable[[], T_Result],
        guardian_only: typing.Callable[[], T_Result],
        trusted_contacts: typing.Callable[[], T_Result],
        any_contact: typing.Callable[[], T_Result],
        strangers: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ChannelAdmissionPolicyListResponsePoliciesItemPolicy.NO_ONE:
            return no_one()
        if self is ChannelAdmissionPolicyListResponsePoliciesItemPolicy.GUARDIAN_ONLY:
            return guardian_only()
        if self is ChannelAdmissionPolicyListResponsePoliciesItemPolicy.TRUSTED_CONTACTS:
            return trusted_contacts()
        if self is ChannelAdmissionPolicyListResponsePoliciesItemPolicy.ANY_CONTACT:
            return any_contact()
        if self is ChannelAdmissionPolicyListResponsePoliciesItemPolicy.STRANGERS:
            return strangers()

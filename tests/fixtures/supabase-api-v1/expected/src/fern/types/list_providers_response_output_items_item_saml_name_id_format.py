

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ListProvidersResponseOutputItemsItemSamlNameIdFormat(enum.StrEnum):
    URN_OASIS_NAMES_TC_SAML11NAMEID_FORMAT_UNSPECIFIED = "urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified"
    URN_OASIS_NAMES_TC_SAML20NAMEID_FORMAT_TRANSIENT = "urn:oasis:names:tc:SAML:2.0:nameid-format:transient"
    URN_OASIS_NAMES_TC_SAML11NAMEID_FORMAT_EMAIL_ADDRESS = "urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress"
    URN_OASIS_NAMES_TC_SAML20NAMEID_FORMAT_PERSISTENT = "urn:oasis:names:tc:SAML:2.0:nameid-format:persistent"

    def visit(
        self,
        urn_oasis_names_tc_saml11nameid_format_unspecified: typing.Callable[[], T_Result],
        urn_oasis_names_tc_saml20nameid_format_transient: typing.Callable[[], T_Result],
        urn_oasis_names_tc_saml11nameid_format_email_address: typing.Callable[[], T_Result],
        urn_oasis_names_tc_saml20nameid_format_persistent: typing.Callable[[], T_Result],
    ) -> T_Result:
        if (
            self
            is ListProvidersResponseOutputItemsItemSamlNameIdFormat.URN_OASIS_NAMES_TC_SAML11NAMEID_FORMAT_UNSPECIFIED
        ):
            return urn_oasis_names_tc_saml11nameid_format_unspecified()
        if (
            self
            is ListProvidersResponseOutputItemsItemSamlNameIdFormat.URN_OASIS_NAMES_TC_SAML20NAMEID_FORMAT_TRANSIENT
        ):
            return urn_oasis_names_tc_saml20nameid_format_transient()
        if (
            self
            is ListProvidersResponseOutputItemsItemSamlNameIdFormat.URN_OASIS_NAMES_TC_SAML11NAMEID_FORMAT_EMAIL_ADDRESS
        ):
            return urn_oasis_names_tc_saml11nameid_format_email_address()
        if (
            self
            is ListProvidersResponseOutputItemsItemSamlNameIdFormat.URN_OASIS_NAMES_TC_SAML20NAMEID_FORMAT_PERSISTENT
        ):
            return urn_oasis_names_tc_saml20nameid_format_persistent()

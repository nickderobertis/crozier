

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ComplianceDocumentType(enum.StrEnum):
    """
    Well-known compliance document types. When idType is COMPLIANCE_DOCUMENT, the idValue SHOULD be one of these values.
    """

    SOC2TYPE_I = "SOC_2_TYPE_I"
    SOC2TYPE_II = "SOC_2_TYPE_II"
    SOC3 = "SOC_3"
    ISO27001 = "ISO_27001"
    ISO27017 = "ISO_27017"
    ISO27018 = "ISO_27018"
    ISO27701 = "ISO_27701"
    ISO42001 = "ISO_42001"
    PCI_DSS = "PCI_DSS"
    HIPAA = "HIPAA"
    FED_RAMP = "FedRAMP"
    GDPR = "GDPR"
    CSA_STAR = "CSA_STAR"
    NIST80053 = "NIST_800_53"
    NIST800171 = "NIST_800_171"
    CMMC = "CMMC"
    HITRUST = "HITRUST"
    TISAX = "TISAX"
    CYBER_ESSENTIALS = "CYBER_ESSENTIALS"
    CYBER_ESSENTIALS_PLUS = "CYBER_ESSENTIALS_PLUS"

    def visit(
        self,
        soc2type_i: typing.Callable[[], T_Result],
        soc2type_ii: typing.Callable[[], T_Result],
        soc3: typing.Callable[[], T_Result],
        iso27001: typing.Callable[[], T_Result],
        iso27017: typing.Callable[[], T_Result],
        iso27018: typing.Callable[[], T_Result],
        iso27701: typing.Callable[[], T_Result],
        iso42001: typing.Callable[[], T_Result],
        pci_dss: typing.Callable[[], T_Result],
        hipaa: typing.Callable[[], T_Result],
        fed_ramp: typing.Callable[[], T_Result],
        gdpr: typing.Callable[[], T_Result],
        csa_star: typing.Callable[[], T_Result],
        nist80053: typing.Callable[[], T_Result],
        nist800171: typing.Callable[[], T_Result],
        cmmc: typing.Callable[[], T_Result],
        hitrust: typing.Callable[[], T_Result],
        tisax: typing.Callable[[], T_Result],
        cyber_essentials: typing.Callable[[], T_Result],
        cyber_essentials_plus: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ComplianceDocumentType.SOC2TYPE_I:
            return soc2type_i()
        if self is ComplianceDocumentType.SOC2TYPE_II:
            return soc2type_ii()
        if self is ComplianceDocumentType.SOC3:
            return soc3()
        if self is ComplianceDocumentType.ISO27001:
            return iso27001()
        if self is ComplianceDocumentType.ISO27017:
            return iso27017()
        if self is ComplianceDocumentType.ISO27018:
            return iso27018()
        if self is ComplianceDocumentType.ISO27701:
            return iso27701()
        if self is ComplianceDocumentType.ISO42001:
            return iso42001()
        if self is ComplianceDocumentType.PCI_DSS:
            return pci_dss()
        if self is ComplianceDocumentType.HIPAA:
            return hipaa()
        if self is ComplianceDocumentType.FED_RAMP:
            return fed_ramp()
        if self is ComplianceDocumentType.GDPR:
            return gdpr()
        if self is ComplianceDocumentType.CSA_STAR:
            return csa_star()
        if self is ComplianceDocumentType.NIST80053:
            return nist80053()
        if self is ComplianceDocumentType.NIST800171:
            return nist800171()
        if self is ComplianceDocumentType.CMMC:
            return cmmc()
        if self is ComplianceDocumentType.HITRUST:
            return hitrust()
        if self is ComplianceDocumentType.TISAX:
            return tisax()
        if self is ComplianceDocumentType.CYBER_ESSENTIALS:
            return cyber_essentials()
        if self is ComplianceDocumentType.CYBER_ESSENTIALS_PLUS:
            return cyber_essentials_plus()

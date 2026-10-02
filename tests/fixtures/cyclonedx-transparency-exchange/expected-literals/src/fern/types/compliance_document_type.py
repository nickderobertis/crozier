

import typing

ComplianceDocumentType = typing.Union[
    typing.Literal[
        "SOC_2_TYPE_I",
        "SOC_2_TYPE_II",
        "SOC_3",
        "ISO_27001",
        "ISO_27017",
        "ISO_27018",
        "ISO_27701",
        "ISO_42001",
        "PCI_DSS",
        "HIPAA",
        "FedRAMP",
        "GDPR",
        "CSA_STAR",
        "NIST_800_53",
        "NIST_800_171",
        "CMMC",
        "HITRUST",
        "TISAX",
        "CYBER_ESSENTIALS",
        "CYBER_ESSENTIALS_PLUS",
    ],
    typing.Any,
]

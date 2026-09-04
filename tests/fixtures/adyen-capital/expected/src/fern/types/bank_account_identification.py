

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .additional_bank_identification import AdditionalBankIdentification
from .ca_local_bank_account_type import CaLocalBankAccountType
from .us_local_bank_account_type import UsLocalBankAccountType


class BankAccountIdentification_AuLocal(UniversalBaseModel):
    type: typing.Literal["auLocal"] = "auLocal"
    account_number: typing_extensions.Annotated[
        str, FieldMetadata(alias="accountNumber"), pydantic.Field(alias="accountNumber")
    ]
    bsb_code: typing_extensions.Annotated[str, FieldMetadata(alias="bsbCode"), pydantic.Field(alias="bsbCode")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class BankAccountIdentification_BrLocal(UniversalBaseModel):
    type: typing.Literal["brLocal"] = "brLocal"
    account_number: typing_extensions.Annotated[
        str, FieldMetadata(alias="accountNumber"), pydantic.Field(alias="accountNumber")
    ]
    bank_code: typing_extensions.Annotated[str, FieldMetadata(alias="bankCode"), pydantic.Field(alias="bankCode")]
    branch_number: typing_extensions.Annotated[
        str, FieldMetadata(alias="branchNumber"), pydantic.Field(alias="branchNumber")
    ]
    ispb: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class BankAccountIdentification_CaLocal(UniversalBaseModel):
    type: typing.Literal["caLocal"] = "caLocal"
    account_number: typing_extensions.Annotated[
        str, FieldMetadata(alias="accountNumber"), pydantic.Field(alias="accountNumber")
    ]
    account_type: typing_extensions.Annotated[
        typing.Optional[CaLocalBankAccountType], FieldMetadata(alias="accountType"), pydantic.Field(alias="accountType")
    ] = None
    institution_number: typing_extensions.Annotated[
        str, FieldMetadata(alias="institutionNumber"), pydantic.Field(alias="institutionNumber")
    ]
    transit_number: typing_extensions.Annotated[
        str, FieldMetadata(alias="transitNumber"), pydantic.Field(alias="transitNumber")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class BankAccountIdentification_CzLocal(UniversalBaseModel):
    type: typing.Literal["czLocal"] = "czLocal"
    account_number: typing_extensions.Annotated[
        str, FieldMetadata(alias="accountNumber"), pydantic.Field(alias="accountNumber")
    ]
    bank_code: typing_extensions.Annotated[str, FieldMetadata(alias="bankCode"), pydantic.Field(alias="bankCode")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class BankAccountIdentification_DkLocal(UniversalBaseModel):
    type: typing.Literal["dkLocal"] = "dkLocal"
    account_number: typing_extensions.Annotated[
        str, FieldMetadata(alias="accountNumber"), pydantic.Field(alias="accountNumber")
    ]
    bank_code: typing_extensions.Annotated[str, FieldMetadata(alias="bankCode"), pydantic.Field(alias="bankCode")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class BankAccountIdentification_HkLocal(UniversalBaseModel):
    type: typing.Literal["hkLocal"] = "hkLocal"
    account_number: typing_extensions.Annotated[
        str, FieldMetadata(alias="accountNumber"), pydantic.Field(alias="accountNumber")
    ]
    clearing_code: typing_extensions.Annotated[
        str, FieldMetadata(alias="clearingCode"), pydantic.Field(alias="clearingCode")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class BankAccountIdentification_HuLocal(UniversalBaseModel):
    type: typing.Literal["huLocal"] = "huLocal"
    account_number: typing_extensions.Annotated[
        str, FieldMetadata(alias="accountNumber"), pydantic.Field(alias="accountNumber")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class BankAccountIdentification_Iban(UniversalBaseModel):
    type: typing.Literal["iban"] = "iban"
    bic: typing.Optional[str] = None
    iban: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class BankAccountIdentification_NoLocal(UniversalBaseModel):
    type: typing.Literal["noLocal"] = "noLocal"
    account_number: typing_extensions.Annotated[
        str, FieldMetadata(alias="accountNumber"), pydantic.Field(alias="accountNumber")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class BankAccountIdentification_NumberAndBic(UniversalBaseModel):
    type: typing.Literal["numberAndBic"] = "numberAndBic"
    account_number: typing_extensions.Annotated[
        str, FieldMetadata(alias="accountNumber"), pydantic.Field(alias="accountNumber")
    ]
    additional_bank_identification: typing_extensions.Annotated[
        typing.Optional[AdditionalBankIdentification],
        FieldMetadata(alias="additionalBankIdentification"),
        pydantic.Field(alias="additionalBankIdentification"),
    ] = None
    bic: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class BankAccountIdentification_NzLocal(UniversalBaseModel):
    type: typing.Literal["nzLocal"] = "nzLocal"
    account_number: typing_extensions.Annotated[
        str, FieldMetadata(alias="accountNumber"), pydantic.Field(alias="accountNumber")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class BankAccountIdentification_PlLocal(UniversalBaseModel):
    type: typing.Literal["plLocal"] = "plLocal"
    account_number: typing_extensions.Annotated[
        str, FieldMetadata(alias="accountNumber"), pydantic.Field(alias="accountNumber")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class BankAccountIdentification_SeLocal(UniversalBaseModel):
    type: typing.Literal["seLocal"] = "seLocal"
    account_number: typing_extensions.Annotated[
        str, FieldMetadata(alias="accountNumber"), pydantic.Field(alias="accountNumber")
    ]
    clearing_number: typing_extensions.Annotated[
        str, FieldMetadata(alias="clearingNumber"), pydantic.Field(alias="clearingNumber")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class BankAccountIdentification_SgLocal(UniversalBaseModel):
    type: typing.Literal["sgLocal"] = "sgLocal"
    account_number: typing_extensions.Annotated[
        str, FieldMetadata(alias="accountNumber"), pydantic.Field(alias="accountNumber")
    ]
    bic: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class BankAccountIdentification_UkLocal(UniversalBaseModel):
    type: typing.Literal["ukLocal"] = "ukLocal"
    account_number: typing_extensions.Annotated[
        str, FieldMetadata(alias="accountNumber"), pydantic.Field(alias="accountNumber")
    ]
    sort_code: typing_extensions.Annotated[str, FieldMetadata(alias="sortCode"), pydantic.Field(alias="sortCode")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class BankAccountIdentification_UsLocal(UniversalBaseModel):
    type: typing.Literal["usLocal"] = "usLocal"
    account_number: typing_extensions.Annotated[
        str, FieldMetadata(alias="accountNumber"), pydantic.Field(alias="accountNumber")
    ]
    account_type: typing_extensions.Annotated[
        typing.Optional[UsLocalBankAccountType], FieldMetadata(alias="accountType"), pydantic.Field(alias="accountType")
    ] = None
    routing_number: typing_extensions.Annotated[
        str, FieldMetadata(alias="routingNumber"), pydantic.Field(alias="routingNumber")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


BankAccountIdentification = typing_extensions.Annotated[
    typing.Union[
        BankAccountIdentification_AuLocal,
        BankAccountIdentification_BrLocal,
        BankAccountIdentification_CaLocal,
        BankAccountIdentification_CzLocal,
        BankAccountIdentification_DkLocal,
        BankAccountIdentification_HkLocal,
        BankAccountIdentification_HuLocal,
        BankAccountIdentification_Iban,
        BankAccountIdentification_NoLocal,
        BankAccountIdentification_NumberAndBic,
        BankAccountIdentification_NzLocal,
        BankAccountIdentification_PlLocal,
        BankAccountIdentification_SeLocal,
        BankAccountIdentification_SgLocal,
        BankAccountIdentification_UkLocal,
        BankAccountIdentification_UsLocal,
    ],
    pydantic.Field(discriminator="type"),
]

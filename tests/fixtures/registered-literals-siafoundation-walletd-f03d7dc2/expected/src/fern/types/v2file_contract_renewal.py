

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .currency import Currency
from .siacoin_output import SiacoinOutput
from .signature import Signature
from .v2file_contract import V2FileContract


class V2FileContractRenewal(UniversalBaseModel):
    final_renter_output: typing_extensions.Annotated[
        SiacoinOutput, FieldMetadata(alias="finalRenterOutput"), pydantic.Field(alias="finalRenterOutput")
    ]
    final_host_output: typing_extensions.Annotated[
        SiacoinOutput, FieldMetadata(alias="finalHostOutput"), pydantic.Field(alias="finalHostOutput")
    ]
    renter_rollover: typing_extensions.Annotated[
        Currency, FieldMetadata(alias="renterRollover"), pydantic.Field(alias="renterRollover")
    ]
    host_rollover: typing_extensions.Annotated[
        Currency, FieldMetadata(alias="hostRollover"), pydantic.Field(alias="hostRollover")
    ]
    new_contract: typing_extensions.Annotated[
        V2FileContract, FieldMetadata(alias="newContract"), pydantic.Field(alias="newContract")
    ]
    renter_signature: typing_extensions.Annotated[
        Signature, FieldMetadata(alias="renterSignature"), pydantic.Field(alias="renterSignature")
    ]
    host_signature: typing_extensions.Annotated[
        Signature, FieldMetadata(alias="hostSignature"), pydantic.Field(alias="hostSignature")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

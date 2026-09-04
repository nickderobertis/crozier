

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CzLocalAccountIdentification(UniversalBaseModel):
    account_number: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="accountNumber"),
        pydantic.Field(
            alias="accountNumber",
            description="The 2- to 16-digit bank account number (Číslo účtu) in the following format:\n\n- The optional prefix (předčíslí).\n\n- The required second part (základní část) which must be at least two non-zero digits.\n\nExamples:\n\n- **19-123457** (with prefix)\n\n- **123457** (without prefix)\n\n- **000019-0000123457** (with prefix, normalized)\n\n- **000000-0000123457** (without prefix, normalized)",
        ),
    ]
    """
    The 2- to 16-digit bank account number (Číslo účtu) in the following format:
    
    - The optional prefix (předčíslí).
    
    - The required second part (základní část) which must be at least two non-zero digits.
    
    Examples:
    
    - **19-123457** (with prefix)
    
    - **123457** (without prefix)
    
    - **000019-0000123457** (with prefix, normalized)
    
    - **000000-0000123457** (without prefix, normalized)
    """

    bank_code: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="bankCode"),
        pydantic.Field(
            alias="bankCode", description="The 4-digit bank code (Kód banky), without separators or whitespace."
        ),
    ]
    """
    The 4-digit bank code (Kód banky), without separators or whitespace.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

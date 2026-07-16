

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ProprietaryBankTransactionCodeStructure1(UniversalBaseModel):
    """
    Set of elements to fully identify a proprietary bank transaction code.
    """

    code: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="Code"),
        pydantic.Field(
            alias="Code", description="Proprietary bank transaction code to identify the underlying transaction."
        ),
    ]
    """
    Proprietary bank transaction code to identify the underlying transaction.
    """

    issuer: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Issuer"),
        pydantic.Field(
            alias="Issuer", description="Identification of the issuer of the proprietary bank transaction code."
        ),
    ] = None
    """
    Identification of the issuer of the proprietary bank transaction code.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

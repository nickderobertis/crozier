

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class OtoroshiSslPkiModelsGenCsrResponse(UniversalBaseModel):
    """
    Response for a csr generation operation
    """

    csr: typing.Optional[str] = pydantic.Field(default=None)
    """
    CSR (PEM encoded)
    """

    public_key: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="publicKey"),
        pydantic.Field(alias="publicKey", description="Public key (PEM encoded)"),
    ] = None
    """
    Public key (PEM encoded)
    """

    private_key: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="privateKey"),
        pydantic.Field(alias="privateKey", description="Private key (PEM encoded)"),
    ] = None
    """
    Private key (PEM encoded)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

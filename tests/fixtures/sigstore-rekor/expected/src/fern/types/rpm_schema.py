

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .rpm_schema_package import RpmSchemaPackage
from .rpm_schema_public_key import RpmSchemaPublicKey


class RpmSchema(UniversalBaseModel):
    """
    Schema for RPM entries
    """

    public_key: typing_extensions.Annotated[
        RpmSchemaPublicKey,
        FieldMetadata(alias="publicKey"),
        pydantic.Field(alias="publicKey", description="The PGP public key that can verify the RPM signature"),
    ]
    """
    The PGP public key that can verify the RPM signature
    """

    package: RpmSchemaPackage = pydantic.Field()
    """
    Information about the package associated with the entry
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

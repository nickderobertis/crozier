

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .alpine_package_schema_package import AlpinePackageSchemaPackage
from .alpine_package_schema_public_key import AlpinePackageSchemaPublicKey


class AlpinePackageSchema(UniversalBaseModel):
    """
    Schema for Alpine Package entries
    """

    public_key: typing_extensions.Annotated[
        AlpinePackageSchemaPublicKey,
        FieldMetadata(alias="publicKey"),
        pydantic.Field(alias="publicKey", description="The public key that can verify the package signature"),
    ]
    """
    The public key that can verify the package signature
    """

    package: AlpinePackageSchemaPackage = pydantic.Field()
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

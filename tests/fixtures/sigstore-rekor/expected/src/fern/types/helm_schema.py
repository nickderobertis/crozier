

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .helm_schema_chart import HelmSchemaChart
from .helm_schema_public_key import HelmSchemaPublicKey


class HelmSchema(UniversalBaseModel):
    """
    Schema for Helm object
    """

    public_key: typing_extensions.Annotated[
        HelmSchemaPublicKey,
        FieldMetadata(alias="publicKey"),
        pydantic.Field(alias="publicKey", description="The public key that can verify the package signature"),
    ]
    """
    The public key that can verify the package signature
    """

    chart: HelmSchemaChart = pydantic.Field()
    """
    Information about the Helm chart associated with the entry
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

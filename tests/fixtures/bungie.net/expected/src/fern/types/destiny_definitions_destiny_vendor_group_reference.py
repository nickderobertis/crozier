

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsDestinyVendorGroupReference(UniversalBaseModel):
    vendor_group_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="vendorGroupHash")] = (
        pydantic.Field(default=None)
    )
    """
    The DestinyVendorGroupDefinition to which this Vendor can belong.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

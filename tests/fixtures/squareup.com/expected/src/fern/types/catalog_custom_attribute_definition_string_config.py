

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CatalogCustomAttributeDefinitionStringConfig(UniversalBaseModel):
    """
    Configuration associated with Custom Attribute Definitions of type `STRING`.
    """

    enforce_uniqueness: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If true, each Custom Attribute instance associated with this Custom Attribute
    Definition must have a unique value within the seller's catalog. For
    example, this may be used for a value like a SKU that should not be
    duplicated within a seller's catalog. May not be modified after the
    definition has been created.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

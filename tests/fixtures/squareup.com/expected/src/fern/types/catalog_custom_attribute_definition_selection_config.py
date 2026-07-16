

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .catalog_custom_attribute_definition_selection_config_custom_attribute_selection import (
    CatalogCustomAttributeDefinitionSelectionConfigCustomAttributeSelection,
)


class CatalogCustomAttributeDefinitionSelectionConfig(UniversalBaseModel):
    """
    Configuration associated with `SELECTION`-type custom attribute definitions.
    """

    allowed_selections: typing.Optional[
        typing.List[CatalogCustomAttributeDefinitionSelectionConfigCustomAttributeSelection]
    ] = pydantic.Field(default=None)
    """
    The set of valid `CatalogCustomAttributeSelections`. Up to a maximum of 100
    selections can be defined. Can be modified.
    """

    max_allowed_selections: typing.Optional[int] = pydantic.Field(default=None)
    """
    The maximum number of selections that can be set. The maximum value for this
    attribute is 100. The default value is 1. The value can be modified, but changing the value will not
    affect existing custom attribute values on objects. Clients need to
    handle custom attributes with more selected values than allowed by this limit.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

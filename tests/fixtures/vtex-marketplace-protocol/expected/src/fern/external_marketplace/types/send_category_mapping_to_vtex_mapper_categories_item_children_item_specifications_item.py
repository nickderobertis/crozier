

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .send_category_mapping_to_vtex_mapper_categories_item_children_item_specifications_item_attribute_values_item import (
    SendCategoryMappingToVtexMapperCategoriesItemChildrenItemSpecificationsItemAttributeValuesItem,
)


class SendCategoryMappingToVtexMapperCategoriesItemChildrenItemSpecificationsItem(UniversalBaseModel):
    """
    Specifications of children categories.
    """

    attribute_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="attributeName"),
        pydantic.Field(alias="attributeName", description="Name of the attribute sent as a specification."),
    ]
    """
    Name of the attribute sent as a specification.
    """

    attribute_values: typing_extensions.Annotated[
        typing.List[SendCategoryMappingToVtexMapperCategoriesItemChildrenItemSpecificationsItemAttributeValuesItem],
        FieldMetadata(alias="attributeValues"),
        pydantic.Field(alias="attributeValues", description="Values of the atttribute specified."),
    ]
    """
    Values of the atttribute specified.
    """

    required: bool = pydantic.Field()
    """
    If the specification is required, mark this flag as `true`. If not, mark it as `false`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

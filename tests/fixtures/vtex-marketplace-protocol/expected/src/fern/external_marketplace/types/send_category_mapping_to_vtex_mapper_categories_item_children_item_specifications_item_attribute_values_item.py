

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class SendCategoryMappingToVtexMapperCategoriesItemChildrenItemSpecificationsItemAttributeValuesItem(
    UniversalBaseModel
):
    """
    Array of the multiple `valueNames` for the attribute specificied.
    """

    value_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="valueName"), pydantic.Field(alias="valueName", description="Name of the value")
    ]
    """
    Name of the value
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

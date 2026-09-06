

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .update_system_models_attribute_value import UpdateSystemModelsAttributeValue


class UpdateSystemModelsCategory(UniversalBaseModel):
    values: typing_extensions.Annotated[
        typing.Optional[typing.List[UpdateSystemModelsAttributeValue]],
        FieldMetadata(alias="Values"),
        pydantic.Field(alias="Values"),
    ] = None
    category: str = pydantic.Field()
    """
    The category name. Limit 50 characters. Categories with names exceeding this limit will be ignored.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .functions_functions_item_arguments_item import FunctionsFunctionsItemArgumentsItem
from .functions_functions_item_returns_item import FunctionsFunctionsItemReturnsItem


class FunctionsFunctionsItem(UniversalBaseModel):
    name: str
    description: typing.Optional[str] = None
    metadata_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="metadataUrl"), pydantic.Field(alias="metadataUrl")
    ] = None
    arguments: typing.Optional[typing.List[FunctionsFunctionsItemArgumentsItem]] = None
    returns: typing.List[FunctionsFunctionsItemReturnsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

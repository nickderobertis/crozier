

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .resources_functions_item import ResourcesFunctionsItem
from .resources_vi_ms_item import ResourcesViMsItem


class Resources(UniversalBaseModel):
    vi_ms: typing_extensions.Annotated[
        typing.Optional[typing.List[ResourcesViMsItem]],
        FieldMetadata(alias="VIMs"),
        pydantic.Field(alias="VIMs", description="A list of all the available VIMs"),
    ] = None
    """
    A list of all the available VIMs
    """

    functions: typing_extensions.Annotated[
        typing.Optional[typing.List[ResourcesFunctionsItem]],
        FieldMetadata(alias="Functions"),
        pydantic.Field(alias="Functions", description="A list of all the available PDUs"),
    ] = None
    """
    A list of all the available PDUs
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

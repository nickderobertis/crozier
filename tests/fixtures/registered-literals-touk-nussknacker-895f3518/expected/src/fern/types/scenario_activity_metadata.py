

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ScenarioActivityMetadata(UniversalBaseModel):
    type: str
    displayable_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="displayableName"), pydantic.Field(alias="displayableName")
    ]
    icon: str
    supported_actions: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="supportedActions"),
        pydantic.Field(alias="supportedActions"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

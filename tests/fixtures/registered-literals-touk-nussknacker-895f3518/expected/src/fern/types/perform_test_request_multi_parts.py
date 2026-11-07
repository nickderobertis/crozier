

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PerformTestRequestMultiParts(UniversalBaseModel):
    scenario_graph: typing_extensions.Annotated[
        typing.Dict[str, typing.Any], FieldMetadata(alias="scenarioGraph"), pydantic.Field(alias="scenarioGraph")
    ]
    test_data: typing_extensions.Annotated[str, FieldMetadata(alias="testData"), pydantic.Field(alias="testData")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

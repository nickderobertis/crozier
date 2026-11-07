

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PlayerRoundResultScore(UniversalBaseModel):
    tests_run: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="testsRun"),
        pydantic.Field(alias="testsRun", description="Number of tests run"),
    ] = None
    """
    Number of tests run
    """

    tests_passed: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="testsPassed"),
        pydantic.Field(alias="testsPassed", description="Number of tests passed"),
    ] = None
    """
    Number of tests passed
    """

    average_runtime: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="averageRuntime"),
        pydantic.Field(alias="averageRuntime", description="Average runtime in milliseconds"),
    ] = None
    """
    Average runtime in milliseconds
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class TestSolutionResponse(UniversalBaseModel):
    test_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="testId"),
        pydantic.Field(
            alias="testId",
            description="An string to allow clients to associate future incoming test results with which request they respond to.",
        ),
    ] = None
    """
    An string to allow clients to associate future incoming test results with which request they respond to.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

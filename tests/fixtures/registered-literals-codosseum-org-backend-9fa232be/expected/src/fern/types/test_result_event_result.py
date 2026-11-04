

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TestResultEventResult(UniversalBaseModel):
    """
    Test result. input, expectedOutput and actualOutput are only sent if the test failed.
    """

    pass_: typing_extensions.Annotated[
        bool, FieldMetadata(alias="pass"), pydantic.Field(alias="pass", description="Whether the test passed or not")
    ]
    """
    Whether the test passed or not
    """

    input: typing.Optional[str] = pydantic.Field(default=None)
    """
    test input
    """

    expected_output: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="expectedOutput"),
        pydantic.Field(alias="expectedOutput", description="correct output"),
    ] = None
    """
    correct output
    """

    actual_output: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="actualOutput"),
        pydantic.Field(alias="actualOutput", description="output produced by the player's code"),
    ] = None
    """
    output produced by the player's code
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

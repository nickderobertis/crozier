

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CreateModerationResponseResultsItemCategoryScores(UniversalBaseModel):
    """
    A list of the categories along with their scores as predicted by model.
    """

    hate: float = pydantic.Field()
    """
    The score for the category 'hate'.
    """

    hate_threatening: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="hate/threatening"),
        pydantic.Field(alias="hate/threatening", description="The score for the category 'hate/threatening'."),
    ]
    """
    The score for the category 'hate/threatening'.
    """

    harassment: float = pydantic.Field()
    """
    The score for the category 'harassment'.
    """

    harassment_threatening: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="harassment/threatening"),
        pydantic.Field(
            alias="harassment/threatening", description="The score for the category 'harassment/threatening'."
        ),
    ]
    """
    The score for the category 'harassment/threatening'.
    """

    self_harm: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="self-harm"),
        pydantic.Field(alias="self-harm", description="The score for the category 'self-harm'."),
    ]
    """
    The score for the category 'self-harm'.
    """

    self_harm_intent: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="self-harm/intent"),
        pydantic.Field(alias="self-harm/intent", description="The score for the category 'self-harm/intent'."),
    ]
    """
    The score for the category 'self-harm/intent'.
    """

    self_harm_instructions: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="self-harm/instructions"),
        pydantic.Field(
            alias="self-harm/instructions", description="The score for the category 'self-harm/instructions'."
        ),
    ]
    """
    The score for the category 'self-harm/instructions'.
    """

    sexual: float = pydantic.Field()
    """
    The score for the category 'sexual'.
    """

    sexual_minors: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="sexual/minors"),
        pydantic.Field(alias="sexual/minors", description="The score for the category 'sexual/minors'."),
    ]
    """
    The score for the category 'sexual/minors'.
    """

    violence: float = pydantic.Field()
    """
    The score for the category 'violence'.
    """

    violence_graphic: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="violence/graphic"),
        pydantic.Field(alias="violence/graphic", description="The score for the category 'violence/graphic'."),
    ]
    """
    The score for the category 'violence/graphic'.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

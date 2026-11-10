

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CreateModerationResponseResultsItemCategories(UniversalBaseModel):
    """
    A list of the categories, and whether they are flagged or not.
    """

    hate: bool = pydantic.Field()
    """
    Content that expresses, incites, or promotes hate based on race, gender, ethnicity, religion, nationality, sexual orientation, disability status, or caste. Hateful content aimed at non-protected groups (e.g., chess players) is harassment.
    """

    hate_threatening: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="hate/threatening"),
        pydantic.Field(
            alias="hate/threatening",
            description="Hateful content that also includes violence or serious harm towards the targeted group based on race, gender, ethnicity, religion, nationality, sexual orientation, disability status, or caste.",
        ),
    ]
    """
    Hateful content that also includes violence or serious harm towards the targeted group based on race, gender, ethnicity, religion, nationality, sexual orientation, disability status, or caste.
    """

    harassment: bool = pydantic.Field()
    """
    Content that expresses, incites, or promotes harassing language towards any target.
    """

    harassment_threatening: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="harassment/threatening"),
        pydantic.Field(
            alias="harassment/threatening",
            description="Harassment content that also includes violence or serious harm towards any target.",
        ),
    ]
    """
    Harassment content that also includes violence or serious harm towards any target.
    """

    self_harm: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="self-harm"),
        pydantic.Field(
            alias="self-harm",
            description="Content that promotes, encourages, or depicts acts of self-harm, such as suicide, cutting, and eating disorders.",
        ),
    ]
    """
    Content that promotes, encourages, or depicts acts of self-harm, such as suicide, cutting, and eating disorders.
    """

    self_harm_intent: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="self-harm/intent"),
        pydantic.Field(
            alias="self-harm/intent",
            description="Content where the speaker expresses that they are engaging or intend to engage in acts of self-harm, such as suicide, cutting, and eating disorders.",
        ),
    ]
    """
    Content where the speaker expresses that they are engaging or intend to engage in acts of self-harm, such as suicide, cutting, and eating disorders.
    """

    self_harm_instructions: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="self-harm/instructions"),
        pydantic.Field(
            alias="self-harm/instructions",
            description="Content that encourages performing acts of self-harm, such as suicide, cutting, and eating disorders, or that gives instructions or advice on how to commit such acts.",
        ),
    ]
    """
    Content that encourages performing acts of self-harm, such as suicide, cutting, and eating disorders, or that gives instructions or advice on how to commit such acts.
    """

    sexual: bool = pydantic.Field()
    """
    Content meant to arouse sexual excitement, such as the description of sexual activity, or that promotes sexual services (excluding sex education and wellness).
    """

    sexual_minors: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="sexual/minors"),
        pydantic.Field(
            alias="sexual/minors", description="Sexual content that includes an individual who is under 18 years old."
        ),
    ]
    """
    Sexual content that includes an individual who is under 18 years old.
    """

    violence: bool = pydantic.Field()
    """
    Content that depicts death, violence, or physical injury.
    """

    violence_graphic: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="violence/graphic"),
        pydantic.Field(
            alias="violence/graphic",
            description="Content that depicts death, violence, or physical injury in graphic detail.",
        ),
    ]
    """
    Content that depicts death, violence, or physical injury in graphic detail.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

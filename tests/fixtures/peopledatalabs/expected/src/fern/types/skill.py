

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Skill(UniversalBaseModel):
    cleaned_skill: typing.Optional[str] = pydantic.Field(default=None)
    """
    The skill that matches the API input skill after passing it through our internal skill cleaner.
    """

    similar_skills: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of to five of the most contextually-similar skills to the cleaned_skill, determined using our global resume data.
    """

    relevant_job_titles: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="relevant_job_titles:"),
        pydantic.Field(
            alias="relevant_job_titles:",
            description="A list of up to five of the most contextually-similar job titles to the cleaned_skill, determined using our global resume data.",
        ),
    ] = None
    """
    A list of up to five of the most contextually-similar job titles to the cleaned_skill, determined using our global resume data.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

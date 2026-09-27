

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class JobTitle(UniversalBaseModel):
    cleaned_job_title: typing.Optional[str] = pydantic.Field(default=None)
    """
    The job title that matches the API input job_title after passing it through our internal job title cleaner.
    """

    similar_job_titles: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of up to five of the most contextually-similar job titles to the cleaned_job_title, determined using our global resume data.
    """

    relevant_skills: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="relevant_skills:"),
        pydantic.Field(
            alias="relevant_skills:",
            description="A list of up to five of the most contextually-similar skills to the cleaned_job_title, determined using our global resume data.",
        ),
    ] = None
    """
    A list of up to five of the most contextually-similar skills to the cleaned_job_title, determined using our global resume data.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

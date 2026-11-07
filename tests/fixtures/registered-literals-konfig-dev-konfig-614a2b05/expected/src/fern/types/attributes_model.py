

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .attributes_model_draft_item import AttributesModelDraftItem
from .attributes_model_paper_source import AttributesModelPaperSource


class AttributesModel(UniversalBaseModel):
    """
    The data that will be used to populate the workflow's fields. Learn more about the various attributes and their associated types by viewing the [Launch a Workflow](https://developer.ironcladapp.com/docs/launch-a-workflow) guide. Your attributes will differ and include more than this simple example.
    """

    counterparty_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="counterpartyName"), pydantic.Field(alias="counterpartyName")
    ]
    draft: typing.Optional[typing.List[AttributesModelDraftItem]] = pydantic.Field(default=None)
    """
    Provide a URL for a file representing the first uploaded version of a counterparty paper. This field is required when the template source is set to third party paper
    """

    paper_source: typing_extensions.Annotated[
        typing.Optional[AttributesModelPaperSource],
        FieldMetadata(alias="paperSource"),
        pydantic.Field(
            alias="paperSource",
            description="Indicate the type of paper source used on a contract that supports both templatized and third party paper functionality. This field is required when there exists a question for selecting paper source on the template",
        ),
    ] = None
    """
    Indicate the type of paper source used on a contract that supports both templatized and third party paper functionality. This field is required when there exists a question for selecting paper source on the template
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

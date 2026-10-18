

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .snippet_response_output_content import SnippetResponseOutputContent
from .snippet_response_output_owner import SnippetResponseOutputOwner
from .snippet_response_output_project import SnippetResponseOutputProject
from .snippet_response_output_type import SnippetResponseOutputType
from .snippet_response_output_updated_by import SnippetResponseOutputUpdatedBy
from .snippet_response_output_visibility import SnippetResponseOutputVisibility


class SnippetResponseOutput(UniversalBaseModel):
    id: str
    inserted_at: str
    updated_at: str
    type: SnippetResponseOutputType
    visibility: SnippetResponseOutputVisibility
    name: str
    description: typing.Optional[str] = None
    project: SnippetResponseOutputProject
    owner: SnippetResponseOutputOwner
    updated_by: SnippetResponseOutputUpdatedBy
    favorite: bool
    content: SnippetResponseOutputContent

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .change_set_summary import ChangeSetSummary


class ListChangeSetsOutput(UniversalBaseModel):
    """
    The output for the <a>ListChangeSets</a> action.
    """

    summaries: typing_extensions.Annotated[
        typing.Optional[typing.List[ChangeSetSummary]], FieldMetadata(alias="Summaries")
    ] = pydantic.Field(default=None)
    """
    A list of <code>ChangeSetSummary</code> structures that provides the ID and status of each change set for the specified stack.
    """

    next_token: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="NextToken")] = pydantic.Field(
        default=None
    )
    """
    If the output exceeds 1 MB, a string that identifies the next page of change sets. If there is no additional page, this value is <code>null</code>.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

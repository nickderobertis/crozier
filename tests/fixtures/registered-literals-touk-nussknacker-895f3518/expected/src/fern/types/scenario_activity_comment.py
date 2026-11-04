

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .scenario_activity_comment_content import ScenarioActivityCommentContent


class ScenarioActivityComment(UniversalBaseModel):
    content: ScenarioActivityCommentContent
    last_modified_by: typing_extensions.Annotated[
        str, FieldMetadata(alias="lastModifiedBy"), pydantic.Field(alias="lastModifiedBy")
    ]
    last_modified_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="lastModifiedAt"), pydantic.Field(alias="lastModifiedAt")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

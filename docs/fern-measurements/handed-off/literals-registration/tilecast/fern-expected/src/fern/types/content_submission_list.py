

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .content_submission import ContentSubmission
from .content_submission_list_policy import ContentSubmissionListPolicy


class ContentSubmissionList(UniversalBaseModel):
    policy: ContentSubmissionListPolicy
    allow_self_approval: typing_extensions.Annotated[
        bool, FieldMetadata(alias="allowSelfApproval"), pydantic.Field(alias="allowSelfApproval")
    ]
    auto_publish_on_approval: typing_extensions.Annotated[
        bool, FieldMetadata(alias="autoPublishOnApproval"), pydantic.Field(alias="autoPublishOnApproval")
    ]
    items: typing.List[ContentSubmission]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

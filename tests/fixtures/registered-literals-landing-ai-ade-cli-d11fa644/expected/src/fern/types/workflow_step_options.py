

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class WorkflowStepOptions(UniversalBaseModel):
    """
    Unified options for the ``parse-extract`` prebuilt step.

    ``pages`` applies to the parse stage; ``strict`` applies to the extract
    stage. Omit entirely to use each stage's defaults.
    """

    pages: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    1-indexed page numbers to process. ``null`` = all pages. Values < 1 are rejected; numbers > page_count are silently ignored.
    """

    strict: typing.Optional[bool] = pydantic.Field(default=None)
    """
    When ``true``, a schema containing fields the model cannot extract fails with a validation error — HTTP 422 on the sync route, or a failed job on the async ``/jobs`` route. When ``false``, unsupported fields are skipped.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .absolute_path import AbsolutePath
from .revision_no import RevisionNo


class FilesystemOperationRestoreRevision(UniversalBaseModel):
    """
    An operation that restores an older revision as the current revision of the file at a path.
    """

    path: AbsolutePath = pydantic.Field()
    """
    The absolute path, which must resolve to a visible file.
    """

    source_revision_no: RevisionNo = pydantic.Field()
    """
    An existing older revision. The operation copies its content into a new current
    revision.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

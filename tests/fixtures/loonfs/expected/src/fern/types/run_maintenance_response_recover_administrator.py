

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .access_revision_no import AccessRevisionNo
from .change_seq import ChangeSeq
from .commit_id import CommitId
from .namespace_id import NamespaceId


class RunMaintenanceResponseRecoverAdministrator(UniversalBaseModel):
    """
    The committed administrator recovery.
    """

    access_revision_no: AccessRevisionNo = pydantic.Field()
    """
    The root's access revision after the recovery.
    """

    commit_id: CommitId = pydantic.Field()
    """
    The ID of the recovery commit.
    """

    committed_seq: ChangeSeq = pydantic.Field()
    """
    The sequence of the recovery commit.
    """

    namespace_id: NamespaceId = pydantic.Field()
    """
    The namespace whose root grants changed.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .absolute_path import AbsolutePath
from .access_revision_no import AccessRevisionNo
from .attributes_revision_no import AttributesRevisionNo
from .binding_version import BindingVersion
from .change_seq import ChangeSeq
from .display_name import DisplayName
from .inode_id import InodeId
from .revision_no import RevisionNo


class CommitPrecondition_AccessRevision(UniversalBaseModel):
    """
    A condition that a commit must meet before its operations run.

    The server checks each condition against the state before the commit. When several commits are
    applied as one batch, that state's head sequence is the sequence of the last commit admitted
    earlier in the batch, or the batch's starting head sequence if no earlier commit was admitted.
    """

    kind: typing.Literal["access_revision"] = "access_revision"
    expected_access_revision_no: AccessRevisionNo
    inode_id: InodeId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class CommitPrecondition_AttributesRevision(UniversalBaseModel):
    """
    A condition that a commit must meet before its operations run.

    The server checks each condition against the state before the commit. When several commits are
    applied as one batch, that state's head sequence is the sequence of the last commit admitted
    earlier in the batch, or the batch's starting head sequence if no earlier commit was admitted.
    """

    kind: typing.Literal["attributes_revision"] = "attributes_revision"
    expected_attributes_revision_no: AttributesRevisionNo
    inode_id: InodeId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class CommitPrecondition_FileRevision(UniversalBaseModel):
    """
    A condition that a commit must meet before its operations run.

    The server checks each condition against the state before the commit. When several commits are
    applied as one batch, that state's head sequence is the sequence of the last commit admitted
    earlier in the batch, or the batch's starting head sequence if no earlier commit was admitted.
    """

    kind: typing.Literal["file_revision"] = "file_revision"
    expected_revision_no: RevisionNo
    inode_id: InodeId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class CommitPrecondition_InodeBinding(UniversalBaseModel):
    """
    A condition that a commit must meet before its operations run.

    The server checks each condition against the state before the commit. When several commits are
    applied as one batch, that state's head sequence is the sequence of the last commit admitted
    earlier in the batch, or the batch's starting head sequence if no earlier commit was admitted.
    """

    kind: typing.Literal["inode_binding"] = "inode_binding"
    expected_binding_version: BindingVersion
    inode_id: InodeId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class CommitPrecondition_NameAbsence(UniversalBaseModel):
    """
    A condition that a commit must meet before its operations run.

    The server checks each condition against the state before the commit. When several commits are
    applied as one batch, that state's head sequence is the sequence of the last commit admitted
    earlier in the batch, or the batch's starting head sequence if no earlier commit was admitted.
    """

    kind: typing.Literal["name_absence"] = "name_absence"
    display_name: DisplayName
    parent_inode_id: InodeId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class CommitPrecondition_NamespaceHead(UniversalBaseModel):
    """
    A condition that a commit must meet before its operations run.

    The server checks each condition against the state before the commit. When several commits are
    applied as one batch, that state's head sequence is the sequence of the last commit admitted
    earlier in the batch, or the batch's starting head sequence if no earlier commit was admitted.
    """

    kind: typing.Literal["namespace_head"] = "namespace_head"
    expected_head_seq: ChangeSeq

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class CommitPrecondition_PathAbsence(UniversalBaseModel):
    """
    A condition that a commit must meet before its operations run.

    The server checks each condition against the state before the commit. When several commits are
    applied as one batch, that state's head sequence is the sequence of the last commit admitted
    earlier in the batch, or the batch's starting head sequence if no earlier commit was admitted.
    """

    kind: typing.Literal["path_absence"] = "path_absence"
    path: AbsolutePath

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class CommitPrecondition_PathBinding(UniversalBaseModel):
    """
    A condition that a commit must meet before its operations run.

    The server checks each condition against the state before the commit. When several commits are
    applied as one batch, that state's head sequence is the sequence of the last commit admitted
    earlier in the batch, or the batch's starting head sequence if no earlier commit was admitted.
    """

    kind: typing.Literal["path_binding"] = "path_binding"
    expected_binding_version: typing.Optional[BindingVersion] = None
    expected_inode_id: InodeId
    path: AbsolutePath

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


CommitPrecondition = typing_extensions.Annotated[
    typing.Union[
        CommitPrecondition_AccessRevision,
        CommitPrecondition_AttributesRevision,
        CommitPrecondition_FileRevision,
        CommitPrecondition_InodeBinding,
        CommitPrecondition_NameAbsence,
        CommitPrecondition_NamespaceHead,
        CommitPrecondition_PathAbsence,
        CommitPrecondition_PathBinding,
    ],
    pydantic.Field(discriminator="kind"),
]

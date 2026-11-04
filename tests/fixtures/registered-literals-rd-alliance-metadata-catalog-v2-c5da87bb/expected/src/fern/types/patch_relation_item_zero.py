

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .patch_relation_item_zero_op import PatchRelationItemZeroOp
from .patch_relation_item_zero_path import PatchRelationItemZeroPath


class PatchRelationItemZero(UniversalBaseModel):
    op: typing.Optional[PatchRelationItemZeroOp] = pydantic.Field(default=None)
    """
    Operation to perform.
    """

    path: typing.Optional[PatchRelationItemZeroPath] = pydantic.Field(default=None)
    """
    Type of relationship to add.
    """

    value: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    When adding, the MSCIDs to add to the new relationship (acts like replacing if relationship already exists); when replacing, the MSCIDs with which to replace the current array; when testing, the MSCIDs with which to compare the current array; ignored when removing.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

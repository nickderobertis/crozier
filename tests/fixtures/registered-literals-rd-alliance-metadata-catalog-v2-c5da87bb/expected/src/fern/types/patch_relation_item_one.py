

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .patch_relation_item_one_op import PatchRelationItemOneOp


class PatchRelationItemOne(UniversalBaseModel):
    op: typing.Optional[PatchRelationItemOneOp] = pydantic.Field(default=None)
    """
    Operation to perform.
    """

    path: typing.Optional[str] = pydantic.Field(default=None)
    """
    Item on which to perform the operation.
    """

    value: typing.Optional[str] = pydantic.Field(default=None)
    """
    Non-semantic internal identifier for the related record. When adding, the MSCID to insert at that position; when replacing, the MSCID with which to replace the current MSCID at that position; when testing, the MSCID with which to compare the current MSCID at that position; ignored when removing.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

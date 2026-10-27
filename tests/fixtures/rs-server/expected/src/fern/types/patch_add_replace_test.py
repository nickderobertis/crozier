

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .patch_add_replace_test_op import PatchAddReplaceTestOp


class PatchAddReplaceTest(UniversalBaseModel):
    """
    Add, Replace or Test Operation.
    """

    path: str
    op: PatchAddReplaceTestOp
    value: typing.Any

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

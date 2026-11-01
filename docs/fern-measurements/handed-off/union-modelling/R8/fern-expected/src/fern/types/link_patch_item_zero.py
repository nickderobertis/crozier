

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .link_patch_item_zero_op import LinkPatchItemZeroOp
from .link_patch_item_zero_path import LinkPatchItemZeroPath


class LinkPatchItemZero(UniversalBaseModel):
    op: typing.Optional[LinkPatchItemZeroOp] = pydantic.Field(default=None)
    """
    What to do with the whole list.
    """

    path: typing.Optional[LinkPatchItemZeroPath] = pydantic.Field(default=None)
    """
    Which list of links.
    """

    value: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

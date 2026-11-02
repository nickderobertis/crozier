

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .link_patch_item_one_op import LinkPatchItemOneOp


class LinkPatchItemOne(UniversalBaseModel):
    op: typing.Optional[LinkPatchItemOneOp] = pydantic.Field(default=None)
    """
    What to do with one link.
    """

    path: typing.Optional[str] = pydantic.Field(default=None)
    """
    One position in a list of links.
    """

    value: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

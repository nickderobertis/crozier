

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .oligo_create import OligoCreate


class OligoCreateHelm(OligoCreate):
    helm: typing.Optional[str] = pydantic.Field(default=None)
    """
    Representation of the oligo in HELM syntax, including any chemical modifications
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

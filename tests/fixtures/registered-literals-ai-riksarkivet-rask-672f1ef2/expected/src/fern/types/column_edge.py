

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ColumnEdge(UniversalBaseModel):
    """
    A field-to-field derivation edge (data flows ``source`` → ``target``); the transformation kind +
    the ``masking`` governance bit ride the edge.
    """

    description: typing.Optional[str] = None
    kind: typing.Optional[str] = None
    masking: typing.Optional[bool] = None
    source_dataset: str
    source_field: str
    target_dataset: str
    target_field: str
    transformation_subtype: typing.Optional[str] = None
    transformation_type: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .context_id_path_part_dto import ContextIdPathPartDto
from .node_id import NodeId


class ContextIdDto(UniversalBaseModel):
    nid: NodeId
    tid: int
    idx: int
    path: typing.Optional[typing.List[ContextIdPathPartDto]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .column_config import ColumnConfig


class UploadConfig(UniversalBaseModel):
    """
    Describes the format of ids for EXTERNAL and entity-preview Id kinds. Also describes the output format for ids in the result files.
    """

    ids: typing.Optional[typing.List[ColumnConfig]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

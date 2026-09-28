

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .marimo_file_data_kind import MarimoFileDataKind


class MarimoFileData(UniversalBaseModel):
    filetypes: typing.List[str]
    multiple: bool
    kind: MarimoFileDataKind
    label: typing.Optional[str] = None
    max_size: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

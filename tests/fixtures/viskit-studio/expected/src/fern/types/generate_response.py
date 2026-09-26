

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GenerateResponse(UniversalBaseModel):
    abort_reason: typing.Optional[str] = None
    color_lock_summary: typing.Dict[str, int]
    compliance_path: str
    cost_path: str
    db_kit_id: int
    kit_id: str
    needs_review: bool
    png_paths: typing.List[str]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

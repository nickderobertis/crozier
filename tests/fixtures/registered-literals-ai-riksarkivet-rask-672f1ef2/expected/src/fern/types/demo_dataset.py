

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .demo_version import DemoVersion


class DemoDataset(UniversalBaseModel):
    """
    A peek at a real Lance dataset on S3 — what's actually in storage and how it evolved.
    """

    current_version: typing.Optional[int] = None
    error: typing.Optional[str] = None
    exists: bool
    lineage_jsonb: typing.Optional[typing.Dict[str, typing.Any]] = None
    name: str
    row_count: typing.Optional[int] = None
    uri: str
    versions: typing.Optional[typing.List[DemoVersion]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

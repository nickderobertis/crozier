

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .schema_field import SchemaField


class DatasetSchema(UniversalBaseModel):
    """
    The column schema recorded for ``dataset`` at ``version`` (the ``WROTE`` edge's schema). (#24)

    ``version`` is the Lance version this schema belongs to; ``None`` with empty ``fields`` means no
    schema has been persisted for the dataset (or the requested version) yet.
    """

    dataset: str
    fields: typing.Optional[typing.List[SchemaField]] = None
    version: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

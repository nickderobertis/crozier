

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ColumnRef(UniversalBaseModel):
    """
    A column identified by its owning dataset + field name (#24).

    ``dataset`` is REQUIRED and is the governance handle: a column is visible iff the caller can read
    its owning ``table:<dataset>``, so column queries filter on it (never on the field).
    """

    dataset: str
    field: str
    namespace: typing.Optional[str] = None
    type: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

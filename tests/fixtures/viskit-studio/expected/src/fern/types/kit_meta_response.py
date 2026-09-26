

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class KitMetaResponse(UniversalBaseModel):
    """
    Side-car payload for kit detail and the EPIC-9 Catalog drawer.
    """

    compliance: typing.Optional[typing.Dict[str, typing.Any]] = None
    cost: typing.Optional[typing.Dict[str, typing.Any]] = None
    db_kit_id: int
    kit_id: typing.Optional[str] = None
    retrieved_bestseller_ids: typing.List[int]
    spec: typing.Optional[typing.Dict[str, typing.Any]] = None
    spec_markdown: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

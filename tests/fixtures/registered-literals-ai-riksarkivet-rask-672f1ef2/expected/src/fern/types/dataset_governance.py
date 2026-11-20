

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DatasetGovernance(UniversalBaseModel):
    """
    A dataset's human-curated governance metadata (#49): tags + description, with last-writer
    attribution per field family (who/when persisted on the node — the auditable trail for curation).
    """

    description: typing.Optional[str] = None
    description_updated_at: typing.Optional[str] = None
    description_updated_by: typing.Optional[str] = None
    name: str
    tags: typing.Optional[typing.List[str]] = None
    tags_updated_at: typing.Optional[str] = None
    tags_updated_by: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

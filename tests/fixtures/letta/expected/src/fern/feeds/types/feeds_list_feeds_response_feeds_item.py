

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class FeedsListFeedsResponseFeedsItem(UniversalBaseModel):
    id: str
    name: str
    description: typing.Optional[str] = None
    project_id: str
    organization_id: str
    created_at: str
    updated_at: str
    subscriptions_count: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

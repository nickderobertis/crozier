

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AutoApplyAdvisoriesResponse(UniversalBaseModel):
    ok: typing.Optional[bool] = None
    policy_modified: typing.Optional[bool] = None
    removed_classical: typing.Optional[typing.List[str]] = None
    removed_pq: typing.Optional[typing.List[str]] = None
    added_replacements: typing.Optional[typing.List[str]] = None
    advisory_rejected_algs: typing.Optional[typing.List[str]] = None
    warnings: typing.Optional[typing.List[str]] = None
    current_mode: typing.Optional[str] = None
    policy_hash: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

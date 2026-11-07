

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CitizenshipBundleV1(UniversalBaseModel):
    responsible_principal_record: typing.Dict[str, typing.Any]
    agent_passport: typing.Dict[str, typing.Any]
    intent: typing.Dict[str, typing.Any]
    policy_decision: typing.Dict[str, typing.Any]
    audit_entries: typing.List[typing.Dict[str, typing.Any]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

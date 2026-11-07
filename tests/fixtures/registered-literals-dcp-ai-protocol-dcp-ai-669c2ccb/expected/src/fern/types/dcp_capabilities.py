

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dcp_capabilities_supported_algs import DcpCapabilitiesSupportedAlgs


class DcpCapabilities(UniversalBaseModel):
    supported_versions: typing.Optional[typing.List[str]] = None
    supported_algs: typing.Optional[DcpCapabilitiesSupportedAlgs] = None
    supported_wire_formats: typing.Optional[typing.List[str]] = None
    features: typing.Optional[typing.Dict[str, typing.Any]] = None
    verifier_policy_hash: typing.Optional[str] = None
    min_accepted_version: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .bundle_manifest import BundleManifest
from .citizenship_bundle_v2dcp_bundle_version import CitizenshipBundleV2DcpBundleVersion
from .signed_payload import SignedPayload


class CitizenshipBundleV2(UniversalBaseModel):
    dcp_bundle_version: CitizenshipBundleV2DcpBundleVersion
    manifest: BundleManifest
    responsible_principal_record: SignedPayload
    agent_passport: SignedPayload
    intent: SignedPayload
    policy_decision: SignedPayload
    audit_entries: typing.List[typing.Dict[str, typing.Any]]
    pq_checkpoints: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

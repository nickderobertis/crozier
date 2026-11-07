

import typing

from ...types.signed_bundle_v1 import SignedBundleV1
from ...types.signed_bundle_v2 import SignedBundleV2

VerifyBundleRequestSignedBundle = typing.Union[SignedBundleV1, SignedBundleV2]

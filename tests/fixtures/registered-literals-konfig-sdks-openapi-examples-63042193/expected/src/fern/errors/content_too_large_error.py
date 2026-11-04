

import typing

from ..core.api_error import ApiError
from ..types.policy_management_create_policy_bundle_for_context_response import (
    PolicyManagementCreatePolicyBundleForContextResponse,
)


class ContentTooLargeError(ApiError):
    def __init__(
        self,
        body: PolicyManagementCreatePolicyBundleForContextResponse,
        headers: typing.Optional[typing.Dict[str, str]] = None,
    ):
        super().__init__(status_code=413, headers=headers, body=body)

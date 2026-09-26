

import typing

from ...types.pre_registration_fallout_report import PreRegistrationFalloutReport
from ...types.pre_registration_fallout_student import PreRegistrationFalloutStudent

GetPreRegistrationFalloutV3Response = typing.Union[
    typing.Optional[PreRegistrationFalloutReport], typing.List[PreRegistrationFalloutStudent]
]

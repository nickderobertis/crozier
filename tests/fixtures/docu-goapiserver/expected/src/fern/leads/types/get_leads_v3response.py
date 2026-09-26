

import typing

from ...types.lead import Lead
from ...types.lead_projection import LeadProjection
from ...types.lead_stages import LeadStages

GetLeadsV3Response = typing.Union[typing.List[Lead], typing.List[LeadProjection], typing.List[LeadStages]]

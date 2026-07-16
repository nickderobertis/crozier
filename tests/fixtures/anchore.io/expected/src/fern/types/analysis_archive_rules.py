

import typing

from .analysis_archive_transition_rule import AnalysisArchiveTransitionRule

AnalysisArchiveRules = typing.List[AnalysisArchiveTransitionRule]
"""
Rule set for automatic archiving of system objects and flushing of archived objects (permament delete).
"""

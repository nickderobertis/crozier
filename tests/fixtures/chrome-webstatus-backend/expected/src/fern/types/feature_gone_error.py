

from .feature_gone_split import FeatureGoneSplit

FeatureGoneError = FeatureGoneSplit
"""
Represents various reasons a feature might be gone due to evolution.
Clients should check the 'type' field to determine the specific error structure.
"""



NodeNamePrefix = str
"""
Prefix for generated node names: `<cluster name>-<nodeNamePrefix>-<suffix>`.
The controller assigns suffix as a 4-digit decimal number (0000–9999).
Generated names must fit within 63 characters (Kubernetes Node name limit).
Maximum prefix length depends on cluster name length.
"""

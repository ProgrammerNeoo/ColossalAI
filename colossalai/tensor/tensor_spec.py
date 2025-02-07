from typing import Optional
from colossalai.tensor.distspec import _DistSpec, DistPlacementPattern
from .compute_spec import ComputeSpec
from colossalai.tensor import ProcessGroup
from dataclasses import dataclass


@dataclass
class ColoTensorSpec:
    """ ColoTensorSpec
    
    A data class for specifications of the `ColoTensor`.
    It contains attributes of `ProcessGroup`, `_DistSpec`, `ComputeSpec`.
    The latter two attributes are optional. If not set, they are default value is `Replicate()` and `None`.
    """
    pg: ProcessGroup
    dist_attr: Optional[_DistSpec] = _DistSpec(DistPlacementPattern.REPLICATE)
    compute_attr: Optional[ComputeSpec] = None

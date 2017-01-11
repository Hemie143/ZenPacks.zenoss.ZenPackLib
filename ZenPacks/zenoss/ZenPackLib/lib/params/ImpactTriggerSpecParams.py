##############################################################################
#
# Copyright (C) Zenoss, Inc. 2016, all rights reserved.
#
# This content is made available according to terms specified in
# License.zenoss under the directory where your Zenoss product is installed.
#
##############################################################################
from .SpecParams import SpecParams
from ..spec.ImpactTriggerSpec import ImpactTriggerSpec

class ImpactTriggerSpecParams(SpecParams, ImpactTriggerSpec):
    """ImpactTriggerSpecParams"""

    def __init__(self, zenpack_spec, name, **kwargs):
        SpecParams.__init__(self, **kwargs)
        self.name = name


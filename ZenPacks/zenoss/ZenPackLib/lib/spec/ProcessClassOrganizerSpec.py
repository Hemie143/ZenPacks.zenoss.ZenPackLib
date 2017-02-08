##############################################################################
#
# Copyright (C) Zenoss, Inc. 2016, all rights reserved.
#
# This content is made available according to terms specified in
# License.zenoss under the directory where your Zenoss product is installed.
#
##############################################################################

from .Spec import Spec
from .ProcessClassSpec import ProcessClassSpec


class ProcessClassOrganizerSpec(Spec):
    """Initialize a Process Set via Python at install time."""
    def __init__(
            self,
            zenpack_spec,
            path,
            description='',
            remove=False,
            process_classes=None,
            _source_location=None,
            zplog=None):
        """
          :param description: Description of Process Class Organizer
          :type description: str
          :param process_classes: Process Class specs
          :type process_classes: SpecsParameter(ProcessClassSpec)
          :param remove: Remove Organizer on ZenPack removal
          :type remove: boolean
        """
        self.zenpack_spec = zenpack_spec
        self.path = path.lstrip('/')
        self.description = description
        self.remove = remove
        self.process_classes = self.specs_from_param(
            ProcessClassSpec, 'process_classes', process_classes, zplog=self.LOG)

    def create(self, dmd, addToZenPack=True):
        # get/create process class organizer
        porg, bCreated = self.get_or_create_organizer(dmd.Processes, self.path)

        if porg.description != self.description:
            porg.description = self.description
        # Flag this as a ZPL managed object, that is, one that should not be
        # exported to objects.xml  (contained objects will also be excluded)
        porg.zpl_managed = bCreated
        for process_class_id, process_class_spec in self.process_classes.items():
            process_class_spec.create(dmd, porg)

        return self.return_or_add_to_zenpack(porg, self.zenpack_spec.name, addToZenPack)

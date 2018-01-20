""" The Common Context (Label, VitalForce) """

from __future__ import print_function

from data_types import data_type
from data_types import data_field
from data_types import data_field_type


# All body parts have a label
# type Label = string
@data_type
class Label(object):
    label = data_field(validator=data_field_type(str))


# The Animal Electricity needed to create a live part
# type VitalForce = {units:int}
@data_type
class VitalForce(object):
    units = data_field(validator=data_field_type(int))


# get one unit of vital force and return the unit and the remaining
# let getVitalForce vitalForce =
#     let oneUnit = {units = 1}
#     let remaining = {units = vitalForce.units-1}  // decrement
#     oneUnit, remaining  // return both
def getVitalForce(vitalForce):
    oneUnit = VitalForce(1)
    remaining = VitalForce(vitalForce.units - 1)
    return oneUnit, remaining


print("Finished...")

""" Types helper for python """

import attr
import sumtypes

data_type = attr.s
abstract_type = sumtypes.sumtype

data_field = attr.ib
data_field_type = attr.validators.instance_of

data_match = sumtypes.match

""" The Common Context (Label, VitalForce) """

# All body parts have a label
type Label = string

# The Animal Electricity needed to create a live part
type VitalForce = {units:int}

# get one unit of vital force and return the unit and the remaining
let getVitalForce vitalForce = 
    let oneUnit = {units = 1}
    let remaining = {units = vitalForce.units-1}  # decrement
    oneUnit, remaining  # return both


// =================================================================================
// The Left Leg 
// =================================================================================

// Dr Frankenfunctor has a dead left leg lying around in the lab
type DeadLeftLeg = DeadLeftLeg of Label 

// and can make a live left leg from it
type LiveLeftLeg = LiveLeftLeg of Label * VitalForce

// how to make a live thing?  -- First approach
module Approach1 = 

    // version 1 -- the input is a tuple of DeadLeftLeg * VitalForce 
    type MakeLiveLeftLeg = 
        DeadLeftLeg * VitalForce -> LiveLeftLeg * VitalForce 

    let makeLiveLeftLeg (deadLeftLeg,vitalForce) = 
        // get the label from the dead leg using pattern matching
        let (DeadLeftLeg label) = deadLeftLeg
        // get one unit of vital force
        let oneUnit, remainingVitalForce = getVitalForce vitalForce 
        // create a live leg from the label and vital force
        let liveLeftLeg = LiveLeftLeg (label,oneUnit)
        // return the leg and the remaining vital force
        liveLeftLeg, remainingVitalForce    


// version 2 -- the input is a curried version. 
module Approach2 = 

    // First param is DeadLeftLeg, and then VitalForce is a separate param
    type MakeLiveLeftLeg = 
        DeadLeftLeg -> VitalForce -> LiveLeftLeg * VitalForce 

    let makeLiveLeftLeg deadLeftLeg vitalForce = 
        let (DeadLeftLeg label) = deadLeftLeg
        let oneUnit, remainingVitalForce = getVitalForce vitalForce 
        let liveLeftLeg = LiveLeftLeg (label,oneUnit)
        liveLeftLeg, remainingVitalForce    

// version 3 -- the input is a DeadLeftLeg, returning a generator function
module Approach3 = 

    type MakeLiveLeftLeg = 
        DeadLeftLeg -> (VitalForce -> LiveLeftLeg * VitalForce)

    let makeLiveLeftLeg deadLeftLeg = 
        // create an inner intermediate function
        let becomeAlive vitalForce = 
            let (DeadLeftLeg label) = deadLeftLeg
            let oneUnit, remainingVitalForce = getVitalForce vitalForce 
            let liveLeftLeg = LiveLeftLeg (label,oneUnit)
            liveLeftLeg, remainingVitalForce    
        // return it
        becomeAlive 


// Demonstrates how currying works
module CurryingExample = 

    // currying example - two parameters
    let add_v1 x y = 
        x + y

    // currying example - one parameter
    let add_v2 x = 
        fun y -> x + y

    // currying example - intermediate function
    let add_v3 x = 
        let addX y = x + y
        addX // return the function


// =================================================================================
// Creating the Monadster type
// =================================================================================


// version 4 -- make the function generic
module Approach4 = 

    type M<'LiveBodyPart> = 
        VitalForce -> 'LiveBodyPart * VitalForce

    let makeLiveLeftLeg deadLeftLeg :M<LiveLeftLeg> = 
        let becomeAlive vitalForce = 
            let (DeadLeftLeg label) = deadLeftLeg
            let oneUnit, remainingVitalForce = getVitalForce vitalForce 
            let liveLeftLeg = LiveLeftLeg (label,oneUnit)
            liveLeftLeg, remainingVitalForce    
        becomeAlive


// final version -- wrap Monadster body part recipe with "M"
type M<'LiveBodyPart> = 
    M of (VitalForce -> 'LiveBodyPart * VitalForce)

// the creation function looks like this now
let makeLiveLeftLegM deadLeftLeg  = 
    let becomeAlive vitalForce = 
        let (DeadLeftLeg label) = deadLeftLeg
        let oneUnit, remainingVitalForce = getVitalForce vitalForce 
        let liveLeftLeg = LiveLeftLeg (label,oneUnit)
        liveLeftLeg, remainingVitalForce    
    M becomeAlive  // wrap the function in a single case union

// and the function signature is:
// val makeLiveLeftLegM : DeadLeftLeg -> M<LiveLeftLeg>

"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow

#  Note for CIS 322 Fall 2016:
#  You MUST provide the following two functions
#  with these signatures, so that I can write
#  automated tests for grading.  You must keep
#  these signatures even if you don't use all the
#  same arguments.  Arguments are explained in the
#  javadoc comments.
#

#It's Spring 2020 tho
#Table contains distance and time
maxSpeed = [34.0, 32.0, 30.0, 28.0, 26.0]
minSpeed = [15.0, 15.0, 15.0, 11.428, 13.333]
    
def addTime(time, initTime):
    totalMinute = time * 60 + 0.5
    int(totalMinute)
    
    total = arrow.get(initTime).shift(minutes=+totalMinute).isoformat()
    
    return total
    
def calculateTime(km, table):
    x = 0
    total = 0
    
    while(km > 200):
        if(x < 3):
            total += 200 / table[x]
            x += 1
            km -= 200
    total += km / table[x]
    
    return total

def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    #Ex1: 200 < 205
    if(brevet_dist_km < control_dist_km):
        control_dist_km = brevet_dist_km
    
    #Use calculator to calculate the time
    time = calculateTime(control_dist_km, maxSpeed)
    #And add up with start time
    return addTime(time, brevet_start_time)
    


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
          brevet_dist_km: number, the nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    
    #In that web page, it adds 1 for 0km
    #IDK why
    if(control_dist_km == 0):
        return addTime(1, brevet_start_time)
    else:
        #Same as open_time
        time = calculateTime(control_dist_km, minSpeed)
        return addTime(time, brevet_start_time)

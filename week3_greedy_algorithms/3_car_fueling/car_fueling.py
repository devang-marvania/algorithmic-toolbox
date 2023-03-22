from sys import stdin


def min_refills(distance, tank, stops):
    # write your code here

    #create an array by adding start and end stops to actual stops
    updated_stops=[0]+stops+[distance]
 
    #initialize refuels to 0
    refuels = 0

    #full = At what milestone tank is full
    #empty= At what milestone tank is empty
    #Full and Empty value initialized assuming that Journey started with full tank
    (full,empty)=(0,tank)

    for i in range(0,len(updated_stops)-1):

        #See if next stop is farther than tank capacity, if so break the loop and return -1 to signify that Journey won't be possible
        if updated_stops[i+1]-updated_stops[i] > tank:
            refuels=-1
            break

        #Check distance to next stop, if its not within tank capacity then do a refuel and update the full and empty milestones and increment refuel counter
        if updated_stops[i+1]>empty:
            refuels=refuels+1
            full = updated_stops[i]
            empty=updated_stops[i]+tank

        

    return refuels


if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))

#print(min_refills(200,250,[100,150]))  
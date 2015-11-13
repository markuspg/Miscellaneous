#!/usr/bin/env python3

##############################################################################
##
## Copyright 2015 Markus Prasser
##
## This file is part of SALBPConverter.
##
##  SALBPConverter is free software: you can redistribute it and/or modify
##  it under the terms of the GNU General Public License as published by
##  the Free Software Foundation, either version 3 of the License, or
##  (at your option) any later version.
##
##  SALBPConverter is distributed in the hope that it will be useful,
##  but WITHOUT ANY WARRANTY; without even the implied warranty of
##  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##  GNU General Public License for more details.
##
##  You should have received a copy of the GNU General Public License
##  along with SALBPConverter.  If not, see <http://www.gnu.org/licenses/>.
##
##############################################################################

import sys

def main():
    print( "  <---- SALBPConverter ----->  " )
    print( "\nThis program is intended to convert SALBP instance files (*.IN2)"
           "\ninto a single file containing all problems line by line." )

    if len( sys.argv ) < 2:
        print( "Please give at least one argument: the path(s) of the file(s) to convert" )
        return 0
    
    with open( "salbp_problems.salbp", 'wt' ) as outputFile:
        for fileName in sys.argv[ 1 : ]:
            print( "\nReading file " + fileName )
            with open( fileName, 'rt' ) as f:
                # Read the overall quantity of tasks
                print( "  Reading the overall quantity of tasks" )
                taskQuantity = int( f.readline().strip() )
                print( "    Reading SALBP of size '{0}'".format( taskQuantity ) )
                
                # Read the tasks durations
                print( "  Reading the tasks durations" )
                taskDurations = []
                for i in range( taskQuantity ):
                    taskDurations.append( int( f.readline().strip() ) )
                print( "    The tasks durations are '{0}'".format( ';'.join( [ str( duration ) for duration in taskDurations ] ) ) )
                
                # Read the precedence relations
                print( "  Reading the precedence relations" )
                precedenceRelations = [ [] for taskIndex in range( taskQuantity ) ]
                line = f.readline().strip()
                while ',' in line:
                    items = line.split( ',' )
                    precedenceRelations[ int( items[ 1 ] ) - 1 ].append( int( items[ 0 ] ) )
                    line = f.readline().strip()
                    if line == "-1,-1":
                        break
                print( "  The precedence relations are '{0}'".format( ';'.join( [ str( pR ) for pR in precedenceRelations ] ) ) )
                
                lineOut = fileName + "|SALBP|" + str( taskQuantity ) + "|" + ';'.join( [ str( duration ) for duration in taskDurations ] ) + "|" + ';'.join( [ ( str( i + 1 ) + ':' + ','.join( [ str( x ) for x in precedenceRelations[ i ] ] ) ) for i in range( taskQuantity ) ] )
                print( lineOut )
                outputFile.write( lineOut + "\n" )
    
    return 0

if __name__ == "__main__":
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

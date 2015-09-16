#!/usr/bin/env python3

##############################################################################
##
## Copyright 2015 Markus Prasser
##
## This file is part of QAPConverter.
##
##  QAPConverter is free software: you can redistribute it and/or modify
##  it under the terms of the GNU General Public License as published by
##  the Free Software Foundation, either version 3 of the License, or
##  (at your option) any later version.
##
##  QAPConverter is distributed in the hope that it will be useful,
##  but WITHOUT ANY WARRANTY; without even the implied warranty of
##  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##  GNU General Public License for more details.
##
##  You should have received a copy of the GNU General Public License
##  along with QAPConverter.  If not, see <http://www.gnu.org/licenses/>.
##
##############################################################################

import sys

def main():
    print( "  <---- QAPConverter ----->  " )
    print( "\nThis program is intended to convert the problem instances of QAPLIB"
           "\nto a single file containing all problems line by line." )

    if len( sys.argv ) < 2:
        print( "Please give at least one argument: the path(s) of the file(s) to convert" )
        return 0
    
    with open( "qap_problems.qap", 'wt' ) as outputFile:
        for fileName in sys.argv[ 1 : ]:
            print( "\nReading file " + fileName )
            with open( fileName, 'rt' ) as f:
                line = f.readline().rstrip( '\n' )
                problemSize = int( line )
                print( "  Reading problem of size {0}".format( problemSize ) )
                
                print( "Reading the flow matrix" )
                flowMatrix = list()
                ReadMatrix( f, flowMatrix, problemSize )
                assert len( flowMatrix ) == problemSize
                assert sum( [ len( column ) for column in flowMatrix ] ) == problemSize * problemSize
                
                print( "Reading the distance matrix" )
                distanceMatrix = list()
                ReadMatrix( f, distanceMatrix, problemSize )
                assert len( distanceMatrix ) == problemSize
                assert sum( [ len( column ) for column in distanceMatrix ] ) == problemSize * problemSize
                
                line = fileName + "|" + str( problemSize ) + "|" + ';'.join( [ str( num ) for row in flowMatrix for num in row ] ) + "|" + ';'.join( [ str( num ) for row in distanceMatrix for num in row ] )
                outputFile.write( line + "\n" )
    
    return 0

def ReadLine( argFile ):
    line = argFile.readline()
    while not line or line == '\n':
        line = argFile.readline()
    return line

def ReadMatrix( argFile, argList, argProblemSize ):
    # Read all rows (their quantity matches the problem size)
    for i in range( argProblemSize ):
        # Read first line
        argList.append( [ int( digit ) for digit in ReadLine( argFile ).rstrip( '\n' ).split() ] )
        # If the row is not yet full, continue on the following lines
        while len( argList[ -1 ] ) < argProblemSize:
            argList[ -1 ].extend( [ int( digit ) for digit in ReadLine( argFile ).rstrip( '\n' ).split() ] )
        assert len( argList[ -1 ] ) == argProblemSize
    
    
    assert len( argList ) == argProblemSize

if __name__ == "__main__":
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

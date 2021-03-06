import get_points
import point_converter
import write_points

'''
INPUT INFORMATION
'''

inputPath = r"C:\Users\Example\TPP204.LS"
outputPath = r"C:\Users\Example\OutputProg.LS"
oldBooth = 10
newBooth = 11
newProgUtoolNum = 2

'''
END OF INPUT INFORMATION
'''

# get points from input file
pntsDict = get_points.makePntsDict(inputPath)

# modify points from old booth to new booth
pntsDict = point_converter.execute(oldBooth, newBooth, newProgUtoolNum,
                                   pntsDict)

# output file with new points
write_points.writeFile(inputPath, outputPath, pntsDict, newProgUtoolNum,
                       newBooth)

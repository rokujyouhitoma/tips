import pyximport; pyximport.install()
import blesenhamLine

if __name__ == '__main__':
    start = [1,1]
    goal = [10,5]
    result = blesenhamLine.blesenhamLine(start, goal)
    print(result)

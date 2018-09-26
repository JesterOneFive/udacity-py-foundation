import webbrowser
import time

count = 1

print "Program started on " + time.ctime()
while count <= 3:
    
    print "Loop " + str(count)
    # webbrowser.open("https://www.youtube.com/watch?v=1vU7XqToZso")
    time.sleep(3)
    count = count +1

print "Done!"

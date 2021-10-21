import glob                                                                                                            
import mmap                                                                                                            
                                                                                                                       
import sys                                                                                                             
server=sys.argv[1]                                                                                                     
                                                                                                                       
for x in glob.glob("./*.png"):                                                                                         
                                                                                                                       
        with open(x, "r+b") as f:                                                                                      
                    mm = mmap.mmap(f.fileno(), 0)                                                                      
                    t=mm.read(50000)                                                                                   
                    content=t.replace(b"SERVER", server)                                                               
                    mm.close()                                                                                         
        with open("./test/"+x, "wb") as f:                                                                             
                    f.write(content)                                                                                   
                    mm.close()         

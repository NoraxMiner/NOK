input_data = open('input.txt', 'r') 
data= input_data.read() 
#-------------------------------------------------------------------------
data = data.split()
n = int(data[0])
m = int(data[1])
 

def gcd(a, b):
  while b:
    a, b = b, a % b
  return a
def mcd(n,m):
    return (n/gcd(n,m))*m  
pr = (int(mcd(n,m)))
#-------------------------------------------------------------------------
output_data = open('output.txt', 'w') 
output_data.write(str(pr)) 

input_data.close() 
output_data.close()
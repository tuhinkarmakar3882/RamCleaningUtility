from itertools import permutations
import psutil
import sys

def get_all_permutations(source_string):      
     list_of_all_permutations = [''.join(char) for char in permutations(source_string)]
     return list_of_all_permutations


def get_memory_info():
     memory_data = {}
     memory_data['total_memory'], memory_data['available_memory'], memory_data['memory_percentage'], memory_data['used_memory'], memory_data['free_memory'] = psutil.virtual_memory()
     return memory_data

     
if __name__ == '__main__':

     round_number = 1
     temporary_list=[]
     total_bytes_per_GB = 1073741824
     memory_data = get_memory_info()
     constant_string = '1234567890'
     print("[+]Total Memory : {} GB\n".format(float(memory_data['total_memory']) / total_bytes_per_GB))

     while(True):
          try:
               print("-"*45) #Line Seperator
               print("[+] Round Number : {}".format(round_number))
               
               memory_data = get_memory_info()
               print("[+]Current Memory Usage : {} %".format(memory_data['memory_percentage']))
               print("[+] Available Memory : {} GB".format(float(memory_data['available_memory']) / total_bytes_per_GB) )          

               temporary_list.append(get_all_permutations(constant_string)) #Main Memory Hog Line
               
               round_number+=1
               
               print("-"*45)            #Line Seperator
               print()                  #adds an extra New Line
               
          except MemoryError:
               print("[+] Memory Flushed!")
               print("[+] Removing temporary Files...")
               
               del(temporary_list)      #delete the total accumulated chunk of memory
               
               memory_data = get_memory_info()
               print("[+] Current Memory Usage : {} %".format(memory_data['memory_percentage']))
               print("[+] Available Memory : {} GB".format(float(memory_data['available_memory']) / total_bytes_per_GB) )
               
               sys.exit(1)


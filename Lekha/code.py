# --------------
##File path for the file 
file_path 
path = file_path
def read_file(path):
    with open(path, mode='r') as f:
        sentence = f.read()
        f.close()
    return sentence
    

sample_message = read_file(file_path)
print(sample_message)
#Code starts here


# --------------
#Code starts here
file_path_1
file_path_2
path1 = file_path_1
path2 = file_path_2
#Call function read_file() for file_path_1 & file_path_2 
def read_file(path):
    with open(path, mode='r') as f:
        sentence = f.read()
        f.close()
    return sentence
#and store their message sentences in variables message_1 and message_2
message_1 = read_file(path1)
message_2 = read_file(path2)
#Print message_1 and message_2
print(message_1)
print(message_2)

#Write a function fuse_msg()
def fuse_msg(message_a, message_b):
        m1 = int(message_a)
        m2 = int(message_b)
        q = m2//m1
        quotient = str(q)
        return quotient
#cal funct fuse_msg
secret_msg_1 = fuse_msg(message_1, message_2)
print(secret_msg_1)







# --------------
#Code starts here
file_path_3

#readfile
def read_file(path):
    with open(path, mode='r') as f:
        sentence = f.read()
        f.close()
    return sentence

#store message from file
message_3 = read_file(file_path_3)
print(message_3)

#function subsittue_msg()
def substitute_msg(message_c):
    #sub = str("Hi ")
    #print(message_c)
    if message_c == 'Red':
        sub = 'Army General'
    elif message_c == 'Green':
        sub = 'Data Scientist'
    elif message_c == 'Blue':
        pass
    return sub
#call function substitute_msg()
secret_msg_2 = substitute_msg(message_3)
print(secret_msg_2)
#code end


# --------------
# File path for message 4  and message 5
file_path_4
file_path_5

#Code starts here
def read_file(path):
    with open(path, mode='r') as f:
        sentence = f.read()
        f.close()
    return sentence

#store message from the files
message_4 = read_file(file_path_4)
message_5 = read_file(file_path_5)
#print messages
print(message_4)
print(message_5)

#fucnt to compare
def compare_msg(message_d, message_e):
    a_list = []
    b_list = []
    c_list = []
    a_list = message_d.split()
    b_list = message_e.split()
    #print(a_list)
    #print(b_list)
    c_list = [member for member in a_list if member not in b_list]
    #print(c_list)
    final_msg = " ".join(c_list)
    return(final_msg)

secret_msg_3 = str(' ')
secret_msg_3 = compare_msg(message_4, message_5)
print(secret_msg_3)

   
    





# --------------
file_path_6
#Code starts here
#function to read file
def read_file(path):
    with open(path, mode='r') as f:
        sentence = f.read()
        f.close()
    return sentence

message_6 = read_file(file_path_6)
print(message_6)

#function extract
def extract_msg(message_f):
    a_list =[]
    b_list = []
    #sentenc to words in a_list
    a_list = message_f.split()
    print('a', a_list)

    #Lambda function to return true if length of x is even
    even_word = lambda x : (len(x)%2==0)
    #def f(x): return x % 2
    # filter() and sequence as a_list and store result in b_list
    #for i in range(1,20):
    b_list = filter(even_word, a_list)
    #print('b', b_list)
    # a list contains both even and odd numbers.  
    final_msg = str( )
    #for i in b_list:
    final_msg = ' '.join(b_list)
    #print('f', final_msg)
    return final_msg

#secret_msg_4 = str('.')
secret_msg_4 = extract_msg(message_6)    
print(secret_msg_4)
#code ends


# --------------
#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]
print(message_parts)
secret_msg = " ".join(message_parts)
print(secret_msg)
final_path= user_data_dir + '/secret_message.txt'

#Code starts here
def write_file(secret_msg, path):
    with open(path, mode='a+') as f:
        f.write(secret_msg)
        f.close()
    return 

final_path=user_data_dir+'/secret_message.txt'
write_file(secret_msg, final_path)
print(secret_msg)



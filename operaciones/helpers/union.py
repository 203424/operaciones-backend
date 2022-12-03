# import string

class Union():
#   Creating and filling outPutTape with blanks
    def transport_str(self,tape):
        aux = []
        for x in tape:
            aux.append(x)
        return aux

    def turing_machine(self,input_tape):
        blank='blank'
        right='right'
        left='left'
        static='static'
        final_state='q8'
        # alphabeth=list(string.ascii_lowercase)
        inicial_state='q1'
        output_tape=[blank for blank in range(200)]   

        transitions=[
        #( Firts block )  --->  (     Second block       )    
        ['q1',"{",blank,        'q2',blank,'{',right,right],
        ['q2', 'a', 'blank', 'q3', 'blank', 'a', 'right', 'right'],
        ['q2', 'b', 'blank', 'q3', 'blank', 'b', 'right', 'right'],
        ['q2', 'c', 'blank', 'q3', 'blank', 'c', 'right', 'right'],
        ['q2', 'd', 'blank', 'q3', 'blank', 'd', 'right', 'right'],
        ['q2', 'e', 'blank', 'q3', 'blank', 'e', 'right', 'right'],
        ['q2', 'f', 'blank', 'q3', 'blank', 'f', 'right', 'right'],
        ['q2', 'g', 'blank', 'q3', 'blank', 'g', 'right', 'right'],
        ['q2', 'h', 'blank', 'q3', 'blank', 'h', 'right', 'right'],
        ['q2', 'i', 'blank', 'q3', 'blank', 'i', 'right', 'right'],
        ['q2', 'j', 'blank', 'q3', 'blank', 'j', 'right', 'right'],
        ['q2', 'k', 'blank', 'q3', 'blank', 'k', 'right', 'right'],
        ['q2', 'l', 'blank', 'q3', 'blank', 'l', 'right', 'right'],
        ['q2', 'm', 'blank', 'q3', 'blank', 'm', 'right', 'right'],
        ['q2', 'n', 'blank', 'q3', 'blank', 'n', 'right', 'right'],
        ['q2', 'o', 'blank', 'q3', 'blank', 'o', 'right', 'right'],
        ['q2', 'p', 'blank', 'q3', 'blank', 'p', 'right', 'right'],
        ['q2', 'q', 'blank', 'q3', 'blank', 'q', 'right', 'right'],
        ['q2', 'r', 'blank', 'q3', 'blank', 'r', 'right', 'right'],
        ['q2', 's', 'blank', 'q3', 'blank', 's', 'right', 'right'],
        ['q2', 't', 'blank', 'q3', 'blank', 't', 'right', 'right'],
        ['q2', 'u', 'blank', 'q3', 'blank', 'u', 'right', 'right'],
        ['q2', 'v', 'blank', 'q3', 'blank', 'v', 'right', 'right'],
        ['q2', 'w', 'blank', 'q3', 'blank', 'w', 'right', 'right'],
        ['q2', 'x', 'blank', 'q3', 'blank', 'x', 'right', 'right'],
        ['q2', 'y', 'blank', 'q3', 'blank', 'y', 'right', 'right'],
        ['q2', 'z', 'blank', 'q3', 'blank', 'z', 'right', 'right'],
        ['q3',',',blank,  'q2',blank,',',right,right],
        ['q3','}',blank,  'q4',blank,',',right,right],
        ['q2','}',blank,  'q4',blank,',',right,right],
        ['q4','#',blank,  'q5',blank,blank,right,static],
        ['q5','{',blank,  'q6',blank,blank,right,static],
        ['q6', 'a', 'blank', 'q7', 'blank', 'a', 'right', 'right'],
        ['q6', 'b', 'blank', 'q7', 'blank', 'b', 'right', 'right'],
        ['q6', 'c', 'blank', 'q7', 'blank', 'c', 'right', 'right'],
        ['q6', 'd', 'blank', 'q7', 'blank', 'd', 'right', 'right'],
        ['q6', 'e', 'blank', 'q7', 'blank', 'e', 'right', 'right'],
        ['q6', 'f', 'blank', 'q7', 'blank', 'f', 'right', 'right'],
        ['q6', 'g', 'blank', 'q7', 'blank', 'g', 'right', 'right'],
        ['q6', 'h', 'blank', 'q7', 'blank', 'h', 'right', 'right'],
        ['q6', 'i', 'blank', 'q7', 'blank', 'i', 'right', 'right'],
        ['q6', 'j', 'blank', 'q7', 'blank', 'j', 'right', 'right'],
        ['q6', 'k', 'blank', 'q7', 'blank', 'k', 'right', 'right'],
        ['q6', 'l', 'blank', 'q7', 'blank', 'l', 'right', 'right'],
        ['q6', 'm', 'blank', 'q7', 'blank', 'm', 'right', 'right'],
        ['q6', 'n', 'blank', 'q7', 'blank', 'n', 'right', 'right'],
        ['q6', 'o', 'blank', 'q7', 'blank', 'o', 'right', 'right'],
        ['q6', 'p', 'blank', 'q7', 'blank', 'p', 'right', 'right'],
        ['q6', 'q', 'blank', 'q7', 'blank', 'q', 'right', 'right'],
        ['q6', 'r', 'blank', 'q7', 'blank', 'r', 'right', 'right'],
        ['q6', 's', 'blank', 'q7', 'blank', 's', 'right', 'right'],
        ['q6', 't', 'blank', 'q7', 'blank', 't', 'right', 'right'],
        ['q6', 'u', 'blank', 'q7', 'blank', 'u', 'right', 'right'],
        ['q6', 'v', 'blank', 'q7', 'blank', 'v', 'right', 'right'],
        ['q6', 'w', 'blank', 'q7', 'blank', 'w', 'right', 'right'],
        ['q6', 'x', 'blank', 'q7', 'blank', 'x', 'right', 'right'],
        ['q6', 'y', 'blank', 'q7', 'blank', 'y', 'right', 'right'],
        ['q6', 'z', 'blank', 'q7', 'blank', 'z', 'right', 'right'],
        ['q7',',',blank,  'q6',blank,',',right,right],
        ['q6','}',blank,  'q9',blank,blank,right,left],
        ['q9',blank,',',  'q8',blank,'}',static,right],
        ['q7','}',blank,  'q8',blank,'}',right,right],
    ] 

        input_tape= self.transport_str(input_tape)
        state= inicial_state
        head1=0
        head2=0
        input_tape.append(blank)

        for _ in range(len(input_tape)): #Iterating each letter from the input
            band=False
            for single_t in transitions:
                if single_t[0] == state  and single_t[2]==output_tape[head2] and single_t[1]==input_tape[head1]:
                    output_tape[head2]=single_t[5]
                    input_tape[head1]=single_t[4]
                    if single_t[6]==right:
                        head1+=1
                    if single_t[6]==left:
                        head1-=1
                    if single_t[7]==right:
                        head2+=1
                    if single_t[7]==left:
                        head2-=1
                    state=single_t[3]
                    band=True
                    
            if(band==False):
                break
        if state==final_state:
            result=''
            for char in output_tape:
                if char!=blank:
                    result+=char
                if char==blank:
                    break
            return result
        return False
    
# accepted=turingMachine("{a}#{z,x,y,a}") #Write here your input {}#{}
# if accepted:
#     print (f'Turing Machine is done: \n {result}')
# else:
#     print(f'String not Accepted')
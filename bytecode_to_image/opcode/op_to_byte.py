import inst

import os
import io

#[]byte: 문자열을 바이트 배열로 변경
def prepareInput(b, error):
    b.append()
    error.append()
    if len(b) > 1 and b[0] == '0' and b[1] == 'x':
        b = b[2:]
    #--수정
	bytecode = bytearray[len(b)] #해당 길이 만큼의 바이트코드 리스트를 생성, n바이트의 base64 인코딩 데이터에 해당하는 디코딩된 데이터의 최대 길이(바이트)를 반환
    #--
	err = hex.Decode(bytecode, b)
	return bytecode, err

def decode(code): # 결과만 보여주는 부분
    code = bytearray[] # bytecode에 append를 해도 아무 의미가 없음 --수정
    L = len(code)
    for i in range(L): #(for i < L)
        op = code[i]
        inst = inst.InstructionSet[op]
        print("% 4d 0x%08x 0x%02x %-12s", i, i, op, inst.Mnemonic)
        # i 4d 0xi08x 0xop02x inst.Mnemonic-12s
		# if ConsumeCount > 0:
		# 	# consumed = make([]byte, inst.ConsumeCount) #slice임
        #     cosumed = []
		# 	if i+ConsumeCount+1 >= L :
		# 		copy(consumed, code[i+1:]) #슬라이스 복사
        #     else:
		# 		copy(consumed, code[i+1:i+ConsumeCount+1])
		# 	print(" 0x%02x", consumed)
        #     #0xconsumed02x
        # print("\n")
        # i += 1 + ConsumeCount



def main():
	flag.Parse()
	for filename in range(flag.Args()):
        input, err = utils.io.ReadFile(filename)
        if err != "" :
            # print(err)
            continue
        b, err = prepareInput(input)
        if err != "":
            print(err)
            os.Exit(1)
        decode(b)

from web3 import Web3
import os

w3 = Web3(Web3.HTTPProvider('https://alpha-virulent-brook.discover.quiknode.pro/e964325ac8ebdb46775528e73e6c7a0749343ba1/'))

check_connection = w3.is_connected()
# print(check_connection)

latest_block = w3.eth.get_block('latest')
# print(latest_block)

read_file = open('addr_list.txt', encoding='utf-8-sig').readlines()
addr_list = [x.replace('\n', '') for x in read_file]
# print(addr_list)

for addr in addr_list:
    addr = addr.split('/')[-1]
    dir_path = '../bytecode'
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    file_name = os.path.join(dir_path, addr + '.txt')

    contract_addr = addr

    addr = w3.to_checksum_address(contract_addr)
    bytecode = w3.eth.get_code(addr)
    print(bytecode.hex())
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(str(bytecode.hex()))
        f.close()
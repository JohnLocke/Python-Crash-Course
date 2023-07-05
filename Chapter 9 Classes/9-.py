def contract_v1():
    contract_version = '1'
    contract = 'contract_v{}.sol'.format(contract_version)
    print('current contract:contract_',contract)

if __name__ == '__main__':
    contract_version = '1' # 默认合约版本
    contract_v1()
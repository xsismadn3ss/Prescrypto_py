from web3 import Web3

# Conéctate a Infura
infura_url = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
web3 = Web3(Web3.HTTPProvider(infura_url))

# Verifica la conexión
if web3.isConnected():
    print("Conectado a Infura")
else:
    print("Error al conectar a Infura")

# Dirección del contrato desplegado
contract_address = "0xYourContractAddress"

# ABI del contrato (recuerda reemplazarlo con el ABI de tu contrato)
contract_abi = [
    {
        "inputs": [
            {"internalType": "uint256", "name": "_prescriptionFee", "type": "uint256"}
        ],
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "anonymous": False,
        "inputs": [
            {"indexed": False, "internalType": "uint256", "name": "id", "type": "uint256"},
            {"indexed": False, "internalType": "string", "name": "doctorName", "type": "string"},
            {"indexed": False, "internalType": "string", "name": "patientName", "type": "string"},
            {"indexed": False, "internalType": "address", "name": "patientWallet", "type": "address"},
            {"indexed": False, "internalType": "string", "name": "medicationName", "type": "string"},
            {"indexed": False, "internalType": "string", "name": "deliveryDate", "type": "string"}
        ],
        "name": "PrescriptionCreated",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {"indexed": False, "internalType": "uint256", "name": "id", "type": "uint256"},
            {"indexed": False, "internalType": "string", "name": "oldDate", "type": "string"},
            {"indexed": False, "internalType": "string", "name": "newDate", "type": "string"}
        ],
        "name": "DeliveryDateUpdated",
        "type": "event"
    },
    {
        "inputs": [],
        "name": "owner",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "prescriptionFee",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [{"internalType": "uint256", "name": "_id", "type": "uint256"}],
        "name": "getPrescription",
        "outputs": [
            {"internalType": "uint256", "name": "", "type": "uint256"},
            {"internalType": "string", "name": "", "type": "string"},
            {"internalType": "string", "name": "", "type": "string"},
            {"internalType": "address", "name": "", "type": "address"},
            {"internalType": "string", "name": "", "type": "string"},
            {"internalType": "string", "name": "", "type": "string"}
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [{"internalType": "uint256", "name": "_id", "type": "uint256"}],
        "name": "getDeliveryDateHistory",
        "outputs": [{"internalType": "string[]", "name": "", "type": "string[]"}],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "withdraw",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [{"internalType": "uint256", "name": "_newFee", "type": "uint256"}],
        "name": "setPrescriptionFee",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "_id", "type": "uint256"},
            {"internalType": "string", "name": "_doctorName", "type": "string"},
            {"internalType": "string", "name": "_patientName", "type": "string"},
            {"internalType": "address", "name": "_patientWallet", "type": "address"},
            {"internalType": "string", "name": "_medicationName", "type": "string"},
            {"internalType": "string", "name": "_deliveryDate", "type": "string"}
        ],
        "name": "createPrescription",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "_id", "type": "uint256"},
            {"internalType": "string", "name": "_newDate", "type": "string"}
        ],
        "name": "updateDeliveryDate",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    }
]

# Crear una instancia del contrato
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

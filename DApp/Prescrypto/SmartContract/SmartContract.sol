// SPDX-License-Identifier: MIT
pragma solidity >=0.8.2 <0.9.0;

contract MedicalPrescription {
    address public owner;
    uint public prescriptionFee;

    struct Prescription {
        uint id;
        string doctorName;
        string patientName;
        address patientWallet;
        string medicationName;
        string deliveryDate;
    }

    Prescription[] public prescriptions;
    mapping(uint => Prescription) public prescriptionById;
    mapping(uint => string[]) public deliveryDateHistory;

    event PrescriptionCreated(
        uint id,
        string doctorName,
        string patientName,
        address patientWallet,
        string medicationName,
        string deliveryDate
    );

    event DeliveryDateUpdated(
        uint id,
        string oldDate,
        string newDate
    );

    constructor(uint _prescriptionFee) {
        owner = msg.sender;
        prescriptionFee = _prescriptionFee;
    }

    function createPrescription(
        uint _id,
        string memory _doctorName,
        string memory _patientName,
        address _patientWallet,
        string memory _medicationName,
        string memory _deliveryDate
    ) public payable {
        require(msg.value >= prescriptionFee, "Insufficient fee");

        Prescription memory newPrescription = Prescription({
            id: _id,
            doctorName: _doctorName,
            patientName: _patientName,
            patientWallet: _patientWallet,
            medicationName: _medicationName,
            deliveryDate: _deliveryDate
        });

        prescriptions.push(newPrescription);
        prescriptionById[_id] = newPrescription;
        deliveryDateHistory[_id].push(_deliveryDate);

        emit PrescriptionCreated(
            _id,
            _doctorName,
            _patientName,
            _patientWallet,
            _medicationName,
            _deliveryDate
        );
    }

    function updateDeliveryDate(uint _id, string memory _newDate) public {
        require(bytes(prescriptionById[_id].doctorName).length != 0, "Prescription not found");

        string memory oldDate = prescriptionById[_id].deliveryDate;
        prescriptionById[_id].deliveryDate = _newDate;
        deliveryDateHistory[_id].push(_newDate);

        emit DeliveryDateUpdated(_id, oldDate, _newDate);
    }

    function getPrescription(uint _id) public view returns (
        uint,
        string memory,
        string memory,
        address,
        string memory,
        string memory
    ) {
        Prescription memory p = prescriptionById[_id];
        return (
            p.id,
            p.doctorName,
            p.patientName,
            p.patientWallet,
            p.medicationName,
            p.deliveryDate
        );
    }
document.addEventListener("DOMContentLoaded", function () {
    console.log("Patients.js loaded!"); // Ověření, že JS funguje

    // Najdeme prvky
    const addPatientBtn = document.getElementById("add-patient-btn");
    const closeFormBtn = document.getElementById("close-form");
    const patientFormContainer = document.getElementById("patient-form-container");

    if (!addPatientBtn || !closeFormBtn || !patientFormContainer) {
        console.error("Některý z prvků nebyl nalezen!");
        return;
    }

    // Otevření formuláře
    addPatientBtn.addEventListener("click", function () {
        console.log("Kliknuto na Add Patient");
        patientFormContainer.style.display = "grid";
        patientFormContainer.style.opacity = "1";
    });

    // Zavření formuláře
    closeFormBtn.addEventListener("click", function () {
        console.log("Kliknuto na Close Form");
        patientFormContainer.style.opacity = "0";
        setTimeout(() => {
            patientFormContainer.style.display = "none";
        }, 300);
    });

    // Zavření formuláře kliknutím mimo něj
    window.addEventListener("click", function (event) {
        if (event.target === patientFormContainer) {
            console.log("Kliknuto mimo formulář");
            patientFormContainer.style.opacity = "0";
            setTimeout(() => {
                patientFormContainer.style.display = "none";
            }, 300);
        }
    });
});

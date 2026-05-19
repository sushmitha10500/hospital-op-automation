import os
from pathlib import Path

list_of_files = [

    # Main App Files
    "app/__init__.py",
    "app/main.py",
    "app/config.py",
    "app/database.py",

    # Models
    "app/models/__init__.py",
    "app/models/patient.py",
    "app/models/doctor.py",
    "app/models/department.py",
    "app/models/consultation.py",
    "app/models/prescription.py",
    "app/models/followup.py",

    # Services
    "app/services/__init__.py",
    "app/services/patient_generator.py",
    "app/services/slot_engine.py",
    "app/services/doctor_rotation.py",
    "app/services/department_allocator.py",
    "app/services/diagnosis_engine.py",
    "app/services/prescription_engine.py",
    "app/services/followup_engine.py",

    # Routes
    "app/routes/__init__.py",
    "app/routes/patients.py",
    "app/routes/dashboard.py",
    "app/routes/reports.py",

    # Utils
    "app/utils/__init__.py",
    "app/utils/uhid_generator.py",
    "app/utils/opid_generator.py",
    "app/utils/random_data.py",

    # Scheduler
    "app/scheduler/__init__.py",
    "app/scheduler/op_scheduler.py",

    # Root Files
    "requirements.txt",
    "README.md",
    ".gitignore",
    "setup.py"
]

for filepath in list_of_files:

    filepath = Path(filepath)

    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):

        with open(filepath, "w") as f:
            pass

        print(f"Created: {filepath}")

    else:
        print(f"File already exists: {filepath}")
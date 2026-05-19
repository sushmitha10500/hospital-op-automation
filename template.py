import os
from pathlib import Path

list_of_files = [

    # =========================
    # MAIN APPLICATION FILES
    # =========================

    "app/__init__.py",
    "app/main.py",
    "app/config.py",
    "app/database.py",

    # =========================
    # MODELS
    # =========================

    "app/models/__init__.py",
    "app/models/patient.py",
    "app/models/doctor.py",
    "app/models/department.py",
    "app/models/consultation.py",
    "app/models/prescription.py",
    "app/models/followup.py",
    "app/models/README.md",

    # =========================
    # SERVICES
    # =========================

    "app/services/__init__.py",
    "app/services/patient_generator.py",
    "app/services/slot_engine.py",
    "app/services/doctor_rotation.py",
    "app/services/department_allocator.py",
    "app/services/diagnosis_engine.py",
    "app/services/prescription_engine.py",
    "app/services/followup_engine.py",
    "app/services/README.md",

    # =========================
    # PATIENT CATEGORIES
    # =========================

    "app/patient_categories/__init__.py",
    "app/patient_categories/README.md",

    # Age Groups
    "app/patient_categories/age_groups/__init__.py",
    "app/patient_categories/age_groups/README.md",
    "app/patient_categories/age_groups/newborn/__init__.py",
    "app/patient_categories/age_groups/child/__init__.py",
    "app/patient_categories/age_groups/teenager/__init__.py",
    "app/patient_categories/age_groups/adult/__init__.py",
    "app/patient_categories/age_groups/senior_citizen/__init__.py",

    # Gender
    "app/patient_categories/gender/__init__.py",
    "app/patient_categories/gender/README.md",
    "app/patient_categories/gender/male/__init__.py",
    "app/patient_categories/gender/female/__init__.py",
    "app/patient_categories/gender/others/__init__.py",

    # Caste Categories
    "app/patient_categories/caste_categories/__init__.py",
    "app/patient_categories/caste_categories/README.md",
    "app/patient_categories/caste_categories/sc/__init__.py",
    "app/patient_categories/caste_categories/st/__init__.py",
    "app/patient_categories/caste_categories/bc/__init__.py",
    "app/patient_categories/caste_categories/obc/__init__.py",
    "app/patient_categories/caste_categories/oc/__init__.py",
    "app/patient_categories/caste_categories/ews/__init__.py",
    "app/patient_categories/caste_categories/minority/__init__.py",

    # Insurance Schemes
    "app/patient_categories/insurance/__init__.py",
    "app/patient_categories/insurance/README.md",
    "app/patient_categories/insurance/aarogyasri/__init__.py",
    "app/patient_categories/insurance/ayushman_bharat/__init__.py",
    "app/patient_categories/insurance/ehs/__init__.py",
    "app/patient_categories/insurance/private/__init__.py",

    # Economic Status
    "app/patient_categories/economic_status/__init__.py",
    "app/patient_categories/economic_status/README.md",
    "app/patient_categories/economic_status/bpl/__init__.py",
    "app/patient_categories/economic_status/apl/__init__.py",
    "app/patient_categories/economic_status/low_income/__init__.py",

    # =========================
    # DATA
    # =========================

    "app/data/__init__.py",
    "app/data/README.md",
    "app/data/names/__init__.py",
    "app/data/diseases/__init__.py",
    "app/data/medicines/__init__.py",
    "app/data/departments/__init__.py",

    # =========================
    # ROUTES
    # =========================

    "app/routes/__init__.py",
    "app/routes/patients.py",
    "app/routes/dashboard.py",
    "app/routes/reports.py",
    "app/routes/README.md",

    # =========================
    # UTILS
    # =========================

    "app/utils/__init__.py",
    "app/utils/uhid_generator.py",
    "app/utils/opid_generator.py",
    "app/utils/random_data.py",
    "app/utils/age_classifier.py",
    "app/utils/gender_classifier.py",
    "app/utils/README.md",

    # =========================
    # SCHEDULER
    # =========================

    "app/scheduler/__init__.py",
    "app/scheduler/op_scheduler.py",
    "app/scheduler/README.md",

    # =========================
    # EXTRA FOLDERS
    # =========================

    "logs/.gitkeep",
    "logs/README.md",

    "tests/__init__.py",
    "tests/README.md",

    "notebooks/.gitkeep",
    "notebooks/README.md",

    # =========================
    # ROOT FILES
    # =========================

    "requirements.txt",
    "README.md",
    ".gitignore",
    "setup.py",
    ".env"
]

for filepath in list_of_files:

    filepath = Path(filepath)

    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):

        with open(filepath, "w") as f:

            if filename == "README.md":

                folder_name = Path(filepath).parent.name

                f.write(f"# {folder_name.upper()} MODULE\n\n")
                f.write(f"This folder contains files related to {folder_name} functionality.\n\n")
                f.write("## Purpose\n")
                f.write(f"- Manage {folder_name} operations\n")
                f.write(f"- Store {folder_name} related logic\n")
                f.write(f"- Maintain scalable architecture\n\n")
                f.write("## Files\n")
                f.write("- Python modules\n")
                f.write("- Business logic\n")
                f.write("- Utility/helper functions\n")

        print(f"Created: {filepath}")

    else:
        print(f"File already exists: {filepath}")
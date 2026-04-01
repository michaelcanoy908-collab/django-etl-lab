import csv
from .models import RawStudent, CleanStudent

def run_etl(filepath="students.csv"):
    # --- EXTRACT ---
    RawStudent.objects.all().delete()
    
    with open(filepath, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        raw_rows = []
        for row in reader:
            raw_rows.append(RawStudent(
                student_id=row.get("id", "").strip(),
                name=row.get("name", "").strip(),
                course=row.get("course", "").strip(),
            ))
        RawStudent.objects.bulk_create(raw_rows)
    
    # --- TRANSFORM ---
    cleaned = []
    for r in RawStudent.objects.all():
        name = r.name if r.name else "Unknown"
        course = r.course if r.course else "Undeclared"
        cleaned.append(CleanStudent(
            student_id=r.student_id,
            name=name,
            course=course,
        ))
    
    # --- LOAD ---
    CleanStudent.objects.all().delete()
    CleanStudent.objects.bulk_create(cleaned)
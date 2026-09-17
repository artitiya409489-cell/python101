"""
===============================================================================
  PROJECT    : ระบบคลินิกสัตว์เลี้ยง (Pet Clinic Management System)
  STRUCTURE  : CLI + Binary File I/O (struct)
  ENTITIES   : เจ้าของ (Owner) / สัตว์เลี้ยง (Pet) / ประวัติรักษา (Visit)
===============================================================================

📌 แนวคิดโครงสร้างไฟล์นี้:
   ต่างจาก template ตัวอย่างที่จัดกลุ่มตาม "การกระทำ" (view/add/update/delete
   ใช้ร่วมกันทุก entity) ไฟล์นี้จัดกลุ่มตาม "เอนทิตี" แทน — แต่ละเอนทิตีมีชุด
   ฟังก์ชันของตัวเอง (CRUD) อยู่ในโซนเดียวกัน อ่านและแก้ง่ายกว่าเวลาโฟกัส
   ทำงานกับข้อมูลชนิดใดชนิดหนึ่ง

   ลำดับการอ่านไฟล์แนะนำ:
   1) ค่าคงที่ + Struct Format
   2) ฟังก์ชันช่วยเหลือ (Helpers)
   3) โซน OWNER
   4) โซน PET
   5) โซน VISIT
   6) โซน REPORT
   7) เมนูหลัก (Main Menu)
"""

import struct
import os
import datetime

# ═══════════════════════════════════════════════════════════════════════════
# 1) ค่าคงที่ + Struct Format
# ═══════════════════════════════════════════════════════════════════════════

OWNER_FILE = "owners.dat"
PET_FILE = "pets.dat"
VISIT_FILE = "visits.dat"
REPORT_FILE = "report.txt"

STATUS_DELETED = 0
STATUS_ACTIVE = 1

# เจ้าของ: owner_id(Q) | name(50s) | phone(15s) | address(100s) | status(I)
OWNER_FORMAT = "<Q 50s 15s 100s I"

# สัตว์เลี้ยง: pet_id(I) | owner_id(Q)[FK] | name(30s) | species(20s)
#             | breed(30s) | birth_date(10s) | status(I)
PET_FORMAT = "<I Q 30s 20s 30s 10s I"

# ประวัติรักษา: visit_id(I) | pet_id(I)[FK] | visit_date(10s)
#              | symptom(100s) | diagnosis(100s) | fee(f) | status(I)
VISIT_FORMAT = "<I I 10s 100s 100s f I"

OWNER_SIZE = struct.calcsize(OWNER_FORMAT)
PET_SIZE = struct.calcsize(PET_FORMAT)
VISIT_SIZE = struct.calcsize(VISIT_FORMAT)


def show_banner():
    print("╔═══════════════════════════════════════════════════════════╗")
    print("║   🐾  ระบบคลินิกสัตว์เลี้ยง (Pet Clinic System)  🐾        ║")
    print("╚═══════════════════════════════════════════════════════════╝")


# ═══════════════════════════════════════════════════════════════════════════
# 2) ฟังก์ชันช่วยเหลือ (Helpers) — ใช้ร่วมกันทุกเอนทิตี
# ═══════════════════════════════════════════════════════════════════════════

def encode_fixed(s: str, size: int) -> bytes:
    """แปลงสตริง -> bytes ขนาดคงที่ (ตัด/เติม null-byte)"""
    # TODO: เขียน logic .encode("utf-8") แล้ว ljust ด้วย b'\x00' ให้ครบ size
    pass


def decode_fixed(b: bytes) -> str:
    """แปลง bytes -> สตริง (ตัด null-byte ทิ้ง)"""
    # TODO: เขียน logic b.split(b'\x00')[0].decode("utf-8")
    pass


def get_next_id(filename: str, record_format: str, record_size: int, id_index: int = 0) -> int:
    """หา ID ถัดไปโดยดูจาก record สุดท้ายในไฟล์ (ใช้ได้ทั้ง 3 เอนทิตี)"""
    # TODO: ถ้าไฟล์ไม่มี/ว่าง return 1, ไม่งั้นอ่าน record สุดท้ายแล้ว +1
    pass


def file_exists_or_create(filename: str):
    """สร้างไฟล์เปล่าถ้ายังไม่มี กัน error ตอนเปิดโหมด 'rb'/'r+b'"""
    if not os.path.exists(filename):
        open(filename, "wb").close()


# ═══════════════════════════════════════════════════════════════════════════
# 3) โซน OWNER (เจ้าของสัตว์เลี้ยง)
# ═══════════════════════════════════════════════════════════════════════════

def owner_add():
    """เพิ่มเจ้าของใหม่"""
    print("\n--- ➕ เพิ่มเจ้าของสัตว์เลี้ยง ---")
    # TODO: รับ name/phone/address -> encode_fixed -> struct.pack -> append ลง OWNER_FILE
    pass


def owner_view_all():
    """แสดงรายชื่อเจ้าของทั้งหมด (status == ACTIVE)"""
    print("\n--- 👤 รายชื่อเจ้าของทั้งหมด ---")
    # TODO: อ่าน OWNER_FILE ทีละ OWNER_SIZE -> unpack -> decode -> แสดงผล
    pass


def owner_update():
    """แก้ไขข้อมูลเจ้าของ (seek + เขียนทับ)"""
    print("\n--- ✏️ แก้ไขข้อมูลเจ้าของ ---")
    # TODO: ค้นหาด้วย owner_id -> seek(offset) -> เขียน record ใหม่ทับ
    pass


def owner_delete():
    """ลบเจ้าของแบบ Soft Delete (status -> DELETED)"""
    print("\n--- 🗑️ ลบเจ้าของ ---")
    # TODO: ค้นหาด้วย owner_id -> เปลี่ยน status เป็น 0 -> เขียนทับ
    pass


def owner_menu():
    while True:
        print("\n┌─ 👤 เมนูจัดการเจ้าของ ──────────────┐")
        print("│ 1) ดูรายชื่อทั้งหมด                 │")
        print("│ 2) เพิ่มเจ้าของใหม่                 │")
        print("│ 3) แก้ไขข้อมูล                      │")
        print("│ 4) ลบข้อมูล                         │")
        print("│ 0) ย้อนกลับ                         │")
        print("└──────────────────────────────────────┘")
        choice = input("เลือกเมนู (0-4): ").strip()
        actions = {"1": owner_view_all, "2": owner_add, "3": owner_update, "4": owner_delete}
        if choice == "0":
            break
        elif choice in actions:
            actions[choice]()
        else:
            print("❌ เลือกเมนูไม่ถูกต้อง")


# ═══════════════════════════════════════════════════════════════════════════
# 4) โซน PET (สัตว์เลี้ยง)
# ═══════════════════════════════════════════════════════════════════════════

def pet_add():
    """เพิ่มสัตว์เลี้ยงใหม่ (ต้องผูกกับ owner_id ที่มีอยู่จริง)"""
    print("\n--- ➕ เพิ่มสัตว์เลี้ยงใหม่ ---")
    # TODO: รับ owner_id (ควรเช็คว่ามีอยู่จริงใน OWNER_FILE) + name/species/breed/birth_date
    pass


def pet_view_all():
    """แสดงสัตว์เลี้ยงทั้งหมด พร้อมชื่อเจ้าของ (join กับ OWNER_FILE)"""
    print("\n--- 🐕 รายชื่อสัตว์เลี้ยงทั้งหมด ---")
    # TODO: อ่าน PET_FILE -> สำหรับแต่ละ record ใช้ owner_id ไปค้นชื่อใน OWNER_FILE
    pass


def pet_update():
    print("\n--- ✏️ แก้ไขข้อมูลสัตว์เลี้ยง ---")
    # TODO: ค้นหาด้วย pet_id -> seek -> เขียนทับ
    pass


def pet_delete():
    print("\n--- 🗑️ ลบสัตว์เลี้ยง ---")
    # TODO: soft delete ด้วย pet_id
    pass


def pet_menu():
    while True:
        print("\n┌─ 🐕 เมนูจัดการสัตว์เลี้ยง ───────────┐")
        print("│ 1) ดูรายชื่อทั้งหมด                 │")
        print("│ 2) เพิ่มสัตว์เลี้ยงใหม่              │")
        print("│ 3) แก้ไขข้อมูล                      │")
        print("│ 4) ลบข้อมูล                         │")
        print("│ 0) ย้อนกลับ                         │")
        print("└──────────────────────────────────────┘")
        choice = input("เลือกเมนู (0-4): ").strip()
        actions = {"1": pet_view_all, "2": pet_add, "3": pet_update, "4": pet_delete}
        if choice == "0":
            break
        elif choice in actions:
            actions[choice]()
        else:
            print("❌ เลือกเมนูไม่ถูกต้อง")


# ═══════════════════════════════════════════════════════════════════════════
# 5) โซน VISIT (ประวัติการรักษา/นัดหมาย)
# ═══════════════════════════════════════════════════════════════════════════

def visit_add():
    """บันทึกการเข้ารักษาใหม่ (ต้องผูกกับ pet_id ที่มีอยู่จริง)"""
    print("\n--- ➕ บันทึกการรักษาใหม่ ---")
    # TODO: รับ pet_id + วันที่ + อาการ + วินิจฉัย + ค่ารักษา
    pass


def visit_view_all():
    """แสดงประวัติการรักษาทั้งหมด พร้อมชื่อสัตว์เลี้ยง (join กับ PET_FILE)"""
    print("\n--- 📝 ประวัติการรักษาทั้งหมด ---")
    # TODO: อ่าน VISIT_FILE -> join กับ PET_FILE เพื่อแสดงชื่อสัตว์
    pass


def visit_update():
    print("\n--- ✏️ แก้ไขประวัติการรักษา ---")
    # TODO: ค้นหาด้วย visit_id -> seek -> เขียนทับ
    pass


def visit_delete():
    print("\n--- 🗑️ ลบประวัติการรักษา ---")
    # TODO: soft delete ด้วย visit_id
    pass


def visit_menu():
    while True:
        print("\n┌─ 📝 เมนูจัดการประวัติการรักษา ───────┐")
        print("│ 1) ดูประวัติทั้งหมด                 │")
        print("│ 2) บันทึกการรักษาใหม่               │")
        print("│ 3) แก้ไขข้อมูล                      │")
        print("│ 4) ลบข้อมูล                         │")
        print("│ 0) ย้อนกลับ                         │")
        print("└──────────────────────────────────────┘")
        choice = input("เลือกเมนู (0-4): ").strip()
        actions = {"1": visit_view_all, "2": visit_add, "3": visit_update, "4": visit_delete}
        if choice == "0":
            break
        elif choice in actions:
            actions[choice]()
        else:
            print("❌ เลือกเมนูไม่ถูกต้อง")


# ═══════════════════════════════════════════════════════════════════════════
# 6) โซน REPORT (รายงานสรุป)
# ═══════════════════════════════════════════════════════════════════════════

def generate_report():
    """สร้างไฟล์ report.txt สรุปข้อมูลทั้งคลินิก"""
    print("\n--- 📄 สร้างรายงานสรุป ---")
    # TODO:
    # 1. อ่าน OWNER_FILE, PET_FILE, VISIT_FILE ทั้งหมด (เฉพาะ status == ACTIVE)
    # 2. join owner_id -> ชื่อเจ้าของ, pet_id -> ชื่อสัตว์เลี้ยง
    # 3. จัด format ตารางสวยงาม + สรุปยอด (จำนวนราย, รายได้รวม)
    # 4. เขียนลง REPORT_FILE โหมด 'w' encoding utf-8
    pass


# ═══════════════════════════════════════════════════════════════════════════
# 7) เมนูหลัก (Main Menu)
# ═══════════════════════════════════════════════════════════════════════════

def main_menu():
    for f, fmt, sz in [(OWNER_FILE, OWNER_FORMAT, OWNER_SIZE),
                        (PET_FILE, PET_FORMAT, PET_SIZE),
                        (VISIT_FILE, VISIT_FORMAT, VISIT_SIZE)]:
        file_exists_or_create(f)

    while True:
        show_banner()
        print("1) จัดการเจ้าของสัตว์เลี้ยง (Owner)")
        print("2) จัดการสัตว์เลี้ยง (Pet)")
        print("3) จัดการประวัติการรักษา (Visit)")
        print("4) สร้างรายงานสรุป (Report)")
        print("0) ออกจากโปรแกรม (Exit)")
        choice = input("เลือกเมนู (0-4): ").strip()

        if choice == "1":
            owner_menu()
        elif choice == "2":
            pet_menu()
        elif choice == "3":
            visit_menu()
        elif choice == "4":
            generate_report()
        elif choice == "0":
            print("\n👋 ขอบคุณที่ใช้งานระบบคลินิกสัตว์เลี้ยง\n")
            break
        else:
            print("❌ เลือกเมนูไม่ถูกต้อง ลองใหม่อีกครั้ง\n")


if __name__ == "__main__":
    main_menu()
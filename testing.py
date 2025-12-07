from sqlalchemy import create_engine

# اطلاعات اتصال به پایگاه داده (مطابق با تنظیمات شما)
DATABASE_URL = "postgresql://mehr:mehrx@localhost:5432/mydb"

# ساخت یک شیء engine برای اتصال به پایگاه داده
engine = create_engine(DATABASE_URL)

# آزمایش اتصال
try:
    with engine.connect() as connection:
        print("اتصال به پایگاه داده موفقیت‌آمیز بود!")
except Exception as e:
    print(f"اتصال به پایگاه داده با خطا مواجه شد: {e}")

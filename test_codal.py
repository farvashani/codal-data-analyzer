#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
تست ساده برای کلاس تحلیلگر کدال
Simple test for Codal Data Analyzer
"""

from codal_data_analyzer import CodalDataAnalyzer
import sys

def test_analyzer():
    """تست عملکرد تحلیلگر"""
    print("🧪 شروع تست تحلیلگر کدال")
    print("=" * 40)
    
    try:
        # ایجاد نمونه تحلیلگر
        analyzer = CodalDataAnalyzer()
        print("✅ تحلیلگر ایجاد شد")
        
        # تست دریافت لیست شرکت‌ها
        print("\n📊 تست دریافت لیست شرکت‌ها...")
        companies = analyzer.get_company_list()
        
        if companies is not None:
            print(f"✅ لیست شرکت‌ها دریافت شد: {len(companies)} شرکت")
        else:
            print("⚠️ لیست شرکت‌ها دریافت نشد (احتمالاً محدودیت API)")
        
        # تست دریافت گزارش‌های نمونه
        print("\n📈 تست دریافت گزارش‌های نمونه...")
        sample_reports = analyzer.get_company_reports("فولاد", days_back=7)
        
        if sample_reports is not None:
            print(f"✅ گزارش‌های نمونه دریافت شد: {len(sample_reports)} گزارش")
            
            # تست تمیزسازی
            print("\n🧹 تست تمیزسازی داده‌ها...")
            clean_data = analyzer.clean_financial_data(sample_reports)
            
            if clean_data is not None:
                print(f"✅ داده‌ها تمیز شدند: {len(clean_data)} سطر")
                
                # تست استخراج فیچر
                print("\n🔧 تست استخراج فیچرها...")
                features = analyzer.extract_financial_features(clean_data)
                
                if features is not None:
                    print(f"✅ فیچرها استخراج شدند: {len(features.columns)} فیچر")
                else:
                    print("⚠️ فیچری استخراج نشد")
            else:
                print("⚠️ داده‌ها تمیز نشدند")
        else:
            print("⚠️ گزارش نمونه دریافت نشد")
        
        print("\n🎉 تست کامل شد!")
        return True
        
    except Exception as e:
        print(f"❌ خطا در تست: {str(e)}")
        return False

if __name__ == "__main__":
    success = test_analyzer()
    sys.exit(0 if success else 1)

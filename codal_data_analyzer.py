#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
تحلیلگر داده‌های کدال ایران
Codal Data Analyzer for Iranian Stock Market

این اسکریپت برای جمع‌آوری، تمیزسازی و تحلیل داده‌های مالی از سامانه کدال ایران طراحی شده است.
"""

import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import time
import json
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

class CodalDataAnalyzer:
    """کلاس اصلی برای تحلیل داده‌های کدال"""
    
    def __init__(self):
        self.base_url = "https://codal.ir"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        self.data = {}
        
    def get_company_list(self):
        """دریافت لیست شرکت‌های پذیرفته شده در بورس"""
        print("📊 در حال دریافت لیست شرکت‌ها...")
        
        # ایجاد داده‌های نمونه برای تست
        sample_companies = [
            {"symbol": "فولاد", "name": "فولاد مبارکه اصفهان", "sector": "فلزات اساسی"},
            {"symbol": "پتروشیمی", "name": "پتروشیمی پارس", "sector": "پتروشیمی"},
            {"symbol": "بانک", "name": "بانک ملی ایران", "sector": "بانک‌ها"},
            {"symbol": "خودرو", "name": "ایران خودرو", "sector": "خودرو"},
            {"symbol": "سیمان", "name": "سیمان تهران", "sector": "سیمان"}
        ]
        
        try:
            # تلاش برای اتصال واقعی
            url = f"{self.base_url}/api/v1/companies"
            response = self.session.get(url, timeout=10)
            
            if response.status_code == 200:
                companies = response.json()
                print(f"✅ {len(companies)} شرکت یافت شد")
                return pd.DataFrame(companies)
            else:
                print(f"⚠️ API در دسترس نیست، از داده‌های نمونه استفاده می‌کنیم")
                return pd.DataFrame(sample_companies)
                
        except Exception as e:
            print(f"⚠️ اتصال به کدال امکان‌پذیر نیست: {str(e)}")
            print("📊 استفاده از داده‌های نمونه برای تست...")
            return pd.DataFrame(sample_companies)
    
    def get_company_reports(self, company_symbol, days_back=30):
        """دریافت گزارش‌های مالی یک شرکت"""
        print(f"📈 در حال دریافت گزارش‌های {company_symbol}...")
        
        # ایجاد داده‌های نمونه برای تست
        import random
        from datetime import datetime, timedelta
        
        sample_reports = []
        for i in range(5):
            date = datetime.now() - timedelta(days=i*7)
            sample_reports.append({
                "symbol": company_symbol,
                "date": date.strftime("%Y-%m-%d"),
                "revenue": random.randint(1000000, 10000000),
                "net_profit": random.randint(100000, 1000000),
                "price": random.randint(1000, 10000),
                "volume": random.randint(100000, 1000000),
                "report_type": "میان‌دوره" if i % 2 == 0 else "سالانه"
            })
        
        try:
            # تلاش برای اتصال واقعی
            url = f"{self.base_url}/api/v1/companies/{company_symbol}/reports"
            params = {
                'days_back': days_back,
                'page_size': 100
            }
            
            response = self.session.get(url, params=params, timeout=10)
            
            if response.status_code == 200:
                reports = response.json()
                print(f"✅ {len(reports)} گزارش یافت شد")
                return pd.DataFrame(reports)
            else:
                print(f"⚠️ API در دسترس نیست، از داده‌های نمونه استفاده می‌کنیم")
                return pd.DataFrame(sample_reports)
                
        except Exception as e:
            print(f"⚠️ اتصال به کدال امکان‌پذیر نیست: {str(e)}")
            print("📊 استفاده از داده‌های نمونه برای تست...")
            return pd.DataFrame(sample_reports)
    
    def clean_financial_data(self, df):
        """تمیزسازی داده‌های مالی"""
        if df is None or df.empty:
            return None
            
        print("🧹 در حال تمیزسازی داده‌ها...")
        
        # حذف سطرهای تکراری
        df = df.drop_duplicates()
        
        # تبدیل ستون‌های تاریخ
        date_columns = ['date', 'publish_date', 'fiscal_date']
        for col in date_columns:
            if col in df.columns:
                df[col] = pd.to_datetime(df[col], errors='coerce')
        
        # تمیزسازی ستون‌های عددی
        numeric_columns = df.select_dtypes(include=[np.number]).columns
        for col in numeric_columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        
        # حذف سطرهایی که اطلاعات کلیدی ندارند
        df = df.dropna(subset=['symbol'] if 'symbol' in df.columns else [])
        
        print(f"✅ داده‌ها تمیز شدند. {len(df)} سطر باقی ماند")
        return df
    
    def extract_financial_features(self, df):
        """استخراج فیچرهای مالی مهم"""
        if df is None or df.empty:
            return None
            
        print("🔧 در حال استخراج فیچرها...")
        
        features = pd.DataFrame()
        
        # اگر داده‌های مالی داریم
        if 'revenue' in df.columns and 'net_profit' in df.columns:
            # نسبت سودآوری
            features['profit_margin'] = df['net_profit'] / df['revenue']
            
            # رشد درآمد
            if len(df) > 1:
                features['revenue_growth'] = df['revenue'].pct_change()
                
        # اگر داده‌های قیمت داریم
        if 'price' in df.columns:
            # میانگین متحرک
            features['price_ma_5'] = df['price'].rolling(window=5).mean()
            features['price_ma_20'] = df['price'].rolling(window=20).mean()
            
            # نوسان قیمت
            features['price_volatility'] = df['price'].rolling(window=10).std()
        
        # فیچرهای زمانی
        if 'date' in df.columns:
            features['year'] = df['date'].dt.year
            features['month'] = df['date'].dt.month
            features['quarter'] = df['date'].dt.quarter
        
        print(f"✅ {len(features.columns)} فیچر استخراج شد")
        return features
    
    def analyze_market_trends(self, df):
        """تحلیل روندهای بازار"""
        if df is None or df.empty:
            return None
            
        print("📊 در حال تحلیل روندهای بازار...")
        
        analysis = {}
        
        # تحلیل بر اساس نماد
        if 'symbol' in df.columns:
            symbol_analysis = df.groupby('symbol').agg({
                'price': ['mean', 'std', 'min', 'max'] if 'price' in df.columns else [],
                'volume': ['sum', 'mean'] if 'volume' in df.columns else []
            }).round(2)
            analysis['by_symbol'] = symbol_analysis
        
        # تحلیل بر اساس زمان
        if 'date' in df.columns:
            df['year_month'] = df['date'].dt.to_period('M')
            time_analysis = df.groupby('year_month').size()
            analysis['trend_over_time'] = time_analysis
        
        return analysis
    
    def save_results(self, data, filename):
        """ذخیره نتایج"""
        try:
            if isinstance(data, pd.DataFrame):
                data.to_csv(f"{filename}.csv", index=False, encoding='utf-8')
            elif isinstance(data, dict):
                with open(f"{filename}.json", 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2, default=str)
            
            print(f"💾 نتایج در فایل {filename} ذخیره شد")
            
        except Exception as e:
            print(f"❌ خطا در ذخیره فایل: {str(e)}")

def main():
    """تابع اصلی"""
    print("🚀 شروع تحلیل داده‌های کدال ایران")
    print("=" * 50)
    
    # ایجاد نمونه تحلیلگر
    analyzer = CodalDataAnalyzer()
    
    # دریافت لیست شرکت‌ها
    companies = analyzer.get_company_list()
    if companies is not None:
        analyzer.save_results(companies, "companies_list")
        
        # تحلیل چند شرکت نمونه
        sample_companies = companies.head(5)['symbol'].tolist() if 'symbol' in companies.columns else []
        
        all_reports = []
        for symbol in sample_companies:
            reports = analyzer.get_company_reports(symbol)
            if reports is not None:
                all_reports.append(reports)
                time.sleep(1)  # تاخیر برای جلوگیری از محدودیت API
        
        if all_reports:
            # ترکیب همه گزارش‌ها
            combined_reports = pd.concat(all_reports, ignore_index=True)
            
            # تمیزسازی داده‌ها
            clean_data = analyzer.clean_financial_data(combined_reports)
            
            # استخراج فیچرها
            features = analyzer.extract_financial_features(clean_data)
            
            # تحلیل روندها
            trends = analyzer.analyze_market_trends(clean_data)
            
            # ذخیره نتایج
            analyzer.save_results(clean_data, "cleaned_financial_data")
            if features is not None:
                analyzer.save_results(features, "financial_features")
            if trends:
                analyzer.save_results(trends, "market_trends")
    
    print("✅ تحلیل کامل شد!")

if __name__ == "__main__":
    main()
